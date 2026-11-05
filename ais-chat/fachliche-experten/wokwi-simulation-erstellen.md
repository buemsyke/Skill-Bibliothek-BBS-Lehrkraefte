<!-- Assistenten-Fassung des Skills 'wokwi-simulation-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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

# ANHÄNGE

## Anhang: assets/vorlage-simulationsblatt.md

---
artefakt: Mikrocontroller-Simulation (Wokwi)
titel: "<Titel der Steuerung>"
skill: wokwi-simulation-erstellen
skill_version: "1.2"
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
| -SJ1 | <Taster Start> | Taster (grün) an D2, gegen 5V, 10 kΩ nach GND | drücken = 1 | <Start betätigt> |

## Zuordnungsliste (<Plattform>)
| BMK | Betriebsmittel | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |
|---|---|---|---|---|
| -SJ1 | <Taster Start> | D2 | <Start betätigt> | NO |

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

> KI-gestützt erstellt (Skill wokwi-simulation-erstellen v1.2). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: references/normen-technik.md

# Normen für Prüfungsaufgaben Technik (Informationstechnik, Mechatronik)

**Wozu:** Was eine Lösung festlegt, folgt einer Norm oder der Notation des Unterrichts. Diese
Referenz fasst zusammen, was Aufgaben, Musterlösungen und Bewertungsmerkmale in den Lerngebieten
*Technische Prozesse steuern* (IT1, METRO 2, ET2), *Netzwerke* (IT2), *Messwerte erfassen* (IT4,
METRO 3), Software (IT3, IT5) und Antriebe (METRO 5) aus den Normen brauchen. Normtexte sind nicht
frei zugänglich: Die Angaben sind in eigenen Worten nach Leseproben, Merkblättern der PAL und
Sekundärquellen zusammengefasst (Abschn. 11, Stand der Recherche 2026-10). Unsicheres ist mit 🔎
markiert – vor der Einreichung mit dem Normtext oder dem eingeführten Tabellenbuch abgleichen.

**Einheitliche Schreibweise:** Wo die Normen Spielraum lassen (Tiefe der Kennbuchstaben, getippte
Negation, Zeitschreibweise, Zuordnungsliste, GRAFCET in Textform, Bezeichner im Programm), legt das
**Notationsblatt** `notation-steuerungstechnik.md` eine Form fest; es geht als Anlage ins
Schülermaterial.

## Inhalt
1. Grundregeln für Aufgaben
2. Referenzkennzeichen – DIN EN IEC 81346-1 und -2
3. GRAFCET – DIN EN 60848
4. Steuerungsprogramme – IEC 61131-3 und Mikrocontroller
5. Schaltpläne, Schaltzeichen, Anschlussbezeichnungen
6. Sicherheit an Maschinen – Bedienteile, Farben, Stopp, Not-Halt
7. Sensorik, Einheitssignale, Regelungstechnik
8. Netzwerke
9. Software – UML, Struktogramm, Programmablaufplan
10. Größen, Einheiten, Schreibweise
11. Quellen

---

## 1. Grundregeln für Aufgaben

1. **Norm und Ausgabe nennen**, wo eine Notation bewertet wird – im Schülermaterial (Hinweise oder
   Teilaufgabe): „Die Betriebsmittel sind nach DIN EN IEC 81346-2:2020 gekennzeichnet.“, „Entwickeln
   Sie einen GRAFCET nach DIN EN 60848.“ `bmk_pruefen.py` liest die genannte Ausgabe (T.8).
2. **Eine Notation je Vorschlag.** Weicht der Unterricht ab (ältere Ausgabe, Hauskonvention,
   Herstellernotation), gilt sie für Aufgabe, Anlagen und Musterlösung gleichermaßen; im
   Schülermaterial nennen, im Begleitblatt begründen. Nie mischen.
3. **„Normgerecht“ im Merkmal auflösen.** Das Lehrermaterial nennt die Normelemente, die zählen
   (z. B. „Initialschritt doppelt umrandet, Rücksprung mit Pfeil, Transitionen mit Bedingung“) –
   eigenes Merkmal mit 1–2 BE, getrennt von der Funktion.
4. **Tabellenbuch beachten.** Ältere Ausgaben (etwa vor 2021 🔎) zeigen Kennbuchstaben der
   Ausgabe 2009. Steht die Lösung nur im Tabellenbuch, den benutzten Stand im Erwartungshorizont
   angeben.
5. **Was nicht genormt ist** – Technologieschema, Zuordnungsliste, Pseudocode – legt die Aufgabe
   selbst fest (Legende, Tabellenkopf mit Beispielzeile, Hilfsmitteldokument).

## 2. Referenzkennzeichen – DIN EN IEC 81346-1 und -2

**Ausgaben**

| Teil | gültige Ausgabe | Inhalt |
|---|---|---|
| Teil 1 | DIN EN IEC 81346-1:2024-07 (IEC 81346-1:2022) | Strukturierung, Aspekte und Vorzeichen |
| Teil 2 | **DIN EN IEC 81346-2:2020-10** (IEC 81346-2:2019) | Klassen und Kennbuchstaben |
| Teil 2, Vorgänger | DIN EN 81346-2:2010-05 (IEC 81346-2:2009) | zurückgezogen; danach noch die zentralen Mechatronik-Prüfungen in Niedersachsen 2020–2026 (z. B. -SF elektrischer Taster, -SJ pneumatischer Taster, -RZ, -AZ) |

Die PAL setzt die Ausgabe 2020 in den IHK-Prüfungen um (Merkblatt Stand Juni 2024). Für neue
Vorschläge gilt **die Ausgabe 2020**; die Ausgabe 2009 nur, wenn der Unterricht sie verwendet – dann
im Schülermaterial nennen (Abschn. 1).

**Aufbau eines Kennzeichens:** Vorzeichen, Kennbuchstaben, Zählnummer, ohne Leerzeichen: `-SJ1`,
`-BT2`, `-QA1`.
- Vorzeichen (Teil 1): `-` Produkt (in Aufgaben üblich), `=` Funktion, `+` Ort, `%` Typ (neu seit
  2022), `#` andere Aspekte. Kombinationen wie `+S1-K1` nur, wenn im Unterricht eingeführt.
- **Ein bis drei Kennbuchstaben** (Teil 2): Klasse (`-B1`), Unterklasse (`-BG1`), Unter-Unterklasse
  (`-BGB1`). Die Norm lässt jede Tiefe zu; die PAL zeigt Schaltpläne nur mit Klassen und mit
  Unterklassen.
- **Klasse und Unterklasse sind Standard** (Vorgabe der Fachberatung, 04.11.2026; ersetzt die
  Festlegung „so kurz wie möglich“ vom 31.10.2026): Jedes Betriebsmittel trägt **zwei Kennbuchstaben** –
  **-SJ1** (Taster), **-MA1** (Elektromotor), **-MM1** (Zylinder), **-EA1** (Leuchte), **-QA1** (Schütz),
  **-KE1** (SPS), **-PF1** (Leuchtmelder). Die Klasse allein (-S1, -M1) wird nicht verwendet, auch nicht,
  wenn eine Klasse nur eine Art Betriebsmittel enthält. Das gilt in **allen Dokumentationsformen**:
  Funktionsbeschreibung, Technologieschema mit Legende, Zuordnungsliste, GRAFCET, Logikplan, Programm,
  Musterlösung. Die dritte Ebene (-BGB1) nur, wenn der Unterricht sie verlangt – dann für alle
  Kennzeichen dieser Klasse (nicht -BG1 neben -BGB2). `bmk_pruefen.py` (T.8) und
  `edu-technologieschema pruefen` melden fehlende Unterklassen und gemischte Tiefe.
- Beispiel Bewässerung: Taster -SJ1, -SJ2; Schütz -QA1; SPS -KE1; Leuchtmelder -PF1, -PF2; Sensoren für
  Füllstand, Bodenfeuchte und Temperatur -BL1, -BM1, -BM2, -BT1; Pumpenmotor -MA1; Magnetventile -MB1,
  -MB2.
- Die Unterklasse macht sichtbar, welche Ausgabe gilt: -SF/-SJ, -KF/-KE, -RZ/-RN unterscheiden sich
  zwischen 2009 und 2020 (Tabelle unten). Neue Aufgaben verwenden die Unterklassen der Ausgabe 2020.
- **A, I und O** sind keine Klassen; **D, J, L, V, Y, Z** sind reserviert. Eine Klasse „Sonstiges“
  gibt es nicht: Passt keine Unterklasse genau, die nächstpassende aus Tabelle 2 wählen und die Aufgabe
  des Betriebsmittels in der Legende nennen.
- Klassifiziert wird nach der **inhärenten Funktion** – was das Objekt erfasst oder bewirkt, nicht
  nach Bauart oder Einbauort: Der Druckschalter am Zylinder ist -BP, der Endlagenschalter daneben
  -BG. Bei mehrdeutigen Fällen die Aufgabe des Betriebsmittels in der Legende nennen.
- Die Zählnummer zählt je Kennbuchstaben: -BG1, -BG2, -BP1.

**Klassen** (Übersicht; im Kennzeichen steht immer zusätzlich die Unterklasse)

| BMK | Klasse | typische Betriebsmittel |
|---|---|---|
| -B | Information erfassen | Sensoren und Geber: Näherungs-, End-, Druck-, Schwimmerschalter, Temperaturfühler |
| -S | menschliche Betätigung erfassen | Taster, Schalter, Wahl- und Schlüsselschalter, handbetätigtes Ventil |
| -K | Signale verarbeiten | SPS, Kleinsteuerung, Mikrocontroller, Relais, Zeitrelais, pneumatisches UND/ODER |
| -Q | Fluss steuern | Schütz, Leistungs- und Motorschutzschalter, Wegeventil |
| -M | Antreiben | Motor, Ventilspule, Elektromagnet, Zylinder |
| -P | Information darstellen | Leuchtmelder, Hupe, Anzeige, Manometer |
| -R | Begrenzen | Drossel- und Drosselrückschlagventil, Rückschlagventil, Widerstand, Diode |
| -G | Fluss erzeugen | Pumpe, Kompressor, Lüfter, Generator; Wartungseinheit (PAL) 🔎 |
| -T | Umwandeln | Netzteil, Frequenzumrichter, Messumformer |
| -F | Schützen | Sicherung, Leitungsschutzschalter, thermisches Überlastrelais |
| -E | Aussenden | Leuchte, Heizung |
| -X, -W | Verbinden, Leiten | Klemme, Steckdose, Patchfeld; Kabel, Leitung |
| -C | Speichern | Kondensator, Akku, Tank |

**Unterklassen – Standard in Aufgaben** (Auswahl der
Ausgabe 2020; deutsche Benennungen sinngemäß; in Klammern Beispiele der dritten Ebene)

| BMK | Bedeutung | typische Betriebsmittel | Ausgabe 2009 |
|---|---|---|---|
| **B** | **Information erfassen** | | |
| -BG | Lage, Abstand, Winkel | Näherungsschalter (induktiv, kapazitiv, optisch), Endlagen-/Positionsschalter (BGB), Zylinderschalter, Abstandssensor (BGC), Drehgeber/Winkel (BGE) | gleich |
| -BP | **Druck** | Druckschalter (BPB), Drucktransmitter (BPA), Differenzdruck (BPC, BPD), Vakuumschalter | gleich |
| -BM | **Feuchte** | Feuchtesensor (BMA), Hygrostat (BMB); Bodenfeuchte 🔎 (2009: „Wassergehalt, Feuchte“) | gleich |
| -BT | Temperatur | Pt100, Thermoelement (BTA), Thermostat/Temperaturschalter (BTB) | gleich |
| -BL | Füllstand | Schwimmerschalter (BLB), Füllstandsensor (BLA) | gleich |
| -BF | Durchfluss | Durchflusssensor, Strömungswächter | gleich |
| -BS | Drehzahl, Geschwindigkeit, Beschleunigung | Tachogenerator, Drehzahlwächter, Beschleunigungssensor | gleich |
| -BW | Kraft, Gewicht, Drehmoment | Wägezelle, DMS-Kraftaufnehmer, Drehmomentsensor | gleich |
| -BR | Strahlung, Licht | Lichtsensor, Lichtschranke/Lichtgitter, Fotozelle, IR- und UV-Sensor | gleich |
| -BQ | Stoffkonzentration | Gas-, Rauch-, CO₂-, Trübungssensor | gleich |
| -BA / -BC | elektrische Spannung / Strom | Spannungs-, Stromwandler, Überlastrelais (elektronisch, BC) | 🔎 |
| -BE | elektrisches oder magnetisches Feld | Reedkontakt, Magnetfeldsensor | 🔎 |
| -BJ / -BH | Leistung / Energie | Leistungsmesser, Energiezähler | 🔎 |
| -BK | Zeit | Uhr, Zeitschaltuhr | 🔎 |
| -BX | Bild und Ton | Kamera, Mikrofon | 🔎 |
| -BY | gespeicherte Information | RFID-, Barcode-, Kartenleser | 🔎 |
| -BZ | Ereignisse, Anzahl | Zähler, Präsenz- und Personenmelder | 🔎 |
| **S** | **menschliche Betätigung erfassen** | | |
| -SJ | Fingerbetätigung | **Drucktaster (SJB)**, Kippschalter (SJA), Touch-Taster (SJC); handbetätigte Ventile | **-SF** (elektrisch); -SJ war nur das handbetätigte Ventil |
| -SG | Handbetätigung | Drehknopf/Knebel (SGA), Handhebel, Schlüsselschalter (SGF) | 🔎 |
| -SH | Fußbetätigung | Fußschalter, Pedal | 🔎 |
| -SK | Bewegung | Joystick, Maus | 🔎 |
| -SF | Gesichtserkennung | (in Prüfungsaufgaben kaum) | **Taster, Schalter elektrisch** |
| **K** | **Signale verarbeiten** | | |
| -KE | elektrische Signale verarbeiten | **SPS, Kleinsteuerung, Mikrocontroller (KEB)**, PC (KEA), E/A- und Kommunikationsbaugruppe (KEC), Router, Firewall (KED) | -KF 🔎 |
| -KF | elektrische Signale weiterleiten | Relais, Hilfsschütz (KFA), Zeitrelais (KFB), Repeater, Netzwerk-Switch (KFE) | gleich (2009 auch SPS) |
| -KH | fluidische Signale verarbeiten | Zweidruck- und Wechselventil (UND/ODER), Vorsteuerventil (KHB) | gleich |
| **M** | **Antreiben** | | |
| -MA | elektromagnetisch, drehend | Elektromotor (MAA), Schrittmotor (MAB) | gleich |
| -MB | elektromagnetisch, linear | **Ventilspule, Elektromagnet (MBB)**, Linearmotor (MBA) | gleich |
| -MM | fluidisch | Pneumatik-/Hydraulikzylinder (MMB/MMA), Druckluft-/Hydraulikmotor | gleich |
| **P** | **Information darstellen** | | |
| -PF | Zustand sichtbar | Leuchtmelder, Signalleuchte (PFA), Stellungsanzeige | gleich |
| -PG | Wert anzeigen | Manometer (PGP), Thermometer (PGT), Volt-/Amperemeter, Zähleranzeige | gleich |
| -PH | grafisch anzeigen | Display, Bildschirm | 🔎 |
| -PJ | akustisch | Hupe (PJB), Summer, Klingel, Lautsprecher | gleich |
| **Q** | **Fluss steuern** | | |
| -QA | elektrische Energie schalten | **Schütz (QAA)**, Leistungs- und Motorschutzschalter (QAB), Halbleiterschalter/SSR (QAC) | gleich |
| -QB | elektrisch trennen | Lasttrennschalter, Hauptschalter (QBA) 🔎 (PAL nennt den Hauptschalter unter QA) | gleich |
| -QM | Fluid schalten (geschlossen) | **Wegeventil**, Absperr-, Schnellentlüftungsventil | gleich |
| -QN | Fluid stetig verstellen | Proportional-, Stellventil | 🔎 |
| **R** | **Begrenzen, stabilisieren** | | |
| -RA | elektrisch begrenzen | Diode (RAA), Widerstand (RAC), Drossel (RAB) | gleich |
| -RM | Rückfluss sperren | Rückschlagventil (RMA) | gleich |
| -RN | Durchfluss begrenzen | **Drosselventil, Drosselrückschlagventil**, Stromregelventil | **-RZ** für das Drosselrückschlagventil (-RN war nur die Drossel) |
| **G** | **Fluss erzeugen** | | |
| -GQ | Gasstrom | Kompressor (GQA), Lüfter (GQB); Wartungseinheit: Klasse G laut PAL 🔎 | 2009: Wartungseinheit oft -AZ (Klasse A entfällt) |
| -GP | Flüssigkeitsstrom | Pumpe (GPA Verdränger-, GPB Kreiselpumpe) | gleich |
| -GA / -GB | Generator / Batterie (Primärzelle) | Generator, Batterie; Akku: -CC | 🔎 |
| **T** | **Umwandeln** | | |
| -TA | Energie, gleiche Stromart | Transformator (TAA), Frequenzumrichter (TAC) | 🔎 |
| -TB | AC ↔ DC | Gleichrichter (TBA), Wechselrichter (TBB) | gleich |
| -TC | Stromversorgung | Netzteil 24 V DC (TCB) | 🔎 |
| -TF | Signal umwandeln | Messumformer (TFC), Verstärker (TFA) | gleich |
| **E, F, C, W, X** | | | |
| -EA / -EB | Licht / elektrische Heizung | Leuchte, Lampe / Heizstab, Heizkabel | gleich |
| -FC | Überstrom schützen | Sicherung (FCA), Leitungsschutzschalter (FCB), Bimetall-Überlastrelais (FCC) | gleich |
| -FB | Fehlerstrom schützen | Fehlerstrom-Schutzschalter (RCD) 🔎 | gleich |
| -CA / -CC / -CM | speichern | Kondensator / Akku / Tank, Behälter | 🔎 |
| -WD / -WG / -WH | leiten | Energiekabel / Signal-, Datenleitung (WGB) / Lichtwellenleiter | gleich |
| -XD / -XG | verbinden | Klemme, Steckdose / Signalklemme, Anschlussdose, Patchfeld (XGC) | gleich |

„gleich“ heißt: Kennbuchstabe und Bedeutung decken sich in Prüfungsaufgaben; die Unterklassen der
Ausgabe 2009 sind nur teilweise belegt (🔎). Belegte Änderungen 2009 → 2020: Taster -SF → **-SJ**,
Drosselrückschlagventil -RZ → **-RN**, Klasse A (z. B. -AZ) entfällt, SPS -KF → **-KE** 🔎.

**Für die Aufgabe**
- Je Betriebsmittel Klasse **und** Unterklasse aus der Tabelle festlegen (inhärente Funktion). Ein
  nicht aufgeführter Code wird mit Tabelle 2 der Norm geprüft.
- Legende: BMK | Betriebsmittel | Lage bzw. Aufgabe (T.3); bei mehrdeutigen Fällen (Lichtschranke
  als Objektmelder: -BR oder -BG) die Aufgabe des Betriebsmittels nennen.
- In Netzplänen sind Gerätenamen wie „SW1“, „R1“ üblich; Referenzkennzeichen (-KFE, -KED) nur, wenn
  eingeführt.
- Fluidtechnik: Die Kennzeichnung nach ISO 1219-2 (z. B. „1V1“, „1A1“) ist eine andere Systematik –
  nicht mit -QM1/-MM1 mischen.

## 3. GRAFCET – DIN EN 60848

**Ausgabe:** DIN EN 60848:2014-12 (IEC 60848:2013, 3. Ausgabe; keine neuere bekannt). GRAFCET ist
eine **herstellerunabhängige Spezifikation** des Ablaufs; die Ablaufsprache (AS) der IEC 61131-3 und
Herstellersprachen (z. B. S7-GRAPH) sind Programmiersprachen. Im Auftrag unterscheiden:
„Entwickeln Sie einen GRAFCET“ ≠ „Programmieren Sie die Schrittkette in AS“. Weil GRAFCET nichts über
die Plattform sagt, ist er die gemeinsame Spezifikation für SPS, Kleinsteuerung und Mikrocontroller.
Festlegungen der Bibliothek (Notationsblatt): Initialschritt 0, getippte Negation „¬“, Zeit „5s/X3“
ohne Leerzeichen, Analogbedingungen mit physikalischem Wert und Einheit („[-BT1 > −16 °C]“), Textform
als Tabelle Schritt | Aktion | Transition zum Folgeschritt (`bmk_pruefen.py`, T.9).

| Element | Darstellung und Regel |
|---|---|
| Schritt | Quadrat mit Name (Zahl, auch 9a); Schrittvariable **X** + Name (X3) ist 1, solange der Schritt aktiv ist |
| Initialschritt | **doppelt umrandet**; aktiv beim Start ohne Bedingung; entspricht der Grundstellung |
| Transition | Querstrich auf der Wirkverbindung, **Bedingung rechts**, optional Name links in Klammern „(T3)“; Quelltransition ohne Verbindung nach oben, Schlusstransition ohne Verbindung nach unten |
| Wirkverbindung | Schritt und Transition wechseln sich ab; von oben nach unten ohne Pfeil, **aufwärts mit Pfeil** (Rücksprung) |
| Logik | UND „·“ (auch „*“), ODER „+“, NICHT als Überstrich; UND vor ODER, sonst Klammern; „1“ unterstrichen = immer erfüllt (Aufgaben schreiben es auch ohne Strich) |
| Flanke | ↑a steigend, ↓a fallend (Pfeil vor der Variablen) |
| Zeit | „t1/Variable/t2“, meist „5s/X3“ = 5 s nach Aktivierung von Schritt 3; „3s/-BG1“ = -BG1 seit 3 s ununterbrochen 1 |
| Vergleich | Bedingungen aus Zahlenwerten in eckigen Klammern, z. B. [C = 3], [-BT1 > −16 °C] 🔎 |
| Kommentar | in Anführungszeichen: „Zylinder fährt aus“ |
| Alternativverzweigung | ein Schritt, mehrere Transitionen; Bedingungen **schließen sich gegenseitig aus** |
| Parallelverzweigung | eine Transition aktiviert mehrere Schritte; Beginn und Ende mit **Doppelstrich**; die Transition nach der Zusammenführung schaltet erst, wenn alle letzten Schritte aktiv sind (Synchronisation) |
| Strukturierung | Makroschritt (Querlinien oben und unten, M…), einschließender Schritt (abgeschrägte Ecken; Rahmen um die eingeschlossene Kette, oben sein Name, zuerst aktiver Schritt mit *), Teil-GRAFCET (G…), Zwangssteuerung im Doppelrahmen: G5 {INIT}, { } leer, {3,4,8} bestimmte Schritte, {*} eingefroren – nur, wenn im Unterricht eingeführt (Betriebsarten, Not-Halt) |

**Aktionen** (Rechteck rechts am Schritt; mehrere Aktionen wirken gleichzeitig)

| Art | Darstellung | Wirkung |
|---|---|---|
| kontinuierlich wirkend | Variable im Rechteck: „-MA1“ | 1, solange der Schritt aktiv ist; danach 0 |
| mit Zuweisungsbedingung | Bedingung an einem Strich über dem Rechteck | 1, solange Schritt aktiv **und** Bedingung erfüllt |
| zeitabhängig | Zuweisungsbedingung mit Zeit („2s/X6“), mit Überstrich zeitbegrenzt | verzögert bzw. zeitbegrenzt |
| speichernd wirkend | **im Rechteck immer die Zuweisung** („-QA1 := 1“), **am Rechteck der Auslöser**: Pfeil nach oben an der linken Kante bei Aktivierung, nach unten bei Deaktivierung, Strich mit Fähnchen und Ereignis („↑-BG1“) bei Ereignis | Wert bleibt bis zur nächsten Zuweisung („-QA1 := 1“ … „-QA1 := 0“) |

Regeln für Musterlösung und Merkmale:
- Kontinuierlich und speichernd wirkende Aktionen **nie auf dieselbe Variable**; speichernde
  Aktionen vor allem für interne Variablen und Zähler („C := C + 1“), Rücksetzen nicht vergessen.
- **Kontaktart** steckt in der Bedingung: Ein Öffner (NC) liefert unbetätigt 1 – „Stopp betätigt“ ist
  dann der negierte Wert. Die Kontaktart steht deshalb im Schülermaterial (T.4).
- Gleichwertig sind: andere Schrittnummern und Kommentare, zusätzliche Leerschritte, gleichwertige
  Bedingungen (z. B. Klammern), kontinuierliche statt speichernde Aktion bei gleicher Wirkung –
  Merkmale funktional formulieren.
- Typische Fehler (Prüfsteine, 0 BE für das Normmerkmal): Schritt an Schritt ohne Transition,
  Rücksprung ohne Pfeil, kein Initialschritt, Alternativzweige nicht ausschließend, speichernde Aktion
  ohne Zuweisung („-QA1“ statt „-QA1 := 1“) oder ohne Pfeil am Rechteck, speichernd gesetzt und nie
  zurückgesetzt, Zeit auf den falschen Schritt bezogen, Öffner nicht negiert.
- **Positionssensor beim Weiterdrehen:** Meldet ein Sensor die Ruhelage und bleibt beim Anlaufen noch
  belegt, schaltet die Transition „-BG1“ sofort, der Antrieb läuft nie. Richtig: Flanke „↑-BG1“ oder
  zwei Schritte mit „¬-BG1“ (Position verlassen) und „-BG1“ (nächste Position erreicht); beide gleichwertig.

## 4. Steuerungsprogramme – IEC 61131-3 und Mikrocontroller

**Ausgabe:** IEC 61131-3:2025 (4. Ausgabe, Mai 2025) ersetzt die Ausgabe 2013 (DIN EN 61131-3:2014-06);
deutsche Fassung 🔎. Wichtigste Änderung für Aufgaben: **AWL (Anweisungsliste, IL) ist gestrichen**
(seit 2013 als veraltet gekennzeichnet). Hersteller bieten AWL/STL zum Teil weiter an – in neuen
Aufgaben nicht verlangen.

| Sprache | Art | Hinweis für Aufgaben |
|---|---|---|
| KOP – Kontaktplan (LD) | grafisch | Öffner/Schließer der **Programmlogik**, nicht der Geberkontakte: Ein NC-Geber wird mit Schließerabfrage auf 1 geprüft |
| FUP – Funktionsbausteinsprache (FBD) | grafisch | Logiksymbole &, ≥1, =1; Negation als Kreis |
| ST – Strukturierter Text | textuell | IF/CASE/FOR; Zuweisung „:=“, Vergleich „=“ |
| AS – Ablaufsprache (SFC) | Struktur | Schritte, Transitionen, Aktionen; nicht mit GRAFCET gleichsetzen |

- **Standardbausteine:** TON (Einschaltverzögerung), TOF (Ausschaltverzögerung), TP (Impuls), CTU,
  CTD, CTUD (Zähler), R_TRIG/F_TRIG (Flanken), SR (**setzdominant**), RS (**rücksetzdominant**).
- **Operanden:** Normform „%IX0.0“, „%QX0.1“, „%MW10“ (Eingang, Ausgang, Merker; X Bit, W Wort);
  Herstellerformen wie „%I0.0“, „E0.0“, „I1“ (LOGO). Die Schreibweise der eingesetzten Steuerung
  im Schülermaterial festlegen (Zuordnungsliste mit Beispielzeile, T.5).
- **Datentypen und Literale:** BOOL, INT, REAL, TIME („T#5s“). Analogwerte: Zahlbereich der
  Baugruppe angeben (Abschn. 7).

**Mikrocontroller als Steuerung** (RRL: IT1 „Steuerungseinheiten“, IT4 „Mikrocontroller für die
Messhardware“). Für Mikrocontroller gibt es keine Norm wie IEC 61131-3; die Aufgabe legt fest, was
die Lösung bestimmt:

| Punkt | Festlegen in der Aufgabe bzw. Anlage | Hintergrund |
|---|---|---|
| Board und Pegel | Board, Logikpegel, ob eine Ein-/Ausgabeplatine 24-V-Geber anpasst | Arduino Uno 5 V; ESP32, STM32 und Raspberry Pi Pico 3,3 V (Tabelle unten); 24-V-Geber nur über Optokoppler oder Spannungsteiler |
| Eingangslogik | Spalte „Signal 1 bedeutet“; Pull-up oder Pull-down | Mit internem Pull-up und Taster gegen Masse liefert ein **betätigter Schließer 0** – die Kontaktart allein bestimmt das Signal nicht mehr |
| Ausgänge | Treiber (Transistor, Relaismodul), ggf. invertierend | Ein Pin liefert nur wenige Milliampere (Uno: 20 mA empfohlen, 40 mA absolut; andere Boards laut Datenblatt 🔎); viele Relaismodule schalten bei Low |
| Analogeingang | Wertebereich **im Programm**, Bürdenwiderstand | hängt von Board, Bibliothek und Einstellung ab (Tabelle unten) – nie nur „12 bit“ angeben |
| Taster | ob Entprellen zur Aufgabe gehört | mechanische Kontakte prellen einige Millisekunden; Software-Entprellung z. B. 20 ms 🔎 |
| Zeiten | Zeit seit Schrittbeginn statt Warteschleife | `delay()` blockiert den Zyklus; Zeitbedingung „5s/X3“ als Vergleich mit der beim Schrittwechsel gespeicherten Zeit (`millis()`) |
| Programmstruktur | Zyklus wie bei der SPS | Eingänge lesen → Transitionen prüfen, Schritt wechseln → Ausgänge aus dem aktiven Schritt setzen; GRAFCET als Zustandsautomat (Variable für den aktiven Schritt, `switch`/`if`) |
| Sprache | „in der im Unterricht verwendeten Sprache“ | C/C++ (Arduino-Umgebung) oder Python (MicroPython); Bezeichner `PIN_SJ1`, `sj1` nach Notationsblatt |
| Sicherheit | Not-Halt und Schutzfunktionen ausklammern | Ein Mikrocontroller ist wie eine Standard-SPS keine Sicherheitssteuerung (Abschn. 6) |

**Analogwerte je Plattform** – den Wertebereich, mit dem das Programm rechnet, in der Anlage nennen;
sonst hat eine Umrechnung mehrere richtige Ergebnisse (K.4).

*Siemens SPS (S7-1200/1500; Analogbaugruppen und -signalboards):*

| Signal | Nennbereich | Übersteuerung bis | Untersteuerung bis | Überlauf / Unterlauf |
|---|---|---|---|---|
| ±10 V, ±5 V, ±20 mA (bipolar) | **−27 648 … +27 648** | 32 511 | −32 512 | 32 767 / −32 768 |
| 0 … 10 V, 0 … 20 mA (unipolar) | 0 … 27 648 | 32 511 (11,76 V bzw. 23,52 mA) | – 🔎 | 32 767 / −32 768 |
| 4 … 20 mA, 1 … 5 V (lebender Nullpunkt) | 0 … 27 648 (4 mA ↦ 0) | 32 511 (22,81 mA) | −4 864 (1,185 mA) | 32 767 / −32 768 (Drahtbruch) |

Umrechnen mit NORM_X (Rohwert → 0,0 … 1,0; bei bipolaren Signalen MIN = −27 648) und SCALE_X
(→ physikalischer Wert); ältere Steuerungen mit dem Baustein SCALE. Analogausgänge nutzen dieselben
Bereiche.

*Kleinsteuerungen und weitere Steuerungen:*

| System | Operanden | Analogwert 0 … 10 V | Analogwert 4 … 20 mA | Hinweise |
|---|---|---|---|---|
| **Siemens LOGO!** (8) | I1 …, Q1 …, AI1 … AI8, AQ1 … AQ8, Merker M1 …, Analogmerker AM1 … 🔎 Anzahl je Modell | 0 … 1000 (über 10 V bleibt 1000) | **200 … 1000** – das Analogmodul rechnet auf 0 … 20 mA, 4 mA ergibt 200 | Basisgeräte 12/24 V: I1, I2, I7, I8 als Analogeingänge (0 … 10 V) nutzbar 🔎; Analogverstärker: Wert · Gain + Offset, für 4 … 20 mA → 0 … 1000 **Gain 1,25, Offset −250**; Analogausgang 0 … 1000 |
| **Eaton easyE4** | Basisgerät I1 … I16, Q1 … Q16; Erweiterungen ab I17, Q17; Analog IA1 … IA4 (Basisgerät, = I5 … I8), ab IA5 bzw. QA5 (Erweiterung); Merker M, MB, MW, MD | 0 … 4095 (12 bit, Datentyp DINT); Basisgerät DC/UC nur 0 … 10 V | **819 … 4095** (Erweiterung EASY-E4-DC-6AE1; bezogen auf 0 … 20 mA) | 0 … 20 mA → 0 … 4095; Pt100- und Ni1000-Erweiterungen liefern skalierte Temperaturen; ältere easy500/700/800: 10 bit, 0 … 1023 🔎 |
| **WAGO** 750 mit PFC100/PFC200 (CODESYS, e!COCKPIT) | IEC 61131-3: %IX, %QX (Byte.Bit), %IW, %QW; im Prozessabbild **zuerst Analog- und Sondermodule wortweise, dann die Digitalbits** – die Adresse hängt von der Modulreihenfolge ab | 0 … **32 760** (0x7FF8), 5 V ↦ 16 384 (750-459) | 0 … **32 760** (750-466, neuere 750-455; ältere Handbücher 0x7FFC) | Messwert in Bit 14 … 3 (12 bit), Bit 2 … 0 Status – für 0 … 4095 drei Bit nach rechts schieben; Über-/Unterbereich: nächster darstellbarer Wert und Statusbyte 0x42 bzw. 0x41; Varianten mit anderem Bereich (z. B. /000-003: 3,8 … 20,5 mA) laut Handbuch 🔎 |

LOGO! und easyE4 beziehen 4 … 20 mA auf den Bereich 0 … 20 mA: Der Rohwert beginnt **nicht** bei 0. In
Aufgaben deshalb den Rohwertbereich für 4 mA und 20 mA ausdrücklich nennen oder die Skalierung
(Gain/Offset bzw. Skalierungsbaustein) vorgeben.

*Mikrocontroller:*

| Board | Pegel | ADC | Wert im Programm | Pins | 4 … 20 mA über Bürde |
|---|---|---|---|---|---|
| Arduino Uno (ATmega328P) | 5 V | 10 bit, Referenz 5 V | `analogRead`: 0 … 1023 | D2 … D13, A0 … A5 | 250 Ω → 1 … 5 V → 205 … 1023 |
| ESP32 | 3,3 V, nicht 5-V-fest | 12 bit, nichtlinear an den Bereichsgrenzen; Messbereich je Dämpfung (bei 11 dB laut Espressif etwa 0,15 … 2,45 V genau 🔎) | Arduino-Kern `analogRead`: 0 … 4095 (Rohwert), `analogReadMilliVolts`: kalibrierte mV; MicroPython `read_u16`: 0 … 65 535 | GPIO-Nummer (GPIO34); bei aktivem WLAN nur ADC1-Pins (GPIO32 … GPIO39) | 120 Ω → 0,48 … 2,4 V → 480 … 2400 mV |
| STM32 (z. B. Nucleo-Boards) | 3,3 V; viele Pins 5-V-fest, nicht im Analogbetrieb 🔎 | meist 12 bit, Referenz 3,3 V (einige Familien bis 16 bit) | Arduino-Kern: `analogRead` 10 bit, mit `analogReadResolution(12)` 0 … 4095; MicroPython `read_u16`: 0 … 65 535 | Port und Nummer (PA0, PB12) | 120 Ω → 0,48 … 2,4 V → 596 … 2978 (12 bit) |
| Raspberry Pi Pico (RP2040, RP2350) | 3,3 V | 12 bit, Referenz 3,3 V; Analog an GP26 … GP28 | MicroPython `read_u16`: 0 … 65 535 (12 bit hochskaliert); Arduino-Kern: `analogRead` 10 bit, mit `analogReadResolution(12)` 0 … 4095 | GP0 … GP28 | 120 Ω → 0,48 … 2,4 V → 596 … 2978 bzw. 9 532 … 47 662 |

- Bürde so wählen, dass 20 mA unter dem genauen Eingangsbereich bleiben (3,3-V-Boards: 120 Ω, 5-V-Board:
  250 Ω) und die Platine einen Schutz gegen Überspannung hat.
- Umrechnung Spannung → Wert als Wert = U / U_ref · (2ⁿ − 1) vorgeben (manche Lehrbücher teilen durch
  2ⁿ) und die Rundung festlegen; beim ESP32 besser die kalibrierte Spannung in mV verwenden.

**Plattformneutrale Steuerungsaufgaben** (wenn die Schule mehrere Plattformen nutzt):
- Funktion als GRAFCET bzw. Logikplan verlangen; Analogwerte im GRAFCET als physikalische Größe.
- Zuordnungsliste mit Spalten „Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller“ und einer
  Anlage mit den verfügbaren Ein- und Ausgängen je Plattform; Rohwert-Rechnungen nur, wenn die
  Plattform feststeht – sonst Stromstärke bzw. Spannung als plattformneutrale Größe rechnen lassen.
- Programmaufträge „in der im Unterricht verwendeten Sprache“; Merkmale prüfen das Verhalten
  (Schrittwechsel, Ausgänge, Zeiten), nicht eine Plattform.

## 5. Schaltpläne, Schaltzeichen, Anschlussbezeichnungen

| Gegenstand | Norm | Kern für Aufgaben |
|---|---|---|
| Schaltzeichen Elektrotechnik | IEC 60617 (Datenbank), DIN EN 60617 🔎 | Kontakte, Spulen, Geber, Melder; binäre Logik &, ≥1, =1, 1 mit Negationskreis |
| Dokumente der Elektrotechnik | DIN EN 61082-1:2015 (IEC 61082-1:2014) | Übersichtsschaltplan, Stromlaufplan (aufgelöste Darstellung, Strompfade nummeriert), Anschlussplan; Betriebsmittel unbetätigt und spannungslos dargestellt 🔎 |
| Anschlüsse an Schaltgeräten | DIN EN 60947-1 und -5-1 🔎 | Spule A1/A2; Hauptkontakte 1-2, 3-4, 5-6; Hilfskontakte: erste Ziffer Ordnungsziffer, zweite Funktionsziffer – **1-2 Öffner, 3-4 Schließer**, 5-6/7-8 Öffner/Schließer mit Sonderfunktion (z. B. verzögert) |
| Leiter und Motoranschlüsse | DIN EN 60445 🔎 | L1, L2, L3, N, PE; Motorwicklung U1-U2, V1-V2, W1-W2 |
| Schaltzeichen Fluidtechnik | DIN ISO 1219-1:2019-01 (ISO 1219-1:2012 + Amd 1:2016) | Wegeventil „5/2“ (Anschlüsse/Schaltstellungen), Betätigungsarten, Zylinder, Drossel |
| Fluidtechnische Schaltpläne | ISO 1219-2:2012 🔎 | eigene Kennzeichnung (z. B. 1V1) – nicht mit 81346 mischen (Abschn. 2) |
| Ventilanschlüsse pneumatisch | ISO 11727 🔎 | 1 Druckluft, 2 und 4 Arbeitsanschlüsse, 3 und 5 Entlüftung, 12 bzw. 14 Steueranschluss (verbindet 1 mit 2 bzw. 1 mit 4) |

Für Aufgaben: Vorlagen (Anschlussplan, Schaltplanausschnitt) als Anlage mit Schaltzeichen des
Unterrichts; die Musterlösung verwendet dieselben Zeichen und Anschlussbezeichnungen.

## 6. Sicherheit an Maschinen – Bedienteile, Farben, Stopp, Not-Halt

**Ausgaben:** DIN EN 60204-1 (VDE 0113-1):2019-06 (IEC 60204-1:2016; Änderung A1 🔎), DIN EN ISO
13850:2016 (Not-Halt), DIN EN 60073 (Farbbedeutung), DIN EN ISO 13849-1:2023 (sicherheitsbezogene
Steuerungsteile, Performance Level).

| Bedienteil | Farbe |
|---|---|
| Start/Ein | **weiß** (bevorzugt), grau, schwarz, grün – **nicht rot** |
| Stopp/Aus | **schwarz** (bevorzugt), grau, weiß; rot erlaubt, aber nicht nahe dem Not-Halt – **nicht grün** |
| abwechselnd Start/Stopp, Tippen | weiß, grau, schwarz – nicht rot, gelb, grün |
| Rücksetzen (Quittieren) | blau, weiß, grau, schwarz – nicht grün |
| Not-Halt | **rot auf gelbem Grund**, nur für Not-Halt |

| Leuchtmelder | Bedeutung |
|---|---|
| rot | Notfall, gefährlicher Zustand – sofort handeln |
| gelb | anormal, kritischer Zustand steht bevor |
| grün | normal, sicherer Betrieb |
| blau | zwingend – Bedienperson muss handeln |
| weiß | neutral, Bestätigung |

- **Stopp-Kategorien:** 0 = Energie sofort abschalten (ungesteuertes Stillsetzen); 1 = gesteuert
  stillsetzen, Energie danach abschalten; 2 = gesteuert stillsetzen, Energie bleibt. **Not-Halt nur
  Kategorie 0 oder 1.**
- **Stopp vor Start:** Ein Stoppbefehl hat Vorrang vor dem zugehörigen Start (rücksetzdominant
  speichern).
- **Not-Halt:** rastet ein; das Entriegeln darf die Maschine nicht wieder anlaufen lassen –
  Neustart nur mit eigenem Startbefehl.
- **Ruhestromprinzip:** Stopp-, Not-Halt- und Sicherheitsgeber als Öffner (drahtbruchsicher; Not-Halt
  mit Zwangsöffnung). Folge für Aufgaben: Kontaktart angeben und in Bedingungen beachten (Abschn. 3).
- **Grenze der Aufgabe:** Eine Standard-SPS ist keine Sicherheitssteuerung. Sicherheitsfunktionen
  (Not-Halt, Schutztür) ausdrücklich ausklammern („Der Not-Halt ist hardwaremäßig gelöst …“, T.7)
  oder als Beurteilungsaufgabe stellen (Risiko, Performance Level nach DIN EN ISO 13849-1 – nur wenn
  unterrichtet).

## 7. Sensorik, Einheitssignale, Regelungstechnik

**Einheitssignale** (IEC 60381 🔎): 4 … 20 mA, 0 … 20 mA, 0 … 10 V.
- 4 … 20 mA hat einen **lebenden Nullpunkt**: Ein Strom unter 4 mA zeigt Drahtbruch oder Ausfall.
  NAMUR-Empfehlung NE 43 (keine Norm): Messbereich 3,8 … 20,5 mA, Ausfall ≤ 3,6 mA oder ≥ 21 mA.
- **Lineare Umrechnung** (in der Aufgabe vorgeben oder als bekannt voraussetzen, wenn unterrichtet):
  x = x_min + (I − 4 mA) · (x_max − x_min) / 16 mA.
- **Digitalwert** der Analogbaugruppe angeben (Siemens 0 … 27 648 für 4 … 20 mA, −27 648 … +27 648 für
  ±10 V; Mikrocontroller je Board und Funktion, Abschn. 4) – sonst hat die Aufgabe mehrere richtige
  Ergebnisse (K.4).

**Pt100** – DIN EN IEC 60751 (IEC 60751:2022 🔎; vorher DIN EN 60751:2009):
- R₀ = 100 Ω bei 0 °C, R(100 °C) = 138,51 Ω, mittlerer Temperaturbeiwert α = 0,003 85 K⁻¹.
- Grenzabweichungen: Klasse AA ±(0,1 + 0,0017·|ϑ|) °C, A ±(0,15 + 0,002·|ϑ|) °C,
  B ±(0,3 + 0,005·|ϑ|) °C, C ±(0,6 + 0,01·|ϑ|) °C.
- Für Aufgaben die **lineare Näherung** R = R₀ · (1 + α · ϑ) ausdrücklich vorgeben (sonst Rechnung
  nach Callendar-Van Dusen) und die Toleranz im Erwartungshorizont nennen.

**Regelungstechnik** – DIN IEC 60050-351:2014-09 (ersetzt DIN 19226):

| Größe | Formelzeichen |
|---|---|
| Regelgröße | x |
| Führungsgröße (Sollwert) | w |
| Regeldifferenz | **e = w − x** |
| Stellgröße | y |
| Störgröße | z |
| Rückführgröße | r |

- Ältere Literatur rechnet mit der Regelabweichung x_w = x − w (umgekehrtes Vorzeichen); Lehrbücher
  der Systemtheorie nennen die Regelgröße y und die Stellgröße u. **Formelzeichen und Vorzeichen im
  Schülermaterial festlegen.**
- Wirkungsplan (Blockschaltbild): Blöcke mit Übertragungsverhalten, Vergleichsstelle als Kreis mit
  Vorzeichen.

## 8. Netzwerke

**Strukturierte Verkabelung** – DIN EN 50173-1 (VDE 0800-173-1):2018-10 (ISO/IEC 11801-1:2017); Teil 2
Bürogebäude, Teil 3 Industrie; Installation: DIN EN 50174.
- Bereiche: Primärbereich (Standort, zwischen Gebäuden) · Sekundärbereich (Gebäude, Steigbereich) ·
  Tertiärbereich (Etage, bis zur Anschlussdose); Verteiler: Standort-, Gebäude-, Etagenverteiler.
- Längen Kupfer im Tertiärbereich: Übertragungsstrecke (Channel) höchstens 100 m, davon fest
  verlegte Strecke (Permanent Link) höchstens 90 m 🔎.
- **Klasse** gilt für die Strecke, **Kategorie** für die Komponente: D / Kat. 5e (100 MHz), E / Kat. 6
  (250 MHz), E_A / Kat. 6_A (500 MHz), F / Kat. 7 (600 MHz), F_A / Kat. 7_A (1000 MHz), I und II /
  Kat. 8.1 und 8.2 (2000 MHz, höchstens 30 m).

**IEEE 802** – 802.3 Ethernet (z. B. 1000BASE-T, 10GBASE-T); PoE: 802.3af 15,4 W, 802.3at 30 W,
802.3bt 60 W bzw. 90 W (je Port an der Quelle); 802.1Q VLAN (VLAN-ID 1 … 4094, 4-Byte-Tag); 802.1X
portbasierte Authentifizierung; 802.11 WLAN.

**Adressen** (RFCs) – in fiktiven Szenarien nur diese Bereiche verwenden:

| Zweck | Bereich | RFC |
|---|---|---|
| private IPv4-Netze | 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 | 1918 |
| **„öffentliche“ Adressen in Beispielen** | 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | 5737 |
| IPv6 in Beispielen | 2001:db8::/32, 3fff::/20 | 3849, 9637 |
| IPv6 privat (ULA) | fc00::/7, genutzt fd00::/8 | 4193 |
| Link-local | 169.254.0.0/16 bzw. fe80::/10 | 3927, 4291 |
| Provider-NAT | 100.64.0.0/10 | 6598 |
| Loopback | 127.0.0.0/8 bzw. ::1 | 1122, 4291 |

- **IPv6-Schreibweise** (RFC 5952): Kleinbuchstaben, führende Nullen je Block weglassen, die längste
  Folge von mindestens zwei Null-Blöcken durch „::“ ersetzen (bei Gleichstand die erste), nie für
  einen einzelnen Block. Musterlösung in dieser Form; andere gültige Kurzformen als *Gleichwertig*.
- **IPv4:** Präfix in CIDR-Schreibweise und Subnetzmaske angeben; Netz- und Broadcastadresse sind keine
  Hostadressen – in der Aufgabe sagen, ob das Gateway die erste oder die letzte nutzbare Adresse ist.

## 9. Software – UML, Struktogramm, Programmablaufplan

- **UML** – OMG UML 2.5.1 (ISO/IEC 19505-2:2012 entspricht UML 2.4.1). Klassendiagramm: Sichtbarkeit
  + public, − private, # protected, ~ package; Attribut „name : Typ“, Operation
  „name(p : Typ) : Rückgabetyp“; statisch unterstrichen, abstrakt kursiv; Assoziation mit
  Multiplizität (1, 0..1, *, 1..*), Aggregation (leere Raute), Komposition (gefüllte Raute),
  Generalisierung (geschlossene leere Pfeilspitze). Zustandsdiagramm: Transition
  „Ereignis [Wächter] / Effekt“.
- **Struktogramm** – DIN 66261:1985 (Nassi-Shneiderman); **Programmablaufplan** – DIN 66001:1983.
- **SQL** – ISO/IEC 9075; den Dialekt des Unterrichts (z. B. SQLite, MySQL) nennen.
- Pseudocode ist nicht genormt: zulässige Sprachelemente als Anlage oder Hilfsmitteldokument.

**Notationsrahmen Informatik in Niedersachsen** – Ergänzende Hinweise zum Kerncurriculum Informatik
(Neufassung Juni 2025, verbindlich für das Zentralabitur ab 2027; ein Teil ist dort als Hilfsmittel
zugelassen). Für das Fach Technik nicht verbindlich, aber das Vorbild, an dem sich Lernende und
Zweitkorrektur orientieren – für Software- und Datenbankteile übernehmen oder Abweichungen in der
Anlage festlegen:
- **Signaturen** wie im Klassendiagramm: `bezeichnung(parameter: Typ, …): Rückgabetyp`, Typnamen
  deutsch (Ganzzahl, Fließkommazahl, Zeichenkette, Wahrheitswert, „dynamische Reihung vom
  Inhaltstyp …“).
- Sprachunabhängig: **Index ab 0** (Zeichenketten, Reihungen), `/` bei zwei Ganzzahlen ganzzahlig,
  `mod` als kleinster positiver Rest, zweidimensionale Reihung `[Zeile][Spalte]`. Bei
  Implementierungen gilt die Syntax der Unterrichtssprache.
- **Zulässige Operationen** werden aufgezählt (Zeichenketten: Länge, Zeichen an Position,
  Teilzeichenkette, Verbinden, Vergleich …; Datenstrukturen mit festen Methodennamen); darüber
  hinausgehende Operationen sind nicht zulässig. Laufzeitfehler (leerer Stapel, ungültiger Index)
  muss die Lösung ausdrücklich abfangen.
- **Struktogramm:** Formulierungen sprachunabhängig, sprachlich („erhöhe anzahl um 1“) oder formal
  („anzahl ← anzahl + 1“); Kommentar mit `//`; „gib … zurück“ beendet die Operation; „erzeuge …“
  ruft den Konstruktor auf.
- **Klassendiagramm:** Sichtbarkeit `+`/`-` im Normalfall Pflicht, Konstruktor mit vorangestelltem
  `c`, nicht aufgeführte Attribute bzw. Operationen als „…“, Assoziationen als einfache Linien;
  Objektkarte `name : Klasse` mit Attributbelegung.
- **Datenbank:** Kurzschreibweise `Tabelle(Schlüssel, Attribut, ↑Fremdschlüssel)` mit
  unterstrichenem Primärschlüssel; ER-Diagramm mit Kardinalitäten (1, n, m) und Schlüsselattributen;
  **SQL-Umfang** SELECT [DISTINCT] … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT,
  Verknüpfung über FROM und WHERE (kein JOIN-Schlüsselwort), Vergleiche einschließlich LIKE mit `_`
  und `%`, Aggregatfunktionen AVG, COUNT, MAX, MIN, SUM; keine verschachtelten Abfragen.
- **Automaten und Grammatiken:** Eingabealphabet Σ, Zustandsgraph; Mealy-Übergang
  „Eingabe/Ausgabe“, leere Ausgabe ε; Kellerautomat „(oberstes Kellerzeichen, Eingabe) :
  abgelegte Zeichen“ mit Vorbelegung #; Grammatik mit N, T, Startsymbol und Regeln, regulär
  rechtsregulär notiert.
- **Codierung:** Lauflängencodierung „Anzahl-Wert“; Kompressionsverhältnis = komprimiert /
  original; (7,4)-Hamming-Code in der Reihenfolge p0 p1 d0 p2 d1 d2 d3 mit gerader Parität.
- Die Vorgaben wechseln mit dem Jahrgang (2026 andere Baum-Operationen als ab 2027) – vor jedem
  Prüfungsjahr mit den aktuellen fachbezogenen Hinweisen abgleichen 🔎.
- Bezeichner aus Klassendiagramm und Code in Schüler- und Lehrermaterial gleich schreiben (K.9).

## 10. Größen, Einheiten, Schreibweise

DIN EN ISO 80000-1 (ISO 80000-1:2022 🔎), DIN 1313 (Größen), DIN 1338 (Formelsatz):
- Zahl und Einheit mit Leerzeichen: „24 V“, „45 %“, „20 °C“; ohne Leerzeichen nur der ebene Winkel
  „90°“. Dezimalkomma. Bereiche „4 mA … 20 mA“ oder „(4 … 20) mA“.
- Formelzeichen kursiv, Einheiten aufrecht. „[U] = V“ heißt „Einheit von U“ – Spaltenköpfe daher
  „U in V“ oder „U / V“, nicht „U [V]“.
- **Datenmengen** – IEC 80000-13 🔎: Bit „bit“, Byte „B“; Dezimalvorsätze k = 10³, M = 10⁶;
  Binärvorsätze Ki = 2¹⁰, Mi = 2²⁰; Datenraten in bit/s (Mbit/s). In der Aufgabe festlegen, ob mit
  1 kB = 1000 B oder 1 KiB = 1024 B gerechnet wird – sonst zwei richtige Ergebnisse (K.4).

## 11. Quellen

Recherche 2026-10-30; Normtexte nicht eingesehen, außer der Leseprobe der IEC 81346-2:2019.
- IEC 81346-2:2019, Leseprobe (Abschnitte 4–5, Tabellen 1 und 2 Klasse B und C):
  https://cdn.standards.iteh.ai/samples/21908/1b996d119d0945b2b28359332ffa9b3f/IEC-81346-2-2019.pdf
- PAL/IHK Stuttgart: „DIN EN IEC 81346-2:2020-10 – Anwendung der aktuellen Referenzkennzeichnungen in
  PAL-Prüfungen“, Stand Juni 2024 (SF → SJ, RZ → RN, Beispielschaltpläne):
  https://www.ihk.de/blueprint/servlet/resource/blob/5090560/d005ab9b73c3e45d81920e28f72b7160/din-en-iec-81346-2-2020-10-referenzkennzeichnung-data.pdf
- PAL: „ISO 1219-2 (2012-09) und DIN EN 81346-2 (2009-10)“, Stand April 2016 (Ausgabe 2009: SF, SJ, RN, RZ):
  https://grafcet-schulungen.de/wp-content/uploads/2017/02/Referenzkennzeichnung_DIN_ISO_1219_81346_PAL_Stand_Dez_2016.pdf
- Wikipedia „IEC 81346“ und „EN IEC 81346“ (Unterklassen und dritte Ebene der Ausgabe 2019; Teil 1
  2022 mit Typaspekt „%“): https://en.wikipedia.org/wiki/IEC_81346, https://de.wikipedia.org/wiki/EN_IEC_81346
- DKE: DIN EN 60848:2014-12 (aktuell): https://www.dke.de/de/normen-standards/dokument?id=7049716&type=dke%7Cdokument
- Wikipedia „GRAFCET“; Europa-Lehrmittel, Leseprobe „GRAFCET“ (Transitionen, Zeiten, speichernde Aktionen):
  https://de.wikipedia.org/wiki/GRAFCET, https://www.europa-lehrmittel.de/leseprobe/37633-4.pdf
- IEC 61131-3:2025, Änderungen gegenüber 2013 (IL gestrichen): https://stefanhenneken.net/2025/06/11/iec-61131-3-comparison-of-edition-3-and-edition-4/
- IFAN: Vergleich DIN EN 60204-1 (VDE 0113-1):2019-06 (Farben, Stopp-Kategorien):
  https://ifan-normung.de/wp-content/uploads/2019/07/Vergleich_EN-60204-1-wa14.pdf
- DKE/Wikipedia zu DIN EN 50173-1:2018-10: https://de.wikipedia.org/wiki/EN_50173
- DIN Media zu DIN IEC 60050-351:2014-09: https://www.dinmedia.de/en/standard/din-iec-60050-351/116876648
- DIN ISO 1219-1:2019-01: https://webstore.ansi.org/standards/din/diniso12192019de
- RFC 1918, 3849, 3927, 4193, 4291, 5737, 5952, 6598, 9637 (rfc-editor.org).
- Niedersächsisches Kultusministerium: Ergänzende Hinweise zum Kerncurriculum Informatik, Neufassung
  Juni 2025 (lokal unter `Klausuren/Beispielklausuren/Abiturprüfungen/Normen Hinweise Notationen/`).
- Zentrale Abiturprüfungen Mechatronik Niedersachsen 2020–2026 (nur gelesen, Kennbuchstaben
  ausgezählt): Ausgabe 2009 (-SF, -RZ, -AZ).

## Anhang: references/notation-steuerungstechnik.md

# Notationsblatt Steuerungstechnik

Einheitliche Schreibweise der Bibliothek für Kennzeichen, Signale, Zuordnungsliste, GRAFCET und
Programme – für Prüfungsaufgaben, Erwartungshorizonte und Unterricht. Grundlage: DIN EN IEC 81346-2:2020,
DIN EN 60848:2014, IEC 61131-3:2025; Hintergrund und Quellen in `normen-technik.md` (Abschn. 2–4).
Stand 04.11.2026.

## Für die Lehrkraft

- **Teil „Anlage“ unten** dem Schülermaterial beifügen („## Anlage N – Notation Steuerungstechnik“,
  das Wort *Notation* in der Überschrift behalten), Abschnitte streichen, die die Aufgabe nicht braucht.
  `bmk_pruefen.py` überspringt diese Anlage bis zur nächsten Überschrift gleicher Ebene; ihre
  Beispiel-Kennzeichen zählen nicht zur Aufgabe. Keine Unterüberschriften in der Anlage. So arbeiten Prüfling, Erst- und Zweitkorrektur
  mit derselben Schreibweise.
- **Abweichungen des Unterrichts** (andere Ausgabe der Kennzeichnung, andere Zeitschreibweise) in der
  Anlage ändern und im Begleitblatt begründen – nie innerhalb eines Vorschlags mischen.
- **Plattformneutral stellen:** Steuerungsaufgaben müssen mit SPS, Kleinsteuerung **oder**
  Mikrocontroller lösbar sein, wenn die Schule mehrere Plattformen nutzt. Dafür:
  1. Funktion als GRAFCET bzw. Logikplan spezifizieren – beides ist plattformunabhängig.
  2. Analogwerte im GRAFCET als physikalische Größe mit Einheit; Rohwerte nur in plattformgebundenen
     Teilaufgaben und immer mit dem Bereich für 4 mA bzw. 20 mA in der Anlage (Bereiche je Plattform:
     `normen-technik.md`, Abschn. 4; für die Prüflinge stehen sie in der Anlage unten).
  3. Zuordnungsliste mit je einer Spalte je Plattform; die Prüflinge füllen die Spalte ihrer
     Plattform. Die verfügbaren Ein- und Ausgänge je Plattform stehen in einer Anlage.
  4. Programmieraufträge „in der im Unterricht verwendeten Sprache“; im Lehrermaterial *Gleichwertig*
     für jede Plattform.
- **Prüfen:** `bmk_pruefen.py` – T.6 Schreibweise, T.8 Kennbuchstaben, T.9 GRAFCET-Textform.

---

## Anlage – Notation Steuerungstechnik

**1. Kennzeichen der Betriebsmittel**

- Bindestrich, **Klasse und Unterklasse**, Zählnummer, ohne Leerzeichen: **-SJ1**, **-MA1**, **-MM1**,
  **-EA1** (DIN EN IEC 81346-2:2020). Die Klasse allein (-S1, -M1) wird nicht verwendet.
- Dieselbe Schreibweise gilt in **Funktionsbeschreibung, Technologieschema (Legende), Zuordnungsliste**,
  GRAFCET, Logikplan und Programm.
- Die Zählnummer zählt je Kennbuchstaben: -BG1, -BG2, -BP1.

| Kennbuchstaben | Betriebsmittel (Beispiele) |
|---|---|
| -SJ | Taster, Schalter, handbetätigtes Ventil |
| -BG | Näherungs-, End-, Zylinderschalter (Lage, Abstand) |
| -BP, -BL, -BT | Druckschalter; Füllstand, Schwimmerschalter; Temperaturfühler |
| -KE, -KF | Steuerung (SPS, Kleinsteuerung, Mikrocontroller); Relais, Zeitrelais |
| -QA, -QM | Schütz, Leistungsschalter; Wegeventil |
| -MA, -MB, -MM | Elektromotor; Ventilspule, Elektromagnet; Zylinder |
| -PF, -PJ | Leuchtmelder, Anzeige; Hupe, Summer |
| -EA, -EB | Leuchte, Lampe; Heizung |
| -RN, -RM | Drossel- und Drosselrückschlagventil; Rückschlagventil |
| -GP, -GQ | Pumpe; Kompressor, Lüfter |
| -TC, -TF | Netzteil; Messumformer |

**2. Signale**

- Im Text, im GRAFCET und im Logikplan steht das Kennzeichen für **sein Signal an der Steuerung**: -BG1
  ist 1 oder 0. Was 1 bedeutet, steht in der Zuordnungsliste (Spalte „Signal 1 bedeutet“).
- **Kontaktart:** NO = Schließer, NC = Öffner. Ein Öffner liefert im unbetätigten Zustand 1.
- **Analogwerte** stehen in Bedingungen als physikalischer Wert mit Einheit: [-BT1 > −16 °C],
  [-BL1 ≥ 80 %]. Die Umrechnung aus dem Rohwert ist Teil des Programms.
- **Interne Variablen** (Merker, Zähler) tragen einen sprechenden Namen ohne Bindestrich in
  Code-Schrift: `M_Pumpe`, `C_Teile`.

**3. Zuordnungsliste**

| BMK | Betriebsmittel | Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |
|---|---|---|---|---|---|---|
| -SJ1 | Taster Start | %I0.0 | I1 | D2 | Start betätigt | NO |
| -SJ2 | Taster Stopp | %I0.1 | I2 | D3 | Stopp nicht betätigt | NC |

- Ausgefüllt wird nur die Spalte der Plattform aus dem Unterricht; die anderen Spalten bleiben
  leer.
- Jeder Operand bzw. Pin wird genau einmal belegt. Analoggeber mit Messbereich und Signal
  („4 … 20 mA für 10 … 60 %“).
- Operanden wie in der Programmiersoftware: Siemens-SPS %I0.0, %IW64; WAGO %IX4.0, %IW0; LOGO! I1, AI1;
  Eaton easyE4 I1, IA1. Pins wie auf dem Board bezeichnet: D2 (Arduino), GPIO16 (ESP32), PB12 (STM32),
  GP2 (Raspberry Pi Pico).

**4. GRAFCET (DIN EN 60848)**

- **Schritt:** Quadrat mit Nummer; **Initialschritt doppelt umrandet** (Nummer 0). Schrittvariable
  X3 = 1, solange Schritt 3 aktiv ist.
- **Transition:** Querstrich, Bedingung rechts daneben, Name wenn nötig links in Klammern: (T2).
  Schritt und Transition wechseln sich ab; Verbindungen nach oben (Rücksprung) mit Pfeil.
- **Verzweigungen:** Alternativ mit einfacher Linie und einer Transition je Ast (die Bedingungen schließen
  sich gegenseitig aus); parallel mit Doppellinie unter der gemeinsamen Transition, zusammengeführt mit
  Doppellinie über der gemeinsamen Transition.
- **Bedingungen:**

  | Bedeutung | Schreibweise |
  |---|---|
  | UND | -SJ1 · -BG1 |
  | ODER | -BG2 + -BG3 |
  | NICHT | Überstrich über dem Kennzeichen; getippt **¬-SJ2** |
  | steigende bzw. fallende Flanke | ↑-BG1, ↓-BG1 |
  | Zeit seit Aktivierung von Schritt 3 | **5s/X3** |
  | Vergleich eines Zahlenwerts | **[-BT1 > −16 °C]**, [C_Teile = 10] |
  | immer erfüllt | 1 (unterstrichen) |

- **Aktionen** im Rechteck rechts am Schritt. Mehrere Aktionen stehen nebeneinander oder lückenlos untereinander:

  | Art | im Rechteck | am Rechteck | Wirkung |
  |---|---|---|---|
  | kontinuierlich | -MA1 | – | 1, solange der Schritt aktiv ist |
  | mit Zuweisungsbedingung | -MA1 | Strich oben, daran die Bedingung | 1, solange Schritt aktiv und Bedingung erfüllt |
  | verzögert | -MA1 | Strich oben, daran 5s/X3 | 1 ab 5 s nach Aktivierung, solange der Schritt aktiv ist |
  | zeitbegrenzt | -MA1 | Strich oben, daran 5s/X3 mit Überstrich | 1 in den ersten 5 s nach Aktivierung |
  | speichernd bei Aktivierung | -QA1 := 1 | Pfeil nach oben an der linken Kante | Wert bleibt bis zur nächsten Zuweisung |
  | speichernd bei Deaktivierung | -QA1 := 0 | Pfeil nach unten an der linken Kante | Wert bleibt bis zur nächsten Zuweisung |
  | speichernd bei Ereignis | -QA1 := 1 | Strich oben mit Fähnchen nach links, daran ↑-BG1 | Zuweisung beim Ereignis, solange der Schritt aktiv ist |
  | Zähler | C_Teile := C_Teile + 1 | Pfeil nach oben an der linken Kante | zählt bei jeder Aktivierung |
  | Zwangssteuerung | G5 {INIT} im Doppelrahmen | – | setzt Teil-GRAFCET G5: {INIT} Anfangssituation, { } leer, {3,4,8} diese Schritte, {*} eingefroren |

- **Speichernd wirkende Aktionen** tragen immer beides: die **Zuweisung** mit := im Rechteck und den
  **Auslöser** am Rechteck. „-QA1“ allein ist kontinuierlich. Dieselbe Variable wirkt nie zugleich
  kontinuierlich und speichernd; was mit := 1 gesetzt wird, wird auch mit := 0 zurückgesetzt.
- **Strukturierung**, wenn im Unterricht eingeführt: Makroschritt (Querlinien oben und unten im Quadrat, M4),
  einschließender Schritt (abgeschrägte Ecken) mit Rahmen um die eingeschlossene Kette, oben der Name
  des einschließenden Schritts; der zuerst aktive Schritt darin trägt links ein *. Quelltransition ohne
  Verbindung nach oben, Schlusstransition ohne Verbindung nach unten.
- **Kommentare** in Anführungszeichen: „Zylinder fährt aus“.

**5. GRAFCET in Textform**

Wird ein GRAFCET getippt statt gezeichnet (Erwartungshorizont, PC-Aufgabe), gilt diese Tabelle:

| Schritt | Aktion | Transition zum Folgeschritt |
|---|---|---|
| 0 (Initialschritt) | – | -SJ1 · -BG1 → 1 |
| 1 Füllen | -MA1 | [-BL1 ≥ 80 %] + 30s/X1 → 2 |
| 2 Prüfen | ↑ C_Teile := C_Teile + 1 | [C_Teile < 10] → 1; [C_Teile = 10] → 3 |
| 3 Fertig | -PF1 | ¬-SJ2 → 0 |

- Folgeschritt nach **→**; Alternativen durch **;** getrennt (sie schließen sich gegenseitig aus).
- Mehrere Aktionen durch **;** getrennt. Speichernd **↑ -QA1 := 1**, **↓ -QA1 := 0**, bei Ereignis
  **-QA1 := 1 bei ↑-BG1**; mit Bedingung **-MA1 wenn -BG1**, verzögert **-MA1 verzögert 5s/X3**, zeitbegrenzt
  **-MA1 begrenzt 5s/X3**.
- Parallelverzweigung „→ 3 und 6 (parallel)“; die gemeinsame Transition danach steht bei beiden
  letzten Schritten mit dem Zusatz „(gemeinsam mit X8)“.

**6. Logikplan und Programm**

- **Logikplan (FUP):** Verknüpfungsglieder & (UND), ≥1 (ODER), =1 (XOR), Negation als Kreis am
  Eingang oder Ausgang; Eingänge und Ausgänge mit Kennzeichen beschriftet.
- **Programm** in der im Unterricht verwendeten Sprache:
  - SPS und Kleinsteuerung nach IEC 61131-3: KOP, FUP, ST oder AS (keine AWL). Zeiten mit TON, TOF,
    TP; Zähler mit CTU, CTD; SR setzdominant, RS rücksetzdominant.
  - Mikrocontroller in C/C++ oder Python: Pin-Konstante `PIN_SJ1`, Signalvariable `sj1` (Kennzeichen
    klein, ohne Bindestrich). Zeiten über die Zeit seit Schrittbeginn (z. B. `millis()`), nicht mit
    Warteschleifen; einen GRAFCET als Zustandsautomat mit einer Variablen für den aktiven Schritt.
- **Mikrocontroller-Eingänge:** Signal 1 ist der High-Pegel am Pin. Bei internem Pull-up-Widerstand
  liefert ein betätigter Schließer 0 – die Zuordnungsliste sagt, was 1 bedeutet.
- **Analogwerte:** Der Wertebereich im Programm steht in der Anlage der Ein- und Ausgänge; er hängt
  von Steuerung, Board und Funktion ab (z. B. 4 … 20 mA: Siemens 0 … 27 648, WAGO 0 … 32 760, LOGO!
  200 … 1000, Eaton easyE4 819 … 4095; Arduino Uno 0 … 1023, 12 bit 0 … 4095, MicroPython 0 … 65 535).

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.
Klausur- und Abiturformat haben eigene Richtwerte (`klausur-erstellen`, `abiturvorschlag-erstellen`);
die vier Regeln gelten dort sinngemäß.

## Inhalt
1. Vier Regeln
2. Darstellungen statt Text
3. Aufträge offen statt kleinschrittig
4. Was entfällt
5. Richtwerte
6. Rückwärtsprobe vor der Ausgabe

## 1. Vier Regeln

1. **Kurz.** Lernende lesen nur, was sie für den Auftrag brauchen. Kein Satz ohne Aufgabe,
   keine Wiederholung, kein Exkurs.
2. **Offen gestellt.** Ein Auftrag nennt Ziel (Operator), Gegenstand, Ergebnisform und woran
   man merkt, dass man fertig ist. Den Weg finden die Lernenden; Schritte und Gerüste stehen in
   gestuften Hilfen, die man bei Bedarf zieht.
3. **Anschaulich.** Aufgaben arbeiten mit Zeichnungen, Darstellungen und Grafiken: ablesen,
   auswerten, ergänzen, Fehler finden, selbst zeichnen. Was eine Darstellung zeigt, wird nicht
   zusätzlich beschrieben.
4. **Ohne Dekoration.** Nur, was dem Ziel dient (Abschn. 4).

Gekürzt wird Überflüssiges, nicht Fachinhalt: Fachbegriffe, Sicherheitshinweise und
Erfolgskriterien bleiben vollständig.

## 2. Darstellungen statt Text

| Inhalt | Darstellung | so entsteht sie |
|---|---|---|
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen`; Technologieschema mit `technologieschema-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen`; GRAFCET und Funktionsplan mit `technologieschema-erstellen` |
| System, Energie- und Datenfluss, Regelkreis | Blockschaltbild | `fachdiagramm-erstellen` |
| Zusammenhang zweier Größen | Diagramm, Kennlinie mit beschrifteten Achsen | aus gerechneten Werten oder dem Datenblatt als SVG erzeugen (Code), nie geschätzt |
| Vergleich, Kriterien, Kenndaten | Tabelle, Matrix | Markdown-Tabelle |
| Begriffe und ihre Beziehungen | Strukturbild | `fachdiagramm-erstellen` (Bauart `flow`), Tabelle |
| Daten und Software | ER-, Klassen-, Sequenzdiagramm | `fachdiagramm-erstellen` |
| Schaltung, Werkstück | Schaltplan, technische Zeichnung nach Norm | Herstellerunterlage, Tabellenbuch, eigene Zeichnung (Platzhalter mit Quelle) |

Jede Zeichnung entsteht als **SVG aus einer Spec** – nie als Zeichnung aus Zeichen (ASCII-Art) und
nie als Mermaid in der Ausgabe (Skill-Vertrag Abschn. 3).

**Die Darstellung ist Arbeitsgegenstand, nicht Beigabe.** Aufträge, die mit ihr arbeiten
(Beispiele am Gurtförderer GF-2, fiktiv):

| Auftrag | Beispiel |
|---|---|
| ablesen, auswerten | „Ermitteln Sie aus der Kennlinie die Drehzahl bei 80 % Last.“ |
| ergänzen | „Benennen Sie im Anlagenbild die Bauteile ① bis ④.“ |
| Fehler finden | „Der Arbeitsplan in Abb. 2 enthält zwei Fehler. Berichtigen Sie sie.“ |
| selbst zeichnen | „Skizzieren Sie, wie die Spannstation verstellt werden muss.“ |
| vergleichen | „Vergleichen Sie die Gurtlaufbilder A und B.“ |

Regeln:
- **Am Auftrag:** Abbildung direkt bei dem Auftrag, der sie braucht; Beschriftung in die
  Abbildung, Positionsnummern statt Legendentext, wo möglich.
- **Fachlich richtig und normgerecht:** Schaltzeichen, Kennzeichen und Formelzeichen nach
  Norm; Werte hinter Diagrammen sind gerechnet.
- **Schwarzweiß lesbar:** Farbe nur mit Bedeutung und nie allein (zusätzlich Linienart oder
  Beschriftung).
- **Nie erfinden:** keine KI-Bilder, die Fotos, echte Anlagen oder Messkurven vortäuschen. Was
  nicht selbst gezeichnet werden kann (Foto, Herstellerzeichnung, Normauszug), steht als
  Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz]` und ist ein Prüfauftrag.
- **Barrierearm:** Alternativtext (ein Satz) je Abbildung.
- **Platz für Zeichnungen der Lernenden:** in der Druckfassung Kasten oder Raster statt Linien.

Nicht jede Aufgabe braucht ein Bild (Begründung, Gespräch, Reflexion). Ein Arbeitsblatt oder
Infoblatt ganz ohne Darstellung ist aber zu begründen.

## 3. Aufträge offen statt kleinschrittig

**Kleinschrittig – so nicht:**

> 1. Lesen Sie den Wartungsplan (M1).
> 2. Unterstreichen Sie alle Arbeiten, die nach 500 Betriebsstunden fällig sind.
> 3. Übertragen Sie die Arbeiten in die erste Spalte der Tabelle.
> 4. Ergänzen Sie in der zweiten Spalte das Werkzeug.
> 5. Ergänzen Sie in der dritten Spalte die Sicherheitsmaßnahme.
> 6. Addieren Sie die Zeiten.

**Offen – so:**

> **1 Erstellen Sie** den Arbeitsplan für die 500-h-Wartung des GF-2 (Wartungsplan M1,
> Vorlage M3). Fertig, wenn jeder Schritt Werkzeug und Sicherheitsmaßnahme hat und die
> Gesamtzeit unter 2 h liegt.

Die Schritte stehen – kürzer – in den gestuften Hilfen (Impuls → Strategie → Teilschritt →
Kontrolle; Skill `differenzierung-erstellen`). Wer sie braucht, zieht sie. Formate mit weniger
Stufen ordnen zu: Lernlandkarte – Kontrolle ist der Selbstcheck des Lernpostens; Lektion –
Orientierung, Werkzeug, Gerüst entsprechen Impuls, Strategie, Teilschritt, die Kontrolle leisten
Realitätstest und Rückmeldung.

Signale für Kleinschrittigkeit:
- mehr als drei Teilaufgaben a), b), c) an einem Auftrag;
- eine Schrittfolge im Auftrag, die den Lösungsweg vorgibt („zunächst …, dann …,
  anschließend …“) oder eine Reihe kurzer Einzelaufträge, die zusammen einen Auftrag ergeben;
- Lesen, Unterstreichen, Abschreiben oder Übertragen als eigener Auftrag – das sind Mittel,
  kein Ziel;
- Lücken, die sich durch Abschreiben aus dem Text füllen lassen;
- Teilaufgaben, deren Ergebnis die nächste schon verrät.

**Zulässig und nicht kleinschrittig:**
- **Sicherheitsrelevante Schritte** (Freischalten, Stoffe, Mengen, Reihenfolge an der
  Maschine) stehen vollständig und in Reihenfolge – auch in einer offenen Anleitung.
- **Bedienschritte**, die nicht Lernziel sind (Messgerät einstellen, Software starten): kurz,
  am besten als Bildfolge oder Hinweis, nicht als Auftrag.
- **Übungsfolgen** zum Einschleifen einer Routine: gleichartige, je für sich vollständige
  Aufgaben (gelöstes Beispiel → steigend → eingekleidet).
- **Lösungsbeispiel mit Ausblenden:** steht als Beispiel, nicht als Auftrag.
- **Einführende Bildungsgänge** (Berufseinstieg, BVJ): enger geführt über Lösungsbeispiele,
  Hilfen und hohen Anschauungsgrad – nicht über zerlegte Aufträge.

## 4. Was entfällt

| entfällt | stattdessen |
|---|---|
| Schmuckbilder, Cliparts, Symbol- und Stockfotos, Illustrationen ohne Fachinhalt | Abbildung mit Fachinhalt – oder keine |
| Emojis und Symbole ohne Funktion (auch farbige Punkte als Stufenkennung) | Wort; zulässig sind die KI-Zeichen 🚫 💡 🔧 (`ki-vereinbarungen.md`, falls vorhanden), Warn- und Gefahrenzeichen, Ankreuzkästchen ☐ und ✔ ~ ✘ zur Selbsteinschätzung |
| Begrüßung, Motivationssätze („Viel Spaß!“, „Los geht’s!“), Ankündigungen („In diesem Arbeitsblatt lernen Sie …“) | gleich mit Situation oder Auftrag beginnen |
| Einleitung, die den Auftrag vorwegnimmt; Zusammenfassung dessen, was eben dastand | Kernaussage einmal, vorn |
| Exkurse, Anekdoten, Technikgeschichte, „Wussten Sie schon?“-Kästen | als Vertiefung, wenn sie zum Ziel beitragen – sonst streichen |
| dasselbe in Fachwissen, Hilfe und Auftrag | einmal, dort, wo es gebraucht wird |
| Zierrahmen, Farbflächen, Schmuckschriften | klare Überschriften; Kästen nur mit Funktion (Hilfe, Stolperstein, Sicherheit) |
| Angaben für die Lehrkraft (AFB, Kompetenzcodes, Annahmen, Prüfvermerke) | im Lehrerteil |
| Information, die kein Auftrag braucht | streichen |

Keine Dekoration, also bleibend: Kopfzeile (Lernsituation, Zeit, Sozialform), Name und Datum
auf Druckblättern, Erfolgskriterien, Bewertungskasten, KI-Zeichen, Quellen- und
Lizenzangaben, KI-Transparenzhinweis.

## 5. Richtwerte

Orientierung, kein Urteil. ⚠️ Noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

| Element | Richtwert |
|---|---|
| Ausgangslage, Bezug zur Situation | höchstens drei Sätze; besser Situationsmaterial (Störmeldung, Foto, Anlagenbild) |
| Arbeitsauftrag | ein bis zwei Sätze, ≤ ~25 Wörter, Operator zuerst; der Kontext steht einmal in der Ausgangslage |
| Teilaufgaben je Auftrag | höchstens drei |
| Satz | meist unter 15 Wörtern, keiner über 25; die sprachsensible Fassung ist bewusst strenger (über 20 Wörter teilen, `lesbarkeit.py`) |
| Infoblatt | eine Seite, ≤ ~300 Wörter Fließtext, mindestens eine tragende Darstellung |
| Arbeitsblatt (Teil für Lernende) | ≤ ~350 Wörter Fließtext (ohne Tabellen, Code, Abbildungen), mindestens eine Darstellung |
| Situationsmaterial | ≤ ~150 Wörter |
| Hilfekarte | je Stufe ≤ ~40 Wörter, gern als Teilbild oder Skizze |
| Rollenkarte | ≤ ~60 Wörter |
| Lektion (90 min) | ≤ ~1 500 Wörter ohne Code (`lektionsmuster.md`, falls vorhanden) |
| Lernlandkarte (eine Unterrichtseinheit) | ≤ ~1 500 Wörter wie eine Lektion; je Karte nur Auftrag, Material, Hilfen, Selbstcheck |
| sonstiges Material | ≤ ~400 Wörter Fließtext je Datei |

Authentische Dokumente (Betriebsanleitung, Datenblatt, Norm, Quelle der Quellenmappe) bleiben
im Original und zählen nicht mit – sie liegen als Auszug mit Fundstelle bei, nicht
abgeschrieben.

## 6. Rückwärtsprobe vor der Ausgabe

1. **Jeder Absatz, jede Abbildung:** Welcher Auftrag braucht das? Keiner → streichen.
2. **Jeder Auftrag:** Operator, Ergebnisform, Erfolgskriterium – und kein vorgegebener
   Lösungsweg? Schritte → in die Hilfen.
3. **Jede Aufgabe:** Mit welcher Darstellung wird gearbeitet? Keine → ergänzen, wo eine trägt.
4. **Dekoration** (Abschn. 4) gestrichen?
5. **Skript:** `python3 scripts/schuelermaterial_pruefen.py DATEI.md` – Fließtext, lange Sätze
   und Aufträge, Teilaufgaben und Schrittfolgen, Darstellungen je Auftrag, Dekoration,
   Lehrerangaben, doppelte Sätze. Wortzahl und Befunde im Qualitätscheck festhalten.

## Anhang: references/skill-vertrag.md

# Skill-Vertrag der Bibliothek „Unterrichtsentwicklung BBS"

Gemeinsamer Standard für alle Skills dieser Bibliothek. Er sorgt dafür, dass jeder Skill
**allein** funktioniert und trotzdem **mit jedem anderen kombinierbar** ist. Die Quelle liegt
in `_gemeinsam/skill-vertrag.md`; jeder Skill trägt eine Kopie unter `references/`.

---

## 1. Eigenständig arbeiten – Entwurf vor Rückfrage

1. Der Skill braucht nur den Auftrag der Lehrkraft. Fehlende Angaben werden durch
   **begründete, fachtypische Annahmen** ersetzt und sichtbar markiert:
   `⚠️ Annahme: 2. Ausbildungsjahr, 24 SuS, heterogen.` bzw. im Beruflichen Gymnasium
   `⚠️ Annahme: Jg. 13 (Qualifikationsphase), 22 SuS, Lerngebiet ING3.`
2. **Rückfragen nur, wenn ohne Antwort der ganze Entwurf unbrauchbar wäre** (z. B. Beruf
   bzw. Fach völlig unbekannt). Dann höchstens drei gebündelte Fragen, jeweils mit Vorschlag
   als Standardantwort.
3. Ziel ist ein **vollständiger erster Entwurf** (alle Abschnitte gefüllt), nicht ein
   perfekter Teil. Die Lehrkraft schärft nach.
4. Ein Skill ruft **keinen anderen Skill selbst auf**. Er empfiehlt am Ende sinnvolle
   Folge-Skills. Das Verketten übernimmt der Orchestrator `unterricht-entwickeln`.

## 2. Kontext übernehmen – die Planungsakte

Liegt eine **Planungsakte** vor (Datei `00_planungsakte.md` im Arbeitsordner oder ein
Planungsakte-Block im Gespräch), übernimmt der Skill daraus alle passenden Angaben und fragt
nichts erneut ab. Nach getaner Arbeit trägt er sein Artefakt in die Akte ein und ergänzt
leere Felder, die er festgelegt hat. Widersprüche zur Akte werden gemeldet, nicht still
überschrieben.

```markdown
---
projekt: "LS 4 – Förderband nach Störung wieder in Betrieb nehmen"
bundesland: Niedersachsen
schulform: Berufsschule (Teilzeit)
bildungsgang: Industriemechaniker/-in
ausbildungsjahr: 2          # vollzeitschulisch (z. B. BG) stattdessen: schuljahrgang, phase, schwerpunkt, lerngebiet
curriculare_vorgabe: "Rahmenlehrplan Industriemechaniker/-in, LF 6"
dqr: 4
zeitrichtwert_ls: 16
lerngruppe: "22 SuS, heterogen, 3 SuS mit Deutsch als Zweitsprache (ca. B1)"
rahmen: "Fachraum Steuerungstechnik, Moodle, 90-Minuten-Blöcke"
handlungssituation: "…"
handlungsergebnis: "…"
leitidee_ls: "…"            # didaktische Leitidee der Lernsituation (1–2 Sätze)
---

## Artefakte
| Nr. | Artefakt | Skill | Status | Datei |
|---|---|---|---|---|
| 10 | DQR-Einordnung | dqr-zuordnen | Entwurf | 10_dqr-einordnung.md |

## Entscheidungen
- …

## Annahmen und Prüfaufträge (gesammelt)
- …
```

## 3. Ausgabe – einheitlich und weiterverwendbar

**Format:** Markdown. Mit Dateizugriff wird als Datei gespeichert, sonst im Chat ausgegeben.
Ein bestehendes Dokument wird **nie überschrieben**; Überarbeitungen erhalten ein Suffix
(`…_sprachsensibel.md`, `…_v2.md`).

**Text zum Einfügen** (Systemanweisung, Moodle-Textfeld, Hinweistext, Importquelle) steht als
eigener Block im Format des Ziels – ohne Erläuterungen darin; Erläuterungen stehen davor oder
danach. **Vorschläge zu Vorhandenem** (Begutachtung, Überarbeitung, Einstellungen) nennen je
Vorschlag Stelle, neuen Wert und Begründung; was schon passt, wird zusammengefasst bestätigt
statt wiederholt.

**Material für Lernende** (alles, was Lernende in die Hand bekommen; Vorgabe der Fachberatung,
31.10.2026): **kurz** – kein Satz ohne Aufgabe; **offen gestellt** – Ziel, Ergebnis und
Erfolgskriterium statt Lösungsweg, Schritte in gestufte Hilfen; **anschaulich** – Aufgaben
arbeiten mit Zeichnungen, Darstellungen und Grafiken; **ohne Dekoration** – keine Schmuckbilder,
Emojis ohne Funktion, Floskeln oder Inhalte, die kein Auftrag braucht. Richtwerte und Beispiele:
`schuelermaterial.md`, falls vorhanden. Die Pflichtabschnitte (unten) stehen im Teil für die
Lehrkraft (nach `# Lösungen und Erwartungshorizont` bzw. `# Didaktische Hinweise`), nie im Teil für
Lernende.
Ausgenommen von den Richtwerten sind Klausur- und Abiturformat mit eigenen Regeln
(`klausur-erstellen`, `abiturvorschlag-erstellen`: Operator-Aufträge bis rund 40 bzw. 45 Wörter,
Antwortraum je Operator); kurz, eindeutig und ohne Dekoration bleiben auch sie.

**Zeichnungen** (Vorgabe der Fachberatung, 01.11.2026): Jede Zeichnung in einem Artefakt – Material
für Lernende, Lösung, Erwartungshorizont, Tafelbild, Entwurf, Begleitblatt – entsteht als **SVG aus
einer Spec** mit dem passenden Zeichen-Skill, dazu eine in diagrams.net bearbeitbare `.drawio.svg`,
eingebunden mit `![Alternativtext](abbildungen/….svg)` und kursiver Bildunterschrift. **Nie** als
Zeichnung aus Zeichen (ASCII-Art: Kästen aus ┌─┐ oder +---+, Pfeilketten, Struktogramm oder GRAFCET
im Codeblock), nie als Mermaid in der Ausgabe, nie als von Hand geschriebenes SVG.

| Zeichnung | Skill bzw. Weg |
|---|---|
| Blockschaltbild, Anlagen- und Systemübersicht, Ablauf, Regelkreis, Struktogramm, ER-Modell, UML, Relationenschema | `fachdiagramm-erstellen` |
| Kennlinie, Messwertdiagramm | aus den Werten per Code als SVG (z. B. matplotlib), Wertetabelle daneben |
| Foto, Werkstückzeichnung, fremde Abbildung | Datei mit Quelle und Lizenz, sonst Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle]` |
| Anlagenbild (Technologieschema), Schaltplanauszug mit Schaltzeichen, GRAFCET, Funktionsplan (FUP), Netzplan | `technologieschema-erstellen` |
| Simulationsschaltung | `circuitjs-schaltung-erstellen` |

Erlaubt bleiben Text-Tabellen derselben Inhalte (GRAFCET in Textform, Zuordnungsliste) für die
Zweitkorrektur und die Barrierefreiheit; Verzeichnisbäume und Programmcode sind keine Zeichnungen.
Lösungsbilder tragen `_loesung` im Namen und stehen nur im Teil für die Lehrkraft. **Ohne
Skriptausführung** (Assistent ohne Code) liefert der Skill die Spec und an der Stelle des Bildes den
Platzhalter `[ABBILDUNG: Inhalt – Spec <datei>.yaml]`; die Lehrkraft erzeugt das SVG lokal.
Vorhandenes Material mit Zeichnungen aus Zeichen wird beim Überarbeiten umgestellt. Prüfung:
`zeichnungen_pruefen.py`, falls vorhanden (❌ Zeichnung aus Zeichen, ⚠ Mermaid). Es öffnet auch jede
eingebundene SVG: ❌ Text über Text, Form oder Linie über Text, Text ragt aus seinem Kasten oder aus
dem Bild; ⚠ SVG ohne Spec und Werkzeugkennung (von Hand?), schräge Leitungen, Datei fehlt. Ein Skill,
der Zeichnungen braucht, ruft dafür das Zeichen-Skill auf oder bringt dessen Werkzeug mit
(`metadata.eduwerkzeuge`) – `pruefen` meldet einen `edu-*`-Befehl ohne beides.

**Dateinamen** (Nummer = Platz in der Planungskette):

| Nr. | Artefakt | Skill |
|---|---|---|
| 00 | Planungsakte | unterricht-entwickeln |
| 10 | DQR-Einordnung | dqr-zuordnen |
| 20 | Lernsituation | lernsituation-dokumentieren |
| 21 | LS-Analyse (Prüfbericht: Analysebogen, Phasencheck, Querschnitt, weitere Aspekte) | lernsituation-analysieren |
| 30 | Unterrichtsentwurf | unterrichtsentwurf-erstellen |
| 35 | Entwurfscheck (Selbstcheck/Beratung) | unterrichtsentwurf-analysieren |
| 36 | Unterrichtsreflexion (nach der Stunde: Selbstreflexion, Nachbesprechung) | unterricht-reflektieren |
| 40 | Unterrichtsmaterial | unterrichtsmaterial-erstellen |
| 41 | Experiment (Versuchsanleitung, Lehrerfassung, Gefährdungsbeurteilung) | experiment-planen |
| 42 | Fachdiagramm (Diagrammblatt, Specs unter `diagramme/`, SVG unter `abbildungen/`) | fachdiagramm-erstellen |
| 43 | Programmieraufgabe (Aufgabe, Codeordner `43_code/`, Erwartungshorizont) | programmieraufgabe-erstellen |
| 44 | Technikfolgenabschätzung (Dossier, Quellenmappe, Rollenkarten) | technikfolgen-abschaetzen |
| 45 | Taxonomie-Analyse | bloom-taxonomie |
| 46 | Technologieschema (Schemablatt mit Legende, Specs unter `schema/`, SVG unter `abbildungen/`) | technologieschema-erstellen |
| 47 | Simulationsschaltung (circuit.js: Schaltungstext, Messgeräte mit Erwartungswerten, Begleitblatt) | circuitjs-schaltung-erstellen |
| 48 | Mikrocontroller-Simulation (Wokwi: Spec, Projektordner mit Sketch, Schaltung und Szenarien, Zeitablauf, Begleitblatt) | wokwi-simulation-erstellen |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 70 | Klassenarbeit / Lernzielkontrolle mit Erwartungshorizont | klausur-erstellen |
| 75 | Abiturvorschlag (dezentral): Schüler- und Lehrermaterial je Vorschlag, Bewertungsbogen, Begleitblatt | abiturvorschlag-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

`abiturvorschlag-erstellen` (Nr. 75) hält Schüler- und Lehrermaterial einreichungsfertig: Kopf und
Pflichtabschnitte stehen im **Begleitblatt** (`75_abitur_<kurztitel>_begleitblatt.md`), nicht in den
Einreichungsunterlagen.

**Werkzeug-Skills** (Nr. 42, 46, 47, 48, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-technologieschema`, `schaltung.py`, `wokwi.py`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
Artefakt mit Pflichtabschnitten – diese hätten in der Quelle Folgen für die Ausgabe –, sondern
Kopf und Pflichtabschnitte stehen in einem **Begleitblatt** (`…_begleitblatt.md`,
Diagrammblatt). Nummern 92–96 (Ausspielen) folgen auf den Prüfbericht: veröffentlicht wird
geprüftes Material. Nr. 93 (agiles Lernen) kann auch für sich stehen, wenn eine Lehrkraft
selbst lernt; die Lernakte gehört dann der lernenden Person.

**Kopf jedes Artefakts:**

```yaml
---
artefakt: Lernsituation
titel: "Förderband nach Störung wieder in Betrieb nehmen"
skill: lernsituation-dokumentieren
skill_version: "1.0"
stand: 2026-10-08
bildungsgang: "Industriemechaniker/-in"
curriculare_vorgabe: "RLP Industriemechaniker/-in, LF 6"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
# optional:
bereich: planung            # planung | pruefen
vertraulich: false          # true bei unveröffentlichten Prüfungsvorschlägen o. Ä.
---
```

**Pflichtabschnitte am Ende jedes Artefakts:**

1. `## Qualitätscheck` – Tabelle *Kriterium | Ergebnis (✅/⚠️/❌) | Hinweis*. Ein ❌ wird vor
   der Ausgabe behoben; was sich nicht beheben lässt, wird zu ⚠️ mit Begründung.
2. `## Annahmen und Prüfaufträge` – alle `⚠️ Annahme:` und alle `🔎 Prüfen:` (Normen,
   Grenzwerte, Rechtsvorgaben, Herstellerangaben, regionale Besonderheiten).
3. `## Übergabe` – kurze Stichpunkte für Folge-Skills (z. B. Handlungsergebnis, zentrale
   Kompetenzen, Dateinamen) und **empfohlene nächste Skills**.
4. Transparenzhinweis als letzte Zeile:
   `> KI-gestützt erstellt (Skill <name> v<version>). Fachliche Prüfung und Verantwortung: Lehrkraft.`
   Die verantwortliche Rolle darf passend zum Artefakt abweichen (z. B. Lehrkraft bzw.
   Bildungsgangteam, Lernende und Fachexpertin); die Zeile beginnt immer mit `> KI-gestützt`, nennt
   Skill und aktuelle Version und steht in **einer** Zeile.

Ausnahmen: **Teilartefakte** tragen Kopf und Pflichtabschnitte im zugehörigen Begleitblatt bzw.
Erwartungshorizont;
**Akten** (Planungsakte) führen einen Verlauf;
**Lektionen** im Kursprojekt folgen `vorlage-lektion.md`, falls vorhanden (Kopf für die Seitenausgabe).

## 4. Fachliche Redlichkeit

- **Nichts erfinden:** keine ausgedachten Normnummern, Paragrafen, Zitate, Studien,
  Grenzwerte, URLs oder Quellen. Unsicheres wird markiert: `[🔎 Norm prüfen]`,
  `[🔎 Wert prüfen]`. „Weiß ich nicht sicher" ist ein gültiges Ergebnis.
- **Rechnen statt schätzen:** Zahlenwerte in Aufgaben und Lösungen werden nachgerechnet,
  Einheiten mitgeführt. Ist ein Code-Werkzeug verfügbar, wird es dafür benutzt.
- **Quellenlage offenlegen:** Unterscheiden zwischen *aus gelieferten Unterlagen* und *aus
  allgemeinem Fachwissen*. Gelieferte Ordnungsmittel haben Vorrang.
- **Fiktive Akteure klar fiktiv:** Firmen, Personen und Adressen in Handlungssituationen
  sind erkennbar ausgedacht („(fiktiv)“ beim ersten Auftreten); keine echten Telefonnummern,
  keine realen Personen; E-Mail-Adressen nur mit Beispiel-Domains (`example.org`, RFC 2606).

## 5. Datenschutz

- Für Begutachtungen, Rückmeldungen und KI-Chatbots gelten zusätzlich die **Leitplanken**
  (`references/leitplanken-bewertung.md`, falls vorhanden): Datenschutzstufen 0–2, keine
  Bewertung einzelner Lernender durch KI, Freigabe durch die Lehrkraft.
- Für Planung und Material werden **keine personenbezogenen Daten** gebraucht.
- Gibt die Lehrkraft Namen oder Leistungsdaten von Lernenden an, werden sie im Artefakt
  pseudonymisiert (S01, S02 …) und es folgt ein kurzer Hinweis.
- Keine Gesundheits-, Förder- oder Herkunftsangaben zu einzelnen Lernenden in Artefakten;
  Lerngruppen werden nur zusammenfassend beschrieben.

## 6. Begriffe und Bezugsrahmen

- Standard ist das **berufsbildende Schulwesen in Niedersachsen**. Für vollzeitschulische
  Bildungsgänge, besonders das **Berufliche Gymnasium** (Lerngebiete, Schuljahrgang,
  Notenpunkte, EPA), gilt zusätzlich `berufliches-gymnasium.md`, falls vorhanden. Verbindliche
  Begriffe nach **Leitlinie SchuCu-BBS 2024**: Handlungssituation, Handlungsergebnis,
  Handlungskompetenz mit **Fachkompetenz** (Wissen, Fertigkeiten) und **Personaler
  Kompetenz** (Sozialkompetenz, Selbständigkeit); vollständige Handlung in sechs Phasen
  (Informieren bzw. Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw.
  Kontrollieren · Reflektieren).
- **SchuCu-BBS 2024 ist verbindlich** (Entscheidung der Fachberatung, 19.10.2026): kein
  anderes Kompetenzmodell (etwa vier Dimensionen), keine anderen Phasen oder Begriffe. Eine
  Gliederung des Studienseminars oder der Schule darf gelten; ihre Abschnitte werden mit den
  Begriffen der Leitlinie gefüllt. Vorgaben anderer Länder übernehmen die Skills nicht.
- **Vollständige Handlung und Lernzeit**: Der
  Handlungskreis wird je Lernsituation geschlossen, aber nicht zwingend in 90 Minuten – er
  darf mehrere Unterrichtseinheiten umfassen (Entscheiden, Überprüfen mit Überarbeitung und
  Reflektieren der Lernsituation bleiben immer). Fachsystematische, lehrkraftgeführte
  Lernphasen sind zulässig, wo zweckdienlich und begründet; die Begründung wird dokumentiert
  (`lernsituationsmuster.md` Abschn. 12, falls vorhanden).
- **Didaktische Leitidee** (Planungshilfe der Bibliothek):
  `didaktische-leitidee.md`, falls vorhanden. Ein bis zwei Sätze, welche übertragbare Einsicht
  die Lernenden am exemplarischen Fall gewinnen und warum sie bedeutsam ist – für die
  Lernsituation (unter *didaktisch-methodische Kommentare*) und für die Stunde (vor dem
  Stundenziel). Sie ergänzt die Begriffe der Leitlinie und ersetzt keinen.
- Sprache: sachlich, geschlechtergerecht („Schülerinnen und Schüler", Abkürzung „SuS").
- Kompetenzen und Ziele werden mit **beobachtbaren Operatoren** formuliert
  (`references/operatoren-afb.md`, falls vorhanden). Nicht verwenden: *verstehen, kennen,
  wissen, lernen, sich bewusst sein*.

## 7. Selbstprüfung

Vor der Ausgabe prüft der Skill sein Ergebnis gegen die eigene Checkliste **und** gegen
diesen Vertrag (Annahmen markiert? Nichts erfunden? Pflichtabschnitte vorhanden? Material für
Lernende kurz, offen gestellt, anschaulich, ohne Dekoration? Jede Zeichnung als SVG aus einer
Spec, keine Zeichnung aus Zeichen – `zeichnungen_pruefen.py`, falls vorhanden?), behebt Mängel und
gibt erst dann aus.

## 8. Plattformen

- **Claude (Skills aktiviert):** Ordner als Skill installieren; Claude lädt ihn bei Bedarf.
- **Assistenten ohne Skill-Funktion (z. B. AIS-Chat.schule, fobizz):** Inhalt von
  `SKILL.md` als Anweisung des Assistenten einfügen, Dateien aus `references/` und
  `assets/` als Wissensbasis hochladen. Die Planungsakte wird dann von Hand zwischen den
  Assistenten weitergegeben.
- **Chatbots für Lernende** (Moodle-KI-Chat, AIS.chat-Lernszenario) bekommen keine
  Skill-Fassung, sondern eine eigene kurze Systemanweisung mit Probelauf (`ki-chatbot-einrichten`,
  im AIS-Paket `agiles-lernen-mit-ki`).

## Anhang: references/spec-format.md

# Spec einer Wokwi-Simulation (`48_wokwi_<kurztitel>.yaml`)

Die Spec bildet die Steuerungsaufgabe so ab, wie sie im Material steht. Aus ihr erzeugt
`scripts/wokwi.py` Sketch, Schaltung, Szenarien und Begleitblatt. Bedingungen stehen in der Schreibweise
des Notationsblatts (`notation-steuerungstechnik.md`). Vollständiges Beispiel mit Zähler, Flanke und
Alternativverzweigung: `assets/spec-muster.yaml`; Testlauf an einer Abituraufgabe: Beispiel
`beispiele/abitur-biogas-v2/48_wokwi_biogas-beschickung.yaml` der Bibliothek.

## 1. Kopf

| Schlüssel | Bedeutung | Standard |
|---|---|---|
| `titel` | Titel der Steuerung | „Steuerung“ |
| `kurztitel` | Dateiname `48_wokwi_<kurztitel>` (Kleinbuchstaben, Bindestriche) | aus dem Titel |
| `quelle` | Aufgabe, aus der die Spec stammt | – |
| `plattform` | `arduino-uno` oder `esp32` | `arduino-uno` |
| `zeitraffer` | `{faktor: 60, ab: 1min}` – Zeiten ab `ab` laufen 1:faktor, kürzere in Echtzeit; `{faktor: 1}` = Echtzeit | Echtzeit |
| `bildungsgang`, `curriculare_vorgabe`, `dqr`, `status`, `vertraulich` | Kopf des Begleitblatts | Platzhalter |
| `annahmen`, `pruefauftraege` | Listen; erscheinen im Begleitblatt als `⚠️ Annahme:` bzw. `🔎 Prüfen:` | leer |
| `einsatz` | Liste mit Einsatzideen für das Begleitblatt | drei Standardideen |

## 2. Zuordnungsliste

```yaml
eingaenge:          # digitale Geber
  - {bmk: -SJ1, name: "Taster Start", pin: D2, kontakt: "NO", bauteil: taster, signal_1: "Start betätigt"}
  - {bmk: -SJ2, name: "Taster Stopp", pin: D3, kontakt: "NC", bauteil: taster, signal_1: "Stopp nicht betätigt"}
  - {bmk: -BL1, name: "Schwimmerschalter", pin: D4, kontakt: "NC", bauteil: schalter,
     signal_1: "Füllstand über Mindesthöhe", start: 1, kurz: "Füllstand"}
analogeingaenge:    # 4 … 20 mA, Wert im Programm als physikalische Größe
  - {bmk: -BT1, name: "Temperaturfühler", pin: A0, bereich: [0, 100], einheit: "°C", start: 38, stellen: 1}
ausgaenge:
  - {bmk: -QA1, name: "Schütz Förderpumpe -MA1", pin: D8, signal_1: "Pumpe ein", kurz: "Pumpe"}
```

- **Pins** wie auf dem Board: `D2` … `D13`, `A0` … `A5` (Uno); `GPIO16` … (ESP32). E/A-Platine (Anlage der
  Bibliothek): Uno D2 … D7 Eingänge, D8 … D13 Ausgänge, A0/A1 analog; ESP32 GPIO16 … 19, GPIO25 … 27/32/33,
  GPIO34/35. Andere Pins sind erlaubt (Hinweis), D0/D1 bzw. GPIO1/3/6 … 11 nicht.
- **`kontakt`** NO oder NC, **immer in Anführungszeichen** (YAML 1.1 liest `NO` als falsch). Das Signal folgt der
  Spalte „Signal 1 bedeutet“; der Öffner liefert unbetätigt 1.
- **`bauteil`**: `taster` (tastend, in Szenarien steuerbar) oder `schalter` (Schiebeschalter für dauerhafte
  Signale – Schwimmer-, End-, Näherungsschalter; in Wokwi-Szenarien nicht steuerbar). `start`: Signal beim
  Start (Taster immer unbetätigt).
- **Analoggeber:** `bereich` [Anfang, Ende] des Messbereichs, `einheit`, `start` (Wert beim Start),
  `stellen` (Nachkommastellen in der Meldung), optional `rohbereich: [r4mA, r20mA]` (Standard der Plattform:
  Uno 205 … 1023, ESP32 480 … 2400 mV).
- **`kurz`** (optional): Kurzname für die Beschriftung in Wokwi (höchstens 9 bis 12 Zeichen); sonst erstes
  Wort aus `signal_1` bzw. `name`. **`farbe`** überschreibt die Farbe (green, black, red, white, blue, orange).
- **`taste`** (optional, Taster): Taste der Tastatur, die den Taster in Wokwi betätigt.

## 3. Merker

```yaml
merker:
  - {name: M_Pumpe, text: "Schrittkette fordert die Pumpe an"}            # aus GRAFCET-Aktion
  - {name: M_TempSperre, setzen: "[-BT1 < 30 °C]", ruecksetzen: "[-BT1 ≥ 32 °C]"}   # Speicher
  - {name: C_Teile, typ: int, text: "Zähler"}                             # Zähler (speichernde Aktion)
```

Ein Merker hat genau eine Quelle: GRAFCET-Aktion, Speicher (`setzen`/`ruecksetzen`, Standard rücksetzdominant;
`dominant: setzen` für SR) oder Verknüpfung. `typ: int` für Zähler; Zähler stehen nur in Vergleichen.

## 4. GRAFCET

```yaml
grafcet:
  - {schritt: 0, name: "Grundstellung", aktionen: [], transition: "-SJ1 · -BL1 → 1"}
  - {schritt: 3, name: "Beschicken", aktionen: [-PF2, -QA2, -QM1, M_Pumpe], transition: "[-BL2 ≥ 4,5 m] + 10min/X3 → 4"}
  - {schritt: 2, name: "Prüfen", aktionen: ["↑ C_Teile := C_Teile + 1"], transition: "[C_Teile < 10] → 1; [C_Teile = 10] → 3"}
```

- Initialschritt ist Schritt 0 (sonst `initial: true` am Schritt). Ein Schritt ist aktiv; je Zyklus höchstens ein
  Schrittwechsel.
- **Aktionen:** `-QA2` (kontinuierlich), `-MA1 wenn <Bedingung>` (mit Zuweisungsbedingung),
  `"↑ X := Wert"` bzw. `"↑ C := C + 1"` (speichernd bei Aktivierung), `"↓ X := 0"` (bei Deaktivierung). Speichernde
  Aktionen in Anführungszeichen.
- **Transition:** `Bedingung → Folgeschritt`; Alternativen mit `;` getrennt, die erste erfüllte gilt (Bedingungen
  müssen sich ausschließen). Parallelverzweigungen („→ 3 und 6“) simuliert der Skill nicht.
- **Zeit** nur am eigenen Schritt: `5min/X1` an der Transition aus X1.

## 5. Zwangssteuerung und Verknüpfungen

```yaml
erzwingen:      # vor den Transitionen, in dieser Reihenfolge; solange die Bedingung gilt, steht die Kette in `nach`
  - {bedingung: "¬-SJ2", nach: 0, grund: "Stopp: alle Ausgänge sofort 0"}
zuweisungen:    # nach den Aktionen; ein Ziel je Eintrag
  - {ziel: -QA1, bedingung: "M_Pumpe · -BL1 · -SJ2 · [-BT1 ≥ 30 °C]", grund: "Freigabe der Pumpe"}
```

Ein Ausgang kommt **entweder** aus GRAFCET-Aktionen **oder** aus einer Verknüpfung. Soll die Schrittkette einen
Aktor anfordern und ein Logikplan ihn freigeben, fordert die Kette einen Merker an (`M_Pumpe`), die Verknüpfung
setzt den Ausgang.

**Zyklus** (Sketch und Logikmodell gleich): Eingänge lesen → Speicher → Zwangssteuerung → Transitionen
(nur ohne Zwang) → Aktionen → Verknüpfungen → Ausgänge schreiben → Flanken merken.

## 6. Testfälle

```yaml
testfaelle:
  - nr: T1
    name: "Zyklus"
    zweck: "Schritte X1 … X6, 3 s zwischen Ventil und Pumpe"
    start: {-BL2: 3.0}                       # optional: Startwerte abweichend von der Zuordnungsliste
    ablauf:
      - {erwarte: {X: 0, -QA1: 0}}
      - {tippe: -SJ1, erwarte: {X: 1, -QA2: 1}}
      - {schrittzeit: 5min, vorher: {X: 1}, erwarte: {X: 2, -QM1: 1}}
      - {setze: {-BL2: 4.6}, erwarte: {X: 4, -QA1: 0}}
      - {druecke: -SJ2, erwarte: {X: 0}}
      - {loese: -SJ2, warte: 1s, erwarte: {X: 0}}
```

| Schlüssel | Wirkung |
|---|---|
| `setze` | Signale setzen: Digitalgeber 0/1 (Signal nach Zuordnungsliste), Analoggeber als Wert in der Einheit |
| `tippe` | Taster 200 ms betätigen und lösen (beim Öffner: Signal 0, dann 1) |
| `druecke`, `loese` | Taster betätigen bzw. lösen |
| `warte` | Aufgabenzeit warten (im Zeitraffer umgerechnet wie die Zeiten des GRAFCET) |
| `schrittzeit` | bis zur Zeitschwelle des aktiven Schritts: `vorher` 100 ms davor, `erwarte` 100 ms danach prüfen |
| `erwarte` | nach den Aktionen (bzw. 50 ms danach) prüfen: `X` (aktiver Schritt), Ausgänge, Merker, Eingänge |
| `text` | Kommentar |

**Abdeckung** (Erwartungen aus der Funktionsbeschreibung, nicht aus dem Programm):
1. Grundstellung (alle Ausgänge 0).
2. Normalablauf mit **jeder** Zeit (`schrittzeit` mit `vorher`) und dem Rücksprung.
3. Jede Verzweigung und jedes Ende über ODER (beide Wege, z. B. Füllstand **und** Zeit).
4. Stopp in einem laufenden Schritt, gehaltener Stopp sperrt den Start.
5. **Jede** Schutzfunktion: Wirkung sofort, Meldung, Neustart erst nach Wegfall (Hysterese an beiden Schwellen).
6. Startsperren (Start ohne Freigabe bleibt in X0, keine Störmeldung in der Grundstellung).

Analogwerte nicht genau auf eine Schwelle setzen (4,6 m statt 4,5 m) – der Rohwert ist gerundet.

## 7. Bedingungen

| Bedeutung | Schreibweise | im Sketch |
|---|---|---|
| UND, ODER, NICHT | `-SJ1 · -BG1`, `-BG2 + -BG3`, `¬-SJ2` (NICHT vor UND vor ODER, Klammern erlaubt) | `&&`, `||`, `!` |
| Flanke | `↑-SJ1`, `↓-BG1` | `(sj1 && !sj1_vorher)` |
| Zeit | `5s/X3` (ms, s, min, h; Komma erlaubt: `5,5h/X6`) | `schrittzeit() >= T_X3` |
| Schrittvariable | `X3`, `¬X0` | `schritt == 3`, `schritt != 0` |
| Vergleich | `[-BT1 ≥ 30 °C]`, `[C_Teile = 10]` (≥ ≤ > < = ≠; auch >= <= !=) | `bt1 >= 30.0` |
| immer | `1` | `true` |

Zahlen mit Dezimalkomma, Minus auch als „−“. Kennzeichen und Merker müssen in der Spec stehen; Einheiten im
Vergleich müssen zur Einheit des Messbereichs passen.

## 8. Befehle

```text
wokwi.py entwurf MATERIAL.md [--plattform …] -o SPEC.yaml   Gerüst aus Zuordnungsliste und GRAFCET-Textform
wokwi.py pruefen SPEC.yaml                                    Spec und Schaltung prüfen
wokwi.py erzeugen SPEC.yaml [-o ORDNER] [--ueberschreiben]    Projektordner schreiben
wokwi.py testen SPEC.yaml [--nur-logik] [--zeitablauf B.svg] [--test T1] [--serial] [--protokoll P.md]
wokwi.py blatt SPEC.yaml [-o BLATT.md] [--ueberschreiben]     Begleitblatt
wokwi.py vorschau SPEC.yaml [--png BILD.png]                  Bauteile mit @wokwi/elements, Pinprüfung
wokwi.py wokwi ORDNER [--timeout MS]                          Szenarien mit wokwi-cli
wokwi.py alles SPEC.yaml [--ueberschreiben]                   pruefen → erzeugen → testen → Zeitablauf → blatt
```

## Anhang: references/wokwi-format.md

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
