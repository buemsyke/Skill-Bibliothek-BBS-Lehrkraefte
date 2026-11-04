---
artefakt: Experiment
titel: "[Frage des Versuchs]"
skill: experiment-planen
skill_version: "1.4"
stand: JJJJ-MM-TT
bildungsgang: "[Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld/Lerngebiet]"
dqr: 4
status: "KI-Entwurf – fachlich und sicherheitlich zu prüfen"
versuchsart: "[Schülerversuch | Lehrerversuch]"
---

# Versuch: [Titel]

<!-- Überschriften so lassen – versuch_pruefen.py prüft sie. Sicherheitsangaben aus dem
     Sicherheitsdatenblatt übernehmen, nicht aus dem Gedächtnis. Teil für Lernende kurz,
     mit Skizze und Diagramm, ohne Prüfvermerke (schuelermaterial.md). -->

## Fragestellung und Hypothese

**Frage aus der Handlungssituation:** [Was soll der Versuch für den Auftrag klären?]

**Ihre Vorhersage (vor dem Versuch):** Ich erwarte, dass … , weil … – skizzieren Sie den
erwarteten Verlauf in das Diagramm der Auswertung.

## Variablen

| Variable | Größe | Wie? |
|---|---|---|
| unabhängig (verändern) | [z. B. Elektrodenmaterial] | [Stufen] |
| abhängig (messen) | [z. B. Gasvolumen] | [Messgerät] |
| konstant halten | [z. B. Elektrolyt, Abstand] | [Wert] |

## Material und Geräte

- [Gerät mit Kenndaten, z. B. Netzgerät 0–12 V DC, Strombegrenzung]
- [Stoff mit Menge und Konzentration]

## Aufbau

ABBILDUNG: [Versuchsaufbau als beschriftete Skizze – Geräte, Messstellen, Polung; Quelle, Alternativtext]

## Durchführung

**Sicherheit – so und in dieser Reihenfolge:** [Schutzbrille, Spannung und Mengen, Aufbau vor
dem Einschalten von der Lehrkraft prüfen lassen]

**Planen Sie** die Messreihe – Einstellungen, Wiederholungen, Reihenfolge – und tragen Sie sie
in die Tabelle ein. *(Öffnungsgrad „angeleitet“. Nur bei „geschlossen“ stehen hier kurze
Schritte, Begründung in den Didaktischen Hinweisen.)*

## Messwerte

| Messung | [Größe] in [Einheit] | [Größe] in [Einheit] | [Größe] in [Einheit] |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Auswertung

1. **Stellen Sie** [abhängige Größe] über [unabhängiger Größe] in einem Diagramm **dar** (Achsen
   mit Größe und Einheit) und [Rechnung mit Formel].
2. Vergleichen Sie mit Ihrer Vorhersage: bestätigt, widerlegt oder offen? Begründen Sie.
3. **Rückbindung:** Was bedeutet Ihr Ergebnis für [Anlage der Handlungssituation]?

## Fehlerbetrachtung

- Messunsicherheit der Geräte und der Ablesung: …
- Systematische Fehler: …

# Lösungen und Erwartungshorizont

| Größe | Erwartung | Herkunft |
|---|---|---|
| [Größe] | [Wert mit Einheit] | Erwartung aus Rechnung (`messwerte_pruefen.py …`) – nach Vorversuch ersetzen |

# Didaktische Hinweise

## Gefährdungsbeurteilung (Entwurf)

| Feld | Eintrag |
|---|---|
| Versuch, Lerngruppe | [Schüler- oder Lehrerversuch, Gruppengröße] |
| Stoffe | [Stoff, Menge, Konzentration, Gefahrenhinweise 🔎 Sicherheitsdatenblatt] |
| Geräte | [Spannung, Leistung, bewegte Teile] |
| Gefährdungen | [chemisch, elektrisch, mechanisch, thermisch] |
| Ersatzstoffprüfung | [geprüfte Alternativen und Entscheidung] |
| Maßnahmen (STOP) | S: … · T: … · O: … · P: … |
| Entsorgung | [Sammelbehälter, Neutralisation] |
| Notfall | [Augendusche, Erste Hilfe, NOT-AUS] |
| Vorversuch | [Datum, Ergebnis] – ausstehend |

Freigabe: ausstehend

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: RiSU (aktuelle Fassung), Sicherheitsdatenblätter, Vorversuch

## Übergabe

- Frage, Erwartungswerte, Gefährdungsbeurteilung (Entwurf) – Freigabe durch die Lehrkraft
- Empfohlen: `material-pruefen` (P, Sicherheit)

> KI-gestützt erstellt (Skill experiment-planen v1.4). Fachliche Prüfung und Verantwortung: Lehrkraft.
