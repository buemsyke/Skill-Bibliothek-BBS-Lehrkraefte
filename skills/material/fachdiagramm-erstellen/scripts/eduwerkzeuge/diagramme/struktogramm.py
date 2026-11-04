#!/usr/bin/env python3
"""
struktogramm — Nassi-Shneiderman-Diagramme (draw.io + SVG).

Struktogramme bestehen aus ineinander geschachtelten Kästen ohne Sprünge. Der
Generator berechnet die Schachtelung selbst; in der Spec steht nur die
Struktur des Algorithmus.

YAML-Spec:
  title: "Struktogramm: Wartung durchführen"
  type: struktogramm
  out: lessons/02_.../diagrams/02_v01_nsd_wartung
  breite: 460                       # optionale Gesamtbreite (Default 460)
  blocks:
    - "Anlage abschalten"                       # Kurzform: Anweisung
    - { typ: anweisung, text: "5 Minuten warten" }
    - typ: verzweigung
      bedingung: "temperatur > 55.0"
      ja:   ["Druck prüfen"]
      nein: ["mit Filterprüfung weiter"]        # leere Liste = einseitig
    - typ: kopfschleife                          # solange … tue (while)
      bedingung: "solange messung <= 3"
      rumpf:
        - "Temperatur messen"
        - "messung um 1 erhöhen"
    - typ: fussschleife                          # tue … solange (do-while)
      bedingung: "solange filter verschmutzt"
      rumpf: ["Filter sichtprüfen"]
    - { typ: aufruf, text: "mittelwert() aufrufen" }   # Unterprogrammaufruf

Unterstützte Blocktypen: ``anweisung``, ``verzweigung``, ``kopfschleife``,
``fussschleife``, ``aufruf``. Statt ``ja``/``nein`` sind auch ``dann``/``sonst``
erlaubt; die Beschriftung der Zweige lässt sich über ``ja_label``/``nein_label``
ändern (z. B. für Fallunterscheidungen mit anderen Wörtern).

``out:`` ist relativ zu ``repo_root`` (Default: aktuelles Arbeitsverzeichnis).
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("PyYAML benoetigt: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

from ._common import mk_mxfile, mk_svg, schreibe_ausgaben, text_breite, xml_escape, zeilen

# Basisverzeichnis für relative out:-Pfade. Wird in main() gesetzt.
REPO_ROOT = Path.cwd()

# Layout
MARGIN = 30
BREITE_DEFAULT = 460

FS = 13.0             # Grundschriftgröße
FS_KLEIN = 11.5       # ja/nein-Beschriftung
ZEILE_H = 18
TEXT_PAD_Y = 11
TEXT_PAD_X = 9
ANW_MIN_H = 40

VERZW_KOPF_H = 66
SCHLEIFE_KOPF_H = 32
INDENT = 22
AUFRUF_RAND = 8       # Abstand der senkrechten Doppellinien beim Unterprogrammaufruf

RAHMEN = "#333333"
FUELLUNG = "#ffffff"
FUELLUNG_BEDINGUNG = "#f5f5f5"


# -------------------- Zeichen-Primitive --------------------
@dataclass
class Rechteck:
    x: float
    y: float
    w: float
    h: float
    fuellung: str = FUELLUNG


@dataclass
class Linie:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Text:
    x: float
    y: float               # vertikale Mitte der Zeile
    text: str
    anker: str = "middle"  # start | middle | end
    size: float = FS
    fett: bool = False


Primitiv = Rechteck | Linie | Text


# -------------------- Textumbruch --------------------
def umbruch(text: str, max_breite: float, size: float = FS) -> list[str]:
    """Bricht Text auf die verfügbare Kastenbreite um (\\n bleibt harter Umbruch)."""
    ergebnis: list[str] = []
    for absatz in zeilen(text):
        worte = absatz.split()
        if not worte:
            ergebnis.append("")
            continue
        aktuell = worte[0]
        for wort in worte[1:]:
            probe = f"{aktuell} {wort}"
            if text_breite(probe, size) <= max_breite:
                aktuell = probe
            else:
                ergebnis.append(aktuell)
                aktuell = wort
        ergebnis.append(aktuell)
    return ergebnis or [""]


# -------------------- Spec normalisieren --------------------
def normalisiere(block) -> dict:
    """Kurzform (String) → Anweisungs-Dict; vereinheitlicht Schlüsselnamen."""
    if isinstance(block, str):
        return {"typ": "anweisung", "text": block}
    if not isinstance(block, dict):
        raise ValueError(f"Unbekannter Block: {block!r}")
    b = dict(block)
    b["typ"] = str(b.get("typ", "anweisung")).lower()
    if b["typ"] == "verzweigung":
        b["ja"] = [normalisiere(x) for x in (b.get("ja") or b.get("dann") or [])]
        b["nein"] = [normalisiere(x) for x in (b.get("nein") or b.get("sonst") or [])]
    elif b["typ"] in ("kopfschleife", "fussschleife"):
        b["rumpf"] = [normalisiere(x) for x in (b.get("rumpf") or [])]
    return b


# -------------------- Höhenberechnung --------------------
def hoehe_block(b: dict, w: float) -> float:
    typ = b["typ"]
    if typ in ("anweisung", "aufruf"):
        rand = TEXT_PAD_X + (AUFRUF_RAND if typ == "aufruf" else 0)
        n = len(umbruch(str(b.get("text", "")), w - 2 * rand))
        return max(ANW_MIN_H, 2 * TEXT_PAD_Y + n * ZEILE_H)
    if typ == "verzweigung":
        links = w / 2
        return VERZW_KOPF_H + max(
            hoehe_liste(b["ja"], links), hoehe_liste(b["nein"], w - links)
        )
    if typ == "kopfschleife":
        return SCHLEIFE_KOPF_H + hoehe_liste(b["rumpf"], w - INDENT)
    if typ == "fussschleife":
        return hoehe_liste(b["rumpf"], w - INDENT) + SCHLEIFE_KOPF_H
    raise ValueError(f"Unbekannter Blocktyp: {typ!r}")


def hoehe_liste(blocks: list[dict], w: float) -> float:
    if not blocks:
        return ANW_MIN_H          # leerer Zweig bleibt als leerer Kasten sichtbar
    return sum(hoehe_block(b, w) for b in blocks)


# -------------------- Zeichnen --------------------
class Zeichner:
    """Sammelt Zeichen-Primitive; die Ausgabeformate entstehen daraus."""

    def __init__(self) -> None:
        self.teile: list[Primitiv] = []

    def rect(self, x, y, w, h, fuellung=FUELLUNG) -> None:
        self.teile.append(Rechteck(x, y, w, h, fuellung))

    def line(self, x1, y1, x2, y2) -> None:
        self.teile.append(Linie(x1, y1, x2, y2))

    def text(self, x, y, s, anker="middle", size=FS, fett=False) -> None:
        if s:
            self.teile.append(Text(x, y, s, anker, size, fett))

    def mehrzeilig(self, x, y_mitte, breite, texte: list[str], anker="middle", size=FS) -> None:
        y = y_mitte - (len(texte) - 1) * ZEILE_H / 2
        for t in texte:
            self.text(x, y, t, anker, size)
            y += ZEILE_H

    # -- Blöcke ------------------------------------------------------
    def block(self, b: dict, x: float, y: float, w: float) -> float:
        typ = b["typ"]
        h = hoehe_block(b, w)
        if typ == "anweisung":
            self.rect(x, y, w, h)
            self.mehrzeilig(
                x + w / 2, y + h / 2, w, umbruch(str(b.get("text", "")), w - 2 * TEXT_PAD_X)
            )
        elif typ == "aufruf":
            self.rect(x, y, w, h)
            self.line(x + AUFRUF_RAND, y, x + AUFRUF_RAND, y + h)
            self.line(x + w - AUFRUF_RAND, y, x + w - AUFRUF_RAND, y + h)
            self.mehrzeilig(
                x + w / 2,
                y + h / 2,
                w,
                umbruch(str(b.get("text", "")), w - 2 * (TEXT_PAD_X + AUFRUF_RAND)),
            )
        elif typ == "verzweigung":
            self.verzweigung(b, x, y, w, h)
        elif typ == "kopfschleife":
            self.kopfschleife(b, x, y, w, h)
        elif typ == "fussschleife":
            self.fussschleife(b, x, y, w, h)
        return h

    def liste(self, blocks: list[dict], x: float, y: float, w: float, h_gesamt: float) -> None:
        """Blockfolge stapeln und Restfläche als leeren Kasten schließen."""
        if not blocks:
            self.rect(x, y, w, h_gesamt)
            return
        cur = y
        for b in blocks:
            cur += self.block(b, x, cur, w)
        rest = y + h_gesamt - cur
        if rest > 0.5:
            self.rect(x, cur, w, rest)

    def verzweigung(self, b: dict, x: float, y: float, w: float, h: float) -> None:
        kopf = VERZW_KOPF_H
        teiler = x + w / 2
        self.rect(x, y, w, kopf, FUELLUNG_BEDINGUNG)
        # Diagonalen: von den oberen Ecken zum Teilungspunkt an der Kopfunterkante
        self.line(x, y, teiler, y + kopf)
        self.line(x + w, y, teiler, y + kopf)
        self.mehrzeilig(
            x + w / 2,
            y + kopf * 0.30,
            w,
            umbruch(str(b.get("bedingung", "")), w * 0.62),
        )
        self.text(
            x + TEXT_PAD_X, y + kopf - 11, str(b.get("ja_label", "ja")), "start", FS_KLEIN
        )
        self.text(
            x + w - TEXT_PAD_X, y + kopf - 11, str(b.get("nein_label", "nein")), "end", FS_KLEIN
        )
        rest = h - kopf
        self.liste(b["ja"], x, y + kopf, w / 2, rest)
        self.liste(b["nein"], teiler, y + kopf, w / 2, rest)

    def kopfschleife(self, b: dict, x: float, y: float, w: float, h: float) -> None:
        self.rect(x, y, w, h, FUELLUNG_BEDINGUNG)
        self.text(
            x + TEXT_PAD_X, y + SCHLEIFE_KOPF_H / 2, str(b.get("bedingung", "")), "start", FS
        )
        self.liste(b["rumpf"], x + INDENT, y + SCHLEIFE_KOPF_H, w - INDENT, h - SCHLEIFE_KOPF_H)

    def fussschleife(self, b: dict, x: float, y: float, w: float, h: float) -> None:
        self.rect(x, y, w, h, FUELLUNG_BEDINGUNG)
        rumpf_h = h - SCHLEIFE_KOPF_H
        self.liste(b["rumpf"], x + INDENT, y, w - INDENT, rumpf_h)
        self.text(
            x + TEXT_PAD_X,
            y + rumpf_h + SCHLEIFE_KOPF_H / 2,
            str(b.get("bedingung", "")),
            "start",
            FS,
        )


# -------------------- Spec lesen --------------------
def parse_spec(path: Path) -> tuple[str, list[dict], float, str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    title = data["title"]
    out = data["out"]
    breite = float(data.get("breite", BREITE_DEFAULT))
    blocks = [normalisiere(b) for b in (data.get("blocks") or [])]
    if not blocks:
        raise ValueError("struktogramm-Spec ohne 'blocks'.")
    return title, blocks, breite, out


def zeichne(blocks: list[dict], breite: float) -> tuple[Zeichner, int, int]:
    z = Zeichner()
    h = hoehe_liste(blocks, breite)
    z.liste(blocks, MARGIN, MARGIN, breite, h)
    return z, int(breite + 2 * MARGIN), int(h + 2 * MARGIN)


# -------------------- Ausgabe: .drawio --------------------
_ALIGN = {"start": "left", "middle": "center", "end": "right"}


def mk_drawio(title: str, z: Zeichner, page_w: int, page_h: int, diagram_id: str) -> str:
    cells: list[str] = []
    for i, t in enumerate(z.teile):
        if isinstance(t, Rechteck):
            cells.append(
                f'<mxCell id="r{i}" value="" style="rounded=0;html=1;fillColor={t.fuellung};'
                f'strokeColor={RAHMEN};strokeWidth=1.5;" vertex="1" parent="1">'
                f'<mxGeometry x="{t.x:.0f}" y="{t.y:.0f}" width="{t.w:.0f}" '
                f'height="{t.h:.0f}" as="geometry"/></mxCell>'
            )
        elif isinstance(t, Linie):
            cells.append(
                f'<mxCell id="l{i}" style="endArrow=none;html=1;rounded=0;'
                f'strokeColor={RAHMEN};strokeWidth=1.5;" edge="1" parent="1">'
                '<mxGeometry relative="1" as="geometry">'
                f'<mxPoint x="{t.x1:.0f}" y="{t.y1:.0f}" as="sourcePoint"/>'
                f'<mxPoint x="{t.x2:.0f}" y="{t.y2:.0f}" as="targetPoint"/>'
                "</mxGeometry></mxCell>"
            )
        else:
            bw = text_breite(t.text, t.size, fett=t.fett) + 14
            if t.anker == "start":
                bx = t.x - 4
            elif t.anker == "end":
                bx = t.x - bw + 4
            else:
                bx = t.x - bw / 2
            stil = (
                "text;html=1;strokeColor=none;fillColor=none;verticalAlign=middle;"
                f"align={_ALIGN[t.anker]};fontSize={t.size:g};"
                + ("fontStyle=1;" if t.fett else "")
            )
            cells.append(
                f'<mxCell id="t{i}" value="{xml_escape(t.text)}" style="{stil}" '
                f'vertex="1" parent="1"><mxGeometry x="{bx:.0f}" y="{t.y - 10:.0f}" '
                f'width="{bw:.0f}" height="20" as="geometry"/></mxCell>'
            )
    return mk_mxfile(cells, page_w, page_h, title, diagram_id)


# -------------------- Ausgabe: preview.svg --------------------
SVG_STYLE = f"""
    .nsd-box {{ stroke: {RAHMEN}; stroke-width: 1.5; }}
    .nsd-line {{ stroke: {RAHMEN}; stroke-width: 1.5; }}
    .nsd-text {{ fill: #000; }}
"""


def mk_preview_svg(title: str, z: Zeichner, page_w: int, page_h: int) -> str:
    parts: list[str] = []
    for t in z.teile:
        if isinstance(t, Rechteck):
            parts.append(
                f'  <rect class="nsd-box" fill="{t.fuellung}" x="{t.x:.0f}" y="{t.y:.0f}" '
                f'width="{t.w:.0f}" height="{t.h:.0f}"/>'
            )
        elif isinstance(t, Linie):
            parts.append(
                f'  <line class="nsd-line" x1="{t.x1:.0f}" y1="{t.y1:.0f}" '
                f'x2="{t.x2:.0f}" y2="{t.y2:.0f}"/>'
            )
        else:
            fett = ' font-weight="bold"' if t.fett else ""
            parts.append(
                f'  <text class="nsd-text" x="{t.x:.0f}" y="{t.y + t.size * 0.36:.1f}" '
                f'text-anchor="{t.anker}" font-size="{t.size:g}"{fett}>'
                f"{xml_escape(t.text)}</text>"
            )
    return mk_svg(parts, page_w, page_h, title, SVG_STYLE)


# -------------------- Ablauf --------------------
def process_spec(spec_path: Path) -> None:
    title, blocks, breite, out = parse_spec(spec_path)
    z, page_w, page_h = zeichne(blocks, breite)
    drawio_xml = mk_drawio(title, z, page_w, page_h, Path(out).name)
    preview_svg = mk_preview_svg(title, z, page_w, page_h)
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
        prog="edu-diagramm struktogramm",
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
