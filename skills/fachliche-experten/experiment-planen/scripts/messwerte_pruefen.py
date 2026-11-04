#!/usr/bin/env python3
"""messwerte_pruefen – Messwerte und Rechnungen in Experimenten und Erwartungshorizonten
plausibilisieren (ohne Zusatzpakete).

Unterbefehle:
  faraday      höchstes Gasvolumen einer Elektrolyse nach Faraday mit einer Angabe vergleichen
               python3 messwerte_pruefen.py faraday --strom 0.2 --zeit 90 --volumen-ml 2.0
               [--gas H2|O2|Cl2] [--temperatur 20] [--druck 1013]
  kette        Wirkungsgradkette rückwärts rechnen (Nutzen → Aufwand) und Angaben prüfen;
               erkennt „multipliziert statt dividiert“ und „Aufschlag (1−η) statt Division“
               python3 messwerte_pruefen.py kette --schritt 22400:0.9:24640 [--schritt AUS:ETA:ANGABE …]
               python3 messwerte_pruefen.py kette --eta 0.9 0.95 0.74 --ausgang 22400 [--angabe 31000]
  wirkungsgrad η = abgegeben / zugeführt; η > 1 ist unmöglich
               python3 messwerte_pruefen.py wirkungsgrad --zu 90 --ab 32
  einheit      Dimension einer Einheit mit der erwarteten vergleichen (erkennt Kehrwerte)
               python3 messwerte_pruefen.py einheit "10 m³/MJ" --erwartet "MJ/m³"
  unsicherheit Wert und Messunsicherheit einer Formel (Gauß und Größtfehler)
               python3 messwerte_pruefen.py unsicherheit "U*I*t" U=10:0.1 I=0.15:0.005 t=60:1

Exit-Code: 0 = plausibel, 1 = mindestens ein ❌, 2 = Eingabefehler. --json für Maschinen.
"""

from __future__ import annotations

import argparse
import ast
import json
import math
import operator
import re
import sys

FARADAY = 96485.33212        # C/mol
R_GAS = 8.314462618          # J/(mol·K)
Z_GAS = {"H2": 2, "O2": 4, "Cl2": 2}
TOLERANZ = 0.02              # 2 % Spielraum für Messwerte (Faraday)
TOL_MUSTER = 0.001           # 0,1 % für das Erkennen von Rechenfehlermustern
TOL_RUNDUNG = 0.005          # 0,5 % Rundungsspielraum bei Rechnungen


def _zahl(text: str) -> float:
    return float(str(text).replace(",", ".").replace(" ", "").replace(" ", ""))


# ───────────────────────────── Faraday ─────────────────────────────

def faraday(strom: float, zeit: float, volumen_ml: float | None, gas: str = "H2",
            temperatur: float = 20.0, druck_hpa: float = 1013.25) -> dict:
    if strom <= 0 or zeit <= 0:
        raise ValueError("Strom und Zeit müssen positiv sein")
    z = Z_GAS[gas]
    n = strom * zeit / (z * FARADAY)
    v_max_ml = n * R_GAS * (temperatur + 273.15) / (druck_hpa * 100) * 1e6
    erg = {"gas": gas, "ladung_C": strom * zeit, "stoffmenge_mol": n, "v_max_ml": v_max_ml}
    if volumen_ml is not None:
        eta = volumen_ml / v_max_ml
        erg["angabe_ml"] = volumen_ml
        erg["faraday_wirkungsgrad"] = eta
        if eta > 1 + TOLERANZ:
            erg["status"] = "❌"
            erg["befund"] = (f"{volumen_ml:g} ml {gas} sind unmöglich – höchstens {v_max_ml:.2f} ml "
                             f"(Faraday-Wirkungsgrad {eta:.0%}); Messwerte aus einem Vorversuch nehmen")
        else:
            erg["status"] = "✅"
            erg["befund"] = f"plausibel – Faraday-Wirkungsgrad {eta:.0%} (Obergrenze {v_max_ml:.2f} ml)"
    else:
        erg["status"] = "✅"
        erg["befund"] = f"Obergrenze {v_max_ml:.2f} ml {gas}"
    return erg


# ───────────────────────────── Wirkungsgradkette ─────────────────────────────

def schritt(ausgang: float, eta: float, angabe: float | None) -> dict:
    """Ein Rückwärtsschritt: Aufwand = Nutzen / η."""
    if not 0 < eta <= 1:
        raise ValueError(f"Wirkungsgrad {eta} außerhalb (0; 1]")
    richtig = ausgang / eta
    erg = {"ausgang": ausgang, "eta": eta, "richtig": richtig}
    if angabe is None:
        erg.update(status="✅", befund=f"{ausgang:g} ÷ {eta:g} = {richtig:.6g}")
        return erg
    erg["angabe"] = angabe

    def nah(a: float, b: float, tol: float) -> bool:
        return abs(a - b) <= tol * max(abs(b), 1e-12)

    # Fehlermuster zuerst und eng prüfen: ×1,1 statt ÷0,9 weicht nur um 1 % ab.
    if nah(angabe, richtig, TOL_MUSTER):
        erg.update(status="✅", befund=f"{angabe:g} stimmt ({ausgang:g} ÷ {eta:g} = {richtig:.6g})")
    elif nah(angabe, ausgang * eta, TOL_MUSTER):
        erg.update(status="❌", befund=f"multipliziert statt dividiert: {ausgang:g} × {eta:g} = {ausgang * eta:.6g}; "
                                       f"richtig {ausgang:g} ÷ {eta:g} = {richtig:.6g}")
    elif nah(angabe, ausgang * (2 - eta), TOL_MUSTER):
        erg.update(status="❌", befund=f"Aufschlag statt Division: {ausgang:g} × (1 + {1 - eta:g}) = {ausgang * (2 - eta):.6g}; "
                                       f"richtig {ausgang:g} ÷ {eta:g} = {richtig:.6g}")
    elif nah(angabe, richtig, TOL_RUNDUNG):
        erg.update(status="✅", befund=f"{angabe:g} stimmt im Rahmen der Rundung ({ausgang:g} ÷ {eta:g} = {richtig:.6g})")
    else:
        erg.update(status="❌", befund=f"{angabe:g} weicht ab; richtig {ausgang:g} ÷ {eta:g} = {richtig:.6g} "
                                       f"({(angabe - richtig) / richtig:+.1%})")
    return erg


def kette(etas: list[float], ausgang: float, angabe: float | None) -> dict:
    gesamt = math.prod(etas)
    erg = schritt(ausgang, gesamt, angabe)
    erg["etas"] = etas
    erg["eta_gesamt"] = gesamt
    return erg


# ───────────────────────────── Einheiten ─────────────────────────────

# Basisdimensionen: m, kg, s, A, K, mol
_BASIS = {
    "m": (1, 0, 0, 0, 0, 0), "g": (0, 1, 0, 0, 0, 0), "s": (0, 0, 1, 0, 0, 0),
    "A": (0, 0, 0, 1, 0, 0), "K": (0, 0, 0, 0, 1, 0), "mol": (0, 0, 0, 0, 0, 1),
}
_ABGELEITET = {
    "N": (1, 1, -2, 0, 0, 0), "J": (2, 1, -2, 0, 0, 0), "W": (2, 1, -3, 0, 0, 0),
    "Pa": (-1, 1, -2, 0, 0, 0), "C": (0, 0, 1, 1, 0, 0), "V": (2, 1, -3, -1, 0, 0),
    "Ω": (2, 1, -3, -2, 0, 0), "Hz": (0, 0, -1, 0, 0, 0),
    "l": (3, 0, 0, 0, 0, 0), "L": (3, 0, 0, 0, 0, 0), "bar": (-1, 1, -2, 0, 0, 0),
    "min": (0, 0, 1, 0, 0, 0), "h": (0, 0, 1, 0, 0, 0), "t": (0, 1, 0, 0, 0, 0),
    "°C": (0, 0, 0, 0, 1, 0), "Wh": (2, 1, -2, 0, 0, 0),
}
_PRAEFIX = {"k": 3, "M": 6, "G": 9, "m": -3, "c": -2, "µ": -6, "u": -6, "h": 2, "n": -9}
_EINHEITEN = {**_BASIS, **_ABGELEITET}


def _dimension_atom(atom: str) -> tuple[int, ...]:
    m = re.fullmatch(r"([^\d^²³⁻]+)(?:\^?(-?\d+)|([²³]))?", atom)
    if not m:
        raise ValueError(f"Einheit unklar: {atom}")
    name, exp = m.group(1), m.group(2) or {"²": "2", "³": "3"}.get(m.group(3) or "", "1")
    if name in _EINHEITEN:
        dim = _EINHEITEN[name]
    elif len(name) > 1 and name[0] in _PRAEFIX and name[1:] in _EINHEITEN:
        dim = _EINHEITEN[name[1:]]
    else:
        raise ValueError(f"Einheit unbekannt: {name}")
    return tuple(d * int(exp) for d in dim)


def dimension(einheit: str) -> tuple[int, ...]:
    text = re.sub(r"^[\s\d.,+-]+", "", einheit.strip())        # Zahl davor entfernen
    text = text.replace("·", "*").replace("⋅", "*").replace(" ", "*")
    zaehler, *nenner = text.split("/")
    dim = [0] * 6
    for teil, vorzeichen in [(zaehler, 1)] + [(n, -1) for n in nenner]:
        for atom in filter(None, teil.split("*")):
            for i, d in enumerate(_dimension_atom(atom)):
                dim[i] += vorzeichen * d
    return tuple(dim)


def einheit_pruefen(angabe: str, erwartet: str) -> dict:
    d1, d2 = dimension(angabe), dimension(erwartet)
    if d1 == d2:
        return {"status": "✅", "befund": f"„{angabe}“ hat die Dimension von {erwartet}"}
    if all(a == -b for a, b in zip(d1, d2)):
        return {"status": "❌", "befund": f"„{angabe}“ ist der Kehrwert von {erwartet} – Einheit vertauscht"}
    return {"status": "❌", "befund": f"„{angabe}“ passt nicht zu {erwartet}"}


# ───────────────────────────── Unsicherheit ─────────────────────────────

_OPS = {ast.Add: operator.add, ast.Sub: operator.sub, ast.Mult: operator.mul,
        ast.Div: operator.truediv, ast.Pow: operator.pow, ast.USub: operator.neg}
_FUNK = {"sqrt": math.sqrt, "pi": math.pi}


def _werte_aus(knoten: ast.AST, werte: dict[str, float]) -> float:
    if isinstance(knoten, ast.Expression):
        return _werte_aus(knoten.body, werte)
    if isinstance(knoten, ast.Constant) and isinstance(knoten.value, (int, float)):
        return float(knoten.value)
    if isinstance(knoten, ast.Name):
        if knoten.id in werte:
            return werte[knoten.id]
        if knoten.id == "pi":
            return math.pi
        raise ValueError(f"Größe ohne Wert: {knoten.id}")
    if isinstance(knoten, ast.BinOp) and type(knoten.op) in _OPS:
        return _OPS[type(knoten.op)](_werte_aus(knoten.left, werte), _werte_aus(knoten.right, werte))
    if isinstance(knoten, ast.UnaryOp) and type(knoten.op) in _OPS:
        return _OPS[type(knoten.op)](_werte_aus(knoten.operand, werte))
    if isinstance(knoten, ast.Call) and isinstance(knoten.func, ast.Name) and knoten.func.id == "sqrt":
        return math.sqrt(_werte_aus(knoten.args[0], werte))
    raise ValueError("Formel darf nur + − * / ** , sqrt und pi enthalten")


def unsicherheit(formel: str, groessen: dict[str, tuple[float, float]]) -> dict:
    baum = ast.parse(formel.replace("^", "**").replace("·", "*"), mode="eval")
    mitte = {k: v for k, (v, _) in groessen.items()}
    wert = _werte_aus(baum, mitte)
    gauss = groesst = 0.0
    beitraege = {}
    for name, (v, u) in groessen.items():
        h = (abs(v) or 1.0) * 1e-6
        plus, minus = dict(mitte), dict(mitte)
        plus[name], minus[name] = v + h, v - h
        ableitung = (_werte_aus(baum, plus) - _werte_aus(baum, minus)) / (2 * h)
        beitrag = abs(ableitung * u)
        beitraege[name] = beitrag
        gauss += beitrag ** 2
        groesst += beitrag
    gauss = math.sqrt(gauss)
    rel = gauss / abs(wert) if wert else float("nan")
    return {"status": "✅", "wert": wert, "u_gauss": gauss, "u_groesstfehler": groesst,
            "relativ": rel, "beitraege": beitraege,
            "befund": f"{wert:.6g} ± {gauss:.3g} (Gauß, {rel:.1%}); Größtfehler ± {groesst:.3g}"}


# ───────────────────────────── CLI ─────────────────────────────

def _ausgeben(ergebnisse: list[dict], als_json: bool) -> int:
    if als_json:
        print(json.dumps(ergebnisse, ensure_ascii=False, indent=2))
    else:
        for e in ergebnisse:
            print(f"{e['status']} {e['befund']}")
    return 1 if any(e["status"] == "❌" for e in ergebnisse) else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Messwerte und Rechnungen plausibilisieren.")
    ap.add_argument("--json", action="store_true")
    sub = ap.add_subparsers(dest="befehl", required=True)
    f = sub.add_parser("faraday")
    f.add_argument("--strom", required=True, help="Stromstärke in A")
    f.add_argument("--zeit", required=True, help="Zeit in s")
    f.add_argument("--volumen-ml", help="angegebenes Gasvolumen in ml")
    f.add_argument("--gas", default="H2", choices=sorted(Z_GAS))
    f.add_argument("--temperatur", default="20", help="°C")
    f.add_argument("--druck", default="1013.25", help="hPa")
    k = sub.add_parser("kette")
    k.add_argument("--schritt", action="append", default=[], help="AUSGANG:ETA:ANGABE (ANGABE optional)")
    k.add_argument("--eta", nargs="+", default=[], help="Wirkungsgrade der Kette")
    k.add_argument("--ausgang", help="Nutzen am Ende der Kette")
    k.add_argument("--angabe", help="angegebener Aufwand am Anfang der Kette")
    w = sub.add_parser("wirkungsgrad")
    w.add_argument("--zu", required=True)
    w.add_argument("--ab", required=True)
    e = sub.add_parser("einheit")
    e.add_argument("angabe")
    e.add_argument("--erwartet", required=True)
    u = sub.add_parser("unsicherheit")
    u.add_argument("formel")
    u.add_argument("groessen", nargs="+", help="NAME=WERT:UNSICHERHEIT")
    a = ap.parse_args(argv)
    try:
        if a.befehl == "faraday":
            ergebnisse = [faraday(_zahl(a.strom), _zahl(a.zeit),
                                  _zahl(a.volumen_ml) if a.volumen_ml else None,
                                  a.gas, _zahl(a.temperatur), _zahl(a.druck))]
        elif a.befehl == "kette":
            ergebnisse = []
            for s in a.schritt:
                teile = s.split(":")
                if len(teile) not in (2, 3):
                    raise ValueError(f"--schritt {s!r}: Form AUSGANG:ETA[:ANGABE]")
                ergebnisse.append(schritt(_zahl(teile[0]), _zahl(teile[1]),
                                          _zahl(teile[2]) if len(teile) == 3 and teile[2] else None))
            if a.eta:
                if not a.ausgang:
                    raise ValueError("--eta braucht --ausgang")
                ergebnisse.append(kette([_zahl(x) for x in a.eta], _zahl(a.ausgang),
                                        _zahl(a.angabe) if a.angabe else None))
            if not ergebnisse:
                raise ValueError("kette braucht --schritt oder --eta mit --ausgang")
        elif a.befehl == "wirkungsgrad":
            zu, ab = _zahl(a.zu), _zahl(a.ab)
            eta = ab / zu
            ergebnisse = [{"status": "❌" if eta > 1 + 1e-9 else "✅", "eta": eta,
                           "befund": f"η = {ab:g} / {zu:g} = {eta:.3f}" + (" – größer als 1, unmöglich" if eta > 1 + 1e-9 else "")}]
        elif a.befehl == "einheit":
            ergebnisse = [einheit_pruefen(a.angabe, a.erwartet)]
        else:
            groessen = {}
            for g in a.groessen:
                m = re.fullmatch(r"(\w+)=([-\d.,eE+]+):([\d.,eE+-]+)", g)
                if not m:
                    raise ValueError(f"Größe {g!r}: Form NAME=WERT:UNSICHERHEIT")
                groessen[m.group(1)] = (_zahl(m.group(2)), _zahl(m.group(3)))
            ergebnisse = [unsicherheit(a.formel, groessen)]
    except (ValueError, KeyError, ZeroDivisionError, SyntaxError) as fehler:
        print(f"Fehler: {fehler}", file=sys.stderr)
        return 2
    return _ausgeben(ergebnisse, a.json)


if __name__ == "__main__":
    sys.exit(main())
