---
artefakt: Mikrocontroller-Simulation (Wokwi)
titel: "<Titel der Steuerung>"
skill: wokwi-simulation-erstellen
skill_version: "1.0"
stand: <JJJJ-MM-TT>
bildungsgang: "<Bildungsgang>"
curriculare_vorgabe: "<Lernfeld bzw. Lerngebiet>"
dqr: <3|4|5>
status: "KI-Entwurf – fachlich zu prüfen"
bereich: planung
# vertraulich: true   bei Prüfungsaufgaben
---

# Wokwi-Simulation: <Titel>

<!-- `wokwi.py blatt` bzw. `alles` füllt alle Abschnitte aus Spec, Prüfung und Testlauf; danach Annahmen,
Prüfaufträge und Einsatz durchsehen. -->

## Aufgabe und Umfang
- **Aufgabe:** <Quelle, Teilaufgaben>
- **Simuliert:** Zuordnungsliste (<n> Eingänge, <m> Ausgänge); GRAFCET mit <k> Schritten; Zwangssteuerung (<…>); Verknüpfungen (<…>).
- **Plattform:** <Arduino Uno | ESP32> auf der E/A-Platine (Signal 1 = High-Pegel am Pin); Aktoren als LEDs, Analoggeber als Potentiometer.
- **Nicht simuliert:** Not-Halt und Schutzeinrichtungen (hardwaremäßig), Lastkreise, Motoren und Ventile selbst, Prellen der Kontakte.
- **Zeit:** <Echtzeit | Zeitraffer 1:60 für Zeiten ab 1 min; kürzere Zeiten in Echtzeit>.

## Projekt
| Datei | Inhalt |
|---|---|
| `48_wokwi_<kurztitel>.yaml` | Spec – Quelle aller Dateien |
| `48_wokwi_<kurztitel>/sketch.ino` | Programm: Zustandsautomat nach Notationsblatt |
| `48_wokwi_<kurztitel>/diagram.json` | Schaltung |
| `48_wokwi_<kurztitel>/wokwi.toml` | Wokwi in VS Code und wokwi-cli |
| `48_wokwi_<kurztitel>/szenarien/` | Testläufe für wokwi-cli |

## In Wokwi öffnen
1. <https://wokwi.com/projects/new/arduino-uno> öffnen.
2. `sketch.ino` und `diagram.json` in die gleichnamigen Reiter kopieren.
3. Simulation starten; der serielle Monitor zeigt Schritt, Signale, Analogwerte und Merker.

## Bedienung in der Simulation
| Kennzeichen | Betriebsmittel | Bauteil in Wokwi | Bedienung | Signal 1 bedeutet |
|---|---|---|---|---|
| -S1 | <Taster Start> | Taster (grün) an D2, gegen 5V, 10 kΩ nach GND | drücken = 1 | <Start betätigt> |

## Zuordnungsliste (<Plattform>)
| BMK | Betriebsmittel | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |
|---|---|---|---|---|
| -S1 | <Taster Start> | D2 | <Start betätigt> | NO |

## Ablauf im Programm
<GRAFCET in Textform (Schritt | Aktion | Transition zum Folgeschritt), Zwangssteuerung, Speicher, Verknüpfungen>

## Zeiten in der Simulation
| Zeit in der Aufgabe | in der Simulation |
|---|---|
| <5 min> | <5 s> |

## Testfälle und Ergebnis
| Nr. | Testfall | Prüfpunkte | Logik (Spec) | Programm (g++) | Wokwi-Szenario |
|---|---|---:|---|---|---|
| T1 | <Name> | <n> | ✅/❌ | ✅/❌/⚠️ | <Datei bzw. entfällt> |

## Zeitablauf
<Abbildung `abbildungen/48_wokwi_<kurztitel>_loesung_zeitablauf.svg` mit Bildunterschrift und Wertetabelle>

## Einsatz im Unterricht
- <Musterlösung prüfen, Inbetriebnahme üben, Fehlersuche>

## Qualitätscheck
| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Spec geprüft (`wokwi.py pruefen`) | ✅/⚠️/❌ | |
| Schaltung: Bauteile, Pins, Netze | ✅/⚠️/❌ | |
| Sketch übersetzt | ✅/⚠️/❌ | |
| Testfälle im Logikmodell und im Programm | ✅/⚠️/❌ | |
| Wokwi-Szenarien, Lauf im Browser | ⚠️ | |
| Zeichnungen als SVG aus Werten bzw. Spec | ✅/⚠️/❌ | |

## Annahmen und Prüfaufträge
- ⚠️ Annahme: <Auslegung der Funktionsbeschreibung, Plattform und Pins, Zeitraffer>
- 🔎 Prüfen: <Lauf in Wokwi, Rohwertbereich, Abgleich mit dem Erwartungshorizont>

## Übergabe
- Projektordner, Spec, Zuordnungsliste, GRAFCET-Textform, Testfälle
- Empfohlene nächste Skills: `programmieraufgabe-erstellen`, `unterrichtsmaterial-erstellen`, `technologieschema-erstellen`, `material-pruefen`

> KI-gestützt erstellt (Skill wokwi-simulation-erstellen v1.0). Fachliche Prüfung und Verantwortung: Lehrkraft.
