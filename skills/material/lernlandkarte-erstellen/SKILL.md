---
name: lernlandkarte-erstellen
description: Erstellt digitale Lernlandkarten für edumaps (nds.edumaps.de) aus Lernsituation, Unterrichtsentwurf oder Material – Lernlandkarte mit Selbstdiagnose und Lernposten, Stundenablauf als Zeitstrahl, Klausurvorbereitung, Lernfeldübersicht oder Workshop. Schreibt eine bearbeitbare Markdown-Quelle mit Pfaden und Karten (Auftrag, Material, gestufte Hilfen, Quiz, Abstimmung, Checklisten, Lösung zum Aufdecken), prüft sie mit edumap_pruefen.py und übersetzt sie mit dem mitgelieferten Werkzeug edu-edumap deterministisch in die Import-Datei (JSON); dazu ein Begleitblatt mit Aufbau, Uploads und Einrichtung. Farbgebung wahlweise Standard oder passend zum Ausgangsmaterial (Präsentation, Arbeitsblatt, Webseite). Verwenden bei „Edumap erstellen", „Lernlandkarte", „Lernpfad", „Stationenlernen digital", „Stundenablauf als Zeitstrahl", „Selbstdiagnose zur Klausurvorbereitung" oder wenn vorhandenes Material in edumaps ausgespielt werden soll.
metadata:
  version: "1.6"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  eduwerkzeuge: "edumap"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Lernlandkarte erstellen (edumaps)

## Zweck
Eine Lernsituation, eine Stunde oder eine Klausurvorbereitung als **Lernlandkarte** in
edumaps ausspielen: Lernende sehen Ziel, Weg, Stationen und Hilfen auf einen Blick und
arbeiten selbstgesteuert. Claude schreibt nur die **Quelle** (Inhalt und Struktur); die
Import-Datei erzeugt das getestete Werkzeug `edu-edumap` – nie von Hand.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Begleitblatt). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Muster

| Muster | wann | Format |
|---|---|---|
| **A Lernlandkarte zur LS** (Standard) | Stationen/Lernposten zu einer Lernsituation | `karte` |
| **B Stundenablauf** | Doppelstunde oder Projekttag als Zeitleiste | `zeitstrahl` |
| **C Klausurvorbereitung** | Selbstdiagnose, Übungsstationen, Lernplan | `karte` |
| **D Lernfeldübersicht** | Orientierung über alle Lernsituationen | `pinnwand` |
| **E Workshop** | SOL-Fortbildung mit Logbuch und Marktplatz | `karte` |

Aufbau, Beispiele und Gestaltungsregeln: `references/kartenmuster.md`.

## Eingaben
- **Pflicht (sonst Rückfrage):** Inhalt – Lernsituation, Entwurf, Material oder Themenliste.
- **Wichtig, sonst Annahme:** Muster, Lerngruppe (zusammenfassend), Zeitrahmen, Ansprache
  (du/Sie nach Schulregel), Präsenz oder Distanz, vorhandene Dateien zum Verlinken.
- **Optional:** Planungsakte, Termine (für Zeitstrahl/Kalender), Edumap-Adressen bereits
  hochgeladener Dateien, Farbwünsche oder ein **Ausgangsmaterial für die Farbgebung**
  (Präsentation, Arbeitsblatt, Webseite, Logo) – ohne Angabe Standardfarben.

## Leitlinien (verbindlich)
1. **Inhalt aus der Planung übernehmen, nicht neu erfinden:** Handlungssituation,
   Handlungsergebnis, Kompetenzen, Aufträge und Zeiten wie in Lernsituation, Entwurf und
   Material. Fehlt etwas, als `⚠️ Annahme:` im Begleitblatt.
2. **Jeder Lernposten ist vollständig:** Auftrag (Operator, Ergebnisform, Sozialform, Zeit,
   Erfolgskriterien) · Material · gestufte Hilfen · Selbstcheck.
3. **Selbstdiagnose hat Folgen:** Ich-kann-Sätze aus den Kompetenzen und eine
   Empfehlungskarte, welcher Lernposten bei welcher Lücke passt.
4. **Lösungen nur zur Selbstkontrolle** von Übungen und nur zum Aufdecken
   (`flags=262148`); nie Lösungen zu Leistungsüberprüfungen, keine Lehrkraft-Hinweise in der
   Map (die gehören ins Begleitblatt).
5. **edumaps-Syntax, nicht Markdown** in Karten: `--` nummeriert, `|||`/`||` Tabellen (Zellen mit einfachem `|` trennen),
   `{Text}{URL}` Links, keine Überschriften (`references/edumap-syntax.md`).
6. **Eine Karte, ein Gedanke;** 3–6 Karten je Pfad; nur Orientierung und Aufträge
   ausgeklappt; eine Leitkarte angepinnt.
7. **Farbe trägt Bedeutung:** je Pfad eine Farbe, Karten in Pfadfarbe; helles Theme
   (`tageslicht`, `morgen`, `kreide`) für Beamer und Druck. Die Quelle schreibt immer die
   **Standardfarben**; eine Farbgebung passend zum Material kommt als eigenes Theme dazu
   (Theme-Datei `92_lernlandkarte_<kurztitel>_farben.yaml`, `edu-edumap --farben-aus`) – so
   bleibt die Standardfassung mit einer Zeile umschaltbar. Pfadfarben mit mindestens 3:1
   Kontrast zu weißer Schrift (`references/edumap-syntax.md`, Abschnitt 5).
8. **Datenschutz:** keine Namen, Fotos oder Kontaktdaten von Lernenden; Logbücher nur mit
   Gruppenkürzeln; kein `password:` in der Quelle.
9. **Material verlinken, nicht abschreiben:** lange Texte als Datei hochladen; externe Links
   nur aus gelieferten Unterlagen oder geprüft – keine erfundenen Adressen.
10. **Sprachsensibel:** Operator vorn, kurze Sätze, Fachbegriffe per Tooltip
    `[Begriff]{Erklärung}` erklären.
11. **Kurz, offen, anschaulich, ohne Dekoration** (`references/schuelermaterial.md`): Karten
    mit wenigen Sätzen; Aufträge nennen Ziel und Ergebnis, Schritte stehen in den Hilfen;
    Abbildungen (Anlagenbild, Diagramm, Skizze) als Datei an der Karte statt Erklärtext; keine
    Emojis außer den KI-Zeichen, keine Floskeln, keine Karten ohne Funktion.

## Vorgehen
1. **Grundlage sichten,** Muster wählen; mit Planungsakte Situation, Namen und Zahlen übernehmen.
2. **Bauplan** (intern): Pfad · Zweck · Karten · Farbe · Flags/Zeit. Umfang an der
   Lernzeit ausrichten.
3. **Quelle schreiben** nach `assets/vorlage-lernlandkarte.md` (Muster A) bzw. den Beispielen
   in `references/kartenmuster.md`; Syntax: `references/edumap-syntax.md`. Alle Platzhalter
   `[…]` ersetzen; Datei-Adressen, die es noch nicht gibt, als Upload im Begleitblatt führen.
4. **Prüfen:** `python3 scripts/edumap_pruefen.py 92_lernlandkarte_<kurztitel>.md` – alle ❌
   beheben, ⚠ beheben oder im Begleitblatt begründen. Das Skript prüft auch die Leitlinien
   2 und 6 (vollständige Lernposten, höchstens sechs Karten je Pfad – gestufte Hilfen als
   mehrere `??`-Spoiler in **einer** Karte).
5. **Farbgebung (optional):** Liegt ein Ausgangsmaterial vor, Theme-Datei erzeugen –
   `edu-edumap --farben-aus folien.pptx -o 92_lernlandkarte_<kurztitel>_farben.yaml`
   (auch `.docx`, `.odp`, PDF, Bild oder Adresse einer Webseite) – und im Frontmatter
   `theme: 92_lernlandkarte_<kurztitel>_farben.yaml` setzen; zurück zum Standard mit
   `theme: tageslicht`. Vorschlag mit der Lehrkraft abstimmen (Farben im Begleitblatt).
6. **Import-Datei erzeugen:**
   `edu-edumap 92_lernlandkarte_<kurztitel>.md -o 92_lernlandkarte_<kurztitel>.json`
   (installierte eduwerkzeuge) oder mit der mitgelieferten Kopie
   `python3 scripts/edu.py edumap 92_lernlandkarte_<kurztitel>.md -o 92_lernlandkarte_<kurztitel>.json`.
7. **Gegenprüfen:** `python3 scripts/edumap_pruefen.py QUELLE --json IMPORT.json` (gleiche
   Zahl an Pfaden und Karten, alle Farben aufgelöst).
8. **Begleitblatt** nach `assets/vorlage-begleitblatt.md`: Aufbau, hochzuladende Dateien,
   Einrichtung in edumaps, Qualitätscheck, Annahmen, Übergabe.

**Ohne Skriptausführung** (Assistent ohne Code): Quelle und Begleitblatt ausgeben; die
Lehrkraft erzeugt die Import-Datei lokal mit `edu-edumap`. Prüfpunkte aus Schritt 4 von
Hand durchgehen. Kein JSON von Hand schreiben.

## Ausgabe
- `92_lernlandkarte_<kurztitel>.md` – Quelle (bearbeitbar, hier ändern)
- `92_lernlandkarte_<kurztitel>.json` – Import-Datei für edumaps (erzeugt)
- `92_lernlandkarte_<kurztitel>_farben.yaml` – nur bei eigener Farbgebung (Theme-Datei)
- `92_lernlandkarte_<kurztitel>_begleitblatt.md` – Artefakt nach Skill-Vertrag mit Kopf und
  Pflichtabschnitten
- Planungsakte: Artefakt 92 eintragen; Uploads als offene Punkte.

## Qualitätscheck
- [ ] `edumap_pruefen.py` ohne ❌; keine Platzhalter mehr?
- [ ] Import-Datei erzeugt und mit `--json` gegengeprüft?
- [ ] Situation, Ergebnis, Kompetenzen und Zeiten wie in der Planung?
- [ ] Jeder Lernposten mit Auftrag, Material, gestuften Hilfen, Selbstcheck?
- [ ] Selbstdiagnose mit Empfehlung?
- [ ] Lösungen nur zum Aufdecken, keine zu Leistungsüberprüfungen?
- [ ] Keine Personendaten, kein Kennwort, keine erfundenen Links?
- [ ] Ansprache einheitlich, Sprache sprachsensibel?
- [ ] Karten kurz, Aufträge offen, Abbildungen statt Erklärtext, keine Dekoration –
      `python3 scripts/schuelermaterial_pruefen.py 92_lernlandkarte_<kurztitel>.md` ohne ❌?
- [ ] Eigene Farbgebung: Quelle mit Standardfarben, Theme-Datei daneben, kein Kontrast-⚠?

## Beispielaufrufe
> „Mach aus `20_lernsituation_gurtfoerderer.md` und den Arbeitsblättern eine Edumap mit
> Selbstdiagnose und drei Lernposten, Sie-Form."

> „Stundenablauf der Doppelstunde aus `30_unterrichtsentwurf_…md` als Zeitstrahl für den
> 3. November, Phasen erst zur Startzeit freischalten."

> „Generalprobe für die Klassenarbeit LF 2: Selbstdiagnose nach Kompetenzen, Stationen,
> Übungsklausur mit Lösung zum Aufdecken."

> „Die Workshop-Map bitte in den Farben unserer Präsentation `input.pptx`."

## Referenzen – wann lesen
- `assets/vorlage-lernlandkarte.md`, `assets/vorlage-begleitblatt.md` – **immer** (Ausgabeformat).
- `references/edumap-syntax.md` – **immer** beim Schreiben der Quelle.
- `references/kartenmuster.md` – Wahl und Aufbau des Musters.
- `references/schuelermaterial.md` – Material für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/edumap_pruefen.py` – Prüfung vor und nach dem Erzeugen.
- `scripts/edu.py` – startet `edu-edumap` aus der mitgelieferten Kopie (`scripts/eduwerkzeuge/`).
