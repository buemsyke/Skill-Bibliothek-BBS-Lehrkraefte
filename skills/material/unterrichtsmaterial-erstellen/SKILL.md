---
name: unterrichtsmaterial-erstellen
description: Erstellt einsatzfertiges Unterrichtsmaterial für berufsbildende Schulen als Markdown – Arbeitsblätter mit handlungsorientierten Aufträgen, Infotexte, Situationsmaterial (Kundenauftrag, Störmeldung, Lastenheft), Vorlagen (Arbeitsplan, Prüfprotokoll, Projektplan), Übungsaufgaben, Tafelbild, Befundkarten, Entscheidungsmatrix, Rollenkarten, Peer-Feedback, Kannliste, Reflexionsauftrag, Bewertungsraster und Lehrerhandreichung – mit Schüler- und Lehrerfassung und vollständigem Erwartungshorizont, für Lernende kurz und anschaulich. Rechnet Zahlenwerte nach und erfindet keine Quellen. Verwenden, wenn zu einer Lernsituation, einem Projekt, einem Entwurf oder einem Thema ein Arbeitsblatt, ein Infoblatt, eine Lösung, ein Erwartungshorizont oder ein Materialpaket benötigt wird. Vorhandenes Material sprachsensibel überarbeiten (sprachsensibel-ueberarbeiten) oder differenzieren (differenzierung-erstellen) leisten eigene Skills.
metadata:
  version: "1.14"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Unterrichtsmaterial erstellen

## Zweck
Material liefern, das **im Unterricht sofort funktioniert**: klarer Auftrag, passendes Niveau,
geprüfte Fachinhalte, Lösung für die Lehrkraft – und erkennbar im Dienst der Handlung. Was
Lernende in die Hand bekommen, ist **kurz, offen gestellt, anschaulich und ohne Dekoration**
(`references/schuelermaterial.md`).

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht (sonst Rückfrage):** Thema **oder** Bezug (Lernsituation/Entwurf) und gewünschte
  Materialart(en) – fehlt die Art, wird sie aus dem Bezug abgeleitet (Standard: Arbeitsblatt +
  Erwartungshorizont).
- **Wichtig, sonst Annahme:** Lerngruppe/Niveau (DQR), Phase der vollständigen Handlung,
  Bearbeitungszeit, Sozialform, verfügbare Hilfsmittel (Tabellenbuch, Datenblätter, PC).
- **Optional:** Lernsituation, Unterrichtsentwurf, Ordnungsmittel, Herstellerunterlagen,
  vorhandenes Material zum Überarbeiten, Layoutvorgaben der Schule.

## Materialarten (Details und Bauschemata: `references/materialtypen.md`)

| Art | Didaktische Funktion | typische Phase |
|---|---|---|
| Situationsmaterial (Auftrag, Störmeldung, E-Mail, Kundengespräch, KI-Auskunft der Kundschaft) | Problem öffnen, Kontext geben | Informieren |
| Informationstext / Infoblatt | Fachwissen bereitstellen | Informieren, Planen |
| Arbeitsblatt mit Arbeitsaufträgen (ggf. Stolperstein-Kasten) | Handlung anleiten, Ergebnis erzeugen | alle |
| Vorlage Arbeitsplan / Prüfprotokoll / Checkliste / Betriebsdokument | Planung und Dokumentation strukturieren | Planen, Durchführen, Überprüfen |
| Prüfplan und Befundkarten | Diagnose selbst planen; Befunde nur zu geplanten Schritten | Planen |
| Entscheidungsmatrix mit Kosteninfo | Alternativen nach Kriterien abwägen, Zielkonflikt lösen | Entscheiden |
| Übungsaufgaben mit Lösungsweg | Verfahren festigen | Durchführen, Üben |
| Tafelbild / Strukturbild | Ergebnis sichern | Sicherung |
| Glossar / Wortspeicher (ggf. mit Kundensprache) | Fachsprache sichern; für ganze Texte und Sprachhilfen je Operator `sprachsensibel-ueberarbeiten` | alle |
| Rollenkarten für Gesprächssimulation | Beratung, Einwände, Einweisung üben | Überprüfen, Durchführen |
| Bewertungsraster / Beobachtungsbogen | Kriterien offenlegen, bewerten | Entscheiden, Überprüfen |
| Peer-Feedback-Bogen | Ergebnis nach Kriterien prüfen, danach überarbeiten | Überprüfen |
| Kompetenzraster / Kannliste | Selbsteinschätzung am Anfang und am Ende | Informieren, Reflektieren |
| Reflexionsauftrag | Vorgehen auswerten, auf neue Lage übertragen | Reflektieren |
| Lehrerhandreichung zur Lernsituation | Einsatz vorbereiten: Überblick, Begründungen, Stolpersteine | vor der Lernsituation |
| Lastenheft (Auftraggeber) und Pflichtenheft-Vorlage | Projekt öffnen: Ziele und Randbedingungen statt Lösung; Antwort der Lernenden | Informieren, Planen |
| Projektplan mit Meilensteinen | Arbeitspakete, Verantwortliche, Termine, Meilenstein-Gespräche | Planen, Entscheiden |
| Projektjournal | Vorgehen, Entscheidungen, eigener Anteil dokumentieren (Grundlage Einzelanteil) | Durchführen, Reflektieren |
| Quellenmappe | Quellen mit Typ und Interessenlage, Kernaussage, Gegenquelle | Informieren, Überprüfen |
| Lektion im Kursprojekt (`lessons/NN_slug/lesson.md`) | Schülerseite einer Lernsituation (eine oder mehrere Lektionen, der Handlungskreis wird je Lernsituation geschlossen), Lehrerteil in derselben Datei | alle |

Jede Phase der Lernsituation bekommt Material, auch Entscheiden, Überprüfen und Reflektieren –
nicht nur ein Raster. Didaktische Muster dazu: `references/lernsituationsmuster.md`.

**Lektion im Kursprojekt** (neu oder Überarbeitung vorhandener Lektionen): Aufbau und Elemente
nach `references/lektionsmuster.md` (Vor dem Start, Vorhersage, Zugänge, Bewertung und KI-Zeichen
vor der ersten Aufgabe, Entscheiden mit eigenem Kriterium, Realitätstest, Rückmeldung, Lernweg,
Stolperstein-Tabelle, verdeckte Schwierigkeit nur im Lehrerteil), Vorlage
`references/vorlage-lektion.md`. Schülerteil **kurz** halten (≤ ~1 500 Wörter ohne Code, Kernweg
≤ 60–65 min je 90 min, Zeitplanung vollständig). Mehrere Lektionen zu *einer* Lernsituation
bündeln (Bewertung, KI, Entscheiden, Realitätstest, Lernweg einmal je Lernsituation); wo
Selbststudium teuer ist, einen begründeten **Lehrkraftinput mit Lösungsbeispiel** einplanen
(`references/lernsituationsmuster.md` Abschn. 12) und keinen Lösungscode ins Fachwissen
schreiben. Vorher und nachher
`python3 scripts/lektion_pruefen.py lessons/*/lesson.md [--loesungen solutions]` – meldet fehlende
Elemente, Punktsummen, Zeitplanung und Wortzahl. Veröffentlichen mit `schuelerseiten-veroeffentlichen`.

Klassenarbeiten und Lernzielkontrollen erstellt `klausur-erstellen`.
Quiz für Moodle/H5P gehört
zu `quizfragen-erstellen`, falls installiert; sonst einfache Fassung hier erstellen. Eigene Skills
gibt es für Versuchsanleitungen mit Gefährdungsbeurteilung (`experiment-planen`),
Programmieraufgaben mit Codeprüfung (`programmieraufgabe-erstellen`) und Technikfolgenabschätzung
mit Quellenmappe und Rollenkarten (`technikfolgen-abschaetzen`) – falls installiert; sonst einfache
Fassung hier nach `references/materialtypen.md` Abschn. 16–19.

**Vollständiger Materialsatz** (nach `bbs-didaktik`): Zu jedem Arbeitsblatt
gehört ein Erwartungshorizont (Lehrerfassung); wird die Stunde geplant, ein Verlaufsplan
(`unterrichtsentwurf-erstellen`, Typ K); zu einer Lernsituation mit mehreren Materialien eine
Lehrerhandreichung. In der Materialübersicht ausweisen, was vorliegt und was fehlt.

## Vorgehen

1. **Funktion klären.** Für jedes Material: Welche Phase, welches Teilziel, welcher Beitrag
   zum Handlungsergebnis? Material ohne Funktion entfällt.
2. **Fachinhalt sichern.** Fakten, Werte, Normbezüge aus gelieferten Unterlagen; sonst
   allgemeines Fachwissen mit `🔎`. **Jede Rechnung tatsächlich nachrechnen** (mit Code, wenn
   verfügbar), Einheiten mitführen, Rundung angeben.
3. **Schülerfassung schreiben** nach `assets/vorlage-arbeitsblatt.md` und
   `references/schuelermaterial.md`: Bezug zur Handlungssituation in höchstens drei Sätzen
   (besser Situationsmaterial mit Bild) → **wenige, offene Aufträge** mit **Operator**,
   Ergebnisform, Sozialform, Zeit und Erfolgskriterium („Sie sind fertig, wenn …") – ein bis
   zwei Sätze, höchstens drei Teilaufgaben, kein vorgegebener Lösungsweg (Schritte gehören in
   gestufte Hilfen) → Darstellung, mit der der Auftrag arbeitet. Pro Auftrag ein Operator;
   Aufgaben über die Taxonomiestufen streuen; kein Blatt nur mit AFB I, kein erster Auftrag auf
   AFB III; Gestaltungsprinzipien beachten (`references/gestaltungsprinzipien.md`). Keine
   Dekoration, keine Ankündigungen, kein Text, den kein Auftrag braucht.
   **Übungsdichte:** Wo eine Routine aufgebaut wird, erst ein gelöstes Beispiel, dann genügend
   gleichartige Aufgaben (leicht → fordernd), dann eine eingekleidete Aufgabe – lieber eine
   Seite mehr Übung als ein „Anreißblatt". Punkte gehören in Leistungsüberprüfungen, nicht in
   die Schülerfassung von Übungsmaterial; am Blattende optional ein Selbstcheck. Bei Rechen-
   und Verfahrensaufträgen einen **Stolperstein-Kasten** mit Kontrollwert und Diagnosehinweis
   aus den Lernhürden der Lernsituation; bei Diagnoseaufgaben nennt kein Auftrag die Ursache.
4. **Mit Darstellungen arbeiten, nie erfinden.** Jedes Arbeitsblatt und Infoblatt trägt
   mindestens eine Darstellung, mit der Aufträge arbeiten (ablesen, ergänzen, Fehler finden,
   selbst zeichnen – `references/schuelermaterial.md` Abschn. 2). Selbst erstellen, was sich
   erstellen lässt: Tabelle, Matrix, Kennlinie aus gerechneten Werten (Code, als SVG);
   Blockschaltbilder, Abläufe, Strukturbilder, Struktogramme und Datenmodelle mit `fachdiagramm-erstellen`, Anlagenbilder zu Steuerungsaufgaben (Technologieschemata), GRAFCET und Funktionspläne mit `technologieschema-erstellen`.
   Jede Zeichnung als SVG aus einer Spec – nie als Zeichnung aus Zeichen oder Mermaid, auch nicht
   in Lösungen und Tafelbild.
   Fotos, Herstellerzeichnungen und Normauszüge nie erfinden: Platzhalter
   `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz – z. B. eigenes Foto Fachraum]` direkt am Auftrag
   (bleibt als Prüfauftrag stehen). Keine Schmuckbilder.
5. **Lehrerfassung schreiben** unter den Überschriften `# Lösungen und Erwartungshorizont`
   und `# Didaktische Hinweise` (genau so – damit `schuelerseiten-veroeffentlichen` mit `edu-seiten strip` die
   Schülerfassung automatisch erzeugen): vollständige Lösung bzw. Erwartungshorizont mit
   Punkten je Aspekt, typische Fehler, Hinweise zum Einsatz, Differenzierungsideen.
6. **Bewertungsraster**, wenn ein Handlungsergebnis bewertet wird: Kriterien aus den
   Kompetenzen, beobachtbare Indikatoren, Stufen, Gewichtung (`assets/vorlage-bewertungsraster.md`).
   **Lehrerhandreichung**, wenn mehrere Materialien eine Lernsituation tragen: Aufbau nach
   `references/materialtypen.md` Abschn. 9 – nennt die Leitidee der Lernsituation
   (`references/didaktische-leitidee.md`), erklärt Entscheidungen, wiederholt keine Lösungen und
   keinen Stundenverlauf.
   **Material für Entscheiden, Überprüfen und Reflektieren** nach `references/materialtypen.md`
   Abschn. 10–15: Entscheidungsmatrix (Pakete gegen Budget nachrechnen), Rollenkarten mit
   Beobachtungsbogen Gespräch und Peer-Feedback-Bogen (`assets/vorlage-bewertungsraster.md`
   Teil C und D), Kannliste bzw. Kompetenzraster, Reflexionsauftrag mit Transfer- und
   Selbstbezugsfrage.
7. **Prüfen** gegen Checkliste und mit
   `python3 scripts/schuelermaterial_pruefen.py 40_material_….md` (Fließtext, Aufträge,
   Teilaufgaben, Schrittfolgen, Darstellungen, Dekoration, Lehrerangaben); ❌ beheben, ⚠
   behandeln oder im Qualitätscheck begründen.

## Ausgabe
Je Material eine Datei `40_material_<art>-<nr>_<kurztitel>.md`, Kopf nach Skill-Vertrag.
Aufbau: Schülerfassung (H1) → `# Lösungen und Erwartungshorizont` → `# Didaktische Hinweise`
→ Pflichtabschnitte. Bei mehr als zwei Materialien zusätzlich `40_materialuebersicht.md`
(Tabelle: Nr. | Material | Phase | Funktion | Zeit | Datei | Erwartungshorizont | Verlaufsplan)
und ggf. `40_handreichung_<kurztitel>.md`.
Weiterverarbeitung: `pandoc DATEI.md -o DATEI.docx` (Word) – oder Layout-Skills wie
`bbs2-arbeitsblatt`/`a4-druck-build`, falls installiert.

## Qualitätscheck
- [ ] Jedes Material hat eine benannte Funktion für Stundenziel bzw. Handlungsergebnis?
- [ ] Aufträge mit Operator, Ergebnisform, Sozialform, Zeit und Erfolgskriterium?
- [ ] Erwartungshorizont vollständig, mit Punkten, passend zu den Operatoren?
- [ ] Alle Zahlen nachgerechnet, Einheiten konsistent, Lösung und Aufgabe widerspruchsfrei?
- [ ] Keine erfundenen Quellen, Normnummern, Bilder oder Links; Platzhalter klar markiert?
- [ ] Schüler- und Lehrerteil sauber getrennt (keine Lösung im Schülerteil)?
- [ ] Sprache der Lerngruppe angemessen (kurze Sätze, Fachbegriffe eingeführt)?
- [ ] Teil für Lernende kurz (Wortzahl ≤ Richtwert), Aufträge offen statt kleinschrittig, Darstellungen als Arbeitsgegenstand, keine Dekoration – `schuelermaterial_pruefen.py` ohne ❌, Wortzahl genannt?
- [ ] Genug gleichartige Übung bei Routinen; Niveau passend zur Schulform?
- [ ] Materialsatz vollständig (Erwartungshorizont je Blatt; Handreichung bei mehreren Materialien)?
- [ ] Material für jede Phase, auch Entscheiden, Überprüfen (mit Überarbeitung) und Reflektieren?
- [ ] Befundkarten und Aufträge verraten die Ursache nicht; Matrix-Pakete und Summen nachgerechnet?
- [ ] Fiktive Firmen/Personen erkennbar fiktiv, keine realen Kontaktdaten (auch im Lastenheft), keine Platzhalter für die Lehrkraft im Schülermaterial?
- [ ] Quellen nach Typ und Interessenlage gekennzeichnet (`references/quellenbewertung.md`)?
- [ ] Lektion im Kursprojekt: `lektion_pruefen.py` ohne ❌, Bewertungssumme gleich Feinraster, Wortzahl vorher/nachher genannt, Kernweg und Zeitplanung ausgewiesen, Handlungskreis je Lernsituation geschlossen?

## Beispielaufrufe
> „Erstelle zur Phase Planen aus `20_lernsituation_gurtfoerderer.md` ein Arbeitsblatt, eine
> Vorlage für den Wartungsplan und ein Bewertungsraster für den Arbeitsplan."

> „Infoblatt Schmierstoffe (Öle/Fette, Auswahlkriterien) für Industriemechaniker 1. Jahr,
> max. eine Seite, dazu 5 Übungsaufgaben mit Lösung."

## Referenzen – wann lesen
- `assets/vorlage-arbeitsblatt.md` – Standardaufbau Schüler-/Lehrerfassung.
- `assets/vorlage-bewertungsraster.md` – Raster, Beobachtungsbogen, Gesprächsbogen, Peer-Feedback.
- `references/materialtypen.md` – Bauschemata und Beispiele für alle Materialarten, inkl. Lehrerhandreichung.
- `references/lernsituationsmuster.md` – Diagnose-Lernsituation, Entscheiden, Überprüfen,
  Reflektieren, Lernhürden, Projekt mit Lastenheft: wofür das Material der Abschn. 10–19 gebraucht wird.
- `references/quellenbewertung.md` – Quellenmappe, Quellentypen (Abschn. 19).
- `references/schuelermaterial.md` – **immer**: Material für Lernende kurz, offen gestellt, anschaulich, ohne Dekoration (Richtwerte, Beispiele, Rückwärtsprobe).
- `references/gestaltungsprinzipien.md` – Lernwirksamkeit, Übungsdichte, Schulform-Spektrum, Lesbarkeit, Urheberrecht.
- `references/operatoren-afb.md` – Operatoren und AFB.
- `references/schucu-bbs-2024.md` – Phasen der vollständigen Handlung.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
- `references/lektionsmuster.md`, `references/vorlage-lektion.md` – Lektion im Kursprojekt erstellen oder überarbeiten.
- `references/ki-vereinbarungen.md` – Zeichen 🚫 💡 🔧 am Arbeitsschritt von Arbeitsblatt und Lektion, Begründung der Phasen ohne KI.
- `scripts/lektion_pruefen.py` – Lektionen gegen das Lektionsmuster prüfen (Signalwörter, Summen, Zeit, Länge).
- `scripts/schuelermaterial_pruefen.py` – jedes Material für Lernende: Kürze, offene Aufträge, Darstellungen, Dekoration.
