---
name: programmieraufgabe-erstellen
description: Erstellt Programmieraufgaben für berufsbildende Schulen und das Berufliche Gymnasium – Mikrocontroller (Arduino, ESP32) in C/C++, Python und CNC-Programme in G-Code (DIN 66025, PAL) – mit Ausgangssituation aus der Lernsituation, Anforderungen, Startcode, Testfällen mit Prüfwerten, gestuften Hilfen, Musterlösung und Erwartungshorizont, auch als Fehlersuchaufgabe mit dokumentierten Fehlern oder als Parsons-Aufgabe. Prüft lokal per Skript (Python-Syntax, C/C++ mit g++ und Arduino-Stub, Dezimalkomma, G-Code mit Vorschub, Kreisbögen, Spindel, Radiuskorrektur, Programmende, Verfahrbereich und PAL-Zyklen), erfindet keine Bibliotheksfunktionen, Pinbelegungen oder Steuerungsdialekte. Für Blockprogrammierung (App Inventor, Scratch) Aufgabe und Prüfliste ohne Skriptprüfung. Verwenden bei „Programmieraufgabe", „Arduino-Aufgabe", „ESP32 Messwert", „CNC-Programm schreiben lassen", „G-Code-Übung", „Fehlersuche im Code", „Code im Erwartungshorizont prüfen".
metadata:
  version: "1.5"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Programmieraufgabe erstellen

## Zweck
Programmieraufgaben, die eine Frage der Lernsituation lösen, auf dem vorhandenen Gerät laufen
und deren Musterlösung **geprüft** ist. Ein Erwartungshorizont mit Code, der nicht kompiliert,
oder ein CNC-Programm mit falschem Kreisbogen kostet im Unterricht mehr Zeit als jede andere
Panne.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

**Nichts erfinden:** keine Bibliotheksfunktionen, Pinbelegungen, Sensorkennlinien oder
Zyklusparameter aus dem Gedächtnis. Was vom Gerät abhängt (Board, Sensor, Steuerung, Dialekt),
steht als Annahme im Kopf oder wird aus dem gelieferten Datenblatt bzw. Handbuch übernommen.

## Drei Modi

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Neue Aufgabe** | „ESP32 soll den Volumenstrom anzeigen – Aufgabe für Jg. 13" | Aufgabe mit Startcode, Testfällen, Hilfen, Musterlösung, Erwartungshorizont |
| **B Code prüfen** | „Stimmt der Code im Erwartungshorizont?" | Prüfbericht des Skripts mit Korrekturvorschlag |
| **C Fehlersuche** | „Fehlersuchaufgabe zum Flansch-Programm" | Code mit 3–5 dokumentierten Fehlern, Lösung mit Begründung |

## Eingaben
- **Pflicht (sonst Rückfrage):** Ziel der Aufgabe bzw. Bezug zur Lernsituation, Sprache bzw.
  Steuerung.
- **Wichtig, sonst Annahme:** Board bzw. Steuerung und Dialekt (Arduino Uno, ESP32; DIN 66025,
  PAL, herstellerspezifisch), Entwicklungsumgebung, Sensor mit Datenblatt, Vorwissen,
  Bearbeitungszeit, Einzel- oder Partnerarbeit.
- **Optional:** vorhandener Code, Zeichnung bzw. Rohteilmaße, Datenblätter, Tabellenbuch.

## Vorgehen (Modus A)
1. **Aufgabe aus der Situation:** Was soll das Programm im Auftrag leisten? Messbare
   Anforderungen (Eingaben, Ausgaben, Einheiten, Grenzwerte) als Tabelle; Situation in
   höchstens drei Sätzen (`references/schuelermaterial.md`). Dazu die **Darstellung, mit der
   programmiert wird:** Anschlussbild bzw. Schaltplan (Pins, Sensor, Aktor; Schaltplanauszug mit `technologieschema-erstellen`), Sensorkennlinie als Diagramm aus den Datenblattwerten (SVG per Code), Ablauf-, Zustands- oder
   Struktogramm (`fachdiagramm-erstellen`), beim G-Code die Werkstückzeichnung mit Maßen und
   Nullpunkt (Platzhalter, wenn sie nicht vorliegt). Sie ersetzt Erklärtext. Alle Zeichnungen –
   auch Struktogramm und Ablauf der Musterlösung – als SVG, nie als Zeichnung aus Zeichen im Codeblock.
2. **Didaktische Form wählen** (`references/programmierdidaktik.md`): PRIMM (vorhersagen,
   ausführen, untersuchen, verändern, selbst schreiben), Parsons-Aufgabe, Lückencode,
   Fehlersuche oder offene Aufgabe – passend zu Vorwissen und Niveau.
3. **Startcode** mit Gerüst und Kommentaren; was die Lernenden ergänzen, ist markiert. Das
   Gerüst gibt Struktur, nicht den Lösungsweg Zeile für Zeile; Lückencode nur, wo das Lernziel
   eine bestimmte Stelle ist.
4. **Testfälle mit Prüfwerten** (Eingabe → erwartete Ausgabe mit Einheit), auch Grenz- und
   Fehlerfälle; beim G-Code Prüfmaße und Simulation. Die Spezifikation legt fest, was mehrere
   Lösungen erzeugen würde (`references/aufgabenmuster-informationstechnik.md`, B1–B14): Signale mit
   Aktivpegel, vorgegebene Namen, Beispiel **und** Gegenbeispiel, Randfall, erlaubte bzw. verbotene
   Bibliotheksfunktionen; hardwarenahe Muster H1–H10, Algorithmen S5.
5. **Gestufte Hilfen** (Hinweis → Teilschritt → Teillösung; die letzte Hilfe löst nicht alles).
6. **Musterlösung** schreiben und **prüfen:**
   `python3 scripts/code_pruefen.py 43_code/DATEI [--rohteil "X-…:…,Y-…:…,Z-…:0"]`
   (Markdown, DOCX und PDF mit Codeblöcken über `scripts/text_lesen.py`). Jedes ❌ beheben; ⚠ zu
   Bibliotheken oder Dialekt als Prüfauftrag übernehmen. Messkette nachrechnen (ADC → Spannung →
   physikalische Größe → Einheit; `references/mikrocontroller.md`).
7. **Erwartungshorizont:** Kriterien Funktion (Testfälle), Struktur, Kommentar, Fehlerbehandlung
   bzw. beim G-Code Maßhaltigkeit, Technologiewerte, sichere Anfahr- und Abfahrwege.
8. **Operatoren:** im Beruflichen Gymnasium EPA-Operatoren (*entwickeln, entwerfen, überprüfen*);
   *programmieren* oder *implementieren* nur als erweiterte Operatoren im Lehrermaterial
   (`references/operatoren-epa-technik.md`).

**Modus B:** Code aus Material oder Erwartungshorizont mit dem Skript prüfen, zusätzlich die
Messkette und die Kommentare lesen (Reste aus Tutorials, fehlende Einheiten). Code, der nur als
Bild vorliegt, abschreiben und als Abschrift kennzeichnen. **Modus C:** Fehler wählen, die zum
Lernziel passen (Dezimalkomma, falsche Kreisrichtung, fehlende Radiuskorrektur-Abwahl,
Einheitenfehler in der Messkette); jeden Fehler mit Zeile, Wirkung und Korrektur in der Lösung.

## Ausgabe
- `43_programmieraufgabe_<kurztitel>.md` nach `assets/vorlage-programmieraufgabe.md`:
  Schülerfassung (Situation, Anforderungen, Startcode, Testfälle, Hilfen) → `# Lösungen und
  Erwartungshorizont` → `# Didaktische Hinweise` → Pflichtabschnitte.
- Codeordner `43_code/` mit Startcode und Musterlösung als eigene Dateien (`.ino`, `.py`, `.nc`).

## Qualitätscheck
- [ ] Aufgabe aus der Lernsituation, Anforderungen messbar, Einheiten angegeben?
- [ ] Startcode lauffähig gerüstet; zu ergänzende Stellen markiert?
- [ ] Testfälle mit Prüfwerten, Grenz- und Fehlerfall?
- [ ] Musterlösung mit `code_pruefen.py` ohne ❌; Messkette nachgerechnet?
- [ ] Keine erfundenen Bibliotheken, Pins, Kennlinien oder Zyklusparameter (sonst 🔎)?
- [ ] Gestufte Hilfen, letzte Hilfe nicht vollständig lösend?
- [ ] Aufgabe kurz, mit Darstellung (Anschlussbild, Kennlinie, Ablauf bzw. Werkstückzeichnung),
      Schritte nur in den Hilfen – `schuelermaterial_pruefen.py` ohne ❌?
- [ ] Operatoren passend zur Schulform (EPA im BG)?

## Beispielaufrufe
> „Programmieraufgabe zur LS ING3.1: ESP32 liest einen analogen Durchflusssensor und gibt den
> Volumenstrom in l/min seriell aus. Arduino-IDE, Jg. 13, 90 Minuten."

> „Prüf den C++-Code und das CNC-Programm im Erwartungshorizont der LS ING3.1."

> „Fehlersuchaufgabe: CNC-Programm für einen Flansch mit fünf Fehlern, PAL."

## Referenzen – wann lesen
- `assets/vorlage-programmieraufgabe.md` – **immer** (Ausgabeformat).
- `references/programmierdidaktik.md` – Aufgabenformen, Testfälle, Hilfen, Bewertung, KI-Assistenz. **Immer.**
- `references/mikrocontroller.md` – Messkette, ADC, Spannungspegel, Grenzen der Prüfung.
- `references/aufgabenmuster-informationstechnik.md` – Aufgabentypen mit Schablone, Festlegungen und
  Prüfstein: Zustandsautomat, Initialisierung, Timer, ISR, PWM, Bus; Algorithmen zu Fachregeln.
- `references/gcode-grundlagen.md` – Satzaufbau, Wegbedingungen, Radiuskorrektur, Zyklen, Dialekte.
- `references/operatoren-afb.md`, `references/operatoren-epa-technik.md` – Operatoren je Schulform.
- `references/berufliches-gymnasium.md` – BG: Lerngebiete, Fach Praxis, Hilfsmittel PC.
- `references/schuelermaterial.md` – Aufgabe für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/code_pruefen.py` (mit `scripts/text_lesen.py`) – Codeprüfung, lokal.
- `scripts/schuelermaterial_pruefen.py` – Form der Aufgabe (Länge, Darstellungen, Dekoration).
