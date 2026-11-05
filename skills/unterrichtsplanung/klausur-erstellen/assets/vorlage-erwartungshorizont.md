---
artefakt: Klassenarbeit – Erwartungshorizont
titel: "[Thema der Arbeit]"
skill: klausur-erstellen
skill_version: "1.13"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
art: "Klassenarbeit"
variante: "A"
vertraulich: true
status: "KI-Entwurf – fachlich zu prüfen"
---

# Erwartungshorizont: [Thema]

Bearbeitungszeit: [90] min · Gesamtpunkte: [60] · Bezug: [Lernsituation(en) Nr./Titel]

So konkret, dass eine Vertretung oder Zweitkorrektur zum selben Ergebnis kommt. Jeder Aspekt
ist einzeln bepunktbar.

## Korrekturschablone

Eine Seite zum Abhaken: [N] der [60] Punkte ([Items]) lassen sich direkt mit dieser Tabelle
korrigieren. Bei [Items mit Ermessen] gibt es mehrere richtige Antworten oder Teilpunkte; die
Regeln stehen in den Abschnitten darunter.

| Item | Lösung | P. |
|---|---|---:|
| 1.1 | 1 **A** · 2 **D** · 3 **B** · 4 **E** · 5 **F** | je 1 |
| 1.2 | [Beispiel mit Varianten siehe unten] | 1 + 1 |
| 2.1 | [ … ] | [ … ] |

## Aufgabe 1.1 – [Operator], AFB [I] – [2] P

| # | Erwartete Leistung | Punkte |
|---|---|---|
| 1 | [konkrete, beobachtbare Teilleistung] | 1 |
| 2 | [ … ] | 1 |

**Zulässige Alternativen:** [fachlich gleichwertige Antworten oder Wege mit voller Punktzahl]
**Toleranz:** [z. B. „auch … werten, wenn begründet"; Rundung ±…; Einheit fehlt → −… P]
**Typische Fehler / Teilpunkte:** [woran Teilleistungen erkennbar sind; Antworten, die **0 P.** ergeben]
**Prüfstein:** [Denkfalle der Aufgabe, z. B. Randfall, verneinte Bedingung – oder „keiner“]

Bei Kurzantworten mit mehreren Feldern (Buchstaben, Ausdrücke) je Feld eine Zeile:

| Feld | Lösung | Ebenfalls richtig | Falsch (0 P.) |
|---|---|---|---|
| ① | [ … ] | [gleichwertige Schreibweise] | [typischer Fehler] |

## Aufgabe 2.1 – [Berechnen], AFB [II] – [6] P

| # | Erwartete Leistung | Punkte |
|---|---|---|
| 1 | Formel: [ … ] | 1 |
| 2 | Werte mit Einheiten eingesetzt: [ … ] | 2 |
| 3 | Ergebnis: [Wert mit Einheit, sinnvoll gerundet] | 2 |
| 4 | Plausibilität / Antwortsatz | 1 |

**Folgefehler:** Rechenweg mit falschem Zwischenwert aus [ … ] richtig fortgeführt → volle
Punkte für die Folgeschritte (Folgefehler **einmal** werten).
**Teilpunkte:** richtiges Ergebnis **ohne** Rechenweg höchstens [1 von 2] P.; Soll und Ist
vertauscht (Testen) höchstens [die Hälfte].

## Aufgabe [n] – [Beurteilen], AFB [III] – [8] P

| # | Erwartete Leistung | Punkte |
|---|---|---|
| 1 | Kriterium 1 benannt und auf den Fall angewendet | 2 |
| 2 | Kriterium 2 benannt und auf den Fall angewendet | 2 |
| 3 | Urteil eindeutig | 1 |
| 4 | Begründung schlüssig, Gegenargument abgewogen | 3 |

**Erwartungsspielraum:** [beide Entscheidungen sind vertretbar, wenn …]
**Keine Punkte:** [Kriterien ohne Bezug zum Adressaten; Kriterium genannt, aber nicht angewendet]

## Punkteübersicht

| Aufgabe | Gegenstand | Operator | AFB | Antwort | Punkte | Min. | Bezug |
|---|---|---|---|---|---:|---:|---|
| 1.1 | [ … ] | [nennen] | I | Kurz | 2 | 3 | [LS 1 · K1] |
| 1.2 | | | I | Kurz | 4 | 6 | |
| 2.1 | | [berechnen] | II | Rechnung | 6 | 9 | |
| 2.2 | | | II | Kurz | 6 | 9 | |
| [n].1 | | [beurteilen] | III | Text | 8 | 12 | |
| **Σ** | | | | | **[60]** | **[≤ 85]** | |

*Antwort* = Format der Antwort im Blatt: `Kurz` (Buchstabe, Zahl, Ausdruck, Tabellenzelle),
`Rechnung`, `Skizze`, `Text` (Schreiblinien). `klausur_check.py` rechnet daraus den
Freitextanteil.

## AFB-Nachweis (gerechnet mit `scripts/klausur_check.py`)

| AFB | verlangt wird | Punkte | Anteil |
|---|---|---|---|
| I | [wiedergeben, beschreiben] | [18] | [30 %] |
| II | [anwenden, berechnen, auswählen] | [24] | [40 %] |
| III | [beurteilen, begründen] | [18] | [30 %] |

    Gesamtsummen (AFB I, AFB II, AFB III, gesamt) [18] [24] [18] [60]

## Notenschlüssel ([15-Punkte-System | Kammer-Schlüssel | Schulregel])

[Tabelle aus `klausur_check.py` bzw. `edu-bewertung schluessel --max [60]` einsetzen]

## Lösungsspiegel Single Choice (nur Lernzielkontrolle)

| Frage | Lösung | warum richtig | AFB | Bezug |
|---|---|---|---|---|
| 1 | [C] | [Begründung in einem Satz] | I | [LS 1] |

## Hinweise zur Durchführung und Korrektur

- **Vorher ankündigen:** [Seiten, Aufgaben, Antworten direkt ins Blatt, Hilfsmittel]. Operatoren
  vorab besprechen (besonders *Beurteilen*, *Entwerfen*, *Erweitern*) – oder auf Seite 1 erklärt.
- **Korrektur:** erst alle Arbeiten mit der Schablone, danach die Items mit Ermessen ([ … ]).
  Folgefehler werden einmal gewertet ([z. B. 5.1 → 5.2]).
- **Nach der Korrektur:** Punkte je Teilaufgabe erfassen;
  besonders aussagekräftig sind die Items mit Prüfstein ([ … ]).
- **Bewusst nicht geprüft:** [Themen, die unterrichtet werden, aber nicht Gegenstand dieser
  Arbeit sind – verhindert Streit bei der Rückgabe].
- **Aufsicht:** [eigene Aufsicht → `vorlage-aufsichtsblatt.md`; sonst „Fachlehrkraft“]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Bezug jeder Teilaufgabe zu LS/Kompetenz | | |
| AFB-Verteilung (gerechnet) | | |
| Aufträge kurz, Antwortraum je Operator, Freitextanteil (gerechnet) | | |
| Takt und Minutensumme | | |
| Punktsumme Aufgabenteil = Erwartungshorizont | | |
| Musterlösung nachgerechnet | | |
| `klausur_check.py` ohne ❌ | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Art, Zeit, Punkte, Notenschlüssel: …
- Aufsichtsblatt (bei fremder Aufsicht): `vorlage-aufsichtsblatt.md`
- Empfohlen: Gegenlesen durch eine zweite Lehrkraft (Lösbarkeit Schritt für Schritt)

> KI-gestützt erstellt (Skill klausur-erstellen v1.13). Fachliche Prüfung und Verantwortung: Lehrkraft.
