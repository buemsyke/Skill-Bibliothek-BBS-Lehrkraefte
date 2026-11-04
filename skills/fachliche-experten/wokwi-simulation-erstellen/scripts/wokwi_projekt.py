#!/usr/bin/env python3
"""wokwi_projekt – Wokwi-Projekt aus der Spec erzeugen: sketch.ino, diagram.json, wokwi.toml, Szenarien.

Der Sketch folgt dem Notationsblatt (Abschn. 6): Pin-Konstante PIN_S1, Signal s1, GRAFCET als
Zustandsautomat mit einer Variablen für den aktiven Schritt, Zeiten über millis() seit Schrittbeginn,
Zyklus wie bei der SPS (Eingänge lesen → Speicher → Erzwingen → Transitionen → Aktionen →
Verknüpfungen → Ausgänge schreiben). Die Schaltung bildet die E/A-Platine nach: Signal 1 = High-Pegel.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import wokwi_spec as ws

SKILL = "wokwi-simulation-erstellen"
VERSION = "1.0"
MANIFEST = ".wokwi-erzeugt.json"
MELDEN_MS = 5000

_CPP_OP = {"≥": ">=", "≤": "<=", "=": "==", "≠": "!=", "<": "<", ">": ">"}


# ───────────────────────────── Bedingungen → C++ ─────────────────────────────

def _zahl_cpp(v: float) -> str:
    s = f"{v:.6g}"
    return s if any(c in s for c in ".e") else s + ".0"


def zeitnamen(spec: ws.Spec) -> dict[tuple[int, int], str]:
    """(Schritt, ms) → Name der Zeitkonstante: T_X1, bei mehreren Zeiten eines Schritts T_X3_2 …"""
    namen: dict[tuple[int, int], str] = {}
    zaehler: dict[int, int] = {}
    for schritt, ms in spec.zeiten():
        zaehler[schritt] = zaehler.get(schritt, 0) + 1
        namen[(schritt, ms)] = f"T_X{schritt}" if zaehler[schritt] == 1 else f"T_X{schritt}_{zaehler[schritt]}"
    return namen


def cpp(spec: ws.Spec, baum: tuple, im_schritt: int | None = None) -> str:
    """Syntaxbaum → C++-Ausdruck (ohne äußere Klammern, ohne -Wparentheses-Warnung)."""
    zn = zeitnamen(spec)

    def r(k) -> tuple[str, str]:
        art = k[0]
        if art == "const":
            return ("true" if k[1] else "false"), "atom"
        if art == "sig":
            return ws.variable(k[1]), "atom"
        if art == "schritt":
            return f"schritt == {k[1]}", "vgl"
        if art == "zeit":
            name = zn[(k[2], k[1])]
            if im_schritt == k[2]:
                return f"schrittzeit() >= {name}", "vgl"
            return f"(schritt == {k[2]} && schrittzeit() >= {name})", "atom"
        if art == "vgl":
            mk = spec.merk(k[1])
            wert = str(int(k[3])) if mk and mk.typ == "int" else _zahl_cpp(k[3])
            return f"{ws.variable(k[1])} {_CPP_OP[k[2]]} {wert}", "vgl"
        if art == "flanke":
            v = ws.variable(k[2])
            return (f"({v} && !{v}_vorher)" if k[1] == "↑" else f"(!{v} && {v}_vorher)"), "atom"
        if art == "nicht":
            t, a = r(k[1])
            if a == "atom":
                return "!" + t, "atom"
            if k[1][0] == "schritt":
                return f"schritt != {k[1][1]}", "vgl"
            return f"!({t})", "atom"
        if art in ("und", "oder"):
            teile = []
            for kind in k[1]:
                t, a = r(kind)
                if (art == "und" and a == "oder") or (art == "oder" and a == "und"):
                    t = f"({t})"
                teile.append(t)
            return (" && " if art == "und" else " || ").join(teile), art
        raise ValueError(art)

    text, art = r(baum)
    if art == "atom" and text.startswith("(") and text.endswith(")") and _klammer_paar(text):
        return text[1:-1]
    return text


def _klammer_paar(text: str) -> bool:
    """True, wenn die erste Klammer erst am Ende schließt: „(a && b)“, nicht „(a) && (b)“."""
    tiefe = 0
    for i, c in enumerate(text):
        tiefe += (c == "(") - (c == ")")
        if tiefe == 0 and i < len(text) - 1:
            return False
    return True


def _schrittmenge(spec: ws.Spec, nummern: list[int]) -> str:
    """[1,2,3,4] → 'schritt >= 1 && schritt <= 4', wenn lückenlos; sonst 'schritt == 1 || …'."""
    alle = sorted(s.nr for s in spec.schritte)
    n = sorted(set(nummern))
    if len(n) >= 3:
        i, j = alle.index(n[0]), alle.index(n[-1])
        if alle[i:j + 1] == n:
            return f"schritt >= {n[0]} && schritt <= {n[-1]}"
    return " || ".join(f"schritt == {x}" for x in n)


# ───────────────────────────── Sketch ─────────────────────────────

def _kommentar_zeile(text: str) -> str:
    return text.replace("*/", "* /")


def sketch(spec: ws.Spec, spec_name: str = "") -> str:
    pf = spec.p
    zr = spec.zeitraffer
    zn = zeitnamen(spec)
    flanken = spec.flanken()
    ziele = spec.aktionsziele()
    sr = [m for m in spec.merker if m.setzen or m.ruecksetzen]
    z: list[str] = []
    a = z.append

    # Kopf
    a("/*")
    a(f"  {_kommentar_zeile(spec.titel)} – Ablaufsteuerung nach GRAFCET ({pf['name']})")
    if spec.quelle:
        a(f"  Aufgabe: {_kommentar_zeile(spec.quelle)}")
    a(f"  Erzeugt mit {SKILL} v{VERSION}" + (f" aus {spec_name}" if spec_name else "")
      + " – Änderungen in der Spec vornehmen und neu erzeugen.")
    a("")
    a(f"  Simulation: {pf['wokwi_neu']} öffnen, sketch.ino und diagram.json ersetzen, Start.")
    a("  Eingänge wie auf der E/A-Platine: Signal 1 = High-Pegel am Pin (Zuordnungsliste, Spalte „Signal 1 bedeutet“).")
    if zr.faktor > 1:
        a(f"  {zr.text()}.")
        a("  Für den Betrieb an der Anlage ZEITRAFFER auf 1 setzen.")
    a("  Der Not-Halt ist hardwaremäßig gelöst und nicht Teil des Programms.")
    a("*/")
    a("")

    # Zuordnungsliste
    a("// ---------- Zuordnungsliste ----------")
    breite = max([len(ws.variable(x.bmk)) for x in (*spec.eingaenge, *spec.analog, *spec.ausgaenge)] or [1])
    def pin_zeile(x, kommentar):
        wert = ws.pin_im_code(spec.plattform, x.pin) + ";"
        a(f"const uint8_t PIN_{ws.variable(x.bmk).upper():<{breite}} = {wert:<4}  // {x.bmk} {kommentar}")

    for e in spec.eingaenge:
        pin_zeile(e, f"{e.name}, {e.kontakt} – 1: {e.signal_1}")
    for an in spec.analog:
        pin_zeile(an, f"{an.name}, {an.signal} für {an.bereich[0]:g} … {an.bereich[1]:g} {an.einheit}")
    for o in spec.ausgaenge:
        pin_zeile(o, f"{o.name} – 1: {o.signal_1}")
    a("")

    # Zeiten
    a("// ---------- Zeiten des GRAFCET ----------")
    a(f"const unsigned long ZEITRAFFER = {zr.faktor};          // 1 = Echtzeit")
    a(f"const unsigned long ZEITRAFFER_AB = {zr.ab_ms}UL;   // ms; kürzere Zeiten laufen in Echtzeit")
    a("constexpr unsigned long zeit(unsigned long ms) { return ZEITRAFFER > 1 && ms >= ZEITRAFFER_AB ? ms / ZEITRAFFER : ms; }")
    for (schritt, ms), name in zn.items():
        a(f"const unsigned long {name} = zeit({ms}UL);  // {ws.dauer_text(ms).replace(' ', '')}/X{schritt}")
    a("")

    # Variablen
    a("// ---------- Signale, Ausgänge, Merker ----------")
    if spec.eingaenge:
        a(f"bool {', '.join(ws.variable(e.bmk) for e in spec.eingaenge)};  // Eingangssignale nach Zuordnungsliste")
    for an in spec.analog:
        a(f"float {ws.variable(an.bmk)};  // {an.bmk} in {an.einheit}")
    if spec.ausgaenge:
        a(f"bool {', '.join(ws.variable(o.bmk) + ' = false' for o in spec.ausgaenge)};")
    for m in spec.merker:
        typ = "int" if m.typ == "int" else "bool"
        start = str(m.start) if m.typ == "int" else ("true" if m.start else "false")
        a(f"{typ} {m.name} = {start};" + (f"  // {m.text}" if m.text else ""))
    for f in flanken:
        a(f"bool {ws.variable(f)}_vorher = false;  // für Flanke von {f}")
    a("")
    a("// ---------- Schrittkette ----------")
    a(f"int schritt = {spec.initial};                 // aktiver Schritt "
      f"(X{min(s.nr for s in spec.schritte)} … X{max(s.nr for s in spec.schritte)})")
    a("unsigned long schrittBeginn = 0;  // millis() bei Aktivierung des Schritts")
    a("")

    # Hilfsfunktionen
    a("unsigned long schrittzeit() { return millis() - schrittBeginn; }")
    a("")
    if spec.analog:
        r0, r1 = pf["rohbereich"]
        a(f"// {pf['adc_text']}")
        a("float analogwert(uint8_t pin, int roh0, int roh1, float von, float bis) {")
        a(f"  float roh = {pf['adc']}(pin);")
        a("  return von + (roh - roh0) * (bis - von) / (roh1 - roh0);")
        a("}")
        a("")
    a("const __FlashStringHelper* schrittName(int x) {")
    a("  switch (x) {")
    for s in spec.schritte:
        a(f"    case {s.nr}: return F(\"{s.name.replace(chr(34), '')}\");")
    a("  }")
    a("  return F(\"?\");")
    a("}")
    a("")

    # speichernde Aktionen
    if spec.gespeichert():
        def zuweisung(akt: ws.Aktion) -> str:
            v = ws.variable(akt.ziel)
            art = akt.ausdruck[0]
            if art == "wert":
                mk = spec.merk(akt.ziel)
                wert = str(akt.ausdruck[1]) if mk and mk.typ == "int" else ("true" if akt.ausdruck[1] else "false")
                return f"{v} = {wert};"
            return f"{v} = {v} {'+' if art == 'plus' else '-'} {akt.ausdruck[2]};"

        for art, fname, text in (("deaktivierung", "beimVerlassen", "bei Deaktivierung (↓)"),
                                 ("aktivierung", "beimAktivieren", "bei Aktivierung (↑)")):
            if not any(x.art == art for s in spec.schritte for x in s.aktionen):
                continue
            a(f"// speichernd wirkende Aktionen {text}")
            a(f"void {fname}(int x) {{")
            a("  switch (x) {")
            for s in spec.schritte:
                akt = [x for x in s.aktionen if x.art == art]
                if akt:
                    a(f"    case {s.nr}: " + " ".join(zuweisung(x) for x in akt) + " break;  // " + "; ".join(x.text for x in akt))
            a("  }")
            a("}")
            a("")

    arten = {x.art for s in spec.schritte for x in s.aktionen}
    a("void schrittWechsel(int neu) {")
    if "deaktivierung" in arten:
        a("  beimVerlassen(schritt);")
    a("  schritt = neu;")
    a("  schrittBeginn = millis();")
    if "aktivierung" in arten:
        a("  beimAktivieren(schritt);")
    a("}")
    a("")

    # Zyklus
    a("// 1. Eingänge lesen")
    a("void eingaengeLesen() {")
    for e in spec.eingaenge:
        a(f"  {ws.variable(e.bmk)} = digitalRead(PIN_{ws.variable(e.bmk).upper()}) == HIGH;"
          f"  // {e.kontakt}: 1 = {e.signal_1}")
    for an in spec.analog:
        a(f"  {ws.variable(an.bmk)} = analogwert(PIN_{ws.variable(an.bmk).upper()}, {an.rohbereich[0]}, "
          f"{an.rohbereich[1]}, {_zahl_cpp(an.bereich[0])}, {_zahl_cpp(an.bereich[1])});")
    a("}")
    a("")
    if sr:
        a("// 2. Speicher (RS rücksetzdominant: erst setzen, dann rücksetzen; SR umgekehrt)")
        a("void speicher() {")
        for m in sr:
            zeilen = []
            if m.setzen:
                zeilen.append(f"  if ({cpp(spec, m.setzen)}) {m.name} = true;   // setzen: {m.setzen_text}")
            if m.ruecksetzen:
                zeilen.append(f"  if ({cpp(spec, m.ruecksetzen)}) {m.name} = false;  // rücksetzen: {m.ruecksetzen_text}")
            if m.dominant == "setzen":
                zeilen.reverse()
            z.extend(zeilen)
        a("}")
        a("")
    if spec.erzwingen:
        a("// 3. Zwangssteuerung: solange die Bedingung gilt, steht die Schrittkette im genannten Schritt")
        a("bool erzwingen() {")
        for e in spec.erzwingen:
            a(f"  if ({cpp(spec, e.bedingung)}) {{  // {e.text}" + (f" – {e.grund}" if e.grund else ""))
            a(f"    if (schritt != {e.nach}) schrittWechsel({e.nach});")
            a("    return true;")
            a("  }")
        a("  return false;")
        a("}")
        a("")
    a("// 4. Transitionen: höchstens ein Schrittwechsel je Zyklus")
    a("void transitionen() {")
    a("  switch (schritt) {")
    for s in spec.schritte:
        a(f"    case {s.nr}:  // {s.name}")
        for i, t in enumerate(s.transitionen):
            schluessel = "if" if i == 0 else "else if"
            a(f"      {schluessel} ({cpp(spec, t.bedingung, s.nr)}) schrittWechsel({t.ziel});  // {t.text}")
        a("      break;")
    a("  }")
    a("}")
    a("")
    a("// 5. Aktionen: kontinuierlich wirkend, 1 solange der Schritt aktiv ist")
    a("void aktionen() {")
    for ziel, arten in ziele.items():
        if arten != {"kontinuierlich"}:
            continue
        teile = []
        einfach = []
        for s in spec.schritte:
            for akt in s.aktionen:
                if akt.ziel == ziel and akt.art == "kontinuierlich":
                    if akt.bedingung:
                        bed = cpp(spec, akt.bedingung)
                        if akt.bedingung[0] == "oder":
                            bed = f"({bed})"
                        teile.append(f"(schritt == {s.nr} && {bed})")
                    else:
                        einfach.append(s.nr)
        ausdruck = []
        if einfach:
            menge = _schrittmenge(spec, einfach)
            ausdruck.append(f"({menge})" if teile else menge)
        ausdruck += teile
        schritte = sorted({s.nr for s in spec.schritte for x in s.aktionen if x.ziel == ziel})
        a(f"  {ws.variable(ziel)} = {' || '.join(ausdruck)};  // {ziel}: " + ", ".join(f"X{n}" for n in schritte))
    a("}")
    a("")
    if spec.zuweisungen:
        a("// 6. Verknüpfungen (Logikplan) nach der Schrittkette")
        a("void verknuepfungen() {")
        for zw in spec.zuweisungen:
            a(f"  {ws.variable(zw.ziel)} = {cpp(spec, zw.bedingung)};  // {zw.ziel} = {zw.text}"
              + (f" – {zw.grund}" if zw.grund else ""))
        a("}")
        a("")
    a("// 7. Ausgänge schreiben")
    a("void ausgaengeSchreiben() {")
    for o in spec.ausgaenge:
        a(f"  digitalWrite(PIN_{ws.variable(o.bmk).upper()}, {ws.variable(o.bmk)} ? HIGH : LOW);")
    a("}")
    a("")
    if flanken:
        a("void flankenMerken() {")
        for f in flanken:
            a(f"  {ws.variable(f)}_vorher = {ws.variable(f)};")
        a("}")
        a("")

    # Meldungen
    bits = [ws.variable(e.bmk) for e in spec.eingaenge] + [ws.variable(o.bmk) for o in spec.ausgaenge]
    a("// Serieller Monitor: Zeile bei jeder Änderung von Schritt, Eingängen oder Ausgängen, sonst alle "
      f"{MELDEN_MS // 1000} s")
    a("int gemeldeterSchritt = -1;")
    a("unsigned long gemeldetesBild = 0;")
    a("unsigned long letzteMeldung = 0;")
    a("")
    a("unsigned long zustandsbild() {")
    a("  unsigned long bild = 0;")
    for i, v in enumerate(bits):
        a(f"  if ({v}) bild |= 1UL << {i};")
    a("  return bild;")
    a("}")
    a("")
    a("void melden() {")
    a("  Serial.print(F(\"[\"));")
    a("  Serial.print(millis() / 1000.0, 1);")
    a("  Serial.print(F(\" s] X\"));")
    a("  Serial.print(schritt);")
    a("  Serial.print(F(\" \"));")
    a("  Serial.print(schrittName(schritt));")
    for gruppe in (spec.eingaenge, spec.ausgaenge):
        if gruppe:
            a("  Serial.print(F(\" |\"));")
            for x in gruppe:
                a(f"  Serial.print(F(\" {x.bmk}=\")); Serial.print((int){ws.variable(x.bmk)});")
    if spec.analog:
        a("  Serial.print(F(\" |\"));")
        for an in spec.analog:
            a(f"  Serial.print(F(\" {an.bmk}=\")); Serial.print({ws.variable(an.bmk)}, {an.stellen}); "
              f"Serial.print(F(\" {an.einheit}\"));")
    if spec.merker:
        a("  Serial.print(F(\" |\"));")
        for m in spec.merker:
            a(f"  Serial.print(F(\" {m.name}=\")); Serial.print((int){m.name});")
    a("  Serial.println();")
    a("  gemeldeterSchritt = schritt;")
    a("  gemeldetesBild = zustandsbild();")
    a("  letzteMeldung = millis();")
    a("}")
    a("")
    a("void meldenBeiAenderung() {")
    a(f"  if (schritt != gemeldeterSchritt || zustandsbild() != gemeldetesBild || millis() - letzteMeldung >= {MELDEN_MS}UL)")
    a("    melden();")
    a("}")
    a("")

    # setup und loop
    a("void setup() {")
    for e in spec.eingaenge:
        a(f"  pinMode(PIN_{ws.variable(e.bmk).upper()}, INPUT);")
    for o in spec.ausgaenge:
        a(f"  pinMode(PIN_{ws.variable(o.bmk).upper()}, OUTPUT);")
    a("  Serial.begin(115200);")
    a(f"  Serial.println(F(\"{spec.titel.replace(chr(34), '')} – Simulation ({pf['name']})\"));")
    if zr.faktor > 1:
        a(f"  Serial.println(F(\"{zr.text()}\"));")
    a("  schrittBeginn = millis();")
    if "aktivierung" in arten:
        a("  beimAktivieren(schritt);")
    a("  Serial.println(F(\"Bereit\"));")
    a("}")
    a("")
    a("void loop() {")
    a("  eingaengeLesen();")
    if sr:
        a("  speicher();")
    if spec.erzwingen:
        a("  if (!erzwingen()) transitionen();")
    else:
        a("  transitionen();")
    a("  aktionen();")
    if spec.zuweisungen:
        a("  verknuepfungen();")
    a("  ausgaengeSchreiben();")
    if flanken:
        a("  flankenMerken();")
    a("  meldenBeiAenderung();")
    a("}")
    return "\n".join(z) + "\n"


# ───────────────────────────── diagram.json ─────────────────────────────

_FARBE_TASTER = (("start", "green"), ("ein", "green"), ("stop", "black"), ("aus", "black"),
                 ("quitt", "blue"), ("rücksetz", "blue"))


def farbe_taster(e: ws.Eingang) -> str:
    if e.farbe:
        return e.farbe
    name = e.name.lower()
    return next((f for wort, f in _FARBE_TASTER if wort in name), "white")


def farbe_led(o: ws.Ausgang) -> str:
    if o.farbe:
        return o.farbe
    name = o.name.lower()
    if "stör" in name or "fehler" in name or "alarm" in name:
        return "red"
    if "warn" in name:
        return "yellow"
    if o.bmk.startswith("-P") and ("betrieb" in name or "automatik" in name or "bereit" in name):
        return "green"
    return "orange" if not o.bmk.startswith("-P") else "white"


def _kurz(text: str, n: int = 22) -> str:
    return text if len(text) <= n else text[: n - 1].rstrip() + "…"


def bauteil_ids(spec: ws.Spec) -> dict[str, str]:
    """Kennzeichen → id des bedienbaren Bauteils in diagram.json (für Szenarien)."""
    ids = {}
    for e in spec.eingaenge:
        ids[e.bmk] = ("btn_" if e.bauteil == "taster" else "sw_") + ws.variable(e.bmk)
    for an in spec.analog:
        ids[an.bmk] = "pot_" + ws.variable(an.bmk)
    for o in spec.ausgaenge:
        ids[o.bmk] = "led_" + ws.variable(o.bmk)
    return ids


def _diagramm_einfach(spec: ws.Spec) -> dict:
    """Einfache Anordnung ohne Leitungsführung (ESP32): Wokwi zeichnet gerade Leitungen."""
    pf = spec.p
    b = pf["id"]
    ids = bauteil_ids(spec)
    teile = [{"type": pf["teil"], "id": b, "top": 0, "left": 0, "attrs": {}}]
    verb: list[list] = []
    vcc, gnd_o, gnd_u = f"{b}:{pf['vcc']}", f"{b}:{pf['gnd_oben']}", f"{b}:{pf['gnd_unten']}"
    if spec.plattform == "esp32":
        verb += [[f"{b}:TX", "$serialMonitor:RX", "", []], [f"{b}:RX", "$serialMonitor:TX", "", []]]

    # Eingänge links vom Board
    for i, e in enumerate(spec.eingaenge):
        y = -40 + i * 100
        pin = f"{b}:{ws.wokwi_pin(spec.plattform, e.pin)}"
        tid = ids[e.bmk]
        if e.bauteil == "taster":
            attrs = {"color": farbe_taster(e), "label": _kurz(f"{e.bmk} {e.name.replace('Taster ', '')}"),
                     "bounce": "0"}
            if e.taste:
                attrs["key"] = e.taste
            teile.append({"type": "wokwi-pushbutton", "id": tid, "top": y, "left": -380, "attrs": attrs})
            r = f"r_{ws.variable(e.bmk)}"
            teile.append({"type": "wokwi-resistor", "id": r, "top": y + 60, "left": -250, "attrs": {"value": "10000"}})
            if e.kontakt == "NO":   # Schließer gegen VCC, Pull-down: betätigt → 1
                verb += [[f"{tid}:1.l", vcc, "red", []], [f"{tid}:2.r", pin, "green", []],
                         [f"{r}:1", f"{tid}:2.l", "green", []], [f"{r}:2", gnd_u, "black", []]]
            else:                   # Öffnerverhalten: Pull-up, Taster gegen GND: unbetätigt → 1
                verb += [[f"{tid}:1.l", gnd_u, "black", []], [f"{tid}:2.r", pin, "green", []],
                         [f"{r}:1", f"{tid}:2.l", "green", []], [f"{r}:2", vcc, "red", []]]
        else:
            teile.append({"type": "wokwi-slide-switch", "id": tid, "top": y, "left": -360,
                          "attrs": {"value": "1" if e.start else "", "bounce": "0"}})
            teile.append({"type": "wokwi-text", "id": f"txt_{ws.variable(e.bmk)}", "top": y + 45, "left": -400,
                          "attrs": {"text": f"{e.bmk} {_kurz(e.name, 26)}\nrechts = 1: {_kurz(e.signal_1, 26)}"}})
            verb += [[f"{tid}:1", gnd_u, "black", []], [f"{tid}:2", pin, "green", []], [f"{tid}:3", vcc, "red", []]]

    # Ausgänge über dem Board
    for j, o in enumerate(spec.ausgaenge):
        x = 20 + j * 75
        pin = f"{b}:{ws.wokwi_pin(spec.plattform, o.pin)}"
        lid, r = ids[o.bmk], f"rv_{ws.variable(o.bmk)}"
        teile.append({"type": "wokwi-led", "id": lid, "top": -230, "left": x,
                      "attrs": {"color": farbe_led(o), "label": _kurz(o.bmk + " " + o.signal_1, 18)}})
        teile.append({"type": "wokwi-resistor", "id": r, "top": -120, "left": x - 20, "rotate": 90,
                      "attrs": {"value": "220"}})
        verb += [[pin, f"{r}:2", "orange", []], [f"{r}:1", f"{lid}:A", "orange", []],
                 [f"{lid}:C", gnd_o, "black", []]]

    # Analoggeber unter dem Board
    for k, an in enumerate(spec.analog):
        x = 40 + k * 150
        pid = ids[an.bmk]
        roh = ws.roh_aus_wert(spec, an, an.start)
        wert = round(roh / pf["roh_vcc"] * 1023)
        teile.append({"type": "wokwi-potentiometer", "id": pid, "top": 280, "left": x,
                      "attrs": {"value": str(max(0, min(1023, wert)))}})
        teile.append({"type": "wokwi-text", "id": f"txt_{ws.variable(an.bmk)}", "top": 360, "left": x - 20,
                      "attrs": {"text": f"{an.bmk} {_kurz(an.name, 22)}\n{an.bereich[0]:g} … {an.bereich[1]:g} {an.einheit}"}})
        verb += [[f"{pid}:GND", gnd_u, "black", []], [f"{pid}:VCC", vcc, "red", []],
                 [f"{pid}:SIG", f"{b}:{ws.wokwi_pin(spec.plattform, an.pin)}", "blue", []]]

    return {"version": 1, "author": f"{SKILL} v{VERSION}", "editor": "wokwi", "parts": teile,
            "connections": verb, "serialMonitor": {"display": "always", "newline": "lf"}, "dependencies": {}}


# Maße und Pins der Wokwi-Bauteile in px, unrotiert (@wokwi/elements 1.9.2: offsetWidth/-Height, pinInfo)
GEOMETRIE = {
    "wokwi-arduino-uno": (274, 206, {
        **{str(i): (x, 9) for i, x in enumerate((255.5, 246, 236.5, 227, 217.5, 208, 198.5, 189,
                                                  173, 163, 153.5, 144, 134.5, 125))},
        "GND.1": (115.5, 9), "AREF": (106, 9), "5V": (160, 191.5), "GND.2": (169.5, 191.5),
        "GND.3": (179, 191.5), "VIN": (188.5, 191.5),
        **{f"A{i}": (x, 191.5) for i, x in enumerate((208, 217.5, 227, 236.5, 246, 255.5))}}),
    "wokwi-pushbutton": (67, 48, {"1.l": (0, 13), "2.l": (0, 32), "1.r": (67, 13), "2.r": (67, 32)}),
    "wokwi-slide-switch": (32, 39, {"1": (6.5, 34), "2": (16, 34), "3": (25.5, 34)}),
    "wokwi-potentiometer": (76, 80, {"GND": (29, 68.5), "SIG": (39, 68.5), "VCC": (49, 68.5)}),
    "wokwi-led": (40, 50, {"A": (25, 42), "C": (15, 42)}),
    "wokwi-resistor": (59, 11, {"1": (0, 5.65), "2": (58.8, 5.65)}),
}


def pin_xy(teil: dict, pin: str) -> tuple[float, float]:
    """Lage eines Bauteil-Pins im Diagramm; Drehung um die Mitte (wie im Wokwi-Editor)."""
    import math
    b, h, pins = GEOMETRIE[teil["type"]]
    px, py = pins[pin]
    dx, dy = px - b / 2, py - h / 2
    w = math.radians(teil.get("rotate", 0))
    rx, ry = dx * math.cos(w) - dy * math.sin(w), dx * math.sin(w) + dy * math.cos(w)
    return round(teil["left"] + b / 2 + rx, 2), round(teil["top"] + h / 2 + ry, 2)


def _zahl_kurz(v: float) -> str:
    return f"{round(v, 2):g}"


def wegpunkte_zu_hinweisen(start, punkte) -> list[str]:
    """Rechtwinklige Wegpunkte → Wokwi-Hinweise (v…/h…); der letzte Punkt ist der Ziel-Pin."""
    hinweise, (x, y) = [], start
    for nx, ny in punkte:
        dx, dy = round(nx - x, 2), round(ny - y, 2)
        if dx and dy:
            raise ValueError(f"Leitung nicht rechtwinklig: ({x}, {y}) → ({nx}, {ny})")
        if dx:
            hinweise.append(f"h{_zahl_kurz(dx)}")
        elif dy:
            hinweise.append(f"v{_zahl_kurz(dy)}")
        x, y = nx, ny
    return hinweise


def hinweise_abfahren(start, hinweise: list[str]) -> tuple[float, float]:
    """Endpunkt einer Leitung, wenn man die Hinweise vom Quell-Pin aus abfährt (ohne „*“)."""
    x, y = start
    for h in hinweise:
        if h == "*":
            break
        if h[0] == "h":
            x += float(h[1:])
        elif h[0] == "v":
            y += float(h[1:])
    return round(x, 2), round(y, 2)


def _beschriftung(x, standard: str, n: int = 9) -> str:
    """Kurzname für Beschriftungen in Wokwi: Feld „kurz“ der Spec, sonst erstes Wort von standard."""
    return _kurz(x.kurz or (standard.split(" ")[0] if standard else ""), n)


def _diagramm_uno(spec: ws.Spec) -> dict:
    """Uno mit Leitungsführung: Ausgänge über dem Board (Reihenfolge der Stiftleiste), Eingänge als
    Bedienfeld rechts mit Versorgungsschienen, Analoggeber unter dem Board. Alle Leitungen rechtwinklig."""
    b = "uno"
    board = {"type": "wokwi-arduino-uno", "id": b, "top": 0, "left": 0, "attrs": {}}
    teile, verb, nach_id = [board], [], {b: board}
    ids = bauteil_ids(spec)

    def teil(t):
        teile.append(t)
        nach_id[t["id"]] = t
        return t

    def xy(ende):
        tid, _, pin = ende.partition(":")
        return pin_xy(nach_id[tid], pin)

    def kabel(q, z, farbe, ecken=()):
        verb.append([q, z, farbe, wegpunkte_zu_hinweisen(xy(q), [*ecken, xy(z)])])

    def text(tid, x, y, inhalt):
        teile.append({"type": "wokwi-text", "id": tid, "top": round(y, 2), "left": round(x, 2),
                      "attrs": {"text": inhalt}})

    upin = lambda pin: f"{b}:{ws.wokwi_pin('arduino-uno', pin)}"  # noqa: E731
    uxy = lambda pin: GEOMETRIE["wokwi-arduino-uno"][2][ws.wokwi_pin("arduino-uno", pin)]  # noqa: E731

    # Ausgänge: LED mit Vorwiderstand senkrecht darunter, Leitung zum Pin; Katoden über eine Masseschiene
    oben = sorted([o for o in spec.ausgaenge if uxy(o.pin)[1] < 100], key=lambda o: uxy(o.pin)[0])
    n = len(oben)
    abstand = 80
    rechts = min(175.0, max([uxy(o.pin)[0] for o in oben] or [175.0]))
    anoden = [rechts - (n - 1 - j) * abstand for j in range(n)]
    rang = {o.bmk: r for r, o in enumerate(sorted(oben, key=lambda o: -abs(uxy(o.pin)[0] - anoden[oben.index(o)])))}
    gnd_bahn = -10
    bahnen = {o.bmk: -18 - rang[o.bmk] * 7 for o in oben}
    unten_r2 = min(bahnen.values(), default=-18) - 12        # Unterkante der Vorwiderstände (Pin 2)
    anode_y = unten_r2 - 70.8                                 # 12 px Abstand LED–Widerstand, Widerstand 58,8 px
    led_top = anode_y - 42
    schiene = led_top - 14
    stamm = (anoden[0] - 45) if anoden else 0
    for j, o in enumerate(oben):
        ax = anoden[j]
        lid, r = ids[o.bmk], f"rv_{ws.variable(o.bmk)}"
        teil({"type": "wokwi-led", "id": lid, "top": round(led_top, 2), "left": round(ax - 25, 2),
              "attrs": {"color": farbe_led(o)}})
        teil({"type": "wokwi-resistor", "id": r, "top": round(anode_y + 36, 2), "left": round(ax - 29.35, 2),
              "rotate": 90, "attrs": {"value": "220"}})
        text(f"txt_{ws.variable(o.bmk)}", ax - 34, schiene - 40, f"{o.bmk}\n{_beschriftung(o, o.signal_1 or o.name)}")
        px, _ = uxy(o.pin)
        kabel(upin(o.pin), f"{r}:2", "orange", [(px, bahnen[o.bmk]), (ax, bahnen[o.bmk])])
        kabel(f"{r}:1", f"{lid}:A", "orange")
        cx, cy = xy(f"{lid}:C")
        kabel(f"{lid}:C", f"{b}:GND.1", "black",
              [(cx, cy + 4), (ax - 55, cy + 4), (ax - 55, schiene), (stamm, schiene), (stamm, gnd_bahn),
               (115.5, gnd_bahn)])

    # Eingänge: Bedienfeld rechts, Signal über eine eigene Bahn über dem Board
    x0, zeile = 360, 90
    x_vcc, x_gnd = x0 + 166, x0 + 180
    ein = sorted(spec.eingaenge, key=lambda e: uxy(e.pin)[0])
    m = len(ein)
    y_gnd = max(245, 10 + (m - 1) * zeile + 80)              # untere Bahnen zu GND.2 und 5V, unter dem Bedienfeld
    y_vcc = y_gnd + 10
    zu_vcc = lambda q, ecken: kabel(q, f"{b}:5V", "red", [*ecken, (x_vcc, y_vcc), (160, y_vcc)])        # noqa: E731
    zu_gnd = lambda q, ecken: kabel(q, f"{b}:GND.2", "black", [*ecken, (x_gnd, y_gnd), (169.5, y_gnd)])  # noqa: E731
    for i, e in enumerate(ein):
        ry = 10 + i * zeile
        px, py = uxy(e.pin)
        bahn, kanal = -18 - (m - 1 - i) * 7, x0 - 20 - i * 8
        tid = ids[e.bmk]
        if e.bauteil == "taster":
            attrs = {"color": farbe_taster(e), "bounce": "0",
                     "label": f"{e.bmk} {_beschriftung(e, e.name.replace('Taster ', ''), 12)}"}
            if e.taste:
                attrs["key"] = e.taste
            teil({"type": "wokwi-pushbutton", "id": tid, "top": ry, "left": x0, "attrs": attrs})
            r = f"r_{ws.variable(e.bmk)}"
            teil({"type": "wokwi-resistor", "id": r, "top": round(ry + 32 - 5.65, 2), "left": x0 + 82,
                  "attrs": {"value": "10000"}})
            if py < 100:
                kabel(upin(e.pin), f"{tid}:2.l", "green", [(px, bahn), (kanal, bahn), (kanal, ry + 32)])
            else:
                verb.append([upin(e.pin), f"{tid}:2.l", "green", []])
            kabel(f"{tid}:2.r", f"{r}:1", "green")
            if e.kontakt == "NO":    # Schließer gegen VCC, 10 kΩ nach GND: betätigt → 1
                zu_vcc(f"{tid}:1.r", [(x_vcc, ry + 13)])
                zu_gnd(f"{r}:2", [(x_gnd, ry + 32)])
            else:                    # Taster gegen GND, 10 kΩ nach VCC: unbetätigt → 1 (Öffnerverhalten)
                zu_gnd(f"{tid}:1.r", [(x_gnd, ry + 13)])
                zu_vcc(f"{r}:2", [(x_vcc, ry + 32)])
        else:
            sx, sy = x0 + 17, ry + 4
            teil({"type": "wokwi-slide-switch", "id": tid, "top": sy, "left": sx,
                  "attrs": {"value": "1" if e.start else "", "bounce": "0"}})
            text(f"txt_{ws.variable(e.bmk)}", x0 + 60, ry + 6,
                 f"{e.bmk} {_beschriftung(e, e.signal_1 or e.name, 12)}\nrechts = 1")
            p2x, p2y = xy(f"{tid}:2")
            if py < 100:
                kabel(upin(e.pin), f"{tid}:2", "green", [(px, bahn), (kanal, bahn), (kanal, p2y + 16), (p2x, p2y + 16)])
            else:
                verb.append([upin(e.pin), f"{tid}:2", "green", []])
            p3x, p3y = xy(f"{tid}:3")
            zu_vcc(f"{tid}:3", [(p3x, p3y + 6), (x_vcc, p3y + 6)])
            p1x, p1y = xy(f"{tid}:1")
            zu_gnd(f"{tid}:1", [(p1x, p1y + 24), (x_gnd, p1y + 24)])

    # Analoggeber: Potentiometer um 180° gedreht (Anschlüsse oben), rechts der Analogpins
    ana = sorted(spec.analog, key=lambda a: uxy(a.pin)[0])
    k_n = len(ana)
    for k, an in enumerate(ana):
        pid = ids[an.bmk]
        left, top = 300 + k * 130, y_vcc + 35
        teil({"type": "wokwi-potentiometer", "id": pid, "top": top, "left": left, "rotate": 180,
                    "attrs": {"value": str(max(0, min(1023, round(ws.roh_aus_wert(spec, an, an.start)
                                                                   / spec.p["roh_vcc"] * 1023))))}})
        text(f"txt_{ws.variable(an.bmk)}", left - 4, top + 86,
             f"{an.bmk} {_beschriftung(an, an.name, 10)}\n{an.bereich[0]:g} … {an.bereich[1]:g} {an.einheit}")
        sx, sy = xy(f"{pid}:SIG")
        ax_, ay_ = uxy(an.pin)
        if ay_ > 100:   # kleinerer Abstand zum Pin → tiefere Bahn (keine Kreuzung der Signalleitungen)
            bahn = 214 + (k_n - 1 - k) * 5
            kabel(f"{pid}:SIG", upin(an.pin), "blue", [(sx, bahn), (ax_, bahn)])
        else:
            verb.append([f"{pid}:SIG", upin(an.pin), "blue", []])
        vx, _ = xy(f"{pid}:VCC")
        kabel(f"{pid}:VCC", f"{b}:5V", "red", [(vx, y_vcc), (160, y_vcc)])
        gx, _ = xy(f"{pid}:GND")
        kabel(f"{pid}:GND", f"{b}:GND.2", "black", [(gx, y_gnd), (169.5, y_gnd)])

    # Ausgänge an Pins der unteren Leiste (selten): ohne Leitungsführung
    for o in spec.ausgaenge:
        if o in oben:
            continue
        lid, r = ids[o.bmk], f"rv_{ws.variable(o.bmk)}"
        x = 20 + len(teile) * 3
        teil({"type": "wokwi-led", "id": lid, "top": 420, "left": x, "attrs": {"color": farbe_led(o)}})
        teil({"type": "wokwi-resistor", "id": r, "top": 480, "left": x - 20, "rotate": 90, "attrs": {"value": "220"}})
        text(f"txt_{ws.variable(o.bmk)}", x - 10, 400, f"{o.bmk}")
        verb += [[upin(o.pin), f"{r}:2", "orange", []], [f"{r}:1", f"{lid}:A", "orange", []],
                 [f"{lid}:C", f"{b}:GND.3", "black", []]]

    return {"version": 1, "author": f"{SKILL} v{VERSION}", "editor": "wokwi", "parts": teile,
            "connections": verb, "serialMonitor": {"display": "always", "newline": "lf"}, "dependencies": {}}


def diagramm(spec: ws.Spec) -> dict:
    return _diagramm_uno(spec) if spec.plattform == "arduino-uno" else _diagramm_einfach(spec)


# Pins der verwendeten Wokwi-Bauteile (docs.wokwi.com/parts, Stand 11/2026; wokwi-boards für den ESP32)
TEILE_PINS = {
    "wokwi-arduino-uno": {str(i) for i in range(14)} | {f"A{i}" for i in range(6)}
                         | {"GND.1", "GND.2", "GND.3", "5V", "VIN"},
    "board-esp32-devkit-c-v4": {"3V3", "EN", "VP", "VN", "34", "35", "32", "33", "25", "26", "27", "14", "12",
                                "GND.1", "13", "D2", "D3", "CMD", "5V", "GND.2", "23", "22", "TX", "RX", "21",
                                "GND.3", "19", "18", "5", "17", "16", "4", "0", "2", "15", "D1", "D0", "CLK"},
    "wokwi-pushbutton": {"1.l", "2.l", "1.r", "2.r"},
    "wokwi-slide-switch": {"1", "2", "3"},
    "wokwi-potentiometer": {"GND", "SIG", "VCC"},
    "wokwi-led": {"A", "C"},
    "wokwi-resistor": {"1", "2"},
    "wokwi-text": set(),
}


def pruefe_diagramm(spec: ws.Spec, d: dict) -> list[ws.Befund]:
    """Formale Prüfung von diagram.json: Bauteile, Pins, Belegung, Netze der Ein- und Ausgänge."""
    b: list[ws.Befund] = []
    teile = {t["id"]: t for t in d.get("parts", [])}
    if len(teile) != len(d.get("parts", [])):
        b.append(ws.Befund("❌", "doppelte Bauteil-id in diagram.json"))
    for t in teile.values():
        if t["type"] not in TEILE_PINS:
            b.append(ws.Befund("⚠️", f"Bauteil {t['id']}: Typ {t['type']} nicht in der Prüftabelle"))
    netz: dict[str, set[str]] = {}

    def knoten(end: str) -> str:
        if end.startswith("$serialMonitor"):
            return end
        tid, _, pin = end.partition(":")
        if tid not in teile:
            b.append(ws.Befund("❌", f"Verbindung zu unbekanntem Bauteil {tid}"))
        elif teile[tid]["type"] in TEILE_PINS and pin not in TEILE_PINS[teile[tid]["type"]]:
            b.append(ws.Befund("❌", f"{tid}: Pin „{pin}“ gibt es bei {teile[tid]['type']} nicht"))
        return end

    for c in d.get("connections", []):
        if len(c) != 4:
            b.append(ws.Befund("❌", f"Verbindung {c}: vier Einträge erwartet (Quelle, Ziel, Farbe, Hinweise)"))
            continue
        q, z = knoten(c[0]), knoten(c[1])
        # Leitungsführung: Hinweise vom Quell-Pin abfahren, Ende muss auf dem Ziel-Pin liegen
        tq, tz = teile.get(c[0].partition(":")[0]), teile.get(c[1].partition(":")[0])
        if c[3] and "*" not in c[3] and tq and tz and tq["type"] in GEOMETRIE and tz["type"] in GEOMETRIE:
            try:
                ende = hinweise_abfahren(pin_xy(tq, c[0].partition(":")[2]), c[3])
                ziel = pin_xy(tz, c[1].partition(":")[2])
            except KeyError:
                continue
            if abs(ende[0] - ziel[0]) > 0.6 and abs(ende[1] - ziel[1]) > 0.6:
                b.append(ws.Befund("⚠️", f"Leitung {c[0]} → {c[1]} endet schräg (Wegpunkte prüfen)"))
        netz.setdefault(q, set()).add(z)
        netz.setdefault(z, set()).add(q)
    # Netze über Leitungen und interne Verbindungen (Taster 1.l–1.r, 2.l–2.r; GND-Pins)
    for t in teile.values():
        if t["type"] == "wokwi-pushbutton":
            for s in ("1", "2"):
                l, r = f"{t['id']}:{s}.l", f"{t['id']}:{s}.r"
                netz.setdefault(l, set()).add(r)
                netz.setdefault(r, set()).add(l)
    bid = spec.p["id"]
    gnds = [f"{bid}:{g}" for g in ("GND.1", "GND.2", "GND.3")]
    for g in gnds:
        netz.setdefault(g, set()).update(x for x in gnds if x != g)

    def huelle(start: str) -> set[str]:
        gesehen, offen = set(), [start]
        while offen:
            n = offen.pop()
            if n in gesehen:
                continue
            gesehen.add(n)
            offen += list(netz.get(n, ()))
        return gesehen

    vcc, gnd = f"{bid}:{spec.p['vcc']}", f"{bid}:{spec.p['gnd_unten']}"
    if gnd in huelle(vcc):
        b.append(ws.Befund("❌", "Kurzschluss: Versorgung und Masse im selben Netz"))
    ids = bauteil_ids(spec)
    for x in (*spec.eingaenge, *spec.analog, *spec.ausgaenge):
        pin = f"{bid}:{ws.wokwi_pin(spec.plattform, x.pin)}"
        tid = ids[x.bmk]
        if tid not in teile:
            b.append(ws.Befund("❌", f"{x.bmk}: Bauteil {tid} fehlt"))
            continue
        h = huelle(pin)
        if not any(n.startswith(tid + ":") for n in h) and not any(
                n.startswith(f"rv_{ws.variable(x.bmk)}:") for n in h):
            b.append(ws.Befund("❌", f"{x.bmk}: Pin {x.pin} nicht mit {tid} verbunden"))
        if vcc in h or gnd in h:
            b.append(ws.Befund("❌", f"{x.bmk}: Pin {x.pin} direkt an Versorgung oder Masse"))
    return b


# ───────────────────────────── wokwi.toml, Szenarien ─────────────────────────────

def wokwi_toml(spec: ws.Spec) -> str:
    pf = spec.p
    elf = pf["firmware"].rsplit(".", 1)[0] + ".elf"
    return ("# Wokwi für VS Code und wokwi-cli: Firmware vorher bauen (Begleitblatt, Abschnitt „In Wokwi öffnen“).\n"
            f"# arduino-cli compile --fqbn {pf['fqbn']} --output-dir build build/sketch\n"
            "[wokwi]\n"
            "version = 1\n"
            f"firmware = '{pf['firmware']}'\n"
            f"elf = '{elf}'\n")


def _yaml_wert(v) -> str:
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, float):
        return f"{v:g}"
    return str(v)


def szenario_yaml(name: str, schritte: list[dict]) -> str:
    """Wokwi-Szenario (docs.wokwi.com/wokwi-ci/automation-scenarios) aus einer Liste von Schritten."""
    z = [f"# Erzeugt mit {SKILL} v{VERSION} – Aufruf: wokwi-cli . --scenario <datei> --timeout <ms>",
         f"name: {_yaml_wert(name)}", "version: 1", f"author: {_yaml_wert(SKILL)}", "steps:"]
    for s in schritte:
        if "kommentar" in s:
            z.append(f"  # {s['kommentar']}")
            continue
        (art, inhalt), = s.items()
        if isinstance(inhalt, dict):
            z.append(f"  - {art}:")
            z += [f"      {k}: {_yaml_wert(v)}" for k, v in inhalt.items()]
        else:
            z.append(f"  - {art}: {_yaml_wert(inhalt) if not str(inhalt).endswith('ms') else inhalt}")
    return "\n".join(z) + "\n"


# ───────────────────────────── Schreiben ─────────────────────────────

def _md5(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def schreibe(ordner: Path, dateien: dict[str, str], ueberschreiben: bool = False) -> list[str]:
    """Schreibt erzeugte Dateien. Von Hand geänderte Dateien (Prüfsumme ≠ Manifest) bleiben stehen,
    außer mit ueberschreiben=True. Gibt Meldungen zurück; ValueError, wenn etwas geschützt ist."""
    ordner.mkdir(parents=True, exist_ok=True)
    manifest_pfad = ordner / MANIFEST
    alt = json.loads(manifest_pfad.read_text(encoding="utf-8")) if manifest_pfad.is_file() else {}
    geschuetzt = []
    for rel in dateien:
        ziel = ordner / rel
        if ziel.is_file() and not ueberschreiben:
            ist = _md5(ziel.read_text(encoding="utf-8"))
            if alt.get(rel) != ist:
                geschuetzt.append(rel)
    if geschuetzt:
        raise ValueError("von Hand geändert oder nicht von diesem Werkzeug erzeugt: " + ", ".join(geschuetzt)
                         + " – neuen Ordner wählen oder --ueberschreiben")
    meldungen = []
    neu = {}
    for rel, text in dateien.items():
        ziel = ordner / rel
        ziel.parent.mkdir(parents=True, exist_ok=True)
        vorher = ziel.read_text(encoding="utf-8") if ziel.is_file() else None
        if vorher != text:
            ziel.write_text(text, encoding="utf-8")
            meldungen.append(f"geschrieben: {ziel}")
        neu[rel] = _md5(text)
    # nicht mehr erzeugte Szenarien entfernen (nur eigene, unveränderte)
    for rel, summe in alt.items():
        if rel not in neu and (ordner / rel).is_file() and _md5((ordner / rel).read_text(encoding="utf-8")) == summe:
            (ordner / rel).unlink()
            meldungen.append(f"entfernt (nicht mehr erzeugt): {ordner / rel}")
    manifest_pfad.write_text(json.dumps(neu, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return meldungen
