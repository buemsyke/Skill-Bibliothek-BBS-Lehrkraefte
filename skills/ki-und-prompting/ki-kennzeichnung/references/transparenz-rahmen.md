# KI-Transparenz bei Unterrichtsmaterial – Rahmen und Praxis

## 1. Warum kennzeichnen?

- **Transparenz und Vertrauen:** Lernende, Eltern, Betriebe und Kolleginnen und Kollegen
  sollen erkennen können, dass KI beteiligt war und wer die Inhalte verantwortet.
- **Ethische Leitlinien** der Europäischen Kommission für Lehrkräfte über die Nutzung von KI
  und Daten beim Lehren und Lernen (2022): Transparenz gegenüber Lernenden als Grundsatz.
- **KI-Verordnung (EU) 2024/1689, Art. 50** (Transparenzpflichten, gilt seit 02.08.2026 🔎):
  Abs. 4 verlangt die Offenlegung KI-erzeugter Texte, die veröffentlicht werden, um die
  Öffentlichkeit über Angelegenheiten von öffentlichem Interesse zu informieren – **nicht**,
  wenn die Inhalte menschlich geprüft wurden und eine Person die redaktionelle Verantwortung
  trägt. Für Unterrichtsmaterial einer Lerngruppe ist eine Pflicht daraus 🔎 nicht eindeutig;
  die Kennzeichnung mit benannter verantwortlicher Person entspricht aber genau dem Gedanken
  der Vorschrift und ist gute Praxis. Keine Rechtsberatung – bei Unsicherheit Schulleitung
  bzw. Datenschutzbeauftragte(n) fragen.
- **Chatbots im Kurs:** Nach Art. 50 Abs. 1 sollen Menschen erfahren, dass sie mit einem
  KI-System interagieren; die Pflicht trifft zunächst den **Anbieter** der Plattform, ob eine
  Schule mit eigener Anweisung selbst als Anbieter gilt, ist 🔎 offen. Für Lernende gilt
  unabhängig davon: sichtbarer Hinweis dort, wo der Chat geöffnet wird, und in der Begrüßung
  (`assets/vorlage-hinweistexte.md`, Text 6).
- **Vorgaben von Land und Schule** können eine Kennzeichnung verlangen 🔎 (Erlasse,
  Handreichungen des Kultusministeriums, Medienkonzept der Schule).

## 2. Was gehört in den Hinweis?

| Angabe | warum | Beispiel |
|---|---|---|
| dass KI beteiligt war | Kern der Transparenz | „mit Unterstützung von Künstlicher Intelligenz erstellt" |
| welches System | Nachvollziehbarkeit | „Claude (Anthropic)" |
| dass ein Mensch geprüft hat | Verantwortung, Ausnahme nach Art. 50 Abs. 4 | „von einer Lehrkraft fachlich geprüft und freigegeben" |
| wer verantwortlich ist | Ansprechperson | Name oder Kürzel und Schule |
| Stand | Aktualität | Datum der letzten inhaltlichen Prüfung |
| Link zur ausführlichen Erklärung | Details ohne Textwüste | `ki-transparenz.md` |

Die ausführliche Erklärung (`assets/vorlage-ki-transparenz.md`) sagt zusätzlich, **wofür**
KI genutzt wurde, **was Menschen getan haben** und **was nicht** geschah (z. B. keine
Schülerdaten an KI) – nur Zutreffendes.

## 3. Wann kennzeichnen?

- **Erst nach der Prüfung durch die Lehrkraft.** Der Hinweis sagt „geprüft und
  freigegeben" – vorher wäre er falsch. Entwürfe tragen stattdessen die Transparenzzeile der
  Bibliothek (`KI-gestützt erstellt (Skill …). Fachliche Prüfung und Verantwortung: Lehrkraft.`).
- Bei jeder Veröffentlichung oder Weitergabe an Lernende (Schülerseiten, LMS, Druck,
  edumaps, Quiz).
- Nach inhaltlichen Änderungen: Stand aktualisieren und neu kennzeichnen (idempotent).

**Nicht** gemeint: Texte, die Lernende selbst mit KI erstellen (Regeln dafür stehen in der
Schul- bzw. Prüfungsordnung), und interne Planungsdokumente der Lehrkraft.

## 4. Wie – Markdown mit edu-kennzeichnung

- Der Hinweis steht als Block zwischen den Markern
  `<!-- KI-KENNZEICHNUNG:START … -->` und `<!-- KI-KENNZEICHNUNG:ENDE -->` am Seitenende.
  Erneutes Ausführen ersetzt ihn, verdoppelt ihn nie; `--entfernen` nimmt ihn heraus.
- Zwei Formen: **Hinweisbox** (`!!! info`, nur in MkDocs-Seiten sinnvoll) und
  **Blockzitat** (überall lesbar: GitHub, Word über pandoc, Moodle). Einfache Ordner deshalb
  mit Blockzitat (`kennzeichnung_einrichten.py` setzt das).
- Der Link zur Erklärung wird je Ordnertiefe relativ berechnet.
- **Eine Quelle für die Angaben:** Block `ki_kennzeichnung:` in
  `scripts/phase_config.yaml` (Kursprojekt) bzw. `ki_kennzeichnung.yaml` (Ordner). Im
  Kursprojekt setzt auch `edu-seiten split` die Hinweise in der Schülerausgabe.

```yaml
ki_kennzeichnung:
  verantwortlich: "MH, BBS Musterstadt"     # Pflicht – ohne Angabe bricht edu-kennzeichnung ab
  ki_system: "Claude (Anthropic)"
  stand: "09.10.2026"
  seite: "ki-transparenz.md"                 # Erklärung, projektrelativ
  quellen: ["*.md"]                          # Dateimuster (Glob), projektrelativ
  ausgenommen: ["ki-transparenz.md"]
  blockzitat: ["40_material_wartung.md"]     # exakte Pfade mit Blockzitat-Form
```

`blockzitat` und `ausgenommen` sind **exakte Pfade**, keine Muster; neue Dateien also
nachtragen (oder `kennzeichnung_einrichten.py` neu aufsetzen lassen).

## 5. Andere Medien

Für Word, PDF, Folien, Moodle-Textfelder, H5P und edumaps: fertige Texte in
`assets/vorlage-hinweistexte.md`. Gleiche Angaben wie im Markdown-Hinweis.

## 6. Datenschutz

Die verantwortliche Person wird veröffentlicht – Kürzel und Schule genügen, wenn die Lerngruppe
weiß, wer gemeint ist. Keine privaten Kontaktdaten; als Kontakt die Lehrkraft im Kurs oder
eine Funktionsadresse der Schule.
