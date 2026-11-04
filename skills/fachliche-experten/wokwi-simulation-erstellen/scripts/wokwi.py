#!/usr/bin/env python3
"""wokwi – Steuerungsaufgabe als Wokwi-Simulation umsetzen, prüfen und testen.

Befehle:
    python3 wokwi.py entwurf QUELLE.md [--plattform arduino-uno|esp32] [-o SPEC.yaml]
        Gerüst der Spec aus Zuordnungsliste und GRAFCET-Textform eines Materials (Lehrermaterial,
        Erwartungshorizont). Zwangssteuerung, Verknüpfungen und Testfälle ergänzt man danach.
    python3 wokwi.py pruefen SPEC.yaml
        Spec und erzeugte Schaltung prüfen (Kennzeichen, Pins, GRAFCET, Bedingungen, Testfälle).
    python3 wokwi.py erzeugen SPEC.yaml [-o ORDNER] [--ueberschreiben]
        sketch.ino, diagram.json, wokwi.toml und Szenarien schreiben (Standard: 48_wokwi_<kurztitel>/).
    python3 wokwi.py testen SPEC.yaml [--nur-logik] [--protokoll DATEI.md] [--zeitablauf DATEI.svg]
                                      [--test T1] [--serial]
        Testfälle im Logikmodell und im übersetzten Sketch (g++) ausführen.
    python3 wokwi.py blatt SPEC.yaml [-o DATEI.md] [--ueberschreiben]
        Begleitblatt mit Bedienung, Zuordnungsliste, Ablauf, Testergebnis, Qualitätscheck.
    python3 wokwi.py vorschau SPEC.yaml|diagram.json [--png DATEI.png]
        Bauteile mit @wokwi/elements in Chromium setzen: Pinnamen gegen die echten Bauteile prüfen,
        Bild zur Sichtprüfung (Chromium und Netz nötig).
    python3 wokwi.py wokwi ORDNER [--timeout MS]
        Szenarien mit wokwi-cli in Wokwi ausführen (wokwi-cli, WOKWI_CLI_TOKEN und gebaute Firmware nötig).
    python3 wokwi.py alles SPEC.yaml [--ueberschreiben]
        pruefen → erzeugen → testen → Zeitablauf (SVG) → Begleitblatt.

Exit-Code: 0 = ohne ❌, 1 = ❌ in Prüfung oder Testfall, 2 = Eingabefehler bzw. Werkzeug fehlt.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import wokwi_blatt as wb  # noqa: E402
import wokwi_projekt as wp  # noqa: E402
import wokwi_sim as sim  # noqa: E402
import wokwi_spec as ws  # noqa: E402
import wokwi_vorschau as wv  # noqa: E402


# ───────────────────────────── Pfade ─────────────────────────────

def _stamm(spec: ws.Spec) -> str:
    return f"48_wokwi_{spec.kurztitel}"


def _basis(spec: ws.Spec) -> Path:
    return spec.pfad.parent if spec.pfad else Path.cwd()


def standard_ordner(spec: ws.Spec) -> Path:
    return _basis(spec) / _stamm(spec)


def standard_blatt(spec: ws.Spec) -> Path:
    return _basis(spec) / f"{_stamm(spec)}_begleitblatt.md"


def standard_zeitablauf(spec: ws.Spec) -> Path:
    return _basis(spec) / "abbildungen" / f"{_stamm(spec)}_loesung_zeitablauf.svg"


def _lade(pfad: str) -> ws.Spec:
    try:
        return ws.lade(pfad)
    except ws.SpecFehler as e:
        print(f"❌ {e}")
        raise SystemExit(2)


# ───────────────────────────── entwurf ─────────────────────────────

def _tabellen(text: str) -> list[list[list[str]]]:
    tabellen, akt = [], []
    for zeile in text.splitlines():
        s = zeile.strip()
        if s.startswith("|") and s.endswith("|"):
            zellen = [c.strip() for c in s.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in zellen if c):
                akt.append(zellen)
        elif akt:
            tabellen.append(akt)
            akt = []
    if akt:
        tabellen.append(akt)
    return tabellen


_ANALOG = re.compile(r"%IW|%AI|^AI\d|^IA\d|^A\d$|GPIO3[2-9]|^GP2[6-8]|^PA[0-7]$")
_BEREICH = re.compile(r"für\s*([−-]?\d+(?:[.,]\d+)?)\s*…\s*([−-]?\d+(?:[.,]\d+)?)\s*([^\s);]+)")
_PIN = re.compile(r"^(?:D\d{1,2}|A[0-5]|GPIO\d{1,2})$")


def entwurf(text: str, plattform: str, quelle: str = "") -> str:
    """Spec-Gerüst (YAML-Text) aus Zuordnungsliste und GRAFCET-Textform eines Markdown-Materials."""
    pf = ws.PLATTFORMEN[plattform]
    tabellen = _tabellen(text)
    zuord = [t for t in tabellen if t and t[0] and t[0][0].upper() in ("BMK", "KENNZEICHEN")]
    zuord = max(zuord, key=len, default=None)
    grafcet = next((t for t in tabellen if t and t[0][0].lower().startswith("schritt")
                    and any("transition" in c.lower() for c in t[0])), None)
    if not zuord:
        raise ws.SpecFehler("keine Zuordnungsliste (Tabelle mit Spalte „BMK“) gefunden")
    kopf = [c.lower() for c in zuord[0]]

    def spalte(*namen):
        return next((i for i, c in enumerate(kopf) if any(n in c for n in namen)), None)

    i_name, i_sig, i_kon = spalte("betriebsmittel"), spalte("signal 1"), spalte("kontakt")
    i_pin, i_ops = spalte("pin"), [i for i, c in enumerate(kopf) if "operand" in c or "pin" in c]
    frei = {"di": list(pf["eap_di"]), "do": list(pf["eap_do"]), "ai": list(pf["eap_ai"])}
    ein, ana, aus, hinweise = [], [], [], []
    for zeile in zuord[1:]:
        if not zeile or not re.fullmatch(r"-[A-Z]{1,3}\d+", zeile[0]):
            continue
        bmk = zeile[0]
        zelle = lambda i: zeile[i].strip() if i is not None and i < len(zeile) else ""  # noqa: E731
        name = zelle(i_name)
        ops = " ".join(zelle(i) for i in i_ops)
        kontakt = zelle(i_kon).upper()
        pin = zelle(i_pin) if _PIN.match(zelle(i_pin)) else ""
        analog = bool(_ANALOG.search(ops.split()[0] if ops.split() else "")) or "mA" in name or " V für" in name
        art = "ai" if analog else ("di" if kontakt in ("NO", "NC") or bmk[1] in "SB" else "do")
        if not pin:
            if not frei[art]:
                hinweise.append(f"{bmk}: kein freier Pin der E/A-Platine – Pin von Hand eintragen")
                pin = "TODO"
            else:
                pin = frei[art].pop(0)
        elif pin in frei[art]:
            frei[art].remove(pin)
        if art == "ai":
            m = _BEREICH.search(name)
            lo, hi, einheit = (m.group(1), m.group(2), m.group(3)) if m else ("0", "100", "TODO")
            name_kurz = re.sub(r"\s*\(.*\)", "", name)
            ana.append(f'  - {{bmk: {bmk}, name: "{name_kurz}", pin: {pin}, signal: "4 … 20 mA", '
                       f'bereich: [{ws.zahl(lo):g}, {ws.zahl(hi):g}], einheit: "{einheit}", '
                       f'start: {(ws.zahl(lo) + ws.zahl(hi)) / 2:g}}}  # TODO Startwert (Bereichsmitte)')
        elif art == "di":
            k = kontakt if kontakt in ("NO", "NC") else "NO"
            bauteil = "taster" if bmk.startswith("-S") and "schalter" not in name.lower() else "schalter"
            ein.append(f'  - {{bmk: {bmk}, name: "{name}", pin: {pin}, kontakt: "{k}", bauteil: {bauteil}, '
                       f'signal_1: "{zelle(i_sig)}"}}' + ("" if kontakt in ("NO", "NC") else "  # TODO Kontaktart"))
        else:
            aus.append(f'  - {{bmk: {bmk}, name: "{name}", pin: {pin}, signal_1: "{zelle(i_sig)}"}}')

    z = ["# Spec-Gerüst – erzeugt mit wokwi.py entwurf; TODO-Stellen ergänzen, dann: wokwi.py alles <Datei>",
         "# Format: references/spec-format.md", "",
         'titel: "TODO Titel der Steuerung"', "kurztitel: TODO-kurztitel",
         f'quelle: "{quelle}"', f"plattform: {plattform}",
         "zeitraffer: {faktor: 60, ab: 1min}   # bei Zeiten über einigen Minuten; sonst faktor: 1", ""]
    z += ["eingaenge:", *ein, "analogeingaenge:", *(ana or ["  []"]), "ausgaenge:", *aus, ""]
    merker = set()
    if grafcet:
        z.append("grafcet:")
        for zeile in grafcet[1:]:
            if not zeile or not zeile[0]:
                continue
            m = re.match(r"X?(\d+)\s*(.*)$", zeile[0])
            if not m:
                continue
            nr, rest = m.group(1), m.group(2).strip()
            name = "Grundstellung" if "initial" in rest.lower() else re.sub(r"[()]", "", rest).strip() or f"Schritt {nr}"
            akt_roh = zeile[1] if len(zeile) > 1 else ""
            akt = [] if akt_roh.strip() in ("", "–", "-") else [x.strip() for x in akt_roh.split(",")]
            merker |= {x for x in akt if re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", x)}
            trans = zeile[2] if len(zeile) > 2 else ""
            trans = re.sub(r"→\s*X(\d+)", r"→ \1", trans)
            akt_yaml = "[" + ", ".join(f'"{x}"' if any(c in x for c in "↑↓:") else x for x in akt) + "]"
            z.append(f'  - {{schritt: {nr}, name: "{name}", aktionen: {akt_yaml}, transition: "{trans}"}}')
    else:
        z += ["grafcet:   # TODO keine GRAFCET-Textform gefunden (Tabelle Schritt | Aktion | Transition)", "  []"]
        hinweise.append("GRAFCET-Textform fehlt – Schritte von Hand eintragen")
    z += ["", "merker:" + ("" if merker else "  []")]
    z += [f'  - {{name: {m}, text: "TODO"}}' for m in sorted(merker)]
    z += ["", "# TODO Stopp und Schutzfunktionen der Funktionsbeschreibung (Schrittkette in die Grundstellung)",
          "erzwingen: []", "",
          "# TODO Verknüpfungen nach der Schrittkette (Logikplan), z. B. Freigabe eines Aktors über einen Merker",
          "zuweisungen: []", "",
          "annahmen: []", "pruefauftraege: []", "",
          "# TODO Testfälle aus der Funktionsbeschreibung: Normalablauf, jede Zeit, jede Verzweigung, Stopp,",
          "# jede Schutzfunktion, Startsperren (references/spec-format.md Abschn. 6)",
          "testfaelle: []"]
    for h in hinweise:
        z.insert(3, f"# ⚠️ {h}")
    return "\n".join(z) + "\n"


# ───────────────────────────── Befehle ─────────────────────────────

def _befunde_ausgeben(befunde: list[ws.Befund], titel: str) -> int:
    fehler = [b for b in befunde if b.stufe == "❌"]
    for b in befunde:
        print(f"  {b}")
    print(f"{titel}: " + ("OK" if not fehler else f"{len(fehler)} Fehler")
          + (f", {len(befunde) - len(fehler)} Hinweise" if len(befunde) > len(fehler) else ""))
    return 1 if fehler else 0


def befehl_pruefen(spec: ws.Spec) -> int:
    rc = _befunde_ausgeben(ws.pruefe(spec), "Spec")
    rc |= _befunde_ausgeben(wp.pruefe_diagramm(spec, wp.diagramm(spec)), "Schaltung")
    return rc


def projekt_dateien(spec: ws.Spec, logik: list[sim.Ergebnis]) -> tuple[dict[str, str], dict[str, str]]:
    """Dateien des Wokwi-Projekts und Testfall → Szenariodatei."""
    name = spec.pfad.name if spec.pfad else ""
    dateien = {"sketch.ino": wp.sketch(spec, name),
               "diagram.json": json.dumps(wp.diagramm(spec), indent=2, ensure_ascii=False) + "\n",
               "wokwi.toml": wp.wokwi_toml(spec)}
    szen = {}
    for erg in logik:
        s = sim.szenario(spec, erg)
        if s:
            dateien[s[0]] = s[1]
            szen[erg.test.nr] = s[0]
    return dateien, szen


def befehl_erzeugen(spec: ws.Spec, ordner: Path | None, ueberschreiben: bool) -> tuple[int, dict]:
    if any(b.stufe == "❌" for b in ws.pruefe(spec)):
        print("erzeugen: Spec hat Fehler – erst `wokwi.py pruefen`")
        return 1, {}
    logik = [sim.fuehre_aus(spec, t, sim.Logikmodell(spec)) for t in spec.testfaelle]
    dateien, szen = projekt_dateien(spec, logik)
    ordner = ordner or standard_ordner(spec)
    try:
        for m in wp.schreibe(ordner, dateien, ueberschreiben):
            print(f"  {m}")
    except ValueError as e:
        print(f"❌ {e}")
        return 2, {}
    print(f"erzeugen: {ordner} ({len(dateien)} Dateien, {len(szen)} Szenarien)")
    return 0, szen


def befehl_testen(spec: ws.Spec, nur_logik: bool, protokoll: Path | None, zeitablauf: Path | None,
                  test: str | None, serial: bool) -> tuple[int, dict, tuple | None]:
    aus = sim.teste_alle(spec, nur_logik=nur_logik)
    _, szen = projekt_dateien(spec, aus["logik"])
    text = sim.protokoll(spec, aus, szen)
    print(text)
    print(f"Programm: {aus['programm_status']}")
    for w in aus["warnungen"]:
        print(f"  ⚠️ {w}")
    if protokoll:
        protokoll.write_text(text, encoding="utf-8")
        print(f"Protokoll: {protokoll}")
    if serial and aus["programm"]:
        erg = next((e for e in aus["programm"] if e.test.nr == (test or e.test.nr)), None)
        print(f"── Serieller Monitor {erg.test.nr} ──")
        print(erg.serial)
    bild = None
    if zeitablauf:
        quelle = aus["programm"] or aus["logik"]
        erg = next((e for e in quelle if e.test.nr == test), quelle[0] if quelle else None)
        if erg is None:
            print("Zeitablauf: kein Testfall")
        else:
            try:
                ab = sim.zeitablauf_svg(spec, erg, zeitablauf)
                bild = (zeitablauf, sim.wertetabelle(spec, ab), erg.test.nr)
                print(f"Zeitablauf: {zeitablauf} ({erg.test.nr}, {len(ab)} Abschnitte, {erg.art})")
            except sim.SimFehler as e:
                print(f"⚠️ {e}")
    ok = all(e.ok for e in aus["logik"]) and all(e.ok for e in aus["programm"])
    return (0 if ok else 1), aus, bild


def befehl_blatt(spec: ws.Spec, ziel: Path | None, ueberschreiben: bool, aus: dict | None = None,
                 bild: tuple | None = None) -> int:
    ziel = ziel or standard_blatt(spec)
    if ziel.exists() and not ueberschreiben:
        print(f"❌ {ziel} besteht – nicht überschrieben (Suffix _v2 wählen oder --ueberschreiben)")
        return 2
    if aus is None:
        aus = sim.teste_alle(spec)
    _, szen = projekt_dateien(spec, aus["logik"])
    bild_rel = tabelle = bild_test = None
    if bild is None and standard_zeitablauf(spec).exists():
        bild = (standard_zeitablauf(spec), None, spec.testfaelle[0].nr if spec.testfaelle else "")
    if bild:
        try:
            bild_rel = Path(os.path.relpath(bild[0], ziel.parent)).as_posix()
        except ValueError:
            bild_rel = str(bild[0])
        tabelle, bild_test = bild[1], bild[2]
    text = wb.begleitblatt(spec, ws.pruefe(spec), wp.pruefe_diagramm(spec, wp.diagramm(spec)), aus, szen,
                           standard_ordner(spec).name, spec.pfad.name if spec.pfad else "spec.yaml",
                           bild_rel, tabelle, bild_test)
    ziel.write_text(text, encoding="utf-8")
    print(f"blatt: {ziel}")
    return 0


def befehl_wokwi(ordner: Path, timeout: int | None) -> int:
    cli = shutil.which("wokwi-cli")
    if not cli:
        print("wokwi-cli nicht gefunden – Szenarien nicht in Wokwi ausgeführt "
              "(Installation: docs.wokwi.com, Abschnitt Wokwi CI)")
        return 2
    if not os.environ.get("WOKWI_CLI_TOKEN"):
        print("WOKWI_CLI_TOKEN fehlt – Token im Wokwi-Konto anlegen (Wokwi CI)")
        return 2
    toml = (ordner / "wokwi.toml").read_text(encoding="utf-8") if (ordner / "wokwi.toml").exists() else ""
    m = re.search(r"^firmware\s*=\s*'([^']+)'", toml, re.M)
    if not m or not (ordner / m.group(1)).exists():
        print("Firmware fehlt – erst bauen (Kommentar in wokwi.toml), dann erneut aufrufen")
        return 2
    rc = 0
    for szen in sorted((ordner / "szenarien").glob("*.test.yaml")):
        dauer = sum(int(x) for x in re.findall(r"delay: (\d+)ms", szen.read_text(encoding="utf-8")))
        grenze = timeout or dauer + 30_000
        r = subprocess.run([cli, str(ordner), "--scenario", str(szen.relative_to(ordner)), "--timeout", str(grenze)],
                           capture_output=True, text=True)
        print(f"  {'✅' if r.returncode == 0 else '❌'} {szen.name}")
        if r.returncode:
            print((r.stdout + r.stderr)[-1500:])
            rc = 1
    return rc


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Steuerungsaufgabe als Wokwi-Simulation umsetzen, prüfen und testen.")
    u = p.add_subparsers(dest="befehl", required=True)
    e = u.add_parser("entwurf")
    e.add_argument("quelle")
    e.add_argument("--plattform", default="arduino-uno", choices=sorted(ws.PLATTFORMEN))
    e.add_argument("-o", "--ausgabe")
    for name in ("pruefen", "erzeugen", "testen", "blatt", "alles"):
        x = u.add_parser(name)
        x.add_argument("spec")
        if name in ("erzeugen", "blatt"):
            x.add_argument("-o", "--ausgabe")
        if name in ("erzeugen", "blatt", "alles"):
            x.add_argument("--ueberschreiben", action="store_true")
        if name == "testen":
            x.add_argument("--nur-logik", action="store_true")
            x.add_argument("--protokoll")
            x.add_argument("--zeitablauf")
            x.add_argument("--test")
            x.add_argument("--serial", action="store_true")
    v = u.add_parser("vorschau")
    v.add_argument("quelle")
    v.add_argument("--png")
    w = u.add_parser("wokwi")
    w.add_argument("ordner")
    w.add_argument("--timeout", type=int)
    a = p.parse_args(argv)

    if a.befehl == "entwurf":
        quelle = Path(a.quelle)
        if not quelle.is_file():
            print(f"❌ {quelle} nicht gefunden")
            return 2
        try:
            text = entwurf(quelle.read_text(encoding="utf-8"), a.plattform, quelle.name)
        except ws.SpecFehler as err:
            print(f"❌ {err}")
            return 2
        if a.ausgabe:
            ziel = Path(a.ausgabe)
            if ziel.exists():
                print(f"❌ {ziel} besteht – nicht überschrieben")
                return 2
            ziel.write_text(text, encoding="utf-8")
            print(f"entwurf: {ziel}")
        else:
            print(text)
        return 0
    if a.befehl == "wokwi":
        return befehl_wokwi(Path(a.ordner), a.timeout)
    if a.befehl == "vorschau":
        if a.quelle.endswith(".json"):
            diagramm = json.loads(Path(a.quelle).read_text(encoding="utf-8"))
        else:
            diagramm = wp.diagramm(_lade(a.quelle))
        rc, meldung = wv.vorschau(diagramm, Path(a.png) if a.png else None)
        print(f"vorschau: {'OK – alle Pins vorhanden, Leitungen rechtwinklig' if rc == 0 else meldung}"
              + (f"; Bild: {a.png}" if a.png and rc != 2 else ""))
        return rc

    spec = _lade(a.spec)
    if a.befehl == "pruefen":
        return befehl_pruefen(spec)
    if a.befehl == "erzeugen":
        return befehl_erzeugen(spec, Path(a.ausgabe) if a.ausgabe else None, a.ueberschreiben)[0]
    if a.befehl == "testen":
        return befehl_testen(spec, a.nur_logik, Path(a.protokoll) if a.protokoll else None,
                             Path(a.zeitablauf) if a.zeitablauf else None, a.test, a.serial)[0]
    if a.befehl == "blatt":
        return befehl_blatt(spec, Path(a.ausgabe) if a.ausgabe else None, a.ueberschreiben)

    # alles
    rc = befehl_pruefen(spec)
    if rc:
        return rc
    rc_e, _ = befehl_erzeugen(spec, None, a.ueberschreiben)
    if rc_e:
        return rc_e
    rc_t, aus, bild = befehl_testen(spec, False, None, standard_zeitablauf(spec), None, False)
    blatt = standard_blatt(spec)
    if blatt.exists() and not a.ueberschreiben:
        print(f"blatt: {blatt} besteht – nicht überschrieben (--ueberschreiben oder `blatt -o …_v2.md`)")
    else:
        befehl_blatt(spec, blatt, True, aus, bild)
    return rc_t


if __name__ == "__main__":
    sys.exit(main())
