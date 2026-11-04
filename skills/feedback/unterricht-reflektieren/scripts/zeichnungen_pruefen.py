#!/usr/bin/env python3
"""zeichnungen_pruefen – Zeichnungen aus Zeichen, Mermaid und fehlerhafte SVG finden (lokal).

Zeichnungen in Artefakten der Bibliothek entstehen als SVG aus einer Spec mit den Zeichen-Skills
(Skill-Vertrag Abschn. 3, „Zeichnungen“). Dieses Skript findet, was dagegen verstößt:

  ❌ ASCII-Zeichnung   mindestens drei aufeinanderfolgende Zeilen mit Rahmen- oder Pfeilzeichen
                      (┌─┐│└┘├┤ ═ ║ ▲▼◄►) bzw. in Codeblöcken mit Zeichengrafik aus +---+, -->, |
                      (Kastengrafik, Struktogramm, GRAFCET, Funktionsplan, Ablauf aus Zeichen)
  ⚠ Mermaid           ```mermaid-Block – als Entwurf zulässig, für die Ausgabe als SVG erzeugen

Eingebundene SVG (`![…](abbildungen/….svg)`, relativ zur Markdown-Datei) und direkt übergebene
SVG-Dateien werden zusätzlich geöffnet:

  Herkunft   erzeugt (draw.io-Inhalt, `.drawio.svg`/`.drawio` oder Spec `.yaml` daneben bzw. in
             `schema/`, `diagramme/`, `specs/`; per Code mit matplotlib), Fremdsoftware (Kennung
             z. B. Inkscape, Export aus Präsentation) oder ⚠ ohne Spec und Kennung – vermutlich von
             Hand geschrieben; ⚠ Datei fehlt (noch nicht erzeugt?)
  Geometrie  ❌ Text über Text · Form über Text · Linie durch Text (außer freigestellt, d. h. von
             einer später gemalten deckenden Fläche verdeckt) · Text ragt aus seinem Kasten ·
             Element außerhalb des Bildes; ⚠ schräge Leitungen (nur bei SVG, die nicht erzeugt sind –
             Diagonalen im Struktogramm oder Chen-Modell sind Notation)

Die Textbreite wird geschätzt wie in den Generatoren (0,55 bzw. fett 0,6 der Schriftgröße je
Zeichen); Drehungen werden nicht ausgewertet. Nicht gemeldet werden Verzeichnisbäume (├── / └──),
Markdown-Tabellen und Programmcode ohne Zeichengrafik. Ein GRAFCET oder Struktogramm darf
zusätzlich als Text-Tabelle stehen (Zweitkorrektur) – die Zeichnung selbst ist SVG.

Aufruf:
    python3 zeichnungen_pruefen.py DATEI.md|BILD.svg… [--json]

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

RAHMEN = re.compile("[─-╿▲▶►▼◀◄]")
VERZEICHNISBAUM = re.compile(r"^\s*(?:│\s*)*(?:├──|└──|│)")
ASCII_GRAFIK = re.compile(r"\+-{2,}|-{2,}\+|-{2,}>|<-{2,}|={2,}>|^\s*[+|]\s*$")
SEITENWAND = re.compile(r"^\s*\|.*\|\s*$")          # | … | nur als Fortsetzung einer Kastengrafik
TEXTSPRACHEN = {"markdown", "md", "html", "xml", "yaml", "yml", "json", "csv"}
FENCE = re.compile(r"^\s*(```+|~~~+)\s*([\w-]*)")
MIN_ZEILEN = 3


def _zeichnungszeile(zeile: str, im_code: bool, sprache: str, laufend: bool) -> bool:
    if len(RAHMEN.findall(zeile)) >= 2 or (RAHMEN.search(zeile) and len(zeile.strip()) <= 3):
        return True
    if not im_code or sprache in TEXTSPRACHEN:
        return False                                     # Tabellen, Kommentare, Vorlagen
    return bool(ASCII_GRAFIK.search(zeile)) or (laufend and bool(SEITENWAND.match(zeile)))


def finde(text: str) -> list[dict]:
    """Liste der Funde: {art: 'ascii'|'mermaid', zeile, bis, hinweis}."""
    funde: list[dict] = []
    zeilen = text.splitlines()
    im_code, sprache, block = False, "", []          # block: Zeilennummern der laufenden Zeichnung

    def abschliessen() -> None:
        if len(block) >= MIN_ZEILEN:
            inhalt = [zeilen[n - 1] for n in block]
            if not all(VERZEICHNISBAUM.match(z) or not z.strip() for z in inhalt):
                funde.append({"art": "ascii", "zeile": block[0], "bis": block[-1],
                              "hinweis": f"Zeichnung aus Zeichen (Z. {block[0]}–{block[-1]}) – als SVG mit dem "
                                         "passenden Zeichen-Skill erzeugen und einbinden"})
        block.clear()

    for nr, zeile in enumerate(zeilen, start=1):
        m = FENCE.match(zeile)
        if m:
            abschliessen()
            if not im_code:
                im_code, sprache = True, m.group(2).lower()
                if sprache == "mermaid":
                    funde.append({"art": "mermaid", "zeile": nr, "bis": nr,
                                  "hinweis": f"Mermaid-Block (Z. {nr}) – für die Ausgabe als SVG erzeugen"})
            else:
                im_code, sprache = False, ""
            continue
        if sprache == "mermaid":
            continue
        if _zeichnungszeile(zeile, im_code, sprache, bool(block)):
            block.append(nr)
        elif block and not zeile.strip() and im_code:
            continue                                     # Leerzeile innerhalb einer Codezeichnung
        else:
            abschliessen()
    abschliessen()
    return funde


# ─────────────────────── eingebundene SVG: Herkunft und Geometrie ───────────────────────

BILD = re.compile(r"!\[[^\]]*\]\(\s*<?([^)\s>]+?\.svg)>?(?:\s+\"[^\"]*\")?\s*\)", re.IGNORECASE)
SPEC_ORTE = (".", "schema", "diagramme", "specs", "../schema", "../diagramme", "../specs")
PER_CODE = ((re.compile(r"matplotlib"), "per Code (matplotlib)"),)
FREMDSOFTWARE = ((re.compile(r"inkscape|sodipodi"), "Inkscape"), (re.compile(r"Adobe Illustrator"), "Illustrator"),
                 (re.compile(r"<symbol[^>]*\bid=\"glyph"), "Export aus Präsentation bzw. PDF"),
                 (re.compile(r"Generator:|Created with"), "Fachsoftware"))
UEBERSPRINGEN = {"defs", "marker", "symbol", "clipPath", "mask", "pattern", "title", "desc", "metadata",
                 "style", "linearGradient", "radialGradient", "filter", "foreignObject", "script", "image", "use"}
VERERBT = ("fill", "stroke", "stroke-width", "font-size", "font-weight", "text-anchor", "dominant-baseline",
           "display", "visibility", "opacity", "fill-opacity")
ZAHL = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
BREITE_NORMAL, BREITE_FETT = 0.55, 0.60     # wie die Generatoren der eduwerkzeuge
LINIE_MIN = 1.5      # sichtbare Länge einer Linie im Textkasten, ab der sie stört (px)
UEBERLAUF_MIN = 1.0  # so weit darf ein Text über seinen Kasten hinausragen (px)
SCHRAEG_GRAD, SCHRAEG_LAENGE = 2.0, 20.0
SYMBOL_MAX = 60.0    # Linien innerhalb so kleiner Formen gehören zum Symbol (Kreuz im Leuchtmelder)

Punkt = tuple[float, float]
Matrix = tuple[float, float, float, float, float, float]


@dataclass
class _Text:
    inhalt: str
    kasten: tuple[float, float, float, float]     # x0, y0, x1, y1
    folge: int


@dataclass
class _Form:
    punkte: list[Punkt]
    deckend: bool
    dunkel: bool
    rand: bool
    folge: int
    kasten: tuple[float, float, float, float] = (0, 0, 0, 0)
    flaeche: float = 0.0

    def __post_init__(self) -> None:
        xs, ys = [p[0] for p in self.punkte], [p[1] for p in self.punkte]
        self.kasten = (min(xs), min(ys), max(xs), max(ys))
        self.flaeche = abs(sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(self.punkte, self.punkte[1:] + self.punkte[:1]))) / 2


@dataclass
class _Strecke:
    a: Punkt
    b: Punkt
    folge: int
    form: int | None = None      # Index der Form, deren Rand die Strecke ist
    offen: bool = False          # Teil einer Linie (line, polyline, offener Pfad)


@dataclass
class _Bild:
    texte: list[_Text] = field(default_factory=list)
    formen: list[_Form] = field(default_factory=list)
    strecken: list[_Strecke] = field(default_factory=list)
    rahmen: tuple[float, float, float, float] | None = None
    folge: int = 0
    gedreht: int = 0


def _tag(el: ET.Element) -> str:
    return el.tag.rsplit("}", 1)[-1] if isinstance(el.tag, str) else ""


def _zahl(wert: str | None, fs: float = 16.0, standard: float = 0.0) -> float:
    m = re.match(rf"\s*({ZAHL})\s*(px|em|pt)?", wert or "")
    if not m:
        return standard
    z = float(m.group(1))
    return z * fs if m.group(2) == "em" else z * 4 / 3 if m.group(2) == "pt" else z


def _deklarationen(text: str) -> dict[str, str]:
    return {k.strip(): v.strip() for k, _, v in (d.partition(":") for d in text.split(";")) if v.strip()}


def _css(wurzel: ET.Element) -> list[tuple[str | None, set[str], dict[str, str], int]]:
    """Regeln aus <style>: Element, .klasse, element.klasse (Spezifität, Reihenfolge)."""
    regeln = []
    for el in wurzel.iter():
        if _tag(el) == "style" and el.text:
            css = re.sub(r"/\*.*?\*/", "", el.text, flags=re.S)
            for selektoren, block in re.findall(r"([^{}]+)\{([^}]*)\}", css):
                eig = _deklarationen(block)
                for sel in selektoren.split(","):
                    m = re.fullmatch(r"([a-zA-Z]*)((?:\.[\w-]+)*)", sel.strip())
                    if m and (m.group(1) or m.group(2)):
                        regeln.append((m.group(1) or None, set(m.group(2).split(".")[1:]), eig,
                                       (1 if m.group(1) else 0) + 10 * m.group(2).count(".")))
    return regeln


def _eigenschaften(el: ET.Element, erbe: dict[str, str], regeln: list) -> dict[str, str]:
    eig = {k: v for k, v in erbe.items() if k in VERERBT}
    eig.update({k: v for k, v in el.attrib.items() if not k.startswith("{")})
    klassen = set((el.get("class") or "").split())
    passend = [(spez, i, r[2]) for i, r in enumerate(regeln) for spez in [r[3]]
               if (r[0] is None or r[0] == _tag(el)) and r[1] <= klassen and (r[0] or r[1])]
    for _, _, dekl in sorted(passend, key=lambda t: (t[0], t[1])):
        eig.update(dekl)
    eig.update(_deklarationen(el.get("style") or ""))
    kurz = eig.pop("font", "")                       # Kurzform „bold 9px 'DejaVu Sans'“ (matplotlib)
    if kurz:
        m = re.search(rf"({ZAHL}(?:px|pt|em)?)\s", kurz + " ")
        if m:
            eig["font-size"] = m.group(1)
        if re.search(r"\b(bold|[6-9]00)\b", kurz):
            eig["font-weight"] = "bold"
    return eig


def _mal(a: Matrix, b: Matrix) -> Matrix:
    return (a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1], a[0] * b[2] + a[2] * b[3],
            a[1] * b[2] + a[3] * b[3], a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5])


def _transform(text: str) -> Matrix | None:
    """Nur Verschieben und Skalieren; None bei Drehung oder Scherung (wird nicht ausgewertet)."""
    m: Matrix = (1, 0, 0, 1, 0, 0)
    for name, args in re.findall(r"(\w+)\s*\(([^)]*)\)", text):
        w = [float(x) for x in re.findall(ZAHL, args)]
        if name == "translate" and w:
            t: Matrix = (1, 0, 0, 1, w[0], w[1] if len(w) > 1 else 0)
        elif name == "scale" and w:
            t = (w[0], 0, 0, w[1] if len(w) > 1 else w[0], 0, 0)
        elif name == "matrix" and len(w) == 6:
            t = tuple(w)  # type: ignore[assignment]
        elif name == "rotate" and w and abs(w[0]) % 360 < 1e-9:
            continue
        else:
            return None
        m = _mal(m, t)
    return None if abs(m[1]) > 1e-9 or abs(m[2]) > 1e-9 else m


def _abb(m: Matrix, p: Punkt) -> Punkt:
    return (m[0] * p[0] + m[2] * p[1] + m[4], m[1] * p[0] + m[3] * p[1] + m[5])


def _farbe(wert: str | None) -> tuple[bool, float]:
    """(sichtbar, Helligkeit 0…1) einer Füllung oder Linie."""
    w = (wert or "").strip().lower()
    if not w or w in ("none", "transparent"):
        return False, 1.0
    namen = {"black": "#000", "white": "#fff", "gray": "#808080", "grey": "#808080", "red": "#f00",
             "blue": "#00f", "green": "#008000", "currentcolor": "#000"}
    w = namen.get(w, w)
    if w.startswith("url("):
        return True, 0.5
    m = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6})", w)
    if m:
        h = m.group(1)
        h = "".join(c * 2 for c in h) if len(h) == 3 else h
        r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
        return True, 0.299 * r + 0.587 * g + 0.114 * b
    m = re.fullmatch(rf"rgba?\(\s*({ZAHL})\s*,\s*({ZAHL})\s*,\s*({ZAHL})", w)
    if m:
        r, g, b = (float(x) / 255 for x in m.groups())
        return True, 0.299 * r + 0.587 * g + 0.114 * b
    return True, 0.5


def _pfad(d: str) -> list[tuple[list[Punkt], bool]]:
    """Teilpfade als Punktfolgen (Kurven und Bögen angenähert) mit Kennung „geschlossen“."""
    teile = re.findall(rf"([MmLlHhVvCcSsQqTtAaZz])|({ZAHL})", d)
    werte: list[str | float] = [c if c else float(z) for c, z in teile]
    pfade: list[tuple[list[Punkt], bool]] = []
    pkte: list[Punkt] = []
    cur = start = (0.0, 0.0)
    cmd, i, ktrl = "", 0, None

    def nimm(n: int) -> list[float] | None:
        nonlocal i
        if i + n > len(werte) or any(isinstance(werte[j], str) for j in range(i, i + n)):
            return None
        w = [float(werte[j]) for j in range(i, i + n)]   # type: ignore[arg-type]
        i += n
        return w

    def kurve(pts: list[Punkt]) -> None:            # Bézier in 8 Stücke
        n = len(pts) - 1
        for s in range(1, 9):
            t = s / 8
            q = list(pts)
            for k in range(n):
                q = [(q[j][0] + (q[j + 1][0] - q[j][0]) * t, q[j][1] + (q[j + 1][1] - q[j][1]) * t)
                     for j in range(len(q) - 1)]
            pkte.append(q[0])

    def abschluss(geschlossen: bool) -> None:
        nonlocal pkte
        if len(pkte) > 1:
            pfade.append((pkte, geschlossen))
        pkte = []

    while i < len(werte):
        if isinstance(werte[i], str):
            cmd = werte[i]  # type: ignore[assignment]
            i += 1
            if cmd in "Zz":
                if pkte:
                    abschluss(True)
                cur = start
                pkte = [cur]
                continue
        rel = cmd.islower()
        c = cmd.upper()
        n = {"M": 2, "L": 2, "H": 1, "V": 1, "C": 6, "S": 4, "Q": 4, "T": 2, "A": 7}.get(c)
        w = nimm(n) if n else None
        if w is None:
            break
        ox, oy = cur if rel else (0.0, 0.0)
        if c == "M":
            abschluss(False)
            cur = start = (w[0] + ox, w[1] + oy)
            pkte = [cur]
            cmd = "l" if rel else "L"
            ktrl = None
            continue
        if c in "LHV":
            cur = ((w[0] + ox, w[1] + oy) if c == "L" else
                   (w[0] + (cur[0] if rel else 0), cur[1]) if c == "H" else (cur[0], w[0] + (cur[1] if rel else 0)))
            pkte.append(cur)
            ktrl = None
        elif c in "CS":
            if c == "C":
                k1, k2, ende = (w[0] + ox, w[1] + oy), (w[2] + ox, w[3] + oy), (w[4] + ox, w[5] + oy)
            else:
                k1 = (2 * cur[0] - ktrl[0], 2 * cur[1] - ktrl[1]) if ktrl else cur
                k2, ende = (w[0] + ox, w[1] + oy), (w[2] + ox, w[3] + oy)
            kurve([cur, k1, k2, ende])
            ktrl, cur = k2, ende
        elif c in "QT":
            if c == "Q":
                k1, ende = (w[0] + ox, w[1] + oy), (w[2] + ox, w[3] + oy)
            else:
                k1, ende = ((2 * cur[0] - ktrl[0], 2 * cur[1] - ktrl[1]) if ktrl else cur), (w[0] + ox, w[1] + oy)
            kurve([cur, k1, ende])
            ktrl, cur = k1, ende
        else:                                        # Bogen: Mittelpunktform (SVG 1.1, F.6.5)
            ende = (w[5] + ox, w[6] + oy)
            pkte += _bogen(cur, ende, abs(w[0]), abs(w[1]), math.radians(w[2]), bool(w[3]), bool(w[4]))
            cur, ktrl = ende, None
    abschluss(False)
    return pfade


def _bogen(p1: Punkt, p2: Punkt, rx: float, ry: float, phi: float, gross: bool, positiv: bool) -> list[Punkt]:
    if rx < 1e-9 or ry < 1e-9 or p1 == p2:
        return [p2]
    c, s = math.cos(phi), math.sin(phi)
    dx, dy = (p1[0] - p2[0]) / 2, (p1[1] - p2[1]) / 2
    x1, y1 = c * dx + s * dy, -s * dx + c * dy
    lam = x1 ** 2 / rx ** 2 + y1 ** 2 / ry ** 2
    if lam > 1:
        rx, ry = rx * math.sqrt(lam), ry * math.sqrt(lam)
    zaehler = rx ** 2 * ry ** 2 - rx ** 2 * y1 ** 2 - ry ** 2 * x1 ** 2
    f = math.sqrt(max(0.0, zaehler / (rx ** 2 * y1 ** 2 + ry ** 2 * x1 ** 2))) * (-1 if gross == positiv else 1)
    cx1, cy1 = f * rx * y1 / ry, -f * ry * x1 / rx
    cx, cy = c * cx1 - s * cy1 + (p1[0] + p2[0]) / 2, s * cx1 + c * cy1 + (p1[1] + p2[1]) / 2
    t1 = math.atan2((y1 - cy1) / ry, (x1 - cx1) / rx)
    dt = math.atan2((-y1 - cy1) / ry, (-x1 - cx1) / rx) - t1
    if positiv and dt < 0:
        dt += 2 * math.pi
    elif not positiv and dt > 0:
        dt -= 2 * math.pi
    return [(cx + rx * math.cos(t1 + dt * k / 12) * c - ry * math.sin(t1 + dt * k / 12) * s,
             cy + rx * math.cos(t1 + dt * k / 12) * s + ry * math.sin(t1 + dt * k / 12) * c) for k in range(1, 13)]


def _ellipse(cx: float, cy: float, rx: float, ry: float) -> list[Punkt]:
    return [(cx + rx * math.cos(2 * math.pi * k / 32), cy + ry * math.sin(2 * math.pi * k / 32)) for k in range(32)]


def _textzeilen(el: ET.Element, fs: float) -> list[tuple[float, float, str]]:
    """Zeilen eines <text> mit eigenen tspan-Positionen (x, y, dy)."""
    def erste(w: str | None) -> float:
        z = re.findall(ZAHL, w or "")
        return float(z[0]) if z else 0.0

    zeilen, akt = [], [erste(el.get("x")), erste(el.get("y")), el.text or ""]
    for kind in el:
        if _tag(kind) == "tspan" and any(kind.get(a) is not None for a in ("x", "y", "dy")):
            zeilen.append(tuple(akt))
            nx = erste(kind.get("x")) if kind.get("x") is not None else akt[0]
            ny = erste(kind.get("y")) if kind.get("y") is not None else akt[1]
            akt = [nx, ny + _zahl(kind.get("dy"), fs), "".join(kind.itertext())]
        else:
            akt[2] += "".join(kind.itertext())
        akt[2] += kind.tail or ""
    zeilen.append(tuple(akt))
    return [(x, y, " ".join(s.split())) for x, y, s in zeilen if s.strip()]


def _sammle(el: ET.Element, erbe: dict[str, str], ctm: Matrix, regeln: list, bild: _Bild) -> None:
    tag = _tag(el)
    if tag in UEBERSPRINGEN:
        return
    eig = _eigenschaften(el, erbe, regeln)
    if eig.get("display") == "none" or eig.get("visibility") == "hidden":
        return
    if el.get("transform"):
        t = _transform(el.get("transform", ""))
        if t is None:
            bild.gedreht += 1
            return
        ctm = _mal(ctm, t)
    if tag == "svg":                                 # verschachteltes <svg>
        ctm = _mal(ctm, (1, 0, 0, 1, _zahl(el.get("x")), _zahl(el.get("y"))))
    fs = _zahl(eig.get("font-size"), standard=16.0) * math.sqrt(abs(ctm[0] * ctm[3]))
    bild.folge += 1
    folge = bild.folge
    deckkraft = _zahl(eig.get("opacity"), standard=1.0) * _zahl(eig.get("fill-opacity"), standard=1.0)
    gefuellt, hell = _farbe(eig.get("fill", "black"))
    linie, _ = _farbe(eig.get("stroke"))
    linie = linie and _zahl(eig.get("stroke-width"), standard=1.0) > 0

    def form(punkte: list[Punkt]) -> None:
        pts = [_abb(ctm, p) for p in punkte]
        if len(pts) < 3:
            return
        f = _Form(pts, gefuellt and deckkraft >= 0.9 and not eig.get("fill", "").startswith("url("),
                  gefuellt and hell < 0.6, linie, folge)
        if f.flaeche < 1e-6:
            return
        bild.formen.append(f)
        if linie:
            idx = len(bild.formen) - 1
            bild.strecken += [_Strecke(a, b, folge, idx) for a, b in zip(pts, pts[1:] + pts[:1])]

    def offen(punkte: list[Punkt]) -> None:
        if linie:
            pts = [_abb(ctm, p) for p in punkte]
            bild.strecken += [_Strecke(a, b, folge, None, True) for a, b in zip(pts, pts[1:])]

    g = lambda a: _zahl(el.get(a))  # noqa: E731
    if tag == "rect" and g("width") > 0 and g("height") > 0:
        x, y, w, h = g("x"), g("y"), g("width"), g("height")
        form([(x, y), (x + w, y), (x + w, y + h), (x, y + h)])
    elif tag == "circle" and g("r") > 0:
        form(_ellipse(g("cx"), g("cy"), g("r"), g("r")))
    elif tag == "ellipse" and g("rx") > 0 and g("ry") > 0:
        form(_ellipse(g("cx"), g("cy"), g("rx"), g("ry")))
    elif tag in ("polygon", "polyline"):
        z = [float(v) for v in re.findall(ZAHL, el.get("points", ""))]
        pts = list(zip(z[0::2], z[1::2]))
        (form if tag == "polygon" else offen)(pts)
    elif tag == "line":
        offen([(g("x1"), g("y1")), (g("x2"), g("y2"))])
    elif tag == "path":
        for pts, geschlossen in _pfad(el.get("d", "")):
            (form if geschlossen else offen)(pts)
    elif tag == "text":
        fett = eig.get("font-weight", "normal") in ("bold", "bolder", "600", "700", "800", "900")
        anker = eig.get("text-anchor", "start")
        grundlinie = eig.get("dominant-baseline", "")
        roh_fs = _zahl(eig.get("font-size"), standard=16.0)
        for x, y, inhalt in _textzeilen(el, roh_fs):
            w = len(inhalt) * roh_fs * (BREITE_FETT if fett else BREITE_NORMAL)
            x0 = x - w / 2 if anker == "middle" else x - w if anker == "end" else x
            y0, y1 = ((y - 0.48 * roh_fs, y + 0.48 * roh_fs) if grundlinie in ("middle", "central") else
                      (y, y + roh_fs) if grundlinie in ("hanging", "text-before-edge") else
                      (y - 0.75 * roh_fs, y + 0.2 * roh_fs))
            a, b = _abb(ctm, (x0, y0)), _abb(ctm, (x0 + w, y1))
            bild.texte.append(_Text(inhalt, (min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])), folge))
        return
    for kind in el:
        _sammle(kind, eig, ctm, regeln, bild)


def lies_svg(text: str) -> _Bild:
    wurzel = ET.fromstring(text)
    bild = _Bild()
    vb = [float(v) for v in re.findall(ZAHL, wurzel.get("viewBox", ""))]
    if len(vb) == 4:
        bild.rahmen = (vb[0], vb[1], vb[0] + vb[2], vb[1] + vb[3])
    else:
        bild.rahmen = (0.0, 0.0, _zahl(wurzel.get("width"), standard=0), _zahl(wurzel.get("height"), standard=0))
    regeln = _css(wurzel)
    eig = _eigenschaften(wurzel, {}, regeln)
    for kind in wurzel:
        _sammle(kind, eig, (1, 0, 0, 1, 0, 0), regeln, bild)
    return bild


def _innen(p: Punkt, pts: list[Punkt]) -> bool:
    drin = False
    for a, b in zip(pts, pts[1:] + pts[:1]):
        if (a[1] > p[1]) != (b[1] > p[1]) and p[0] < (b[0] - a[0]) * (p[1] - a[1]) / (b[1] - a[1]) + a[0]:
            drin = not drin
    return drin


def _abstand(p: Punkt, pts: list[Punkt]) -> float:
    best = math.inf
    for a, b in zip(pts, pts[1:] + pts[:1]):
        dx, dy = b[0] - a[0], b[1] - a[1]
        t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy or 1)))
        best = min(best, math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy))
    return best


def _schnitt(a: Punkt, b: Punkt, k: tuple[float, float, float, float]) -> tuple[Punkt, Punkt] | None:
    """Teil der Strecke a–b im Kasten k (Liang–Barsky)."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, a[0] - k[0]), (dx, k[2] - a[0]), (-dy, a[1] - k[1]), (dy, k[3] - a[1])):
        if abs(p) < 1e-12:
            if q < 0:
                return None
            continue
        r = q / p
        if p < 0:
            if r > t1:
                return None
            t0 = max(t0, r)
        else:
            if r < t0:
                return None
            t1 = min(t1, r)
    return (a[0] + t0 * dx, a[1] + t0 * dy), (a[0] + t1 * dx, a[1] + t1 * dy)


def _kurz(s: str, n: int = 32) -> str:
    return s if len(s) <= n else s[: n - 1] + "…"


def geometrie(bild: _Bild, erzeugt: bool = False) -> list[dict]:
    """Befunde {art, stufe, text} zu Überlagerungen, Überlauf, Bildrand und schrägen Linien."""
    befunde: list[dict] = []
    T, F, S = bild.texte, bild.formen, bild.strecken
    gross = [i for i, f in enumerate(F) if f.rand]

    def umgebend(t: _Text) -> int | None:
        m = ((t.kasten[0] + t.kasten[2]) / 2, (t.kasten[1] + t.kasten[3]) / 2)
        flaeche = (t.kasten[2] - t.kasten[0]) * (t.kasten[3] - t.kasten[1])
        kandidaten = [i for i in gross if F[i].folge < t.folge and F[i].flaeche >= flaeche
                      and F[i].kasten[0] <= m[0] <= F[i].kasten[2] and F[i].kasten[1] <= m[1] <= F[i].kasten[3]
                      and _innen(m, F[i].punkte)]
        return min(kandidaten, key=lambda i: F[i].flaeche) if kandidaten else None

    # Text über Text
    for i, t in enumerate(T):
        a = (t.kasten[0] + 1, t.kasten[1] + 1, t.kasten[2] - 1, t.kasten[3] - 1)
        for u in T[i + 1:]:
            if u.inhalt == t.inhalt and abs(u.kasten[0] - t.kasten[0]) < 0.5 and abs(u.kasten[1] - t.kasten[1]) < 0.5:
                continue
            b = (u.kasten[0] + 1, u.kasten[1] + 1, u.kasten[2] - 1, u.kasten[3] - 1)
            if min(a[2], b[2]) - max(a[0], b[0]) > 0.5 and min(a[3], b[3]) - max(a[1], b[1]) > 0.5:
                befunde.append({"art": "text_text", "stufe": "❌",
                                "text": f"„{_kurz(t.inhalt)}“ und „{_kurz(u.inhalt)}“ überlagern sich"})
    for t in T:
        k = (t.kasten[0] + 1.5, t.kasten[1] + 1, t.kasten[2] - 1.5, t.kasten[3] - 1)
        if k[2] <= k[0] or k[3] <= k[1]:
            continue
        rahmen_von = umgebend(t)
        # Text ragt aus seinem Kasten
        if rahmen_von is not None:
            f = F[rahmen_von]
            x0, y0, x1, y1 = t.kasten
            proben = [(x0 + (x1 - x0) * s / 8, y) for s in range(9) for y in (y0, y1)] + \
                     [(x, y0 + (y1 - y0) * s / 2) for s in range(3) for x in (x0, x1)]
            if any(not _innen(p, f.punkte) and _abstand(p, f.punkte) > UEBERLAUF_MIN for p in proben):
                befunde.append({"art": "text_ueberlauf", "stufe": "❌",
                                "text": f"„{_kurz(t.inhalt)}“ ragt aus seinem Kasten"})
        # Form über Text: dunkle Fläche auf dem Text oder deckende Fläche über ihm
        for j, f in enumerate(F):
            if j == rahmen_von or f.kasten[2] < k[0] or f.kasten[0] > k[2] or f.kasten[3] < k[1] or f.kasten[1] > k[3]:
                continue
            raster = [(k[0] + (k[2] - k[0]) * a / 6, k[1] + (k[3] - k[1]) * b / 2) for a in range(7) for b in range(3)]
            treffer = sum(_innen(p, f.punkte) for p in raster)
            umschliesst = treffer == len(raster)
            ueberlapp = (max(0.0, min(k[2], f.kasten[2]) - max(k[0], f.kasten[0])) *
                         max(0.0, min(k[3], f.kasten[3]) - max(k[1], f.kasten[1])))
            if (f.dunkel and ueberlapp >= 6 and not umschliesst) or (f.deckend and f.folge > t.folge and treffer >= 3):
                befunde.append({"art": "form_text", "stufe": "❌",
                                "text": f"eine Form liegt auf „{_kurz(t.inhalt)}“"})
                break
        # Linie durch Text (nicht der Rand des eigenen Kastens – das meldet der Überlauf)
        for s in S:
            if s.form is not None and s.form == rahmen_von:
                continue
            if max(s.a[0], s.b[0]) < k[0] or min(s.a[0], s.b[0]) > k[2] or max(s.a[1], s.b[1]) < k[1] \
                    or min(s.a[1], s.b[1]) > k[3]:
                continue
            teil = _schnitt(s.a, s.b, k)
            if teil is None:
                continue
            laenge = math.dist(*teil)
            if laenge < LINIE_MIN:
                continue
            n = max(2, int(laenge))
            frei = [f for f in F if f.deckend and f.folge > s.folge
                    and f.kasten[0] <= k[2] and f.kasten[2] >= k[0] and f.kasten[1] <= k[3] and f.kasten[3] >= k[1]]
            sichtbar = sum(1 for m in range(n + 1)
                           if not any(_innen((teil[0][0] + (teil[1][0] - teil[0][0]) * m / n,
                                              teil[0][1] + (teil[1][1] - teil[0][1]) * m / n), f.punkte) for f in frei))
            if laenge * sichtbar / (n + 1) >= LINIE_MIN:
                befunde.append({"art": "linie_text", "stufe": "❌",
                                "text": f"eine Linie läuft durch „{_kurz(t.inhalt)}“"})
                break
    # außerhalb des Bildes
    if bild.rahmen and bild.rahmen[2] > bild.rahmen[0]:
        r = bild.rahmen
        for t in T:
            if t.kasten[0] < r[0] - 2 or t.kasten[2] > r[2] + 2 or t.kasten[1] < r[1] - 2 or t.kasten[3] > r[3] + 2:
                befunde.append({"art": "ausserhalb", "stufe": "❌", "text": f"„{_kurz(t.inhalt)}“ ragt aus dem Bild"})
        aussen = sum(1 for f in F if f.kasten[0] < r[0] - 1 or f.kasten[2] > r[2] + 1
                     or f.kasten[1] < r[1] - 1 or f.kasten[3] > r[3] + 1)
        if aussen:
            befunde.append({"art": "ausserhalb", "stufe": "❌", "text": f"{aussen} Form(en) ragen aus dem Bild"})
    # schräge Leitungen – nur bei nicht erzeugten SVG (Diagonalen der Notation sind gewollt)
    if not erzeugt:
        klein = [f.kasten for f in F if max(f.kasten[2] - f.kasten[0], f.kasten[3] - f.kasten[1]) <= SYMBOL_MAX]

        def im_symbol(s: _Strecke) -> bool:
            return any(all(k[0] - 1 <= q[0] <= k[2] + 1 and k[1] - 1 <= q[1] <= k[3] + 1 for q in (s.a, s.b))
                       for k in klein)

        schraeg = 0
        for s in S:
            dx, dy = abs(s.b[0] - s.a[0]), abs(s.b[1] - s.a[1])
            if not s.offen or math.hypot(dx, dy) < SCHRAEG_LAENGE or im_symbol(s):
                continue
            if min(math.degrees(math.atan2(dy, dx or 1e-12)), math.degrees(math.atan2(dx, dy or 1e-12))) > SCHRAEG_GRAD:
                schraeg += 1
        if schraeg:
            befunde.append({"art": "schraeg", "stufe": "⚠",
                            "text": f"{schraeg} schräge Linie(n) – Leitungen waagerecht und senkrecht führen"})
    if bild.gedreht:
        befunde.append({"art": "gedreht", "stufe": "➖", "text": f"{bild.gedreht} gedrehte Gruppe(n) nicht geprüft"})
    return befunde


def herkunft(pfad: Path, text: str) -> tuple[str, str]:
    """('erzeugt' | 'fremd' | 'hand', Kennung) einer SVG-Datei."""
    if "<mxfile" in text or "&lt;mxfile" in text:
        return "erzeugt", "draw.io-Inhalt"
    stamm = pfad.name
    for endung in (".preview.svg", ".drawio.svg", ".svg"):
        if stamm.lower().endswith(endung):
            stamm = stamm[: -len(endung)]
            break
    for name in (f"{stamm}.drawio.svg", f"{stamm}.drawio"):
        if name != pfad.name and (pfad.parent / name).is_file():
            return "erzeugt", f"{name} daneben"
    for ort in SPEC_ORTE:
        for endung in (".yaml", ".yml"):
            if (pfad.parent / ort / f"{stamm}{endung}").is_file():
                return "erzeugt", f"Spec {Path(ort, stamm + endung).as_posix()}"
    for kennung, name in PER_CODE:
        if kennung.search(text):
            return "erzeugt", name
    for kennung, name in FREMDSOFTWARE:
        if kennung.search(text):
            return "fremd", name
    return "hand", ""


def pruefe_svg(pfad: Path) -> dict:
    """Herkunft und Geometrie einer SVG-Datei: {datei, herkunft, kennung, status, befunde}."""
    erg = {"datei": str(pfad), "herkunft": "", "kennung": "", "status": "✅", "befunde": []}
    if not pfad.is_file():                           # ohne Skriptausführung erzeugt die Lehrkraft später
        erg.update(status="⚠", befunde=[{"art": "fehlt", "stufe": "⚠",
                                         "text": "Datei fehlt – aus der Spec erzeugen oder Pfad prüfen"}])
        return erg
    text = pfad.read_text(encoding="utf-8", errors="replace")
    art, kennung = herkunft(pfad, text)
    erg.update(herkunft=art, kennung=kennung)
    try:
        befunde = geometrie(lies_svg(text), erzeugt=art == "erzeugt")
    except ET.ParseError as e:
        befunde = [{"art": "xml", "stufe": "❌", "text": f"kein gültiges SVG ({e})"}]
    if art == "hand":
        befunde.append({"art": "ohne_spec", "stufe": "⚠", "text": f"ohne Spec und Werkzeugkennung – {HAND_HINWEIS}"})
    erg["befunde"] = befunde
    stufen = {b["stufe"] for b in befunde}
    erg["status"] = "❌" if "❌" in stufen else "⚠" if "⚠" in stufen else "✅"
    return erg


HAND_HINWEIS = ("von Hand geschrieben? Mit dem Zeichen-Skill aus einer Spec erzeugen; Export aus "
                "Fachsoftware mit Quelle angeben")


def svg_hinweis(erg: dict, n: int = 3, ohne: tuple[str, ...] = ()) -> str:
    """Kurzer Befundtext zu einer SVG (gleichartige Befunde zusammengefasst, Arten in `ohne` ausgelassen)."""
    name = Path(erg["datei"]).name
    if erg["status"] == "✅":
        return f"{name} ✅" + (f" ({erg['kennung']})" if erg["kennung"] else "")
    teile = []
    for art in dict.fromkeys(b["art"] for b in erg["befunde"] if b["stufe"] in ("❌", "⚠") and b["art"] not in ohne):
        gleich = [b for b in erg["befunde"] if b["art"] == art]
        teile.append(f"{gleich[0]['stufe']} " + "; ".join(b["text"] for b in gleich[:n]) +
                     (f" (+{len(gleich) - n})" if len(gleich) > n else ""))
    return f"{name}: " + " · ".join(teile)


def bilder(text: str) -> list[str]:
    """Pfade der eingebundenen SVG (ohne Adressen im Netz), in Reihenfolge, ohne Doppelte."""
    return list(dict.fromkeys(unquote(p) for p in BILD.findall(text) if "://" not in p))


def pruefe_bilder(text: str, basis: Path) -> list[dict]:
    return [pruefe_svg(basis / p) for p in bilder(text)]


def pruefe_zeichnungen(text: str, basis: Path | None = None) -> tuple[str, str, list[dict]]:
    """Status (✅/⚠/❌), Befundtext und Funde – für andere Prüfskripte.

    Mit `basis` (Ordner der Markdown-Datei) werden die eingebundenen SVG mitgeprüft.
    """
    funde = finde(text)
    ascii_ = [f for f in funde if f["art"] == "ascii"]
    mermaid = [f for f in funde if f["art"] == "mermaid"]
    svg = pruefe_bilder(text, basis) if basis is not None else []
    funde += [{"art": "svg", **e} for e in svg]
    teile = []
    if ascii_:
        teile.append(f"{len(ascii_)} Zeichnung(en) aus Zeichen (" +
                     ", ".join(f"Z. {f['zeile']}–{f['bis']}" for f in ascii_[:4]) +
                     ") – als SVG erzeugen (Skill-Vertrag Abschn. 3)")
    if mermaid:
        teile.append(f"{len(mermaid)} Mermaid-Block/Blöcke (" +
                     ", ".join(f"Z. {f['zeile']}" for f in mermaid[:4]) + ") – als SVG erzeugen")
    auffaellig = [e for e in svg if e["status"] != "✅"]
    hand = [Path(e["datei"]).name for e in svg if e["herkunft"] == "hand"]
    teile += [svg_hinweis(e, ohne=("ohne_spec",)) for e in auffaellig
              if any(b["stufe"] in ("❌", "⚠") and b["art"] != "ohne_spec" for b in e["befunde"])]
    if hand:
        teile.append(f"⚠ {len(hand)} SVG ohne Spec und Werkzeugkennung ({', '.join(hand[:3])}"
                     f"{', …' if len(hand) > 3 else ''}) – {HAND_HINWEIS}")
    if not teile:
        return "✅", "keine Zeichnung aus Zeichen, kein Mermaid" + (
            f"; {len(svg)} SVG geprüft (Herkunft, Geometrie)" if svg else ""), funde
    if svg and len(auffaellig) < len(svg):
        teile.append(f"{len(svg) - len(auffaellig)} weitere SVG ✅")
    stufen = {"❌" if ascii_ else "⚠" if mermaid else "✅"} | {e["status"] for e in svg}
    return ("❌" if "❌" in stufen else "⚠" if "⚠" in stufen else "✅"), "; ".join(teile), funde


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Zeichnungen aus Zeichen, Mermaid und fehlerhafte SVG finden (lokal).")
    p.add_argument("dateien", nargs="+", help="Markdown-Dateien (samt eingebundener SVG) oder SVG-Dateien")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    ergebnisse, rc = [], 0
    for d in a.dateien:
        pfad = Path(d)
        if not pfad.is_file():
            print(f"Datei nicht gefunden: {d}", file=sys.stderr)
            return 2
        if pfad.suffix.lower() == ".svg":
            erg = pruefe_svg(pfad)
            status, text, funde = erg["status"], svg_hinweis(erg, n=8), erg["befunde"]
        else:
            status, text, funde = pruefe_zeichnungen(pfad.read_text(encoding="utf-8", errors="replace"),
                                                     basis=pfad.parent)
        ergebnisse.append({"datei": d, "status": status, "befund": text, "funde": funde})
        if status == "❌":
            rc = 1
    if a.json:
        print(json.dumps(ergebnisse, ensure_ascii=False, indent=2))
    else:
        print("| Datei | Ergebnis | Befund |\n|---|---|---|")
        for e in ergebnisse:
            print(f"| {e['datei']} | {e['status']} | {e['befund']} |")
        print("\n_Regelbasierte Suche. Zeichnungen als SVG: fachdiagramm-erstellen (Abläufe, Struktogramme, "
              "Datenmodelle) und die Zeichen-Skills der Bibliothek (Skill-Vertrag Abschn. 3)._")
    return rc


if __name__ == "__main__":
    sys.exit(main())
