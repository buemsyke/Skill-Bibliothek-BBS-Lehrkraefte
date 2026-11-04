---
name: wokwi-simulation-erstellen
description: Setzt eine Steuerungsaufgabe (Funktionsbeschreibung, Zuordnungsliste, GRAFCET, Logikplan) vollständig als Wokwi-Simulation für Arduino Uno oder ESP32 um – Sketch als Zustandsautomat nach dem Notationsblatt, Schaltung mit Tastern, Schaltern, Potentiometern und LEDs (diagram.json), Testszenarien für wokwi-cli. Prüft die Umsetzung automatisch mit Testfällen aus der Funktionsbeschreibung, im Logikmodell und im übersetzten Sketch (g++), zeichnet den Zeitablauf und schreibt ein Begleitblatt mit Bedienung und Testergebnis. Verwenden bei „Wokwi Simulation", „Steuerung in Wokwi simulieren", „GRAFCET auf Arduino testen", „Ablaufsteuerung Mikrocontroller simulieren", „Musterlösung Steuerungsaufgabe prüfen", „Schrittkette ESP32". Nicht für Analogschaltungen mit Messgeräten (circuitjs-schaltung-erstellen) und nicht für GRAFCET- oder Schaltplanzeichnungen (technologieschema-erstellen).
metadata:
  version: "1.0"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Wokwi-Simulation erstellen

## Zweck
Eine Steuerungsaufgabe wird **vollständig und nachprüfbar** im Simulator Wokwi lauffähig: Programm,
Schaltung und Testläufe entstehen aus einer **Spec**, die die Aufgabe in der Schreibweise des
Notationsblatts abbildet (Zuordnungsliste, GRAFCET in Textform, Zwangssteuerung, Verknüpfungen,
Testfälle). Frei geschriebene Sketche und Schaltungen scheitern an Kleinigkeiten (Öffner nicht
beachtet, Zeit am falschen Schritt, Pinname falsch, Poti am falschen Pin). Deshalb erzeugt ein Skript
alles aus der Spec und prüft es zweifach: im **Logikmodell** der Spec und im **übersetzten Sketch**
(g++ mit nachgebildetem Arduino-Kern). So zeigt die Simulation, ob eine Musterlösung tut, was die
Funktionsbeschreibung verlangt.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen · einheitlicher Kopf und Pflichtabschnitte
(Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis) im Begleitblatt. Details:
`references/skill-vertrag.md`. Der Skill ruft keinen anderen Skill selbst auf.
**Zeichnungen** nur als SVG aus den Zeichen-Skills bzw. aus Werten per Code, nie als ASCII-Art oder
Mermaid (Skill-Vertrag Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht (sonst Rückfrage):** die Steuerungsaufgabe – Funktionsbeschreibung oder Material mit
  Zuordnungsliste und GRAFCET bzw. Logikplan (Schüler- und Lehrermaterial, Erwartungshorizont).
- **Wichtig, sonst Annahme:** Plattform (Standard Arduino Uno; ESP32), Pins (Standard: E/A-Platine,
  Reihenfolge der Zuordnungsliste), Lösung für GRAFCET und Verknüpfungen (aus dem Lehrermaterial,
  sonst selbst entwickeln und als Annahme kennzeichnen), Zeitraffer bei Zeiten über einigen Minuten.
- **Optional:** Kurznamen für die Beschriftung, Startwerte der Analoggeber, Bildungsgang und Vorgabe
  für den Kopf, Einsatzideen.

## Vorgehen
1. **Aufgabe lesen:** Funktionsbeschreibung, Zuordnungsliste, Notation (`references/notation-steuerungstechnik.md`),
   Plattformdaten (`references/normen-technik.md`, Abschn. 4). Unklare Stellen der Funktionsbeschreibung
   (Ende einer Störmeldung, Gültigkeit einer Schutzfunktion in allen Schritten, Startsperren) notieren –
   sie werden Annahmen.
2. **Gerüst erzeugen:** `python3 scripts/wokwi.py entwurf <Material.md> --plattform arduino-uno -o 48_wokwi_<kurztitel>.yaml`
   übernimmt Zuordnungsliste (Pins der E/A-Platine in Reihenfolge) und GRAFCET-Textform. Ohne Tabellen die
   Spec nach `references/spec-format.md` selbst schreiben.
3. **Spec vervollständigen** (`references/spec-format.md`): Titel, Kurznamen, Startwerte; **Zwangssteuerung**
   für Stopp und Schutzfunktionen (Schrittkette in die Grundstellung), **Speicher** (Störmeldung,
   Neustartsperre mit Hysterese), **Verknüpfungen** (Freigaben aus dem Logikplan, Aktion auf einen Merker
   wie `M_Pumpe`), Annahmen, Prüfaufträge.
4. **Testfälle aus der Funktionsbeschreibung** (Abschn. 6 der Spec-Referenz): Grundstellung, Normalablauf
   mit **jeder** Zeit (`schrittzeit` mit `vorher` und `erwarte`), jede Verzweigung, Stopp in einem
   laufenden Schritt, **jede** Schutzfunktion mit Neustart, Startsperren. Erwartungen aus dem Text
   ableiten, nicht aus dem Programm.
5. **Prüfen:** `python3 scripts/wokwi.py pruefen 48_wokwi_<kurztitel>.yaml` – jedes ❌ beheben, Hinweise
   begründen.
6. **Alles erzeugen und testen:** `python3 scripts/wokwi.py alles 48_wokwi_<kurztitel>.yaml` – Projektordner,
   Testlauf (Logik und Programm), Zeitablauf-SVG, Begleitblatt. Ein ❌ im Testfall heißt: Spec und
   Funktionsbeschreibung vergleichen; erst klären, ob der **Test** oder die **Lösung** falsch ist, dann
   ändern – nie den Test an ein falsches Programm anpassen.
7. **Vorschau:** `python3 scripts/wokwi.py vorschau 48_wokwi_<kurztitel>.yaml --png <Datei>` setzt die Bauteile
   mit der echten Wokwi-Bibliothek, prüft jeden Pinnamen und zeigt das Layout (Chromium und Netz nötig;
   sonst `🔎 Prüfen: Vorschau nicht erstellt`). Bild nur zur Sichtprüfung, nicht ins Material.
8. **Begleitblatt durchsehen:** Annahmen, Prüfaufträge und Einsatz ergänzen; Kopf (Bildungsgang, Vorgabe)
   aus der Planungsakte. Optional mit wokwi-cli: `python3 scripts/wokwi.py wokwi <Ordner>`.

## Regeln
- **Spec ist die Quelle.** Sketch, Schaltung und Szenarien nie von Hand ändern, sondern die Spec und neu
  erzeugen. Von Hand geänderte Dateien überschreibt `erzeugen` nicht (Prüfsumme in `.wokwi-erzeugt.json`).
- **Signale wie auf der E/A-Platine:** Signal 1 = High-Pegel am Pin, Spalte „Signal 1 bedeutet“ gilt.
  Schließer-Taster gegen VCC mit 10 kΩ nach GND, Öffnerverhalten als Taster gegen GND mit 10 kΩ nach VCC
  (unbetätigt 1), dauerhafte Signale (Schwimmer-, Endschalter) als Schiebeschalter (rechts = 1).
  `kontakt: "NO"` in Anführungszeichen (YAML liest NO sonst als falsch; das Skript fängt es ab).
- **GRAFCET-Treue:** ein aktiver Schritt, höchstens ein Schrittwechsel je Zyklus, Zeit nur am eigenen Schritt
  (`5min/X1` an der Transition aus X1), Aktionen kontinuierlich oder speichernd – nie beides auf
  dieselbe Variable. Ein Ausgang kommt **entweder** aus Aktionen **oder** aus einer Verknüpfung.
  Parallelverzweigungen simuliert der Skill nicht (Lücke).
- **Stopp und Schutz** als Zwangssteuerung (DIN EN 60848: Erzwingen), Speicher rücksetzdominant (Stopp vor
  Start). Der Not-Halt bleibt hardwaremäßig gelöst und wird nicht simuliert.
- **Zeitraffer** nur für die Simulation: Zeiten ab der Schwelle (Standard 1 min) laufen 1:Faktor, kürzere in
  Echtzeit, damit Verriegelungszeiten (3 s) sichtbar bleiben. Im Sketch stehen die Zeiten in Aufgabenzeit;
  im Begleitblatt Tabelle Aufgabe → Simulation.
- **Farben** der Bedienteile nach DIN EN 60204-1 (Start nicht rot, Stopp nicht grün), Leuchtmelder nach
  Bedeutung (Störung rot, Betrieb grün); Aktoren als orange LEDs.
- **Lösung bleibt Lehrermaterial:** Sketch, Begleitblatt und Zeitablauf enthalten die Lösung; Dateinamen der
  Abbildung mit `_loesung`. Bei Prüfungsaufgaben `vertraulich: true` in der Spec (Kopf des Begleitblatts).
  Was Lernende sehen (Beschriftungen, serieller Monitor, Aufgabenblatt), folgt `references/schuelermaterial.md`.
- **Nichts erfinden:** Wokwi-Bauteile, Pins und Formate stehen in `references/wokwi-format.md` mit Quelle;
  alles andere als `🔎 Prüfen`. Wokwi im Browser hat dieser Skill nicht bedient – der Lauf dort bleibt
  Prüfauftrag, bis die Lehrkraft ihn bestätigt oder wokwi-cli die Szenarien ausgeführt hat.

## Ausgabe
Im Ordner der Planungsakte bzw. neben dem Material:
- `48_wokwi_<kurztitel>.yaml` – Spec (Quelle)
- `48_wokwi_<kurztitel>/` – `sketch.ino`, `diagram.json`, `wokwi.toml`, `szenarien/*.test.yaml`
- `48_wokwi_<kurztitel>_begleitblatt.md` – Begleitblatt nach `assets/vorlage-simulationsblatt.md`
- `abbildungen/48_wokwi_<kurztitel>_loesung_zeitablauf.svg` – Zustandsfolge eines Testfalls (aus Werten)

## Qualitätscheck
- [ ] Spec aus der Aufgabe, Unklarheiten als Annahme, `wokwi.py pruefen` ohne ❌?
- [ ] Jede Zeit, jede Verzweigung, Stopp und jede Schutzfunktion durch einen Testfall abgedeckt?
- [ ] Testfälle im Logikmodell **und** im Programm bestanden (oder Prüfauftrag „nicht getestet“)?
- [ ] Erwartungen aus der Funktionsbeschreibung, nicht aus dem Programm abgeleitet?
- [ ] Schaltung: alle Pins vorhanden (`vorschau` bzw. Prüftabelle), Leitungen rechtwinklig, Beschriftungen lesbar?
- [ ] Zeitraffer begründet, Zeiten-Tabelle im Begleitblatt, `ZEITRAFFER = 1` für die Anlage genannt?
- [ ] Begleitblatt mit Bedienung, Zuordnungsliste, Ablauf, Testergebnis, Annahmen, Prüfaufträgen;
      keine Zeichnung aus Zeichen (`python3 scripts/zeichnungen_pruefen.py 48_*.md` ohne ❌)?
- [ ] Lösung nur im Lehrermaterial, vertrauliche Aufgaben gekennzeichnet?

## Beispielaufrufe
> „Setz die Steuerungsaufgabe 2 aus dem Abiturvorschlag Biogas in Wokwi um und prüf die Musterlösung.“

> „Ich brauche die Sortieranlage aus LF 7 als Wokwi-Simulation auf dem ESP32.“

> „Teste meinen GRAFCET der Tankfüllung mit Wokwi – Start, Füllen bis 80 %, Stopp und Überlauf.“

## Referenzen – wann lesen
- `references/spec-format.md` – **immer** (Aufbau der Spec, Bedingungen, Testfälle, Beispiel).
- `references/wokwi-format.md` – **immer**, wenn Wokwi geöffnet, die Schaltung geändert oder ein Fehler gesucht
  wird (Bauteile, Pins, Szenarien, Fallen, Lücken).
- `references/notation-steuerungstechnik.md` – Schreibweise von Kennzeichen, Bedingungen und Programm.
- `references/normen-technik.md` – Abschn. 3 (GRAFCET) und 4 (Mikrocontroller, Analogwerte je Plattform).
- `assets/vorlage-simulationsblatt.md` – Aufbau des Begleitblatts.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/wokwi.py` – Befehle `entwurf`, `pruefen`, `erzeugen`, `testen`, `blatt`, `vorschau`, `wokwi`, `alles`;
  Module `scripts/wokwi_spec.py` (Spec, Bedingungen, Prüfung), `scripts/wokwi_projekt.py` (Sketch, Schaltung,
  Szenarien), `scripts/wokwi_sim.py` (Logikmodell, g++-Lauf, Protokoll, Zeitablauf), `scripts/wokwi_blatt.py`
  (Begleitblatt), `scripts/wokwi_vorschau.py` (Vorschau mit @wokwi/elements).

## Empfohlene Folge-Skills
`programmieraufgabe-erstellen` (Programmierauftrag zur Steuerung mit Erwartungshorizont),
`unterrichtsmaterial-erstellen` (Arbeitsblatt zur Inbetriebnahme oder Fehlersuche), `technologieschema-erstellen`
(GRAFCET und Logikplan als SVG), `material-pruefen`.
