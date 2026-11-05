#!/usr/bin/env python3
"""wokwi_blatt – Begleitblatt (Artefakt 48) aus Spec, Prüfung und Testlauf schreiben.

Aufbau wie assets/vorlage-simulationsblatt.md: Kopf, Aufgabe und Umfang, Projekt, In Wokwi öffnen,
Bedienung, Zuordnungsliste, Ablauf, Zeitraffer, Testfälle, Zeitablauf, Einsatz, Qualitätscheck,
Annahmen und Prüfaufträge, Übergabe, Transparenzzeile. Annahmen und Prüfaufträge der Spec werden
übernommen, die festen Annahmen der Simulation ergänzt.
"""

from __future__ import annotations

from datetime import date

import wokwi_projekt as wp
import wokwi_spec as ws


def _kopf(spec: ws.Spec) -> list[str]:
    r = spec.roh
    z = ["---", "artefakt: Mikrocontroller-Simulation (Wokwi)", f'titel: "{spec.titel}"',
         f"skill: {wp.SKILL}", f'skill_version: "{wp.VERSION}"', f"stand: {date.today().isoformat()}",
         f'bildungsgang: "{r.get("bildungsgang", "<Bildungsgang>")}"',
         f'curriculare_vorgabe: "{r.get("curriculare_vorgabe", "<Lernfeld bzw. Lerngebiet>")}"',
         f"dqr: {r.get('dqr', '<3|4|5>')}", f'status: "{r.get("status", "KI-Entwurf – fachlich zu prüfen")}"',
         "bereich: planung"]
    if r.get("vertraulich"):
        z.append("vertraulich: true")
    return z + ["---", ""]


_FARBEN = {"green": "grün", "black": "schwarz", "red": "rot", "orange": "orange", "white": "weiß", "blue": "blau",
           "yellow": "gelb"}


def _farbe(f: str) -> str:
    return _FARBEN.get(f, f)


def _bauteil(spec: ws.Spec, x) -> tuple[str, str]:
    pf = spec.p
    if isinstance(x, ws.Eingang):
        if x.bauteil == "schalter":
            return (f"Schiebeschalter an {x.pin}", "rechts = 1, links = 0")
        farbe = _farbe(wp.farbe_taster(x))
        if x.kontakt == "NO":
            return (f"Taster ({farbe}) an {x.pin}, gegen {pf['vcc']}, 10 kΩ nach GND", "drücken = 1")
        return (f"Taster ({farbe}) an {x.pin}, gegen GND, 10 kΩ nach {pf['vcc']}", "unbetätigt = 1, drücken = 0")
    if isinstance(x, ws.Analog):
        return (f"Drehpotentiometer an {x.pin}",
                f"drehen: {x.bereich[0]:g} … {x.bereich[1]:g} {x.einheit}; links vom Messbereich unter 4 mA")
    return (f"LED ({_farbe(wp.farbe_led(x))}) an {x.pin} mit 220 Ω", "leuchtet bei 1")


def _ablauf(spec: ws.Spec) -> list[str]:
    z = ["**GRAFCET in Textform** (Notationsblatt Abschn. 5):", "",
         "| Schritt | Aktion | Transition zum Folgeschritt |", "|---|---|---|"]
    for s in spec.schritte:
        name = f"{s.nr} (Initialschritt)" if s.nr == spec.initial else f"{s.nr} {s.name}"
        akt = ", ".join(a.text for a in s.aktionen) or "–"
        tr = "; ".join(f"{t.text} → {t.ziel}" for t in s.transitionen) or "–"
        z.append(f"| {name} | {akt} | {tr} |")
    if spec.erzwingen:
        z += ["", "**Zwangssteuerung** (vor den Transitionen; solange die Bedingung gilt, steht die Schrittkette "
              "im genannten Schritt, Aktionen dieses Schritts):", "",
              "| Bedingung | Schritt | Zweck |", "|---|---|---|"]
        z += [f"| {e.text} | X{e.nach} | {e.grund or '–'} |" for e in spec.erzwingen]
    sr = [m for m in spec.merker if m.setzen or m.ruecksetzen]
    if sr:
        z += ["", "**Speicher** (RS rücksetzdominant, wenn nicht anders angegeben):", "",
              "| Merker | setzen | rücksetzen | Bedeutung |", "|---|---|---|---|"]
        z += [f"| `{m.name}` | {m.setzen_text or '–'} | {m.ruecksetzen_text or '–'} | {m.text or '–'} |" for m in sr]
    if spec.zuweisungen:
        z += ["", "**Verknüpfungen** (Logikplan, nach der Schrittkette):", "",
              "| Ausgang bzw. Merker | Bedingung | Zweck |", "|---|---|---|"]
        z += [f"| {v.ziel} | {v.text} | {v.grund or '–'} |" for v in spec.zuweisungen]
    return z


def _einsatz_standard(spec: ws.Spec) -> list[str]:
    return [
        "Musterlösung prüfen: GRAFCET und Logikplan laufen lassen, Testfälle als Prüfliste nachvollziehen.",
        "Inbetriebnahme üben: Lernende prüfen ihre Lösung gegen die Simulation (Schrittfolge, Zeiten, "
        "Schutzfunktionen) und begründen Abweichungen.",
        "Fehlersuche: In einer Kopie der Spec einen Fehler einbauen (z. B. Öffner nicht negiert, Zeit auf den "
        "falschen Schritt bezogen), neu erzeugen; Lernende finden ihn über den seriellen Monitor.",
    ]


def begleitblatt(spec: ws.Spec, befunde: list[ws.Befund], diagramm_befunde: list[ws.Befund], aus: dict,
                 szenarien: dict[str, str], ordner_name: str, spec_name: str, bild: str | None,
                 bild_tabelle: str | None, bild_test: str | None) -> str:
    pf = spec.p
    zr = spec.zeitraffer
    z = _kopf(spec)
    a = z.append
    a(f"# Wokwi-Simulation: {spec.titel}")
    a("")

    # Aufgabe und Umfang
    a("## Aufgabe und Umfang")
    if spec.quelle:
        a(f"- **Aufgabe:** {spec.quelle}")
    teile = [f"Zuordnungsliste ({len(spec.eingaenge) + len(spec.analog)} Eingänge, {len(spec.ausgaenge)} Ausgänge)",
             f"GRAFCET mit {len(spec.schritte)} Schritten"]
    if spec.erzwingen:
        teile.append("Zwangssteuerung (" + ", ".join(e.grund or e.text for e in spec.erzwingen) + ")")
    if spec.zuweisungen:
        teile.append("Verknüpfungen (" + ", ".join(v.ziel for v in spec.zuweisungen) + ")")
    a("- **Simuliert:** " + "; ".join(teile) + ".")
    a(f"- **Plattform:** {pf['name']} auf der E/A-Platine (Signal 1 = High-Pegel am Pin); Aktoren als LEDs, "
      "Analoggeber als Potentiometer.")
    a("- **Nicht simuliert:** Not-Halt und Schutzeinrichtungen (hardwaremäßig), Lastkreise, Motoren und "
      "Ventile selbst, Prellen der Kontakte (in der Schaltung abgeschaltet).")
    a(f"- **Zeit:** {zr.text()}.")
    a("")

    # Projekt
    a("## Projekt")
    a("| Datei | Inhalt |")
    a("|---|---|")
    a(f"| `{spec_name}` | Spec – Quelle aller Dateien; Änderungen hier, dann `wokwi.py alles` |")
    a(f"| `{ordner_name}/sketch.ino` | Programm: Zustandsautomat nach Notationsblatt (PIN_SJ1, sj1, millis()) |")
    a(f"| `{ordner_name}/diagram.json` | Schaltung: {pf['name']}, Taster, Schalter, Potentiometer, LEDs |")
    a(f"| `{ordner_name}/wokwi.toml` | für Wokwi in VS Code und wokwi-cli (Firmware vorher bauen) |")
    if szenarien:
        a(f"| `{ordner_name}/szenarien/` | {len(szenarien)} Testläufe für wokwi-cli (aus den Testfällen) |")
    a("")

    # In Wokwi öffnen
    a("## In Wokwi öffnen")
    a(f"1. {pf['wokwi_neu']} im Browser öffnen.")
    a("2. Den Inhalt von `sketch.ino` in den Reiter *sketch.ino* kopieren, den Inhalt von `diagram.json` in den "
      "Reiter *diagram.json* (jeweils alles ersetzen).")
    a("3. Simulation starten (▶). Der serielle Monitor zeigt bei jeder Änderung Schritt, Signale, Analogwerte "
      "und Merker.")
    a("")
    a("Speichern und Teilen eines Projekts braucht ein Wokwi-Konto. **Wokwi in VS Code bzw. wokwi-cli:** "
      f"`sketch.ino` nach `build/sketch/` kopieren, `arduino-cli compile --fqbn {pf['fqbn']} --output-dir build "
      "build/sketch`, dann die Simulation über `wokwi.toml` starten; die Szenarien laufen mit "
      "`python3 scripts/wokwi.py wokwi <Ordner>` (wokwi-cli und `WOKWI_CLI_TOKEN` nötig).")
    a("")

    # Bedienung
    a("## Bedienung in der Simulation")
    a("| Kennzeichen | Betriebsmittel | Bauteil in Wokwi | Bedienung | Signal 1 bedeutet |")
    a("|---|---|---|---|---|")
    for x in (*spec.eingaenge, *spec.analog, *spec.ausgaenge):
        teil, bed = _bauteil(spec, x)
        a(f"| {x.bmk} | {x.name} | {teil} | {bed} | {getattr(x, 'signal_1', '') or '–'} |")
    a("")

    # Zuordnungsliste
    a(f"## Zuordnungsliste ({pf['name']})")
    a("| BMK | Betriebsmittel | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |")
    a("|---|---|---|---|---|")
    for e in spec.eingaenge:
        a(f"| {e.bmk} | {e.name} | {e.pin} | {e.signal_1} | {e.kontakt} |")
    for o in spec.ausgaenge:
        a(f"| {o.bmk} | {o.name} | {o.pin} | {o.signal_1} | – |")
    for an in spec.analog:
        a(f"| {an.bmk} | {an.name} ({an.signal} für {an.bereich[0]:g} … {an.bereich[1]:g} {an.einheit}) | "
          f"{an.pin} | – | – |")
    a("")
    a(f"Analogwerte: {pf['adc_text']}; das Programm rechnet in die physikalische Größe um (Funktion "
      "`analogwert`).")
    a("")

    # Ablauf
    a("## Ablauf im Programm")
    z.extend(_ablauf(spec))
    a("")
    a("Zyklus je Durchlauf von `loop()`: Eingänge lesen → Speicher → Zwangssteuerung → Transitionen "
      "(höchstens ein Schrittwechsel) → Aktionen → Verknüpfungen → Ausgänge schreiben.")
    a("")

    # Zeitraffer
    zeiten = sorted({ms for _, ms in spec.zeiten()})
    if zeiten:
        a("## Zeiten in der Simulation")
        a("| Zeit in der Aufgabe | in der Simulation |")
        a("|---|---|")
        for ms in zeiten:
            a(f"| {ws.dauer_text(ms)} | {ws.dauer_text(zr(ms))} |")
        a("")
        if zr.faktor > 1:
            a("An der Anlage `ZEITRAFFER = 1` setzen; die Zeitkonstanten (`T_X1` …) bleiben in Aufgabenzeit "
              "geschrieben.")
            a("")

    # Testfälle
    a("## Testfälle und Ergebnis")
    a("Die Testfälle stammen aus der Funktionsbeschreibung. Jeder läuft zweimal: im Logikmodell der Spec und "
      "im übersetzten Sketch (g++ mit nachgebildetem Arduino-Kern, `loop()` je Millisekunde). Zeitschwellen werden "
      "100 ms vor und nach der Schwelle geprüft.")
    a("")
    z.append(_protokoll_mit_pfaden(spec, aus, szenarien, ordner_name).rstrip())
    a("")
    for t in spec.testfaelle:
        if t.zweck:
            a(f"- **{t.nr}** {t.zweck}")
    a("")

    # Zeitablauf
    if bild:
        a("## Zeitablauf")
        a(f"![Zustandsfolge der Simulation im Testfall {bild_test}]({bild})")
        a("")
        a(f"*Zustandsfolge des Sketches im Testfall {bild_test} (Werte aus dem g++-Lauf): ein Feld je Abschnitt "
          "zwischen zwei Änderungen; dunkel = Signal 1; darunter Beginn und Dauer in Simulationszeit.*")
        a("")
        if bild_tabelle:
            z.append(bild_tabelle.rstrip())
            a("")

    # Einsatz
    a("## Einsatz im Unterricht")
    for e in [str(x) for x in spec.roh.get("einsatz") or []] or _einsatz_standard(spec):
        a(f"- {e}")
    a("")

    # Qualitätscheck
    fehler = [b for b in befunde if b.stufe == "❌"]
    warn = [b for b in befunde if b.stufe != "❌"]
    dfehler = [b for b in diagramm_befunde if b.stufe == "❌"]
    logik_ok = all(e.ok for e in aus["logik"])
    n_l = sum(len(e.punkte) for e in aus["logik"])
    ok_l = sum(e.bestanden for e in aus["logik"])
    n_p = sum(len(e.punkte) for e in aus["programm"])
    ok_p = sum(e.bestanden for e in aus["programm"])
    prog_ok = bool(aus["programm"]) and all(e.ok for e in aus["programm"])

    def zeichen(ok, mittel=False):
        return "✅" if ok else ("⚠️" if mittel else "❌")

    a("## Qualitätscheck")
    a("| Kriterium | Ergebnis | Hinweis |")
    a("|---|---|---|")
    a(f"| Spec geprüft (`wokwi.py pruefen`) | {zeichen(not fehler, False)} | "
      f"{len(fehler)} Fehler, {len(warn)} Hinweise" + (": " + "; ".join(b.text for b in warn) if warn else "") + " |")
    a(f"| Schaltung: Bauteile, Pins, Netze (`diagram.json`) | {zeichen(not dfehler)} | "
      f"{'; '.join(b.text for b in diagramm_befunde) or 'ohne Befund'} |")
    a(f"| Sketch übersetzt | {zeichen(bool(aus['programm']), True)} | {aus['programm_status']} |")
    a(f"| Testfälle im Logikmodell | {zeichen(logik_ok)} | {ok_l}/{n_l} Prüfpunkte |")
    a(f"| Testfälle im Programm | {zeichen(prog_ok, not aus['programm'])} | "
      + (f"{ok_p}/{n_p} Prüfpunkte" if aus["programm"] else "nicht ausgeführt") + " |")
    entfallen = [e.test.nr for e in aus["logik"] if e.test.nr not in szenarien]
    a(f"| Wokwi-Szenarien | ⚠️ | {len(szenarien)} von {len(spec.testfaelle)} erzeugt"
      + (f" (entfallen: {', '.join(entfallen)})" if entfallen else "")
      + "; in Wokwi nur mit wokwi-cli und Token ausführbar |")
    a("| Lauf im Browser | ⚠️ | einmal in Wokwi starten und Testfall T1 nachvollziehen |")
    a("| Bedienteile nach DIN EN 60204-1 (Start nicht rot, Stopp nicht grün) | ✅ | Farben in `diagram.json` |")
    a("| Zeichnungen als SVG aus Werten bzw. Spec, keine Zeichnung aus Zeichen | ✅ | "
      + ("Zeitablauf aus den Simulationswerten (matplotlib)" if bild else "keine Abbildung") + " |")
    a("")

    # Annahmen
    a("## Annahmen und Prüfaufträge")
    for x in spec.annahmen:
        a(f"- ⚠️ Annahme: {x}")
    if zr.faktor > 1:
        a(f"- ⚠️ Annahme: {zr.text()} – nur für die Simulation.")
    a("- ⚠️ Annahme: Aktoren (Schütze, Ventile) und Leuchtmelder als LEDs; Geber ohne Prellen, Analoggeber als "
      "Potentiometer am Analogeingang (Bürde und Schutzbeschaltung der E/A-Platine nicht nachgebildet).")
    for x in spec.pruefauftraege:
        a(f"- 🔎 Prüfen: {x}")
    if not aus["programm"]:
        a(f"- 🔎 Prüfen: Programm nicht getestet ({aus['programm_status']}) – in Wokwi nachvollziehen.")
    a("- 🔎 Prüfen: Lauf in Wokwi (Browser oder wokwi-cli) – hier nur mit nachgebildetem Arduino-Kern getestet.")
    if spec.analog:
        a(f"- 🔎 Prüfen: Rohwertbereich {pf['rohbereich'][0]} … {pf['rohbereich'][1]} mit der Anlage der Ein- und "
          "Ausgänge bzw. der realen E/A-Platine abgleichen.")
    a("")

    # Übergabe
    a("## Übergabe")
    a(f"- Projektordner `{ordner_name}/` (sketch.ino, diagram.json, wokwi.toml, Szenarien), Spec `{spec_name}`")
    a(f"- Plattform {pf['name']}, Zuordnungsliste und GRAFCET-Textform wie oben; Testfälle "
      + ", ".join(t.nr for t in spec.testfaelle))
    a("- Empfohlene nächste Skills: `programmieraufgabe-erstellen` (Programmierauftrag zur Steuerung), "
      "`unterrichtsmaterial-erstellen` (Arbeitsblatt zur Inbetriebnahme), `technologieschema-erstellen` "
      "(GRAFCET und Logikplan als SVG), `material-pruefen`")
    a("")
    a(f"> KI-gestützt erstellt (Skill {wp.SKILL} v{wp.VERSION}). Fachliche Prüfung und Verantwortung: Lehrkraft.")
    return "\n".join(z) + "\n"


def _protokoll_mit_pfaden(spec, aus, szenarien, ordner_name):
    import wokwi_sim as sim
    return sim.protokoll(spec, aus, {k: f"{ordner_name}/{v}" for k, v in szenarien.items()})
