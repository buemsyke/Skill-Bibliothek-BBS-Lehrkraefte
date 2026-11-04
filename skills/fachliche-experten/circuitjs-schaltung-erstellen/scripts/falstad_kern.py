#!/usr/bin/env python3
"""falstad_kern – Lesen, Prüfen und Nachrechnen von circuit.js-Schaltungen (Falstad-Textformat).

Nur Python-Standardbibliothek. Ein Aufruf besteht aus drei Teilen:

* ``lese(text)``       zerlegt den Schaltungstext in Elemente mit Anschlusspunkten (Posten).
* ``pruefe(text)``     statische Prüfung: Raster, offene Anschlüsse, Berührung ohne Verbindung,
                       Überlappungen, Messgeräte (Amperemeter in Reihe, Voltmeter parallel).
* ``rechne(elemente)`` Nachrechnung linearer Schaltungen (Gleich- und Wechselstrom, ein
                       Frequenzpunkt) mit der Knotenpotentialmethode; Dioden und Transistoren
                       rechnet nur die Engine (siehe ``engine_pruefen.py``).

Positive Zählrichtung wie in Falstad: Strom und Spannung eines Zweipols zeigen von Anschluss 1
(erster Punkt der Zeile) zu Anschluss 2; ein Voltmeter zeigt U(Anschluss 1) - U(Anschluss 2),
ein Amperemeter den Strom von Anschluss 1 nach Anschluss 2.
"""

from __future__ import annotations

import cmath
import math
import re
from dataclasses import dataclass, field

RASTER = 16
KOPF_STANDARD = "$ 1 0.000005 10.20027730826997 50 5 43 5e-11"  # wie in den Versuchen des Projekts

# Elementtypen, deren Anschlusspunkte und Rechenmodell bekannt sind.
ZWEIPOLE = {"w", "r", "c", "l", "v", "s", "d", "z", "i", "p", "370", "181"}
MESSGERAETE = {"p": "Voltmeter", "370": "Amperemeter"}
NICHTLINEAR = {"d", "z", "f", "181"}
NICHT_DIN = {"R": "Rail (Spannungsanschluss) ist kein DIN-Schaltzeichen – Spannungsquelle v mit Leitungen verwenden"}
BEKANNT_OHNE_POSTEN = {"$", "o", "x", "h", "%", "38", "A", "B"}  # Kopf, Oszi, Text, Beschriftung …

# Mindestlänge in Pixeln, damit Schaltzeichen und Werte nicht überlappen.
MIN_LAENGE = {"r": 48, "c": 48, "l": 48, "v": 48, "s": 48, "d": 48, "z": 48, "i": 48, "p": 64, "370": 64}

EPS = 1e-9


# ───────────────────────────── Lesen ─────────────────────────────

@dataclass
class Element:
    nr: int                  # Zeilennummer im Text (1-basiert)
    typ: str
    x1: int = 0
    y1: int = 0
    x2: int = 0
    y2: int = 0
    flags: int = 0
    werte: list = field(default_factory=list)
    roh: str = ""
    index: int = -1          # Platz in der Elementliste der Engine (ohne Kopf, Oszi, Text)

    @property
    def posten(self) -> list:
        t = self.typ
        if t == "g":
            return [(self.x1, self.y1)]
        if t == "T":     # Transformator: Primär links, Sekundär rechts, Anschlüsse 32 px auseinander
            return [(self.x1, self.y1), (self.x1, self.y1 + 32), (self.x2, self.y1), (self.x2, self.y1 + 32)]
        if t == "f":     # MOSFET (n-Kanal, waagerecht): Gate, Drain oben, Source unten
            return [(self.x1, self.y1), (self.x2, self.y1 - 16), (self.x2, self.y1 + 16)]
        return [(self.x1, self.y1), (self.x2, self.y2)]

    @property
    def bekannt(self) -> bool:
        return self.typ in ZWEIPOLE or self.typ in ("g", "T", "f")

    def zahl(self, k: int, standard: float = 0.0) -> float:
        try:
            return float(self.werte[k])
        except (IndexError, ValueError):
            return standard


@dataclass
class Schaltung:
    kopf: str
    elemente: list
    sonstige: list           # Oszi-, Text-, Hinweiszeilen: (Zeilennummer, Zeile)


def lese(text: str) -> Schaltung:
    kopf, elemente, sonstige = "", [], []
    index = 0
    for nr, zeile in enumerate(text.splitlines(), 1):
        z = zeile.strip()
        if not z:
            continue
        teile = z.split()
        typ = teile[0]
        if typ == "$":
            kopf = z
            continue
        if typ in BEKANNT_OHNE_POSTEN:
            sonstige.append((nr, z))
            if typ in ("x", "38"):   # Text und Schieberegler stehen in der Elementliste der Engine
                index += 1
            continue
        if len(teile) < 6:
            sonstige.append((nr, z))
            continue
        try:
            x1, y1, x2, y2, flags = (int(float(t)) for t in teile[1:6])
        except ValueError:
            sonstige.append((nr, z))
            continue
        el = Element(nr, typ, x1, y1, x2, y2, flags, teile[6:], z, index)
        index += 1
        elemente.append(el)
    return Schaltung(kopf, elemente, sonstige)


# ───────────────────────────── Prüfen ─────────────────────────────

@dataclass
class Befund:
    stufe: str    # "fehler" | "warnung" | "hinweis"
    code: str
    text: str

    def __str__(self) -> str:
        zeichen = {"fehler": "❌", "warnung": "⚠️", "hinweis": "ℹ️"}[self.stufe]
        return f"{zeichen} [{self.code}] {self.text}"


@dataclass
class Bericht:
    befunde: list = field(default_factory=list)
    schaltung: Schaltung | None = None
    messung: "Messung | None" = None

    def melde(self, stufe: str, code: str, text: str) -> None:
        self.befunde.append(Befund(stufe, code, text))

    @property
    def fehler(self) -> list:
        return [b for b in self.befunde if b.stufe == "fehler"]

    @property
    def warnungen(self) -> list:
        return [b for b in self.befunde if b.stufe == "warnung"]

    @property
    def ok(self) -> bool:
        return not self.fehler


class Knoten:
    """Union-Find über Rasterpunkte."""

    def __init__(self) -> None:
        self.eltern: dict = {}

    def finde(self, p):
        self.eltern.setdefault(p, p)
        while self.eltern[p] != p:
            self.eltern[p] = self.eltern[self.eltern[p]]
            p = self.eltern[p]
        return p

    def vereine(self, a, b) -> None:
        ra, rb = self.finde(a), self.finde(b)
        if ra != rb:
            self.eltern[ra] = rb


def _auf_strecke_innen(p, e: Element) -> bool:
    """Liegt der Punkt p im Inneren der (waagerechten oder senkrechten) Strecke von e?"""
    (xa, ya), (xb, yb) = (e.x1, e.y1), (e.x2, e.y2)
    px, py = p
    if ya == yb == py:
        return min(xa, xb) < px < max(xa, xb)
    if xa == xb == px:
        return min(ya, yb) < py < max(ya, yb)
    return False


def _ueberlappung(a: Element, b: Element) -> bool:
    """Zwei kollineare Strecken teilen mehr als einen Punkt."""
    if a.y1 == a.y2 == b.y1 == b.y2:
        lo, hi = max(min(a.x1, a.x2), min(b.x1, b.x2)), min(max(a.x1, a.x2), max(b.x1, b.x2))
        return hi - lo > 0
    if a.x1 == a.x2 == b.x1 == b.x2:
        lo, hi = max(min(a.y1, a.y2), min(b.y1, b.y2)), min(max(a.y1, a.y2), max(b.y1, b.y2))
        return hi - lo > 0
    return False


def pruefe(text: str, *, messgeraete: bool = True, rechnen: bool = True) -> Bericht:
    """Statische Prüfung; bei linearen Schaltungen zusätzlich Nachrechnung und Messgeräte-Plausibilität."""
    sch = lese(text)
    b = Bericht(schaltung=sch)
    els = sch.elemente

    if not sch.kopf:
        b.melde("fehler", "KOPF", "Kopfzeile '$ …' fehlt (z. B. " + KOPF_STANDARD + ")")
    if not els:
        b.melde("fehler", "LEER", "Keine Bauelemente gefunden")
        return b

    for e in els:
        if e.typ in NICHT_DIN:
            b.melde("warnung", "DIN", f"Zeile {e.nr}: {NICHT_DIN[e.typ]}")
        if not e.bekannt:
            b.melde("warnung", "TYP", f"Zeile {e.nr}: Typ '{e.typ}' nicht im Katalog – Anschlusspunkte ungeprüft")
            continue
        for p in e.posten:
            if p[0] % RASTER or p[1] % RASTER:
                b.melde("fehler", "RASTER", f"Zeile {e.nr}: Anschluss {p} liegt nicht im 16-px-Raster")
                break
        if e.typ in ZWEIPOLE and (e.x1, e.y1) == (e.x2, e.y2):
            b.melde("fehler", "LAENGE0", f"Zeile {e.nr}: Element '{e.typ}' hat die Länge 0")
        if e.typ in ZWEIPOLE and e.x1 != e.x2 and e.y1 != e.y2:
            b.melde("warnung", "SCHRAEG", f"Zeile {e.nr}: schräges Element '{e.typ}' – DIN-Schaltpläne sind rechtwinklig")
        mind = MIN_LAENGE.get(e.typ)
        if mind and 0 < abs(e.x2 - e.x1) + abs(e.y2 - e.y1) < mind:
            b.melde("warnung", "KURZ", f"Zeile {e.nr}: '{e.typ}' kürzer als {mind} px – Beschriftung kann überlappen")

    # Verbindungen: nur gemeinsame Anschlusspunkte verbinden (Falstad kennt keine T-Verbindung)
    kn = Knoten()
    zaehler: dict = {}
    for e in els:
        if not e.bekannt:
            continue
        ps = e.posten
        for p in ps:
            zaehler.setdefault(p, []).append(e)
            kn.finde(p)
        if e.typ == "w":
            kn.vereine(ps[0], ps[1])
    for p, liste in zaehler.items():
        gruppe = {id(x) for x in liste}
        if len(gruppe) == 1:
            e = liste[0]
            b.melde("fehler", "OFFEN", f"Zeile {e.nr}: Anschluss {p} ({e.typ}) ist mit nichts verbunden")

    strecken = [e for e in els if e.typ in ZWEIPOLE and (e.x1 == e.x2 or e.y1 == e.y2)]
    for e in els:
        if not e.bekannt:
            continue
        for p in e.posten:
            for s in strecken:
                if s is not e and _auf_strecke_innen(p, s):
                    b.melde("fehler", "BERUEHRUNG",
                            f"Zeile {e.nr}: Anschluss {p} liegt mitten auf Zeile {s.nr} ({s.typ}) – "
                            "keine elektrische Verbindung; Leitung an dieser Stelle teilen")
    for i, a in enumerate(strecken):
        for c in strecken[i + 1:]:
            if _ueberlappung(a, c):
                b.melde("fehler", "UEBERLAPPT", f"Zeilen {a.nr} und {c.nr} überlappen sich")

    # Messgeräte
    ammeter = [e for e in els if e.typ == "370"]
    voltmeter = [e for e in els if e.typ == "p"]
    if messgeraete:
        if not ammeter:
            b.melde("fehler", "MESS_A", "Kein Amperemeter (370) vorhanden")
        if not voltmeter:
            b.melde("fehler", "MESS_V", "Kein Voltmeter (p) vorhanden")
    for e in ammeter + voltmeter:
        name = MESSGERAETE[e.typ]
        if kn.finde((e.x1, e.y1)) == kn.finde((e.x2, e.y2)):
            wie = ("kurzgeschlossen – die Leitung überbrückt es" if e.typ == "370"
                   else "an beiden Anschlüssen am selben Knoten – zeigt immer 0")
            b.melde("fehler", "MESS_KNOTEN", f"Zeile {e.nr}: {name} {wie}")
        if e.flags & 3 != 3:
            b.melde("warnung", "MESS_DIN",
                    f"Zeile {e.nr}: {name} ohne Kreissymbol – Flags 3 setzen (Kreis mit V bzw. A nach DIN)")

    if rechnen and not b.fehler:
        _rechnen_und_pruefen(sch, kn, b)
    return b


def _rechnen_und_pruefen(sch: Schaltung, kn: Knoten, b: Bericht) -> None:
    nichtlin = [e for e in sch.elemente if e.typ in NICHTLINEAR]
    if nichtlin or any(e.typ == "f" for e in sch.elemente):
        b.melde("hinweis", "NICHTLINEAR",
                "Dioden/Transistoren: keine Nachrechnung in Python – Werte mit engine_pruefen.py aus der Engine lesen")
        return
    try:
        m = rechne(sch)
    except RechenFehler as fe:
        b.melde("fehler", "RECHNUNG", str(fe))
        return
    b.messung = m
    for e in sch.elemente:
        if e.typ == "370":
            i = m.anzeige(e)
            if i is not None and abs(i) > 1e3:
                b.melde("fehler", "MESS_KURZ", f"Zeile {e.nr}: Amperemeter führt {i:.3g} A – liegt es parallel statt in Reihe?")
            elif i is not None and i < -1e-9 and not m.hat_wechsel:
                b.melde("warnung", "POLUNG", f"Zeile {e.nr}: Amperemeter zeigt {i:.4g} A (negativ) – Anschlüsse tauschen")
        if e.typ == "p":
            u = m.anzeige(e)
            if u is not None and u < -1e-6 and not m.hat_wechsel:
                b.melde("warnung", "POLUNG", f"Zeile {e.nr}: Voltmeter zeigt {u:.4g} V (negativ) – Anschlüsse tauschen")
    if not any(e.typ == "v" or e.typ == "i" for e in sch.elemente):
        b.melde("warnung", "QUELLE", "Keine Spannungs- oder Stromquelle gefunden")


# ───────────────────────────── Rechnen ─────────────────────────────

class RechenFehler(Exception):
    pass


@dataclass
class Messung:
    """Ergebnis je Element: Gleichanteil (u_dc, i_dc) und Wechselanteil als komplexe Effektivwerte."""
    sch: Schaltung
    u_dc: dict = field(default_factory=dict)
    i_dc: dict = field(default_factory=dict)
    u_ac: dict = field(default_factory=dict)
    i_ac: dict = field(default_factory=dict)
    frequenz: float = 0.0

    @property
    def hat_wechsel(self) -> bool:
        return self.frequenz > 0

    def u(self, e: Element) -> float:
        """Spannungsanzeige: Gleichwert bzw. Effektivwert (Gleich- und Wechselanteil geometrisch)."""
        return self._wert(self.u_dc.get(e.nr, 0.0), self.u_ac.get(e.nr, 0j))

    def i(self, e: Element) -> float:
        return self._wert(self.i_dc.get(e.nr, 0.0), self.i_ac.get(e.nr, 0j))

    def _wert(self, dc: float, ac: complex) -> float:
        if not self.hat_wechsel:
            return dc
        return math.sqrt(dc * dc + abs(ac) ** 2)

    def anzeige(self, e: Element):
        """Angezeigter Wert eines Messgeräts (Effektivwert bei Messart 1, sonst Gleichwert)."""
        if e.typ == "p":
            return self.u(e) if (self.hat_wechsel or e.zahl(0) == 1) else self.u_dc.get(e.nr, 0.0)
        if e.typ == "370":
            return self.i(e) if (self.hat_wechsel or e.zahl(0) == 1) else self.i_dc.get(e.nr, 0.0)
        return None

    def phase_u_i(self, e: Element) -> float:
        """Phasenwinkel von U gegenüber I in Grad (Zählpfeil gleich gerichtet), nur Wechselstrom."""
        u, i = self.u_ac.get(e.nr, 0j), self.i_ac.get(e.nr, 0j)
        if abs(u) < EPS or abs(i) < EPS:
            return 0.0
        return math.degrees(cmath.phase(u / i))


def _loese(a: list, rhs: list) -> list:
    """Gauß mit Spaltenpivotsuche (reell oder komplex)."""
    n = len(a)
    m = [zeile[:] + [rhs[k]] for k, zeile in enumerate(a)]
    for s in range(n):
        piv = max(range(s, n), key=lambda r: abs(m[r][s]))
        if abs(m[piv][s]) < 1e-18:
            raise RechenFehler("Singuläre Matrix – Kurzschluss, Quellenschleife oder Teilnetz ohne Bezugspunkt")
        m[s], m[piv] = m[piv], m[s]
        for r in range(s + 1, n):
            f = m[r][s] / m[s][s]
            if f:
                for c in range(s, n + 1):
                    m[r][c] -= f * m[s][c]
    x = [0j] * n
    for r in range(n - 1, -1, -1):
        x[r] = (m[r][n] - sum(m[r][c] * x[c] for c in range(r + 1, n))) / m[r][r]
    return x


def _quellwert(e: Element, wechsel: bool, omega: float):
    """Effektivzeiger der Quelle (Sinus, Phase im Bogenmaß) oder Gleichwert."""
    wellenform = int(e.zahl(0))
    freq = e.zahl(1, 40.0)
    amp = e.zahl(2)
    bias = e.zahl(3)
    phase = e.zahl(4)
    if wechsel:
        if wellenform != 1:
            return 0j, freq
        return cmath.rect(amp / math.sqrt(2), phase), freq
    if wellenform == 0:
        return amp + bias, freq
    return bias, freq


def rechne(sch: Schaltung) -> Messung:
    """Gleichstrom- und Wechselstromanalyse (Überlagerung); nur lineare Elemente."""
    freqs = {e.zahl(1, 40.0) for e in sch.elemente if e.typ == "v" and int(e.zahl(0)) == 1}
    if len(freqs) > 1:
        raise RechenFehler("Mehrere Frequenzen – Python-Nachrechnung kennt nur eine; Engine verwenden")
    m = Messung(sch)
    m.frequenz = freqs.pop() if freqs else 0.0
    _analyse(sch, m, wechsel=False)
    if m.frequenz > 0:
        _analyse(sch, m, wechsel=True)
    return m


def _analyse(sch: Schaltung, m: Messung, wechsel: bool) -> None:
    omega = 2 * math.pi * m.frequenz if wechsel else 0.0
    kn = Knoten()
    for e in sch.elemente:
        if e.typ not in ZWEIPOLE and e.typ not in ("g", "T"):
            raise RechenFehler(f"Zeile {e.nr}: Typ '{e.typ}' wird nicht nachgerechnet")
        if e.typ in NICHTLINEAR:
            raise RechenFehler(f"Zeile {e.nr}: nichtlineares Element '{e.typ}'")
        for p in e.posten:
            kn.finde(p)
        if e.typ == "w":
            kn.vereine(*e.posten)
    bezug = None
    for e in sch.elemente:
        if e.typ == "g":
            bezug = kn.finde(e.posten[0])
            break
    knoten = sorted({kn.finde(p) for e in sch.elemente for p in e.posten})
    if bezug is None:
        bezug = knoten[0]
    knoten = [k for k in knoten if k != bezug]
    idx = {k: n for n, k in enumerate(knoten)}
    nk = len(knoten)

    zweige = []        # Elemente mit eigenem Zweigstrom: Quellen, Kurzschlüsse, Transformator
    for e in sch.elemente:
        if e.typ in ("v", "370"):
            zweige.append(e)
        elif e.typ == "s" and int(e.zahl(0)) == 0:
            zweige.append(e)
        elif e.typ == "l" and not wechsel:
            zweige.append(e)
        elif e.typ == "T":
            zweige.append(e)
    # Spaltenzahl: Knoten + Zweigströme (Transformator hat zwei)
    nz = sum(2 if e.typ == "T" else 1 for e in zweige)
    n = nk + nz
    A = [[0j] * n for _ in range(n)]
    z = [0j] * n

    def node(p):
        k = kn.finde(p)
        return None if k == bezug else idx[k]

    def leitwert(p, q, y):
        a, c = node(p), node(q)
        if a is not None:
            A[a][a] += y
        if c is not None:
            A[c][c] += y
        if a is not None and c is not None:
            A[a][c] -= y
            A[c][a] -= y

    for k in range(nk):            # kleiner Leitwert gegen Bezug: schwebende Teilnetze bleiben lösbar
        A[k][k] += 1e-11

    spalte = {}
    nxt = nk
    for e in zweige:
        spalte[e.nr] = nxt
        nxt += 2 if e.typ == "T" else 1

    for e in sch.elemente:
        p = e.posten
        if e.typ == "r":
            r = e.zahl(0)
            if r <= 0:
                raise RechenFehler(f"Zeile {e.nr}: Widerstand {r} Ω nicht positiv")
            leitwert(p[0], p[1], 1 / r)
        elif e.typ == "c":
            y = 1j * omega * e.zahl(0)
            leitwert(p[0], p[1], y if wechsel else 0)
        elif e.typ == "l" and wechsel:
            L = e.zahl(0)
            leitwert(p[0], p[1], 1 / (1j * omega * L))
        elif e.typ == "s" and int(e.zahl(0)) != 0:
            pass
        elif e.typ == "i":
            wert = 0.0 if wechsel else e.zahl(0)
            a, c = node(p[0]), node(p[1])
            if a is not None:
                z[a] -= wert
            if c is not None:
                z[c] += wert
        elif e.typ == "p":
            pass

    for e in zweige:
        s = spalte[e.nr]
        p = e.posten
        a, c = node(p[0]), node(p[1])
        if e.typ == "T":
            # Spulen: Anschlüsse 0-1 primär, 2-3 sekundär; Strom von 0 nach 1 bzw. 2 nach 3
            l1, ratio, kopp = e.zahl(0), e.zahl(1, 1.0), e.zahl(4, 0.999)
            l2 = l1 * ratio * ratio
            mm = kopp * l1 * ratio
            for sp, (pa, pb) in ((s, (p[0], p[1])), (s + 1, (p[2], p[3]))):
                ka, kb = node(pa), node(pb)
                if ka is not None:
                    A[ka][sp] += 1
                if kb is not None:
                    A[kb][sp] -= 1
            for sp, (pa, pb), lself, lmut, anderer in ((s, (p[0], p[1]), l1, mm, s + 1), (s + 1, (p[2], p[3]), l2, mm, s)):
                ka, kb = node(pa), node(pb)
                if ka is not None:
                    A[sp][ka] += 1
                if kb is not None:
                    A[sp][kb] -= 1
                A[sp][sp] -= 1e-6
                if wechsel:
                    A[sp][sp] -= 1j * omega * lself
                    A[sp][anderer] -= 1j * omega * lmut
            continue
        if a is not None:
            A[a][s] += 1
        if c is not None:
            A[c][s] -= 1
        # Spannung U(p0) - U(p1) = E  (Quelle: U(p1) - U(p0) = Wert)
        if a is not None:
            A[s][a] += 1
        if c is not None:
            A[s][c] -= 1
        if e.typ == "v":
            wert, _ = _quellwert(e, wechsel, omega)
            z[s] = -wert
        else:
            z[s] = 0
            A[s][s] -= 1e-6      # Kurzschlusszweig mit 1 µΩ: Schleifen aus Nullspannungszweigen bleiben lösbar

    x = _loese(A, z)
    for e in sch.elemente:
        p = e.posten
        if e.typ in ("g", "w") or not e.posten:
            continue

        def spg(a_, b_):
            ua = x[node(a_)] if node(a_) is not None else 0j
            ub = x[node(b_)] if node(b_) is not None else 0j
            return ua - ub

        if e.typ == "T":
            s = spalte[e.nr]
            u, i = spg(p[0], p[1]), x[s]
            _eintragen(m, e, u, i, wechsel)
            continue
        u = spg(p[0], p[1])
        if e.typ == "r":
            i = u / e.zahl(0)
        elif e.typ == "c":
            i = u * 1j * omega * e.zahl(0) if wechsel else 0j
        elif e.typ == "l" and wechsel:
            i = u / (1j * omega * e.zahl(0))
        elif e.typ == "i":
            i = 0.0 if wechsel else e.zahl(0)
        elif e.typ == "p":
            i = 0j
        elif e.nr in spalte:
            i = x[spalte[e.nr]]
        else:
            i = 0j
        if e.typ == "v":
            u = -u   # Falstad zeigt bei Quellen U(Anschluss 2) - U(Anschluss 1)
        _eintragen(m, e, u, i, wechsel)


def _eintragen(m: Messung, e: Element, u: complex, i: complex, wechsel: bool) -> None:
    if wechsel:
        m.u_ac[e.nr], m.i_ac[e.nr] = u, i
    else:
        m.u_dc[e.nr], m.i_dc[e.nr] = u.real, i.real


# ───────────────────────────── Ausgabe ─────────────────────────────

def tabelle(m: Messung) -> str:
    """Lesbare Tabelle der berechneten Werte je Bauteil und Messgerät."""
    zeilen = ["Zeile  Typ  Wert                 U in V      I in A       Anzeige"]
    for e in m.sch.elemente:
        if e.typ in ("w", "g"):
            continue
        anz = m.anzeige(e)
        wert = e.werte[0] if e.werte and e.typ in ("r", "c", "l") else ""
        zeilen.append(f"{e.nr:5}  {e.typ:4} {wert:18} {m.u(e):10.4g}  {m.i(e):11.4g}  "
                      + (f"{anz:.4g}" if anz is not None else ""))
    return "\n".join(zeilen)


def bericht_text(b: Bericht) -> str:
    teile = [str(x) for x in b.befunde] or ["✅ keine Befunde"]
    if b.messung:
        teile += ["", tabelle(b.messung)]
    return "\n".join(teile)
