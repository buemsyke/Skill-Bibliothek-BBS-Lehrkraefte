#!/usr/bin/env python3
"""
box — Generiert UML-Klassen- oder Relationenschema-Diagramme.

Beide Formate haben dieselbe Grundstruktur:
  * Boxen (Klassen oder Tabellen) mit Header + Attribut-/Spaltenliste
  * Beziehungslinien (UML: Assoziation, Relationenschema: FK-Pfeil)

YAML-Spec:
  title: "..."
  type: uml | relational
  out: lessons/.../diagrams/<basisname>
  classes:
    Kunde:
      x: 0
      y: 0
      attrs:
        - "kunde_id*: INT"
        - "firmenname: VARCHAR"
        - "email: VARCHAR"
    Auftrag:
      x: 2
      y: 0
      attrs:
        - "auftrag_id*: INT"
        - "kunde_id^: INT"    # ^ markiert Fremdschluessel (nur relational)
        - "betreff: VARCHAR"
  relations:
    - name: "erstellt"
      from: Kunde
      to: Auftrag
      cardinality: ["1", "0..*"]    # UML: an den Enden; relational: ignoriert
      kind: association             # UML-Kantenart, siehe unten

Zusätzlich je Klasse (nur UML):
  stereotype: "interface"   -> Kopfzeile «interface» über dem Klassennamen
  attrs-Eintrag "---"       -> Trennlinie (Attribut- / Methodenfach)

UML-Kantenarten (``kind:``):
  association (Default) offener Pfeil
  inheritance / extends  hohles Dreieck, durchgezogen (Vererbung)
  implements / realization  hohles Dreieck, gestrichelt (Schnittstelle)
  dependency             offener Pfeil, gestrichelt
  aggregation            hohle Raute an der Quelle
  composition            gefüllte Raute an der Quelle

``out:`` ist relativ zu ``repo_root`` (Default: aktuelles Arbeitsverzeichnis).
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

# Layout
COL_W = 360
ROW_H = 320
MARGIN_X = 60
MARGIN_Y = 60

BOX_W = 280
HEADER_H = 32
STEREO_H = 16          # zusätzliche Kopfhöhe für «stereotype»
SEP_H = 12             # Höhe einer Trennlinie zwischen zwei Fächern
ATTR_LINE_H = 22
ATTR_PAD_TOP = 12
ATTR_PAD_BOTTOM = 12

# UML-Kantenarten: (draw.io-Stilzusatz, SVG-Spitze, gestrichelt?)
#   SVG-Spitze: "open" = offener Pfeil, "triangle" = hohles Dreieck,
#               "diamond" / "diamond_full" = Raute an der Quelle
KANTEN_ARTEN = {
    "association": ("endArrow=open;endFill=0;endSize=12;", "open", False),
    "inheritance": ("endArrow=block;endFill=0;endSize=14;", "triangle", False),
    "extends": ("endArrow=block;endFill=0;endSize=14;", "triangle", False),
    "implements": ("endArrow=block;endFill=0;endSize=14;dashed=1;", "triangle", True),
    "realization": ("endArrow=block;endFill=0;endSize=14;dashed=1;", "triangle", True),
    "dependency": ("endArrow=open;endFill=0;endSize=12;dashed=1;", "open", True),
    "aggregation": ("endArrow=none;startArrow=diamondThin;startFill=0;startSize=14;", "diamond", False),
    "composition": ("endArrow=none;startArrow=diamondThin;startFill=1;startSize=14;", "diamond_full", False),
}


@dataclass
class BoxAttr:
    raw: str          # Originaltext aus Spec
    is_pk: bool
    is_fk: bool
    text: str         # ohne Markierungs-Sigil
    is_sep: bool = False   # "---" = Trennlinie zwischen zwei Fächern

    @property
    def hoehe(self) -> int:
        return SEP_H if self.is_sep else ATTR_LINE_H


@dataclass
class Box:
    name: str
    gx: int
    gy: int
    attrs: list[BoxAttr]
    stereotype: str = ""

    @property
    def x(self) -> int: return MARGIN_X + self.gx * COL_W
    @property
    def y(self) -> int: return MARGIN_Y + self.gy * ROW_H
    @property
    def header_h(self) -> int:
        return HEADER_H + (STEREO_H if self.stereotype else 0)
    @property
    def body_h(self) -> int:
        return ATTR_PAD_TOP + sum(a.hoehe for a in self.attrs) + ATTR_PAD_BOTTOM

    def zeilen(self) -> list[tuple[BoxAttr, int]]:
        """(Attribut, y-Versatz ab Oberkante des Rumpfes) für jede Zeile."""
        y = ATTR_PAD_TOP
        ergebnis = []
        for a in self.attrs:
            ergebnis.append((a, y))
            y += a.hoehe
        return ergebnis
    @property
    def total_h(self) -> int:
        return self.header_h + self.body_h
    @property
    def cx(self) -> int: return self.x + BOX_W // 2
    @property
    def cy(self) -> int: return self.y + self.total_h // 2
    @property
    def left(self) -> int: return self.x
    @property
    def right(self) -> int: return self.x + BOX_W
    @property
    def top(self) -> int: return self.y
    @property
    def bottom(self) -> int: return self.y + self.total_h


@dataclass
class BoxRelation:
    name: str
    src: str
    dst: str
    cardinality: tuple[str | None, str | None] = (None, None)
    kind: str = "association"


def parse_attr(s: str) -> BoxAttr:
    if set(str(s).strip()) == {"-"} and len(str(s).strip()) >= 3:
        return BoxAttr(raw=s, is_pk=False, is_fk=False, text="", is_sep=True)
    is_pk = False
    is_fk = False
    text = s
    # Akzeptiere "name*" oder "name^" am Bezeichner (vor dem Doppelpunkt)
    head, sep, tail = s.partition(":")
    if head.endswith("*"):
        is_pk = True
        head = head[:-1]
    if head.endswith("^"):
        is_fk = True
        head = head[:-1]
    text = head + (":" + tail if sep else "")
    return BoxAttr(raw=s, is_pk=is_pk, is_fk=is_fk, text=text.strip())


def parse_spec(path: Path) -> tuple[str, str, dict[str, Box], list[BoxRelation], str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    title = data["title"]
    dtype = data.get("type", "uml")
    out = data["out"]

    # Normalisiere gx/gy auf 0..N, damit Boxen immer im positiven Canvas-Bereich liegen.
    raw = list(data["classes"].items())
    min_gx = min(p["x"] for _, p in raw)
    min_gy = min(p["y"] for _, p in raw)
    boxes: dict[str, Box] = {}
    for name, props in raw:
        attrs_raw = props.get("attrs", []) or []
        attrs = [parse_attr(a) for a in attrs_raw]
        boxes[name] = Box(
            name=name, gx=props["x"] - min_gx, gy=props["y"] - min_gy, attrs=attrs,
            stereotype=str(props.get("stereotype", "")),
        )

    rels: list[BoxRelation] = []
    for r in data.get("relations", []):
        card = r.get("cardinality", [None, None])
        kind = str(r.get("kind", "association")).lower()
        if kind not in KANTEN_ARTEN:
            raise ValueError(
                f"Unbekannte Kantenart {kind!r}; erlaubt: {', '.join(sorted(KANTEN_ARTEN))}"
            )
        rels.append(BoxRelation(
            name=r.get("name", ""), src=r["from"], dst=r["to"],
            cardinality=(card[0], card[1]) if card else (None, None),
            kind=kind,
        ))

    return title, dtype, boxes, rels, out


def edge_anchor(b: Box, ox: int, oy: int) -> tuple[int, int]:
    """Anschlusspunkt am Rand der Box Richtung (ox, oy)."""
    dx = ox - b.cx
    dy = oy - b.cy
    h = b.total_h
    if abs(dx) * h >= abs(dy) * BOX_W:
        x = b.right if dx > 0 else b.left
        y = b.cy + (dy * (BOX_W // 2) / abs(dx) if dx else 0)
    else:
        y = b.bottom if dy > 0 else b.top
        x = b.cx + (dx * (h // 2) / abs(dy) if dy else 0)
    return int(x), int(y)


# -------------------- .drawio (mxfile) --------------------
def mk_drawio(title: str, dtype: str, boxes: dict[str, Box], relations: list[BoxRelation], diagram_id: str) -> str:
    cells: list[str] = ['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>']

    for name, b in boxes.items():
        bid = f"box_{slug(name)}"
        titel = xml_escape(name)
        if b.stereotype:
            titel = (
                f"&lt;font style=&quot;font-size: 11px&quot;&gt;&#171;{xml_escape(b.stereotype)}"
                f"&#187;&lt;/font&gt;&lt;br/&gt;{titel}"
            )
        cells.append(
            f'<mxCell id="{bid}" value="{titel}" '
            'style="swimlane;fontStyle=1;align=center;verticalAlign=top;startSize=' + str(b.header_h) +
            ';horizontal=1;swimlaneFillColor=#ffffff;fillColor=#dae8fc;strokeColor=#6c8ebf;fontSize=14;rounded=0;html=1" '
            f'vertex="1" parent="1"><mxGeometry x="{b.x}" y="{b.y}" width="{BOX_W}" height="{b.total_h}" as="geometry"/></mxCell>'
        )
        for i, (a, dy) in enumerate(b.zeilen()):
            aid = f"{bid}_a{i}"
            if a.is_sep:
                cells.append(
                    f'<mxCell id="{aid}" value="" '
                    'style="line;strokeWidth=1;html=1;fillColor=none;align=left;verticalAlign=middle;'
                    'points=[];rotatable=0;strokeColor=#6c8ebf" '
                    f'vertex="1" parent="{bid}"><mxGeometry y="{dy}" '
                    f'width="{BOX_W}" height="{SEP_H}" as="geometry"/></mxCell>'
                )
                continue
            label = xml_escape(a.text)
            if a.is_pk:
                label = f"&lt;u&gt;{label}&lt;/u&gt;"
            if a.is_fk and dtype == "relational":
                label = f"&#9656; {label}"   # ▸ Marker fuer FK
            cells.append(
                f'<mxCell id="{aid}" value="{label}" '
                'style="text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=8;fontSize=12" '
                f'vertex="1" parent="{bid}"><mxGeometry y="{dy}" '
                f'width="{BOX_W}" height="{ATTR_LINE_H}" as="geometry"/></mxCell>'
            )

    for ri, r in enumerate(relations):
        b1 = boxes[r.src]
        b2 = boxes[r.dst]
        if dtype == "uml":
            art, _spitze, _dashed = KANTEN_ARTEN[r.kind]
            style = f"{art}html=1;rounded=0;fontSize=12;fontStyle=1;strokeColor=#555555"
        else:
            # Relationenschema: FK -> PK Pfeil mit Pfeilspitze
            style = "endArrow=block;endFill=1;endSize=10;html=1;rounded=0;fontSize=11;strokeColor=#6c8ebf"
        eid = f"rel_{ri}_{slug(r.name)}"
        v = f' value="{xml_escape(r.name)}"' if r.name and dtype == "uml" else ""
        cells.append(
            f'<mxCell id="{eid}"{v} style="{style}" edge="1" parent="1" '
            f'source="box_{slug(r.src)}" target="box_{slug(r.dst)}"><mxGeometry relative="1" as="geometry"/></mxCell>'
        )
        c1, c2 = r.cardinality
        if c1:
            cells.append(
                f'<mxCell id="{eid}_lbl1" value="{xml_escape(c1)}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;fontSize=12" '
                f'vertex="1" connectable="0" parent="{eid}"><mxGeometry x="-0.85" y="-1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>'
            )
        if c2:
            cells.append(
                f'<mxCell id="{eid}_lbl2" value="{xml_escape(c2)}" style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;fontSize=12" '
                f'vertex="1" connectable="0" parent="{eid}"><mxGeometry x="0.85" y="-1" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>'
            )

    page_w, page_h = canvas_size(boxes)
    inner = "\n        ".join(cells)
    return (
        f'<mxfile host="app.diagrams.net" type="device">\n'
        f'  <diagram id="{diagram_id}" name="{xml_escape(title)}">\n'
        f'    <mxGraphModel dx="{page_w}" dy="{page_h}" grid="1" gridSize="10" guides="1" tooltips="1" '
        f'connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0">\n'
        f'      <root>\n        {inner}\n      </root>\n'
        f'    </mxGraphModel>\n  </diagram>\n</mxfile>\n'
    )


# -------------------- preview.svg --------------------
def mk_preview_svg(title: str, dtype: str, boxes: dict[str, Box], relations: list[BoxRelation]) -> str:
    page_w, page_h = canvas_size(boxes)
    style = """
    .box-header { fill: #dae8fc; stroke: #6c8ebf; stroke-width: 2; }
    .box-body { fill: #ffffff; stroke: #6c8ebf; stroke-width: 2; }
    .box-name { fill: #000; font-size: 15px; font-weight: bold; letter-spacing: 0.5px; }
    .box-stereo { fill: #000; font-size: 11px; }
    .box-sep { stroke: #6c8ebf; stroke-width: 2; }
    .box-attr { fill: #000; font-size: 13px; }
    .pk { text-decoration: underline; }
    .fk { fill: #1f4e8c; }
    .edge-uml { stroke: #555555; stroke-width: 2; fill: none; }
    .edge-rel { stroke: #6c8ebf; stroke-width: 2; fill: none; }
    .edge-lbl { fill: #000; font-size: 13px; font-weight: bold; }
    .card-lbl { fill: #000; font-size: 12px; }
    """

    parts: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" font-family="Helvetica, Arial, sans-serif">',
        f'  <title>{xml_escape(title)}</title>',
        f'  <style>{style}</style>',
    ]

    # Beziehungslinien
    parts.append('  <g id="edges">')
    segments: list[tuple[BoxRelation, tuple[int,int], tuple[int,int]]] = []
    for r in relations:
        b1 = boxes[r.src]
        b2 = boxes[r.dst]
        p1 = edge_anchor(b1, b2.cx, b2.cy)
        p2 = edge_anchor(b2, b1.cx, b1.cy)
        cls = "edge-uml" if dtype == "uml" else "edge-rel"
        spitze = KANTEN_ARTEN[r.kind][1] if dtype == "uml" else "filled"
        gestrichelt = KANTEN_ARTEN[r.kind][2] if dtype == "uml" else False
        strich = ' stroke-dasharray="7 5"' if gestrichelt else ""
        parts.append(
            f'    <line class="{cls}"{strich} x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}"/>'
        )
        # Kantenende (Pfeil / Dreieck / Raute)
        import math
        if spitze in ("diamond", "diamond_full"):
            ax, ay = p1                      # Raute sitzt am Quellende
            bx, by = p2
        else:
            ax, ay = p2
            bx, by = p1
        ang = math.atan2(ay - by, ax - bx)
        size = 14 if spitze in ("triangle", "diamond", "diamond_full") else 8
        tx1 = ax - size * math.cos(ang - math.pi/6)
        ty1 = ay - size * math.sin(ang - math.pi/6)
        tx2 = ax - size * math.cos(ang + math.pi/6)
        ty2 = ay - size * math.sin(ang + math.pi/6)
        if spitze == "open":
            parts.append(f'    <polyline class="{cls}" stroke-dasharray="none" points="{tx1:.1f},{ty1:.1f} {ax},{ay} {tx2:.1f},{ty2:.1f}"/>')
        elif spitze == "triangle":
            parts.append(
                f'    <polygon points="{ax},{ay} {tx1:.1f},{ty1:.1f} {tx2:.1f},{ty2:.1f}" '
                'fill="#ffffff" stroke="#555555" stroke-width="2"/>'
            )
        elif spitze in ("diamond", "diamond_full"):
            hx = ax - 2 * size * math.cos(ang)
            hy = ay - 2 * size * math.sin(ang)
            fuell = "#555555" if spitze == "diamond_full" else "#ffffff"
            parts.append(
                f'    <polygon points="{ax},{ay} {tx1:.1f},{ty1:.1f} {hx:.1f},{hy:.1f} '
                f'{tx2:.1f},{ty2:.1f}" fill="{fuell}" stroke="#555555" stroke-width="2"/>'
            )
        else:
            parts.append(f'    <polygon points="{ax},{ay} {tx1:.1f},{ty1:.1f} {tx2:.1f},{ty2:.1f}" fill="#6c8ebf"/>')
        segments.append((r, p1, p2))
    parts.append('  </g>')

    # Boxen
    for b in boxes.values():
        parts.append('  <g>')
        parts.append(f'    <rect class="box-header" x="{b.x}" y="{b.y}" width="{BOX_W}" height="{b.header_h}"/>')
        if b.stereotype:
            parts.append(f'    <text class="box-stereo" x="{b.cx}" y="{b.y + 16}" text-anchor="middle">&#171;{xml_escape(b.stereotype)}&#187;</text>')
            parts.append(f'    <text class="box-name" x="{b.cx}" y="{b.y + 36}" text-anchor="middle">{xml_escape(b.name)}</text>')
        else:
            parts.append(f'    <text class="box-name" x="{b.cx}" y="{b.y + 22}" text-anchor="middle">{xml_escape(b.name)}</text>')
        parts.append(f'    <rect class="box-body" x="{b.x}" y="{b.y + b.header_h}" width="{BOX_W}" height="{b.body_h}"/>')
        for a, dy in b.zeilen():
            if a.is_sep:
                sy = b.y + b.header_h + dy + SEP_H / 2
                parts.append(f'    <line class="box-sep" x1="{b.x}" y1="{sy}" x2="{b.right}" y2="{sy}"/>')
                continue
            ay = b.y + b.header_h + dy + 14
            classes = "box-attr"
            if a.is_pk:
                classes += " pk"
            if a.is_fk and dtype == "relational":
                classes += " fk"
            prefix = "&#9656; " if (a.is_fk and dtype == "relational") else ""
            parts.append(f'    <text class="{classes}" x="{b.x + 12}" y="{ay}">{prefix}{xml_escape(a.text)}</text>')
        parts.append('  </g>')

    # Beziehungsbeschriftung und Kardinalitaeten
    parts.append('  <g id="rel-labels">')
    for (r, p1, p2) in segments:
        mx = (p1[0] + p2[0]) // 2
        my = (p1[1] + p2[1]) // 2
        if r.name and dtype == "uml":
            parts.append(f'    <rect x="{mx-40}" y="{my-22}" width="80" height="18" rx="2" fill="#ffffff"/>')
            parts.append(f'    <text class="edge-lbl" x="{mx}" y="{my-8}" text-anchor="middle">{xml_escape(r.name)}</text>')
        c1, c2 = r.cardinality
        if c1:
            # Position nahe p1
            lx, ly = int(p1[0] * 0.85 + p2[0] * 0.15), int(p1[1] * 0.85 + p2[1] * 0.15)
            parts.append(f'    <rect x="{lx-16}" y="{ly+6}" width="32" height="16" rx="2" fill="#ffffff"/>')
            parts.append(f'    <text class="card-lbl" x="{lx}" y="{ly+18}" text-anchor="middle">{xml_escape(c1)}</text>')
        if c2:
            lx, ly = int(p1[0] * 0.15 + p2[0] * 0.85), int(p1[1] * 0.15 + p2[1] * 0.85)
            parts.append(f'    <rect x="{lx-20}" y="{ly+6}" width="40" height="16" rx="2" fill="#ffffff"/>')
            parts.append(f'    <text class="card-lbl" x="{lx}" y="{ly+18}" text-anchor="middle">{xml_escape(c2)}</text>')
    parts.append('  </g>')

    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def canvas_size(boxes: dict[str, Box]) -> tuple[int, int]:
    rights = [b.right for b in boxes.values()]
    bottoms = [b.bottom for b in boxes.values()]
    return max(rights) + MARGIN_X, max(bottoms) + MARGIN_Y


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


def slug(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_").lower()


def xml_escape(s: str) -> str:
    return su.escape(s, {'"': "&quot;", "'": "&apos;"})


def process_spec(spec_path: Path) -> None:
    title, dtype, boxes, relations, out = parse_spec(spec_path)
    diagram_id = Path(out).name
    drawio_xml = mk_drawio(title, dtype, boxes, relations, diagram_id)
    preview_svg = mk_preview_svg(title, dtype, boxes, relations)
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

    p = argparse.ArgumentParser(prog="edu-diagramm box", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("specs", nargs="+")
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
        process_spec(path)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
