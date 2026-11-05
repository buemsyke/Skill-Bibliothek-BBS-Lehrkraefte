---
name: quizfragen-erstellen
description: Erstellt kompetenzorientierte Quizfragen für Moodle und H5P aus Lernsituation, Material, Text oder Themenliste – Single und Multiple Choice, Wahr/Falsch, Lückentext, Zuordnung, Reihenfolge, Freitext – als eine Markdown-Quelle, die das mitgelieferte Werkzeug edu-quiz deterministisch nach GIFT (Moodle-Fragensammlung) und H5P exportiert. Prüft Aufbau, Antworten, Lücken, Titel und AFB-Verteilung per Skript (quiz_pruefen.py, Bloom-Check) und liefert ein Begleitblatt mit Übersicht und Import-Anleitung. Verwenden bei „Quiz erstellen", „Moodle-Fragen", „GIFT-Datei", „H5P-Übung", „Lückentext", „Wiederholungsfragen zur Lernsituation", „Selbsttest" oder „Fragen für die Sicherungsphase". Nicht für benotete Klassenarbeiten und nicht für die Probeprüfung in einer Lernakte (agiles-lernen-mit-ki, kann diesen Fragenpool nutzen).
metadata:
  version: "2.6"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  eduwerkzeuge: "quiz, check"
  ersetzt: "quizfragen-erstellen 1.x (eduwerkzeuge)"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Quizfragen erstellen (GIFT und H5P)

## Zweck
Übungs- und Selbsttestfragen, die **eine Kompetenz je Frage** prüfen und Lernenden eine
Rückmeldung geben – aus **einer** Markdown-Quelle für Moodle (GIFT) und H5P. Claude schreibt
nur den Inhalt; das fehleranfällige Format (Escaping, Prozente bei Mehrfachauswahl, H5P-Paket)
erzeugt das getestete Werkzeug `edu-quiz`. GIFT und H5P nie von Hand schreiben.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Begleitblatt). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht (sonst Rückfrage):** Inhalt – Lernsituation, Material, Text oder Themenliste.
- **Wichtig, sonst Annahme:** Zweck (Einstieg/Vorwissen, Übung, Sicherung, Selbsttest vor der
  Klassenarbeit), Anzahl (Standard 8–12 Übungen), Typen (Standard gemischt), AFB-Verteilung
  (Standard etwa 40/40/20 – Übung mit Rückmeldung verträgt mehr AFB III als die LZK mit 40/50/10), Ansprache (du/Sie), Moodle-Kategorie, Ziel (GIFT, H5P, beides).
- **Optional:** Planungsakte, Erwartungshorizonte (typische Fehler als Ablenker), Projekt mit
  `h5p/`-Ordner (Schülerseiten).

## Leitlinien (verbindlich)
1. **Eine Frage, eine Kompetenz.** Jede Übung ist einer Kompetenz bzw. einem Inhalt der
   Lernsituation zugeordnet (Begleitblatt, Spalte *Bezug*). Nur Unterrichtetes abfragen.
2. **Typ nach Lernziel** wählen, nicht nach Bequemlichkeit (Tabelle in
   `references/quizquelle.md`); mindestens drei Typen bei acht und mehr Übungen.
3. **Kognitiv aktivieren:** höchstens rund die Hälfte AFB I; Anwendungsfragen in der
   Handlungssituation verankern; mindestens eine Beurteilungsfrage (AFB III) – in Moodle als
   Freitext von der Lehrkraft bewertet. Operatoren: `references/operatoren-afb.md`.
4. **Ablenker sind plausibel:** typische Fehlvorstellungen aus Unterricht und
   Erwartungshorizont; gleiche Länge und Form wie die richtige Antwort; keine „alle/keine der
   genannten", keine doppelten Verneinungen.
5. **Rückmeldung, die weiterhilft:** zu jeder falschen Antwort ein Satz, *warum* sie falsch
   ist (`→ Feedback:`); bei Wahr/Falsch die Berichtigung nach `**Falsch** –`.
6. **Fachlich und rechnerisch geprüft:** Zahlen nachrechnen (mit Code), Einheiten mitführen;
   keine erfundenen Normen oder Grenzwerte – sonst `🔎 Prüfen:` im Begleitblatt. Rechenergebnisse
   als **Zahlenlücke mit Toleranz** (`*22,7±0,3*`, `references/quizquelle.md`), nicht als Text.
7. **Sprachsensibel und knapp:** kurze Fragen (Stamm ≤ ~25 Wörter), Operator vorn,
   Fachbegriffe beibehalten, keine Fangfragen über Sprache; keine Einleitung, keine Emojis,
   keine Floskeln im Feedback (`references/schuelermaterial.md`).
8. **Keine Personendaten** in Fragen; fiktive Betriebe und Personen aus der Lernsituation.
9. **Formeln für MathJax:** `\( … \)` im Satz, `$$ … $$` abgesetzt – nie `$ … $` (rendert
   Moodle nicht); Einheiten in `\mathrm{…}`. Code als Codeblock. Maskieren für GIFT übernimmt
   `edu-quiz` (mitgeliefert ≥ 0.2.3; `references/quizquelle.md`, Abschn. 3).

## Vorgehen
1. **Inhalt sichten:** prüfbare Teilkompetenzen und typische Fehler listen; mit
   Planungsakte Situation und Begriffe übernehmen.
2. **Bauplan** (intern): Übung · Kompetenz/Bezug · Typ · AFB.
3. **Quelle schreiben** nach `references/quizquelle.md`; Aufbau wie
   `assets/vorlage-quiz.md`. Kopfzeile `# Quiz Lektion N: Titel`, jede Übung
   `## Übung N – Beschreibung (H5P.Typ) | AFB X` mit `**Titel:**`. Nichts nach der letzten
   Übung (würde ihr angehängt).
4. **Prüfen:** `python3 scripts/quiz_pruefen.py 65_quiz_<kurztitel>.md` – alle ❌ beheben,
   ⚠ beheben oder im Begleitblatt begründen. Ergänzend Bloom-Streuung:
   `python3 scripts/edu.py check bloom 65_quiz_<kurztitel>.md` (Hinweise, keine Urteile).
5. **Exportieren:**
   `edu-quiz 65_quiz_<kurztitel>.md --to both --category "LF4/LS 4.2"` (installiert) oder
   `python3 scripts/edu.py quiz 65_quiz_<kurztitel>.md --to both --category "LF4/LS 4.2"`
   (mitgeliefert) → `.gift` und `.h5p` neben der Quelle. Warnungen zu Lücken in der
   Quelle beheben und neu exportieren – nie `.gift`/`.h5p` von Hand ändern.
6. **Sichten:** GIFT-Datei lesen (Fragen vollständig, Prozente plausibel, je Frage genau ein
   unmaskierter Antwortblock `{…}` – Klammern in Formeln und Code stehen als `\{ \}` –,
   Zahlenlücken als `{#…}`).
7. **Begleitblatt** nach `assets/vorlage-begleitblatt.md`: Übersicht mit Bezug und AFB,
   Import-Anleitung, Qualitätscheck, Annahmen, Übergabe.

**Projekt mit Schülerseiten:** Quelle nach `<projekt>/h5p/` legen; `edu-h5p` (bzw.
`python3 scripts/edu.py h5p <projekt>`) erzeugt alle Quizze nach `h5p/generated/`;
`schuelerseiten-veroeffentlichen` bindet sie ein.

**Ohne Skriptausführung** (Assistent ohne Code): Quelle und Begleitblatt ausgeben; Export
lokal mit `edu-quiz`. Muss GIFT ausnahmsweise direkt entstehen, streng nach
`references/gift-format.md` und im Begleitblatt als `⚠️ ungeprüft (ohne edu-quiz)` markieren.

## Ausgabe
- `65_quiz_<kurztitel>.md` – Quelle (hier ändern)
- `65_quiz_<kurztitel>.gift` und `65_quiz_<kurztitel>.h5p` – erzeugt mit `edu-quiz`
- `65_quiz_<kurztitel>_begleitblatt.md` – Artefakt nach Skill-Vertrag mit Kopf und
  Pflichtabschnitten
- Planungsakte: Artefakt 65 eintragen.

## Qualitätscheck
- [ ] `quiz_pruefen.py` ohne ❌; jede Übung liefert mindestens eine Frage?
- [ ] Jede Übung mit Bezug zu Kompetenz/Inhalt; nur Unterrichtetes?
- [ ] AFB gemischt (höchstens etwa die Hälfte AFB I), mindestens drei Typen?
- [ ] Ablenker plausibel, Rückmeldung zu falschen Antworten?
- [ ] Zahlen nachgerechnet, Fachbegriffe korrekt, nichts erfunden?
- [ ] Formeln mit `\( … \)`/`$$ … $$`, MathJax im Kurs bzw. H5P MathDisplay geprüft 🔎?
- [ ] Export ohne Warnungen; GIFT gesichtet?
- [ ] Titel eindeutig, Moodle-Kategorie gesetzt?
- [ ] Fragen und Feedback knapp, ohne Einleitung und Dekoration (`references/schuelermaterial.md`)?
      Von Hand prüfen: `schuelermaterial_pruefen.py` passt nicht zur Quizquelle – Reihenfolge- und
      Zuordnungsfragen sind kurze Einzelzeilen und würden als Kleinschrittigkeit gemeldet.

## Beispielaufrufe
> „Erstelle zu `20_lernsituation_gurtfoerderer.md` zehn Übungsfragen für die Sicherung,
> gemischte Typen, Sie-Form, Moodle-Kategorie LF4/LS 4.2, GIFT und H5P."

> „Mach aus dem Infotext zu Schmierstoffen einen Lückentext und eine Zuordnung als H5P für
> die Schülerseiten."

## Referenzen – wann lesen
- `references/quizquelle.md` – **immer** (Format je Typ, Typwahl, Stolperfallen).
- `assets/vorlage-quiz.md`, `assets/vorlage-begleitblatt.md` – **immer** (Ausgabeformat).
- `references/operatoren-afb.md` – Operatoren und AFB.
- `references/gift-format.md` – nur ohne Skriptausführung oder zur Fehlersuche im Import.
- `references/schuelermaterial.md` – Material für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/quiz_pruefen.py` – Prüfung vor dem Export.
- `scripts/edu.py` – startet `edu-quiz`, `edu-h5p`, `edu-check` aus der mitgelieferten Kopie
  (`scripts/eduwerkzeuge/`).
