---
artefakt: Probeprüfung
titel: "P[n] – [Thema des Sprints]"
skill: agiles-lernen-mit-ki
skill_version: "1.4"
stand: [JJJJ-MM-TT]
lernakte: "93_lernakte_[thema].md"
sprint: [n]
status: "KI-Entwurf – Lösungen an der Fundstelle prüfen"
---

# Probeprüfung P[n] – [Thema]

Selbstkontrolle zum Sprintziel, **keine Note**. Herkunft der Fragen:
[öffentliche Musterfragen: Titel, Stand | KI-erstellt aus Q1, Q2 – Lösungen an der Fundstelle prüfen].

So läuft es: Die KI stellt die Fragen **einzeln** und nennt Lösungen erst am Ende. Die
lernende Person öffnet diese Datei erst nach der Probeprüfung.

## Fragen

### Frage 1 – [Kapitel/Thema]
[Fragetext]
- a) [ … ]
- b) [ … ]
- c) [ … ]
- d) [ … ]

### Frage 2 – [Kapitel/Thema]
[Fragetext – Mehrfachauswahl: „Wähle zwei."]
- a) [ … ]
- b) [ … ]
- c) [ … ]
- d) [ … ]

### Frage 3 – [Kapitel/Thema]
[Aussage] – wahr oder falsch?

## Auswertung

Spalte *Antwort* während der Probeprüfung füllen; dann
`python3 scripts/probepruefung_auswerten.py 93_probepruefung_[thema]_P[n].md`.
Mehrfachauswahl als `a,c`; wahr/falsch als `w`/`f`; leer = nicht beantwortet.

| Nr. | Kapitel | Lösung | Antwort | Fundstelle |
|---|---|---|---|---|
| 1 | [Kap.] | [c] | | [Q1 S. x] |
| 2 | [Kap.] | [a,d] | | [Q1 S. y] |
| 3 | [Kap.] | [f] | | [Q2 Abschn. z] |

<!-- Hier die Ausgabe von probepruefung_auswerten.py einfügen; sie beginnt mit „## Ergebnis P[n]“
     und endet mit der Zeile für die Lernakte: - **Beleg:** P[n] x/n richtig (… %) · wiederholen: … -->

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Jede Frage prüft das Sprintziel; je Kapitel mindestens eine Frage | ✅/⚠️/❌ | |
| Jede Lösung mit Fundstelle in einer öffentlichen Quelle | | |
| Fragen kurz und eindeutig, keine Hinweise auf die Lösung im Fragetext | | |
| Keine Note, keine personenbezogenen Daten | | |

## Annahmen und Prüfaufträge

- 🔎 Prüfen: KI-erstellte Lösungen an der Fundstelle prüfen (Fachexpertin bzw. Lehrkraft).

## Übergabe

- Zeile **Beleg** in die Lernakte (`93_lernakte_[thema].md`), Review des Sprints.

> KI-gestützt erstellt (Skill agiles-lernen-mit-ki v1.4). Fachliche Prüfung und Verantwortung: Lernende und Fachexpertin bzw. Lehrkraft.
