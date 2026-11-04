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
