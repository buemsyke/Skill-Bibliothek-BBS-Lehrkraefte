---
name: technologieschema-erstellen
description: Erstellt Technologieschemata (Anlagenbilder für Steuerungsaufgaben) aus einer kurzen YAML-Beschreibung. Zylinder mit Endlagensensoren, Ventile, Sensoren, Taster, Motoren, Pumpen, Behälter und Schaltzeichen nach DIN EN 60617 setzt das mitgelieferte Werkzeug edu-technologieschema zu SVG und bearbeitbarer drawio.svg zusammen, mit Referenzkennzeichen nach DIN EN IEC 81346-2:2020, Legende und Schemablatt. GRAFCET nach DIN EN 60848 als eigenes Bauteil mit Prüfung und Textform; nach Muster auch Funktionsplan (FUP) und Netzwerkplan als Aufgaben- oder Lösungsbild. Verwenden bei „Technologieschema zeichnen“, „Anlagenbild für die Steuerungsaufgabe“, „GRAFCET zeichnen“, „Ablaufsteuerung als GRAFCET“, „Funktionsplan zeichnen“, „Netzwerkplan“, „ASCII-Skizze einer Anlage ersetzen“. Nicht für Blockschaltbild, Struktogramm, ER- oder UML-Diagramm (fachdiagramm-erstellen) und nicht für vollständige Stromlaufpläne, Pneumatik-/Hydraulikpläne oder technische Zeichnungen.
metadata:
  version: "1.7"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  eduwerkzeuge: "technologieschema"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Technologieschema erstellen

## Zweck
Das Bild zur Steuerungsaufgabe: **die Anlage, wie Lernende sie vor sich sehen** – Zylinder, Sensoren,
Ventile, Bedienelemente, Werkstück und Bewegungsrichtungen. Es ersetzt weder Schaltplan noch
Pneumatikplan; es zeigt, **was wo sitzt**, damit Funktionsbeschreibung, Zuordnungsliste und
Programm darauf Bezug nehmen können. Claude beschreibt die Anlage in einer YAML-Spec; Zeichnung,
Anker, Prüfung und Legende übernimmt `edu-technologieschema`. Kein von Hand geschriebenes SVG.
Jede Abbildung gibt es **zweimal**: als Bild (`.svg`) und als **bearbeitbare Zeichnung**
(`.drawio.svg`), die die Lehrkraft in diagrams.net weiterbearbeitet – Bauteile verschieben,
Kennzeichen und Texte ändern, Bauteile kopieren, ohne dass Linien abreißen.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Schemablatt). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Wann dieser Skill, wann ein anderer
| Inhalt | Skill |
|---|---|
| Bild der **Anlage** mit Betriebsmitteln (Technologieschema) | dieser Skill |
| Blockschaltbild, Ablauf, Regelkreis, Struktogramm, ER, UML | `fachdiagramm-erstellen` |
| Auszug eines Stromlaufplans mit Schaltzeichen (Steuerstromkreis, Sensoranschluss) | dieser Skill (`typ: symbol`) |
| GRAFCET (Ablaufkette mit Aktionen, Transitionen, Rücksprung) | dieser Skill, eigenes Bauteil `typ: grafcet` nach `assets/spec-grafcet.yaml` |
| Funktionsplan (FUP, Logikplan mit &, ≥1, Vergleicher) | dieser Skill, Grundformen nach `assets/spec-fup.yaml` |
| Netzplan (Gebäude, Switches, Router, LWL/Kupfer/VPN) | dieser Skill, Grundformen (`rechteck`, `text`, `linie`) |
| vollständiger Stromlaufplan, Pneumatik-/Hydraulikplan, technische Zeichnung | Fachsoftware – hier nicht |

Zeichnungen aus Zeichen (ASCII-Art) gibt es in der Bibliothek nicht (Skill-Vertrag Abschn. 3): Auch
Lösungsbilder im Erwartungshorizont – GRAFCET, FUP, Netzplan – entstehen hier als SVG.

## Eingaben
- **Pflicht (sonst Rückfrage):** welche Anlage – Aufgabentext, Skizze, Foto, ASCII-Zeichnung oder
  Beschreibung der Teile und Bewegungen.
- **Wichtig, sonst Annahme:** Verwendung (Übung, Klassenarbeit, Abitur, Tafelbild), Grundstellung,
  Bildgröße, Aufgabenbild oder Lösungsbild. Kennzeichen sind **immer** nach DIN EN IEC 81346-2:2020;
  Vorlagen mit anderer Schreibweise (S1, Y1) werden umgestellt (Entsprechungen in der Legende nennen).
- **Optional:** Planungsakte, vorhandene Funktionsbeschreibung und Zuordnungsliste (Kennzeichen
  übernehmen), Abbildungsnummer.

## Leitlinien (verbindlich)
1. **Nur zeigen, was die Aufgabe nennt.** Jedes Betriebsmittel der Aufgabe steht im Bild und in der
   Legende, nichts darüber hinaus. Fehlt eine Angabe (Lage eines Sensors, Wirkrichtung), Annahme
   markieren oder `🔎 Prüfen:`.
2. **Bild plus Text-Legende.** Kennzeichen im Bild sind für Prüfskripte und Zweitkorrektur
   unsichtbar; die Legende (Referenzkennzeichen | Betriebsmittel | Lage/Aufgabe) kommt aus
   `edu-technologieschema legende` und steht neben dem Bild. Kontaktart (NO/NC) und
   Bedeutung der Signale stehen in Funktionsbeschreibung und Zuordnungsliste, nicht im Bild.
3. **Referenzkennzeichen immer nach aktueller Norm** (DIN EN IEC 81346-2:2020; immer Klasse und Unterklasse: -SJ1, -MA1,
   -MM1, -EA1, -BR1; Notationsblatt `references/notation-steuerungstechnik.md`). Das Werkzeug lässt keine
   andere Schreibweise zu: Form, Klasse und Unterklasse nach Tabelle 2, **Klasse passend zum
   Bauteil** (Taster S, Sensor B, Zylinder M, Leuchtmelder P), Kennzeichen der Ausgabe 2009 sind
   ❌, die Klasse allein (-S1, -M1) ist ❌ „Unterklasse fehlt“, **eine Tiefe je Klasse** (nie
   -MM1 neben -MMB1). Dieselben
   Kennzeichen wie in Legende, Aufgaben und Musterlösung.
4. **Wirkungslinien rechtwinklig.** Linien und Rohre verlaufen waagerecht oder senkrecht; das
   Werkzeug fügt bei schrägen Punktpaaren einen Knick ein und warnt bei kleinem Versatz
   (Positionen angleichen). Schräg nur mit `schraeg: true` und gutem Grund; geneigte Teile
   (Förderband) sind erlaubt, die Verbindungen dazu bleiben rechtwinklig.
5. **Schaltzeichen nach DIN EN 60617**, wo ein Bauteil als Zeichen statt als Bild dargestellt
   wird (`typ: symbol`, Liste mit `edu-technologieschema symbole`). Zeichen mit der Herkunft
   *abgleichen* stehen in der Liste mit 🔎: vor dem Einsatz mit Norm oder eingeführtem Tabellenbuch
   vergleichen und im Schemablatt vermerken. Zeichen nicht erfinden und nicht von Hand in Pfaden
   nachbauen.
6. **Grundstellung zeigen** und in der Fußzeile nennen (Zylinder eingefahren, Werkstück am
   Anschlag, Füllstand zwischen -BG1 und -BG2). Bild und Text stimmen überein.
7. **Das Bild verrät die Lösung nicht:** keine Soll-Abläufe, Schrittnummern, Signalzustände oder
   beschriftete Wirkungen. Lösungsbilder (Zustand nach einem Schritt, Markierungen) sind eigene
   Specs mit Namen `…_loesung` und gehören nur ins Lehrermaterial.
8. **Fachlich richtig vor schön:** Bauteile, Bewegungsrichtungen und Lage wie in der Aufgabe oder
   in Herstellerunterlagen; Vereinfachungen im Schemablatt benennen („ohne Sicherheitseinrichtungen“).
   Keine Normzeichnung vortäuschen.
9. **Lesbar im Druck:** nur Graustufen (Farbe trägt nie die Bedeutung), kurze Beschriftungen,
   Schrift 11–13 Pixel bei 720–780 Pixel Breite, höchstens etwa 15 Bauteile je Bild – sonst zwei
   Bilder (Anlage und Bedienfeld).
10. **Barrierefrei:** Alternativtext (ein Satz mit den Kennzeichen), Bildunterschrift und
   `<title>` „Abbildung N – Titel“ sind Pflicht.
11. **Vorlagen Dritter:** Eine Abbildung aus Buch, Webseite oder Aufgabensammlung wird nur
   nachgezeichnet, wenn die Rechte geklärt sind; die Quelle steht im Schemablatt. Besser: eigene
   Anlage aus der Aufgabenbeschreibung entwerfen. Kopien fremder Bilder gehören nicht in den Skill.
12. **Die Spec ist die Quelle:** Änderungen in der YAML, dann neu erzeugen. Hat die Lehrkraft die
   `.drawio.svg` in diagrams.net bearbeitet, ist **diese Datei** die Quelle: nicht ungefragt neu
   erzeugen (ihre Änderungen gingen verloren); geänderte Kennzeichen prüft dort kein Werkzeug – Legende
   und Zuordnungsliste von Hand abgleichen.
13. **Bearbeitbar ausliefern:** immer `.drawio.svg` mitgeben (nicht `--ohne-drawio`), außer die Lehrkraft
   will nur das Bild. Eine `.drawio.svg` ist zugleich SVG – Browser, Word und Markdown zeigen sie als Bild.
14. **GRAFCET nur als `typ: grafcet`** (nie aus Rechtecken und Linien): Die Spec nennt die Struktur, das
   Werkzeug zeichnet die Normsymbole (`references/technologieschema-specs.md` Abschn. 5a, Schreibweise
   `references/notation-steuerungstechnik.md`). **Speichernde Aktionen haben immer beides:** die
   **Zuweisung** im Rechteck (`-QA1 := 1`, nicht `-QA1`) und den **Auslöser** am Rechteck (Pfeil bei
   Aktivierung oder Deaktivierung, Fähnchen bei Ereignis); `pruefen` meldet sonst ❌. Negation erscheint als
   Überstrich, Kommentare in Anführungszeichen. Immer `zuordnung` angeben, wenn eine Zuordnungsliste
   vorliegt; gibt eine fremde Aufgabe ältere Kennzeichen vor (`-SF1`), bleiben sie darüber erhalten (⚠).
   Als Lösungsbild (`…_loesung_…`) nur im Lehrerteil; die Text-Tabelle für die Zweitkorrektur kommt aus
   `edu-technologieschema textform`, nicht von Hand.
15. **FUP und Netzplan aus Grundformen** (Bausteine wie DIN EN 61131-3; Spec-Referenz Abschn. 5b): Elemente
   ohne Betriebsmittel tragen `ref` und `legende: false`.

## Vorgehen
1. **Anlage klären:** Bauteile, Bewegungen, Sensoren und Bedienelemente mit Kennzeichen sammeln
   (Aufgabentext Satz für Satz durchgehen); Verwendung und Notation festlegen.
2. **Anordnen:** Bereiche planen (Bedienfeld oben links, Prozess in der Mitte, Werkstückfluss von
   links nach rechts), Raster von 10 Pixeln, Rand mindestens 40 Pixel. Maße und Teile in
   `references/technologieschema-specs.md`, Muster in `assets/`.
3. **Spec schreiben:** `schema/46_<kurztitel>.yaml` mit `out: abbildungen/46_<kurztitel>`; im
   Abitur-Projekt die Namen des Projekts übernehmen (z. B. `…_abbN_<thema>`). Ausgangspunkt ist
   das passende Muster: `assets/spec-biegestation.yaml` (Zylinder), `assets/spec-tankanlage.yaml`
   (Behälter, Rohre, Pumpe), `assets/spec-foerderstation.yaml` (Band, Lichtschranke),
   `assets/spec-steuerstromkreis.yaml` (Schaltzeichen, Taster, Verbindungspunkte),
   `assets/spec-naeherungsschalter.yaml` (Näherungsschalter an Relais), `assets/spec-grafcet.yaml`
   (GRAFCET-Kette), `assets/spec-grafcet-verzweigung.yaml` (parallel, alternativ, alle Aktionsarten),
   `assets/spec-grafcet-teil.yaml` (einschließender Schritt, Zwangssteuerung), `assets/spec-fup.yaml`
   (Funktionsplan). Alle GRAFCET-Symbole: `assets/spec-grafcet-symbole.yaml`.
   Schaltzeichen: `references/schaltzeichen.md` bzw. `python3 scripts/edu.py technologieschema symbole`.
4. **Prüfen:** `python3 scripts/edu.py technologieschema pruefen schema/46_<kurztitel>.yaml` –
   alle ❌ beheben, jedes ⚠ ansehen (überlappende Beschriftungen, Linien durch Texte).
5. **Erzeugen:** `python3 scripts/edu.py technologieschema svg schema/46_<kurztitel>.yaml`
   (oder installiert `edu-technologieschema svg …`) – schreibt `.svg` und `.drawio.svg`.
6. **Ansehen:** `python3 scripts/vorschau_png.py abbildungen/46_<kurztitel>.svg` und die PNG
   betrachten – Teile am richtigen Ort, Pfeile in der richtigen Richtung, Beschriftungen frei,
   Grundstellung wie in der Fußzeile? Spec anpassen, neu erzeugen.
7. **Legende:** `python3 scripts/edu.py technologieschema legende schema/46_<kurztitel>.yaml`;
   Spalte *Lage / Aufgabe* ergänzen, wo die Aufgabe mehr sagt. Beim GRAFCET stattdessen die **Textform**:
   `python3 scripts/edu.py technologieschema textform schema/46_<kurztitel>.yaml`.
8. **Schemablatt** nach `assets/vorlage-schemablatt.md`: Einbindung, Alternativtext, Legende,
   Grundstellung, Vereinfachungen, Quelle, Qualitätscheck, Annahmen, Übergabe.

**Ohne Skriptausführung** (Assistent ohne Code): Spec, Legende (von Hand nach der Spec) und
Schemablatt ausgeben; die Lehrkraft erzeugt lokal mit `edu-technologieschema` (Aufruf wie oben)
und prüft die Vorschau. Kein SVG von Hand schreiben.

## Ausgabe
- `schema/46_<kurztitel>.yaml` – Spec (hier ändern)
- `abbildungen/46_<kurztitel>.drawio.svg` – **bearbeitbar** (app.diagrams.net, draw.io Desktop,
  draw.io-Erweiterung in VS Code; Datei öffnen bzw. hineinziehen): jedes Bauteil eine Form mit
  Andockpunkten an den Ankern (`unten`, `an1` …), Kennzeichen/Betriebsmittel/Aufgabe als Formdaten
  (*Bearbeiten → Daten bearbeiten*), Beschriftungen als Text zum Bauteil gruppiert (Doppelklick in die
  Gruppe), Linien und Rohre als Verbinder, die beim Verschieben angeschlossen bleiben
- `abbildungen/46_<kurztitel>.svg` (Bild, eine Gruppe `<g id="eN">` je Element, auch für Inkscape),
  `.png` (Word) – erzeugt
- `46_schema_<kurztitel>.md` – Schemablatt (Artefakt nach Skill-Vertrag) mit Legende
- Planungsakte: Artefakt 46 eintragen.

## Qualitätscheck
- [ ] `technologieschema pruefen` ohne ❌, Warnungen angesehen?
- [ ] PNG-Vorschau angesehen, nichts überlagert, Pfeile und Lage stimmen?
- [ ] Jedes Betriebsmittel der Aufgabe im Bild und in der Legende, nichts zusätzlich?
- [ ] Kennzeichen in Bild, Legende, Text und Zuordnungsliste gleich, eine Notation?
- [ ] Grundstellung in Bild und Fußzeile gleich; Bild verrät die Lösung nicht?
- [ ] Alternativtext, Bildunterschrift, Graustufen; keine Normzeichnung vorgetäuscht?
- [ ] Vorlage eines Dritten nur mit geklärten Rechten und Quelle?
- [ ] GRAFCET als `typ: grafcet`: speichernde Aktionen mit `:=` und Pfeil oder Fähnchen, Negation als Überstrich,
      Rücksprung mit Pfeil, `zuordnung` angegeben, Text-Tabelle aus `textform`?
- [ ] Bearbeitbare `.drawio.svg` mitgeliefert und in der Übergabe erklärt?
- [ ] Schemablatt für Lernende ohne Lösung und ohne Erklärtext, den das Bild schon zeigt
      (`references/schuelermaterial.md` Abschn. 2); keine Zeichnung aus Zeichen
      (`python3 scripts/zeichnungen_pruefen.py 46_*.md` ohne ❌)?

## Beispielaufrufe
> „Zeichne das Technologieschema zur Aufgabe: Ein Förderband bringt Werkstücke zu einer
> Lichtschranke, ein Zylinder schiebt sie in einen Behälter. Notation nach 81346.“

> „Die Biegestation in der Klausur braucht ein Bild: drei Zylinder mit je zwei Endlagensensoren,
> Start- und Stopptaster, Meldeleuchte. Dazu die Legende für das Schülermaterial.“

> „Ich habe eine Skizze der Tankanlage mit drei Füllstandsschaltern – mach daraus ein sauberes
> Schema und eine Lösungsfassung mit eingezeichnetem Füllstand.“

> „Im Erwartungshorizont stehen GRAFCET und FUP als ASCII-Skizze – zeichne beide als Lösungsbild.“

> „GRAFCET zur Funktionsbeschreibung: Die Warnleuchte wird im Schritt 4 gesetzt und im Schritt 1 wieder
> zurückgesetzt, dazu die Tabelle für die Zweitkorrektur.“

## Referenzen – wann lesen
- `references/technologieschema-specs.md` – **immer** (Spec-Aufbau, Bauteile, Anker, Maße, Fehler).
- `assets/spec-biegestation.yaml`, `assets/spec-tankanlage.yaml`, `assets/spec-foerderstation.yaml`,
  `assets/spec-steuerstromkreis.yaml`, `assets/spec-naeherungsschalter.yaml`, `assets/spec-grafcet.yaml`,
  `assets/spec-grafcet-verzweigung.yaml`, `assets/spec-grafcet-teil.yaml`, `assets/spec-fup.yaml` – Muster; das
  passende als Ausgangspunkt nehmen. `assets/spec-grafcet-symbole.yaml` – alle GRAFCET-Symbole auf einer Tafel.
- `references/schaltzeichen.md` – alle Schaltzeichen mit Klassen, Anschlüssen und Herkunft (bei `typ: symbol`).
- `assets/vorlage-schemablatt.md` – **immer** (Ausgabeformat).
- `references/notation-steuerungstechnik.md` – Kennzeichen und Schreibweise (Anlage zum Material).
- `references/normen-technik.md` – Hintergrund zu Kennzeichen und Normen (Abschn. 2 und 5), bei Fragen zur Notation.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/edu.py` – startet `edu-technologieschema` aus der mitgelieferten Kopie
  (`scripts/eduwerkzeuge/`); `scripts/vorschau_png.py` – PNG-Vorschau für Sichtprüfung und Word.
