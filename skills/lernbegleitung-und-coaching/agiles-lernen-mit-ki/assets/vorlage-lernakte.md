---
artefakt: Lernakte
titel: "[Lernthema]"
skill: agiles-lernen-mit-ki
skill_version: "1.4"
stand: [JJJJ-MM-TT]
lernende: "[Lehrkraft (selbst) | Lerngruppe: Bildungsgang, Ausbildungsjahr bzw. Schuljahrgang – keine Namen]"
plattform: "[Claude Code | Claude (Browser) | AIS.chat]"
start: [JJJJ-MM-TT]
termin: [JJJJ-MM-TT]
status: "Kickoff"            # Kickoff | Sprints | Retro | abgeschlossen
---

# Lernakte: [Lernthema]

## Kickoff

| Frage | Antwort |
|---|---|
| 1 Ziel – was kann ich am Ende, woran merke ich es? | Ich kann [Operator + Gegenstand], nachweisbar durch [Nachweis]. |
| 2 Zeithorizont – bis wann? | bis [TT.MM.JJJJ] ([n] Wochen) |
| 3 Sprint – Länge und Lernzeit je Sprint | [1] Woche · [2] h je Sprint |
| 4 Ort und Zeitpunkt | [wo, wann; feste Termine oder nach Bedarf] |
| 5 Lernform | [Selbststudium mit KI · angeleitete Schulung · Mischform] |
| 6 Ressourcen – Quellen und Menschen | siehe *Quellen* und *Rollen* |

## Rollen

| Rolle | wer | Aufgabe |
|---|---|---|
| Lernende | [Lehrkraft selbst / Lerngruppe – keine Namen] | steuert den Lernpfad, verantwortet das Ergebnis |
| KI – Lernarchitektin | [Claude / AIS.chat] | strukturiert, erklärt, schlägt Quellen und Übungen vor |
| KI – Lernbegleiterin | [Claude / AIS.chat] | fragt nach, prüft das Verständnis |
| Fachexpertin | [Funktion, Kürzel] | checkt den Lernpfad gegen, bleibt ansprechbar |
| Ermöglicher (optional) | [Schulleitung / Ausbildungsbetrieb] | Lernzeit, Anwendungsgelegenheit |

## Quellen (gebunden)

Nur öffentliches oder freigegebenes Material. Fundstelle = wo man nachschlägt.

| Nr. | Quelle | Art | öffentlich | Fundstelle als |
|---|---|---|---|---|
| Q1 | [Titel, Herausgeber, Ausgabe/Stand] | [Handbuch (PDF) / Fachseite / Video / Buch] | [ja] | [Seite / Abschnitt / Minute] |

## Lernpfad

Freigabe Lernpfad: ausstehend

Fragen an die Fachexpertin: Stimmt das Ziel? Fehlt Wesentliches oder ist etwas überflüssig?
Taugen die Quellen? Passt das Niveau?

### Sprint 1 – [Thema]
- **Sprintziel:** Ich kann [Operator + Gegenstand].
- **Zeit:** [2] h
- **Quellen:** [Q1 S. x–y]
- **Lernaktivitäten:** [erklären lassen und nachfragen · Zettel schreiben · Beispiel finden · Übung]
- **Nachweis im Review:** [Probeprüfung P1 (5 Fragen) · in eigenen Worten erklären]
- **Review:** offen
- **Entscheidung:** –

### Sprint 2 – [Thema]
- **Sprintziel:** Ich kann [Operator + Gegenstand].
- **Zeit:** [2] h
- **Quellen:** [Q1 Kap. z]
- **Lernaktivitäten:** [ … ]
- **Nachweis im Review:** [ … ]
- **Review:** offen
- **Entscheidung:** –

### Sprint 3 – [Thema] (grob, wird nach Review 2 geschärft)
- **Sprintziel:** [grob]
- **Zeit:** [2] h
- **Quellen:** [Q2]
- **Review:** offen

## Zettel (Kernaussagen in eigenen Worten)
- Z1 – [Kernaussage] (Q1 S. x)

## Offene Fragen an die Fachexpertin
- [Frage, mit Fundstelle des Widerspruchs]

## Retro
(nach dem letzten Sprint, ca. 20 Minuten)

| Frage | Antwort |
|---|---|
| Was hat funktioniert? | |
| Was hat nicht funktioniert? | |
| Welche Quelle hat getragen, welche nicht? | |
| Was mache ich im nächsten Lernzyklus anders? | |
| Wo lege ich das Ergebnis ab, damit andere es finden? | |

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Ziel als Können mit Termin und Nachweis | ✅/⚠️/❌ | |
| Sprintanzahl und Lernzeit passen in den Zeithorizont | | |
| Fachexpertin benannt, Freigabezeile vorhanden | | |
| Nur öffentliche Quellen, je Sprint Fundstellen | | |
| Keine Namen, Noten, Betriebe | | |
| `lernakte_pruefen.py` ohne ❌ | | |

## Annahmen und Prüfaufträge
- ⚠️ Annahme: [ … ]
- 🔎 Prüfen: [ … ]

## Übergabe
- Nächster Schritt: [Freigabe Lernpfad durch die Fachexpertin / Sprint 1 starten]
- Empfohlene Skills: `quizfragen-erstellen` (Probeprüfung als Moodle-Test), `ki-kennzeichnung`
  (AIS-Paket an Lernende)

> KI-gestützt erstellt (Skill agiles-lernen-mit-ki v1.4). Fachliche Prüfung und Verantwortung: Lernende und Fachexpertin bzw. Lehrkraft.
