---
artefakt: Veröffentlichungsprotokoll Schülerausgabe
titel: "[Kurs / Lernfeld / Material]"
skill: schuelerseiten-veroeffentlichen
skill_version: "1.7"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
modus: "[P Kursprojekt | D Einzeldokumente]"
status: "KI-Entwurf – Freigabe durch die Lehrkraft ausstehend"
---

# Veröffentlichung: [Titel]

**Quelle:** [Projektordner bzw. Dateien der Lehrerfassung]
**Ausgabe:** [`_student_site/` bzw. `_schuelerfassung/`] · **Ziel:** [GitHub Pages, Moodle,
Schulserver, Druck] · **Sichtbar für:** [Lerngruppe / öffentlich]

## Inhalt der Ausgabe

| Lektion bzw. Datei | Seiten / Phasen | ausgelassen (Lehrerteil) | Hinweise |
|---|---|---|---|
| [01_gurtfoerderer_warten] | [Situation, Hilfen, Übungen] | [Lösungen, Didaktische Hinweise] | |

## Prüfergebnisse

| Prüfung | Ergebnis | Hinweis |
|---|---|---|
| `ausgabe_pruefen.py` (keine Lehrerinhalte, keine offenen Prüfaufträge) | | |
| Projektkonfiguration (`--projekt`: site-Block, copy_dirs, Überschriften zugeordnet) | | |
| KI-Transparenzhinweis auf jeder Seite (`edu-kennzeichnung --pruefen`) | | |
| `mkdocs build --strict` (interne Links) | | |
| externe Links (`material-pruefen` bzw. `edu-linkcheck`) | | |
| Stichprobe im Browser: Navigation, Bilder, H5P, Formeln | | |

## Freigabe

Ich habe die Schülerausgabe geprüft. Sie enthält keine Lösungen zu Leistungsüberprüfungen,
keine Lehrerhinweise und keine personenbezogenen Daten.

Freigabe: ausstehend

*(Nach Durchsicht ersetzen durch: `Freigabe: erteilt – KÜRZEL, JJJJ-MM-TT`. Erst dann
veröffentlichen.)*

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Lehrerfassung vorher geprüft (Prüfbericht, Freigabe) | | |
| keine Lösungen, Erwartungshorizonte, Bewertungskriterien, vertraulichen Dateien | | |
| alle Abschnitte der Lektionen einer Phase zugeordnet oder bewusst ausgeschlossen | | |
| KI-Kennzeichnung und Transparenzseite vorhanden | | |
| Build und Links ohne Fehler | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: Rechte an Bildern und verlinkten Dateien für eine öffentliche Seite.

## Übergabe

- Ausgabeordner und Build: …
- Veröffentlichung erst nach Freigabezeile (`freigabe_pruefen.py`) und ausdrücklichem
  Auftrag der Lehrkraft.
- Empfohlene nächste Skills: `ki-kennzeichnung`, `material-pruefen` (Links)

> KI-gestützt erstellt (Skill schuelerseiten-veroeffentlichen v1.7). Fachliche Prüfung und Verantwortung: Lehrkraft.
