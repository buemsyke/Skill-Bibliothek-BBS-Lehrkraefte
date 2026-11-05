<!-- Assistenten-Fassung des Skills 'lernlandkarte-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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

# ANHÄNGE

## Anhang: assets/vorlage-begleitblatt.md

---
artefakt: Lernlandkarte (edumaps) – Begleitblatt
titel: "[Titel der Karte]"
skill: lernlandkarte-erstellen
skill_version: "1.6"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
muster: "[A Lernlandkarte zur LS | B Stundenablauf | C Klausurvorbereitung | D Lernfeldübersicht | E Workshop]"
status: "KI-Entwurf – fachlich zu prüfen"
---

# Lernlandkarte: [Titel]

**Dateien:** `92_lernlandkarte_[kurztitel].md` (Quelle, hier ändern) ·
`92_lernlandkarte_[kurztitel].json` (Import-Datei, erzeugt mit edu-edumap – nicht von Hand ändern)
**Bezug:** [Lernsituation / Entwurf / Material, Dateinamen]
**Einsatz:** [Lerngruppe zusammenfassend, Zeitraum, Präsenz/Distanz, Endgerät]
**Farbgebung:** [Standard (`theme: tageslicht`) / aus Material: Datei → `92_lernlandkarte_[kurztitel]_farben.yaml`]

## Aufbau

| Pfad | Zweck | Karten | Farbe | Hinweis |
|---|---|---|---|---|
| Start | Handlungssituation, Ablauf, Arbeitsweise | 3 | ozeanblau | Auftrag angepinnt |
| ① Selbstdiagnose | Ich-kann-Sätze, Abstimmung, Empfehlung | 3 | tuerkis | |
| [Lernposten A] | [ … ] | [ ] | [ ] | [Hilfen gestuft, Lösung zum Aufdecken] |

Gesamt: [n] Pfade, [m] Karten, davon [k] ausgeklappt.

## Hochzuladende Dateien

Dateien in edumaps über die Büroklammer hochladen und die erzeugte Adresse in der Quelle
eintragen (`https://nds.edumaps.de/file/…`), dann die Import-Datei neu erzeugen.

| Karte | Datei | Quelle im Projekt |
|---|---|---|
| Material A | Arbeitsblatt A (PDF) | `40_material_[ … ].md` → PDF |

## In edumaps einrichten

1. In [nds.edumaps.de](https://nds.edumaps.de) anmelden.
2. Neue Map über den JSON-Import anlegen und `92_lernlandkarte_[kurztitel].json` hochladen.
   🔎 Prüfen: Bezeichnung der Import-Funktion in der aktuellen Oberfläche.
3. Hochzuladende Dateien ergänzen (Tabelle oben), Adressen in die Quelle übernehmen,
   Import-Datei neu erzeugen – oder die Adressen direkt in edumaps eintragen und die Quelle
   nachziehen.
4. Rechte setzen: [Lernende dürfen Karten im Pfad „Ergebnis sichern" anlegen, nicht löschen].
5. Als Lernende bzw. Lernender testen: Karten aufklappen, Quiz, Abstimmung, Lösungskarten.
6. Link oder QR-Code an die Lerngruppe geben.

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| `edumap_pruefen.py` ohne ❌, Platzhalter ersetzt | | |
| Import-Datei gegengeprüft (`--json`: Pfade/Karten gleich, Farben aufgelöst) | | |
| Handlungssituation und Handlungsergebnis wie in der Lernsituation | | |
| Jeder Lernposten: Auftrag mit Operator, Ergebnisform, Sozialform, Zeit, Erfolgskriterien | | |
| Selbstdiagnose führt zu einer Empfehlung | | |
| Hilfen gestuft, verraten die Lösung nicht | | |
| Lösungen nur zur Selbstkontrolle und nur zum Aufdecken; keine Lösungen zu Leistungsüberprüfungen | | |
| Keine Personendaten, kein Kennwort in der Quelle | | |
| Links und Dateien erreichbar (Linkcheck) | | |
| Ansprache einheitlich (du/Sie), Sprache sprachsensibel | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: Verhalten der Karten-Flags (eingeklappt, Aufdecken, Buchung) nach dem Import testen.

## Übergabe

- Quelle und Import-Datei: …
- Offene Uploads: …
- Empfohlene nächste Skills: `material-pruefen` (Links, Fakten in den Karten),
  `quizfragen-erstellen` (H5P-Übungen für die Lernposten), `fachdiagramm-erstellen`
  (Abbildungen), `differenzierung-erstellen` (weitere Hilfekarten)

> KI-gestützt erstellt (Skill lernlandkarte-erstellen v1.6). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: assets/vorlage-lernlandkarte.md

---
# Quelle für edu-edumap – Skill lernlandkarte-erstellen v1.6
# Begleitblatt: 92_lernlandkarte_[kurztitel]_begleitblatt.md
# Muster A (Lernlandkarte zur Lernsituation). Andere Muster: references/kartenmuster.md
title: "[LS-Nr.] – [Titel der Lernsituation als Handlung]"
language: de
theme: tageslicht
format: karte
---

## Start – worum geht es? [color=ozeanblau] [box_color=ozeanblau]

### Der Auftrag [flags=16420]
**[Fiktiver Betrieb]** braucht bis **[Termin]** [Handlungsergebnis in einem Satz].

[Handlungssituation in höchstens drei Sätzen aus der Lernsituation gekürzt – Inhalt unverändert, besser mit Situationsmaterial (Störmeldung, Foto).]

**Euer Ergebnis:** [Handlungsergebnis, z. B. Wartungsplan mit Prüfprotokoll]

### Ablauf [flags=0]
-- Selbstdiagnose (10 min)
-- Lernposten bearbeiten ([2] × [30] min)
-- Ergebnis sichern und vorstellen ([20] min)
-- Rückblick (10 min)

### So arbeitest du
- Du startest mit der Selbstdiagnose und wählst danach deine Lernposten.
- Jeder Lernposten hat einen Auftrag, Material, Hilfen und einen Selbstcheck.
- Hilfen zuerst selbst versuchen, dann die nächste Hilfe öffnen.
- Dein Ergebnis sicherst du im Logbuch deiner Gruppe.

## ① Selbstdiagnose [color=tuerkis] [box_color=tuerkis]

### Was kann ich schon? [flags=0]
Kreuze an, was du schon sicher kannst:

[ ] Ich kann [Teilkompetenz 1 als Ich-kann-Satz mit Operator].
[ ] Ich kann [Teilkompetenz 2].
[ ] Ich kann [Teilkompetenz 3].

### Wie sicher fühlst du dich? [flags=0]
<poll>
Sicher – ich lege gleich los
Teilweise – ich brauche Hilfen
Unsicher – ich starte mit den Grundlagen
</poll>

### Deine Empfehlung
- Teilkompetenz 1 noch unsicher → **Lernposten A**
- Teilkompetenz 2 und 3 unsicher → **Lernposten B**
- Alles sicher → **Lernposten B** und danach die Vertiefung

## Lernposten A – [Thema A] [color=mintgruen] [box_color=mintgruen]

### Auftrag A [flags=0]
**[Operator]** Sie/du [Auftrag mit Bezug zur Handlungssituation].

- **Ergebnis:** [Ergebnisform, z. B. ausgefüllte Checkliste]
- **Sozialform und Zeit:** [Partnerarbeit], [30] min
- **Erfolgskriterien:** [beobachtbares Kriterium 1], [Kriterium 2]

### Material A
https://nds.edumaps.de/file/[ID].pdf/[kuerzel]
Arbeitsblatt A (PDF)

{[Linktext]}{https://www.example.org/[seite]}

### Hilfe A1 – Impuls
?? [Denkanstoß, der auf den nächsten Schritt lenkt]

### Hilfe A2 – Strategie
?? [Vorgehen in Schritten, ohne die Lösung zu verraten]

### Selbstcheck A
[Frage zum Kern des Lernpostens]

<quiz>
[plausible falsche Antwort]
# [richtige Antwort]
[plausible falsche Antwort]
</quiz>

### Lösung A – erst nach der Bearbeitung öffnen [flags=262148]
[Kurzfassung des Erwartungshorizonts für die Selbstkontrolle]

## Lernposten B – [Thema B] [color=bernstein] [box_color=bernstein]

### Auftrag B [flags=0]
**[Operator]** [Auftrag].

- **Ergebnis:** [Ergebnisform]
- **Sozialform und Zeit:** [Einzelarbeit], [30] min
- **Erfolgskriterien:** [Kriterium]

### Material B
[Tabelle, Code oder Link – Syntax siehe references/edumap-syntax.md]

||| Größe | Wert | Einheit
|| [Größe 1] | [Wert] | [Einheit]
|| [Größe 2] | [Wert] | [Einheit]

### Hilfe B1 – Impuls
?? [Denkanstoß]

### Selbstcheck B
[ ] [Erfolgskriterium als Ich-kann-Satz]
[ ] [Erfolgskriterium]

## Ergebnis sichern [color=indigo] [box_color=indigo]

### So sichert ihr euer Ergebnis [flags=0]
-- Legt im Logbuch eine eigene Karte an (＋), Titel: **Gruppe und Lernposten**, z. B. „G1 · A".
-- Haltet fest: Ergebnis, offene Fragen, nächster Schritt.
-- Keine Namen, nur das Gruppenkürzel.

### Logbuch – Beispielkarte
**G0 · A** (Muster)
- Ergebnis: [ … ]
- Offene Frage: [ … ]
- Nächster Schritt: [ … ]

## Rückblick [color=lila] [box_color=lila]

### Was nimmst du mit? [flags=0]
<poll>
Ich habe das Ergebnis erreicht
Ich habe es teilweise erreicht
Ich brauche noch Unterstützung
</poll>

### Wie geht es weiter?
[Ausblick auf die nächste Lernsituation oder Übungsangebot, z. B. H5P-Quiz]

## Anhang: references/edumap-syntax.md

# Edumap-Quelle – Syntax für edu-edumap

Die Quelle ist Markdown mit YAML-Frontmatter (oder reines YAML). `edu-edumap` übersetzt sie
deterministisch in die Import-Datei (JSON) für edumaps (in Niedersachsen: nds.edumaps.de).
**Karteninhalte folgen der edumaps-Syntax, nicht Markdown** – Tabellen, Links, Listen und
Bilder werden anders geschrieben (Abschnitt 4).

## 1. Gerüst

```markdown
---
title: "LS 4 – Gurtförderer nach Störung wieder in Betrieb nehmen"
language: de
theme: tageslicht            # Farbthema (Abschnitt 5)
format: karte                # karte | pinnwand | zeitstrahl | kalender
---

## Pfad-Titel [color=tuerkis] [box_color=tuerkis]

### Karten-Titel [flags=0]
Inhalt der Karte …

### Nächste Karte
…
```

| Ebene | Schreibweise | wird in edumaps |
|---|---|---|
| Karte (Map) | Frontmatter `title:` oder Zeile `# Titel` | Titel der Map |
| Pfad | `## Titel [attribut=wert] …` | Spalte bzw. Abschnitt |
| Karte | `### Titel [attribut=wert] …` | Box im Pfad |
| Inhalt | alle Zeilen bis zur nächsten `##`/`###` | Boxinhalt |

**Achtung:** Text zwischen `##` und dem ersten `###` eines Pfads übernimmt edu-edumap nicht.
Zeilen, die mit `## ` oder `### ` beginnen, starten immer einen neuen Pfad bzw. eine neue
Karte – in Karten deshalb keine Markdown-Überschriften, sondern **fett**.

## 2. Frontmatter

| Schlüssel | Werte | Hinweis |
|---|---|---|
| `title` | Text | Pflicht (oder `# Titel`) |
| `language` | `de`, `en`, … | Standard `de` |
| `theme` | Name, Theme-Datei (`.yaml`) oder Mapping – Abschnitt 5 | setzt Hintergrund und Pfadfarben |
| `format` | `karte` (0), `pinnwand` (1), `zeitstrahl` (2), `kalender` (3) | Zeitstrahl/Kalender ordnen nach `showdate` |
| `mapbg` | Farbname oder `#rrggbb` | überschreibt das Theme |
| `extras` | `nmc` | Kurs-Modus (strukturierte Navigation) |
| `password` | Text | **nicht verwenden** – stünde im Klartext in Quelle und JSON; nach dem Import in edumaps setzen |

Weitere Schlüssel (z. B. YAML-Kommentare mit Skill und Begleitblatt) ignoriert edu-edumap.
Ohne PyYAML ignoriert edu-edumap das ganze Frontmatter – `edumap_pruefen.py` meldet das.

## 3. Attribute

**Pfad (`##`):** `color`, `box_color` (Farbe aller Karten im Pfad), `color_inherit=true`
(Karten erben die Pfadfarbe), `flags`, `showdate`, `annotation`, `extras`.

**Karte (`###`):** `color`, `flags`, `showdate`, `book`, `booktime`, `booklimit`, `subject`,
`extras`, `file_url`, `file_label`.

| Flags | Karte | Hinweis |
|---|---|---|
| (keins) = `4` | eingeklappt, nur Titel sichtbar | Standard |
| `0` | ausgeklappt | Orientierung, Aufträge |
| `16420` | hervorgehoben/angepinnt | eine Leitkarte je Map (empfohlen mit `color=ozeanblau`) |
| `262148` | eingeklappt, Inhalt erst nach Aufdecken | Lösung zur Selbstkontrolle 🔎 nach Import testen |
| `1048576` | Navigationskarte ohne Titel (`### -`) | z. B. `-- {Karte A}{!#b12345}` |
| `131072` / `524288` | Buchung offen / zeitgesteuert | wird über `book=` automatisch gesetzt |

| Flags | Pfad |
|---|---|
| `0` | normal |
| `640` | gesperrt bis `showdate` (Zeitstrahl, Kalender) – ohne `showdate` öffnet er sich nie |

**Zeitangaben:** `showdate=2026-11-03 08:00:00` (auch `2026-11-03`).
**Buchung:** `[book=open] [booklimit=6]` oder `[book=timed] [booktime=2026-11-03 07:30:00] [booklimit=6]`.
**Datei an der Karte:** `[file_url=https://nds.edumaps.de/file/…] [file_label=Arbeitsblatt A]`.

## 4. Inhaltssyntax (in Karten)

| Zweck | edumaps-Schreibweise | nicht so (Markdown) |
|---|---|---|
| fett / kursiv | `**fett**`, `*kursiv*` | |
| nummerierte Liste | `-- Schritt` (zwei Striche) | `1. Schritt` |
| Aufzählung | `- Punkt` | |
| Trennlinie | `---` | |
| Tabelle | `\|\|\| Kopf A \| Kopf B` und `\|\| Zelle \| Zelle` (Zellen trennt ein einzelner Strich) | `\| a \| b \|` mit `\|---\|` |
| Link | `{Linktext}{https://…}` | `[Linktext](https://…)` |
| interner Link | `{Text}{!#path-123}` (Pfad), `{Text}{!#b123}` (Karte) | |
| Datei/Bild mit Vorschau | Adresse allein in einer Zeile, Beschriftung in der Zeile darunter | `![Bild](…)` |
| Code | `` `Code` `` – mehrzeilig: Backtick am Anfang der ersten und am Ende der letzten Zeile; im Code keine Backticks | |
| Formel | `\( U = R \cdot I \)`, Block `$$ … $$` | |
| Spoiler/Hilfe | `?? Text` (eingeklappt bis Klick) | |
| Checkbox | `[ ] offen`, `[x] erledigt` | |
| Countdown | `&&count: 600&&` (Sekunden), `&&msg:popup&&` | |
| QR-Code | `{qrcode:https://…}` | |
| Tooltip | `[Begriff]{Erklärung}` | |
| Vorlesen | `<audio-de>Text</audio>` | |
| Anker / Tag | `!#anker-name`, `#tag-name` | |

**Quiz** (eine richtige Antwort mit `#` markieren):

```
<quiz>
Die Gurtgeschwindigkeit steigt
# Der Gurt läuft seitlich ab
Der Motor wird lauter
</quiz>
```

**Abstimmung:**

```
<poll>
Sicher
Teilweise
Unsicher
</poll>
```

**Quiz- und Kurs-Modus** ab einer Stelle: `~|quizstart|~`, `~|coursestart|~`.

Tabellen brauchen eine **Leerzeile davor** – steht Text direkt darüber, zeigt edumaps die
Tabelle als Fließtext. edu-edumap ergänzt die Leerzeile; `edumap_pruefen.py` weist darauf hin
(wichtig, wenn Karten von Hand in edumaps bearbeitet werden).

Seit der Umstellung des Anbieters (Oktober 2026) trennt ein **einzelner Strich** die
Zellen: `||| Kopf 1 | Kopf 2 | Kopf 3`, darunter `|| Zelle | Zelle | Zelle`. Das Zeichen `|` darf
deshalb nicht im Zelltext stehen. Leere Zellen bleiben leer (`|| 1 |  |  `). Die alte Schreibweise
mit `||` als Trenner (`|||Kopf||Kopf`) erkennt edu-edumap an der Kopfzeile und wandelt sie beim
Erzeugen um; `edumap_pruefen.py` meldet sie als Warnung. Datenzeilen mit weniger Zellen füllt
edu-edumap auf (sonst fehlte in edumaps die letzte Spalte); mehr Zellen als der Kopf meldet
`edumap_pruefen.py`. Bereits importierte Karten mit alten Tabellen in edumaps neu importieren
oder die Tabelle dort in der neuen Schreibweise überschreiben.

## 5. Farben und Themes

**Themes** (`theme:`) – hell, für Unterricht und Beamer empfohlen: `tageslicht` (hellgrau,
Pfade blau), `morgen` (eisblau, türkis), `kreide` (creme, bernstein), `standard` (hellblau,
blau). Dunkel: `nacht`, `schiefer`, `anthrazit`, `wald`, `warm`, `abend`.

**Pfad- und Kartenfarben:** `blau`, `ozeanblau`, `tuerkis`, `mintgruen`, `gruen`, `waldgruen`,
`bernstein`, `orange`, `rot`, `koralle`, `lila`, `violett`, `indigo`, `pink`, `grau`, `silber`
– oder `#rrggbb`.

**Hintergründe** (`mapbg:`): hell `hellblau`, `eisblau`, `mintweiss`, `hellgrau`, `creme`,
`lavendel`, `pastellblau`, `pastellgruen`, `pastellrose`; dunkel `anthrazit`, `schiefergrau`,
`nachtblau`, `dunkelgrau`, `warmgrau`, `olivgrau`, `mitternacht`, `stahlblau`.

Unbekannte Farbnamen übernimmt edu-edumap ungeprüft – edumaps zeigt dann keine Farbe.
`edumap_pruefen.py` meldet sie.

### Eigene Farbgebung (passend zum Ausgangsmaterial)

Statt eines Theme-Namens nimmt `theme:` ein **Mapping** oder eine **Theme-Datei**:

```yaml
theme: 92_lernlandkarte_gurtfoerderer_farben.yaml   # Datei neben der Quelle
# oder direkt im Frontmatter:
theme:
  basis: tageslicht          # optional: eingebautes Theme als Grundlage
  hintergrund: "#eef3f8"     # Name oder #rrggbb
  pfade: [farbe1, farbe2, farbe3]
  karten: pfad               # optional: Karten ohne eigene Farbe in Pfadfarbe
  farben:                    # eigene Farbnamen – auch in [color=…] nutzbar
    farbe1: "#1f4e79"
    farbe2: "#c55a11"
    farbe3: "#548235"
```

**Farbtausch:** `pfade` ersetzt die Standardfarben der Quelle der Reihe nach – die erste
Standardfarbe (Palette-Name oder Pfad ohne `color`) wird `farbe1`, die zweite `farbe2` …
Gleiche Farben bleiben gleich (Pfad und Karten in Pfadfarbe, die Leitkarte in der Farbe des
Start-Pfads), verschiedene bleiben verschieden. `#rrggbb` und eigene Namen bleiben, wie sie
sind. Gibt es mehr Standardfarben als `pfade`, wiederholen sich die Farben (ℹ im Prüfskript).
Die Quelle bleibt also in Standardfarben; umgeschaltet wird nur die Zeile `theme:`.

**Farben aus dem Material** liest edu-edumap selbst und schreibt einen Theme-Vorschlag:

```bash
edu-edumap --farben-aus input.pptx -o 92_lernlandkarte_gurtfoerderer_farben.yaml
edu-edumap --farben-aus https://www.schule.example/     # Webseite, Ausgabe im Terminal
edu-edumap quelle.md --farben-aus arbeitsblatt.pdf -o quelle.json   # direkt anwenden
edu-edumap quelle.md --theme kreide -o quelle.json      # einmalig anderes Theme
```

| Material | gelesen werden |
|---|---|
| `.pptx`, `.docx`, `.xlsx` (+ Vorlagen) | Design-Farben (Akzente) und tatsächlich verwendete Farben |
| `.odp`, `.odt`, `.ods` | verwendete Farben (Schrift, Füllung, Linien) |
| `.html`, `.css`, `.svg`, Adresse | CSS-Farben, verlinkte Stylesheets, Markenvariablen (`--primary` …), `theme-color` |
| `.png`, `.jpg`, `.pdf` | Flächenfarben der Seiten (braucht Pillow; PDF zusätzlich `pdftoppm`) |

Der Vorschlag nimmt bunte Farben nach Häufigkeit, lässt Weiß, Grau und blasse Flächen
weg, **dunkelt zu helle Farben ab**, bis weiße Titelschrift mindestens 3:1 Kontrast hat
(Kommentar „abgedunkelt von …“), und wählt einen hellen Hintergrund. Hat das Material zu
wenige Farben, ergänzt er hellere und dunklere Töne. Den Vorschlag mit der Lehrkraft
abstimmen; Farben in der Datei frei änderbar. `edumap_pruefen.py` prüft Theme-Datei und
Kontrast (⚠ unter 3:1).

Hinweis: Farben einer Schule oder eines Trägers sind Gestaltung, kein Logo – Logos und
Wortmarken nicht in die Map übernehmen, ohne dass die Nutzung geklärt ist.

## 6. YAML statt Markdown

Gleiche Struktur als `paths:` → `boxes:`; mehrzeiliger Inhalt mit `content: |`; Dateien als
Liste `files:` (je `url`, `label`) – sie werden vor den Inhalt gesetzt.

```yaml
title: "LS 4 – Gurtförderer"
theme: tageslicht
paths:
  - title: "Lernposten A – Schmierplan"
    color: mintgruen
    box_color: mintgruen
    boxes:
      - title: "Auftrag A"
        flags: "0"
        content: |
          **Erstellen** Sie den Schmierplan …
```

Markdown ist für Lehrkräfte leichter zu lesen und zu ändern; YAML lohnt sich, wenn Karten
per Skript erzeugt werden.

## 7. Erzeugen

```bash
edu-edumap 92_lernlandkarte_gurtfoerderer.md -o 92_lernlandkarte_gurtfoerderer.json   # installiert
python3 scripts/edu.py edumap 92_lernlandkarte_gurtfoerderer.md -o 92_lernlandkarte_gurtfoerderer.json   # mitgeliefert
```

Ohne `-o` heißt die Datei wie ein edumaps-Export: `JJJJ-MM-TT Edumaps - <Titel>.json`.
`--pretty` rückt das JSON lesbar ein; `--theme` und `--farben-aus` siehe Abschnitt 5. Die Import-Datei nie von Hand ändern – immer die Quelle
ändern und neu erzeugen.

## Anhang: references/kartenmuster.md

# Kartenmuster – welche Lernlandkarte für welchen Zweck

Eine Lernlandkarte macht den **Lernweg sichtbar**: Wo stehe ich, was ist das Ziel, welche
Schritte führen dorthin, wo finde ich Hilfe? Sie ersetzt nicht die Lernsituation, sondern
spielt sie für die Lernenden aus. Fünf bewährte Muster:

| Muster | Zweck | Format | Pfade | typische Quelle |
|---|---|---|---|---|
| **A Lernlandkarte zur LS** | selbstorganisiertes Arbeiten an einer Lernsituation (Stationen, Lernposten) | `karte` | Start · Selbstdiagnose · 2–5 Lernposten · Ergebnis sichern · Rückblick | `20_lernsituation`, `40_material`, `60_differenzierung` |
| **B Stundenablauf** | eine Doppelstunde oder ein Projekttag als Zeitleiste | `zeitstrahl` | je Phase der vollständigen Handlung ein Pfad mit `showdate` | `30_unterrichtsentwurf` (Verlaufsplan) |
| **C Klausurvorbereitung** | Generalprobe: Selbstdiagnose nach Kompetenzen, Übungsstationen, Lernplan | `karte` | Übersicht · Selbstdiagnose · Stationen je Kompetenz · Übungsklausur · Lernplan | `70_klausur` (Bauplan, **nicht** die Aufgaben), Lernsituationen |
| **D Lernfeldübersicht** | Orientierung über ein Lernfeld | `pinnwand` | je Lernsituation ein Pfad: Situation, Ergebnis, Zeitraum, Material | Lernfeld-Auszug, Abdeckungsmatrix |
| **E Workshop / Fortbildung** | SOL-Workshop mit Lernposten, Logbuch und Marktplatz | `karte` | Willkommen · Selbstdiagnose · Werkzeugkasten · Lernposten · Marktplatz · Transfer | Fortbildungskonzept |

## Muster A – Lernlandkarte zur Lernsituation

Vorlage: `assets/vorlage-lernlandkarte.md`.

1. **Start** (ozeanblau): Leitkarte „Der Auftrag" angepinnt (`flags=16420`) mit
   Handlungssituation und Handlungsergebnis; Ablauf als `--`-Liste; Arbeitsweise.
2. **Selbstdiagnose** (türkis): Ich-kann-Sätze als Checkboxen (aus den Kompetenzen der LS,
   mit Operator), Abstimmung zur Selbsteinschätzung, **Empfehlungskarte** (welcher Lernposten
   bei welcher Lücke) – sonst bleibt die Diagnose folgenlos.
3. **Lernposten** (je eigene Farbe): Auftrag (Operator, Ergebnisform, Sozialform, Zeit,
   Erfolgskriterien) · Material (Datei-Adresse oder Link) · gestufte Hilfen als Spoiler
   (Impuls → Strategie → Teilschritt) · Selbstcheck (Quiz oder Checkliste; vierte Hilfestufe Kontrolle) · optional Lösung
   zum Aufdecken (`flags=262148`). Pflicht- und Wahlposten unterscheiden (Titel oder Farbe).
4. **Ergebnis sichern** (indigo): Anleitung fürs Logbuch, eine Musterkarte; Lernende legen
   eigene Karten an – nur mit Gruppenkürzel, ohne Namen.
5. **Rückblick** (lila): Abstimmung zur Zielerreichung, Ausblick.

Umfang: 3–6 Karten je Pfad, insgesamt meist 15–30 Karten. Ausgeklappt nur Orientierung und
Aufträge, alles Weitere eingeklappt.

## Muster B – Stundenablauf als Zeitstrahl

```markdown
---
title: "LF 3 – Doppelstunde 5: Steuerung prüfen"
theme: morgen
format: zeitstrahl
---

## 08:00 Informieren [showdate=2026-11-03 08:00:00] [color=tuerkis] [box_color=tuerkis]
### Einstieg [flags=0]
…

## 08:20 Planen [showdate=2026-11-03 08:20:00] [flags=640] [color=mintgruen] [box_color=mintgruen]
### Auftrag [flags=0]
…
```

- Je Phase ein Pfad, Titel mit Uhrzeit und Phase der vollständigen Handlung (Informieren bzw.
  Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw. Kontrollieren · Reflektieren).
- `showdate` = geplanter Beginn; `flags=640` sperrt den Pfad bis dahin (Lösungs- und
  Sicherungsphasen erst später sichtbar). **Datum mit der Lehrkraft abstimmen** – sonst
  `⚠️ Annahme:` und Hinweis im Begleitblatt, dass die Zeiten vor dem Import anzupassen sind.
- Countdown für Arbeitsphasen: `&&count: 900&&`.

## Muster C – Klausurvorbereitung (Generalprobe)

- **Selbstdiagnose je Kompetenz-Cluster** (A, B, C …) mit sicher/unsicher, Empfehlung:
  Pflichtstationen für alle, Wahlstationen nach Diagnose.
- **Stationen** mit Übungsaufgaben **im Stil** der Arbeit (gleiche Operatoren und AFB), nie mit
  den Aufgaben der Arbeit selbst.
- **Übungsklausur** mit Zeitvorgabe (Countdown) und Erwartungshorizont zum Aufdecken.
- **Lernplan** als Checkliste: was bis wann wiederholen.

## Muster D – Lernfeldübersicht

`format: pinnwand`; je Lernsituation ein Pfad mit Karten „Situation", „Ergebnis",
„Zeitraum" und „Material". Zukünftige Lernsituationen eingeklappt; abgeschlossene mit Link
zur Sicherung. Gut als Einstieg ins Schuljahr und für Distanzphasen.

## Muster E – Workshop / Fortbildung

Wie Muster A, ergänzt um einen **Werkzeugkasten** (immer offen), einen **Marktplatz** (bestes
Produkt je Lernposten) und **Transfer** (Plan für die eigene Praxis). Parallel arbeitende
Tandems legen eigene Logbuch-Karten an (Kürzel `T1 · MK`). Für die Moderation eine **getrennte
Regie-Map**, die nicht geteilt wird.

## Gestaltungsregeln (alle Muster)

- **Eine Karte, ein Gedanke** – lieber eine Karte mehr als eine überladene.
- **Farbe bedeutet etwas:** je Pfad eine Farbe, Karten in der Pfadfarbe (`box_color` = `color`);
  Bedeutungen über die ganze Map gleich halten (z. B. grün = Pflicht, bernstein = Wahl).
- **Helles Theme** für Beamer und Ausdruck (`tageslicht`, `morgen`, `kreide`).
- **Gleiche Ansprache** (du oder Sie nach Schulregel) auf allen Karten.
- **Sprachsensibel:** Operator vorn, kurze Sätze, Fachbegriffe mit Tooltip
  `[Begriff]{Erklärung}` statt sie zu umgehen.
- **Lösungen:** nur zur Selbstkontrolle von Übungen und nur zum Aufdecken; nie Lösungen zu
  Leistungsüberprüfungen; Lehrkraft-Hinweise gehören ins Begleitblatt, nicht in die Map.
- **Datenschutz:** keine Namen, Fotos oder Kontaktdaten von Lernenden; Logbücher mit
  Gruppenkürzeln; kein Kennwort in der Quelle.
- **Material verlinken, nicht abschreiben:** lange Texte als PDF hochladen und verlinken;
  in der Karte nur Auftrag und Kern.

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.

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
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen` |
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
| GRAFCET, Funktionsplan, Schaltplan | Fachsoftware; im Text zusätzlich als Tabelle (Schritt, Aktion, Transition) |

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
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

**Werkzeug-Skills** (Nr. 42, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
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
