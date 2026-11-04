#!/usr/bin/env python3
"""falstad_vorlagen – geprüfte Vorlagen für Versuchsschaltungen in circuit.js (Falstad).

Jede Vorlage liefert eine ``Vorlage``: Schaltungstext, eingebaute Messgeräte und die **gerechneten
Erwartungswerte** (aus Formeln, nicht aus der Simulation). Die Tests vergleichen Formel, Python-
Nachrechnung und – falls Chromium und Falstad vorhanden sind – die Engine.

Aufruf über ``schaltung.py vorlage NAME [--param wert …]``.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

from falstad_bau import Bau


@dataclass
class Erwartung:
    name: str            # Name des Messgeräts (I1, U2 …)
    wert: float
    einheit: str
    toleranz: float = 0.02   # relativ (Formel gegen Nachrechnung/Engine)
    quelle: str = "Rechnung"  # Rechnung (Formel) | Naeherung (Modell vereinfacht)


@dataclass
class Vorlage:
    name: str
    titel: str
    bereich: str                 # gleichstrom | wechselstrom | elektronik
    bau: Bau
    erwartung: list = field(default_factory=list)
    parameter: dict = field(default_factory=dict)
    hinweise: list = field(default_factory=list)
    dauer: float = 0.1           # Simulationszeit in s, bis Endwerte stehen (Engine-Prüfung)
    fenster: float = 0.04        # Mittelungsfenster in s
    formeln: list = field(default_factory=list)   # LaTeX-Zeilen für das Begleitblatt

    @property
    def text(self) -> str:
        return self.bau.text_ausgabe()


REGISTER: dict = {}


def vorlage(name: str, bereich: str, titel: str, beschreibung: str):
    """Registriert eine Vorlagenfunktion; die Parameter stehen in der Signatur."""
    def deko(fn):
        REGISTER[name] = {"fn": fn, "bereich": bereich, "titel": titel, "beschreibung": beschreibung}
        return fn
    return deko


def _para(**kw) -> dict:
    return kw


def _dt(f: float) -> float:
    """Zeitschritt in s: etwa 1000 Schritte je Periode, höchstens 20 µs."""
    return min(2e-5, 1 / (f * 1000))


# ═══════════════════════════ Gleichstrom ═══════════════════════════

@vorlage("ohmsches-gesetz", "gleichstrom", "Ohmsches Gesetz",
         "Spannungsquelle, Widerstand, Amperemeter in Reihe, Voltmeter parallel (Messen von U und I).")
def ohmsches_gesetz(u: float = 10.0, r: float = 220.0) -> Vorlage:
    b = Bau("Ohmsches Gesetz")
    b.quelle_dc((6, 16), (6, 6), u, "U")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I")
    b.schiene((14, 6), (20, 6), (28, 6), (28, 8))
    b.draht((20, 6), (20, 8))
    b.widerstand((20, 8), (20, 14), r, "R")
    b.draht((20, 14), (20, 16))
    b.voltmeter((28, 8), (28, 14), "U_R")
    b.draht((28, 14), (28, 16))
    b.schiene((6, 16), (20, 16), (28, 16))
    i = u / r
    return Vorlage("ohmsches-gesetz", "Ohmsches Gesetz", "gleichstrom", b,
                   [Erwartung("I", i, "A"), Erwartung("U_R", u, "V")],
                   _para(u=u, r=r),
                   formeln=[r"R = \frac{U}{I}", r"I = \frac{U}{R}"])


@vorlage("reihenschaltung", "gleichstrom", "Reihenschaltung von Widerständen",
         "Drei Widerstände in Reihe; Amperemeter in der Leitung, je ein Voltmeter an jedem Widerstand und an der Reihenschaltung.")
def reihenschaltung(u: float = 10.0, r1: float = 220.0, r2: float = 470.0, r3: float = 680.0) -> Vorlage:
    b = Bau("Reihenschaltung")
    b.quelle_dc((6, 28), (6, 6), u, "U")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I")
    b.draht((14, 6), (20, 6), (20, 8))
    b.widerstand((20, 8), (20, 14), r1, "R1")
    b.widerstand((20, 14), (20, 20), r2, "R2")
    b.widerstand((20, 20), (20, 26), r3, "R3")
    b.draht((20, 26), (20, 28))
    b.draht((20, 28), (6, 28))
    for k, (ya, yb) in enumerate(((8, 14), (14, 20), (20, 26)), 1):
        b.draht((20, ya), (28, ya))
        b.draht((28, ya), (28, ya + 1))
        b.voltmeter((28, ya + 1), (28, yb - 1), f"U{k}")
        b.draht((28, yb - 1), (28, yb))
    b.draht((20, 26), (28, 26))
    b.draht((28, 8), (36, 8))
    b.draht((28, 26), (36, 26))
    b.voltmeter((36, 8), (36, 26), "U")
    rg = r1 + r2 + r3
    i = u / rg
    return Vorlage("reihenschaltung", "Reihenschaltung von Widerständen", "gleichstrom", b,
                   [Erwartung("I", i, "A"), Erwartung("U1", i * r1, "V"), Erwartung("U2", i * r2, "V"),
                    Erwartung("U3", i * r3, "V"), Erwartung("U", u, "V")],
                   _para(u=u, r1=r1, r2=r2, r3=r3),
                   formeln=[r"R_{ges} = R_1 + R_2 + R_3", r"I = \frac{U}{R_{ges}}",
                            r"U = U_1 + U_2 + U_3", r"\frac{U_1}{U_2} = \frac{R_1}{R_2}"])


@vorlage("parallelschaltung", "gleichstrom", "Parallelschaltung von Widerständen",
         "Drei Widerstände parallel; Amperemeter im Gesamtstrom und in jedem Zweig, ein Voltmeter an der Quelle.")
def parallelschaltung(u: float = 10.0, r1: float = 220.0, r2: float = 470.0, r3: float = 680.0) -> Vorlage:
    b = Bau("Parallelschaltung")
    b.quelle_dc((6, 20), (6, 6), u, "U")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I")
    b.schiene((14, 6), (20, 6), (28, 6), (36, 6), (44, 6), (44, 8))
    for k, (x, r) in enumerate(((20, r1), (28, r2), (36, r3)), 1):
        b.draht((x, 6), (x, 8))
        b.amperemeter((x, 8), (x, 12), f"I{k}")
        b.widerstand((x, 12), (x, 18), r, f"R{k}")
        b.draht((x, 18), (x, 20))
    b.voltmeter((44, 8), (44, 18), "U")
    b.draht((44, 18), (44, 20))
    b.schiene((6, 20), (20, 20), (28, 20), (36, 20), (44, 20))
    g = 1 / r1 + 1 / r2 + 1 / r3
    return Vorlage("parallelschaltung", "Parallelschaltung von Widerständen", "gleichstrom", b,
                   [Erwartung("I", u * g, "A"), Erwartung("I1", u / r1, "A"), Erwartung("I2", u / r2, "A"),
                    Erwartung("I3", u / r3, "A"), Erwartung("U", u, "V")],
                   _para(u=u, r1=r1, r2=r2, r3=r3),
                   formeln=[r"\frac{1}{R_{ges}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}",
                            r"I = I_1 + I_2 + I_3", r"\frac{I_1}{I_2} = \frac{R_2}{R_1}"])


@vorlage("gemischte-schaltung", "gleichstrom", "Gemischte Schaltung (Gruppenschaltung)",
         "R1 in Reihe zu R2 parallel R3; Amperemeter im Gesamtstrom und in den Parallelzweigen, Voltmeter an R1 und an der Parallelgruppe.")
def gemischte_schaltung(u: float = 12.0, r1: float = 100.0, r2: float = 220.0, r3: float = 330.0) -> Vorlage:
    b = Bau("Gemischte Schaltung")
    b.quelle_dc((6, 18), (6, 6), u, "U")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I")
    b.draht((14, 6), (16, 6))
    b.widerstand((16, 6), (24, 6), r1, "R1")
    b.schiene((24, 6), (30, 6), (38, 6), (46, 6), (46, 8))
    b.draht((16, 6), (16, 3), (18, 3))
    b.voltmeter((18, 3), (22, 3), "U1")
    b.draht((22, 3), (24, 3), (24, 6))
    for k, (x, r) in enumerate(((30, r2), (38, r3)), 2):
        b.draht((x, 6), (x, 8))
        b.amperemeter((x, 8), (x, 12), f"I{k}")
        b.widerstand((x, 12), (x, 16), r, f"R{k}")
        b.draht((x, 16), (x, 18))
    b.voltmeter((46, 8), (46, 16), "U23")
    b.draht((46, 16), (46, 18))
    b.schiene((6, 18), (30, 18), (38, 18), (46, 18))
    r23 = r2 * r3 / (r2 + r3)
    i = u / (r1 + r23)
    u23 = i * r23
    return Vorlage("gemischte-schaltung", "Gemischte Schaltung", "gleichstrom", b,
                   [Erwartung("I", i, "A"), Erwartung("U1", i * r1, "V"), Erwartung("U23", u23, "V"),
                    Erwartung("I2", u23 / r2, "A"), Erwartung("I3", u23 / r3, "A")],
                   _para(u=u, r1=r1, r2=r2, r3=r3),
                   formeln=[r"R_{23} = \frac{R_2 \cdot R_3}{R_2 + R_3}", r"R_{ges} = R_1 + R_{23}",
                            r"I = \frac{U}{R_{ges}}", r"U_{23} = I \cdot R_{23}"])


@vorlage("spannungsteiler", "gleichstrom", "Spannungsteiler (unbelastet und belastet)",
         "R1 und R2 als Spannungsteiler; mit rl > 0 zusätzlich Lastwiderstand parallel zu R2 (belasteter Spannungsteiler).")
def spannungsteiler(u: float = 12.0, r1: float = 1000.0, r2: float = 1000.0, rl: float = 0.0) -> Vorlage:
    b = Bau("Spannungsteiler")
    b.quelle_dc((6, 24), (6, 6), u, "U")
    b.draht((6, 6), (8, 6))
    b.amperemeter((8, 6), (12, 6), "I")
    b.draht((12, 6), (14, 6))
    b.draht((14, 6), (20, 6))
    b.draht((14, 6), (14, 8))
    b.voltmeter((14, 8), (14, 12), "U1")
    b.draht((14, 12), (14, 14), (20, 14))
    b.draht((20, 6), (20, 7))
    b.widerstand((20, 7), (20, 13), r1, "R1")
    b.draht((20, 13), (20, 14))
    b.draht((20, 14), (20, 16))
    b.widerstand((20, 16), (20, 22), r2, "R2")
    b.draht((20, 22), (20, 24))
    b.draht((20, 14), (28, 14), (28, 16))
    b.voltmeter((28, 16), (28, 22), "U2")
    b.draht((28, 22), (28, 24))
    if rl > 0:
        b.draht((28, 14), (36, 14), (36, 16))
        b.amperemeter((36, 16), (36, 20), "IL")
        b.widerstand((36, 20), (36, 24), rl, "RL")
        b.schiene((6, 24), (20, 24), (28, 24), (36, 24))
    else:
        b.schiene((6, 24), (20, 24), (28, 24))
    r2l = r2 if rl <= 0 else r2 * rl / (r2 + rl)
    i = u / (r1 + r2l)
    u2 = i * r2l
    erw = [Erwartung("I", i, "A"), Erwartung("U1", i * r1, "V"), Erwartung("U2", u2, "V")]
    if rl > 0:
        erw.append(Erwartung("IL", u2 / rl, "A"))
    return Vorlage("spannungsteiler", "Spannungsteiler", "gleichstrom", b, erw,
                   _para(u=u, r1=r1, r2=r2, rl=rl),
                   formeln=[r"\frac{U_2}{U} = \frac{R_2}{R_1 + R_2}",
                            r"\frac{U_2}{U} = \frac{R_{2L}}{R_1 + R_{2L}} \quad \text{mit} \quad R_{2L} = \frac{R_2 \cdot R_L}{R_2 + R_L}"])


@vorlage("bruecke", "gleichstrom", "Brückenschaltung (Wheatstone)",
         "Zwei Spannungsteiler mit Voltmeter in der Brücke und Amperemeter im Gesamtstrom; Abgleich bei R1/R2 = R3/R4.")
def bruecke(u: float = 10.0, r1: float = 100.0, r2: float = 200.0, r3: float = 300.0, r4: float = 600.0) -> Vorlage:
    b = Bau("Brückenschaltung")
    b.quelle_dc((6, 22), (6, 6), u, "U")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I")
    b.schiene((14, 6), (20, 6), (36, 6))
    b.widerstand((20, 6), (20, 14), r1, "R1")
    b.widerstand((20, 14), (20, 22), r2, "R2")
    b.widerstand((36, 6), (36, 14), r3, "R3")
    b.widerstand((36, 14), (36, 22), r4, "R4")
    b.draht((20, 14), (24, 14))
    b.voltmeter((24, 14), (32, 14), "U_B")
    b.draht((32, 14), (36, 14))
    b.schiene((6, 22), (20, 22), (36, 22))
    m1 = u * r2 / (r1 + r2)
    m2 = u * r4 / (r3 + r4)
    i = u / (r1 + r2) + u / (r3 + r4)
    return Vorlage("bruecke", "Brückenschaltung", "gleichstrom", b,
                   [Erwartung("I", i, "A"), Erwartung("U_B", m1 - m2, "V")],
                   _para(u=u, r1=r1, r2=r2, r3=r3, r4=r4),
                   hinweise=["Abgleich: Brückenspannung null bei R1/R2 = R3/R4 (Standard 100/200/300/600 Ω ist abgeglichen)."],
                   formeln=[r"U_B = U\left(\frac{R_2}{R_1 + R_2} - \frac{R_4}{R_3 + R_4}\right)",
                            r"\text{Abgleich:}\ \frac{R_1}{R_2} = \frac{R_3}{R_4}"])


@vorlage("quelle-belastet", "gleichstrom", "Reale Spannungsquelle mit Innenwiderstand",
         "Quelle U0 mit Innenwiderstand Ri und Lastwiderstand Ra; Klemmenspannung, Strom, Spannungsabfall an Ri (Leistungsanpassung bei Ra = Ri).")
def quelle_belastet(u0: float = 12.0, ri: float = 2.0, ra: float = 10.0) -> Vorlage:
    b = Bau("Reale Spannungsquelle")
    b.quelle_dc((6, 16), (6, 6), u0, "U0")
    b.draht((6, 6), (8, 6))
    b.widerstand((8, 6), (16, 6), ri, "Ri")
    b.draht((16, 6), (18, 6))
    b.amperemeter((18, 6), (22, 6), "I")
    b.schiene((22, 6), (28, 6), (36, 6), (36, 8))
    b.draht((8, 6), (8, 3), (10, 3))
    b.voltmeter((10, 3), (14, 3), "Ui")
    b.draht((14, 3), (16, 3), (16, 6))
    b.draht((28, 6), (28, 8))
    b.widerstand((28, 8), (28, 14), ra, "Ra")
    b.draht((28, 14), (28, 16))
    b.voltmeter((36, 8), (36, 14), "Uk")
    b.draht((36, 14), (36, 16))
    b.schiene((6, 16), (28, 16), (36, 16))
    i = u0 / (ri + ra)
    return Vorlage("quelle-belastet", "Reale Spannungsquelle", "gleichstrom", b,
                   [Erwartung("I", i, "A"), Erwartung("Uk", i * ra, "V"), Erwartung("Ui", i * ri, "V")],
                   _para(u0=u0, ri=ri, ra=ra),
                   formeln=[r"I = \frac{U_0}{R_i + R_a}", r"U_K = U_0 - I \cdot R_i", r"P_a = I^2 \cdot R_a",
                            r"P_{a,max}\ \text{bei}\ R_a = R_i"])


@vorlage("rc-schaltvorgang", "gleichstrom", "Laden und Entladen eines Kondensators (RC-Glied)",
         "Quelle, Schalter S1 (Laden) über Vorwiderstand zum Kondensator, Schalter S2 mit Entladewiderstand; Strom und Kondensatorspannung messbar.")
def rc_schaltvorgang(u: float = 10.0, r: float = 1000.0, c: float = 100e-6, re: float = 1000.0) -> Vorlage:
    b = Bau("RC-Schaltvorgang", zeitschritt=1e-4)
    b.quelle_dc((6, 22), (6, 6), u, "U")
    b.draht((6, 6), (8, 6))
    b.schalter((8, 6), (12, 6), True, "S1")
    b.amperemeter((12, 6), (16, 6), "I")
    b.widerstand((16, 6), (24, 6), r, "R")
    b.schiene((24, 6), (30, 6), (38, 6), (46, 6), (46, 8))
    b.draht((30, 6), (30, 8))
    b.kondensator((30, 8), (30, 16), c, 0.0, "C")
    b.draht((30, 16), (30, 22))
    b.draht((38, 6), (38, 8))
    b.schalter((38, 8), (38, 12), False, "S2")
    b.widerstand((38, 12), (38, 18), re, "Re")
    b.draht((38, 18), (38, 22))
    b.voltmeter((46, 8), (46, 20), "Uc")
    b.draht((46, 20), (46, 22))
    b.schiene((6, 22), (30, 22), (38, 22), (46, 22))
    tau = r * c
    return Vorlage("rc-schaltvorgang", "Laden und Entladen eines Kondensators", "gleichstrom", b,
                   [Erwartung("Uc", u, "V", quelle="Endwert nach 10 τ"), Erwartung("I", 0.0, "A", 0.02, "Endwert nach 10 τ")],
                   _para(u=u, r=r, c=c, re=re),
                   hinweise=[f"τ = R·C = {tau:.3g} s; S1 geschlossen lädt den Kondensator, danach S1 öffnen und S2 schließen (Entladen)."],
                   dauer=10 * tau, fenster=tau * 0.1,
                   formeln=[r"\tau = R \cdot C", r"u_C(t) = U\left(1 - e^{-t/\tau}\right)",
                            r"i(t) = \frac{U}{R} e^{-t/\tau}"])


@vorlage("rl-schaltvorgang", "gleichstrom", "Einschalten einer Spule (RL-Glied)",
         "Quelle, Schalter, Amperemeter, Widerstand und Spule in Reihe; Spannungen an R und L zeigen den Einschaltvorgang.")
def rl_schaltvorgang(u: float = 12.0, r: float = 100.0, l: float = 1.0) -> Vorlage:
    b = Bau("RL-Schaltvorgang", zeitschritt=1e-5)
    b.quelle_dc((6, 20), (6, 6), u, "U")
    b.draht((6, 6), (8, 6))
    b.schalter((8, 6), (12, 6), True, "S")
    b.amperemeter((12, 6), (16, 6), "I")
    b.schiene((16, 6), (24, 6), (32, 6))
    b.widerstand((24, 6), (24, 12), r, "R")
    b.spule((24, 12), (24, 18), l, 0.0, "L")
    b.draht((24, 18), (24, 20))
    b.draht((24, 20), (6, 20))
    b.voltmeter((32, 6), (32, 12), "U_R")
    b.draht((24, 12), (32, 12))
    b.voltmeter((32, 12), (32, 18), "U_L")
    b.draht((24, 18), (32, 18))
    tau = l / r
    return Vorlage("rl-schaltvorgang", "Einschalten einer Spule", "gleichstrom", b,
                   [Erwartung("I", u / r, "A", quelle="Endwert nach 10 τ"), Erwartung("U_R", u, "V", quelle="Endwert nach 10 τ"),
                    Erwartung("U_L", 0.0, "V", 0.02, "Endwert nach 10 τ")],
                   _para(u=u, r=r, l=l),
                   hinweise=[f"τ = L/R = {tau:.3g} s. Ausschalten: Spulenspannung springt hoch – im Versuch Freilaufdiode oder Löschglied ergänzen."],
                   dauer=10 * tau, fenster=tau * 0.1,
                   formeln=[r"\tau = \frac{L}{R}", r"i(t) = \frac{U}{R}\left(1 - e^{-t/\tau}\right)",
                            r"u_L(t) = U\, e^{-t/\tau}"])


# ═══════════════════════════ Wechselstrom ═══════════════════════════

def _ac_reihe(name: str, titel: str, u_eff: float, f: float, r: float, l: float, c: float) -> Vorlage:
    """Reihenschaltung aus R, L, C (0 = Bauteil weglassen) an Wechselspannung."""
    teile = [("R", r, "r"), ("L", l, "l"), ("C", c, "c")]
    teile = [t for t in teile if t[1] > 0]
    if not teile:
        raise ValueError("mindestens ein Bauteil (r, l oder c) angeben")
    ys = [8 + 6 * k for k in range(len(teile) + 1)]     # Knoten der Kette
    unten = ys[-1] + 2
    b = Bau(titel, zeitschritt=_dt(f))
    # Reine Spule: Start im Spannungsmaximum (Kosinus), sonst bliebe ein Gleichanteil im Strom bestehen
    start = math.pi / 2 if (r <= 0 and l > 0 and c <= 0) else 0.0
    quelle = b.quelle_ac((6, unten), (6, 6), u_eff, f, start, name="u")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I", effektiv=True)
    b.draht((14, 6), (20, 6), (20, 8))
    w = 2 * math.pi * f
    zr = r
    zx = w * l - (1 / (w * c) if c > 0 else 0.0)
    z = complex(zr, zx)
    i = u_eff / abs(z)
    erw = [Erwartung("I", i, "A")]
    for k, (kn, wert, typ) in enumerate(teile):
        ya, yb = ys[k], ys[k + 1]
        if typ == "r":
            b.widerstand((20, ya), (20, yb), wert, kn)
            u_k = i * r
        elif typ == "l":
            b.spule((20, ya), (20, yb), wert, 0.0, kn)
            u_k = i * w * l
        else:
            b.kondensator((20, ya), (20, yb), wert, 0.0, kn)
            u_k = i / (w * c)
        b.draht((28, ya), (28, ya + 1))
        b.voltmeter((28, ya + 1), (28, yb - 1), f"U_{kn}", effektiv=True)
        b.draht((28, yb - 1), (28, yb))
        erw.append(Erwartung(f"U_{kn}", u_k, "V"))
    for y in ys:
        b.draht((20, y), (28, y))
    b.draht((20, ys[-1]), (20, unten))
    b.draht((20, unten), (6, unten))
    xs = 36
    b.draht((28, ys[0]), (xs, ys[0]))
    b.draht((28, ys[-1]), (xs, ys[-1]))
    b.voltmeter((xs, ys[0]), (xs, ys[-1]), "U", effektiv=True)
    erw.append(Erwartung("U", u_eff, "V"))
    b.oszi(quelle, tempo=64, skala=u_eff * math.sqrt(2) * 1.25, zeitmass=0.05)
    formeln = [r"Z = \sqrt{R^2 + (X_L - X_C)^2}", r"I = \frac{U}{Z}", r"X_L = \omega L,\quad X_C = \frac{1}{\omega C}",
               r"\tan\varphi = \frac{X_L - X_C}{R}"]
    phi = math.degrees(math.atan2(zx, zr))
    return Vorlage(name, titel, "wechselstrom", b, erw,
                   _para(u_eff=u_eff, f=f, r=r, l=l, c=c),
                   hinweise=[f"|Z| = {abs(z):.4g} Ω, φ = {phi:.4g}° (Spannung eilt dem Strom bei φ > 0 voraus). "
                             "Alle Messgeräte zeigen Effektwerte; Oszilloskop: u (grün) und i (gelb)."],
                   dauer=0.3 if (l > 0 and r > 0) else 0.08, fenster=0.06, formeln=formeln)


@vorlage("ac-r", "wechselstrom", "Wirkwiderstand im Wechselstromkreis",
         "Widerstand an Wechselspannung: Strom und Spannung in Phase, Effektivwerte.")
def ac_r(u_eff: float = 12.0, f: float = 50.0, r: float = 100.0) -> Vorlage:
    return _ac_reihe("ac-r", "Wirkwiderstand im Wechselstromkreis", u_eff, f, r, 0, 0)


@vorlage("ac-l", "wechselstrom", "Spule im Wechselstromkreis",
         "Ideale Spule an Wechselspannung: induktiver Blindwiderstand, Strom eilt nach.")
def ac_l(u_eff: float = 12.0, f: float = 50.0, l: float = 0.2) -> Vorlage:
    return _ac_reihe("ac-l", "Spule im Wechselstromkreis", u_eff, f, 0, l, 0)


@vorlage("ac-c", "wechselstrom", "Kondensator im Wechselstromkreis",
         "Kondensator an Wechselspannung: kapazitiver Blindwiderstand, Strom eilt vor.")
def ac_c(u_eff: float = 12.0, f: float = 50.0, c: float = 47e-6) -> Vorlage:
    return _ac_reihe("ac-c", "Kondensator im Wechselstromkreis", u_eff, f, 0, 0, c)


@vorlage("ac-rl", "wechselstrom", "Reihenschaltung R und L",
         "Widerstand und Spule in Reihe an Wechselspannung (Scheinwiderstand, Phasenverschiebung).")
def ac_rl(u_eff: float = 12.0, f: float = 50.0, r: float = 50.0, l: float = 0.2) -> Vorlage:
    return _ac_reihe("ac-rl", "Reihenschaltung R und L", u_eff, f, r, l, 0)


@vorlage("ac-rc", "wechselstrom", "Reihenschaltung R und C",
         "Widerstand und Kondensator in Reihe an Wechselspannung.")
def ac_rc(u_eff: float = 12.0, f: float = 50.0, r: float = 50.0, c: float = 47e-6) -> Vorlage:
    return _ac_reihe("ac-rc", "Reihenschaltung R und C", u_eff, f, r, 0, c)


@vorlage("ac-rlc", "wechselstrom", "Reihenschwingkreis R, L und C",
         "Reihenschaltung aus R, L und C; f = 0 setzt die Resonanzfrequenz f0 = 1/(2π√(LC)) ein.")
def ac_rlc(u_eff: float = 12.0, f: float = 0.0, r: float = 20.0, l: float = 0.2, c: float = 47e-6) -> Vorlage:
    f0 = 1 / (2 * math.pi * math.sqrt(l * c))
    freq = f0 if f <= 0 else f
    v = _ac_reihe("ac-rlc", "Reihenschwingkreis R, L und C", u_eff, freq, r, l, c)
    v.hinweise.append(f"Resonanzfrequenz f0 = {f0:.4g} Hz; bei f0 ist I maximal (I = U/R), U_L = U_C.")
    v.parameter["f"] = freq
    return v


@vorlage("ac-parallel", "wechselstrom", "Parallelschaltung R, L und C",
         "R, L und C parallel an Wechselspannung; Amperemeter im Gesamtstrom und in jedem Zweig (Blindstromkompensation, Parallelschwingkreis).")
def ac_parallel(u_eff: float = 12.0, f: float = 50.0, r: float = 100.0, l: float = 0.2, c: float = 47e-6) -> Vorlage:
    b = Bau("Parallelschaltung R, L, C", zeitschritt=_dt(f))
    quelle = b.quelle_ac((6, 20), (6, 6), u_eff, f, math.pi / 2, name="u")   # Kosinus: kein Einschaltgleichanteil in L
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I", effektiv=True)
    b.schiene((14, 6), (20, 6), (28, 6), (36, 6), (44, 6), (44, 8))
    w = 2 * math.pi * f
    zweige = [("R", 20, r, "r", u_eff / r), ("L", 28, l, "l", u_eff / (w * l)), ("C", 36, c, "c", u_eff * w * c)]
    for kn, x, wert, typ, i_k in zweige:
        b.draht((x, 6), (x, 8))
        b.amperemeter((x, 8), (x, 12), f"I_{kn}", effektiv=True)
        if typ == "r":
            b.widerstand((x, 12), (x, 18), wert, kn)
        elif typ == "l":
            b.spule((x, 12), (x, 18), wert, 0.0, kn)
        else:
            b.kondensator((x, 12), (x, 18), wert, u_eff * math.sqrt(2), kn)
        b.draht((x, 18), (x, 20))
    b.voltmeter((44, 8), (44, 18), "U", effektiv=True)
    b.draht((44, 18), (44, 20))
    b.schiene((6, 20), (20, 20), (28, 20), (36, 20), (44, 20))
    b.oszi(quelle, skala=u_eff * math.sqrt(2) * 1.25)
    i_w = u_eff / r
    i_b = u_eff * (w * c - 1 / (w * l))
    erw = [Erwartung("I", math.hypot(i_w, i_b), "A"), Erwartung("I_R", i_w, "A"),
           Erwartung("I_L", u_eff / (w * l), "A"), Erwartung("I_C", u_eff * w * c, "A"), Erwartung("U", u_eff, "V")]
    return Vorlage("ac-parallel", "Parallelschaltung R, L und C", "wechselstrom", b, erw,
                   _para(u_eff=u_eff, f=f, r=r, l=l, c=c),
                   hinweise=["Die Zweigströme addieren sich geometrisch: I² = I_R² + (I_C − I_L)²."],
                   dauer=0.08, fenster=0.06,
                   formeln=[r"I = \sqrt{I_R^2 + (I_C - I_L)^2}", r"I_L = \frac{U}{\omega L},\quad I_C = U\,\omega C"])


@vorlage("ac-kompensation", "wechselstrom", "Blindstromkompensation einer induktiven Last",
         "Last aus R und L (Motor, Leuchtstofflampe) mit parallelem Kompensationskondensator über Schalter; c = 0 wählt C für cos φ = 1.")
def ac_kompensation(u_eff: float = 230.0, f: float = 50.0, r: float = 40.0, l: float = 0.1,
                    c: float = 0.0, kompensiert: bool = True) -> Vorlage:
    w = 2 * math.pi * f
    c_opt = l / (r * r + (w * l) ** 2)
    c_wert = c_opt if c <= 0 else c
    b = Bau("Blindstromkompensation", zeitschritt=_dt(f))
    quelle = b.quelle_ac((6, 22), (6, 6), u_eff, f, name="u")
    b.draht((6, 6), (10, 6))
    b.amperemeter((10, 6), (14, 6), "I", effektiv=True)
    b.schiene((14, 6), (20, 6), (30, 6), (38, 6), (38, 8))
    b.draht((20, 6), (20, 8))
    b.amperemeter((20, 8), (20, 12), "I_L", effektiv=True)
    b.widerstand((20, 12), (20, 16), r, "R")
    b.spule((20, 16), (20, 20), l, 0.0, "L")
    b.draht((20, 20), (20, 22))
    b.draht((30, 6), (30, 8))
    b.schalter((30, 8), (30, 11), kompensiert, "S")
    b.amperemeter((30, 11), (30, 15), "I_C", effektiv=True)
    b.kondensator((30, 15), (30, 20), c_wert, 0.0, "C")
    b.draht((30, 20), (30, 22))
    b.voltmeter((38, 8), (38, 20), "U", effektiv=True)
    b.draht((38, 20), (38, 22))
    b.schiene((6, 22), (20, 22), (30, 22), (38, 22))
    b.oszi(quelle, skala=u_eff * math.sqrt(2) * 1.25)
    zl = complex(r, w * l)
    il = u_eff / zl
    ic = 1j * w * c_wert * u_eff if kompensiert else 0j
    # Zeiger: I_L = U/Z_L (Spannung als Bezug), I_C = jωC·U
    ig = il + ic
    erw = [Erwartung("I", abs(ig), "A"), Erwartung("I_L", abs(il), "A"), Erwartung("I_C", abs(ic), "A"),
           Erwartung("U", u_eff, "V")]
    cos_vor = r / abs(zl)
    cos_nach = math.cos(math.atan2(-ig.imag, ig.real)) if kompensiert else cos_vor
    return Vorlage("ac-kompensation", "Blindstromkompensation", "wechselstrom", b, erw,
                   _para(u_eff=u_eff, f=f, r=r, l=l, c=c_wert, kompensiert=kompensiert),
                   hinweise=[f"cos φ der Last = {cos_vor:.3g}; Kompensation auf cos φ = 1 mit C = {c_opt * 1e6:.4g} µF. "
                             f"Gesamtstrom mit Kompensation {abs(il + 1j * w * c_wert * u_eff):.4g} A (cos φ = {cos_nach:.3g})."],
                   dauer=0.08, fenster=0.06,
                   formeln=[r"\cos\varphi = \frac{R}{\sqrt{R^2 + (\omega L)^2}}",
                            r"C = \frac{L}{R^2 + (\omega L)^2}\quad (\cos\varphi = 1)"])


@vorlage("ac-transformator", "wechselstrom", "Belasteter Transformator",
         "Transformator mit Lastwiderstand; Spannungen und Ströme auf Primär- und Sekundärseite (Übersetzungsverhältnis, Wirkungsgrad).")
def ac_transformator(u1_eff: float = 24.0, f: float = 50.0, l1: float = 5.0, ratio: float = 0.5,
                     r_last: float = 10.0) -> Vorlage:
    b = Bau("Transformator", zeitschritt=_dt(f))
    quelle = b.quelle_ac((6, 16), (6, 6), u1_eff, f, math.pi / 2, name="u1")   # Kosinus: kein Einschalt-Magnetisierungsstrom
    b.draht((6, 6), (8, 6))
    b.amperemeter((8, 6), (12, 6), "I1", effektiv=True)
    b.draht((12, 6), (16, 6), (16, 8))
    b.draht((12, 6), (12, 8))
    b.voltmeter((12, 8), (12, 14), "U1", effektiv=True)
    b.draht((12, 14), (12, 16))
    b.transformator((16, 8), (24, 8), l1, ratio)
    b.draht((16, 10), (16, 16))
    b.schiene((6, 16), (12, 16), (16, 16))
    b.draht((24, 8), (24, 6))
    b.amperemeter((24, 6), (28, 6), "I2", effektiv=True)
    b.schiene((28, 6), (34, 6), (40, 6), (40, 8))
    b.draht((34, 6), (34, 8))
    b.widerstand((34, 8), (34, 14), r_last, "R")
    b.draht((34, 14), (34, 16))
    b.voltmeter((40, 8), (40, 14), "U2", effektiv=True)
    b.draht((40, 14), (40, 16))
    b.draht((24, 10), (24, 16))
    b.schiene((24, 16), (34, 16), (40, 16))
    b.oszi(quelle, skala=u1_eff * math.sqrt(2) * 1.25)
    # Ersatzschaltung: Streuinduktivität (1-k)·L1 in Reihe, Hauptinduktivität ·k parallel
    w = 2 * math.pi * f
    k = 0.999
    l2 = l1 * ratio * ratio
    m = k * l1 * ratio
    z1, z2, zm = 1j * w * l1, 1j * w * l2 + r_last, 1j * w * m
    # U1 = z1·I1 + zm·I2 ; 0 = zm·I1 + z2·I2 (Strom I2 in Gegenrichtung zur Last)
    det = z1 * z2 - zm * zm
    i1 = u1_eff * z2 / det
    i2 = -u1_eff * zm / det
    u2 = abs(i2) * r_last
    erw = [Erwartung("U1", u1_eff, "V"), Erwartung("I1", abs(i1), "A", 0.03), Erwartung("U2", u2, "V", 0.03),
           Erwartung("I2", abs(i2), "A", 0.03)]
    return Vorlage("ac-transformator", "Belasteter Transformator", "wechselstrom", b, erw,
                   _para(u1_eff=u1_eff, f=f, l1=l1, ratio=ratio, r_last=r_last),
                   hinweise=[f"Übersetzung ü = N1/N2 = {1 / ratio:.3g}; Leerlauf-Näherung U2 ≈ U1·{ratio:g} = {u1_eff * ratio:.4g} V. "
                             "Primärinduktivität und Kopplung (0,999) begrenzen den Magnetisierungsstrom und die Genauigkeit."],
                   dauer=0.08, fenster=0.06,
                   formeln=[r"\frac{U_1}{U_2} \approx \frac{N_1}{N_2}", r"\frac{I_1}{I_2} \approx \frac{N_2}{N_1}",
                            r"\eta = \frac{P_2}{P_1}"])


def _filter(name: str, titel: str, tiefpass: bool, u_eff: float, f: float, r: float, c: float) -> Vorlage:
    b = Bau(titel, zeitschritt=_dt(f))
    quelle = b.quelle_ac((6, 20), (6, 6), u_eff, f, name="u_e")
    b.draht((6, 6), (8, 6))
    b.amperemeter((8, 6), (12, 6), "I", effektiv=True)
    b.draht((12, 6), (14, 6))
    # Eingangsspannung an der Quelle
    b.draht((8, 6), (8, 8))
    b.voltmeter((8, 8), (8, 18), "U_e", effektiv=True)
    b.draht((8, 18), (8, 20))
    if tiefpass:
        b.widerstand((14, 6), (24, 6), r, "R")
        b.schiene((24, 6), (30, 6), (36, 6), (36, 8))
        b.draht((30, 6), (30, 8))
        b.kondensator((30, 8), (30, 16), c, 0.0, "C")
    else:
        b.kondensator((14, 6), (24, 6), c, 0.0, "C")
        b.schiene((24, 6), (30, 6), (36, 6), (36, 8))
        b.draht((30, 6), (30, 8))
        b.widerstand((30, 8), (30, 16), r, "R")
    b.draht((30, 16), (30, 20))
    b.voltmeter((36, 8), (36, 18), "U_a", effektiv=True)
    b.draht((36, 18), (36, 20))
    b.schiene((6, 20), (8, 20), (30, 20), (36, 20))
    b.oszi(quelle, skala=u_eff * math.sqrt(2) * 1.25, zeitmass=0.05 if f < 200 else 0.0025)
    w = 2 * math.pi * f
    xc = 1 / (w * c)
    ue = u_eff
    ua = ue * (xc / math.hypot(r, xc) if tiefpass else r / math.hypot(r, xc))
    i = ue / math.hypot(r, xc)
    fg = 1 / (2 * math.pi * r * c)
    return Vorlage(name, titel, "wechselstrom", b,
                   [Erwartung("U_e", ue, "V"), Erwartung("U_a", ua, "V"), Erwartung("I", i, "A")],
                   _para(u_eff=u_eff, f=f, r=r, c=c),
                   hinweise=[f"Grenzfrequenz f_g = 1/(2π·R·C) = {fg:.4g} Hz; bei f_g ist U_a = U_e/√2."],
                   dauer=max(0.08, 20 / f), fenster=max(0.06, 10 / f),
                   formeln=[r"f_g = \frac{1}{2\pi R C}",
                            r"\frac{U_a}{U_e} = \frac{X_C}{\sqrt{R^2 + X_C^2}}" if tiefpass
                            else r"\frac{U_a}{U_e} = \frac{R}{\sqrt{R^2 + X_C^2}}"])


@vorlage("ac-tiefpass", "wechselstrom", "RC-Tiefpass",
         "Spannungsteiler aus R und C; Eingangs- und Ausgangsspannung, Grenzfrequenz f_g = 1/(2πRC).")
def ac_tiefpass(u_eff: float = 5.0, f: float = 1000.0, r: float = 1000.0, c: float = 100e-9) -> Vorlage:
    return _filter("ac-tiefpass", "RC-Tiefpass", True, u_eff, f, r, c)


@vorlage("ac-hochpass", "wechselstrom", "RC-Hochpass",
         "Spannungsteiler aus C und R; Eingangs- und Ausgangsspannung, Grenzfrequenz f_g = 1/(2πRC).")
def ac_hochpass(u_eff: float = 5.0, f: float = 1000.0, r: float = 1000.0, c: float = 100e-9) -> Vorlage:
    return _filter("ac-hochpass", "RC-Hochpass", False, u_eff, f, r, c)


@vorlage("drehstrom-stern", "wechselstrom", "Drehstrom: Sternschaltung",
         "Drei Strangspannungen (120° versetzt) an drei Lastwiderständen in Sternschaltung; Strangströme, Strangspannungen, Außenleiterspannung L1–L2, Neutralleiterstrom.")
def drehstrom_stern(u_str: float = 230.0, f: float = 50.0, r1: float = 100.0, r2: float = 100.0,
                    r3: float = 100.0, neutralleiter: bool = True) -> Vorlage:
    b = Bau("Drehstrom Stern", zeitschritt=_dt(f))
    ys = (8, 18, 28)
    phasen = (0.0, -2 * math.pi / 3, 2 * math.pi / 3)
    rs = (r1, r2, r3)
    for k, (y, ph, r) in enumerate(zip(ys, phasen, rs), 1):
        q = b.quelle_ac((6, y), (14, y), u_str, f, ph, name=f"u{k}")
        b.draht((14, y), (18, y))
        b.amperemeter((18, y), (22, y), f"I{k}", effektiv=True)
        b.draht((22, y), (26, y))
        b.draht((26, y), (30, y))
        b.widerstand((30, y), (38, y), r, f"R{k}")
        # Strangspannung über dem Lastwiderstand (Spannung L - N')
        b.draht((30, y), (30, y - 3), (32, y - 3))
        b.voltmeter((32, y - 3), (36, y - 3), f"U{k}", effektiv=True)
        b.draht((36, y - 3), (38, y - 3), (38, y))
        b.draht((38, y), (42, y))
        if k == 1:
            b.oszi(q, skala=u_str * math.sqrt(2) * 1.25)
    b.draht((6, ys[0]), (6, ys[1]))
    b.draht((6, ys[1]), (6, ys[2]))
    b.draht((42, ys[0]), (42, ys[1]))
    b.draht((42, ys[1]), (42, ys[2]))
    if neutralleiter:
        b.draht((6, ys[2]), (6, 34))
        b.draht((6, 34), (18, 34))
        b.amperemeter((18, 34), (22, 34), "I_N", effektiv=True)
        b.draht((22, 34), (42, 34), (42, ys[2]))
    # Außenleiterspannung zwischen L1 und L2 (Leitung bei x = 26 zwischen beiden Strängen)
    b.voltmeter((26, ys[0]), (26, ys[1]), "U_12", effektiv=True)
    # Zeigerrechnung
    ua = [cmath_rect(u_str, p) for p in phasen]
    if neutralleiter:
        i_ph = [ua[k] / rs[k] for k in range(3)]
        un = 0j
    else:
        y_ = [1 / x for x in rs]
        un = sum(ua[k] * y_[k] for k in range(3)) / sum(y_)
        i_ph = [(ua[k] - un) / rs[k] for k in range(3)]
    i_n = abs(sum(i_ph)) if neutralleiter else 0.0
    erw = [Erwartung(f"I{k + 1}", abs(i_ph[k]), "A") for k in range(3)]
    erw += [Erwartung(f"U{k + 1}", abs(ua[k] - un), "V") for k in range(3)]
    erw.append(Erwartung("U_12", abs(ua[0] - ua[1]), "V"))
    if neutralleiter:
        erw.append(Erwartung("I_N", i_n, "A", 0.02))
    return Vorlage("drehstrom-stern", "Drehstrom: Sternschaltung", "wechselstrom", b, erw,
                   _para(u_str=u_str, f=f, r1=r1, r2=r2, r3=r3, neutralleiter=neutralleiter),
                   hinweise=["Außenleiterspannung U_L = √3·U_Str = "
                             f"{math.sqrt(3) * u_str:.4g} V (bei Standard 230 V Strangspannung: 400 V). "
                             "Ohne Neutralleiter (neutralleiter=False) verschiebt ein unsymmetrischer Last den Sternpunkt."],
                   dauer=0.08, fenster=0.06,
                   formeln=[r"U_L = \sqrt{3}\cdot U_{Str}", r"I_L = I_{Str}", r"\underline{I}_N = \underline{I}_1 + \underline{I}_2 + \underline{I}_3"])


def cmath_rect(betrag: float, phase: float) -> complex:
    import cmath
    return cmath.rect(betrag, phase)
