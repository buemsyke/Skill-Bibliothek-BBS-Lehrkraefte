---
artefakt: Quiz – Begleitblatt
titel: "[Thema des Quiz]"
skill: quizfragen-erstellen
skill_version: "2.6"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
zweck: "[Einstieg | Übung | Sicherung | Selbsttest]"
status: "KI-Entwurf – fachlich zu prüfen"
---

# Quiz: [Thema]

**Dateien:** `65_quiz_[kurztitel].md` (Quelle, hier ändern) · `65_quiz_[kurztitel].gift`
(Moodle) · `65_quiz_[kurztitel].h5p` (H5P) – erzeugt mit edu-quiz, nicht von Hand ändern
**Bezug:** [Lernsituation / Material, Dateinamen] · **Moodle-Kategorie:** [LF4/LS 4.2]
**Einsatz:** [Zweck, Zeitpunkt, geschätzte Bearbeitungszeit in Minuten]

## Übersicht

| Übung | Titel | Typ | AFB | Bezug (Kompetenz/Inhalt) |
|---|---|---|---|---|
| 1 | [ … ] | MultiChoice | I | [Kompetenz aus der LS] |

[Zeile „Übungen · Fragen · AFB I/II/III · Typen" aus `quiz_pruefen.py` einsetzen]

## In Moodle und H5P verwenden

1. **GIFT:** Kurs → *Fragensammlung* → *Importieren* → Format *GIFT* →
   `65_quiz_[kurztitel].gift`. Danach im Test „aus Fragensammlung hinzufügen"; Antworten
   mischen lassen. Freitext- und Reihenfolge-Fragen bewertet die Lehrkraft.
2. **H5P:** `65_quiz_[kurztitel].h5p` als H5P-Aktivität oder in der Inhaltsdatenbank
   hochladen bzw. auf den Schülerseiten einbinden.
3. Einmal als Lernende bzw. Lernender durchspielen (Rückmeldungen, Lücken, Prozente).

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| `quiz_pruefen.py` ohne ❌, jede Übung liefert eine Frage | | |
| Export mit edu-quiz ohne Warnungen, GIFT gesichtet | | |
| Bezug jeder Übung zu Kompetenz/Inhalt, nur Unterrichtetes | | |
| AFB-Verteilung (gezählt) und Typenvielfalt | | |
| Ablenker plausibel, Rückmeldung zu falschen Antworten | | |
| Zahlen nachgerechnet, Fachbegriffe korrekt | | |
| Bloom-Check (`edu.py check bloom`) gesichtet | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Quelle und Exporte: …
- Übungen mit hoher Fehlerquote später als Hilfekarte
  (`differenzierung-erstellen`) aufgreifen.
- Empfohlene nächste Skills: `schuelerseiten-veroeffentlichen` (H5P einbinden),
  `lernlandkarte-erstellen` (Selbstcheck in der Lernlandkarte), `material-pruefen`

> KI-gestützt erstellt (Skill quizfragen-erstellen v2.6). Fachliche Prüfung und Verantwortung: Lehrkraft.
