#!/usr/bin/env python3
"""falstad_elektronik – Vorlagen für Leistungselektronik und Umrichter (Gleichrichter, Steller, Z-Diode).

Die Schaltungen enthalten Dioden und MOSFETs; Python rechnet sie nicht nach. Die Erwartungswerte
sind Formelwerte (ideal bzw. mit grober Verlustkorrektur) mit weiter Toleranz; maßgeblich sind die
Messwerte der Engine (``engine_pruefen.py``).
"""

from __future__ import annotations

import math

from falstad_bau import Bau
from falstad_vorlagen import Erwartung, Vorlage, _para, vorlage

def _dt_schalt(f_s: float) -> float:
    """Zeitschritt: 40 Schritte je Schaltperiode, nicht unter 1 µs (sonst unbrauchbar langsam)."""
    return max(1e-6, 1 / (40 * f_s))


UD = 0.7   # Durchlassspannung der Falstad-Standarddiode (grobe Näherung für die Erwartung)


def _last_und_messung(b: Bau, x_start: int, y_o: int, y_u: int, r: float, c: float, mittelwert: bool,
                      erw: list, effektiv_name: str = "U_a") -> None:
    """Last (R), optionale Glättung (C), Effektivwert-Voltmeter und Drehspul-Ersatz für den Mittelwert.

    Der Knoten (x_start, y_o) der oberen Schiene liegt bereits; die untere Schiene (y_u) wird hier gezeichnet.
    """
    x = x_start
    b.draht((x, y_o), (x, y_o + 2))
    b.widerstand((x, y_o + 2), (x, y_u - 2), r, "R")
    b.draht((x, y_u - 2), (x, y_u))
    unten = [x]
    letzter = x
    if c > 0:
        b.draht((x, y_o), (x + 6, y_o))
        b.draht((x + 6, y_o), (x + 6, y_o + 2))
        b.kondensator((x + 6, y_o + 2), (x + 6, y_u - 2), c, 0.0, "C")
        b.draht((x + 6, y_u - 2), (x + 6, y_u))
        unten.append(x + 6)
        letzter = x + 6
    xv = letzter + 6
    b.draht((letzter, y_o), (xv, y_o))
    b.draht((xv, y_o), (xv, y_o + 2))
    b.voltmeter((xv, y_o + 2), (xv, y_u - 2), effektiv_name, effektiv=True)
    b.draht((xv, y_u - 2), (xv, y_u))
    unten.append(xv)
    if mittelwert:
        xm = xv + 6
        b.draht((xv, y_o), (xm, y_o))
        b.widerstand((xm, y_o), (xm + 6, y_o), 100e3, "Rm")
        b.draht((xm + 6, y_o), (xm + 6, y_o + 2))
        b.kondensator((xm + 6, y_o + 2), (xm + 6, y_u - 2), 1e-6, 0.0, "Cm")
        b.draht((xm + 6, y_u - 2), (xm + 6, y_u))
        b.draht((xm + 6, y_o), (xm + 12, y_o), (xm + 12, y_o + 2))
        b.voltmeter((xm + 12, y_o + 2), (xm + 12, y_u - 2), "U_av")
        b.draht((xm + 12, y_u - 2), (xm + 12, y_u))
        unten += [xm + 6, xm + 12]
        b.text((xm - 1, y_o - 5), "Mittelwertmesser")
    b.schiene((unten[0], y_u), *[(u, y_u) for u in unten[1:]])


def _gleichrichter(name: str, titel: str, bruecke: bool, u_eff: float, f: float, r: float, c: float,
                   mittelwert: bool) -> Vorlage:
    b = Bau(titel, zeitschritt=2e-5 if mittelwert else 1e-5)
    erw: list = []
    if not bruecke:
        quelle = b.quelle_ac((6, 20), (6, 8), u_eff, f, name="u")
        b.draht((6, 8), (8, 8))
        b.diode((8, 8), (14, 8), "D")
        b.draht((14, 8), (16, 8))
        b.amperemeter((16, 8), (20, 8), "I", effektiv=True)
        b.draht((20, 8), (26, 8))
        b.draht((6, 20), (6, 22))
        b.masse((6, 22))
        y_u = 22
        x_last = 26
        b.schiene((6, 22), (x_last, 22))
        u_peak = u_eff * math.sqrt(2)
        u_av = (u_peak - UD) / math.pi
        u_rms = (u_peak - UD) / 2
    else:
        ring_tl, ring_tr, ring_br, ring_bl = (16, 8), (28, 8), (28, 20), (16, 20)
        quelle = b.quelle_ac((6, 20), (6, 8), u_eff, f, name="u")
        b.draht((6, 8), (16, 8))
        b.draht((16, 8), (19, 8))
        b.diode((19, 8), (25, 8), "D1")
        b.draht((25, 8), (28, 8))
        b.draht((28, 20), (28, 17))
        b.diode((28, 17), (28, 11), "D2")
        b.draht((28, 11), (28, 8))
        b.draht((16, 20), (16, 17))
        b.diode((16, 17), (16, 11), "D3")
        b.draht((16, 11), (16, 8))
        b.draht((16, 20), (19, 20))
        b.diode((19, 20), (25, 20), "D4")
        b.draht((25, 20), (28, 20))
        b.draht((6, 20), (6, 24), (28, 24), (28, 20))
        b.draht((28, 8), (31, 8))
        b.amperemeter((31, 8), (35, 8), "I", effektiv=True)
        b.draht((35, 8), (38, 8))
        y_u = 26
        x_last = 38
        b.draht((16, 20), (16, 26), (x_last, 26))
        b.masse((16, 26))
        u_peak = u_eff * math.sqrt(2)
        u_av = 2 * (u_peak - 2 * UD) / math.pi
        u_rms = (u_peak - 2 * UD) / math.sqrt(2)
    _last_und_messung(b, x_last, 8, y_u, r, c, mittelwert, erw)
    b.oszi(quelle, skala=u_eff * math.sqrt(2) * 1.25, zeitmass=0.05)
    if c > 0:
        hinweis = "Mit Glättungskondensator: Mittelwert nahe am Scheitelwert, Restwelligkeit sichtbar im Oszilloskop."
        erw = [Erwartung("U_av", u_peak - (2 if bruecke else 1) * UD, "V", 0.15, "Naeherung")] if mittelwert else []
    else:
        hinweis = ("Ohne Glättung gilt für den Mittelwert näherungsweise "
                   + (r"U_av ≈ 2·Û/π (Brücke)" if bruecke else r"U_av ≈ Û/π (Einweg)")
                   + " abzüglich Diodenspannung.")
        erw = [Erwartung("U_av", u_av, "V", 0.12, "Naeherung"), Erwartung("U_a", u_rms, "V", 0.12, "Naeherung")] if mittelwert else [
            Erwartung("U_a", u_rms, "V", 0.12, "Naeherung")]
    return Vorlage(name, titel, "elektronik", b, erw,
                   _para(u_eff=u_eff, f=f, r=r, c=c, mittelwert=mittelwert),
                   hinweise=[hinweis, "Die Voltmeter sind Effektivwertmesser (U_a); Mittelwert (Drehspulmessgerät) über RC-Mittelwertmesser U_av. "
                             "Falstad hat kein Mittelwert-Messgerät; Dioden verwenden das Falstad-Standardmodell."],
                   dauer=0.8 if mittelwert else 0.1, fenster=0.1 if mittelwert else 0.06,
                   formeln=[r"U_{av} = \frac{\hat{u}}{\pi}\ \text{(Einweg)},\qquad U_{av} = \frac{2\hat{u}}{\pi}\ \text{(Brücke)}",
                            r"\hat{u} = \sqrt{2}\,U_{eff}"])


@vorlage("einweggleichrichter", "elektronik", "Einweggleichrichter (M1U)",
         "Eine Diode in Reihe zur Last, optional Glättungskondensator c; Oszilloskop für u und i, Effektivwertmesser und Mittelwertmesser.")
def einweggleichrichter(u_eff: float = 12.0, f: float = 50.0, r: float = 100.0, c: float = 0.0,
                        mittelwert: bool = True) -> Vorlage:
    return _gleichrichter("einweggleichrichter", "Einweggleichrichter", False, u_eff, f, r, c, mittelwert)


@vorlage("brueckengleichrichter", "elektronik", "Brückengleichrichter (B2U)",
         "Vier Dioden in Brückenschaltung, optional Glättungskondensator c; Oszilloskop für u und i, Effektivwertmesser und Mittelwertmesser.")
def brueckengleichrichter(u_eff: float = 12.0, f: float = 50.0, r: float = 100.0, c: float = 0.0,
                          mittelwert: bool = True) -> Vorlage:
    return _gleichrichter("brueckengleichrichter", "Brückengleichrichter", True, u_eff, f, r, c, mittelwert)


@vorlage("zdiode-stabilisierung", "elektronik", "Spannungsstabilisierung mit Z-Diode",
         "Vorwiderstand und Z-Diode parallel zur Last; Eingangsstrom, Z-Strom, Laststrom und Ausgangsspannung.")
def zdiode_stabilisierung(u_ein: float = 12.0, r_v: float = 100.0, u_z: float = 5.1, r_l: float = 470.0) -> Vorlage:
    b = Bau("Z-Diode", zeitschritt=5e-6)
    b.quelle_dc((6, 22), (6, 6), u_ein, "U_e")
    b.draht((6, 6), (8, 6))
    b.amperemeter((8, 6), (12, 6), "I")
    b.draht((12, 6), (14, 6))
    b.widerstand((14, 6), (22, 6), r_v, "Rv")
    b.schiene((22, 6), (28, 6), (36, 6), (44, 6), (44, 8))
    b.draht((28, 6), (28, 8))
    b.amperemeter((28, 8), (28, 12), "I_Z")
    b.draht((28, 12), (28, 13))
    b.zenerdiode((28, 19), (28, 13), u_z, "Z")
    b.draht((28, 19), (28, 22))
    b.draht((36, 6), (36, 8))
    b.amperemeter((36, 8), (36, 12), "I_L")
    b.widerstand((36, 12), (36, 18), r_l, "RL")
    b.draht((36, 18), (36, 22))
    b.voltmeter((44, 8), (44, 20), "U_a")
    b.draht((44, 20), (44, 22))
    b.schiene((6, 22), (28, 22), (36, 22), (44, 22))
    b.masse((6, 22))
    # Erwartung: Z-Diode leitet, falls Spannung am Teiler über u_z liegt
    u_leer = u_ein * r_l / (r_v + r_l)
    if u_leer > u_z:
        ua = u_z
        i_l = ua / r_l
        i_ges = (u_ein - ua) / r_v
        i_z = i_ges - i_l
    else:
        ua = u_leer
        i_ges = u_ein / (r_v + r_l)
        i_l, i_z = i_ges, 0.0
    return Vorlage("zdiode-stabilisierung", "Spannungsstabilisierung mit Z-Diode", "elektronik", b,
                   [Erwartung("U_a", ua, "V", 0.06, "Naeherung"), Erwartung("I", i_ges, "A", 0.06, "Naeherung"),
                    Erwartung("I_L", i_l, "A", 0.06, "Naeherung"), Erwartung("I_Z", i_z, "A", 0.10, "Naeherung")],
                   _para(u_ein=u_ein, r_v=r_v, u_z=u_z, r_l=r_l),
                   hinweise=["Die Falstad-Z-Diode hat einen kleinen differentiellen Widerstand; Abweichungen von wenigen Prozent sind normal."],
                   dauer=0.05, fenster=0.02,
                   formeln=[r"I_V = \frac{U_e - U_Z}{R_V}", r"I_Z = I_V - I_L", r"I_{Z} \ge I_{Z,min}"])


@vorlage("tiefsetzsteller", "elektronik", "Tiefsetzsteller (Buck-Wandler, Gleichspannungswandler)",
         "MOSFET als Schalter mit Rechteckansteuerung (Tastgrad d), Freilaufdiode, Speicherdrossel, Glättungskondensator und Last; Ausgangsspannung ≈ d·Ue.")
def tiefsetzsteller(u_ein: float = 24.0, tastgrad: float = 0.5, f_s: float = 5e3, l: float = 2e-3,
                    c: float = 100e-6, r: float = 10.0) -> Vorlage:
    b = Bau("Tiefsetzsteller", zeitschritt=_dt_schalt(f_s))
    b.quelle_dc((6, 24), (6, 6), u_ein, "U_e")
    b.draht((6, 6), (8, 6))
    b.amperemeter((8, 6), (12, 6), "I_e")
    b.draht((12, 6), (20, 6), (20, 9))
    b.mosfet((16, 10), (20, 9), (20, 11), 2.0, "T")
    b.draht((20, 11), (20, 14))
    b.quelle_rechteck((14, 14), (14, 10), 10.0, f_s, tastgrad)
    b.draht((14, 10), (16, 10))
    b.draht((14, 14), (20, 14))
    b.draht((20, 14), (20, 16))
    b.diode((20, 22), (20, 16), "D")
    b.draht((20, 22), (20, 24))
    b.draht((20, 14), (24, 14))
    quelle_l = b.spule((24, 14), (32, 14), l, 0.0, "L")
    b.draht((32, 14), (36, 14))
    b.draht((36, 14), (36, 16))
    b.kondensator((36, 16), (36, 22), c, 0.0, "C")
    b.draht((36, 22), (36, 24))
    b.draht((36, 14), (38, 14))
    b.amperemeter((38, 14), (42, 14), "I_a")
    b.draht((42, 14), (44, 14), (44, 16))
    b.widerstand((44, 16), (44, 22), r, "R")
    b.draht((44, 22), (44, 24))
    b.draht((44, 14), (52, 14), (52, 16))
    b.voltmeter((52, 16), (52, 22), "U_a")
    b.draht((52, 22), (52, 24))
    b.schiene((6, 24), (20, 24), (36, 24), (44, 24), (52, 24))
    b.masse((6, 24))
    b.oszi(quelle_l, tempo=2, skala=u_ein, zeitmass=2e-6)
    ua = tastgrad * u_ein
    ia = ua / r
    return Vorlage("tiefsetzsteller", "Tiefsetzsteller", "elektronik", b,
                   [Erwartung("U_a", ua, "V", 0.12, "Naeherung"), Erwartung("I_a", ia, "A", 0.12, "Naeherung"),
                    Erwartung("I_e", tastgrad * ia, "A", 0.15, "Naeherung")],
                   _para(u_ein=u_ein, tastgrad=tastgrad, f_s=f_s, l=l, c=c, r=r),
                   hinweise=[f"Ideal: U_a = d·U_e = {ua:.4g} V; Ströme im Lückbetrieb ab Δi_L > 2·I_a. "
                             f"Stromwelligkeit Δi_L = (U_e − U_a)·d/(f·L) = {(u_ein - ua) * tastgrad / (f_s * l):.3g} A. "
                             "Der Schalter wird vom MOSFET mit potentialfreier Gate-Quelle (0 … 10 V Rechteck) angesteuert."],
                   dauer=0.03, fenster=0.004,
                   formeln=[r"U_a = d \cdot U_e", r"\Delta i_L = \frac{(U_e - U_a)\, d}{f_s \cdot L}",
                            r"d = \frac{t_{ein}}{T}"])


@vorlage("hochsetzsteller", "elektronik", "Hochsetzsteller (Boost-Wandler)",
         "Speicherdrossel, MOSFET gegen Masse mit Rechteckansteuerung (Tastgrad d), Diode, Glättungskondensator und Last; Ausgangsspannung ≈ Ue/(1−d).")
def hochsetzsteller(u_ein: float = 12.0, tastgrad: float = 0.5, f_s: float = 5e3, l: float = 5e-3,
                    c: float = 100e-6, r: float = 50.0) -> Vorlage:
    b = Bau("Hochsetzsteller", zeitschritt=_dt_schalt(f_s))
    b.quelle_dc((6, 24), (6, 6), u_ein, "U_e")
    b.draht((6, 6), (8, 6))
    b.amperemeter((8, 6), (12, 6), "I_e")
    b.draht((12, 6), (14, 6))
    quelle_l = b.spule((14, 6), (22, 6), l, 0.0, "L")
    b.draht((22, 6), (24, 6))
    b.draht((24, 6), (24, 13))
    b.mosfet((20, 14), (24, 13), (24, 15), 2.0, "T")
    b.draht((24, 15), (24, 24))
    b.quelle_rechteck((16, 18), (16, 14), 10.0, f_s, tastgrad)
    b.draht((16, 14), (20, 14))
    b.draht((16, 18), (16, 24))
    b.draht((24, 6), (28, 6))
    b.diode((28, 6), (34, 6), "D")
    b.draht((34, 6), (38, 6))
    b.draht((38, 6), (38, 8))
    b.kondensator((38, 8), (38, 18), c, 0.0, "C")
    b.draht((38, 18), (38, 24))
    b.draht((38, 6), (44, 6))
    b.amperemeter((44, 6), (48, 6), "I_a")
    b.draht((48, 6), (54, 6), (54, 8))
    b.widerstand((54, 8), (54, 18), r, "R")
    b.draht((54, 18), (54, 24))
    b.draht((54, 6), (60, 6), (60, 8))
    b.voltmeter((60, 8), (60, 18), "U_a")
    b.draht((60, 18), (60, 24))
    b.schiene((6, 24), (16, 24), (24, 24), (38, 24), (54, 24), (60, 24))
    b.masse((6, 24))
    b.oszi(quelle_l, tempo=2, skala=2 * u_ein, zeitmass=2e-6)
    ua = u_ein / (1 - tastgrad)
    ia = ua / r
    return Vorlage("hochsetzsteller", "Hochsetzsteller", "elektronik", b,
                   [Erwartung("U_a", ua, "V", 0.12, "Naeherung"), Erwartung("I_a", ia, "A", 0.12, "Naeherung"),
                    Erwartung("I_e", ia / (1 - tastgrad), "A", 0.15, "Naeherung")],
                   _para(u_ein=u_ein, tastgrad=tastgrad, f_s=f_s, l=l, c=c, r=r),
                   hinweise=[f"Ideal: U_a = U_e/(1−d) = {ua:.4g} V. Bei kleinen Lasten (großes R) geht der Wandler in den Lückbetrieb über; "
                             "der Ausgang steigt dann über die ideale Formel."],
                   dauer=0.06, fenster=0.004,
                   formeln=[r"U_a = \frac{U_e}{1 - d}", r"I_e = \frac{I_a}{1 - d}", r"\Delta i_L = \frac{U_e\, d}{f_s \cdot L}"])
