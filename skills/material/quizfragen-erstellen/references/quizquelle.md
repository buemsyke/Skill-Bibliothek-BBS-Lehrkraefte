# Quizquelle – das eine Eingabeformat für edu-quiz und edu-h5p

Eine `.md`-Datei in diesem Format wird deterministisch nach **GIFT** (Moodle-Fragensammlung)
und **H5P** exportiert. Vollständiges Beispiel mit allen Typen: `assets/vorlage-quiz.md`.

```bash
edu-quiz 65_quiz_gurtfoerderer.md --to both --category "LF4/LS 4.2"
python3 scripts/edu.py quiz 65_quiz_gurtfoerderer.md --to both --category "LF4/LS 4.2"   # mitgeliefert
# → 65_quiz_gurtfoerderer.gift und 65_quiz_gurtfoerderer.h5p neben der Quelle
```

## 1. Aufbau

```
# Quiz Lektion 4: LS 4.2 – Gurtförderer warten      ← Titel des H5P-Pakets

## Übung 1 – Kurzbeschreibung (H5P.MultiChoice) | AFB I
**Titel:** Nachschmieren der Lager                   ← Fragetitel in Moodle (::Titel::)
<typabhängiger Körper>

## Übung 2 – …
```

- **Kopfzeile** muss `Lektion <Zahl>:` enthalten, sonst heißt das H5P-Paket „Quiz". Die
  Zahl ist frei (z. B. Nummer des Lernfelds).
- **Übungskopf** genau so: `## Übung <Nr> – <Beschreibung> (H5P.<Typ>) | AFB <I|II|III>`
  (Gedankenstrich oder Bindestrich). Wird er nicht erkannt, fällt die Übung still weg.
- **Alles bis zur nächsten `## Übung`** gehört zur Übung – auch Abschnitte wie
  `## Qualitätscheck` am Dateiende. Deshalb stehen Qualitätscheck und Übergabe im
  Begleitblatt, nicht in der Quelle. Kommentare vor der Kopfzeile als `<!-- … -->`.
- `**Titel:**` je Übung, **eindeutig** – sonst heißen in der Fragensammlung alle Fragen gleich.
- **Was die Lernenden zum Lösen brauchen** (Anlagendaten, Vorgaben), gehört in `**Frage:**`
  bzw. bei Lückentexten **in denselben Absatz des Blockzitats** wie die Lücken. Freier Text
  davor oder dazwischen wird nicht exportiert – die Frage wäre unlösbar. `quiz_pruefen.py`
  meldet solche Zeilen.

## 2. Typen

| Lernziel | Typ | GIFT-Export |
|---|---|---|
| Begriff/Fakt erkennen, Fall einordnen | `H5P.MultiChoice` mit einem `- [x]` | Single Choice (`=`/`~`) |
| mehrere Merkmale auswählen | `H5P.MultiChoice` mit mehreren `- [x]` | Mehrfachauswahl mit Prozenten |
| Aussage prüfen, Fehlvorstellung aufdecken | `H5P.TrueFalse` (Tabelle) | `{T}`/`{F}` je Zeile |
| Fachbegriff aktiv einsetzen | `H5P.Blanks` | Lückentext `{=…}`, **eine Frage je Lücke** |
| Rechenergebnis prüfen | `H5P.Blanks` mit Zahlenlücke `*22,7±0,3*` | numerisch `{#22.7:0.3}` mit Toleranz |
| Begriffe zuordnen | `H5P.DragText` (Blockzitat) oder `H5P.DragQuestion` (Tabelle) | Lückentext |
| Ablauf ordnen | `H5P.SortParagraphs` | Freitext, Reihenfolge als Kommentar für die Lehrkraft |
| begründen, beurteilen | `H5P.Essay` | Freitext `{}` (Lehrkraft bewertet) |

### MultiChoice

```
## Übung 1 – Grundmaßnahmen (H5P.MultiChoice) | AFB I
**Titel:** Nachschmieren der Lager

**Frage:** Zu welcher Grundmaßnahme gehört das Nachschmieren der Lager?
- [x] Wartung → Feedback: Richtig, Wartung bewahrt den Sollzustand.
- [ ] Inspektion → Feedback: Inspektion stellt den Istzustand nur fest.
- [ ] Instandsetzung
- [ ] Verbesserung

**Feedback:** allgemeine Rückmeldung (optional)
```

- Richtige Antwort `- [x]` – **kleines x**; `[X]` wird nicht erkannt.
- Mehrere `- [x]` → Mehrfachauswahl; edu-quiz verteilt die Prozente (falsche Antworten
  negativ).
- Mehrere Fragen in einer Übung: `**Frage 1:** …`, `**Frage 2:** …`.
- Code zur Frage: ein Code-Block (```` ``` ````) in der Übung wird an die Frage angehängt.

### TrueFalse

```
## Übung 3 – Aussagen (H5P.TrueFalse) | AFB I
**Titel:** Aussagen zur Instandhaltung

| Aussage | Bewertung |
|---|---|
| Bei der Inspektion wird der Istzustand festgestellt. | **Wahr** |
| Ein Lagertausch ist Wartung. | **Falsch** – Tausch ist Instandsetzung. |
```

Jede Zeile wird eine Frage. Text nach `**Falsch** –` ist die Rückmeldung bei falscher
Antwort. Zeilen ohne `**Wahr**`/`**Falsch**` werden übergangen. Wahre und falsche Aussagen
mischen.

### Blanks (Lückentext)

Zwei gleichwertige Schreibweisen:

```
> Die Grundmaßnahmen sind Wartung, *Inspektion*, *Instandsetzung* und *Verbesserung*.
```

```
1. Der Akkumulator gehört **\*vor\*** die Schleife.
```

- Im Blockzitat (`>`) reicht `*Antwort*`. Außerhalb eines Blockzitats `**\*Antwort\***`
  verwenden; dann dürfen Lücken auch in Tabellen und Code-Blöcken stehen.
- Alternativen: `*Wartung/Pflege*`. Tipp (nur H5P): `*Wartung:Sollzustand bewahren*`.
- **Nicht in Antworten:** `/` (trennt Alternativen), `:` (leitet Tipp ein), `<`, `>`, `&`
  (so nicht eintippbar) – umformulieren oder MultiChoice verwenden. edu-quiz warnt.
- **Zahlenlücken** (eduwerkzeuge ≥ 0.2.2): `*22,7±0,3*` (auch `+/-`) – Moodle wertet jeden
  Wert im Bereich, mit Komma oder Punkt; `*25*` wird ebenfalls numerisch. H5P kennt keine
  Toleranz und nimmt nur Komma-, Punkt- und gerundete Ganzzahl-Fassung. Toleranz nach der
  Rundung der Aufgabe wählen (eine Nachkommastelle → ±0,1 bis ±0,3).
- **GIFT: eine Frage je Lücke.** Moodle wertet je GIFT-Frage nur den ersten Antwortblock aus;
  edu-quiz legt deshalb je Lücke eine Frage „Titel (k/n)“ an, die übrigen Lücken stehen dort
  als „…“. Lücken so setzen, dass jede Frage mit „…“ verständlich bleibt.
- Der Aufgabenkörper endet vor `**Feedback…**`, `**Tipp…**`, `**Hinweis…**`,
  `**Bewertung…**` oder `---`.

### DragText (Zuordnung im Text)

```
> Das Nachschmieren ist *Wartung*. Das Messen der Gurtspannung ist *Inspektion*.
```

Zuordnung als Tabelle (zwei Spalten) mit Typ `H5P.DragQuestion`:

```
## Übung 5 – Begriffe (H5P.DragQuestion) | AFB II
**Titel:** Arbeiten zuordnen

| Arbeit | Grundmaßnahme |
|---|---|
| Lager nachschmieren | Wartung |
| Gurtspannung messen | Inspektion |
```

### SortParagraphs

```
**Aufgabenstellung:** Bringen Sie die Schritte in die richtige Reihenfolge.

1. Wartungsplan auswerten
2. Anlage stillsetzen und sichern
3. Probelauf durchführen
```

Die Liste steht in der richtigen Reihenfolge; H5P mischt sie. Mindestens drei Schritte.

### Essay

```
**Aufgabentext:**
Beurteilen Sie, ob der Förderer weiterlaufen kann, und begründen Sie Ihre Empfehlung.

**Schlüsselwörter:**
- Verschleiß
- Instandsetzung

**Musterlösung:**
…
```

Schlüsselwörter steuern die automatische Rückmeldung in H5P; in GIFT stehen sie und die
Musterlösung als Kommentar nur für die Lehrkraft.

## 3. Formeln und Code

Moodle zeigt Formeln über den Filter *MathJax* (für Kurs bzw. Website aktiv 🔎), H5P nur mit
der Bibliothek *MathDisplay* auf der Plattform 🔎. In der Quelle steht TeX mit diesen
Begrenzern – in Frage, Antworten und Rückmeldungen gleich:

| wofür | schreiben | nicht |
|---|---|---|
| Formel im Satz | `\( P = U \cdot I \)` | `$P = U \cdot I$` (rendert Moodle nicht) |
| abgesetzte Formel | `$$ P = \frac{W}{t} $$` | Formel im Codeblock |
| Einheit, Dezimalkomma | `\( 2{,}3\,\mathrm{kW} \)` | `2,3 kW` innerhalb der Formel ohne `{,}` |
| Code zur Frage | Codeblock mit Sprache (```` ```cpp ````) | Code im Fließtext mit `{ }` ohne Codeblock |

- **Maskieren ist Sache des Werkzeugs:** `edu-quiz` (≥ 0.2.3) setzt vor `\ { } = ~ # :` in
  Titel, Frage, Antworten und Rückmeldungen einen Backslash – in der Quelle also normales TeX
  bzw. normalen Code schreiben, **nicht** selbst maskieren. Ältere Fassungen ließen den
  Fragetext unmaskiert; Moodle las dann das erste `{` einer Formel als Antwortblock.
- **Zahlen, die geprüft werden,** gehören in eine Zahlenlücke (`*2,3±0,1*`), nicht in eine
  Formel – Moodle wertet Formeltext nicht numerisch.
- `quiz_pruefen.py` meldet `$ … $`, unpaarige `\( \)` bzw. `$$` und nennt die Zahl der Formeln
  (Erinnerung an MathJax und MathDisplay).

## 4. Stolperfallen

| Fehler | Folge | Abhilfe |
|---|---|---|
| Übungskopf ohne `(H5P.Typ)` oder mit anderem Strich | Übung fehlt | Kopf exakt nach Abschnitt 1 |
| `- [X]` | Antwort gilt als falsch | `- [x]` |
| Abschnitt nach der letzten Übung | hängt an der letzten Übung | ins Begleitblatt |
| gleiche Titel | Fragensammlung unübersichtlich | eindeutige Titel |
| `/` oder `:` in einer Lücke | Lücke unlösbar | umformulieren |
| „alle/keine der genannten" | rät sich leicht | echte Ablenker |
| Formel mit `$ … $` | erscheint als Text mit Dollarzeichen | `\( … \)` |

`scripts/quiz_pruefen.py` findet diese Fehler vor dem Export.

## 5. In Moodle und H5P verwenden

- **GIFT:** Kurs → *Fragensammlung* → *Importieren* → Format *GIFT* → Datei wählen. Die
  Kategorie (`--category`) legt Moodle an. Danach im Test „aus Fragensammlung hinzufügen".
  Antworten mischen lassen (Test-Einstellung). 🔎 Menübezeichnungen je Moodle-Version.
- **H5P:** `.h5p` als H5P-Aktivität oder in der Inhaltsdatenbank hochladen; auf
  Schülerseiten über `schuelerseiten-veroeffentlichen` einbinden.
- Freitext- und Reihenfolge-Fragen bewertet in Moodle die Lehrkraft.
