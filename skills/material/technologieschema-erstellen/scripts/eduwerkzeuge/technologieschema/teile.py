"""
teile — Bauteile eines Technologieschemas und ihr Aufbau aus der YAML-Spec.

Jedes Bauteil (``typ``) kennt seine Pflicht- und optionalen Schlüssel (``SCHEMA``), zeichnet sich
selbst und meldet seinen Rahmen. Aus dem Rahmen entstehen **Anker** (``-MM1@unten``), mit denen
Linien und Rohre an Bauteilen enden, ohne dass Koordinaten ausgerechnet werden müssen.

Koordinaten: x nach rechts, y nach unten, Einheit Pixel des SVG.
Rechteckige Teile: ``x, y`` = obere linke Ecke. Runde Teile (kreis, sensor, taster, leuchte,
motor, pumpe, ventil): ``x, y`` = Mittelpunkt.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field

from . import symbole
from .zeichnung import (ALLE_FUELLUNGEN, LINIENARTEN, Zeichnung, f, textmasse)


class SpecFehler(ValueError):
    """Fehler in der Spec – die Meldung nennt Element und Schlüssel."""


# ───────────────────────────── Schema ─────────────────────────────

LAGEN = ("oben", "unten", "links", "rechts", "keine")
GEMEIN = {"typ", "id", "ref", "name", "lage", "abstand", "betriebsmittel", "funktion", "legende", "kommentar",
          "gehoert_zu"}

SCHEMA: dict[str, tuple[set[str], set[str]]] = {
    # typ: (Pflicht, optional)  – zusätzlich GEMEIN
    "rechteck": ({"x", "y", "b", "h"}, {"fuellung", "linie", "rundung", "text", "textgroesse"}),
    "kreis": ({"x", "y", "r"}, {"fuellung", "linie", "text", "textgroesse"}),
    "polygon": ({"punkte"}, {"fuellung", "linie", "offen"}),
    "linie": ({"punkte"}, {"stil", "pfeil", "radius", "route", "schraeg"}),
    "rohr": ({"punkte"}, {"weite", "radius", "route"}),
    "text": ({"x", "y", "text"}, {"groesse", "ausrichtung", "fett", "kursiv"}),
    "etikett": ({"x", "y", "text"}, {"ziel", "groesse", "ausrichtung", "fett", "kursiv"}),
    "behaelter": ({"x", "y", "b", "h"}, {"form", "fuellung", "offen", "kopf", "auslass", "fuellstand"}),
    "zylinder": ({"x", "y"}, {"ausfahrt", "laenge", "breite", "stange", "feder", "werkzeug", "werkzeug_b",
                              "sensoren"}),
    "ventil": ({"x", "y"}, {"achse", "groesse", "spule"}),
    "sensor": ({"x", "y"}, {"art", "stiel"}),
    "taster": ({"x", "y"}, {"r", "symbol", "farbe", "text"}),
    "leuchte": ({"x", "y"}, {"r", "farbe", "text"}),
    "motor": ({"x", "y"}, {"r", "phasen"}),
    "pumpe": ({"x", "y"}, {"r", "richtung"}),
    "band": ({"x", "y", "b", "h"}, {"winkel", "rollen"}),
    "bedienfeld": ({"x", "y", "b", "h", "eintraege"}, {"titel", "spalten", "rundung"}),
    "ampel": ({"x", "y", "b", "h", "lampen"}, set()),
    "symbol": ({"x", "y", "symbol"}, {"drehung", "spiegeln", "groesse", "text", "betaetigung", "wirklaenge"}),
    "knoten": ({"punkt"}, {"r"}),
}

SENSOR_SCHEMA = ({"seite"}, {"id", "name", "pos", "betriebsmittel", "funktion", "legende"})
EINTRAG_TYPEN = ("taster", "leuchte")

ZAHLEN = {"x", "y", "b", "h", "r", "laenge", "breite", "stange", "weite", "radius", "groesse", "abstand",
          "winkel", "fuellstand", "kopf", "auslass", "pos", "spalten", "textgroesse", "werkzeug_b", "rundung",
          "wirklaenge"}
WAHRHEITEN = {"feder", "offen", "fett", "kursiv", "rollen", "schraeg", "spiegeln"}
AUFZAEHLUNGEN: dict[str, tuple[str, ...]] = {
    "fuellung": ALLE_FUELLUNGEN, "linie": LINIENARTEN, "stil": LINIENARTEN, "lage": LAGEN,
    "pfeil": ("kein", "ende", "anfang", "beide"),
    "route": ("auto", "hv", "vh"),
    "drehung": (0, 90, 180, 270),
    "betaetigung": tuple(symbole.BETAETIGUNGEN),
    "ausrichtung": ("links", "mitte", "rechts"),
    "form": ("tank", "silo", "trichter"),
    "ausfahrt": ("unten", "oben", "rechts", "links"),
    "werkzeug": ("keine", "platte", "keil"),
    "achse": ("senkrecht", "waagerecht"),
    "spule": ("rechts", "links", "oben", "unten", "keine"),
    "art": ("block", "rolle", "lichtschranke", "kontakt", "initiator"),
    "stiel": ("oben", "unten", "links", "rechts", "keiner"),
    "symbol": ("keins", "pfeil_auf", "pfeil_ab", "doppelpfeil_auf", "ring", "not_halt"),
    "farbe": ("weiss", "hellgrau", "grau", "mittelgrau", "dunkelgrau", "schwarz"),
    "richtung": ("rechts", "links", "oben", "unten"),
    "seite": ("links", "rechts", "oben", "unten"),
}

#: Legende: Betriebsmittel-Bezeichnung, wenn nichts angegeben ist
BETRIEBSMITTEL = {
    "zylinder": "Zylinder", "ventil": "Ventil", "taster": "Taster", "leuchte": "Leuchtmelder",
    "motor": "Motor", "pumpe": "Pumpe", "band": "Förderband", "behaelter": "Behälter",
    "ampel": "Signalgeber", "rechteck": "Bauteil", "kreis": "Bauteil",
}
SENSOR_BEZEICHNUNG = {"block": "Sensor", "rolle": "Endschalter", "lichtschranke": "Lichtschranke",
                      "kontakt": "Schwimmerschalter", "initiator": "Näherungssensor"}

ANKER_NAMEN = ("mitte", "oben", "unten", "links", "rechts", "oben_links", "oben_rechts", "unten_links",
               "unten_rechts")
ANKER_MUSTER = re.compile(r"^(?P<id>.+?)@(?P<punkt>[a-z_0-9]+)(?::(?P<dx>[+-]?\d+(?:\.\d+)?),(?P<dy>[+-]?\d+(?:\.\d+)?))?$")

#: Schlüssel, die Punkte enthalten (Liste oder Einzelpunkt)
PUNKTLISTEN = {"punkte"}
EINZELPUNKTE = {"ziel"}

SCHRIFT_ID = 13.0
SCHRIFT_NAME = 11.0
ZEILENABSTAND = 3.0


# ───────────────────────────── Kontext ─────────────────────────────

@dataclass
class Teilinfo:
    index: int
    typ: str
    id: str | None
    box: tuple[float, float, float, float]
    klein: bool


@dataclass
class Kontext:
    z: Zeichnung
    anker_vorher: dict[str, dict[str, tuple[float, float]]]
    strikt: bool
    anker: dict[str, dict[str, tuple[float, float]]] = field(default_factory=dict)
    teile: list[Teilinfo] = field(default_factory=list)
    legende: list[tuple[str, str, str, str]] = field(default_factory=list)  # id, betriebsmittel, funktion, name
    ids: list[tuple[str, int]] = field(default_factory=list)
    unaufgeloest: list[str] = field(default_factory=list)
    warnungen: list[tuple[int, str]] = field(default_factory=list)   # (Element, Text) aus dem Aufbau
    index: int = 0
    # für den draw.io-Export: Anker je Zelle, Zelle je Kennzeichen, Verbindungen (Linie, Rohr, Etikett)
    zellen_anker: dict[str, dict[str, tuple[float, float]]] = field(default_factory=dict)
    zelle_von: dict[str, str] = field(default_factory=dict)
    kanten: dict[str, dict] = field(default_factory=dict)
    _anker_name: str | None = None
    _anker_id: str | None = None
    _enden: tuple[str | None, str | None] = (None, None)

    # ── Punkte und Anker ─────────────────────────────────────────
    def punkt(self, p) -> tuple[float, float]:
        self._anker_name = None
        self._anker_id = None
        if isinstance(p, (list, tuple)) and len(p) == 2 and all(_ist_zahl(v) for v in p):
            return float(p[0]), float(p[1])
        if isinstance(p, str):
            m = ANKER_MUSTER.match(p.strip())
            if not m:
                raise SpecFehler(f"Punkt '{p}' ist weder [x, y] noch ein Anker der Form \"ID@punkt\"")
            ziel = self.anker_vorher.get(m["id"])
            if ziel is None or m["punkt"] not in ziel:
                if self.strikt:
                    if ziel is None:
                        raise SpecFehler(f"Anker '{p}': kein Teil mit id oder ref '{m['id']}'")
                    raise SpecFehler(f"Anker '{p}': '{m['punkt']}' gibt es bei '{m['id']}' nicht "
                                     f"(vorhanden: {', '.join(sorted(ziel))})")
                return 0.0, 0.0
            x, y = ziel[m["punkt"]]
            self._anker_name = m["punkt"]
            self._anker_id = m["id"]
            return x + float(m["dx"] or 0), y + float(m["dy"] or 0)
        raise SpecFehler(f"Punkt {p!r} ist weder [x, y] noch ein Anker")

    def punkte(self, ps) -> list[tuple[float, float]]:
        return self.punkte_mit_anker(ps)[0]

    def punkte_mit_anker(self, ps) -> tuple[list[tuple[float, float]], list[str | None]]:
        if not isinstance(ps, list) or len(ps) < 2:
            raise SpecFehler("'punkte' braucht eine Liste mit mindestens zwei Punkten")
        pts, namen, ids = [], [], []
        for p in ps:
            pts.append(self.punkt(p))
            namen.append(self._anker_name)
            ids.append(self._anker_id)
        self._enden = (ids[0], ids[-1])
        return pts, namen

    def kante(self, art: str, pts, enden=(None, None), **d) -> None:
        """Verbindung für den draw.io-Export merken: Punkte und die Kennzeichen an Anfang und Ende."""
        self.kanten[self.z.zelle] = dict(art=art, punkte=list(pts), von=enden[0], nach=enden[1], **d)

    def rechtwinklig(self, ps, route: str = "auto", erlaube_schraeg: bool = False):
        """Punkte aufloesen und rechtwinklig verbinden (Wirkungslinien verlaufen waagerecht oder senkrecht)."""
        pts, namen = self.punkte_mit_anker(ps)
        if erlaube_schraeg:
            return pts
        ergebnis, knicke = ortho(pts, namen, route)
        for dx, dy in knicke:
            if min(dx, dy) < KNICK_MIN:
                self.warnungen.append((self.index, f"Linie knickt nur um {min(dx, dy):.0f} px – fast gerade; "
                                                   f"Positionen oder Anker angleichen (Linien verlaufen waagerecht "
                                                   f"oder senkrecht)"))
        return ergebnis

    def melde(self, e: dict, box, klein: bool = False, extra: dict | None = None, anker_box=None) -> None:
        """Rahmen, Anker, Legende eines Bauteils eintragen.

        ``box`` ist der belegte Rahmen (für die Prüfung); die Anker liegen am ``anker_box``
        (Standard: ``box``) – beim Zylinder am Gehäuse, nicht am breiteren Werkzeug.
        """
        x1, y1, x2, y2 = anker_box or box
        cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
        anker = {"mitte": (cx, cy), "oben": (cx, y1), "unten": (cx, y2), "links": (x1, cy), "rechts": (x2, cy),
                 "oben_links": (x1, y1), "oben_rechts": (x2, y1), "unten_links": (x1, y2), "unten_rechts": (x2, y2)}
        if extra:
            anker.update(extra)
        for schluessel in (e.get("id"), e.get("ref")):
            if schluessel:
                self.anker[str(schluessel)] = anker
                self.zelle_von[str(schluessel)] = self.z.zelle
        self.zellen_anker.setdefault(self.z.zelle, anker)
        self.teile.append(Teilinfo(self.index, e.get("typ", "?"), e.get("id"), tuple(box), klein))
        if e.get("id") and e.get("legende", True) is not False:
            self.ids.append((str(e["id"]), self.index))
            self.legende.append((str(e["id"]), e.get("betriebsmittel") or _bm_standard(e),
                                 e.get("funktion") or e.get("name") or "", e.get("name") or ""))


def _ist_zahl(v) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def _bm_standard(e: dict) -> str:
    typ = e.get("typ")
    if typ == "symbol":
        s = symbole.SYMBOLE.get(e.get("symbol"))
        return s.titel if s else "Bauteil"
    if typ == "sensor":
        return SENSOR_BEZEICHNUNG.get(e.get("art", "block"), "Sensor")
    if typ == "taster" and e.get("symbol") == "not_halt":
        return "Not-Halt-Taster"
    if typ == "zylinder" and e.get("feder"):
        return "Zylinder, einfachwirkend (Feder)"
    return BETRIEBSMITTEL.get(typ, "Bauteil")


KNICK_MIN = 15.0   # kleinerer Versatz zwischen zwei Punkten gilt als Positionsfehler


def ortho(pts, namen=None, route: str = "auto"):
    """Verbindet Punkte nur waagerecht und senkrecht; schräge Teilstücke bekommen einen Knick.

    ``route``: ``hv`` erst waagerecht, ``vh`` erst senkrecht, ``auto`` richtet sich nach dem Anker
    (``links``/``rechts`` → waagerecht heraus, ``oben``/``unten`` → senkrecht heraus; am Ziel gilt
    dasselbe rückwärts) und wechselt sonst gegenüber dem vorigen Teilstück.
    Rückgabe: (Punkte, Versätze der eingefügten Knicke als (|dx|, |dy|)).
    """
    namen = namen or [None] * len(pts)
    res = [pts[0]]
    knicke = []
    letzte_waagerecht: bool | None = None
    for i in range(len(pts) - 1):
        a, b = pts[i], pts[i + 1]
        dx, dy = abs(b[0] - a[0]), abs(b[1] - a[1])
        if dx < 0.5 or dy < 0.5:                       # schon rechtwinklig
            res.append(b)
            letzte_waagerecht = dy < 0.5
            continue
        if route == "hv":
            hfirst = True
        elif route == "vh":
            hfirst = False
        elif namen[i] in ("links", "rechts"):
            hfirst = True
        elif namen[i] in ("oben", "unten"):
            hfirst = False
        elif namen[i + 1] in ("links", "rechts"):      # am Ziel waagerecht ankommen → zuerst senkrecht
            hfirst = False
        elif namen[i + 1] in ("oben", "unten"):
            hfirst = True
        elif letzte_waagerecht is not None:
            hfirst = not letzte_waagerecht
        else:
            hfirst = True
        res.append((b[0], a[1]) if hfirst else (a[0], b[1]))
        res.append(b)
        knicke.append((dx, dy))
        letzte_waagerecht = not hfirst
    return res, knicke


# ───────────────────────────── Beschriftung ─────────────────────────────

def beschrifte(ctx: Kontext, e: dict, box, standard: str, extra_zeilen: list | None = None) -> None:
    """Kennzeichen (fett) und Kurzname (kursiv) neben das Teil setzen."""
    zeilen = []
    kennung = e.get("id") or e.get("gehoert_zu")      # Teil eines Betriebsmittels (z. B. Kontakt des Schützes -Q1)
    if kennung:
        zeilen.append((str(kennung), SCHRIFT_ID, True, False))
    if e.get("name"):
        zeilen.append((str(e["name"]), SCHRIFT_NAME, False, True))
    if extra_zeilen:
        zeilen += extra_zeilen
    if not zeilen:
        return
    lage = e.get("lage", standard)
    if lage == "keine":
        return
    block(ctx, zeilen, box, lage, float(e.get("abstand", 8)))


def block(ctx: Kontext, zeilen, box, lage: str, abstand: float) -> None:
    """Textblock (Liste (text, größe, fett, kursiv)) an eine Seite eines Rahmens setzen."""
    x1, y1, x2, y2 = box
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    hoehen = [g + ZEILENABSTAND for (_, g, _, _) in zeilen]
    gesamt = sum(hoehen)
    z = ctx.z
    if lage == "oben":
        y = y1 - abstand - gesamt + hoehen[0] - ZEILENABSTAND
        for (t, g, fett, kursiv), h in zip(zeilen, hoehen):
            z.text(cx, y, t, g, "middle", fett, kursiv)
            y += h
    elif lage == "unten":
        y = y2 + abstand + zeilen[0][1] * 0.8
        for (t, g, fett, kursiv), h in zip(zeilen, hoehen):
            z.text(cx, y, t, g, "middle", fett, kursiv)
            y += h
    else:
        x = x1 - abstand if lage == "links" else x2 + abstand
        anker = "end" if lage == "links" else "start"
        y = cy - gesamt / 2 + zeilen[0][1] * 0.8 + 2
        for (t, g, fett, kursiv), h in zip(zeilen, hoehen):
            z.text(x, y, t, g, anker, fett, kursiv)
            y += h


# ───────────────────────────── einfache Teile ─────────────────────────────

def _zahl(e: dict, k: str, standard: float) -> float:
    v = e.get(k, standard)
    return float(v)


def _innentext(ctx: Kontext, text: str, cx: float, cy: float, groesse: float) -> None:
    zeilen = text.split("\n")
    zh = groesse * 1.2
    y = cy - (len(zeilen) - 1) * zh / 2 + groesse * 0.35
    for i, t in enumerate(zeilen):
        ctx.z.text(cx, y + i * zh, t, groesse, "middle")


def t_rechteck(ctx, e):
    x, y, b, h = (float(e[k]) for k in ("x", "y", "b", "h"))
    ctx.z.rechteck(x, y, x + b, y + h, e.get("fuellung", "weiss"), e.get("linie", "normal"), _zahl(e, "rundung", 0))
    if e.get("text"):
        _innentext(ctx, str(e["text"]), x + b / 2, y + h / 2, _zahl(e, "textgroesse", 12))
    box = (x, y, x + b, y + h)
    ctx.melde(e, box, klein=b * h < 6000)
    beschrifte(ctx, e, box, "unten")


def t_kreis(ctx, e):
    x, y, r = (float(e[k]) for k in ("x", "y", "r"))
    ctx.z.kreis(x, y, r, e.get("fuellung", "weiss"), e.get("linie", "normal"))
    if e.get("text"):
        _innentext(ctx, str(e["text"]), x, y, _zahl(e, "textgroesse", 12))
    box = (x - r, y - r, x + r, y + r)
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "unten")


def t_polygon(ctx, e):
    pts = ctx.punkte(e["punkte"])
    ctx.z.polygon(pts, e.get("fuellung", "weiss"), e.get("linie", "normal"), geschlossen=not e.get("offen", False))
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    box = (min(xs), min(ys), max(xs), max(ys))
    ctx.melde(e, box, klein=(box[2] - box[0]) * (box[3] - box[1]) < 6000)
    beschrifte(ctx, e, box, "unten")


def t_linie(ctx, e):
    pts = ctx.rechtwinklig(e["punkte"], e.get("route", "auto"), bool(e.get("schraeg")))
    ctx.kante("linie", pts, ctx._enden, stil=e.get("stil", "normal"), pfeil=e.get("pfeil", "kein"),
              radius=_zahl(e, "radius", 0), schraeg=bool(e.get("schraeg")))
    ctx.z.linienzug(pts, e.get("stil", "normal"), e.get("pfeil", "kein"), _zahl(e, "radius", 0), registrieren=True)
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    ctx.melde(e, (min(xs), min(ys), max(xs), max(ys)))
    beschrifte(ctx, e, (min(xs), min(ys), max(xs), max(ys)), "oben")


def t_rohr(ctx, e):
    pts = ctx.rechtwinklig(e["punkte"], e.get("route", "auto"))
    ctx.kante("rohr", pts, ctx._enden, weite=_zahl(e, "weite", 14), radius=_zahl(e, "radius", 12))
    ctx.z.rohr(pts, _zahl(e, "weite", 14), _zahl(e, "radius", 12))
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    w = _zahl(e, "weite", 14) / 2
    box = (min(xs) - w, min(ys) - w, max(xs) + w, max(ys) + w)
    ctx.melde(e, box)
    beschrifte(ctx, e, box, "oben")


_AUSR = {"links": "start", "mitte": "middle", "rechts": "end"}


def t_text(ctx, e):
    g = _zahl(e, "groesse", 12)
    box = ctx.z.text(float(e["x"]), float(e["y"]), str(e["text"]), g, _AUSR[e.get("ausrichtung", "links")],
                     bool(e.get("fett")), bool(e.get("kursiv")))
    ctx.melde(e, (box.x1, box.y1, box.x2, box.y2), klein=False)


def t_etikett(ctx, e):
    g = _zahl(e, "groesse", 12)
    x, y = float(e["x"]), float(e["y"])
    box = ctx.z.text(x, y, str(e["text"]), g, _AUSR[e.get("ausrichtung", "links")],
                     bool(e.get("fett")), bool(e.get("kursiv")))
    if e.get("ziel") is not None:
        zx, zy = ctx.punkt(e["ziel"])
        kandidaten = [(((box.x1 + box.x2) / 2, box.y1 - 2), False), (((box.x1 + box.x2) / 2, box.y2 + 2), False),
                      ((box.x1 - 3, (box.y1 + box.y2) / 2), True), ((box.x2 + 3, (box.y1 + box.y2) / 2), True)]
        ziel_id = ctx._anker_id
        (sx, sy), waagerecht = min(kandidaten, key=lambda k: math.hypot(k[0][0] - zx, k[0][1] - zy))
        pts, _ = ortho([(sx, sy), (zx, zy)], None, "hv" if waagerecht else "vh")
        ctx.kante("linie", pts, (None, ziel_id), stil="duenn", pfeil="kein", radius=0, schraeg=False, etikett=True)
        ctx.z.linienzug(pts, "duenn")
    ctx.melde(e, (box.x1, box.y1, box.x2, box.y2))


# ───────────────────────────── Behälter ─────────────────────────────

def t_behaelter(ctx, e):
    x, y, b, h = (float(e[k]) for k in ("x", "y", "b", "h"))
    form = e.get("form", "tank")
    fuell = e.get("fuellung", "weiss")
    z = ctx.z
    if form == "tank":
        niveau = e.get("fuellstand") is not None
        if niveau:
            ny = y + h * (1 - float(e["fuellstand"]))
            z.rechteck(x, y, x + b, y + h, "weiss", "keine")
            z.rechteck(x, ny, x + b, y + h, "hellgrau", "keine")
            z.linie(x, ny, x + b, ny, "duenn")
        huelle = "keine" if niveau else fuell
        if e.get("offen"):
            z.polygon([(x, y), (x, y + h), (x + b, y + h), (x + b, y)], huelle, "normal", geschlossen=False)
        else:
            z.rechteck(x, y, x + b, y + h, huelle, "normal")
    else:
        auslass = _zahl(e, "auslass", b * 0.4)
        kopf = _zahl(e, "kopf", h * 0.5) if form == "trichter" else 0.0
        pts = ([(x, y), (x + b, y), (x + b, y + kopf), (x + b / 2 + auslass / 2, y + h),
                (x + b / 2 - auslass / 2, y + h), (x, y + kopf)])
        z.polygon(pts, fuell, "normal")
    box = (x, y, x + b, y + h)
    ctx.melde(e, box)
    beschrifte(ctx, e, box, "unten")


# ───────────────────────────── Zylinder ─────────────────────────────

def t_zylinder(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    laenge, breite, stange = _zahl(e, "laenge", 110), _zahl(e, "breite", 36), _zahl(e, "stange", 56)
    ri = e.get("ausfahrt", "unten")
    senkrecht = ri in ("unten", "oben")
    w, h = (breite, laenge) if senkrecht else (laenge, breite)
    x2, y2 = x + w, y + h
    cx, cy = (x + x2) / 2, (y + y2) / 2
    werkzeug = e.get("werkzeug", "keine")
    tb, tt = _zahl(e, "werkzeug_b", breite * 1.5), 16.0
    z = ctx.z

    def P(u, v):
        if ri == "unten":
            return cx + v, y + u
        if ri == "oben":
            return cx + v, y2 - u
        if ri == "rechts":
            return x + u, cy + v
        return x2 - u, cy + v

    def viereck(u0, v0, u1, v1, fuellung, linie="normal"):
        z.polygon([P(u0, v0), P(u1, v0), P(u1, v1), P(u0, v1)], fuellung, linie)

    viereck(0, -breite / 2, laenge, breite / 2, "weiss")
    kappe = 6.0
    if e.get("feder"):
        n = max(2, round((laenge - 2 * kappe - 12) / 20))
        u0, u1 = kappe + 6, laenge - 6
        z.polygon([P(u0 + (u1 - u0) * i / n, (breite / 2 - 5) * (1 if i % 2 == 0 else -1)) for i in range(n + 1)],
                  "keine", "dick", geschlossen=False)
    viereck(0, -breite / 2 + 1, kappe, breite / 2 - 1, "schwarz", "keine")
    viereck(kappe, -3, laenge + stange, 3, "weiss")
    ende = laenge + stange
    if werkzeug == "platte":
        viereck(ende, -tb / 2, ende + tt, tb / 2, "grau")
        ende += tt
    elif werkzeug == "keil":
        z.polygon([P(ende, -tb / 2), P(ende, tb / 2), P(ende + tt, tb / 4), P(ende + tt, -tb / 4)], "grau")
        ende += tt
    pts = [P(0, -breite / 2), P(ende, breite / 2 if werkzeug == "keine" else tb / 2),
           P(ende, -(breite / 2 if werkzeug == "keine" else tb / 2))]
    gx, gy = [p[0] for p in pts], [p[1] for p in pts]
    gesamt = (min(gx), min(gy), max(gx), max(gy))
    gehaeuse = (x, y, x2, y2)
    extra = {"hinten": P(0, 0), "spitze": P(ende, 0)}

    ctx.melde(e, gesamt, klein=True, extra=extra, anker_box=gehaeuse)

    # Sensoren an der Gehäusewand (nach dem Zylinder in der Legende)
    seiten = set()
    ziel = {"links": (-1, 0), "rechts": (1, 0), "oben": (0, -1), "unten": (0, 1)}
    sensor_info = []
    for s in e.get("sensoren", []) or []:
        u = float(s.get("pos", 0.5)) * laenge
        dx, dy = ziel[s["seite"]]
        o0, o1 = P(u, 0), P(u, 1)
        s_v = 1 if (o1[0] - o0[0]) * dx + (o1[1] - o0[1]) * dy > 0 else -1
        if abs((o1[0] - o0[0]) * dx + (o1[1] - o0[1]) * dy) < 0.5:
            raise SpecFehler(f"Sensor '{s.get('id', '?')}': Seite '{s['seite']}' passt nicht zur Zylinderachse "
                             f"(ausfahrt: {ri})")
        seiten.add(s["seite"])
        sensor_info.append((s, u, s_v, dx, dy))
    hauptzelle = z.zelle
    for j, (s, u, s_v, dx, dy) in enumerate(sensor_info):
        z.zelle = f"{hauptzelle}s{j + 1}"
        z.polygon([P(u - 6, s_v * breite / 2), P(u + 6, s_v * breite / 2),
                   P(u + 6, s_v * (breite / 2 + 9)), P(u - 6, s_v * (breite / 2 + 9))], "schwarz")
        a, b_ = P(u, s_v * (breite / 2 + 9)), P(u, s_v * (breite / 2 + 9 + 24))
        z.linie(a[0], a[1], b_[0], b_[1], "duenn")
        sbox = (min(P(u - 6, s_v * breite / 2)[0], b_[0]), min(P(u - 6, s_v * breite / 2)[1], b_[1]),
                max(P(u + 6, s_v * (breite / 2 + 9))[0], b_[0]), max(P(u + 6, s_v * (breite / 2 + 9))[1], b_[1]))
        se = {"typ": "sensor", "art": "block", **s}
        ctx.melde(se, sbox, klein=True)
        zeilen = []
        if s.get("id"):
            zeilen.append((str(s["id"]), SCHRIFT_ID, False, False))
        if s.get("name"):
            zeilen.append((str(s["name"]), SCHRIFT_NAME, False, True))
        if zeilen:
            lage = s["seite"]
            block(ctx, zeilen, (b_[0], b_[1], b_[0], b_[1]), lage, 4)
    z.zelle = hauptzelle

    if e.get("lage") is None:
        if senkrecht:
            standard = "links" if "rechts" in seiten else "rechts"
        else:
            standard = "unten" if "oben" in seiten else "oben"
    else:
        standard = e["lage"]
    beschrifte(ctx, e, gehaeuse, standard)


# ───────────────────────────── Ventil, Sensor, Taster, Leuchte, Motor, Pumpe ─────────────────────────────

def t_ventil(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    g = _zahl(e, "groesse", 9)
    h = g * 1.3
    waagerecht = e.get("achse", "senkrecht") == "waagerecht"
    if waagerecht:
        hw, hh = h, g
        pts = [(x - hw, y - hh), (x - hw, y + hh), (x + hw, y - hh), (x + hw, y + hh)]
    else:
        hw, hh = g, h
        pts = [(x - hw, y - hh), (x + hw, y - hh), (x - hw, y + hh), (x + hw, y + hh)]
    z = ctx.z
    z.polygon(pts, "weiss", "normal")
    box = [x - hw, y - hh, x + hw, y + hh]
    spule = e.get("spule", "oben" if waagerecht else "rechts")
    bw, bh = 20.0, 14.0
    if spule != "keine":
        if spule == "rechts":
            z.linie(x + hw, y, x + hw + 12, y, "normal")
            sb = (x + hw + 12, y - bh / 2, x + hw + 12 + bw, y + bh / 2)
        elif spule == "links":
            z.linie(x - hw, y, x - hw - 12, y, "normal")
            sb = (x - hw - 12 - bw, y - bh / 2, x - hw - 12, y + bh / 2)
        elif spule == "oben":
            z.linie(x, y - hh, x, y - hh - 12, "normal")
            sb = (x - bh / 2, y - hh - 12 - bw, x + bh / 2, y - hh - 12)
        else:
            z.linie(x, y + hh, x, y + hh + 12, "normal")
            sb = (x - bh / 2, y + hh + 12, x + bh / 2, y + hh + 12 + bw)
        z.rechteck(*sb, "weiss", "normal")
        box = [min(box[0], sb[0]), min(box[1], sb[1]), max(box[2], sb[2]), max(box[3], sb[3])]
    extra = {"oben": (x, y - hh), "unten": (x, y + hh), "links": (x - hw, y), "rechts": (x + hw, y), "mitte": (x, y)}
    ctx.melde(e, tuple(box), klein=True, extra=extra)
    if e.get("lage") is None:
        if waagerecht:
            standard = "unten" if spule != "unten" else "oben"
        else:
            standard = "links" if spule != "links" else "rechts"
    else:
        standard = e["lage"]
    beschrifte(ctx, e, tuple(box), standard)


def t_sensor(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    art = e.get("art", "block")
    z = ctx.z
    stiel = e.get("stiel", "links" if art == "kontakt" else "keiner")
    laenge = 26.0 if art == "kontakt" else 16.0
    if art == "block":
        z.rechteck(x - 4, y - 6, x + 4, y + 6, "schwarz", "normal")
        box = (x - 4, y - 6, x + 4, y + 6)
    elif art == "rolle":
        z.kreis(x, y, 9, "weiss", "normal")
        box = (x - 9, y - 9, x + 9, y + 9)
    elif art == "lichtschranke":
        z.kreis(x, y, 11, "weiss", "normal")
        d = 11 * 0.707
        z.linie(x - d, y - d, x + d, y + d)
        z.linie(x - d, y + d, x + d, y - d)
        box = (x - 11, y - 11, x + 11, y + 11)
    elif art == "kontakt":
        z.kreis(x, y, 5, "weiss", "normal")
        box = (x - 5, y - 5, x + 5, y + 5)
    else:  # initiator
        z.rechteck(x - 11, y - 6, x + 11, y + 6, "grau", "normal")
        z.rechteck(x - 11, y - 6, x - 5, y + 6, "schwarz", "normal")
        box = (x - 11, y - 6, x + 11, y + 6)
    if stiel != "keiner":
        r = (box[2] - box[0]) / 2
        dx, dy = {"links": (-1, 0), "rechts": (1, 0), "oben": (0, -1), "unten": (0, 1)}[stiel]
        z.linie(x + dx * r, y + dy * r, x + dx * (r + laenge), y + dy * (r + laenge), "normal")
        box = (min(box[0], x + dx * (r + laenge)), min(box[1], y + dy * (r + laenge)),
               max(box[2], x + dx * (r + laenge)), max(box[3], y + dy * (r + laenge)))
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "unten" if stiel in ("links", "rechts", "keiner") else "rechts")


def t_taster(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    r = _zahl(e, "r", 14)
    symbol = e.get("symbol", "keins")
    z = ctx.z
    z.kreis(x, y, r, e.get("farbe", "weiss"))
    if symbol == "ring":
        z.kreis(x, y, r * 0.5, "weiss")
    elif symbol == "not_halt":
        z.kreis(x, y, r * 0.55, "mittelgrau")
    elif symbol in ("pfeil_auf", "pfeil_ab"):
        if symbol == "pfeil_auf":
            z.linienzug([(x, y + r * 0.55), (x, y - r * 0.55)], "dick", "ende")
        else:
            z.linienzug([(x, y - r * 0.55), (x, y + r * 0.55)], "dick", "ende")
    elif symbol == "doppelpfeil_auf":
        for dx in (-r * 0.28, r * 0.28):
            z.linienzug([(x + dx, y + r * 0.55), (x + dx, y - r * 0.55)], "dick", "ende")
    if e.get("text"):
        _innentext(ctx, str(e["text"]), x, y, max(8.0, r * 0.7))
    box = (x - r, y - r, x + r, y + r)
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "unten")


def t_leuchte(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    r = _zahl(e, "r", 13)
    z = ctx.z
    z.kreis(x, y, r, e.get("farbe", "weiss"))
    if e.get("text"):
        _innentext(ctx, str(e["text"]), x, y, max(8.0, r * 0.7))
    else:
        d = r * 0.707
        z.linie(x - d, y - d, x + d, y + d)
        z.linie(x - d, y + d, x + d, y - d)
    box = (x - r, y - r, x + r, y + r)
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "unten")


def t_motor(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    r = _zahl(e, "r", 24)
    ctx.z.kreis(x, y, r)
    _innentext(ctx, "M\n" + str(e.get("phasen", "3~")), x, y, r * 0.55)
    box = (x - r, y - r, x + r, y + r)
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "unten")


def t_pumpe(ctx, e):
    x, y = float(e["x"]), float(e["y"])
    r = _zahl(e, "r", 20)
    z = ctx.z
    z.kreis(x, y, r)
    pts = [(-0.45 * r, -0.55 * r), (-0.45 * r, 0.55 * r), (0.6 * r, 0.0)]
    winkel = {"rechts": 0, "unten": 90, "links": 180, "oben": 270}[e.get("richtung", "rechts")]
    a = math.radians(winkel)
    z.polygon([(x + px * math.cos(a) - py * math.sin(a), y + px * math.sin(a) + py * math.cos(a)) for px, py in pts],
              "weiss")
    box = (x - r, y - r, x + r, y + r)
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "unten")


# ───────────────────────────── Band, Bedienfeld, Ampel ─────────────────────────────

def t_band(ctx, e):
    x, y, b, h = (float(e[k]) for k in ("x", "y", "b", "h"))
    winkel = _zahl(e, "winkel", 0)
    cx, cy = x + b / 2, y + h / 2
    z = ctx.z
    if winkel:
        z.drehen(winkel, cx, cy)
    z.rechteck(x, y, x + b, y + h, "weiss", "normal", rundung=h / 2)
    if e.get("rollen", True):
        for rx in (x + h / 2, x + b - h / 2):
            z.kreis(rx, cy, h * 0.3)
    if winkel:
        z.drehen_ende()
    a = math.radians(winkel)

    def drehe(px, py):
        dx, dy = px - cx, py - cy
        return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)

    ecken = [drehe(px, py) for px, py in ((x, y), (x + b, y), (x + b, y + h), (x, y + h))]
    box = (min(p[0] for p in ecken), min(p[1] for p in ecken), max(p[0] for p in ecken), max(p[1] for p in ecken))
    extra = {"links": drehe(x + h / 2, cy), "rechts": drehe(x + b - h / 2, cy),
             "oben": drehe(cx, y), "unten": drehe(cx, y + h)}
    ctx.melde(e, box, klein=False, extra=extra)
    beschrifte(ctx, e, box, "unten")


def t_bedienfeld(ctx, e):
    x, y, b, h = (float(e[k]) for k in ("x", "y", "b", "h"))
    eintraege = [en for en in e["eintraege"]]
    spalten = int(e.get("spalten", 3))
    zeilen = max(1, math.ceil(len(eintraege) / spalten))
    ctx.z.rechteck(x, y, x + b, y + h, "weiss", "normal", rundung=_zahl(e, "rundung", 8))
    if e.get("titel"):
        ctx.z.text(x + b / 2, y - 8, str(e["titel"]), 12, "middle")
    zw, zh = b / spalten, h / zeilen
    box = (x, y, x + b, y + h)
    ctx.melde(e, box)
    hauptzelle = ctx.z.zelle
    for i, en in enumerate(eintraege):
        spalte, zeile = i % spalten, i // spalten
        kind = dict(en)
        if kind.get("typ") == "leer":
            continue
        kind["x"] = x + (spalte + 0.5) * zw
        kind["y"] = y + zeile * zh + zh * 0.42
        ctx.z.zelle = f"{hauptzelle}k{i + 1}"
        ZEICHNER[kind["typ"]](ctx, kind)
    ctx.z.zelle = hauptzelle


def t_ampel(ctx, e):
    x, y, b, h = (float(e[k]) for k in ("x", "y", "b", "h"))
    lampen = [str(l) for l in e["lampen"]]
    n = len(lampen)
    r = min(b / 2 - 4, h / n / 2 - 3)
    ctx.z.rechteck(x, y, x + b, y + h, "weiss", "normal")
    for i, text in enumerate(lampen):
        cy = y + (i + 0.5) * h / n
        ctx.z.kreis(x + b / 2, cy, r)
        _innentext(ctx, text, x + b / 2, cy, max(8.0, r * 0.75))
    box = (x, y, x + b, y + h)
    ctx.melde(e, box, klein=True)
    beschrifte(ctx, e, box, "rechts")


def t_knoten(ctx, e):
    """Verbindungspunkt (ausgefüllter Punkt) an einem Anker oder bei [x, y]."""
    x, y = ctx.punkt(e["punkt"])
    r = _zahl(e, "r", 2.8)
    ctx.z.kreis(x, y, r, "schwarz", "keine")
    ctx.melde(e, (x - r, y - r, x + r, y + r))


def t_symbol(ctx, e):
    sym = symbole.SYMBOLE.get(e["symbol"])
    if sym is None:
        raise SpecFehler(f"unbekanntes Symbol '{e['symbol']}' (Liste: edu-technologieschema symbole)")
    bet = e.get("betaetigung")
    if bet and sym.wirk is None:
        raise SpecFehler(f"Das Zeichen '{sym.name}' hat keine Wirkverbindung – 'betaetigung' gibt es nur bei Kontakten "
                         f"(schliesser, oeffner, … ohne Betätigungszusatz)")
    rahmen, anker = symbole.zeichne(ctx.z, sym, float(e["x"]), float(e["y"]), int(e.get("drehung", 0)),
                                    bool(e.get("spiegeln")), _zahl(e, "groesse", 1.0), e.get("text"), bet,
                                    _zahl(e, "wirklaenge", 2.0))
    ctx.melde(e, rahmen, klein=True, extra=anker)
    breit = (rahmen[2] - rahmen[0]) > (rahmen[3] - rahmen[1])
    beschrifte(ctx, e, rahmen, "unten" if breit else "rechts")


ZEICHNER = {
    "rechteck": t_rechteck, "kreis": t_kreis, "polygon": t_polygon, "linie": t_linie, "rohr": t_rohr,
    "text": t_text, "etikett": t_etikett, "behaelter": t_behaelter, "zylinder": t_zylinder, "ventil": t_ventil,
    "sensor": t_sensor, "taster": t_taster, "leuchte": t_leuchte, "motor": t_motor, "pumpe": t_pumpe,
    "band": t_band, "bedienfeld": t_bedienfeld, "ampel": t_ampel, "symbol": t_symbol, "knoten": t_knoten,
}
assert set(ZEICHNER) == set(SCHEMA)
