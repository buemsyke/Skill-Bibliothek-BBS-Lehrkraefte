# Wokwi – Formate, Bauteile, Fallen

Stand 11/2026. Quellen: docs.wokwi.com (Seiten *Diagram format*, *Automation scenarios*, *Project
configuration*, *Serial monitor*, Bauteilseiten), Board-Definition `wokwi-boards/boards/esp32-devkit-c-v4`,
Bauteilbibliothek `@wokwi/elements` 1.9.2 (Pinlage gemessen mit `wokwi.py vorschau`). Was hier nicht steht, ist
nicht geprüft – im Begleitblatt als `🔎 Prüfen`.

## 1. Projekt im Browser

1. `https://wokwi.com/projects/new/arduino-uno` bzw. `…/new/esp32` öffnen (ohne Konto möglich).
2. Inhalt von `sketch.ino` und `diagram.json` in die gleichnamigen Reiter kopieren (alles ersetzen).
3. Start. Der serielle Monitor öffnet sich (`serialMonitor.display: always`).

Speichern und Teilen braucht ein Wokwi-Konto. 🔎 Prüfen: Konten für Lernende nur nach den Regeln der Schule
(Datenschutz); für den Unterricht genügt das Kopieren ohne Konto.

**VS Code und wokwi-cli** brauchen eine gebaute Firmware (Wokwi übersetzt dort nicht):
`sketch.ino` nach `build/sketch/sketch.ino` kopieren, `arduino-cli compile --fqbn arduino:avr:uno --output-dir build
build/sketch` (ESP32: `esp32:esp32:esp32`), dann `wokwi.toml` (`firmware`, `elf`). Szenarien:
`wokwi-cli <Ordner> --scenario szenarien/<datei>.test.yaml --timeout <ms>`; Token in `WOKWI_CLI_TOKEN`.
🔎 Prüfen: beim ESP32 Firmwaredatei (`sketch.ino.bin` bzw. `.merged.bin`) nach der Wokwi-Doku der eingesetzten Version.

## 2. diagram.json

- Kopf: `version: 1`, `author`, `editor: "wokwi"`, `parts`, `connections`, optional `serialMonitor`, `dependencies`.
- Bauteil: `type`, `id` (eindeutig), `top`, `left` (px), `rotate` (Grad, um die Mitte), `attrs`.
- Verbindung: `[Quelle, Ziel, Farbe, Hinweise]`, Enden als `id:pin`. Hinweise `v<px>` senkrecht, `h<px>` waagrecht,
  höchstens ein `*` (davor ab Quelle, danach ab Ziel rückwärts). Der Generator legt alle Wegpunkte vor das Ziel,
  ohne `*`: die Leitung endet genau auf dem Ziel-Pin, Wokwi muss nichts ergänzen.
- ESP32 braucht `["esp:TX", "$serialMonitor:RX", "", []]` und `["esp:RX", "$serialMonitor:TX", "", []]`.

| Bauteil (`type`) | Pins | Attribute (Auswahl) | Szenario-Steuerung |
|---|---|---|---|
| `wokwi-arduino-uno` | `0` … `13`, `A0` … `A5`, `GND.1` (oben), `GND.2`, `GND.3`, `5V`, `VIN` | – | – |
| `board-esp32-devkit-c-v4` | GPIO als Zahl (`16`, `34`), `VP` (36), `VN` (39), `3V3`, `5V`, `GND.1` … `GND.3`, `TX`, `RX` | – | – |
| `wokwi-pushbutton` | `1.l`/`1.r` (verbunden), `2.l`/`2.r` (verbunden); Druck verbindet 1 mit 2 | `color`, `label`, `key`, `bounce: "0"` | `pressed` 0/1 |
| `wokwi-slide-switch` | `1` links, `2` Mitte, `3` rechts; links verbindet 1–2, rechts 3–2 | `value: "1"` = rechts, `bounce` | **keine** |
| `wokwi-potentiometer` | `GND`, `SIG`, `VCC` | `value` 0 … 1023 (Startstellung) | `position` 0,0 … 1,0 |
| `wokwi-led` | `A`, `C` | `color`, `label` | – |
| `wokwi-resistor` | `1`, `2` | `value` in Ω als Zahl („10000“) | – |
| `wokwi-text` | – | `text` (Zeilenumbruch `\n`); in der Doku ohne eigene Seite | – |

Uno: 3.3V, IOREF, AREF, RESET sind in der Simulation nicht verfügbar. Widerstände wirken als Pull-up und
Pull-down an Digitaleingängen; mit Potentiometern und analogen Sensoren rechnet Wokwi **nicht** (deshalb Poti
direkt am Analogeingang, Bürde nicht nachgebildet).

## 3. Schaltung des Generators (Uno)

- **Ausgänge** über dem Board in der Reihenfolge der Stiftleiste (13 … 8 von links): LED, darunter 220 Ω senkrecht,
  Leitung vom Pin über eine eigene Bahn; Katoden über eine gemeinsame Schiene zu `GND.1`. Beschriftung (Kennzeichen,
  Kurzname) als `wokwi-text` über der LED.
- **Eingänge** als Bedienfeld rechts: Signalleitung über eine Bahn über dem Board und einen Kanal links vom Feld;
  Versorgungsschienen rechts (VCC, GND), untere Bahnen zu `5V` und `GND.2`. Zeilen von oben nach unten in der
  Reihenfolge der Stiftleiste (kreuzungsfrei).
- **Analoggeber** unter dem Board, um 180° gedreht (Anschlüsse oben), Signal über eigene Bahnen zu `A0` … `A5`.
- Kreuzungen bleiben nur, wo zwei Versorgungsschienen sie erzwingen; alle Leitungen rechtwinklig.
- ESP32: einfache Anordnung ohne Wegpunkte (Wokwi zeichnet gerade Leitungen) – im Editor nachziehen (Lücke).

## 4. Szenarien (wokwi-cli)

```yaml
name: "T1 …"
version: 1
author: "wokwi-simulation-erstellen"
steps:
  - wait-serial: "Bereit"
  - set-control: {part-id: btn_s1, name: pressed, value: 1}
  - delay: 200ms
  - expect-pin: {part-id: uno, name: "8", value: 1}
```

- Schritte: `delay` (mit Einheit), `wait-serial`, `set-control`, `expect-pin`, `write-serial`, `take-screenshot`.
  `name` ersetzt seit wokwi-cli 0.22.1 die älteren Schlüssel `pin` bzw. `control`.
- Steuerbar sind Taster (`pressed`) und Potentiometer (`position`), **Schiebeschalter nicht**. Testfälle, die einen
  Schiebeschalter ändern oder abweichend starten, erzeugen kein Szenario (Protokoll: „entfällt“); sie laufen nur im
  Logikmodell und im g++-Lauf.
- Die Szenarien entstehen aus dem Lauf des Logikmodells (Zeitpunkte ab „Bereit“). Geprüft werden nur Ausgänge
  (`expect-pin`); Schritt und Merker prüfen Logikmodell und g++-Lauf.
- `wokwi.py wokwi` setzt `--timeout` auf die Summe der `delay` plus 30 s (🔎 Prüfen: Standardgrenze der eingesetzten wokwi-cli-Version).

## 5. Fallen

| Falle | Wirkung | Abhilfe im Skill |
|---|---|---|
| `kontakt: NO` ohne Anführungszeichen | YAML 1.1 liest `false`, der Taster würde zum Öffner | Anführungszeichen; Lader setzt `false` → NO |
| Prellen | Taster und Schalter prellen in Wokwi | `bounce: "0"` (Entprellen ist nicht Teil der Aufgabe) |
| Serielle Ausgabe | `Serial.print` wartet, wenn der Puffer voll ist (115 200 Bd ≈ 13 ms je Zeile) | Ausgänge vor der Meldung schreiben; Prüfung 50 ms nach einer Aktion |
| Zeiten von Stunden | in Echtzeit nicht beobachtbar | Zeitraffer ab einer Schwelle; Verriegelungszeiten in Echtzeit |
| Zeitraffer vertauscht Reihenfolge | 59 s bleibt 59 s, 2 min werden 2 s | `pruefen` warnt |
| Analogwert genau auf der Schwelle | Rohwert gerundet, Ergebnis zufällig | Testwerte neben die Schwelle legen |
| Startwert unter einer Schutzschwelle | Speicher setzt schon beim Start | Startwerte im Normalbereich wählen |
| Startwert in `diagram.json` ≠ Testfall | Wokwi beginnt mit dem Wert aus `diagram.json` | Poti im Szenario sofort setzen; Schiebeschalter → kein Szenario |
| Pinname falsch (`2` statt `2.l`) | Leitung ohne Wirkung, keine Fehlermeldung im Editor | `pruefen` (Prüftabelle) und `vorschau` (echte Bauteile) |

## 6. Lücken (Stand 1.0)

- Parallelverzweigungen im GRAFCET, Makroschritte, Teil-GRAFCET (nur Zwangssteuerung in die Grundstellung bzw. einen
  Schritt).
- Zeitbedingungen an Signalen (`3s/-BG1`) – als Schritt mit Zeit oder über einen Merker lösen.
- Plattformen Raspberry Pi Pico (MicroPython) und STM32; LCD, Relaismodule, Motoren und Servos als Aktoren.
- Leitungsführung für den ESP32.
