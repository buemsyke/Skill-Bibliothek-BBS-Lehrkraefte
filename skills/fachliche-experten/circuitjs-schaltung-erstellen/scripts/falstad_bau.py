#!/usr/bin/env python3
"""falstad_bau – Baukasten für circuit.js-Schaltungen im Falstad-Textformat.

Alle Koordinaten sind **Rasterpunkte** (1 Einheit = 16 px). Der Baukasten schreibt Pixelwerte,
sodass jeder Anschluss im Raster liegt. Plus-Anschluss einer Gleichspannungsquelle ist der
**zweite** Punkt; ein Voltmeter ist positiv, wenn der erste Punkt höheres Potential hat; ein
Amperemeter zeigt den Strom vom ersten zum zweiten Punkt positiv.

Beispiel (Reihenschaltung, Quelle links, Last rechts)::

    b = Bau("Ohmsches Gesetz")
    b.quelle_dc((6, 18), (6, 6), 10)         # unten Minus, oben Plus
    b.draht((6, 6), (10, 6))
    a = b.amperemeter((10, 6), (14, 6))
    b.draht((14, 6), (20, 6))
    b.widerstand((20, 6), (20, 18), 220, name="R")
    b.draht((20, 18), (6, 18))
    print(b)
"""

from __future__ import annotations

from dataclasses import dataclass, field

from falstad_kern import RASTER

# Kopfzeile: Flags 1 = Stromrichtung anzeigen (wie in den Versuchen); Zeitschritt wird gesetzt.
KOPF_VORLAGE = "$ {flags} {dt} 10.20027730826997 50 5 43 5e-11"


def zahl(v: float) -> str:
    """Zahl so schreiben, dass Falstad sie sicher liest (keine Tausendertrenner, kurze Form)."""
    if isinstance(v, int):
        return str(v)
    s = format(float(v), ".10g")
    return s


def px(p) -> tuple:
    return (int(p[0] * RASTER), int(p[1] * RASTER))


@dataclass
class Messstelle:
    """Ein eingebautes Messgerät und was es zeigen soll."""
    name: str          # z. B. "I1", "U2"
    art: str           # "A" | "V"
    element: int       # Platz in der Elementliste der Engine
    modus: int         # 0 Gleichwert/Momentanwert, 1 Effektivwert, 2 Spitzenwert
    zeile: int         # Zeilennummer im Text (1-basiert, Kopf = 1)


@dataclass
class Bau:
    titel: str = ""
    zeitschritt: float = 5e-6
    stromrichtung: bool = True
    zeilen: list = field(default_factory=list)
    index: int = 0
    messstellen: list = field(default_factory=list)
    oszis: list = field(default_factory=list)

    # ── Grundbausteine ──
    def _el(self, typ: str, a, b, flags: int = 0, *werte) -> int:
        xa, ya = px(a)
        xb, yb = px(b)
        teile = [typ, xa, ya, xb, yb, flags, *[zahl(w) if not isinstance(w, str) else w for w in werte]]
        self.zeilen.append(" ".join(str(t) for t in teile))
        self.index += 1
        return self.index - 1

    def draht(self, *punkte) -> None:
        """Leitung; mehrere Punkte ergeben einen rechtwinkligen Linienzug."""
        for a, b in zip(punkte, punkte[1:]):
            if a == b:
                continue
            if a[0] != b[0] and a[1] != b[1]:
                raise ValueError(f"Leitung {a}→{b} ist schräg")
            self._el("w", a, b, 0)

    def schiene(self, *punkte) -> None:
        """Leitung durch alle Punkte; jeder Punkt wird Endpunkt, damit Abzweige verbinden."""
        for a, b in zip(punkte, punkte[1:]):
            self.draht(a, b)

    def widerstand(self, a, b, ohm: float, name: str | None = None) -> int:
        i = self._el("r", a, b, 0, ohm)
        if name:
            self.beschrifte_element(a, b, name)
        return i

    def kondensator(self, a, b, farad: float, spannung0: float = 0.0, name: str | None = None) -> int:
        i = self._el("c", a, b, 0, farad, spannung0, 0.001)
        if name:
            self.beschrifte_element(a, b, name)
        return i

    def spule(self, a, b, henry: float, strom0: float = 0.0, name: str | None = None) -> int:
        i = self._el("l", a, b, 0, henry, strom0)
        if name:
            self.beschrifte_element(a, b, name)
        return i

    def quelle_dc(self, minus, plus, volt: float, name: str | None = None) -> int:
        i = self._el("v", minus, plus, 0, 0, 40, volt, 0, 0, 0.5)
        if name:
            self.beschrifte_element(minus, plus, name, abstand=3)
        return i

    def quelle_ac(self, a, b, u_eff: float, frequenz: float = 50.0, phase: float = 0.0,
                  name: str | None = None) -> int:
        """Wechselspannungsquelle mit **Effektivwert** u_eff; Phase im Bogenmaß (Sinus)."""
        import math
        i = self._el("v", a, b, 0, 1, frequenz, u_eff * math.sqrt(2), 0, phase, 0)
        if name:
            self.beschrifte_element(a, b, name, abstand=6)
        return i

    def quelle_rechteck(self, minus, plus, spitze: float, frequenz: float, tastgrad: float,
                        phase: float = 0.0) -> int:
        """Rechteck 0 … spitze (Ansteuerung von Schaltern). Mitte spitze/2 ± spitze/2, Tastgrad = High-Anteil."""
        return self._el("v", minus, plus, 0, 2, frequenz, spitze / 2, spitze / 2, phase, tastgrad)

    def schalter(self, a, b, geschlossen: bool = True, name: str | None = None) -> int:
        i = self._el("s", a, b, 0, 0 if geschlossen else 1, "false")
        if name:
            self.beschrifte_element(a, b, name)
        return i

    def diode(self, anode, kathode, name: str | None = None) -> int:
        i = self._el("d", anode, kathode, 2, "default")
        if name:
            self.beschrifte_element(anode, kathode, name)
        return i

    def zenerdiode(self, anode, kathode, u_z: float, name: str | None = None) -> int:
        i = self._el("z", anode, kathode, 1, 0.805904783, u_z)
        if name:
            self.beschrifte_element(anode, kathode, name)
        return i

    def mosfet(self, gate, drain, source, schwelle: float = 2.0, name: str | None = None, beta: float = 1.0) -> int:
        """n-Kanal-MOSFET, waagerecht: Gate links, Drain oben rechts, Source unten rechts.

        gate = (x, y); drain = (x + 4, y - 1); source = (x + 4, y + 1) in Rasterpunkten.
        """
        gx, gy = gate
        if tuple(drain) != (gx + 4, gy - 1) or tuple(source) != (gx + 4, gy + 1):
            raise ValueError("MOSFET-Anschlüsse: drain=(gx+4, gy-1), source=(gx+4, gy+1)")
        i = self._el("f", gate, (gx + 4, gy), 0, schwelle, beta)   # beta 1 A/V² ≈ 0,13 Ω bei Vgs 10 V
        if name:
            self.text((gx + 1, gy - 3), name)
        return i

    def transformator(self, p1, p2, l_prim: float, uebersetzung: float, kopplung: float = 0.999) -> int:
        """Transformator: p1 = oberer Anschluss Primärseite, p2 = oberer Anschluss Sekundärseite (gleiche Höhe).

        Anschlüsse: (x1,y), (x1,y+2) primär; (x2,y), (x2,y+2) sekundär (Rasterpunkte).
        uebersetzung = Windungszahl sekundär / primär (Falstad „ratio“).
        """
        if p1[1] != p2[1]:
            raise ValueError("Transformator: beide Punkte auf gleicher Höhe")
        return self._el("T", p1, p2, 0, l_prim, uebersetzung, 0, 0, kopplung)

    def masse(self, p) -> int:
        """Bezugspotential (Masse); Schaltungen mit Halbleiterschaltern brauchen es für die Konvergenz."""
        return self._el("g", p, (p[0], p[1] + 1), 0)

    # ── Messgeräte ──
    def voltmeter(self, plus, minus, name: str, effektiv: bool = False, modus: int | None = None) -> int:
        """Voltmeter (Kreis mit V) parallel zum Bauteil; zeigt U(plus) − U(minus)."""
        m = (1 if effektiv else 0) if modus is None else modus
        i = self._el("p", plus, minus, 3, m)
        self.messstellen.append(Messstelle(name, "V", i, m, len(self.zeilen) + 1))
        self.beschrifte_element(plus, minus, name, abstand=2)
        return i

    def amperemeter(self, a, b, name: str, effektiv: bool = False) -> int:
        """Amperemeter (Kreis mit A) in Reihe; positiv, wenn der Strom von a nach b fließt."""
        m = 1 if effektiv else 0
        i = self._el("370", a, b, 3, m)
        self.messstellen.append(Messstelle(name, "A", i, m, len(self.zeilen) + 1))
        self.beschrifte_element(a, b, name, abstand=2)
        return i

    # ── Beschriftung, Oszilloskop ──
    def text(self, p, inhalt: str, groesse: int = 12) -> int:
        x, y = px(p)
        roh = inhalt.replace(" ", "\\s")
        breite = max(8, int(len(inhalt) * groesse * 0.55))
        return self._el_roh("x", x, y, x + breite, y + 3, 4, groesse, roh)

    def _el_roh(self, typ, x1, y1, x2, y2, flags, *werte) -> int:
        self.zeilen.append(" ".join(str(t) for t in [typ, x1, y1, x2, y2, flags, *werte]))
        self.index += 1
        return self.index - 1

    def beschrifte_element(self, a, b, name: str, abstand: int = 2) -> None:
        """Bezeichner neben ein Bauteil: links neben senkrechte, über waagerechte Bauteile."""
        (xa, ya), (xb, yb) = a, b
        if xa == xb:
            self.text((xa - abstand - max(0, len(name) - 2) * 0.5, (ya + yb) / 2), name)
        else:
            self.text(((xa + xb) / 2 - len(name) * 0.25, ya - abstand - 0.5), name)

    def oszi(self, element: int, tempo: int = 64, skala: float = 5.0, zeitmass: float = 0.05) -> None:
        """Oszilloskop-Kanal für ein Element (Spannung und Strom); wird unter dem Schaltbild angezeigt."""
        self.oszis.append(f"o {element} {tempo} 0 3 {zahl(skala)} {zahl(zeitmass)} {len(self.oszis)}")

    # ── Ausgabe ──
    def kopf(self) -> str:
        return KOPF_VORLAGE.format(flags=1 if self.stromrichtung else 0, dt=zahl(self.zeitschritt))

    def text_ausgabe(self) -> str:
        return "\n".join([self.kopf(), *self.zeilen, *self.oszis]) + "\n"

    def __str__(self) -> str:
        return self.text_ausgabe()
