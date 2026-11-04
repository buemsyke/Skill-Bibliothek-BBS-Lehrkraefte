# Kursprojekt und Schülerausgabe – Aufbau, Befehle, Stolperfallen

## 1. Zwei Wege zur Schülerausgabe

| | Modus P – Kursprojekt | Modus D – Einzeldokumente |
|---|---|---|
| Quelle | `lessons/NN_slug/lesson.md` je Unterrichtseinheit | Artefakte der Bibliothek (`40_material_…`, `60_differenzierung_…`) oder andere Markdown-Dateien mit Lehrerteil |
| Werkzeug | `edu-seiten split` | `edu-seiten strip` |
| Ergebnis | `_student_site/` – MkDocs-Site, je Lektion eine Seite pro LMS-Phase | `_schuelerfassung/` – dieselben Dateien ohne Lehrerteil |
| Weiter | `mkdocs build --strict` → HTML (GitHub Pages, Schulserver) | Druck/PDF/Word (`pandoc`), Moodle, edumaps |

## 2. Modus P – Aufbau eines Kursprojekts

```
<projekt>/
├── lessons/
│   ├── 00_beispiel/lesson.md        ← ausgeschlossen (excluded_lessons)
│   └── 01_gurtfoerderer_warten/
│       ├── lesson.md                ← H1-Abschnitte = Bausteine der Phasen
│       └── diagrams/                ← nur .drawio.svg wird veröffentlicht
├── solutions/                       ← Lösungen, Lösungsdiagramme – nie veröffentlichen
├── h5p/                             ← Quizquellen (*.md) → h5p/generated/*.h5p
├── docs/ki-transparenz.md           ← Transparenzerklärung (Skill ki-kennzeichnung)
├── scripts/phase_config.yaml        ← Phasen, site-Block, KI-Kennzeichnung
└── _student_site/                   ← erzeugt (docs/, mkdocs.yml)
```

**lesson.md:** Frontmatter (`title`, `lesson_id`, `duration`, `learning_goals`; optional
`kompetenz_codes` sowie `lernsituation` und `teil` "k/n", wenn eine Lernsituation mehrere
Lektionen umfasst – die Seitenerzeugung wertet sie nicht aus) und feste
H1-Überschriften (`vorlage-lektion.md`, didaktisch `lektionsmuster.md`). `edu-seiten split` ordnet jede H1 über
`phase_config.yaml` einer Phase zu; nicht zugeordnete und nicht ausgeschlossene H1 **fallen
still weg**. Unterüberschriften (`##`) wandern mit ihrer H1.

**phase_config.yaml** (`assets/phase_config-vorlage.yaml`):
- `site:` – Name, Startseite, `copy_dirs` (ohne `solutions`), `link_solutions: false`.
  **Ohne `site:`-Block** heißt die Ausgabe „BINFQ2 Datenbanken" und `solutions/` wird
  mitkopiert (Altlast aus Kompatibilitätsgründen).
- `phases:` – Reihenfolge = Reihenfolge im LMS; `sections` exakt wie die H1.
- `excluded_sections:` – nie veröffentlichen (Didaktische Hinweise, Lösungen, Bewertungskriterien).
  Gilt nur für Abschnitte der `lesson.md` – der Ordner `solutions/` wird über `copy_dirs`
  gesteuert.
- `ki_kennzeichnung:` – Angaben für den Transparenzhinweis (Skill `ki-kennzeichnung`).

**Diagramme:** Aus `lessons/*/diagrams/` wird **jede** `.drawio.svg` kopiert.
Lösungsdiagramme (`NN_l01_…`) deshalb unter `solutions/diagrams/` (Skill
`fachdiagramm-erstellen`).

## 3. Befehle (Modus P)

```bash
cd <projekt>
edu-seiten split                                    # installiert
python3 <skill>/scripts/edu.py seiten split --project-root .   # mitgeliefert
python3 <skill>/scripts/ausgabe_pruefen.py _student_site/docs --projekt .
edu-kennzeichnung --pruefen                         # Quellen gekennzeichnet?
cd _student_site && mkdocs build --strict           # HTML, bricht bei toten internen Links ab
mkdocs serve                                         # Vorschau unter http://127.0.0.1:8000
```

`mkdocs` braucht `mkdocs-material` und `pymdown-extensions`
(`python3 -m pip install mkdocs-material pymdown-extensions`). Fehlen sie, die Prüfung mit
`ausgabe_pruefen.py` trotzdem durchführen und den Build als offenen Schritt vermerken.

Quizze: Quellen nach `h5p/` (Skill `quizfragen-erstellen`), dann `edu-h5p .` – `split`
kopiert `h5p/` über `copy_dirs`.

## 4. Befehle (Modus D)

```bash
# eine oder mehrere Dateien im aktuellen Ordner → _schuelerfassung/
edu-seiten strip --teacher . --student _schuelerfassung --lf .=40_material_wartung.md,60_differenzierung_wartung.md
python3 <skill>/scripts/edu.py seiten strip --teacher . --student _schuelerfassung --lf .=40_material_wartung.md
python3 <skill>/scripts/ausgabe_pruefen.py _schuelerfassung
pandoc _schuelerfassung/40_material_wartung.md -o 40_material_wartung_schueler.docx   # optional
```

`strip` entfernt `# Didaktische Hinweise` und `# Lösungen …` jeweils bis zur nächsten
H1 sowie `## Bewertungskriterien …` und `## Erwartungshorizont …`. Bibliotheks-Artefakte
schreiben ihre Pflichtabschnitte (Qualitätscheck, Annahmen, Übergabe) unter
`# Didaktische Hinweise` – sie fallen mit weg. Das gilt seit Bibliothek 1.4 auch für
`differenzierung-erstellen` (Überblick, Organisation) und `sprachsensibel-ueberarbeiten`
(Änderungsprotokoll, Lesbarkeit, Hinweise für die Lehrkraft); ältere Fassungen dieser
Artefakte vorher umstellen – `ausgabe_pruefen.py` meldet die Abschnitte auch nummeriert. Andere Überschriften (z. B. „Lösungsvorschlag",
„Hinweise für Lehrkräfte") erkennt `strip` nicht; `ausgabe_pruefen.py` meldet sie – dann in
der Lehrerfassung umbenennen und erneut erzeugen.

## 5. Veröffentlichen – nur nach Freigabe

1. Lehrerfassung geprüft (`material-pruefen`, Ampel mindestens 🟡) und Schülerausgabe
   erzeugt.
2. `ausgabe_pruefen.py` ohne ❌, KI-Kennzeichnung vollständig, Build ohne Fehler.
3. Lehrkraft sieht die Ausgabe durch und trägt im Veröffentlichungsprotokoll
   `Freigabe: erteilt – KÜRZEL, JJJJ-MM-TT` ein; `freigabe_pruefen.py` bestätigt.
4. **Erst dann und nur auf ausdrücklichen Auftrag:** veröffentlichen (Commit und Push für
   GitHub Pages, Upload nach Moodle oder auf den Schulserver). Claude veröffentlicht nichts
   eigenständig.

**Öffentlich oder Lerngruppe?** Eine öffentliche Seite (GitHub Pages) ist für alle
lesbar und wird ggf. von Suchmaschinen erfasst: keine Lösungen zu Klassenarbeiten, keine
Fotos oder Namen von Lernenden, Rechte an Bildern und Texten klären 🔎. Material nur für die
Lerngruppe gehört ins LMS.

## 6. Häufige Fehler

| Fehler | Folge | Abhilfe |
|---|---|---|
| kein `site:`-Block | falscher Titel, Lösungen veröffentlicht | Block aus der Vorlage übernehmen |
| H1 mit Tippfehler („Hilfestellung") | Abschnitt fehlt still | H1 exakt wie in `sections` |
| Lösungsdiagramm in `lessons/*/diagrams/` | Lösung veröffentlicht | nach `solutions/diagrams/` |
| `solutions` in `copy_dirs` | Lösungen veröffentlicht | entfernen, `link_solutions: false` |
| Lehrerteil unter anderer Überschrift | bleibt in der Schülerfassung | umbenennen (`# Didaktische Hinweise`, `# Lösungen …`) |
| offene `⚠️ Annahme:`/`🔎 Prüfen:` | Planungsnotizen bei Lernenden | in der Lehrerfassung klären |
