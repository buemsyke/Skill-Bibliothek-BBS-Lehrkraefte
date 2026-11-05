---
name: experiment-planen
description: Plant Experimente und Schülerversuche für berufsbildende Schulen und das Berufliche Gymnasium – Fragestellung und Hypothese, Variablen, Material und Aufbau, Durchführung, Messwerttabelle mit Einheiten, Auswertung und Fehlerbetrachtung mit Messunsicherheit – als Versuchsanleitung für Lernende, Lehrerfassung mit erwarteten Messwerten und Entwurf der Gefährdungsbeurteilung (Ersatzstoffprüfung, Maßnahmen nach STOP, Entsorgung, Notfall). Prüft per Skript Vollständigkeit, Gefahrenhinweise, Freigabezeile und Messwerte gegen physikalische Grenzen (Faraday, Wirkungsgrad, Einheiten). Ersetzt weder Gefährdungsbeurteilung noch Vorversuch der Lehrkraft und gibt keinen Versuch frei. Verwenden bei „Versuch planen", „Experiment zur Lernsituation", „Versuchsanleitung", „Messprotokoll", „Schülerversuch Elektrolyse", „Wirkungsgrad messen", „Gefährdungsbeurteilung für den Versuch". Nicht für reine Simulationen am Rechner.
metadata:
  version: "1.5"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Experiment planen

## Zweck
Ein Versuch, der eine echte Frage der Lernsituation beantwortet, sicher durchführbar ist und
Messwerte liefert, die zur Physik passen. Die Rahmenrichtlinien des Beruflichen Gymnasiums
zählen das Experimentieren und das Formulieren und Prüfen von Hypothesen zu den übergeordneten
Kompetenzen. In der Berufsausbildung stehen Messungen und Inbetriebnahmen ohnehin im Zentrum.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

**Sicherheit vor Didaktik:** Der Skill liefert einen **Entwurf** der Gefährdungsbeurteilung. Die
Lehrkraft prüft ihn gegen die aktuelle RiSU und die Landesregeln, macht den Vorversuch und setzt
die Freigabezeile. Ohne `Freigabe: erteilt – KÜRZEL, Datum` geht die Anleitung nicht an Lernende
(Gate GE im Orchestrator). Erwartungswerte ohne Vorversuch tragen den Vermerk *Erwartung aus
Rechnung*.

## Drei Modi

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Neuer Versuch** | „Schülerversuch zur Elektrolyse für die Wasserstoff-LS" | Versuchsanleitung + Lehrerfassung + Gefährdungsbeurteilung (Entwurf) |
| **B Überarbeiten** | „Mach aus unserem Elektrolyse-Blatt einen sicheren, offenen Versuch" | überarbeitete Anleitung mit Änderungsliste |
| **C Plausibilisieren** | „Stimmen die Messwerte im Erwartungshorizont?" | Prüfung mit `messwerte_pruefen.py`, Befunde und korrigierte Erwartungswerte |

## Eingaben
- **Pflicht (sonst Rückfrage):** Fragestellung oder Bezug (Lernsituation, Phase, Kompetenz).
- **Wichtig, sonst Annahme:** vorhandene Geräte und Stoffe, Lehrer- oder Schülerversuch,
  Gruppengröße, Zeit, Vorwissen, Raum (Fachraum mit Abzug? Experimentiertische mit
  Sicherheitsbuchsen?).
- **Optional:** vorhandene Anleitung, Herstellerunterlagen der Geräte, Sicherheitsdatenblätter.

## Vorgehen (Modus A)
1. **Frage aus der Lernsituation:** Was soll der Versuch für die Handlungssituation klären?
   (Beispiel: „Wie viel der eingesetzten elektrischen Energie steckt am Ende im Wasserstoff?“)
2. **Hypothese und Variablen** (`references/experimentdidaktik.md`): Vorhersage mit Begründung;
   unabhängige, abhängige und konstant gehaltene Variable; mindestens eine Wahl liegt bei den
   Lernenden (Öffnungsgrad passend zum Niveau).
3. **Ersatzstoff- und Ersatzverfahrensprüfung zuerst** (`references/experimentsicherheit.md`):
   geringste Gefährdung, kleinste Mengen, Schutzkleinspannung.
4. **Anleitung schreiben** nach `assets/vorlage-versuchsanleitung.md` und
   `references/schuelermaterial.md` – kurz, mit Skizze und Diagramm: Material, **Aufbau als
   beschriftete Skizze** (SVG mit `fachdiagramm-erstellen`, Schaltung mit `technologieschema-erstellen` bzw. `circuitjs-schaltung-erstellen`
   oder als `ABBILDUNG:`-Platzhalter; nie als Zeichnung aus Zeichen),
   **Durchführung nach Öffnungsgrad** – im Regelfall *angeleitet*: Vorgegeben sind nur die
   Sicherheitsschritte (Spannung, Stoffe, Mengen, Prüfung des Aufbaus durch die Lehrkraft), die
   Messreihe planen die Lernenden; *geschlossen* mit kurzen Schritten nur mit Begründung in den
   Didaktischen Hinweisen. Messwerttabelle mit Einheiten im Tabellenkopf, **Auswertung mit
   Diagramm** (Achsen mit Größe und Einheit; im Lehrerteil als SVG aus den Erwartungswerten per Code), Fehlerbetrachtung, Rückbindungsfrage an die
   Anlage. Prüfvermerke (`🔎`) und Hinweise für die Lehrkraft stehen im Lehrerteil, nicht in der
   Anleitung.
5. **Erwartungswerte rechnen**, nicht schätzen: physikalische Grenze mit
   `python3 scripts/messwerte_pruefen.py faraday|kette|wirkungsgrad|unsicherheit …`; Werte als
   *Erwartung aus Rechnung* kennzeichnen, bis der Vorversuch sie ersetzt.
6. **Gefährdungsbeurteilung (Entwurf)**: Stoffe mit Menge und Gefahrenhinweisen 🔎 (aus dem
   Sicherheitsdatenblatt, nicht aus dem Gedächtnis), Gefährdungen, Maßnahmen nach STOP,
   Entsorgung, Notfall, Vorversuch, Freigabezeile `Freigabe: ausstehend`.
7. **Prüfen:** `python3 scripts/versuch_pruefen.py 41_experiment_….md` und
   `python3 scripts/schuelermaterial_pruefen.py 41_experiment_….md` (Länge, vorgegebene
   Schritte, Skizze und Diagramm, Prüfvermerke im Teil für Lernende) – alle ❌ beheben, jedes ⚠
   behandeln oder begründen.

**Modus C:** Angaben aus Anleitung oder Erwartungshorizont mit `messwerte_pruefen.py` prüfen
(Faraday-Grenze, Energieerhaltung, Rückrechnung einer Wirkungsgradkette durch Division,
Einheiten von Stoffwerten); Befunde wie in `material-pruefen`.

## Ausgabe
Datei `41_experiment_<kurztitel>.md`:
- Schülerfassung (Anleitung, Messwerttabelle, Auswertungsauftrag)
- `# Lösungen und Erwartungshorizont` (Erwartungswerte mit Rechnung)
- `# Didaktische Hinweise` mit der Gefährdungsbeurteilung (Entwurf), Vorversuch und Freigabezeile
- Pflichtabschnitte

## Qualitätscheck
- [ ] Frage und Hypothese aus der Lernsituation; Rückbindungsfrage an die Anlage?
- [ ] Variablen benannt, mindestens eine Entscheidung bei den Lernenden?
- [ ] Ersatzstoffe geprüft; Gefährdungsbeurteilung mit STOP-Maßnahmen, Entsorgung, Notfall?
- [ ] Erwartungswerte gerechnet und unter der physikalischen Grenze; als Erwartung gekennzeichnet?
- [ ] Messwerttabelle mit Einheiten; Auswertung mit Fehlerbetrachtung?
- [ ] `Freigabe: ausstehend` gesetzt – keine Freigabe durch die KI?
- [ ] Anleitung kurz, Aufbau als Skizze, Auswertung mit Diagramm, nur Sicherheitsschritte
      vorgegeben (sonst Öffnungsgrad begründet), keine Prüfvermerke im Teil für Lernende?
- [ ] `versuch_pruefen.py` und `schuelermaterial_pruefen.py` ohne ❌?

## Beispielaufrufe
> „Plane zur LS ING3.1 einen Schülerversuch: Wie viel Wasserstoff erzeugt eine kleine
> Elektrolysezelle je Wattstunde? Geräte: Netzgerät 0–12 V, zwei Multimeter, Hofmann-Apparat."

> „Prüf die Messwerte im Erwartungshorizont: 150 mA, 60 s, 3 ml Wasserstoff."

## Referenzen – wann lesen
- `assets/vorlage-versuchsanleitung.md` – **immer** (Ausgabeformat, vom Skript gelesen).
- `references/experimentsicherheit.md` – **immer** (Ablauf, Gefährdungsbeurteilung, typische Gefahren, Grenzen).
- `references/experimentdidaktik.md` – Hypothese, Variablen, Öffnungsgrad, Auswertung, Messunsicherheit.
- `references/berufliches-gymnasium.md` – BG: übergeordnete Kompetenzen, Fach Praxis.
- `references/operatoren-afb.md` – Aufträge und Anforderungsbereiche.
- `references/schuelermaterial.md` – Anleitung für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/versuch_pruefen.py` (liest auch DOCX/PDF über `scripts/text_lesen.py`) – Vollständigkeit, Gefahrenhinweise, Freigabezeile.
- `scripts/messwerte_pruefen.py` – Faraday, Wirkungsgrad, Kette, Einheit, Unsicherheit.
- `scripts/schuelermaterial_pruefen.py` – Form der Anleitung (Länge, Schritte, Darstellungen).
