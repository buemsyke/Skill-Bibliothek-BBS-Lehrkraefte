#!/usr/bin/env python3
"""schaltung – Versuchsschaltungen für circuit.js (Falstad) erzeugen, prüfen und messen.

    python3 scripts/schaltung.py vorlagen                         # Katalog mit Parametern
    python3 scripts/schaltung.py vorlage reihenschaltung --u 12 --r1 100 -o 41_schaltung.txt
    python3 scripts/schaltung.py pruefen schaltung.txt            # Raster, Anschlüsse, Messgeräte, Nachrechnung
    python3 scripts/schaltung.py pruefen schaltung.txt --engine   # zusätzlich in der echten Engine messen
    python3 scripts/schaltung.py engine schaltung.txt             # Messwerte aller Elemente aus der Engine
    python3 scripts/schaltung.py url schaltung.txt                # Link für den lokalen Simulationsserver

Ausgabeformate von ``vorlage``: Falstad-Text (Standard), ``--js`` (const circuit = `…`;) oder ``--json``.
Exit-Code 1 bei Fehlern der Prüfung, 2 wenn die Engine nicht verfügbar ist.
"""

from __future__ import annotations

import argparse
import inspect
import json
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import falstad_elektronik  # noqa: E402,F401  (registriert die Vorlagen)
import falstad_kern as kern  # noqa: E402
import falstad_vorlagen as vorl  # noqa: E402
from engine_pruefen import EngineFehler, anzeige, messe, vergleiche  # noqa: E402

URL_PARAMETER = "euroResistors=true&whiteBackground=true&conventionalCurrent=true&running=true&editable=true"


def _wert(text: str, standard):
    if isinstance(standard, bool):
        return text.lower() in ("1", "true", "ja", "wahr")
    return float(text.replace(",", "."))


def cmd_vorlagen(args) -> int:
    for bereich in ("gleichstrom", "wechselstrom", "elektronik"):
        print(f"\n== {bereich} ==")
        for name, info in vorl.REGISTER.items():
            if info["bereich"] != bereich:
                continue
            sig = inspect.signature(info["fn"])
            para = ", ".join(f"{k}={p.default}" for k, p in sig.parameters.items())
            print(f"{name:24} {info['titel']}\n{'':24} {info['beschreibung']}\n{'':24} Parameter: {para}")
    return 0


def _erzeuge(name: str, rest: list):
    if name not in vorl.REGISTER:
        raise SystemExit(f"Unbekannte Vorlage '{name}'. Katalog: schaltung.py vorlagen")
    fn = vorl.REGISTER[name]["fn"]
    sig = inspect.signature(fn)
    werte = {}
    i = 0
    while i < len(rest):
        schluessel = rest[i].lstrip("-").replace("-", "_")
        if schluessel not in sig.parameters or i + 1 >= len(rest):
            raise SystemExit(f"Unbekannter Parameter '{rest[i]}' für {name}; erlaubt: {', '.join(sig.parameters)}")
        werte[schluessel] = _wert(rest[i + 1], sig.parameters[schluessel].default)
        i += 2
    return fn(**werte)


def cmd_vorlage(args) -> int:
    v = _erzeuge(args.name, args.rest)
    bericht = kern.pruefe(v.text)
    if not bericht.ok:
        print(kern.bericht_text(bericht), file=sys.stderr)
        return 1
    if args.json:
        ausgabe = json.dumps({
            "name": v.name, "titel": v.titel, "bereich": v.bereich, "parameter": v.parameter,
            "dauer": v.dauer, "fenster": v.fenster, "hinweise": v.hinweise, "formeln": v.formeln,
            "erwartung": [{"messgeraet": e.name, "wert": e.wert, "einheit": e.einheit, "toleranz": e.toleranz,
                           "quelle": e.quelle} for e in v.erwartung],
            "messgeraete": [m.__dict__ for m in v.bau.messstellen],
            "schaltung": v.text}, ensure_ascii=False, indent=1)
    elif args.js:
        ausgabe = "const circuit = `" + v.text + "`;\n"
    else:
        ausgabe = v.text
    if args.o:
        Path(args.o).write_text(ausgabe, encoding="utf-8")
        print(f"geschrieben: {args.o}")
    else:
        print(ausgabe, end="")
    print(f"# Erwartungswerte ({v.titel})", file=sys.stderr)
    for e in v.erwartung:
        print(f"#   {e.name:8} = {e.wert:.5g} {e.einheit}  ({e.quelle}, ±{e.toleranz * 100:g} %)", file=sys.stderr)
    for h in v.hinweise:
        print(f"# {h}", file=sys.stderr)
    return 0


def cmd_pruefen(args) -> int:
    text = Path(args.datei).read_text(encoding="utf-8")
    bericht = kern.pruefe(text, messgeraete=not args.ohne_messgeraete)
    print(kern.bericht_text(bericht))
    code = 0 if bericht.ok else 1
    if args.engine:
        try:
            erg = messe(text, falstad=args.falstad, dauer=args.dauer, fenster=args.fenster)
        except EngineFehler as e:
            print(f"Engine nicht verfügbar: {e}", file=sys.stderr)
            return 2
        print("\nEngine (Mittel über das Fenster):")
        sch = bericht.schaltung
        for el in sch.elemente:
            if el.typ in ("w", "g"):
                continue
            ev = erg["elemente"][el.index]
            zeile = f"  Zeile {el.nr:3} {el.typ:4} U_eff={ev['vrms']:10.4g} V  I_eff={ev['irms']:10.4g} A"
            if bericht.messung and el.typ in ("r", "c", "l", "v", "370", "p", "s", "i"):
                u_r, i_r = bericht.messung.u(el), bericht.messung.i(el)
                ab_u = abs(ev["vrms"] - u_r) > 0.02 * max(abs(u_r), 1e-3) + 1e-4
                ab_i = abs(ev["irms"] - i_r) > 0.02 * max(abs(i_r), 1e-6) + 1e-7
                zeile += f"   Rechnung U={u_r:.4g} I={i_r:.4g}" + ("  ⚠️ weicht ab" if ab_u or ab_i else "")
            print(zeile)
    return code


def cmd_engine(args) -> int:
    text = Path(args.datei).read_text(encoding="utf-8")
    try:
        erg = messe(text, falstad=args.falstad, dauer=args.dauer, fenster=args.fenster)
    except EngineFehler as e:
        print(f"Engine nicht verfügbar: {e}", file=sys.stderr)
        return 2
    sch = kern.lese(text)
    zeilen = {el.index: el for el in sch.elemente}
    print(f"t = {erg['t']:.4g} s, {erg['schritte']} Schritte im Mittelungsfenster")
    for ev in erg["elemente"]:
        el = zeilen.get(ev["k"])
        if el is None or el.typ in ("w", "g"):
            continue
        print(f"Zeile {el.nr:3} {el.typ:4} U: Mittel {ev['vm']:10.4g} eff {ev['vrms']:10.4g} max {ev['vmax']:10.4g} "
              f"| I: Mittel {ev['im']:10.4g} eff {ev['irms']:10.4g} max {ev['imax']:10.4g}")
    return 0


def cmd_vergleich(args) -> int:
    v = _erzeuge(args.name, args.rest)
    try:
        erg = messe(v.text, falstad=args.falstad, dauer=v.dauer, fenster=v.fenster)
    except EngineFehler as e:
        print(f"Engine nicht verfügbar: {e}", file=sys.stderr)
        return 2
    schlecht = 0
    for name, soll, ist, einheit, ok in vergleiche(v, erg):
        print(f"{'✅' if ok else '❌'} {name:8} Formel {soll:.5g} {einheit}   Engine {ist:.5g} {einheit}")
        schlecht += not ok
    return 1 if schlecht else 0


def cmd_url(args) -> int:
    text = Path(args.datei).read_text(encoding="utf-8")
    print(f"{args.basis.rstrip('/')}/falstad/circuitjs.html?cct={urllib.parse.quote(text.strip())}&{URL_PARAMETER}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="befehl", required=True)
    sub.add_parser("vorlagen").set_defaults(fn=cmd_vorlagen)
    s = sub.add_parser("vorlage", help="Vorlage erzeugen; Parameter als --name wert")
    s.add_argument("name")
    s.add_argument("-o")
    s.add_argument("--js", action="store_true")
    s.add_argument("--json", action="store_true")
    s.set_defaults(fn=cmd_vorlage)
    s = sub.add_parser("pruefen")
    s.add_argument("datei")
    s.add_argument("--ohne-messgeraete", action="store_true")
    s.add_argument("--engine", action="store_true")
    s.add_argument("--dauer", type=float, default=0.1)
    s.add_argument("--fenster", type=float, default=0.04)
    s.add_argument("--falstad")
    s.set_defaults(fn=cmd_pruefen)
    s = sub.add_parser("engine")
    s.add_argument("datei")
    s.add_argument("--dauer", type=float, default=0.1)
    s.add_argument("--fenster", type=float, default=0.04)
    s.add_argument("--falstad")
    s.set_defaults(fn=cmd_engine)
    s = sub.add_parser("vergleich", help="Vorlage: Formelwerte gegen Engine")
    s.add_argument("name")
    s.add_argument("--falstad")
    s.set_defaults(fn=cmd_vergleich)
    s = sub.add_parser("url")
    s.add_argument("datei")
    s.add_argument("--basis", default="http://localhost:8000")
    s.set_defaults(fn=cmd_url)
    args, rest = p.parse_known_args(argv)
    if args.befehl in ("vorlage", "vergleich"):
        args.rest = rest
    elif rest:
        p.error(f"Unbekannte Argumente: {rest}")
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
