"""
symbole — Schaltzeichen der Elektrotechnik und Mechatronik (DIN EN 60617 / IEC 60617).

Jedes Zeichen ist aus Grundformen auf einem Raster gezeichnet (eigene Zeichnung nach der
Formensprache der Norm; keine Kopie fremder Dateien). Ein Rasterschritt (Einheit) sind 10 Pixel
bei ``groesse: 1``. Der Ursprung (0, 0) ist die Mitte des Zeichens; y zeigt nach unten.

Jedes Zeichen kennt

* seine **Anschlusspunkte** (``an1``, ``an2`` …), an denen Linien über Anker enden
  (``"-S1@an1"``), auch nach Drehen und Spiegeln,
* die **Klassen** des Referenzkennzeichens, die zu ihm passen (Schließer als Taster → S, als
  Schützkontakt → Q, als Relaiskontakt → K),
* seine **Herkunft**: ``liste`` = Form mit dem Zeichen der Wikipedia-Liste der Schaltzeichen
  (Elektrik/Elektronik) abgeglichen, ``fachwissen`` = nach Lehrbuch-Formensprache gezeichnet, **vor
  dem Einsatz mit Norm oder eingeführtem Tabellenbuch abgleichen** 🔎.

Primitive (Koordinaten in Einheiten): ``("l", [(x, y), …])`` Linienzug, ``("d", [...])``
gestrichelt, ``("f", [...])`` dicke Linie, ``("r", x1, y1, x2, y2, fuellung)`` Rechteck,
``("c", x, y, r, fuellung)`` Kreis, ``("p", [...], fuellung)`` Vieleck, ``("b", x, y, r, w0, w1)`` Bogen
(Winkel in Grad, 0 = rechts, 90 = unten), ``("t", x, y, text, groesse)`` Text (bleibt beim Drehen
aufrecht).
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

EINHEIT = 10.0   # Pixel je Rasterschritt bei groesse 1


@dataclass(frozen=True)
class Symbol:
    name: str
    titel: str
    kategorie: str
    klassen: str                  # passende Klassen des Referenzkennzeichens, z. B. "SKQ"
    herkunft: str                 # "liste" | "zusammengesetzt" | "fachwissen"
    prims: tuple
    anschluesse: dict = field(default_factory=dict)
    rahmen: tuple = (-1.5, -3.0, 1.5, 3.0)      # x1, y1, x2, y2 in Einheiten (für Beschriftung und Prüfung)
    norm: str = ""                # Zeichennummer der EN-60617-Reihe, wenn die Quelle sie nennt
    hinweis: str = ""
    wirk: tuple | None = None     # Punkt der Wirkverbindung (Klingenmitte) für Betätigungsarten
    quelle: str = "Wikipedia-Liste der Schaltzeichen"


#: Herkunft: Form gegen eine Vorlage abgeglichen (liste), aus abgeglichenen Teilen zusammengesetzt
#: (zusammengesetzt) oder nach Lehrbuch gezeichnet (fachwissen, vor dem Einsatz prüfen)
GEPRUEFT = ("liste", "zusammengesetzt")


@dataclass(frozen=True)
class Betaetigung:
    """Betätigungsart: Endzeichen einer gestrichelten Wirkverbindung (Ursprung = Anschluss der Wirkverbindung)."""
    name: str
    titel: str
    prims: tuple
    breite: float                 # Ausdehnung nach links in Einheiten
    hoehe: float = 1.0            # halbe Höhe
    quelle: str = "elektricks.com, Betätigungsarten nach DIN EN 60617-7"
    hinweis: str = ""


BETAETIGUNGEN: dict[str, Betaetigung] = {}


SYMBOLE: dict[str, Symbol] = {}


def _breg(**kw) -> None:
    b = Betaetigung(**kw)
    assert b.name not in BETAETIGUNGEN, b.name
    BETAETIGUNGEN[b.name] = b


def _reg(**kw) -> None:
    s = Symbol(**kw)
    assert s.name not in SYMBOLE, s.name
    SYMBOLE[s.name] = s


# ───────────────────────────── Zeichnen ─────────────────────────────

def transformiere(p, drehung: int, spiegeln: bool, groesse: float, mx: float, my: float):
    """Punkt aus Zeichen-Einheiten in Bildkoordinaten."""
    x, y = p
    if spiegeln:
        x = -x
    for _ in range((drehung // 90) % 4):          # im Uhrzeigersinn (y zeigt nach unten)
        x, y = -y, x
    return mx + x * EINHEIT * groesse, my + y * EINHEIT * groesse


def _verschiebe(prims, dx: float, dy: float):
    """Primitive um (dx, dy) verschieben."""
    res = []
    for pr in prims:
        a = pr[0]
        if a in ("l", "d", "f"):
            res.append((a, [(x + dx, y + dy) for x, y in pr[1]]))
        elif a == "r":
            res.append((a, pr[1] + dx, pr[2] + dy, pr[3] + dx, pr[4] + dy, pr[5]))
        elif a == "c":
            res.append((a, pr[1] + dx, pr[2] + dy, pr[3], pr[4]))
        elif a == "p":
            res.append((a, [(x + dx, y + dy) for x, y in pr[1]], pr[2]))
        elif a == "b":
            res.append((a, pr[1] + dx, pr[2] + dy, *pr[3:]))
        elif a == "t":
            res.append((a, pr[1] + dx, pr[2] + dy, *pr[3:]))
    return tuple(res)


def mit_betaetigung(sym: Symbol, bet: str, laenge: float = 2.0):
    """(Primitive, Rahmen) eines Kontakts mit Betätigungsart: gestrichelte Wirkverbindung nach links."""
    if sym.wirk is None:
        raise ValueError(f"Das Zeichen '{sym.name}' hat keine Wirkverbindung – Betätigungsarten gibt es nur bei Kontakten")
    b = BETAETIGUNGEN[bet]
    wx, wy = sym.wirk
    prims = (*sym.prims, ("d", [(wx, wy), (wx - laenge, wy)]), *_verschiebe(b.prims, wx - laenge, wy))
    x1, y1, x2, y2 = sym.rahmen
    return prims, (min(x1, wx - laenge - b.breite - 0.2), min(y1, wy - b.hoehe), x2, max(y2, wy + b.hoehe))


def zeichne(z, sym: Symbol, mx: float, my: float, drehung: int = 0, spiegeln: bool = False,
            groesse: float = 1.0, text: str | None = None, betaetigung: str | None = None,
            wirklaenge: float = 2.0):
    """Zeichen in die Zeichnung ``z`` setzen. Gibt (Rahmen, Anker) in Bildkoordinaten zurück."""
    T = lambda p: transformiere(p, drehung, spiegeln, groesse, mx, my)  # noqa: E731
    prims, symrahmen = sym.prims, sym.rahmen
    if betaetigung:
        prims, symrahmen = mit_betaetigung(sym, betaetigung, wirklaenge)
    for pr in prims:
        art = pr[0]
        if art in ("l", "d", "f"):
            pts = [T(p) for p in pr[1]]
            linie = {"l": "normal", "d": "gestrichelt", "f": "dick"}[art]
            z.linienzug(pts, linie)
        elif art == "r":
            x1, y1, x2, y2, fuell = pr[1:]
            z.polygon([T((x1, y1)), T((x2, y1)), T((x2, y2)), T((x1, y2))], fuell, "normal")
        elif art == "c":
            cx, cy = T((pr[1], pr[2]))
            z.kreis(cx, cy, pr[3] * EINHEIT * groesse, pr[4], "normal")
        elif art == "p":
            z.polygon([T(p) for p in pr[1]], pr[2], "normal")
        elif art == "b":
            _, cx, cy, r, w0, w1 = pr
            n = max(6, int(abs(w1 - w0) / 15))
            pts = [T((cx + r * math.cos(math.radians(w0 + (w1 - w0) * i / n)),
                      cy + r * math.sin(math.radians(w0 + (w1 - w0) * i / n)))) for i in range(n + 1)]
            z.linienzug(pts, "normal")
        elif art == "t":
            tx, ty = T((pr[1], pr[2]))
            s = text if (text is not None and pr[3] == "@") else pr[3]
            g = pr[4] * EINHEIT * groesse
            z.text(tx, ty + g * 0.35, s, g, "middle")
    x1, y1, x2, y2 = symrahmen
    ecken = [T(p) for p in ((x1, y1), (x2, y1), (x2, y2), (x1, y2))]
    rahmen = (min(p[0] for p in ecken), min(p[1] for p in ecken), max(p[0] for p in ecken), max(p[1] for p in ecken))
    anker = {n: T(p) for n, p in sym.anschluesse.items()}
    return rahmen, anker


# ───────────────────────────── Katalog ─────────────────────────────
# Die Zeichen sind in ihrer natürlichen Lage (wie in der Wikipedia-Liste) gezeichnet; Drehen mit ``drehung``.

def _kontakt_anschluesse():
    return {"an1": (0, -3), "an2": (0, 3)}


# Maße der Kontakte (aus der Wikipedia-Liste in Rasterschritten abgelesen):
# Anschluss oben/unten auf der Achse x = 0, Klinge um 0,95 Einheiten geneigt.
_SCHLIESSER = (("l", [(0, -3), (0, -1.45)]), ("l", [(0, 3), (0, 1.45)]), ("l", [(0, 1.45), (-0.95, -1.4)]))
_OEFFNER = (("l", [(0, -3), (0, -0.81), (0.93, -0.81)]), ("l", [(0, 3), (0, 1.4)]), ("l", [(0, 1.4), (0.93, -1.4)]))
_BOGEN_SCHLIESSER = ("b", 0, -1.78, 0.31, 90, 270)      # Halbkreis links am festen Anschluss (Schaltvermögen)
_BOGEN_OEFFNER = ("b", 0, -1.12, 0.31, -90, 90)
_DREIECK_SCHLIESSER = ("p", [(-0.88, -1.07), (-1.36, -0.9), (-0.52, -0.17)], "weiss")   # Grundlinie auf der Klinge
_DREIECK_OEFFNER = ("p", [(0.05, -0.45), (0.26, 0.62), (0.55, -0.24)], "weiss")

_reg(name="schliesser", titel="Schließer", kategorie="Kontakte", klassen="SBKQF", herkunft="liste",
     prims=_SCHLIESSER, anschluesse=_kontakt_anschluesse(),
     hinweis="allgemeiner Schalter; schließt, wenn betätigt")
_reg(name="oeffner", titel="Öffner", kategorie="Kontakte", klassen="SBKQF", herkunft="liste",
     prims=_OEFFNER, anschluesse=_kontakt_anschluesse(), hinweis="öffnet, wenn betätigt")
_reg(name="schliesser_schuetz", titel="Schließer eines Schützes", kategorie="Kontakte", klassen="QK", herkunft="liste",
     prims=(*_SCHLIESSER, _BOGEN_SCHLIESSER), anschluesse=_kontakt_anschluesse(),
     hinweis="Halbkreis: Schaltgerät mit Schaltvermögen (Leistungskontakt)")
_reg(name="oeffner_schuetz", titel="Öffner eines Schützes", kategorie="Kontakte", klassen="QK", herkunft="liste",
     prims=(*_OEFFNER, _BOGEN_OEFFNER), anschluesse=_kontakt_anschluesse())
_reg(name="positionsschalter_schliesser", titel="Positionsschalter, Schließer", kategorie="Kontakte",
     klassen="BS", herkunft="liste", prims=(*_SCHLIESSER, _DREIECK_SCHLIESSER), anschluesse=_kontakt_anschluesse(),
     hinweis="in der Wikipedia-Liste „Grenzschalter“; Dreieck an der Klinge: Betätigung durch die Position")
_reg(name="positionsschalter_oeffner", titel="Positionsschalter, Öffner", kategorie="Kontakte",
     klassen="BS", herkunft="liste", prims=(*_OEFFNER, _DREIECK_OEFFNER), anschluesse=_kontakt_anschluesse())
_WECHSLER = (("l", [(-1.6, -3), (-1.6, -0.45), (-0.375, -0.45)]), ("l", [(0, -3), (0, -1.45)]),
             ("l", [(0, 3), (0, 1.45)]), ("l", [(0, 1.45), (-0.94, -1.42)]))
_reg(name="wechsler", titel="Wechsler (mit Unterbrechung)", kategorie="Kontakte", klassen="SBKQ", herkunft="liste",
     prims=_WECHSLER, anschluesse={"an1": (-1.6, -3), "an2": (0, -3), "an3": (0, 3)}, rahmen=(-1.8, -3, 1.0, 3),
     hinweis="an3 = Mittelanschluss; an1 Öffnerseite, an2 Schließerseite")
_reg(name="wechsler_ohne_unterbrechung", titel="Wechsler (ohne Unterbrechung)", kategorie="Kontakte", klassen="SBKQ",
     herkunft="liste", prims=(*_WECHSLER, ("l", [(-1.4, -1.24), (-0.52, -1.52)])),
     anschluesse={"an1": (-1.6, -3), "an2": (0, -3), "an3": (0, 3)}, rahmen=(-1.8, -3, 1.0, 3),
     hinweis="Querstrich an der Klinge: Überlappung, kein Unterbrechen beim Umschalten")

# Schaltgeräte: Zeichen am festen Anschluss (Schließer-Grundform)
_reg(name="leistungsschalter", titel="Leistungsschalter", kategorie="Schaltgeräte", klassen="Q", herkunft="liste",
     prims=(*_SCHLIESSER, ("l", [(-0.35, -1.8), (0.35, -1.1)]), ("l", [(-0.35, -1.1), (0.35, -1.8)])),
     anschluesse=_kontakt_anschluesse(), hinweis="Kreuz am Anschluss: selbsttätige Auslösung möglich (Schaltgerät)")
_reg(name="trennschalter", titel="Trennschalter", kategorie="Schaltgeräte", klassen="Q", herkunft="liste",
     prims=(*_SCHLIESSER, ("l", [(-0.3, -1.45), (0.3, -1.45)])), anschluesse=_kontakt_anschluesse())
_reg(name="lasttrennschalter", titel="Lasttrennschalter", kategorie="Schaltgeräte", klassen="Q", herkunft="liste",
     prims=(*_SCHLIESSER, ("l", [(-0.3, -1.45), (0.3, -1.45)]), ("b", 0, -1.16, 0.3, 0, 360)),
     anschluesse=_kontakt_anschluesse(), hinweis="Kreis: Schaltvermögen (Last schalten)")

# Selbsttätiger Rückgang (Feder): gefülltes Dreieck am festen Anschluss – Grundlage der Taster
_TRI_SCHLIESSER = ("p", [(-0.72, -1.81), (0, -2.16), (0, -1.44)], "schwarz")
_reg(name="schliesser_rueckgang", titel="Schließer mit selbsttätigem Rückgang", kategorie="Kontakte", klassen="SBK",
     herkunft="liste", prims=(*_SCHLIESSER, _TRI_SCHLIESSER), anschluesse=_kontakt_anschluesse(),
     hinweis="Dreieck: Rückgang in die Ruhelage nach Loslassen (Feder), die Grundform des Tasters")
_reg(name="oeffner_rueckgang", titel="Öffner mit selbsttätigem Rückgang", kategorie="Kontakte", klassen="SBK",
     herkunft="liste",
     prims=(("l", [(0, -3), (0, -0.75)]), ("l", [(0, 3), (0, 1.4)]), ("l", [(0, 1.4), (0.94, -1.4)]),
            ("p", [(0.72, -1.12), (0, -1.5), (0, -0.75)], "schwarz")),
     anschluesse=_kontakt_anschluesse(), hinweis="das Dreieck ersetzt den Fuß des Öffners")

# Antriebe und Auslöser
_reg(name="spule", titel="Spule (Relais, Schütz, Magnetventil)", kategorie="Antriebe", klassen="QKM", herkunft="liste",
     prims=(("l", [(0, -3), (0, -1.125)]), ("l", [(0, 1.125), (0, 3)]), ("r", -1.875, -1.125, 1.875, 1.125, "weiss")),
     anschluesse={"an1": (0, -3), "an2": (0, 3)}, rahmen=(-1.9, -3, 1.9, 3), norm="07-15-01",
     hinweis="elektromechanischer Antrieb; Relais -K, Schütz -Q, Ventilspule -MB")
_reg(name="thermorelais", titel="Thermisches Überlastrelais (Bimetall)", kategorie="Antriebe", klassen="F", herkunft="liste",
     prims=(("r", -2.27, -1.1, 2.27, 1.17, "weiss"), ("l", [(0, -3), (0, -0.73), (-1.14, -0.73), (-1.14, 0.79), (0, 0.79), (0, 3)])),
     anschluesse={"an1": (0, -3), "an2": (0, 3)}, rahmen=(-2.3, -3, 2.3, 3),
     hinweis="Bügel im Rechteck: Bimetall; Auslösung des Motorschutzes")

# ── Bauelemente ────────────────────────────────────────────────────
def _pfeilkopf(sx, sy, bx, by, laenge=0.45, breite=0.2):
    """Spitze bei (sx, sy), Richtung von (bx, by) her."""
    dx, dy = sx - bx, sy - by
    d = math.hypot(dx, dy) or 1.0
    ux, uy = dx / d, dy / d
    px, py = -uy * breite, ux * breite
    mx, my = sx - ux * laenge, sy - uy * laenge
    return [(sx, sy), (mx + px, my + py), (mx - px, my - py)]


_HORIZ = {"an1": (-2.5, 0), "an2": (2.5, 0)}
_RAHMEN_H = (-2.5, -1.3, 2.5, 1.3)

_reg(name="widerstand", titel="Widerstand", kategorie="Bauelemente", klassen="R", herkunft="fachwissen",
     prims=(("l", [(-2.5, 0), (-1.5, 0)]), ("l", [(1.5, 0), (2.5, 0)]), ("r", -1.5, -0.6, 1.5, 0.6, "weiss")),
     anschluesse=_HORIZ, rahmen=_RAHMEN_H, norm="04-01-01")
_reg(name="kondensator", titel="Kondensator", kategorie="Bauelemente", klassen="C", herkunft="fachwissen",
     prims=(("l", [(-2.5, 0), (-0.3, 0)]), ("l", [(0.3, 0), (2.5, 0)]), ("l", [(-0.3, -1.1), (-0.3, 1.1)]),
            ("l", [(0.3, -1.1), (0.3, 1.1)])), anschluesse=_HORIZ, rahmen=_RAHMEN_H, norm="04-02-01")
_reg(name="induktivitaet", titel="Induktivität (Spule, Drossel)", kategorie="Bauelemente", klassen="R", herkunft="fachwissen",
     prims=(("l", [(-2.5, 0), (-2.0, 0)]), ("l", [(2.0, 0), (2.5, 0)]),
            *[("b", -1.5 + i, 0, 0.5, 180, 360) for i in range(4)]),
     anschluesse=_HORIZ, rahmen=_RAHMEN_H, hinweis="vier Halbkreise (Wicklung)")
_DIODE = (("l", [(-2.6, 0), (-0.89, 0)]), ("l", [(0.89, 0), (2.6, 0)]),
          ("p", [(-0.89, -1), (-0.89, 1), (0.89, 0)], "weiss"), ("l", [(0.89, -1), (0.89, 1)]))
_reg(name="diode", titel="Diode", kategorie="Bauelemente", klassen="R", herkunft="liste", prims=_DIODE,
     anschluesse={"an1": (-2.6, 0), "an2": (2.6, 0)}, rahmen=(-2.6, -1.3, 2.6, 1.3), norm="05-03-01",
     hinweis="an1 Anode, an2 Kathode")
_reg(name="led", titel="Leuchtdiode (LED)", kategorie="Bauelemente", klassen="RPE", herkunft="liste",
     prims=(*_DIODE, ("l", [(0.17, -0.9), (-0.45, -1.8)]), ("p", _pfeilkopf(-0.66, -2.03, 0.17, -0.9), "schwarz"),
            ("l", [(0.56, -1.23), (-0.05, -2.1)]), ("p", _pfeilkopf(-0.28, -2.35, 0.56, -1.23), "schwarz")),
     anschluesse={"an1": (-2.6, 0), "an2": (2.6, 0)}, rahmen=(-2.6, -2.4, 2.6, 1.3), norm="05-03-02",
     hinweis="an1 Anode, an2 Kathode")
_reg(name="sicherung", titel="Sicherung", kategorie="Bauelemente", klassen="F", herkunft="fachwissen",
     prims=(("r", -2, -0.6, 2, 0.6, "weiss"), ("l", [(-3, 0), (3, 0)])),
     anschluesse={"an1": (-3, 0), "an2": (3, 0)}, rahmen=(-3, -1.3, 3, 1.3), hinweis="Rechteck mit durchgehender Linie")
_reg(name="meldeleuchte", titel="Meldeleuchte", kategorie="Melden", klassen="PE", herkunft="fachwissen",
     prims=(("l", [(0, -3), (0, -1)]), ("l", [(0, 1), (0, 3)]), ("c", 0, 0, 1, "weiss"),
            ("l", [(-0.707, -0.707), (0.707, 0.707)]), ("l", [(-0.707, 0.707), (0.707, -0.707)])),
     anschluesse={"an1": (0, -3), "an2": (0, 3)}, rahmen=(-1.2, -3, 1.2, 3), hinweis="Kreis mit Kreuz")
_motor_prims = lambda phase, leitungen: (   # noqa: E731
    ("c", 0, 0, 1.6, "weiss"), ("t", 0, -0.45, "M", 0.95), ("t", 0, 0.65, phase, 0.8),
    *[("l", [(x, -1.6 if abs(x) < 1 else -1.48), (x, -2.6)]) for x in leitungen])
_reg(name="motor_drehstrom", titel="Drehstrommotor", kategorie="Antriebe", klassen="M", herkunft="fachwissen",
     prims=_motor_prims("3~", (-0.8, 0, 0.8)), anschluesse={"an1": (-0.8, -2.6), "an2": (0, -2.6), "an3": (0.8, -2.6)},
     rahmen=(-1.7, -2.6, 1.7, 1.7), hinweis="Kreis mit M und Stromart; an1 bis an3 = U1, V1, W1")
_reg(name="motor_wechselstrom", titel="Wechselstrommotor", kategorie="Antriebe", klassen="M", herkunft="fachwissen",
     prims=_motor_prims("1~", (-0.5, 0.5)), anschluesse={"an1": (-0.5, -2.6), "an2": (0.5, -2.6)},
     rahmen=(-1.7, -2.6, 1.7, 1.7))
_reg(name="motor_gleichstrom", titel="Gleichstrommotor", kategorie="Antriebe", klassen="M", herkunft="fachwissen",
     prims=_motor_prims("=", (-0.5, 0.5)), anschluesse={"an1": (-0.5, -2.6), "an2": (0.5, -2.6)},
     rahmen=(-1.7, -2.6, 1.7, 1.7))

_reg(name="masse", titel="Masse, Gehäuse", kategorie="Erdung", klassen="X", herkunft="liste",
     prims=(("l", [(0, -2), (0, 0)]), ("l", [(-1.2, 0), (1.2, 0)]), ("l", [(-1.2, 0), (-1.6, 0.75)]),
            ("l", [(0, 0), (-0.4, 0.75)]), ("l", [(1.2, 0), (0.8, 0.75)])),
     anschluesse={"an1": (0, -2)}, rahmen=(-1.7, -2, 1.3, 0.8), norm="02-15-04", hinweis="IEC 60417-5020")


# ── Betätigungsarten (Wirkverbindung nach links, Endzeichen am Ursprung) ───────────────
def _ellipse(cx, cy, rx, ry, n=20):
    return [(cx + rx * math.cos(2 * math.pi * k / n), cy + ry * math.sin(2 * math.pi * k / n)) for k in range(n)]


_STIEL = lambda x: ("l", [(0, 0), (x, 0)])    # noqa: E731
_BALKEN = lambda x, h=0.6: ("l", [(x, -h), (x, h)])    # noqa: E731
_RAUTE = (("p", [(0, 0), (-1, -1), (-2, 0), (-1, 1)], "weiss"),
          ("l", [(-1.25, -0.75), (-1.25, 0.75)]), ("l", [(-0.75, -0.75), (-0.75, 0.75)]))

_breg(name="hand", titel="Handbetätigung, allgemein", prims=(_STIEL(-0.7), _BALKEN(-0.7)), breite=0.7)
_breg(name="kippen", titel="Betätigung durch Kippen", prims=(_STIEL(-0.7), _BALKEN(-0.7), ("l", [(-1.0, -0.6), (-0.4, -0.6)])),
      breite=1.0)
_breg(name="drucken", titel="Betätigung durch Drücken (Drucktaster)",
      prims=(_STIEL(-0.7), _BALKEN(-0.7), ("l", [(-0.7, -0.6), (-0.3, -0.6)]), ("l", [(-0.7, 0.6), (-0.3, 0.6)])), breite=0.7)
_breg(name="ziehen", titel="Betätigung durch Ziehen",
      prims=(_STIEL(-0.6), _BALKEN(-0.6), ("l", [(-0.6, -0.6), (-1.0, -0.6)]), ("l", [(-0.6, 0.6), (-1.0, 0.6)])), breite=1.0)
_breg(name="drehen", titel="Betätigung durch Drehen",
      prims=(_STIEL(-0.7), _BALKEN(-0.7), ("l", [(-0.7, -0.6), (-0.3, -0.6)]), ("l", [(-0.7, 0.6), (-1.1, 0.6)])), breite=1.1)
_breg(name="not_aus", titel="Betätigung durch Drücken, Not-Aus (Pilz)",
      prims=(_STIEL(-0.6), _BALKEN(-0.6), ("b", -0.6, 0, 0.6, 90, 270)), breite=1.2,
      hinweis="Pilzkopf; die Rastung (Verriegelung) zeigt die Quelle nicht")
_breg(name="thermisch", titel="Betätigung durch thermischen Effekt",
      prims=(_STIEL(-0.6), ("l", [(-1.0, -0.85), (-1.0, -0.5), (-0.6, -0.5), (-0.6, 0.5), (-1.0, 0.5), (-1.0, 0.85)])),
      breite=1.0, hoehe=0.85)
_breg(name="annaehern", titel="Betätigung durch Annähern", prims=_RAUTE, breite=2.0)
_breg(name="beruehren", titel="Betätigung durch Berühren", prims=(*_RAUTE, ("l", [(-2.0, -0.8), (-2.0, 0.8)])), breite=2.0)
_breg(name="annaehern_eisen", titel="Betätigung durch Annähern von Eisen", prims=(*_RAUTE, ("t", -3.1, 0, "Fe", 1.0)),
      breite=3.8, quelle="gallery.proficad.com, Zeichen 07-20-04 der EN-60617-Reihe")
_breg(name="annaehern_magnet", titel="Betätigung durch Annähern eines Magneten",
      prims=(*_RAUTE, ("p", [(-3.5, -0.8), (-2.7, -0.8), (-2.7, -0.45), (-3.15, -0.45), (-3.15, 0.45), (-2.7, 0.45),
                             (-2.7, 0.8), (-3.5, 0.8)], "schwarz")),
      breite=3.6, quelle="gallery.proficad.com, Zeichen 07-20-03 der EN-60617-Reihe")
_breg(name="handrad", titel="Betätigung durch Handrad",
      prims=(("c", -0.8, 0, 0.8, "weiss"), ("l", [(-0.8, 0), (-0.8, -0.8)]), ("l", [(-0.8, 0), (-0.11, 0.4)]),
             ("l", [(-0.8, 0), (-1.49, 0.4)])), breite=1.6, hoehe=0.8)
_breg(name="fuss", titel="Betätigung durch Fuß",
      prims=(("l", [(-1.46, 0.16), (-0.66, 0.96), (1.02, -1.52)]),), breite=1.5, hoehe=1.5)
_breg(name="schluessel", titel="Betätigung durch Schlüssel",
      prims=(_STIEL(-0.4), ("c", -0.55, -0.35, 0.3, "weiss"), ("p", [(-0.7, -0.05), (-0.4, -0.05), (-0.25, 0.75), (-0.85, 0.75)], "weiss")),
      breite=0.9, hoehe=0.75)
_breg(name="nocken", titel="Betätigung durch Nockensteuerung",
      prims=(("l", [(-0.85, -0.85), (-0.85, 0), (0, 0)]), ("b", -0.85, 0, 0.85, 270, 0)), breite=1.7, hoehe=0.85)
_breg(name="pegel", titel="Betätigung durch Flüssigkeitspegel",
      prims=(_STIEL(-0.25), ("p", _ellipse(-0.8, 0, 0.55, 0.35), "weiss"), ("l", [(-0.8, -0.35), (-0.8, -0.75)])),
      breite=1.35, hoehe=0.75)
_breg(name="motor", titel="Antrieb durch Elektromotor",
      prims=(("c", -0.8, 0, 0.8, "weiss"), ("t", -0.8, 0, "M", 1.0)), breite=1.6, hoehe=0.8)
_breg(name="elektromagnet", titel="Elektromagnetischer Antrieb",
      prims=(("r", -2.1, -0.55, 0, 0.55, "weiss"), ("l", [(-1.05, -1.0), (-1.05, 1.0)])), breite=2.1)

# Kontakte erhalten ihren Punkt für die Wirkverbindung (Klingenmitte)
import dataclasses as _dc  # noqa: E402

for _n in ("schliesser", "schliesser_schuetz", "schliesser_rueckgang", "wechsler", "wechsler_ohne_unterbrechung",
           "leistungsschalter", "trennschalter", "lasttrennschalter"):
    SYMBOLE[_n] = _dc.replace(SYMBOLE[_n], wirk=(-0.47, 0.02))
for _n in ("oeffner", "oeffner_schuetz", "oeffner_rueckgang"):
    SYMBOLE[_n] = _dc.replace(SYMBOLE[_n], wirk=(0.47, 0.0))


def _komp(name, titel, kategorie, basis, bet, klassen, laenge=2.0, herkunft="zusammengesetzt", **kw):
    b = SYMBOLE[basis]
    prims, rahmen = mit_betaetigung(b, bet, laenge)
    _reg(name=name, titel=titel, kategorie=kategorie, klassen=klassen, herkunft=herkunft, prims=prims,
         anschluesse=b.anschluesse, rahmen=rahmen, **kw)


_ZUSAMMEN = "zusammengesetzt aus Zeichen der Wikipedia-Liste und der Betätigungsarten (elektricks.com)"
_komp("taster_schliesser", "Taster, Schließer (handbetätigt)", "Taster", "schliesser_rueckgang", "hand", "S",
      quelle=_ZUSAMMEN, hinweis="Schließer mit Rückgang plus Handbetätigung")
_komp("taster_oeffner", "Taster, Öffner (handbetätigt)", "Taster", "oeffner_rueckgang", "hand", "S", quelle=_ZUSAMMEN)
_komp("drucktaster_schliesser", "Drucktaster, Schließer", "Taster", "schliesser_rueckgang", "drucken", "S",
      quelle=_ZUSAMMEN, hinweis="Betätigung durch Drücken")
_komp("drucktaster_oeffner", "Drucktaster, Öffner", "Taster", "oeffner_rueckgang", "drucken", "S", quelle=_ZUSAMMEN)
_komp("notaus_taster", "Not-Halt-Taster (Pilz, Öffner)", "Taster", "oeffner_rueckgang", "not_aus", "S", quelle=_ZUSAMMEN,
      hinweis="Pilz-Betätigung; die Rastung (Verriegelung) zeigt die Quelle nicht – bei Bedarf im Text nennen")

# Näherungsschalter und -sensoren (ProfiCAD-Galerie mit Zeichennummern der EN-60617-Reihe, Teil 7)
_PC = "gallery.proficad.com, Zeichen der EN-60617-Reihe (Teil 7)"
_komp("naeherungsschalter_schliesser", "Näherungsschalter, Schließer", "Näherungsschalter", "schliesser", "annaehern",
      "B", laenge=1.2, herkunft="liste", norm="07-20-02", quelle=_PC,
      hinweis="Rhombus: Näherung; die Wirkverbindung ist kurz")
_komp("naeherungsschalter_oeffner", "Näherungsschalter, Öffner", "Näherungsschalter", "oeffner", "annaehern", "B",
      laenge=1.2, quelle=_ZUSAMMEN, hinweis="Öffner-Gegenstück zu 07-20-02")
_komp("naeherungsschalter_eisen_oeffner", "Näherungsschalter, Öffner, Betätigung durch Eisen", "Näherungsschalter",
      "oeffner", "annaehern_eisen", "B", laenge=1.2, herkunft="liste", norm="07-20-04", quelle=_PC)
_komp("naeherungsschalter_magnet_schliesser", "Näherungsschalter, Schließer, Betätigung durch Magnet",
      "Näherungsschalter", "schliesser", "annaehern_magnet", "B", laenge=1.2, herkunft="liste", norm="07-20-03",
      quelle=_PC, hinweis="z. B. Reedkontakt, Zylinderschalter")
_reg(name="naeherungssensor", titel="Näherungssensor", kategorie="Näherungsschalter", klassen="B", herkunft="liste",
     prims=_verschiebe(_RAUTE, 1, 0), anschluesse={"an1": (-1, 0), "an2": (1, 0)}, rahmen=(-1.2, -1.2, 1.2, 1.2),
     norm="07-19-01", quelle=_PC, hinweis="allgemein; Rhombus mit zwei Linien")
_reg(name="beruehrungssensor", titel="Berührungssensor", kategorie="Näherungsschalter", klassen="B", herkunft="liste",
     prims=(*_verschiebe(_RAUTE, 1, 0), ("l", [(-1, -0.8), (-1, 0.8)])), anschluesse={"an1": (-1, 0), "an2": (1, 0)},
     rahmen=(-1.2, -1.2, 1.2, 1.2), norm="07-19-04", quelle=_PC)
_reg(name="naeherungseinrichtung_block", titel="Näherungsempfindliche Einrichtung (Blocksymbol)",
     kategorie="Näherungsschalter", klassen="B", herkunft="liste",
     prims=(("r", -2, -2, 2, 2, "weiss"), *_verschiebe(_RAUTE, 1, -1.0)),
     anschluesse={"an1": (-2, 0), "an2": (2, 0)}, rahmen=(-2.2, -2.2, 2.2, 2.2), norm="07-19-02", quelle=_PC,
     hinweis="Quadrat mit Rhombus; Anschlüsse links und rechts")


# ───────────────────────────── Katalogbogen ─────────────────────────────

def katalog_svg(spalten: int = 4, groesse: float = 1.5) -> str:
    """Bogen mit allen Zeichen, ihren Namen, Klassen und Anschlusspunkten (zur Sichtprüfung)."""
    from .zeichnung import Zeichnung
    zellb, zellh = 200.0, 170.0
    kategorien: dict[str, list[Symbol]] = {}
    for s in SYMBOLE.values():
        kategorien.setdefault(s.kategorie, []).append(s)
    z = Zeichnung(spalten * zellb + 20, 100, "Schaltzeichen der Skill-Bibliothek",
                  "Katalog aller Schaltzeichen mit Namen, Klassen des Kennzeichens und Anschlusspunkten.",
                  "Eigene Zeichnungen nach der Formensprache von DIN EN 60617.")
    y = 30.0
    for kat, liste in kategorien.items():
        z.text(10, y, kat, 15, "start", True)
        y += 14
        for i, s in enumerate(liste):
            cx = 10 + (i % spalten) * zellb + zellb / 2
            cy = y + (i // spalten) * zellh + 70
            z.rechteck(cx - zellb / 2 + 3, cy - 66, cx + zellb / 2 - 3, cy + 94, "keine", "duenn")
            zeichne(z, s, cx, cy, groesse=groesse)
            for p in s.anschluesse.values():
                px, py = transformiere(p, 0, False, groesse, cx, cy)
                z.kreis(px, py, 2.2, "schwarz", "keine")
            z.text(cx, cy + 66, s.name, min(11, 188 / (len(s.name) * 0.62)), "middle", True)
            z.text(cx, cy + 79, s.titel, min(9.5, 188 / (len(s.titel) * 0.55)), "middle")
            z.text(cx, cy + 91, f"Klasse {s.klassen} · {dict(liste='Liste', zusammengesetzt='zusammengesetzt').get(s.herkunft, 'abgleichen!')}",
                   8.5, "middle", False, True)
        zeilen = (len(liste) + spalten - 1) // spalten
        y += zeilen * zellh + 18
    z.text(10, y, "Betätigungsarten (am Schließer dargestellt)", 15, "start", True)
    y += 14
    basis = SYMBOLE["schliesser"]
    for i, b in enumerate(BETAETIGUNGEN.values()):
        cx = 10 + (i % spalten) * zellb + zellb / 2 + 40
        cy = y + (i // spalten) * zellh + 70
        z.rechteck(cx - zellb / 2 - 37, cy - 66, cx + zellb / 2 - 43, cy + 94, "keine", "duenn")
        zeichne(z, basis, cx, cy, groesse=groesse, betaetigung=b.name)
        z.text(cx - 40, cy + 66, b.name, 11, "middle", True)
        z.text(cx - 40, cy + 79, b.titel, 8.5, "middle")
    y += ((len(BETAETIGUNGEN) + spalten - 1) // spalten) * zellh + 14
    z.hoehe = y + 10
    return z.svg()
