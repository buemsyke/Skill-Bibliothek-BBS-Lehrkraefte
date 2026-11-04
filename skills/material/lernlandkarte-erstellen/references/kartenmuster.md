# Kartenmuster – welche Lernlandkarte für welchen Zweck

Eine Lernlandkarte macht den **Lernweg sichtbar**: Wo stehe ich, was ist das Ziel, welche
Schritte führen dorthin, wo finde ich Hilfe? Sie ersetzt nicht die Lernsituation, sondern
spielt sie für die Lernenden aus. Fünf bewährte Muster:

| Muster | Zweck | Format | Pfade | typische Quelle |
|---|---|---|---|---|
| **A Lernlandkarte zur LS** | selbstorganisiertes Arbeiten an einer Lernsituation (Stationen, Lernposten) | `karte` | Start · Selbstdiagnose · 2–5 Lernposten · Ergebnis sichern · Rückblick | `20_lernsituation`, `40_material`, `60_differenzierung` |
| **B Stundenablauf** | eine Doppelstunde oder ein Projekttag als Zeitleiste | `zeitstrahl` | je Phase der vollständigen Handlung ein Pfad mit `showdate` | `30_unterrichtsentwurf` (Verlaufsplan) |
| **C Klausurvorbereitung** | Generalprobe: Selbstdiagnose nach Kompetenzen, Übungsstationen, Lernplan | `karte` | Übersicht · Selbstdiagnose · Stationen je Kompetenz · Übungsklausur · Lernplan | `70_klausur` (Bauplan, **nicht** die Aufgaben), Lernsituationen |
| **D Lernfeldübersicht** | Orientierung über ein Lernfeld | `pinnwand` | je Lernsituation ein Pfad: Situation, Ergebnis, Zeitraum, Material | Lernfeld-Auszug, Abdeckungsmatrix |
| **E Workshop / Fortbildung** | SOL-Workshop mit Lernposten, Logbuch und Marktplatz | `karte` | Willkommen · Selbstdiagnose · Werkzeugkasten · Lernposten · Marktplatz · Transfer | Fortbildungskonzept |

## Muster A – Lernlandkarte zur Lernsituation

Vorlage: `assets/vorlage-lernlandkarte.md`.

1. **Start** (ozeanblau): Leitkarte „Der Auftrag" angepinnt (`flags=16420`) mit
   Handlungssituation und Handlungsergebnis; Ablauf als `--`-Liste; Arbeitsweise.
2. **Selbstdiagnose** (türkis): Ich-kann-Sätze als Checkboxen (aus den Kompetenzen der LS,
   mit Operator), Abstimmung zur Selbsteinschätzung, **Empfehlungskarte** (welcher Lernposten
   bei welcher Lücke) – sonst bleibt die Diagnose folgenlos.
3. **Lernposten** (je eigene Farbe): Auftrag (Operator, Ergebnisform, Sozialform, Zeit,
   Erfolgskriterien) · Material (Datei-Adresse oder Link) · gestufte Hilfen als Spoiler
   (Impuls → Strategie → Teilschritt) · Selbstcheck (Quiz oder Checkliste; vierte Hilfestufe Kontrolle) · optional Lösung
   zum Aufdecken (`flags=262148`). Pflicht- und Wahlposten unterscheiden (Titel oder Farbe).
4. **Ergebnis sichern** (indigo): Anleitung fürs Logbuch, eine Musterkarte; Lernende legen
   eigene Karten an – nur mit Gruppenkürzel, ohne Namen.
5. **Rückblick** (lila): Abstimmung zur Zielerreichung, Ausblick.

Umfang: 3–6 Karten je Pfad, insgesamt meist 15–30 Karten. Ausgeklappt nur Orientierung und
Aufträge, alles Weitere eingeklappt.

## Muster B – Stundenablauf als Zeitstrahl

```markdown
---
title: "LF 3 – Doppelstunde 5: Steuerung prüfen"
theme: morgen
format: zeitstrahl
---

## 08:00 Informieren [showdate=2026-11-03 08:00:00] [color=tuerkis] [box_color=tuerkis]
### Einstieg [flags=0]
…

## 08:20 Planen [showdate=2026-11-03 08:20:00] [flags=640] [color=mintgruen] [box_color=mintgruen]
### Auftrag [flags=0]
…
```

- Je Phase ein Pfad, Titel mit Uhrzeit und Phase der vollständigen Handlung (Informieren bzw.
  Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw. Kontrollieren · Reflektieren).
- `showdate` = geplanter Beginn; `flags=640` sperrt den Pfad bis dahin (Lösungs- und
  Sicherungsphasen erst später sichtbar). **Datum mit der Lehrkraft abstimmen** – sonst
  `⚠️ Annahme:` und Hinweis im Begleitblatt, dass die Zeiten vor dem Import anzupassen sind.
- Countdown für Arbeitsphasen: `&&count: 900&&`.

## Muster C – Klausurvorbereitung (Generalprobe)

- **Selbstdiagnose je Kompetenz-Cluster** (A, B, C …) mit sicher/unsicher, Empfehlung:
  Pflichtstationen für alle, Wahlstationen nach Diagnose.
- **Stationen** mit Übungsaufgaben **im Stil** der Arbeit (gleiche Operatoren und AFB), nie mit
  den Aufgaben der Arbeit selbst.
- **Übungsklausur** mit Zeitvorgabe (Countdown) und Erwartungshorizont zum Aufdecken.
- **Lernplan** als Checkliste: was bis wann wiederholen.

## Muster D – Lernfeldübersicht

`format: pinnwand`; je Lernsituation ein Pfad mit Karten „Situation", „Ergebnis",
„Zeitraum" und „Material". Zukünftige Lernsituationen eingeklappt; abgeschlossene mit Link
zur Sicherung. Gut als Einstieg ins Schuljahr und für Distanzphasen.

## Muster E – Workshop / Fortbildung

Wie Muster A, ergänzt um einen **Werkzeugkasten** (immer offen), einen **Marktplatz** (bestes
Produkt je Lernposten) und **Transfer** (Plan für die eigene Praxis). Parallel arbeitende
Tandems legen eigene Logbuch-Karten an (Kürzel `T1 · MK`). Für die Moderation eine **getrennte
Regie-Map**, die nicht geteilt wird.

## Gestaltungsregeln (alle Muster)

- **Eine Karte, ein Gedanke** – lieber eine Karte mehr als eine überladene.
- **Farbe bedeutet etwas:** je Pfad eine Farbe, Karten in der Pfadfarbe (`box_color` = `color`);
  Bedeutungen über die ganze Map gleich halten (z. B. grün = Pflicht, bernstein = Wahl).
- **Helles Theme** für Beamer und Ausdruck (`tageslicht`, `morgen`, `kreide`).
- **Gleiche Ansprache** (du oder Sie nach Schulregel) auf allen Karten.
- **Sprachsensibel:** Operator vorn, kurze Sätze, Fachbegriffe mit Tooltip
  `[Begriff]{Erklärung}` statt sie zu umgehen.
- **Lösungen:** nur zur Selbstkontrolle von Übungen und nur zum Aufdecken; nie Lösungen zu
  Leistungsüberprüfungen; Lehrkraft-Hinweise gehören ins Begleitblatt, nicht in die Map.
- **Datenschutz:** keine Namen, Fotos oder Kontaktdaten von Lernenden; Logbücher mit
  Gruppenkürzeln; kein Kennwort in der Quelle.
- **Material verlinken, nicht abschreiben:** lange Texte als PDF hochladen und verlinken;
  in der Karte nur Auftrag und Kern.
