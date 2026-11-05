"""
zeichnung — SVG-Grundbausteine für Technologieschemata.

Eine ``Zeichnung`` sammelt SVG-Elemente und merkt sich dabei die Rahmen aller Texte und
Linien. Die Prüfung (``pruefen.py``) nutzt sie, um verdeckte oder überlagerte Beschriftungen
zu finden, ohne das Bild zu rendern.

Jedes Element gehört zu einer **Zelle** (``zelle``, z. B. ``e3`` für Element 3, ``e3s1`` für
dessen ersten Sensor). Daraus entstehen die Gruppen im SVG und die Formen im draw.io-Export
(``drawio.py``), der dafür alle Grundformen zusätzlich als ``Prim`` mitschreibt.

Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from xml.sax.saxutils import escape

FONT_FAMILY = "DejaVu Sans, Arial, Helvetica, sans-serif"

#: Strichstärken (Pixel im SVG-Koordinatensystem)
LINIEN = {"duenn": 1.0, "normal": 1.6, "dick": 2.8}
LINIENARTEN = (*LINIEN, "gestrichelt", "keine")

#: Füllungen – bewusst nur Graustufen, damit das Bild in Schwarzweiß lesbar bleibt.
FUELLUNGEN = {
    "weiss": "#ffffff",
    "hellgrau": "#e2e2e2",
    "grau": "#bdbdbd",
    "mittelgrau": "#9a9a9a",
    "dunkelgrau": "#6f6f6f",
    "schwarz": "#000000",
    "keine": "none",
}
MUSTER = ("schraffur", "punkte", "ziegel")
ALLE_FUELLUNGEN = (*FUELLUNGEN, *MUSTER)

#: grobe Zeichenbreite relativ zur Schriftgröße (DejaVu Sans, die Prüfung rechnet damit)
BREITE_NORMAL = 0.55
BREITE_FETT = 0.62

#: Laufweiten von DejaVu Sans in 1/1000 em – für Abschnitte mit Überstrich, die genau sitzen müssen
LAUFWEITE = {' ': 318, '!': 401, '"': 460, '#': 838, '$': 636, '%': 950, '&': 780, "'": 275, '(': 390, ')': 390, '*': 500,
             '+': 838, ',': 318, '-': 361, '.': 318, '/': 337, '0': 636, '1': 636, '2': 636, '3': 636, '4': 636, '5': 636,
             '6': 636, '7': 636, '8': 636, '9': 636, ':': 337, ';': 337, '<': 838, '=': 838, '>': 838, '?': 531, '@': 1000,
             'A': 684, 'B': 686, 'C': 698, 'D': 770, 'E': 632, 'F': 575, 'G': 775, 'H': 752, 'I': 295, 'J': 295, 'K': 656,
             'L': 557, 'M': 863, 'N': 748, 'O': 787, 'P': 603, 'Q': 787, 'R': 695, 'S': 635, 'T': 611, 'U': 732, 'V': 684,
             'W': 989, 'X': 685, 'Y': 611, 'Z': 685, '[': 390, '\\': 337, ']': 390, '^': 838, '_': 500, '`': 500, 'a': 613,
             'b': 635, 'c': 550, 'd': 635, 'e': 615, 'f': 352, 'g': 635, 'h': 634, 'i': 278, 'j': 278, 'k': 579, 'l': 278,
             'm': 974, 'n': 634, 'o': 612, 'p': 635, 'q': 635, 'r': 411, 's': 521, 't': 392, 'u': 634, 'v': 592, 'w': 818,
             'x': 592, 'y': 592, 'z': 525, '{': 636, '|': 337, '}': 636, '~': 838, '·': 318, '¬': 838, '↑': 838, '↓': 838,
             '≥': 838, '≤': 838, '≠': 838, 'ä': 613, 'ö': 612, 'ü': 634, 'Ä': 684, 'Ö': 787, 'Ü': 732, 'ß': 630, '°': 500,
             '„': 518, '“': 518, '−': 838, '–': 500}


def f(v: float) -> str:
    """Zahl kurz formatieren."""
    s = ("%.1f" % v).rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def laufweite(text: str, groesse: float) -> float:
    """Breite eines Textes in DejaVu Sans; genauer als ``textmasse``, die nur für die Prüfung schätzt."""
    return sum(LAUFWEITE.get(c, 600) for c in text) * groesse / 1000


def textmasse(text: str, groesse: float, fett: bool = False, zeilenhoehe: float | None = None) -> tuple[float, float]:
    """(Breite, Höhe) eines möglicherweise mehrzeiligen Textes."""
    zeilen = text.split("\n")
    zh = zeilenhoehe or groesse * 1.25
    b = max(len(z) for z in zeilen) * groesse * (BREITE_FETT if fett else BREITE_NORMAL)
    return b, groesse + (len(zeilen) - 1) * zh


@dataclass
class Textbox:
    x1: float
    y1: float
    x2: float
    y2: float
    text: str
    teil: int          # Index des besitzenden Elements (-1 = Zeichnung selbst)


@dataclass
class Segment:
    x1: float
    y1: float
    x2: float
    y2: float
    teil: int


@dataclass
class Prim:
    """Grundform in Bildkoordinaten (für den draw.io-Export)."""
    zelle: str
    art: str           # rechteck, kreis, polygon, linie, zug, rohr, text
    d: dict


@dataclass
class Zeichnung:
    breite: float
    hoehe: float
    titel: str
    beschreibung: str
    hinweis: str = ""
    defs: dict[str, str] = field(default_factory=dict)
    el: list[str] = field(default_factory=list)
    texte: list[Textbox] = field(default_factory=list)
    segmente: list[Segment] = field(default_factory=list)
    aktuell: int = -1  # Index des Elements, das gerade zeichnet
    zelle: str = "rahmen"  # Zelle (Gruppe/Form), zu der neue Elemente gehören
    prims: list[Prim] = field(default_factory=list)
    el_zelle: list[str] = field(default_factory=list)   # Zelle je Eintrag in ``el``
    drehungen: dict[str, tuple[float, float, float]] = field(default_factory=dict)  # Zelle → (Winkel, cx, cy)

    def _el(self, svg: str, art: str | None = None, **d) -> None:
        self.el.append(svg)
        self.el_zelle.append(self.zelle)
        if art:
            self.prims.append(Prim(self.zelle, art, d))

    def drehen(self, winkel: float, cx: float, cy: float) -> None:
        """Folgende Elemente der Zelle um (cx, cy) drehen, bis ``drehen_ende``."""
        self._el(f'<g transform="rotate({f(winkel)} {f(cx)} {f(cy)})">')
        self.drehungen[self.zelle] = (winkel, cx, cy)

    def drehen_ende(self) -> None:
        self._el("</g>")

    # ── Füllung und Linie ────────────────────────────────────────────
    def fuellung(self, name: str) -> str:
        if name in FUELLUNGEN:
            return FUELLUNGEN[name]
        if name == "schraffur":
            self.defs["schraffur"] = (
                '<pattern id="schraffur" width="6" height="6" patternUnits="userSpaceOnUse" '
                'patternTransform="rotate(45)"><rect width="6" height="6" fill="#fff"/>'
                '<line x1="0" y1="0" x2="0" y2="6" stroke="#555" stroke-width="1.2"/></pattern>')
            return "url(#schraffur)"
        if name == "punkte":
            self.defs["punkte"] = (
                '<pattern id="punkte" width="5" height="5" patternUnits="userSpaceOnUse">'
                '<rect width="5" height="5" fill="#d0d0d0"/><circle cx="2.5" cy="2.5" r="0.9" fill="#333"/></pattern>')
            return "url(#punkte)"
        if name == "ziegel":
            self.defs["ziegel"] = (
                '<pattern id="ziegel" width="28" height="24" patternUnits="userSpaceOnUse">'
                '<rect width="28" height="24" fill="#fff"/>'
                '<path d="M0 0H28M0 12H28M14 0V12M0 12V24M28 12V24" fill="none" stroke="#777" '
                'stroke-width="1"/></pattern>')
            return "url(#ziegel)"
        raise ValueError(f"unbekannte Füllung '{name}'")

    @staticmethod
    def _strich(linie: str, farbe: str = "#000") -> str:
        if linie == "keine":
            return 'stroke="none"'
        breite = LINIEN.get(linie, LINIEN["normal"])
        dash = ' stroke-dasharray="6 4"' if linie == "gestrichelt" else ""
        return f'stroke="{farbe}" stroke-width="{f(breite)}"{dash}'

    # ── Formen ───────────────────────────────────────────────────────
    def rechteck(self, x1, y1, x2, y2, fuellung="weiss", linie="normal", rundung=0.0) -> None:
        r = f' rx="{f(rundung)}"' if rundung else ""
        self._el(f'<rect x="{f(x1)}" y="{f(y1)}" width="{f(x2 - x1)}" height="{f(y2 - y1)}"{r} '
                 f'fill="{self.fuellung(fuellung)}" {self._strich(linie)}/>',
                 "rechteck", x1=x1, y1=y1, x2=x2, y2=y2, fuellung=fuellung, linie=linie, rundung=rundung)

    def kreis(self, cx, cy, r, fuellung="weiss", linie="normal") -> None:
        self._el(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{self.fuellung(fuellung)}" '
                 f'{self._strich(linie)}/>', "kreis", cx=cx, cy=cy, r=r, fuellung=fuellung, linie=linie)

    def polygon(self, punkte, fuellung="weiss", linie="normal", geschlossen=True) -> None:
        p = " ".join(f"{f(x)},{f(y)}" for x, y in punkte)
        tag = "polygon" if geschlossen else "polyline"
        fill = self.fuellung(fuellung) if geschlossen else "none"
        self._el(f'<{tag} points="{p}" fill="{fill}" {self._strich(linie)} stroke-linejoin="round"/>',
                 "polygon", punkte=[tuple(q) for q in punkte], fuellung=fuellung if geschlossen else "keine",
                 linie=linie, geschlossen=geschlossen)

    def linie(self, x1, y1, x2, y2, linie="normal", registrieren=False) -> None:
        self._el(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" {self._strich(linie)}/>',
                 "linie", punkte=[(x1, y1), (x2, y2)], linie=linie)
        if registrieren:
            self.segmente.append(Segment(x1, y1, x2, y2, self.aktuell))

    def linienzug(self, punkte, linie="normal", pfeil="kein", radius=0.0, registrieren=False) -> None:
        """Linienzug mit optional gerundeten Ecken und Pfeilspitze am Ende/Anfang."""
        pts = [tuple(p) for p in punkte]
        kopf = 9.0
        if pfeil in ("ende", "beide") and len(pts) >= 2:
            pts[-1], spitze_e = _kuerzen(pts[-1], pts[-2], kopf), pts[-1]
        else:
            spitze_e = None
        if pfeil in ("anfang", "beide") and len(pts) >= 2:
            pts[0], spitze_a = _kuerzen(pts[0], pts[1], kopf), pts[0]
        else:
            spitze_a = None
        self._el(f'<path d="{_rundweg(pts, radius)}" fill="none" {self._strich(linie)} '
                 f'stroke-linejoin="round" stroke-linecap="butt"/>',
                 "zug", punkte=[tuple(p) for p in punkte], linie=linie, pfeil=pfeil, radius=radius)
        if spitze_e:
            self._pfeilspitze(spitze_e, pts[-1])
        if spitze_a:
            self._pfeilspitze(spitze_a, pts[0])
        if registrieren:
            for a, b in zip(punkte, list(punkte)[1:]):
                self.segmente.append(Segment(a[0], a[1], b[0], b[1], self.aktuell))

    def _pfeilspitze(self, spitze, basis) -> None:
        a = math.atan2(spitze[1] - basis[1], spitze[0] - basis[0])
        px, py = -math.sin(a) * 3.6, math.cos(a) * 3.6
        # gehört zum Linienzug (Prim "zug" trägt den Pfeil) – im draw.io-Export Teil der Linie
        self._el(f'<polygon points="{f(spitze[0])},{f(spitze[1])} {f(basis[0] + px)},{f(basis[1] + py)} '
                 f'{f(basis[0] - px)},{f(basis[1] - py)}" fill="#000"/>')

    def rohr(self, punkte, weite=14.0, radius=12.0, fuellung="weiss") -> None:
        """Rohr als Doppellinie (Kontur und heller Kern)."""
        d = _rundweg([tuple(p) for p in punkte], radius)
        wand = LINIEN["normal"]
        self._el(f'<path d="{d}" fill="none" stroke="#000" stroke-width="{f(weite + 2 * wand)}" '
                 f'stroke-linejoin="round"/>', "rohr", punkte=[tuple(p) for p in punkte], weite=weite,
                 radius=radius, fuellung=fuellung)
        self._el(f'<path d="{d}" fill="none" stroke="{self.fuellung(fuellung) if fuellung != "keine" else "#fff"}" '
                 f'stroke-width="{f(weite)}" stroke-linejoin="round"/>')
        for a, b in zip(punkte, list(punkte)[1:]):
            self.segmente.append(Segment(a[0], a[1], b[0], b[1], self.aktuell))

    # ── Text ─────────────────────────────────────────────────────────
    def text(self, x, y, s, groesse=12.0, anker="start", fett=False, kursiv=False,
             zeilenhoehe=None, teil=None, spans=None) -> Textbox:
        """Text mit Grundlinie bei y (erste Zeile). Gibt den belegten Rahmen zurück.

        ``spans`` (nur einzeilig): Abschnitte (Text, ``overline``/``underline``/None) – Negation als Überstrich.
        Jeder Abschnitt steht an eigener Stelle, der Strich ist eine echte Linie: Eine Negation darf nicht davon
        abhängen, ob ein Programm (Word) ``text-decoration`` im SVG darstellt.
        """
        zeilen = s.split("\n")
        zh = zeilenhoehe or groesse * 1.25
        attrs = (f'font-size="{f(groesse)}" text-anchor="{anker}" '
                 f'font-weight="{"bold" if fett else "normal"}" font-style="{"italic" if kursiv else "normal"}"')
        if spans:
            self._abschnitte(x, y, spans, groesse, anker, fett, kursiv)
        elif len(zeilen) == 1:
            self._el(f'<text x="{f(x)}" y="{f(y)}" {attrs} fill="#000">{escape(s)}</text>')
        else:
            inhalt = "".join(f'<tspan x="{f(x)}" dy="{f(0 if i == 0 else zh)}">{escape(z)}</tspan>'
                             for i, z in enumerate(zeilen))
            self._el(f'<text x="{f(x)}" y="{f(y)}" {attrs} fill="#000">{inhalt}</text>')
        b, h = textmasse(s, groesse, fett, zh)
        if anker == "middle":
            x1 = x - b / 2
        elif anker == "end":
            x1 = x - b
        else:
            x1 = x
        box = Textbox(x1, y - groesse * 0.8, x1 + b, y - groesse * 0.8 + h + groesse * 0.2, s,
                      self.aktuell if teil is None else teil)
        self.texte.append(box)
        self.prims.append(Prim(self.zelle, "text", dict(x=x, y=y, text=s, groesse=groesse, anker=anker, fett=fett,
                                                        kursiv=kursiv, zeilenhoehe=zh, spans=spans)))
        return box

    def _abschnitte(self, x, y, spans, groesse, anker, fett, kursiv) -> None:
        """Text aus Abschnitten; Überstrich und Unterstrich nur im Bild (draw.io: Textformat, siehe ``drawio``)."""
        gesamt = laufweite("".join(t for t, _ in spans), groesse)
        xa = x - {"start": 0.0, "middle": gesamt / 2, "end": gesamt}[anker]
        attrs = (f'font-size="{f(groesse)}" text-anchor="start" font-weight="{"bold" if fett else "normal"}" '
                 f'font-style="{"italic" if kursiv else "normal"}"')
        for t, deko in spans:
            kern = t.strip(" ")
            xa += laufweite(t[:len(t) - len(t.lstrip(" "))], groesse)      # Leerzeichen am Rand fällt im SVG weg
            b = laufweite(kern, groesse)
            self._el(f'<text x="{f(xa)}" y="{f(y)}" {attrs} fill="#000">{escape(kern)}</text>')
            if deko:
                ys = y - groesse * 0.86 if deko == "overline" else y + groesse * 0.17
                name = "ueberstrich" if deko == "overline" else "unterstrich"
                self._el(f'<line class="{name}" x1="{f(xa)}" y1="{f(ys)}" x2="{f(xa + b)}" y2="{f(ys)}" '
                         f'stroke="#000" stroke-width="{f(max(0.9, groesse * 0.08))}"/>')
            xa += b + laufweite(t[len(t.rstrip(" ")):] if t.strip(" ") else "", groesse)

    # ── Ausgabe ──────────────────────────────────────────────────────
    def svg(self) -> str:
        """SVG mit einer Gruppe je Element (``<g id="e3">``), damit es sich in Inkscape & Co. bauteilweise
        verschieben lässt."""
        defs = "\n".join(self.defs.values())
        kopf = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
                f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(self.breite)}" height="{f(self.hoehe)}" '
                f'viewBox="0 0 {f(self.breite)} {f(self.hoehe)}" font-family="{FONT_FAMILY}">\n'
                f'<title>{escape(self.titel)}</title>\n'
                f'<desc>{escape(self.beschreibung)}</desc>\n')
        if self.hinweis:
            kopf += f'<!-- {escape(self.hinweis).replace("--", "- -")} -->\n'
        if defs:
            kopf += f'<defs>\n{defs}\n</defs>\n'
        kopf += f'<rect x="0" y="0" width="{f(self.breite)}" height="{f(self.hoehe)}" fill="#ffffff"/>\n'
        teile, offen = [], None
        for svg, zelle in zip(self.el, self.el_zelle):
            gruppe = _gruppe(zelle)
            if gruppe != offen:
                if offen is not None:
                    teile.append("</g>")
                teile.append(f'<g id="{gruppe}">')
                offen = gruppe
            teile.append(svg)
        if offen is not None:
            teile.append("</g>")
        return kopf + "\n".join(teile) + "\n</svg>\n"


# ── Hilfsfunktionen ──────────────────────────────────────────────────

def _gruppe(zelle: str) -> str:
    """Element-Gruppe einer Zelle: ``e3s1`` → ``e3``."""
    if zelle.startswith("e"):
        i = 1
        while i < len(zelle) and zelle[i].isdigit():
            i += 1
        return zelle[:i]
    return zelle


def _kuerzen(p, von, laenge):
    """Punkt p um ``laenge`` in Richtung ``von`` verschieben."""
    dx, dy = von[0] - p[0], von[1] - p[1]
    d = math.hypot(dx, dy) or 1.0
    laenge = min(laenge, d * 0.9)
    return (p[0] + dx / d * laenge, p[1] + dy / d * laenge)


def _rundweg(pts, radius: float) -> str:
    """Pfad durch die Punkte; Ecken mit Radius als quadratische Kurven gerundet."""
    if len(pts) < 2:
        raise ValueError("Ein Linienzug braucht mindestens zwei Punkte.")
    if radius <= 0 or len(pts) == 2:
        return "M " + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
    d = f"M {f(pts[0][0])} {f(pts[0][1])}"
    for i in range(1, len(pts) - 1):
        p0, p1, p2 = pts[i - 1], pts[i], pts[i + 1]
        r = min(radius, math.hypot(p1[0] - p0[0], p1[1] - p0[1]) / 2, math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / 2)
        a = _kuerzen(p1, p0, r)
        b = _kuerzen(p1, p2, r)
        d += f" L {f(a[0])} {f(a[1])} Q {f(p1[0])} {f(p1[1])} {f(b[0])} {f(b[1])}"
    d += f" L {f(pts[-1][0])} {f(pts[-1][1])}"
    return d
