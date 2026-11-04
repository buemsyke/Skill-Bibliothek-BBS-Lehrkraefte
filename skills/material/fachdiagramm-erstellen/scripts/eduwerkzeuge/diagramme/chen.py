#!/usr/bin/env python3
"""
chen — Generiert Chen-ER-Diagramme aus einer YAML-Spec.

Input-Format:
  title: "Anzeige-Titel"
  type: chen
  out: <basisname-ohne-erweiterung relativ zum repo>
  entities:
    Kunde:       { x: 0, y: 0, attrs: [kunde_id*, firmenname, email] }
    Auftrag:     { x: 2, y: 0 }
    Kategorie:   { x: 2, y: -1 }
  relations:
    - name: erstellt
      from: Kunde
      to: Auftrag
      cardinality: ["(1,n)", "(1,1)"]    # optional, Labels am Linien-Mittelpunkt
    - name: "gehört zu"
      from: Auftrag
      to: Kategorie

Konvention:
  * Schluesselattribute markiert man mit nachgestelltem "*", z.B. "kunde_id*"
    -> wird im SVG unterstrichen, im .drawio mit <u>...</u>
  * Wenn keine Entitaet ein "attrs"-Feld hat, wird _uebersicht-Suffix gesetzt
    (kein Attribut-Plausibilitaetsfehler im Validator).

Erzeugt (relativ zu repo_root, Default: aktuelles Arbeitsverzeichnis):
  <out>.drawio
  <out>.preview.svg
  <out>.drawio.svg    (Hybrid)
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.sax.saxutils as su
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML benoetigt: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# Basisverzeichnis für relative out:-Pfade. Wird in main() gesetzt.
REPO_ROOT = Path.cwd()

# -------------------- Layout-Konstanten (Defaults, ueberschreibbar pro Spec) --------------------
COL_W = 280           # horizontaler Abstand zweier Grid-Spalten
ROW_H = 220           # vertikaler Abstand zweier Grid-Zeilen
MARGIN_X = 80
MARGIN_Y = 80

ENT_W, ENT_H = 160, 60
REL_W, REL_H = 160, 80
ATTR_RX, ATTR_RY = 60, 25
ATTR_OFFSET = 110     # vertikaler Abstand Entitaet <-> Attribut
ATTR_SPACING = 130    # horizontaler Abstand zwischen Attributen einer Entitaet
ATTR_RAND = 20        # Mindestabstand der aeussersten Attribut-Ellipse zum Bildrand


def apply_layout_overrides(layout: dict) -> None:
    """Erlaubt pro Spec ueberschriebene Layout-Konstanten."""
    global COL_W, ROW_H, MARGIN_X, MARGIN_Y, ATTR_OFFSET, ATTR_SPACING
    if not layout:
        return
    COL_W = layout.get("col_w", COL_W)
    ROW_H = layout.get("row_h", ROW_H)
    MARGIN_X = layout.get("margin_x", MARGIN_X)
    MARGIN_Y = layout.get("margin_y", MARGIN_Y)
    ATTR_OFFSET = layout.get("attr_offset", ATTR_OFFSET)
    ATTR_SPACING = layout.get("attr_spacing", ATTR_SPACING)


def reset_layout() -> None:
    """Setzt Layout-Konstanten auf Defaults zurueck (zwischen Specs in --all-Modus)."""
    global COL_W, ROW_H, MARGIN_X, MARGIN_Y, ATTR_OFFSET, ATTR_SPACING
    COL_W, ROW_H = 280, 220
    MARGIN_X, MARGIN_Y = 80, 80
    ATTR_OFFSET, ATTR_SPACING = 110, 130

# -------------------- Datenklassen --------------------
@dataclass
class Entity:
    name: str
    gx: int
    gy: int
    attrs: list[tuple[str, bool]] = field(default_factory=list)  # (name, is_key)

    @property
    def cx(self) -> int:
        return MARGIN_X + self.gx * COL_W + ENT_W // 2

    @property
    def cy(self) -> int:
        # gy ist auf 0..N normalisiert; oberhalb wird Platz fuer Attribute reserviert.
        return MARGIN_Y + ATTR_OFFSET + 2 * ATTR_RY + self.gy * ROW_H + ENT_H // 2

    @property
    def left(self) -> int:    return self.cx - ENT_W // 2
    @property
    def right(self) -> int:   return self.cx + ENT_W // 2
    @property
    def top(self) -> int:     return self.cy - ENT_H // 2
    @property
    def bottom(self) -> int:  return self.cy + ENT_H // 2


@dataclass
class Relation:
    name: str
    src: str
    dst: str
    cardinality: tuple[str | None, str | None] = (None, None)


@dataclass
class TernaryRelation:
    """Beziehung mit >= 3 Teilnehmern (eine Raute, viele Linien)."""
    name: str
    participants: list[str]                          # Entitaetsnamen
    cardinalities: list[str | None] = field(default_factory=list)
    # Optional: explizite Grid-Position der Raute, sonst Schwerpunkt
    gx: int | None = None
    gy: int | None = None


# -------------------- Geometrie-Helfer --------------------
def attr_ausdehnung(ent: Entity) -> tuple[int, int]:
    """x-Bereich (links, rechts), den Entitaet und Attribut-Ellipsen zusammen belegen."""
    if not ent.attrs:
        return ent.left, ent.right
    halb = (len(ent.attrs) - 1) * ATTR_SPACING // 2 + ATTR_RX
    return min(ent.left, ent.cx - halb), max(ent.right, ent.cx + halb)


def platz_fuer_attribute(entities: dict[str, Entity]) -> None:
    """Vergroessert MARGIN_X, wenn Attribut-Ellipsen links ueber den Bildrand ragen.

    Die Attribute einer Entitaet werden mittig ueber ihr aufgefaechert und sind
    bei drei oder mehr Attributen breiter als die Entitaet selbst. Ein in der
    Spec gesetzter, ausreichender ``layout.margin_x`` bleibt unveraendert.
    """
    global MARGIN_X
    if not entities:
        return
    links = min(attr_ausdehnung(e)[0] for e in entities.values())
    if links < ATTR_RAND:
        MARGIN_X += ATTR_RAND - links


def edge_anchor(ent: Entity, rel_cx: int, rel_cy: int) -> tuple[int, int]:
    """Wo verlaesst die Linie das Entitaets-Rechteck Richtung (rel_cx, rel_cy)?"""
    dx = rel_cx - ent.cx
    dy = rel_cy - ent.cy
    if abs(dx) * ENT_H >= abs(dy) * ENT_W:
        x = ent.right if dx > 0 else ent.left
        y = ent.cy + (dy * (ENT_W // 2) / abs(dx) if dx else 0)
    else:
        y = ent.bottom if dy > 0 else ent.top
        x = ent.cx + (dx * (ENT_H // 2) / abs(dy) if dy else 0)
    return int(x), int(y)


def rhombus_anchor(cx: int, cy: int, other_cx: int, other_cy: int) -> tuple[int, int]:
    """Anschlusspunkt der Beziehungsraute Richtung (other_cx, other_cy).
    Eine Raute hat 4 Spitzen: oben, rechts, unten, links."""
    dx = other_cx - cx
    dy = other_cy - cy
    if abs(dx) * REL_H >= abs(dy) * REL_W:
        return (cx + REL_W // 2, cy) if dx > 0 else (cx - REL_W // 2, cy)
    return (cx, cy + REL_H // 2) if dy > 0 else (cx, cy - REL_H // 2)


def _collides_with_entity(cx: int, cy: int, entities: dict[str, Entity], exclude: tuple[Entity, ...]) -> Entity | None:
    """Pruefe, ob Punkt (cx, cy) +/- REL_W/2 mit einer fremden Entitaets-Box ueberlappt."""
    pad = REL_W // 2
    for e in entities.values():
        if e in exclude:
            continue
        if e.left - pad <= cx <= e.right + pad and e.top - pad <= cy <= e.bottom + pad:
            return e
    return None


def relation_center(e1: Entity, e2: Entity, entities: dict[str, Entity] | None = None) -> tuple[int, int]:
    if e1 is e2:
        # Rekursive Beziehung: Raute oberhalb der Entitaet platzieren.
        return e1.cx, e1.top - 130
    cx = (e1.cx + e2.cx) // 2
    cy = (e1.cy + e2.cy) // 2
    if entities is None:
        return cx, cy
    # Wenn der Mittelpunkt auf einer fremden Entitaet liegt, weiche aus.
    blocker = _collides_with_entity(cx, cy, entities, exclude=(e1, e2))
    if blocker is None:
        return cx, cy
    # Versuche zuerst oberhalb, dann unterhalb des Blockers
    offsets = [
        (0, blocker.top - REL_H - 20 - cy),     # nach oben verschieben
        (0, blocker.bottom + REL_H + 20 - cy),  # nach unten verschieben
    ]
    for dx, dy in offsets:
        nx, ny = cx + dx, cy + dy
        if _collides_with_entity(nx, ny, entities, exclude=(e1, e2)) is None:
            return nx, ny
    return cx, cy


# -------------------- Spec parsen --------------------
def parse_attr(s: str) -> tuple[str, bool]:
    if s.endswith("*"):
        return s[:-1], True
    return s, False


def parse_spec(path: Path) -> tuple[str, dict[str, Entity], list[Relation], list[TernaryRelation], str, bool]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if "entities" not in data:
        raise ValueError(f"{path.name}: keine 'entities:' - vermutlich UML/Relationenschema-Spec (gen_box_diagram.py verwenden).")
    title = data["title"]
    out = data["out"]
    reset_layout()
    apply_layout_overrides(data.get("layout", {}))

    # Normalisiere gx/gy auf 0..N, damit Entitaeten immer im positiven Canvas-Bereich liegen.
    raw = list(data["entities"].items())
    min_gx = min(p["x"] for _, p in raw)
    min_gy = min(p["y"] for _, p in raw)
    entities: dict[str, Entity] = {}
    has_attrs = False
    for name, props in raw:
        attrs_raw = props.get("attrs", []) or []
        attrs = [parse_attr(a) for a in attrs_raw]
        if attrs:
            has_attrs = True
        entities[name] = Entity(name=name, gx=props["x"] - min_gx, gy=props["y"] - min_gy, attrs=attrs)
    platz_fuer_attribute(entities)

    relations: list[Relation] = []
    ternaries: list[TernaryRelation] = []
    for r in data.get("relations", []):
        if "participants" in r:
            tgx = r.get("x")
            tgy = r.get("y")
            if tgx is not None:
                tgx -= min_gx
            if tgy is not None:
                tgy -= min_gy
            ternaries.append(TernaryRelation(
                name=r["name"],
                participants=r["participants"],
                cardinalities=r.get("cardinality", []) or [],
                gx=tgx, gy=tgy,
            ))
        else:
            card = r.get("cardinality", [None, None])
            relations.append(Relation(
                name=r["name"], src=r["from"], dst=r["to"],
                cardinality=(card[0], card[1]) if card else (None, None),
            ))

    return title, entities, relations, ternaries, out, has_attrs


# -------------------- .drawio (mxfile) erzeugen --------------------
def ternary_center(t: TernaryRelation, entities: dict[str, Entity]) -> tuple[int, int]:
    if t.gx is not None and t.gy is not None:
        # Verwende die gleiche Formel wie Entity.cy (mit Attribut-Reserve)
        x = MARGIN_X + t.gx * COL_W + ENT_W // 2
        y = MARGIN_Y + ATTR_OFFSET + 2 * ATTR_RY + t.gy * ROW_H + ENT_H // 2
        return x, y
    cxs = [entities[p].cx for p in t.participants]
    cys = [entities[p].cy for p in t.participants]
    return sum(cxs) // len(cxs), sum(cys) // len(cys)


def mk_drawio(title: str, entities: dict[str, Entity], relations: list[Relation], ternaries: list[TernaryRelation], diagram_id: str) -> str:
    cells: list[str] = []
    cells.append('<mxCell id="0"/>')
    cells.append('<mxCell id="1" parent="0"/>')

    # Entitaeten
    for name, e in entities.items():
        eid = f"ent_{slug(name)}"
        cells.append(
            f'<mxCell id="{eid}" value="{xml_escape(name)}" '
            'style="rounded=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;fontStyle=1" '
            f'vertex="1" parent="1"><mxGeometry x="{e.left}" y="{e.top}" width="{ENT_W}" height="{ENT_H}" as="geometry"/></mxCell>'
        )
        # Attribute
        for i, (aname, is_key) in enumerate(e.attrs):
            aid = f"att_{slug(name)}_{i}"
            # In drawio interpretiert das value-Attribut HTML; im XML-Attribut
            # muss < / > als &lt;/&gt; codiert sein. xml_escape macht das.
            label = (
                f"&lt;u&gt;{xml_escape(aname)}&lt;/u&gt;"
                if is_key else xml_escape(aname)
            )
            # Attribut-Ellipsen oberhalb der Entitaet, gleichmaessig verteilt
            ax = e.cx - (len(e.attrs) - 1) * ATTR_SPACING // 2 + i * ATTR_SPACING - ATTR_RX
            ay = e.top - ATTR_OFFSET - ATTR_RY
            cells.append(
                f'<mxCell id="{aid}" value="{label}" '
                'style="ellipse;whiteSpace=wrap;html=1;fillColor=#d5e8d4;strokeColor=#82b366;fontSize=11" '
                f'vertex="1" parent="1"><mxGeometry x="{ax}" y="{ay}" width="{2*ATTR_RX}" height="{2*ATTR_RY}" as="geometry"/></mxCell>'
            )
            cells.append(
                f'<mxCell id="edge_att_{slug(name)}_{i}" '
                'style="endArrow=none;html=1;strokeColor=#82b366" edge="1" parent="1" '
                f'source="{aid}" target="{eid}"><mxGeometry relative="1" as="geometry"/></mxCell>'
            )

    # Beziehungen mit Rauten dazwischen
    for i, r in enumerate(relations):
        e1 = entities[r.src]
        e2 = entities[r.dst]
        cx, cy = relation_center(e1, e2, entities)
        rid = f"rel_{i}_{slug(r.name)}"
        cells.append(
            f'<mxCell id="{rid}" value="{xml_escape(r.name)}" '
            'style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=13;fontStyle=1" '
            f'vertex="1" parent="1"><mxGeometry x="{cx - REL_W//2}" y="{cy - REL_H//2}" width="{REL_W}" height="{REL_H}" as="geometry"/></mxCell>'
        )
        c1, c2 = r.cardinality
        v1 = f' value="{xml_escape(c1)}"' if c1 else ""
        v2 = f' value="{xml_escape(c2)}"' if c2 else ""
        cells.append(
            f'<mxCell id="{rid}_e1"{v1} style="endArrow=none;html=1;strokeColor=#555555;fontSize=11" edge="1" parent="1" '
            f'source="ent_{slug(r.src)}" target="{rid}"><mxGeometry relative="1" as="geometry"/></mxCell>'
        )
        cells.append(
            f'<mxCell id="{rid}_e2"{v2} style="endArrow=none;html=1;strokeColor=#555555;fontSize=11" edge="1" parent="1" '
            f'source="{rid}" target="ent_{slug(r.dst)}"><mxGeometry relative="1" as="geometry"/></mxCell>'
        )

    # Ternaere Beziehungen
    for ti, t in enumerate(ternaries):
        cx, cy = ternary_center(t, entities)
        rid = f"tern_{ti}_{slug(t.name)}"
        cells.append(
            f'<mxCell id="{rid}" value="{xml_escape(t.name)}" '
            'style="rhombus;whiteSpace=wrap;html=1;fillColor=#fff2cc;strokeColor=#d6b656;fontSize=13;fontStyle=1" '
            f'vertex="1" parent="1"><mxGeometry x="{cx - REL_W//2}" y="{cy - REL_H//2}" width="{REL_W}" height="{REL_H}" as="geometry"/></mxCell>'
        )
        for i, p in enumerate(t.participants):
            card = t.cardinalities[i] if i < len(t.cardinalities) else None
            v = f' value="{xml_escape(card)}"' if card else ""
            cells.append(
                f'<mxCell id="{rid}_e{i}"{v} style="endArrow=none;html=1;strokeColor=#555555;fontSize=11" edge="1" parent="1" '
                f'source="ent_{slug(p)}" target="{rid}"><mxGeometry relative="1" as="geometry"/></mxCell>'
            )

    page_w, page_h = canvas_size(entities)
    inner = "\n        ".join(cells)
    return (
        f'<mxfile host="app.diagrams.net" type="device">\n'
        f'  <diagram id="{diagram_id}" name="{xml_escape(title)}">\n'
        f'    <mxGraphModel dx="{page_w}" dy="{page_h}" grid="1" gridSize="10" guides="1" tooltips="1" '
        f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0">\n'
        f'      <root>\n        {inner}\n      </root>\n'
        f'    </mxGraphModel>\n  </diagram>\n</mxfile>\n'
    )


# -------------------- preview.svg erzeugen --------------------
def mk_preview_svg(title: str, entities: dict[str, Entity], relations: list[Relation], ternaries: list[TernaryRelation]) -> str:
    page_w, page_h = canvas_size(entities)

    style = """
    .shape-entity { fill: #dae8fc; stroke: #6c8ebf; stroke-width: 2; }
    .shape-relation { fill: #fff2cc; stroke: #d6b656; stroke-width: 2; }
    .shape-attr { fill: #d5e8d4; stroke: #82b366; stroke-width: 1.5; }
    .edge-attr { stroke: #82b366; stroke-width: 1; fill: none; }
    .edge-rel { stroke: #555555; stroke-width: 2; fill: none; }
    .lbl-entity { fill: #000; font-size: 16px; font-weight: bold; letter-spacing: 0.6px; }
    .lbl-relation { fill: #000; font-size: 14px; font-weight: bold; letter-spacing: 0.4px; }
    .lbl-attr { fill: #000; font-size: 13px; letter-spacing: 0.3px; }
    .lbl-card { fill: #1f4e8c; font-size: 12px; font-weight: bold; }
    .lbl-card-bg { fill: #ffffff; }
    .key { text-decoration: underline; }
    """

    parts: list[str] = []
    parts.append(f'<?xml version="1.0" encoding="UTF-8"?>')
    parts.append(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" '
        'font-family="Helvetica, Arial, sans-serif">'
    )
    parts.append(f'  <title>{xml_escape(title)}</title>')
    parts.append(f'  <style>{style}</style>')

    # Attribut-Linien (zuerst, damit sie unter den Shapes liegen)
    parts.append('  <g id="edges-attr">')
    for e in entities.values():
        for i, (_, _) in enumerate(e.attrs):
            ax = e.cx - (len(e.attrs) - 1) * ATTR_SPACING // 2 + i * ATTR_SPACING
            ay = e.top - ATTR_OFFSET
            parts.append(f'    <line class="edge-attr" x1="{ax}" y1="{ay}" x2="{e.cx}" y2="{e.top}"/>')
    parts.append('  </g>')

    # Beziehungs-Linien (Entitaet -> Raute -> Entitaet)
    parts.append('  <g id="edges-rel">')
    segments: list[tuple[Relation, tuple[int,int], tuple[int,int], tuple[int,int], tuple[int,int]]] = []
    for r in relations:
        e1 = entities[r.src]
        e2 = entities[r.dst]
        cx, cy = relation_center(e1, e2, entities)
        if e1 is e2:
            # Rekursive Beziehung: links-oben und rechts-oben der Entitaet
            a1 = (e1.left + 30, e1.top)
            a2 = (e1.right - 30, e1.top)
            r1 = (cx - REL_W // 2 + 20, cy + REL_H // 2 - 5)
            r2 = (cx + REL_W // 2 - 20, cy + REL_H // 2 - 5)
        else:
            a1 = edge_anchor(e1, cx, cy)
            a2 = edge_anchor(e2, cx, cy)
            r1 = rhombus_anchor(cx, cy, e1.cx, e1.cy)
            r2 = rhombus_anchor(cx, cy, e2.cx, e2.cy)
        parts.append(f'    <line class="edge-rel" x1="{a1[0]}" y1="{a1[1]}" x2="{r1[0]}" y2="{r1[1]}"/>')
        parts.append(f'    <line class="edge-rel" x1="{r2[0]}" y1="{r2[1]}" x2="{a2[0]}" y2="{a2[1]}"/>')
        segments.append((r, a1, r1, r2, a2))
    # ternaere Beziehungs-Linien (zur Raute hin)
    tern_segments: list[tuple[TernaryRelation, tuple[int,int], list[tuple[int,int]], list[tuple[int,int]]]] = []
    for t in ternaries:
        cx, cy = ternary_center(t, entities)
        anchors_ent: list[tuple[int,int]] = []
        anchors_rel: list[tuple[int,int]] = []
        for p in t.participants:
            e = entities[p]
            ae = edge_anchor(e, cx, cy)
            ar = rhombus_anchor(cx, cy, e.cx, e.cy)
            anchors_ent.append(ae)
            anchors_rel.append(ar)
            parts.append(f'    <line class="edge-rel" x1="{ae[0]}" y1="{ae[1]}" x2="{ar[0]}" y2="{ar[1]}"/>')
        tern_segments.append((t, (cx,cy), anchors_ent, anchors_rel))
    parts.append('  </g>')

    # Entitaets-Rechtecke
    parts.append('  <g id="entities">')
    for e in entities.values():
        parts.append(
            f'    <rect class="shape-entity" x="{e.left}" y="{e.top}" width="{ENT_W}" height="{ENT_H}"/>'
            f'<text class="lbl-entity" x="{e.cx}" y="{e.cy+6}" text-anchor="middle">{xml_escape(e.name)}</text>'
        )
    parts.append('  </g>')

    # Beziehungs-Rauten
    parts.append('  <g id="relations">')
    for r in relations:
        e1 = entities[r.src]
        e2 = entities[r.dst]
        cx, cy = relation_center(e1, e2, entities)
        pts = f"{cx},{cy-REL_H//2} {cx+REL_W//2},{cy} {cx},{cy+REL_H//2} {cx-REL_W//2},{cy}"
        parts.append(
            f'    <polygon class="shape-relation" points="{pts}"/>'
            f'<text class="lbl-relation" x="{cx}" y="{cy+5}" text-anchor="middle">{xml_escape(r.name)}</text>'
        )
    for (t, (cx, cy), _, _) in tern_segments:
        pts = f"{cx},{cy-REL_H//2} {cx+REL_W//2},{cy} {cx},{cy+REL_H//2} {cx-REL_W//2},{cy}"
        parts.append(
            f'    <polygon class="shape-relation" points="{pts}"/>'
            f'<text class="lbl-relation" x="{cx}" y="{cy+5}" text-anchor="middle">{xml_escape(t.name)}</text>'
        )
    parts.append('  </g>')

    # Attribut-Ellipsen
    parts.append('  <g id="attrs">')
    for e in entities.values():
        for i, (aname, is_key) in enumerate(e.attrs):
            ax = e.cx - (len(e.attrs) - 1) * ATTR_SPACING // 2 + i * ATTR_SPACING
            ay = e.top - ATTR_OFFSET
            key_cls = " key" if is_key else ""
            parts.append(
                f'    <ellipse class="shape-attr" cx="{ax}" cy="{ay}" rx="{ATTR_RX}" ry="{ATTR_RY}"/>'
                f'<text class="lbl-attr{key_cls}" x="{ax}" y="{ay+4}" text-anchor="middle">{xml_escape(aname)}</text>'
            )
    parts.append('  </g>')

    # Kardinalitaeten-Labels (mittig auf der jeweiligen Linie zur Entitaet)
    parts.append('  <g id="cardinalities">')
    for (r, a1, r1, r2, a2) in segments:
        c1, c2 = r.cardinality
        for label, p_ent, p_rel in ((c1, a1, r1), (c2, a2, r2)):
            if not label:
                continue
            lx = (p_ent[0] + p_rel[0]) // 2
            ly = (p_ent[1] + p_rel[1]) // 2
            parts.append(
                f'    <rect class="lbl-card-bg" x="{lx-22}" y="{ly-10}" width="44" height="18" rx="2"/>'
                f'<text class="lbl-card" x="{lx}" y="{ly+4}" text-anchor="middle">{xml_escape(label)}</text>'
            )
    for (t, _, anchors_ent, anchors_rel) in tern_segments:
        for i, label in enumerate(t.cardinalities):
            if not label:
                continue
            p_ent = anchors_ent[i]
            p_rel = anchors_rel[i]
            lx = (p_ent[0] + p_rel[0]) // 2
            ly = (p_ent[1] + p_rel[1]) // 2
            parts.append(
                f'    <rect class="lbl-card-bg" x="{lx-22}" y="{ly-10}" width="44" height="18" rx="2"/>'
                f'<text class="lbl-card" x="{lx}" y="{ly+4}" text-anchor="middle">{xml_escape(label)}</text>'
            )
    parts.append('  </g>')

    parts.append('</svg>')
    return "\n".join(parts) + "\n"


# -------------------- Canvas-Groesse --------------------
def canvas_size(entities: dict[str, Entity]) -> tuple[int, int]:
    xs = [e.right for e in entities.values()]
    ys = [e.bottom for e in entities.values()]
    has_attr = any(e.attrs for e in entities.values())
    # Rechts sowohl den Rand neben der Entitaet als auch die Attribut-Ellipsen einschliessen
    w = max(max(xs) + MARGIN_X, max(attr_ausdehnung(e)[1] for e in entities.values()) + ATTR_RAND)
    h = max(ys) + MARGIN_Y
    if has_attr:
        h += 40  # bisschen mehr Luft fuer Attribute oben (sind schon eingerechnet ueber gy+2)
    return w, h


# -------------------- Hybrid-Datei zusammenbauen --------------------
def mk_hybrid(drawio_xml: str, preview_svg: str) -> str:
    m = re.search(r"<svg[^>]*>(.*)</svg>", preview_svg, flags=re.DOTALL)
    inner = m.group(1)
    viewbox_m = re.search(r'viewBox="([^"]+)"', preview_svg)
    viewbox = viewbox_m.group(1) if viewbox_m else "0 0 1000 600"
    content_attr = su.quoteattr(drawio_xml)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{viewbox}" '
        'font-family="Helvetica, Arial, sans-serif" '
        f'content={content_attr}>'
        + inner +
        '</svg>\n'
    )


# -------------------- kleine Helfer --------------------
def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_").lower()


def xml_escape(s: str) -> str:
    return su.escape(s, {'"': "&quot;", "'": "&apos;"})


# -------------------- main --------------------
def process_spec(spec_path: Path) -> None:
    title, entities, relations, ternaries, out_base, has_attrs = parse_spec(spec_path)

    # Wenn kein Attribut definiert ist, automatisch _uebersicht-Suffix sichern
    out = out_base
    if not has_attrs and "_uebersicht" not in Path(out).name:
        out = out + "_uebersicht"
        print(f"  (Hinweis: keine Attribute -> Suffix _uebersicht ergaenzt)")

    diagram_id = Path(out).name
    drawio_xml = mk_drawio(title, entities, relations, ternaries, diagram_id)
    preview_svg = mk_preview_svg(title, entities, relations, ternaries)
    hybrid = mk_hybrid(drawio_xml, preview_svg)

    out_drawio = REPO_ROOT / f"{out}.drawio"
    out_preview = REPO_ROOT / f"{out}.preview.svg"
    out_hybrid = REPO_ROOT / f"{out}.drawio.svg"
    out_drawio.parent.mkdir(parents=True, exist_ok=True)
    out_drawio.write_text(drawio_xml, encoding="utf-8")
    out_preview.write_text(preview_svg, encoding="utf-8")
    out_hybrid.write_text(hybrid, encoding="utf-8")
    print(f"  OK {out_hybrid.relative_to(REPO_ROOT)}")


def main(argv: list[str], repo_root: Path | None = None) -> int:
    global REPO_ROOT
    REPO_ROOT = Path(repo_root) if repo_root is not None else Path.cwd()

    p = argparse.ArgumentParser(prog="edu-diagramm chen", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("specs", nargs="+", help="YAML-Specs")
    args = p.parse_args(argv[1:])

    for s in args.specs:
        path = Path(s)
        if not path.is_absolute():
            path = REPO_ROOT / path
        try:
            rel = path.relative_to(REPO_ROOT)
        except ValueError:
            rel = path
        print(f"Spec: {rel}")
        try:
            process_spec(path)
        except ValueError as e:
            print(f"  SKIP {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
