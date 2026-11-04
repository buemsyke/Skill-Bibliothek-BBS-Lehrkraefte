---
name: circuitjs-schaltung-erstellen
description: Baut zuverlässige Versuchsschaltungen für den Simulator circuit.js (Falstad) aus einem Katalog geprüfter Vorlagen – Gleichstrom (Ohmsches Gesetz, Reihen- und Parallelschaltung, Spannungsteiler, Brücke, RC- und RL-Schaltvorgang), Wechselstrom (R, L, C, Schwingkreis, Kompensation, Transformator, Filter, Drehstrom) und Elektronik (Gleichrichter, Z-Diode, Tief- und Hochsetzsteller). Setzt Voltmeter und Amperemeter an die richtigen Stellen, rechnet Erwartungswerte und misst jede Schaltung per Skript in der Falstad-Engine; dazu ein Begleitblatt mit Rechenweg und Beobachtungshinweisen. Verwenden bei „circuit.js Schaltung", „Falstad Versuch", „Simulation Gleichstrom", „Wechselstrom simulieren", „Gleichrichter simulieren", „Tiefsetzsteller", „Messschaltung mit Voltmeter und Amperemeter". Nicht für Realversuche mit Gefährdungsbeurteilung (experiment-planen) und nicht für Schaltplanauszüge im Material (technologieschema-erstellen).
metadata:
  version: "1.3"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# circuit.js-Schaltung erstellen

## Zweck
Eine Versuchsschaltung für den Simulator, die **sofort läuft, richtig misst und zur Norm passt**:
rechtwinklig im Raster, Messgeräte in Reihe bzw. parallel, Bezeichner an jedem Bauteil, Werte, die
zur Rechnung der Lernenden passen. Freihändig geschriebene Falstad-Zeilen scheitern an Kleinigkeiten
(Anschluss mitten auf einer Leitung, falsche Zählrichtung, fehlende Masse, Einschalttransient).
Deshalb entsteht die Schaltung aus **geprüften Vorlagen** und wird vor der Ausgabe geprüft und gemessen.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen · einheitlicher Kopf und Pflichtabschnitte
(Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis). Details:
`references/skill-vertrag.md`. Der Skill ruft keinen anderen Skill selbst auf.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht (sonst Rückfrage):** was gezeigt oder gemessen werden soll (Schaltung oder Thema).
- **Wichtig, sonst Annahme:** Bauteilwerte und Quellenspannung (Standardwerte der Vorlage), Gleich- oder
  Wechselspannung und Frequenz, Zielort (Seite im Simulationsprojekt `uebungen/`, Moodle, Folie).
- **Optional:** Aufgabenblatt, Handlungssituation, Ziel-Bildungsgang. Das Projekt „Simulationen
  Grundlagen Elektrotechnik“ (Ordner mit `falstad/`, `uebungen/`, `js/circuit-loader.js`) liefert den
  Rahmen; ohne Projekt wird nur der Schaltungstext erzeugt.

## Vorgehen
1. **Vorlage wählen:** `python3 scripts/schaltung.py vorlagen` (Katalog in
   `references/schaltungskatalog.md`). Passt keine Vorlage, die ähnlichste wählen und mit dem
   Baukasten `scripts/falstad_bau.py` abwandeln; nie Koordinaten „aus dem Gedächtnis“ schreiben.
2. **Werte festlegen:** Standardwerte der Vorlage nehmen oder Parameter setzen
   (`--u 12 --r1 100`). Werte so wählen, dass Zeigerausschläge sinnvoll sind (Ströme in mA bis A,
   Spannungen unter 50 V im Unterricht, Netzspannung nur bei ausdrücklichem Netzbezug).
3. **Erzeugen:** `python3 scripts/schaltung.py vorlage <name> [Parameter] -o 47_schaltung_<kurztitel>.txt`;
   `--js` liefert den Block `const circuit = …` für die Seite, `--json` Erwartungswerte,
   Hinweise und Formeln für das Begleitblatt.
4. **Prüfen:** `python3 scripts/schaltung.py pruefen 47_schaltung_<kurztitel>.txt` – Raster,
   offene Anschlüsse, Berührung ohne Verbindung, Überlappung, Messgeräte (Amperemeter nicht
   kurzgeschlossen, Voltmeter nicht am selben Knoten, Polung, Kreissymbol), Nachrechnung linearer
   Schaltungen. Jedes ❌ beheben.
5. **In der Engine messen:** `python3 scripts/schaltung.py vergleich <name> [Parameter]` bei Vorlagen,
   `pruefen DATEI --engine` bei eigenen Schaltungen. Formelwert und Engine-Anzeige müssen
   innerhalb der Toleranz liegen. Ist Chromium oder Falstad nicht vorhanden (Ausgabe „Engine nicht
   verfügbar“, Code 2), steht im Begleitblatt `🔎 Prüfen: in der Engine nicht gemessen`.
6. **Begleitblatt** nach `assets/vorlage-schaltungsblatt.md`: Schaltung, Messgeräte mit
   Erwartungswerten und Rechenweg, Hinweise zur Beobachtung, Einbau in die Seite.
7. **Einbinden (falls Projekt vorhanden):** den `const circuit`-Block in die Seite `uebungen/NN-….html`
   einsetzen, Seite im Browser öffnen (lokaler Server, `schaltung.py url`) und die Messgeräte
   mit der Rechnung vergleichen. Dateien des Projekts nicht überschreiben; neue Seite oder Kopie mit Suffix.

## Regeln
- **Darstellung** wie in den vorhandenen Versuchen: weißer Hintergrund, Widerstand als Rechteck,
  technische Stromrichtung (Parameter von `CircuitLoader`), Schaltzeichen normnah; Quelle links,
  Verbraucher rechts, Plus oben (`references/darstellung-din.md`).
- **Messgeräte:** Amperemeter (Kreis mit A) nur in Reihe, Voltmeter (Kreis mit V) nur parallel;
  Gesamtstrom an der Quelle, Zweigströme je Zweig, Spannung an jedem Bauteil, das die Aufgabe
  braucht. Wechselgrößen und Gleichrichterströme als Effektivwert. Die Messgeräte sind ideal
  (0 Ω bzw. unendlich); Messabweichungen nur mit ergänztem Innenwiderstand und Kennzeichnung.
- **Erwartungswerte** stammen aus Formeln und tragen den Vermerk *Erwartung aus Rechnung*; bei
  Dioden und MOSFETs sind es Näherungen, die Engine-Messung gilt.
- **Halbleiter:** Masse setzen; Zeitschritt der Vorlage beibehalten.
- **Netzspannung:** `ac-kompensation`, `drehstrom-stern` und `ac-transformator` können mit 230 V
  arbeiten. Im Modell ungefährlich, aber der reale Aufbau gehört nur in die Hand von
  Fachkräften; im Begleitblatt `🔎 Prüfen: Realversuch nur nach Gefährdungsbeurteilung` (siehe
  `experiment-planen`, wenn ein Realversuch folgt).
- **Nichts erfinden:** Normnummern stehen als `🔎 Norm prüfen`; Bauteilwerte realer Geräte nicht
  aus dem Gedächtnis.

## Ausgabe
Datei `47_schaltung_<kurztitel>.txt` (Falstad-Text, im Ordner der Planungsakte oder neben der Seite)
und Begleitblatt `47_schaltung_<kurztitel>_begleitblatt.md`. Weitere Dateien nur auf Wunsch
(Seite für `uebungen/`).

## Qualitätscheck
- [ ] Vorlage oder Baukasten verwendet, keine freihändigen Koordinaten?
- [ ] `schaltung.py pruefen` ohne ❌, Warnungen begründet?
- [ ] Voltmeter parallel, Amperemeter in Reihe, alle Anzeigen positiv und beschriftet?
- [ ] Formelwerte gegen Engine geprüft (oder Prüfauftrag vermerkt)?
- [ ] Darstellung wie die vorhandenen Versuche (weiß, Rechteck-Widerstand, DIN-Kreissymbole)?
- [ ] Masse bei Halbleiterschaltungen, Zeitschritt passend, kein Einschaltgleichanteil?
- [ ] Begleitblatt mit Erwartungswerten, Rechenweg, Annahmen und Prüfaufträgen?
- [ ] Beobachtungshinweise und Aufgabentext für Lernende kurz und offen gestellt
      (`references/schuelermaterial.md`); Schaltpläne im Begleitblatt als SVG, keine Zeichnung aus
      Zeichen (`python3 scripts/zeichnungen_pruefen.py 47_*.md` ohne ❌)?

## Beispielaufrufe
> „Baue eine Reihenschaltung mit drei Widerständen und Messgeräten für die Seite 03 im Simulationsprojekt.“

> „Ich brauche einen Reihenschwingkreis mit R = 20 Ω, L = 0,2 H, C = 47 µF in Resonanz.“

> „Zeige den Tiefsetzsteller mit Tastgrad 0,25 bei 24 V Eingangsspannung.“

## Referenzen – wann lesen
- `references/falstad-format.md` – **immer**, wenn eine Schaltung von Hand abgewandelt wird (Zeilenformate, Fallen).
- `references/schaltungskatalog.md` – **immer** (Vorlagen, Parameter, Messgeräte, Lücken).
- `references/darstellung-din.md` – Darstellung, Messgeräteregeln, Einbau in das Projekt.
- `assets/vorlage-schaltungsblatt.md` – **immer** (Ausgabeformat).
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/schaltung.py` – Befehle `vorlagen`, `vorlage`, `pruefen`, `engine`, `vergleich`, `url`.
- `scripts/falstad_bau.py` – Baukasten in Rasterpunkten; `scripts/falstad_kern.py` – Prüfung und Nachrechnung;
  `scripts/falstad_vorlagen.py` und `scripts/falstad_elektronik.py` – Vorlagen; `scripts/engine_pruefen.py` – Messung in Chromium.

## Empfohlene Folge-Skills
`unterrichtsmaterial-erstellen` (Aufgabenblatt zur Schaltung), `experiment-planen` (Realversuch mit
Gefährdungsbeurteilung), `fachdiagramm-erstellen` (Kennlinien aus Messwerten), `material-pruefen`.
