#!/usr/bin/env python3
"""
flow — Generische Block-/Ablaufdiagramme (draw.io + SVG).

Gedacht für alles, was *kein* ER- oder Klassendiagramm ist: Architekturskizzen,
Datenflüsse, Werkzeugketten, Verdrahtungspläne, Zyklen. Die Knoten werden in
einem Raster platziert, die Kanten sucht der Generator selbst an die passenden
Kanten der Kästen.

YAML-Spec:
  title: "Arbeitsteilung Arduino / PC"
  type: flow
  out: lessons/10_.../diagrams/10_v01_flow_arbeitsteilung
  spalte: 340            # optional: Rasterbreite  (Default 320)
  zeile: 200             # optional: Rasterhöhe    (Default 190)
  nodes:
    arduino:
      x: 0               # Rasterspalte
      y: 0               # Rasterzeile
      label: "Arduino UNO"
      lines: ["misst", "C++ (vorgegeben)"]
      caption: "~30 Zeilen"          # Text unter dem Kasten
      shape: box                     # box|rounded|ellipse|raute|note|zylinder
      color: blau                    # blau|gruen|gelb|rot|lila|orange|grau|weiss
      w: 260                         # optional feste Breite/Höhe
    pc:
      x: 1
      y: 0
      label: "PC / Notebook"
      children:                      # Unterkästen (Container-Knoten)
        - { id: pc_php, label: "auswertung.php" }
  edges:
    - from: arduino
      to: pc
      label: "CSV über die serielle Schnittstelle"
      style: solid                   # solid|dashed
      arrow: single                  # single|double|none
      route: direkt                  # direkt|links|rechts|oben|unten (Umleitung außen herum)
  notes:
    - { x: 0, y: 1, text: "der gesamte Kurs" }

Umleitungen (``route``): ``links``/``rechts`` führen außen an der Seite herum und
verbinden Knoten in verschiedenen Zeilen (Rückführung im Regelkreis). Überlappen
Start und Ziel in der Höhe (gleiche Zeile), liefe die Umleitung quer über die
Zeile – sie wird dann unten herum geführt. ``unten``/``oben`` führen ausdrücklich
unter bzw. über dem Diagramm entlang; mehrere solcher Umleitungen bekommen
eigene, parallele Bahnen.

``out:`` ist relativ zu ``repo_root`` (Default: aktuelles Arbeitsverzeichnis).
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - identische Meldung wie in box/chen
    print("PyYAML benoetigt: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

from ._common import (
    br_join,
    farben,
    mk_hybrid,  # noqa: F401  (Teil der öffentlichen Modulfläche)
    mk_mxfile,
    mk_svg,
    schreibe_ausgaben,
    slug,
    text_breite,
    xml_escape,
    zeilen,
)

# Basisverzeichnis für relative out:-Pfade. Wird in main() gesetzt.
REPO_ROOT = Path.cwd()

# Layout-Konstanten
MARGIN = 40
COL_W_DEFAULT = 320
ROW_H_DEFAULT = 190

PAD_X = 22
PAD_Y = 14
TITEL_H = 26
ZEILEN_H = 20
MIN_W = 150
MIN_H = 60

KIND_H = 30          # Höhe eines Unterkastens
KIND_ABSTAND = 8
GRUPPE_PAD = 12

TITEL_FS = 14        # Schriftgröße Kopfzeile
ZEILEN_FS = 12.5
KANTEN_FS = 12
NOTIZ_FS = 12.5

UMWEG = 50           # Abstand der Umleitung (route: links|rechts|oben|unten) vom Diagramm
BAHN_ABSTAND = 26    # Abstand paralleler Umleitungen oben bzw. unten
OBEN_RAND = 20       # Mindestabstand einer oberen Umleitung zum Bildrand


@dataclass
class Knoten:
    """Ein Kasten mit absoluter Pixelgeometrie."""

    kid: str
    label: str
    lines: list[str]
    shape: str
    color: str | None
    caption: str
    x: int = 0
    y: int = 0
    w: int = MIN_W
    h: int = MIN_H
    parent: str | None = None
    children: list[str] = field(default_factory=list)

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    @property
    def right(self) -> int:
        return self.x + self.w

    @property
    def bottom(self) -> int:
        return self.y + self.h


@dataclass
class Kante:
    src: str
    dst: str
    label: list[str]
    stil: str
    pfeil: str
    route: str
    bahn: int = 0        # laufende Nummer bei mehreren Umleitungen oben/unten


@dataclass
class Notiz:
    x: float
    y: float
    text: list[str]


# -------------------- Spec lesen --------------------
def _knoten_masse(label: str, lines: list[str], props: dict) -> tuple[int, int]:
    """Breite/Höhe eines einfachen Kastens aus seinem Text ableiten."""
    breiten = [text_breite(label, TITEL_FS, fett=True)] if label else [0.0]
    breiten += [text_breite(z, ZEILEN_FS) for z in lines]
    w = int(props.get("w") or max(MIN_W, math.ceil(max(breiten) + 2 * PAD_X)))
    inhalt = (TITEL_H if label else 0) + ZEILEN_H * len(lines)
    h = int(props.get("h") or max(MIN_H, inhalt + 2 * PAD_Y))
    return w, h


def parse_spec(path: Path) -> tuple[str, dict[str, Knoten], list[Kante], list[Notiz], str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    title = data["title"]
    out = data["out"]
    col_w = int(data.get("spalte", COL_W_DEFAULT))
    row_h = int(data.get("zeile", ROW_H_DEFAULT))

    roh = list((data.get("nodes") or {}).items())
    if not roh:
        raise ValueError("flow-Spec ohne 'nodes'.")
    # Rasterkoordinaten dürfen Bruchzahlen sein (0.5 = halbe Spalte/Zeile).
    min_gx = min(float(p.get("x", 0)) for _, p in roh)
    min_gy = min(float(p.get("y", 0)) for _, p in roh)

    knoten: dict[str, Knoten] = {}
    for name, props in roh:
        props = props or {}
        label = str(props.get("label", name))
        lines = zeilen(props.get("lines"))
        kinder_spec = props.get("children") or []

        if kinder_spec:
            # Container: Breite/Höhe ergeben sich aus Titel und Unterkästen.
            kind_breiten = [
                text_breite(str(k.get("label", "")), ZEILEN_FS, fett=True) for k in kinder_spec
            ]
            kind_breiten.append(text_breite(label, TITEL_FS, fett=True) - 2 * GRUPPE_PAD)
            innen_w = max([MIN_W - 2 * GRUPPE_PAD] + kind_breiten) + 2 * PAD_X
            w = int(props.get("w") or math.ceil(innen_w + 2 * GRUPPE_PAD))
            kopf = TITEL_H + PAD_Y
            h = int(
                props.get("h")
                or kopf
                + GRUPPE_PAD
                + len(kinder_spec) * KIND_H
                + (len(kinder_spec) - 1) * KIND_ABSTAND
                + GRUPPE_PAD
            )
        else:
            w, h = _knoten_masse(label, lines, props)

        k = Knoten(
            kid=name,
            label=label,
            lines=lines,
            shape=str(props.get("shape", "box")).lower(),
            color=props.get("color"),
            caption=str(props.get("caption", "")),
            w=w,
            h=h,
        )
        gx = float(props.get("x", 0)) - min_gx
        gy = float(props.get("y", 0)) - min_gy
        zellen_links = MARGIN + gx * col_w
        zellen_oben = MARGIN + gy * row_h
        k.x = int(zellen_links + (col_w - w) / 2)
        k.y = int(zellen_oben + (row_h - h) / 2)
        knoten[name] = k

        # Unterkästen absolut positionieren
        ky = k.y + TITEL_H + PAD_Y + GRUPPE_PAD
        for kind in kinder_spec:
            kid = str(kind["id"])
            kk = Knoten(
                kid=kid,
                label=str(kind.get("label", kid)),
                lines=zeilen(kind.get("lines")),
                shape="box",
                color=kind.get("color", props.get("color")),
                caption=str(kind.get("caption", "")),
                x=k.x + GRUPPE_PAD,
                y=ky,
                w=k.w - 2 * GRUPPE_PAD,
                h=KIND_H,
                parent=name,
            )
            knoten[kid] = kk
            k.children.append(kid)
            ky += KIND_H + KIND_ABSTAND

    kanten: list[Kante] = []
    for e in data.get("edges") or []:
        for ende in ("from", "to"):
            if e[ende] not in knoten:
                raise ValueError(f"Kante verweist auf unbekannten Knoten: {e[ende]!r}")
        kanten.append(
            Kante(
                src=e["from"],
                dst=e["to"],
                label=zeilen(e.get("label")),
                stil=str(e.get("style", "solid")).lower(),
                pfeil=str(e.get("arrow", "single")).lower(),
                route=str(e.get("route", "direkt")).lower(),
            )
        )

    notizen: list[Notiz] = []
    for n in data.get("notes") or []:
        gx = float(n.get("x", 0)) - min_gx
        gy = float(n.get("y", 0)) - min_gy
        notizen.append(
            Notiz(
                x=MARGIN + gx * col_w + col_w / 2,
                y=MARGIN + gy * row_h + row_h / 2,
                text=zeilen(n.get("text")),
            )
        )

    _routen_festlegen(knoten, kanten, notizen)
    return title, knoten, kanten, notizen, out


def _routen_festlegen(knoten: dict[str, Knoten], kanten: list[Kante], notizen: list[Notiz]) -> None:
    """Umleitungen auflösen: gleiche Zeile → unten herum; Bahnen nummerieren; Platz oben schaffen."""
    zaehler = {"oben": 0, "unten": 0}
    for e in kanten:
        a, b = knoten[e.src], knoten[e.dst]
        if e.route in ("links", "rechts") and a.y < b.bottom and b.y < a.bottom:
            e.route = "unten"   # seitlich herum liefe die Kante quer über die Zeile
        if e.route in zaehler:
            e.bahn = zaehler[e.route]
            zaehler[e.route] += 1
    if zaehler["oben"]:
        oberste = _bahn_y(knoten, notizen, "oben", zaehler["oben"] - 1)
        verschiebung = math.ceil(OBEN_RAND - oberste) if oberste < OBEN_RAND else 0
        if verschiebung:
            for k in knoten.values():
                k.y += verschiebung
            for n in notizen:
                n.y += verschiebung


def _bahn_y(knoten: dict[str, Knoten], notizen: list[Notiz] | tuple, seite: str, bahn: int) -> float:
    """y-Koordinate der Umleitungsbahn unter bzw. über dem Diagramm."""
    if seite == "unten":
        basis = max([k.bottom + (24 if k.caption else 0) for k in knoten.values()]
                    + [n.y - 12 + 20 * max(1, len(n.text)) for n in notizen])
        return basis + UMWEG + bahn * BAHN_ABSTAND
    basis = min([k.y for k in knoten.values()] + [n.y - 12 for n in notizen])
    return basis - UMWEG - bahn * BAHN_ABSTAND


# -------------------- Geometrie --------------------
def anschluss(k: Knoten, zx: float, zy: float) -> tuple[float, float]:
    """Punkt auf dem Rand von ``k`` in Richtung (zx, zy)."""
    dx = zx - k.cx
    dy = zy - k.cy
    if dx == 0 and dy == 0:
        return k.cx, k.bottom
    if abs(dx) * k.h >= abs(dy) * k.w:
        x = k.right if dx > 0 else k.x
        y = k.cy + (dy * (k.w / 2) / abs(dx) if dx else 0)
    else:
        y = k.bottom if dy > 0 else k.y
        x = k.cx + (dx * (k.h / 2) / abs(dy) if dy else 0)
    return x, y


def kanten_punkte(
    kante: Kante, knoten: dict[str, Knoten], links_aussen: float, rechts_aussen: float,
    *, notizen: list[Notiz] | tuple = (),
) -> list[tuple[float, float]]:
    """Stützpunkte einer Kante — direkt oder als Umleitung außen herum."""
    a = knoten[kante.src]
    b = knoten[kante.dst]
    if kante.route in ("unten", "oben"):
        y = _bahn_y(knoten, notizen, kante.route, kante.bahn)
        ya, yb = (a.bottom, b.bottom) if kante.route == "unten" else (a.y, b.y)
        return [(a.cx, ya), (a.cx, y), (b.cx, y), (b.cx, yb)]
    if kante.route == "rechts":
        ox = rechts_aussen
        return [(a.right, a.cy), (ox, a.cy), (ox, b.cy), (b.right, b.cy)]
    if kante.route == "links":
        ox = links_aussen
        return [(a.x, a.cy), (ox, a.cy), (ox, b.cy), (b.x, b.cy)]
    p1 = anschluss(a, b.cx, b.cy)
    p2 = anschluss(b, a.cx, a.cy)
    return [p1, p2]


def label_mitte(pts: list[tuple[float, float]]) -> tuple[float, float]:
    """Mittelpunkt des mittleren Kantensegments — dort sitzt die Beschriftung."""
    m = len(pts) // 2
    if len(pts) == 2:
        return (pts[0][0] + pts[1][0]) / 2, (pts[0][1] + pts[1][1]) / 2
    return (pts[m - 1][0] + pts[m][0]) / 2, (pts[m - 1][1] + pts[m][1]) / 2


def label_masse(label: list[str]) -> tuple[float, float]:
    return max(text_breite(z, KANTEN_FS) for z in label) + 12, 16 * len(label)


def leinwand(knoten: dict[str, Knoten], notizen: list[Notiz], kanten: list[Kante]) -> tuple[int, int]:
    """Seitengröße aus Knoten, Bildunterschriften, Notizen und Kanten­beschriftungen."""
    rechts = max(k.right for k in knoten.values())
    unten = max(k.bottom + (24 if k.caption else 0) for k in knoten.values())
    if notizen:
        rechts = max(rechts, max(n.x + 120 for n in notizen))
        unten = max(unten, max(n.y + 10 + NOTIZ_FS * len(n.text) for n in notizen))
    links_aussen, rechts_aussen = _aussen(knoten)
    for e in kanten:
        pts = kanten_punkte(e, knoten, links_aussen, rechts_aussen, notizen=notizen)
        rechts = max(rechts, max(px for px, _ in pts))
        unten = max(unten, max(py for _, py in pts))
        if e.label:
            mx, my = label_mitte(pts)
            bw, bh = label_masse(e.label)
            rechts = max(rechts, mx + bw / 2)
            unten = max(unten, my + bh / 2)
    return int(rechts + MARGIN), int(unten + MARGIN)


def _aussen(knoten: dict[str, Knoten]) -> tuple[float, float]:
    """x-Koordinaten der Umleitungsbahnen links und rechts vom Diagramm."""
    links = max(10.0, min(k.x for k in knoten.values()) - UMWEG)
    rechts = max(k.right for k in knoten.values()) + UMWEG
    return links, rechts


# -------------------- .drawio --------------------
_SHAPE_STYLE = {
    "box": "rounded=0;whiteSpace=wrap;html=1;",
    "rounded": "rounded=1;arcSize=12;whiteSpace=wrap;html=1;",
    "ellipse": "ellipse;whiteSpace=wrap;html=1;",
    "raute": "rhombus;whiteSpace=wrap;html=1;",
    "note": "shape=note;size=18;whiteSpace=wrap;html=1;",
    "zylinder": "shape=cylinder3;boundedLbl=1;backgroundOutline=1;size=12;whiteSpace=wrap;html=1;",
}


def _label_html(label: str, lines: list[str]) -> str:
    teile = []
    if label:
        teile.append("&lt;b&gt;" + xml_escape(label) + "&lt;/b&gt;")
    teile += [xml_escape(z) for z in lines]
    return "&lt;br/&gt;".join(teile)


def mk_drawio(
    title: str,
    knoten: dict[str, Knoten],
    kanten: list[Kante],
    notizen: list[Notiz],
    diagram_id: str,
) -> str:
    cells: list[str] = []
    ids = {name: f"n_{slug(name)}" for name in knoten}

    for name, k in knoten.items():
        fill, stroke = farben(k.color)
        if k.children:
            style = (
                f"swimlane;startSize={TITEL_H + PAD_Y};html=1;fontStyle=1;fontSize={TITEL_FS};"
                f"fillColor={fill};strokeColor={stroke};swimlaneFillColor=#ffffff;"
                "align=center;verticalAlign=middle;rounded=0;"
            )
            cells.append(
                f'<mxCell id="{ids[name]}" value="{xml_escape(k.label)}" style="{style}" '
                f'vertex="1" parent="1"><mxGeometry x="{k.x}" y="{k.y}" width="{k.w}" '
                f'height="{k.h}" as="geometry"/></mxCell>'
            )
            continue
        if k.parent is not None:
            continue  # wird unten relativ zum Container ausgegeben

        style = (
            _SHAPE_STYLE.get(k.shape, _SHAPE_STYLE["box"])
            + f"fillColor={fill};strokeColor={stroke};align=center;verticalAlign=middle;"
            f"fontSize={ZEILEN_FS};"
        )
        cells.append(
            f'<mxCell id="{ids[name]}" value="{_label_html(k.label, k.lines)}" style="{style}" '
            f'vertex="1" parent="1"><mxGeometry x="{k.x}" y="{k.y}" width="{k.w}" '
            f'height="{k.h}" as="geometry"/></mxCell>'
        )

    # Unterkästen relativ zu ihrem Container
    for name, k in knoten.items():
        if k.parent is None:
            continue
        eltern = knoten[k.parent]
        fill, stroke = farben(k.color)
        style = (
            "rounded=0;whiteSpace=wrap;html=1;align=center;verticalAlign=middle;"
            f"fontSize={ZEILEN_FS};fillColor=#ffffff;strokeColor={stroke};"
        )
        cells.append(
            f'<mxCell id="{ids[name]}" value="{_label_html(k.label, k.lines)}" style="{style}" '
            f'vertex="1" parent="{ids[k.parent]}"><mxGeometry x="{k.x - eltern.x}" '
            f'y="{k.y - eltern.y}" width="{k.w}" height="{k.h}" as="geometry"/></mxCell>'
        )

    # Bildunterschriften
    for name, k in knoten.items():
        if not k.caption:
            continue
        cells.append(
            f'<mxCell id="{ids[name]}_cap" value="{xml_escape(k.caption)}" '
            'style="text;html=1;strokeColor=none;fillColor=none;align=center;'
            f'verticalAlign=top;fontSize={NOTIZ_FS};fontColor=#444444" vertex="1" parent="1">'
            f'<mxGeometry x="{k.x}" y="{k.bottom + 6}" width="{k.w}" height="20" '
            'as="geometry"/></mxCell>'
        )

    links_aussen, rechts_aussen = _aussen(knoten)
    for i, e in enumerate(kanten):
        pfeil_ende = "none" if e.pfeil == "none" else "block"
        pfeil_start = "block" if e.pfeil == "double" else "none"
        strich = "dashed=1;" if e.stil == "dashed" else ""
        umleitung = e.route in ("links", "rechts", "oben", "unten")
        orth = "edgeStyle=orthogonalEdgeStyle;" if umleitung else ""
        if e.route in ("oben", "unten"):
            seite = "1" if e.route == "unten" else "0"
            orth += (f"exitX=0.5;exitY={seite};exitDx=0;exitDy=0;"
                     f"entryX=0.5;entryY={seite};entryDx=0;entryDy=0;")
        style = (
            f"html=1;rounded=0;{orth}{strich}endArrow={pfeil_ende};endFill=1;endSize=8;"
            f"startArrow={pfeil_start};startFill=1;startSize=8;strokeColor=#555555;"
            f"fontSize={KANTEN_FS};labelBackgroundColor=#ffffff;"
        )
        eid = f"e{i}_{slug(e.src)}_{slug(e.dst)}"
        wert = f' value="{br_join(e.label)}"' if e.label else ""
        punkte = ""
        if umleitung:
            zwischen = kanten_punkte(e, knoten, links_aussen, rechts_aussen, notizen=notizen)[1:-1]
            inner = "".join(f'<mxPoint x="{int(px)}" y="{int(py)}"/>' for px, py in zwischen)
            punkte = f'<Array as="points">{inner}</Array>'
        cells.append(
            f'<mxCell id="{eid}"{wert} style="{style}" edge="1" parent="1" '
            f'source="{ids[e.src]}" target="{ids[e.dst]}">'
            f'<mxGeometry relative="1" as="geometry">{punkte}</mxGeometry></mxCell>'
        )

    for i, n in enumerate(notizen):
        cells.append(
            f'<mxCell id="note{i}" value="{br_join(n.text)}" '
            'style="text;html=1;strokeColor=none;fillColor=none;align=center;'
            f'verticalAlign=middle;fontSize={NOTIZ_FS}" vertex="1" parent="1">'
            f'<mxGeometry x="{int(n.x - 110)}" y="{int(n.y - 12)}" width="220" '
            f'height="{20 * max(1, len(n.text))}" as="geometry"/></mxCell>'
        )

    page_w, page_h = leinwand(knoten, notizen, kanten)
    return mk_mxfile(cells, page_w, page_h, title, diagram_id)


# -------------------- preview.svg --------------------
SVG_STYLE = """
    .knoten { stroke-width: 2; }
    .titel { font-size: 14px; font-weight: bold; fill: #000; }
    .zeile { font-size: 12.5px; fill: #000; }
    .caption { font-size: 12.5px; fill: #444; }
    .notiz { font-size: 12.5px; fill: #000; }
    .kante { stroke: #555555; stroke-width: 2; fill: none; }
    .kante-gestrichelt { stroke: #555555; stroke-width: 2; fill: none; stroke-dasharray: 6 4; }
    .kantenlabel { font-size: 12px; fill: #000; }
"""


def _shape_svg(k: Knoten, fill: str, stroke: str) -> tuple[list[str], float]:
    """SVG-Form eines Knotens; liefert (Fragmente, vertikaler Textversatz)."""
    x, y, w, h = k.x, k.y, k.w, k.h
    a = f'class="knoten" fill="{fill}" stroke="{stroke}"'
    if k.shape == "ellipse":
        return [f'<ellipse {a} cx="{k.cx}" cy="{k.cy}" rx="{w / 2}" ry="{h / 2}"/>'], 0.0
    if k.shape == "raute":
        pts = f"{k.cx},{y} {x + w},{k.cy} {k.cx},{y + h} {x},{k.cy}"
        return [f'<polygon {a} points="{pts}"/>'], 0.0
    if k.shape == "note":
        s = 18
        pts = f"{x},{y} {x + w - s},{y} {x + w},{y + s} {x + w},{y + h} {x},{y + h}"
        return [
            f'<polygon {a} points="{pts}"/>',
            f'<polyline fill="none" stroke="{stroke}" stroke-width="2" '
            f'points="{x + w - s},{y} {x + w - s},{y + s} {x + w},{y + s}"/>',
        ], 0.0
    if k.shape == "zylinder":
        ry = 12
        d = (
            f"M {x},{y + ry} A {w / 2},{ry} 0 0 1 {x + w},{y + ry} "
            f"L {x + w},{y + h - ry} A {w / 2},{ry} 0 0 1 {x},{y + h - ry} Z"
        )
        return [
            f'<path {a} d="{d}"/>',
            f'<ellipse {a} cx="{k.cx}" cy="{y + ry}" rx="{w / 2}" ry="{ry}"/>',
        ], ry / 2
    rx = 8 if k.shape == "rounded" else 0
    return [f'<rect {a} x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/>'], 0.0


def _text_block(k: Knoten, versatz: float) -> list[str]:
    """Kopfzeile (fett) und Textzeilen mittig im Kasten."""
    n = (1 if k.label else 0) + len(k.lines)
    if n == 0:
        return []
    gesamt = (TITEL_H if k.label else 0) + ZEILEN_H * len(k.lines)
    y = k.cy - gesamt / 2 + versatz
    teile: list[str] = []
    if k.label:
        y += TITEL_H * 0.72
        teile.append(
            f'<text class="titel" x="{k.cx}" y="{y:.1f}" text-anchor="middle">'
            f"{xml_escape(k.label)}</text>"
        )
        y += TITEL_H * 0.28
    for z in k.lines:
        y += ZEILEN_H * 0.75
        teile.append(
            f'<text class="zeile" x="{k.cx}" y="{y:.1f}" text-anchor="middle">'
            f"{xml_escape(z)}</text>"
        )
        y += ZEILEN_H * 0.25
    return teile


def _pfeilspitze(p_von: tuple[float, float], p_zu: tuple[float, float]) -> str:
    ang = math.atan2(p_zu[1] - p_von[1], p_zu[0] - p_von[0])
    size = 9
    x1 = p_zu[0] - size * math.cos(ang - math.pi / 7)
    y1 = p_zu[1] - size * math.sin(ang - math.pi / 7)
    x2 = p_zu[0] - size * math.cos(ang + math.pi / 7)
    y2 = p_zu[1] - size * math.sin(ang + math.pi / 7)
    return (
        f'<polygon points="{p_zu[0]:.1f},{p_zu[1]:.1f} {x1:.1f},{y1:.1f} {x2:.1f},{y2:.1f}" '
        'fill="#555555"/>'
    )


def mk_preview_svg(
    title: str, knoten: dict[str, Knoten], kanten: list[Kante], notizen: list[Notiz]
) -> str:
    page_w, page_h = leinwand(knoten, notizen, kanten)
    links_aussen, rechts_aussen = _aussen(knoten)
    parts: list[str] = ['  <g id="kanten">']

    # Erst alle Linien, dann alle Beschriftungen — sonst zieht eine später
    # gezeichnete Kante einen Strich durch ein früher gesetztes Label.
    beschriftungen: list[str] = []
    for e in kanten:
        pts = kanten_punkte(e, knoten, links_aussen, rechts_aussen, notizen=notizen)
        cls = "kante-gestrichelt" if e.stil == "dashed" else "kante"
        poly = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
        parts.append(f'    <polyline class="{cls}" points="{poly}"/>')
        if e.pfeil != "none":
            parts.append("    " + _pfeilspitze(pts[-2], pts[-1]))
        if e.pfeil == "double":
            parts.append("    " + _pfeilspitze(pts[1], pts[0]))
        if e.label:
            mx, my = label_mitte(pts)
            bw, bh = label_masse(e.label)
            beschriftungen.append(
                f'    <rect x="{mx - bw / 2:.1f}" y="{my - bh / 2 - 2:.1f}" width="{bw:.1f}" '
                f'height="{bh + 4}" fill="#ffffff"/>'
            )
            ty = my - bh / 2 + 12
            for z in e.label:
                beschriftungen.append(
                    f'    <text class="kantenlabel" x="{mx:.1f}" y="{ty:.1f}" '
                    f'text-anchor="middle">{xml_escape(z)}</text>'
                )
                ty += 16
    parts += beschriftungen
    parts.append("  </g>")

    # Container zuerst, damit Unterkästen darüber liegen.
    for k in sorted(knoten.values(), key=lambda n: (n.parent is not None, n.y)):
        fill, stroke = farben(k.color)
        if k.children:
            parts.append(f'  <g id="{slug(k.kid)}">')
            parts.append(
                f'    <rect class="knoten" fill="#ffffff" stroke="{stroke}" x="{k.x}" y="{k.y}" '
                f'width="{k.w}" height="{k.h}"/>'
            )
            parts.append(
                f'    <rect class="knoten" fill="{fill}" stroke="{stroke}" x="{k.x}" y="{k.y}" '
                f'width="{k.w}" height="{TITEL_H + PAD_Y}"/>'
            )
            parts.append(
                f'    <text class="titel" x="{k.cx}" y="{k.y + TITEL_H + PAD_Y / 2 - 4:.1f}" '
                f'text-anchor="middle">{xml_escape(k.label)}</text>'
            )
            parts.append("  </g>")
            continue
        if k.parent is not None:
            fill = "#ffffff"
        formen, versatz = _shape_svg(k, fill, stroke)
        parts.append("  <g>")
        parts += ["    " + f for f in formen]
        parts += ["    " + t for t in _text_block(k, versatz)]
        parts.append("  </g>")

    for k in knoten.values():
        if k.caption:
            parts.append(
                f'  <text class="caption" x="{k.cx}" y="{k.bottom + 20}" '
                f'text-anchor="middle">{xml_escape(k.caption)}</text>'
            )

    for n in notizen:
        y = n.y - (len(n.text) - 1) * 8
        for z in n.text:
            parts.append(
                f'  <text class="notiz" x="{n.x:.1f}" y="{y:.1f}" text-anchor="middle">'
                f"{xml_escape(z)}</text>"
            )
            y += 17

    return mk_svg(parts, page_w, page_h, title, SVG_STYLE)


# -------------------- Ablauf --------------------
def process_spec(spec_path: Path) -> None:
    title, knoten, kanten, notizen, out = parse_spec(spec_path)
    drawio_xml = mk_drawio(title, knoten, kanten, notizen, Path(out).name)
    preview_svg = mk_preview_svg(title, knoten, kanten, notizen)
    hybrid = schreibe_ausgaben(REPO_ROOT, out, drawio_xml, preview_svg)
    try:
        gezeigt = hybrid.relative_to(REPO_ROOT)
    except ValueError:  # pragma: no cover
        gezeigt = hybrid
    print(f"  OK {gezeigt}")


def main(argv: list[str], repo_root: Path | None = None) -> int:
    global REPO_ROOT
    REPO_ROOT = Path(repo_root) if repo_root is not None else Path.cwd()

    p = argparse.ArgumentParser(
        prog="edu-diagramm flow",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
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


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main(sys.argv))
