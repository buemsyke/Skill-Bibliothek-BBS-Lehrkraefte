---
artefakt: KI-Kennzeichnung – Protokoll
titel: "[Kurs / Projekt / Materialpaket]"
skill: ki-kennzeichnung
skill_version: "1.4"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
status: "KI-Entwurf – fachlich zu prüfen"
---

# KI-Kennzeichnung: [Titel]

**Ordner:** [Pfad] · **Art:** [Kursprojekt mit phase_config.yaml | Ordner mit ki_kennzeichnung.yaml | andere Medien]
**Verantwortlich:** [Name oder Kürzel, Schule] · **KI-System:** [ … ] · **Stand:** [TT.MM.JJJJ]
**Transparenzerklärung:** `[docs/ki-transparenz.md | ki-transparenz.md]`

## Gekennzeichnet

| Datei bzw. Medium | Form | Ergebnis |
|---|---|---|
| [lessons/01_…/lesson.md] | Hinweisbox (MkDocs) | gesetzt |
| [40_material_….md] | Blockzitat | gesetzt |
| [Moodle-Kurs LF 4] | Text 2 aus `vorlage-hinweistexte.md` | von der Lehrkraft einzufügen |

[Ausgabe von `edu-kennzeichnung --pruefen` einsetzen: „Alle Seiten sind gekennzeichnet."]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Material vor der Kennzeichnung von der Lehrkraft geprüft | | Der Hinweis behauptet die Prüfung |
| Verantwortliche Person benannt (kein Platzhalter) | | |
| Transparenzerklärung vorhanden, Platzhalter ersetzt, nur Zutreffendes | | |
| `edu-kennzeichnung --pruefen` ohne Lücken | | |
| Form passt zum Medium (Hinweisbox nur in MkDocs, sonst Blockzitat) | | |
| Angaben in allen Medien gleich (System, Verantwortlich, Stand) | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: Vorgaben von Schule und Land zur Kennzeichnung KI-gestützter Materialien.

## Übergabe

- Nach inhaltlichen Änderungen: Stand im Block `ki_kennzeichnung:` anpassen und
  `edu-kennzeichnung` erneut laufen lassen (ändert nur den Hinweis).
- Empfohlene nächste Skills: `schuelerseiten-veroeffentlichen`

> KI-gestützt erstellt (Skill ki-kennzeichnung v1.4). Fachliche Prüfung und Verantwortung: Lehrkraft.
