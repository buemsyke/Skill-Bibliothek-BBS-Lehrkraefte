<!-- Assistenten-Fassung des Skills 'unterrichtsmaterial-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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
   Blockschaltbilder, Abläufe, Strukturbilder, Struktogramme und Datenmodelle mit `fachdiagramm-erstellen`.
   Jede Zeichnung als SVG aus einer Spec – nie als Zeichnung aus Zeichen oder Mermaid, auch nicht
   in Lösungen und Tafelbild. Steuerungsaufgaben: Betriebsmittelkennzeichen immer mit Klasse und
   Unterklasse (-SJ1, -MA1, -MM1, -EA1), gleich in Funktionsbeschreibung, Technologieschema und
   Zuordnungsliste (DIN EN IEC 81346-2:2020).
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

# ANHÄNGE

## Anhang: assets/vorlage-arbeitsblatt.md

---
artefakt: Unterrichtsmaterial
materialart: Arbeitsblatt
titel: "[Kurztitel]"
skill: unterrichtsmaterial-erstellen
skill_version: "1.14"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[Lernfeld]"
lernsituation: "[Nr. und Titel]"
phase: "[Phase der vollständigen Handlung]"
dqr: 0
status: "KI-Entwurf – fachlich zu prüfen"
---

# Arbeitsblatt [Nr.]: [Titel]

**Lernsituation:** [Titel] · **Phase:** [z. B. Planen] · **Zeit:** [__ min] · **Sozialform:** [EA/PA/GA]
**Name:** ______________________ **Datum:** __________

<!-- Teil für Lernende nach references/schuelermaterial.md: kurz, offen gestellt, anschaulich,
     ohne Dekoration. Prüfen: python3 scripts/schuelermaterial_pruefen.py DATEI.md -->

## Ausgangslage

[Höchstens drei Sätze, die an die Handlungssituation anknüpfen: Was ist passiert, was wird von
Ihnen erwartet? Besser: Situationsmaterial – Störmeldung, Foto, Anlagenbild.]

## Arbeitsaufträge

*KI-Zeichen (nur wo Lernende KI nutzen könnten; ein Zeichen je Arbeitsschritt):*
🚫 Ohne KI · 💡 KI zum Verstehen · 🔧 Mit KI arbeiten – *Warum bei „Ohne KI": [ein Satz, der das Ziel nennt]*

**1.** [🚫|💡|🔧] **[Operator] [Gegenstand] [Ergebnisform, mit Bezug auf die Darstellung].** *(ca. __ min)*

[ABBILDUNG: Darstellung, mit der der Auftrag arbeitet – Skizze, Anlagenbild, Diagramm, Kennlinie
oder Tabelle; Inhalt, Zweck, Quelle/Lizenz, Alternativtext. Direkt am Auftrag.]

[Höchstens drei Teilaufgaben a)–c), je ein Operator – keine Schrittfolge, Zwischenschritte
gehören in die Hilfen. Bei 💡 und 🔧: wie KI genutzt werden darf – Werkzeug, Umfang, was nicht.]

**2.** […] …

**3.** […] …

> **Stolpersteine – darauf achten!** *(bei Rechen- und Verfahrensaufträgen; aus den Lernhürden)*
> - [typischer Fehler als Hinweis, ohne Lösung]
>
> **Selbstkontrolle:** [Kontrollwert bzw. Bereich] Wenn nicht: [was prüfen]

**Ergebnis:** [Form, z. B. ausgefüllte Vorlage Arbeitsplan, Skizze, Tabelle, Kurzvortrag 2 min]

**Sie sind fertig, wenn …**
- [Erfolgskriterium 1, prüfbar]
- [Erfolgskriterium 2]

**Selbstcheck** *(optional, einmal je Lernsituation)*

| Ich kann … | sicher | unsicher | muss ich üben |
|---|---|---|---|
| [Teilziel 1 in Schülersprache] | ☐ | ☐ | ☐ |
| [Teilziel 2] | ☐ | ☐ | ☐ |

## Material und Hilfen

- M1: [Material, z. B. Auszug Betriebsanleitung, S. x]
- M2: [Tabellenbuch, Abschnitt …]
- Hilfekarten: [Stufen 1–3 am Lehrertisch / im LMS]

<!-- Platz für Schülerantworten bei Druckfassung: Kasten oder Raster für Zeichnungen, sonst
     Linien oder Tabelle -->

---
_Erstellt mit KI-Unterstützung; fachlich geprüft von: [Lehrkraft]_

# Lösungen und Erwartungshorizont

| Aufgabe | Operator / AFB | Erwartete Leistung | Punkte |
|---|---|---|---|
| 1 | | [Aspekte; Rechenweg mit Einheiten] | |
| 2 | | | |
| Σ | | | |

**Typische Fehler und Fehlvorstellungen:** …

# Didaktische Hinweise

- **Einsatz:** [Ort im Verlauf, Vorbereitung, Zeitbedarf]
- **Differenzierung:** [Hilfekarten, Sprinteraufgabe, sprachliche Hilfen]
- **Form für Lernende:** [Wortzahl Fließtext, Darstellungen, Begründung, wo eine Darstellung fehlt oder Schritte vorgegeben sind]
- **Sicherung:** [wie das Ergebnis gesichert wird]
- **Bezug Bewertung:** [welche Kriterien des Rasters betroffen sind]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Aufgaben/Operatoren: … → `bloom-taxonomie` (Analyse)
- Sprachliche Hürden: … → `sprachsensibel-ueberarbeiten`
- Hilfebedarf: … → `differenzierung-erstellen`
- Prüfbedarf: … → `material-pruefen`

> KI-gestützt erstellt (Skill unterrichtsmaterial-erstellen v1.14). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: assets/vorlage-bewertungsraster.md

# Vorlage: Bewertungsraster und Beobachtungsbogen

## A. Bewertungsraster für ein Handlungsergebnis

**Handlungsergebnis:** [z. B. Arbeitsplan für die Wartung]
**Bezug:** Lernsituation [Nr.], Kompetenzen [FK x, PK y] · **Gewichtung in der LS:** [__ %]

| Kriterium (aus Kompetenz) | Indikator (beobachtbar) | 3 – vollständig | 2 – überwiegend | 1 – ansatzweise | 0 – nicht erkennbar | Gewicht |
|---|---|---|---|---|---|---|
| Fachliche Richtigkeit | Arbeitsschritte entsprechen den Herstellerangaben | alle Schritte korrekt, vollständig | 1 Schritt fehlt/fehlerhaft | mehrere Lücken | nicht vorhanden | ×2 |
| Sicherheit | Schutzmaßnahmen an der richtigen Stelle | … | … | … | … | ×2 |
| Logik/Reihenfolge | … | | | | | ×1 |
| Dokumentation/Form | … | | | | | ×1 |

**Punkte:** ___ / ___ · **Umrechnung:** [Notenschlüssel der Schule]
**Rückmeldung (lernförderlich):** Stärke: … · nächster Schritt: …

Regeln:
- Kriterien aus den **Kompetenzen der Lernsituation** ableiten, nicht aus Fleiß oder Form allein.
- Indikatoren so formulieren, dass zwei Lehrkräfte zum selben Ergebnis kämen.
- Raster **vor** der Bearbeitung offenlegen (SchuCu-BBS: „verbindliche und offengelegte Kriterien").
- Bei Hilfekarten festlegen, welche Stufen ohne Abzug genutzt werden dürfen.

## B. Beobachtungsbogen für die Durchführung

**Tandem/Gruppe:** [Kürzel] · **Datum:** ___ · **Beobachtung durch:** [Lehrkraft / Peer]

| Beobachtungsmerkmal | ++ | + | – | Bemerkung |
|---|---|---|---|---|
| setzt Schutzmaßnahmen vor Arbeitsbeginn um | | | | |
| arbeitet nach eigenem Plan, passt ihn begründet an | | | | |
| stimmt sich im Team ab, verteilt Aufgaben | | | | |
| dokumentiert während der Arbeit | | | | |
| … | | | | |

## C. Beobachtungsbogen für ein Gespräch (Beratung, Übergabe, Einweisung)

**Fachkraft:** ___ · **Kundenrolle / Beobachtung:** ___ · **Rollenkarte:** [Typ]

| Kriterium | gelungen | teilweise | noch nicht | Beobachtung (Stichwort) |
|---|---|---|---|---|
| Ursache bzw. Ergebnis richtig und **ohne Fachjargon** erklärt | | | | |
| Empfehlung begründet, Kosten bzw. Aufwand genannt | | | | |
| Einwände aufgegriffen und beantwortet | | | | |
| eingewiesen: [Sollwert, was bei Abweichung zu tun ist, Wartung] | | | | |
| Auftreten: hört zu, fragt nach, freundlich | | | | |

**Rückmeldung:** Stärke 1: … · Stärke 2: … · nächster Schritt: …

## D. Peer-Feedback zum Handlungsergebnis

**Geprüft von (Gruppe):** ___ · **Ergebnis von (Gruppe):** ___

| Prüffrage (aus dem Bewertungsraster) | ja | teilweise | nein | Fundstelle / Hinweis |
|---|---|---|---|---|
| Sind alle Abschnitte der Vorlage vorhanden? | | | | |
| Stimmen die Werte mit den Kontrollwerten überein? | | | | |
| Ist die Empfehlung mit Kriterien begründet? | | | | |
| [weitere Kriterien des Rasters als Frage] | | | | |

**Zwei Stärken:** 1. … 2. …
**Ein nächster Schritt:** … (konkret und machbar: „Ergänzen Sie …")

Regeln für das Feedback:
- Beschreiben Sie, was Sie im Ergebnis sehen – nicht die Person.
- Der nächste Schritt ist konkret und in der Überarbeitungszeit machbar.
- Wer Feedback erhält, hört zu und fragt höchstens nach; danach wird überarbeitet
  ([__] min, Änderungen markieren).

Hinweis Datenschutz: Bögen mit Namen nicht in KI-Werkzeuge hochladen; für Auswertungen mit KI
vorher pseudonymisieren.

## Anhang: references/didaktische-leitidee.md

# Didaktische Leitidee einer Stunde bzw. Lernsituation

Planungshilfe der Bibliothek (Entscheidung der Fachberatung, 19.10.2026), in eigenen Worten.
Die Leitlinie SchuCu-BBS 2024 kennt den Begriff nicht; die Leitidee **ergänzt** ihre Begriffe –
Handlungssituation, Handlungsergebnis, Fach- und Personale Kompetenz, sechs Phasen – und
**ersetzt keinen** davon. Sie ist kein zusätzliches Feld der Lernsituation, kein Kriterium des
Analysebogens und kein zweites Ziel.

## Inhalt
1. Was die Leitidee ist
2. Abgrenzung zu den Begriffen der Leitlinie
3. Zwei Ebenen und wo sie steht
4. Formulieren – Muster und Kriterien
5. Beispiele
6. Typische Fehler
7. Prüffragen vor und nach dem Unterricht

## 1. Was die Leitidee ist

Die didaktische Leitidee sagt in **ein bis zwei Sätzen**, worum es im Kern geht: welche
**übertragbare Einsicht**, Fertigkeit oder Haltung die Lernenden **am exemplarischen Fall**
gewinnen sollen und **warum** das für sie in Beruf bzw. Lebenswelt bedeutsam ist. Sie bündelt
die Analyse (Sachstruktur, Lernausgangslage, Bedeutsamkeit, Exemplarität) zu einer Richtung,
an der sich Auswahl und Reduktion, Phasierung, Arbeitsaufträge und Sicherung ausrichten.

## 2. Abgrenzung zu den Begriffen der Leitlinie

| Begriff | Frage | Beispiel LS 4.2 *Gurtförderer warten* |
|---|---|---|
| Thema | Worum geht es inhaltlich? | Wartung eines Gurtförderers |
| **Handlungssituation** (Leitlinie) | Vor welchem Problem stehen die Lernenden? | Wartung seit drei Monaten überfällig, höchstens zwei Stunden Stillstand, Plan muss freigegeben werden |
| **Didaktische Leitidee** (Bibliothek) | Was sollen die Lernenden an diesem Fall exemplarisch erfassen – und warum ist das bedeutsam? | Eine Anlage läuft nur sicher und zuverlässig weiter, wenn nach dem Plan des Herstellers gewartet wird statt nach Gefühl – Planung ist Teil der Arbeitssicherheit, nicht Papierkram. |
| **Fach- und Personale Kompetenz** (Leitlinie) bzw. Stundenziel | Was können die Lernenden am Ende nachweisbar? | erstellen einen Arbeitsplan …, indem …; stimmen Arbeitsteilung im Tandem ab, indem … |
| **Handlungsergebnis** (Leitlinie) | Was liegt am Ende vor? | Arbeitsplan, gewartete Anlage, Wartungsprotokoll, Übergabe mit Empfehlung |

Die Leitidee beschreibt die **Richtung**, die Kompetenzen bzw. das Stundenziel machen sie
**überprüfbar**, das Handlungsergebnis macht sie **sichtbar**.

## 3. Zwei Ebenen und wo sie steht

| Ebene | Reichweite | Ort in der Dokumentation |
|---|---|---|
| **Leitidee der Lernsituation** | trägt alle Phasen der vollständigen Handlung | Lernsituation: unter *Vereinbarungen und Hinweise zur Umsetzung → didaktisch-methodische Kommentare* (kein neues Feld); Entwurf Typ A: *Darstellung der Lernsituation*; Sequenz (Typ S): über der Sequenzübersicht; Lehrerhandreichung: Abschnitt 2 |
| **Leitidee der Stunde** | konkretisiert die Leitidee der Lernsituation für den Schritt dieser Stunde | Entwurf: unmittelbar vor dem Stundenziel; Reflexion: Zeile in der Zielerreichung |

Die Leitidee der Stunde widerspricht der der Lernsituation nicht; sie zeigt, welchen Teil davon
diese Stunde einlöst.

## 4. Formulieren – Muster und Kriterien

**Muster:**
> Am [Fall aus der Handlungssituation] erfassen die Lernenden, dass bzw. wie [übertragbare
> Einsicht] – bedeutsam, weil [Gegenwart bzw. Zukunft in Beruf oder Lebenswelt].

Ebenso möglich: ein bis zwei Sätze ohne Muster oder eine **Leitfrage** aus Sicht der Lernenden
(„Woran erkenne ich, ob die Anlage ohne Bedenken weiterlaufen kann?"), sofern Einsicht und
Bedeutsamkeit erkennbar bleiben.

**Fünf Kriterien:**
1. **verdichtet** – ein bis zwei Sätze, eine Idee;
2. **exemplarisch** – reicht über den Fall hinaus (auf andere Anlagen, Aufträge, Situationen);
3. **bedeutsam** – mit Bezug zu Beruf bzw. Lebenswelt jetzt oder später (knüpft an die
   Anforderungen 2, 3 und 5 der Leitlinie an die Handlungssituation an);
4. **stimmig** – passt zur Handlungssituation und wird durch Kompetenzen bzw. Stundenziel
   operationalisiert, ohne sie zu wiederholen;
5. **tragend** – Auswahl und Reduktion, Phasierung und Arbeitsaufträge lassen sich auf sie
   zurückführen; Sicherung oder Reflexion greift sie auf.

## 5. Beispiele

| Lernsituation bzw. Stunde | Leitidee |
|---|---|
| IM 1, LS 4.2, Stunde Planen *Arbeitsplan erstellen* | Ein Arbeitsplan ist die Voraussetzung für sicheres Arbeiten: Wer die Herstellerangaben in eine begründete Reihenfolge bringt und das Wiedereinschalten ausschließt, kann eine Anlage in knapper Zeit zuverlässig warten. |
| AM SHK 2, LS 7.1 *Luft aus einer Heizungsanlage beseitigen* | Luft in der Anlage ist ein Symptom: Wer Befunde systematisch vergleicht, findet die Ursache, statt nur zu entlüften – und kann der Kundin erklären, warum das Problem nicht wiederkommt. |
| BG Technik, ING3, Kickoff *Lastenheft analysieren* | Ein Lastenheft beschreibt, was der Auftraggeber braucht, nicht wie es gebaut wird – wer zuerst die richtigen Fragen stellt, vermeidet teure Fehlentwicklungen. |
| FI, LS 5.2 *Ticket-Tool entwickeln* | Software wird für Menschen gebaut: Erst wenn die Anforderungen des Supports als Testfälle feststehen, lässt sich zeigen, dass das Werkzeug zuverlässig hilft. |

## 6. Typische Fehler

| Fehler | Beispiel | Besser |
|---|---|---|
| Thema statt Leitidee | „Wartung von Gurtförderern" | Einsicht und Bedeutsamkeit benennen (Abschn. 5) |
| Ziel statt Leitidee | „Die SuS erstellen einen Arbeitsplan." | das ist das Stundenziel – die Leitidee sagt, *wofür* |
| zu allgemein | „Die SuS sollen selbstständig arbeiten." | an den Fall binden: was genau, warum gerade hier |
| zu viele Ideen | drei Sätze mit drei Schwerpunkten | eine Idee; Weiteres in die didaktischen Entscheidungen |
| steht nur im Entwurf | Leitidee formuliert, Sicherung greift sie nicht auf | in Sicherung oder Reflexion eine Frage dazu stellen |
| fremdes Kompetenzmodell | Leitidee als Kopf eines Rasters mit vier Kompetenzdimensionen | Kompetenzen bleiben Fach- und Personale Kompetenz (Leitlinie) |

## 7. Prüffragen vor und nach dem Unterricht

**Vor dem Unterricht** (Entwurf, Selbstcheck):
- Ist die Leitidee formuliert – und erfüllt sie die fünf Kriterien?
- Lässt sich jede Phase auf sie beziehen? Was im Verlauf trägt nichts zu ihr bei?
- Wo im Verlauf (Sicherung, Reflexion) wird sie für die Lernenden sichtbar?

**Nach dem Unterricht** (Reflexion):
- Woran ließ sich erkennen, dass die Lernenden die Leitidee erfasst haben – Äußerungen,
  Stundenergebnis, Transfer (Anzahlen, ohne Namen)?
- Hat die Leitidee die Stunde getragen, oder war sie zu groß bzw. zu klein für die Zeit?
- Was folgt für die Leitidee der nächsten Stunde?

## Anhang: references/gestaltungsprinzipien.md

# Gestaltungsprinzipien für lernwirksames Material

## 1. Kognitive Belastung steuern (Sweller; Mayer)

| Prinzip | Umsetzung |
|---|---|
| Kohärenz | Nur, was dem Ziel dient: keine Schmuckbilder, Emojis ohne Funktion, Floskeln oder Exkurse im Schülerteil; jeder Absatz wird von einem Auftrag gebraucht (`schuelermaterial.md` Abschn. 4). |
| Wort und Bild | Den Kern trägt eine Darstellung (Skizze, Diagramm, Tabelle), der Text erklärt sie – nicht umgekehrt; Aufträge arbeiten mit ihr (`schuelermaterial.md` Abschn. 2). |
| Signalisierung | Operator fett, Schlüsselbegriffe bei Einführung fett, klare Zwischenüberschriften. |
| Räumliche Nähe | Abbildung direkt neben dem Text, der sie erklärt; Beschriftungen in die Abbildung. |
| Segmentierung | Großes Handlungsergebnis in wenige Teilprodukte gliedern, je ein offener Auftrag mit Ergebnis; Einzelschritte nicht vorgeben, sondern als gestufte Hilfe anbieten. Eine Aufgabe = ein Kasten. |
| Lösungsbeispiele | Neues Verfahren erst an einem vollständig gelösten Beispiel zeigen, dann Schritte schrittweise weglassen (Fading). |
| Expertise-Umkehr | Für Fortgeschrittene Lösungsbeispiele und Hilfen reduzieren (→ Differenzierung). |

## 1a. Übungsdichte und Niveau der Schulform

- **Übungsdichte:** Tragfähige Grundlagen entstehen durch Wiederholung mit Erfolgserlebnis.
  Reine „Anreißblätter" mit drei Alibi-Aufgaben reichen nicht. Mehr Übung heißt mehr
  gleichartige, kurze Aufgaben – nicht mehr Text. Aufgaben folgen dem Ziel, nicht dem
  freien Platz auf der Seite.
- **Schulform-Spektrum** (Bezeichnungen je Land verschieden):

| Bildungsgang | Ausrichtung |
|---|---|
| einführend/grundbildend (BES, BVJ, Berufseinstieg) | stark sprach- und alltagssensibel, eng geführt über Lösungsbeispiele und gestufte Hilfen (nicht über zerlegte Aufträge), hoher Anschauungsgrad, viel Übung |
| Berufsfachschule, Berufsschule (dual) | ausgeprägter Praxis- und Betriebsbezug, Verzahnung von Theorie und Werkstatt/Betrieb |
| Fachoberschule, Berufliches Gymnasium, Fachschule | höheres Abstraktions- und Reflexionsniveau, mehr AFB III |

*Quelle der beiden Punkte: `bbs-didaktik`, Abschnitte Übungsdichte und Differenzierung.*

## 2. Lesbarkeit (Grundregeln, Vertiefung im Skill `sprachsensibel-ueberarbeiten`)
- Sätze mit meist unter 15 Wörtern; ein Gedanke pro Satz.
- Aktiv statt Passiv, Verben statt Nominalketten („Prüfen Sie die Spannung" statt „Die
  Durchführung der Spannungsprüfung ist vorzunehmen").
- Fachbegriffe beibehalten, aber einführen und im Glossar sichern.
- Zahlen mit Einheiten, Einheiten konsistent (mm, nicht gemischt mm/cm).
- Aufzählungen statt Schachtelsätze.

## 3. Handlungsorientierung sichtbar machen
- Jedes Blatt beginnt mit dem Bezug zur Handlungssituation – in höchstens drei Sätzen oder
  als Situationsmaterial mit Bild.
- Ergebnisse fließen in das Handlungsergebnis ein (Material „sammelt" sich zum Produkt).
- Erfolgskriterien vorab nennen; Selbstkontrolle ermöglichen (Lösung im LMS nach Abgabe,
  Checkliste).

## 4. Barrierearm
- Überschriftenhierarchie korrekt (für Vorlesefunktionen).
- Für jede Abbildung ein Alternativtext im Platzhalter.
- Information nie nur über Farbe codieren.
- Tabellen einfach halten (keine verbundenen Zellen in Markdown).

## 5. Rechtliches und Transparenz
- Eigene Formulierungen; keine längeren Passagen aus Fachbüchern oder Tabellenbüchern
  übernehmen. Fremdmaterial nur im Rahmen der Schranken für Unterricht (§ 60a UrhG) oder mit
  freier Lizenz (z. B. CC BY) – Quelle und Lizenz angeben. 🔎 Im Zweifel Schulleitung/
  Medienberatung fragen.
- Keine echten Firmenlogos, Personen oder Kontaktdaten in Situationsmaterial.
- KI-Unterstützung transparent machen (Fußzeile in der Schülerfassung nach Prüfung durch die
  Lehrkraft).

## 6. Sicherheit (Werkstatt, Labor)
- Sicherheitsrelevante Schritte im Material ausdrücklich nennen (Stillsetzen, gegen
  Wiedereinschalten sichern, PSA), nie als „bekannt" voraussetzen.
- Werte für Drücke, Spannungen, Drehmomente nur aus Hersteller- oder Normangaben; sonst
  `🔎 Wert prüfen`.

## Anhang: references/ki-vereinbarungen.md

# KI-Vereinbarungen auf drei Ebenen – Klasse, Unterricht, Aufgabe

Gemeinsame Referenz für `unterricht-entwickeln`, `unterrichtsentwurf-erstellen`,
`unterrichtsmaterial-erstellen`, `lernsituation-dokumentieren`, `schuelerseiten-veroeffentlichen`,
`lernsituation-analysieren` und `ki-chatbot-einrichten`. Sie beantwortet: **Wo legt die Lehrkraft
fest, ob und wie Lernende KI nutzen – und wie sagt sie es so, dass die Lernenden es verstehen?**

Herkunft: Praxisbericht einer BBS-Lehrkraft zu KI-Regeln auf drei Ebenen; die Ebenen greift ein
angekündigter Artikel in der Zeitschrift PÄDAGOGIK auf, Grundlage der Klassenregeln ist dort ein
KI-Leitfaden für Lehrende und Lernende (Angaben 🔎 ergänzen). In eigenen Worten gefasst und um
Voreinstellungen, Prüffragen und Planungsorte der Bibliothek ergänzt. Stand 1.33. Keine Vorgabe
der Leitlinie SchuCu-BBS 2024, sondern ergänzende Planungshilfe; Vorgaben der Schule und des
Landes zur KI-Nutzung gehen vor 🔎.

## Inhalt
1. Warum Klassenregeln allein nicht reichen
2. Drei Ebenen
3. Die drei Zeichen am Arbeitsschritt
4. Voreinstellung je Phase
5. Begründen und ansagen
6. Lockern: Lernende entscheiden mehr
7. Wo das in der Planung steht
8. Prüffragen
9. Formulierungshilfen
10. Ältere Fassung: die KI-Ampel

---

## 1. Warum Klassenregeln allein nicht reichen

Ein Beispiel aus dem Praxisbericht: Die Klassenregel lautet „KI darf das Lernen unterstützen“.
Eine Übungsphase ist bewusst ohne KI angelegt, weil die Lehrkraft sehen will, was die Lernenden
schon selbst können. Ein Schüler beruft sich auf die Regel – „Üben ist doch auch Lernen“ – und hat
aus seiner Sicht recht. Die Lehrkraft widerspricht scheinbar der eigenen Vereinbarung.

- **Ob KI hilft oder im Weg steht, hängt vom Ziel der Phase ab.** Dieses Ziel kennt zuerst nur die
  Lehrkraft.
- Ein Zusatz wie „außer die Lehrkraft sagt etwas anderes“ zeigt, *dass* es Ausnahmen gibt, nicht
  *warum* diese Phase eine ist.
- Also braucht es neben der Klassenregel Vereinbarungen und Hinweise, die zeigen, **wann und wie**
  KI konkret genutzt werden kann und soll – und das **Ziel** dahinter sichtbar machen.

## 2. Drei Ebenen

Klarheit entsteht, wenn alle drei Ebenen festgelegt sind und ineinandergreifen.

| Ebene | Was wird festgelegt | Wann und wo | Beispiel |
|---|---|---|---|
| **Klasse** | verbindlicher Rahmen: freigegebene KI-Werkzeuge, Datenschutz, Angabe der KI-Nutzung bei Abgaben, Grundsatz zur Lernunterstützung, Vorrang von Ansage und Zeichen | zu Beginn des Schuljahres bzw. der Lernsituation, mit der Klasse vereinbart; Regelseite oder Aushang | „Freigegeben sind … Personenbezogene Daten gehören nicht in KI-Werkzeuge. Bei Abgaben geben wir an, wofür wir KI genutzt haben.“ |
| **Unterricht** | KI-Einsatz **phasenweise**: welche Phase mit, welche bewusst ohne KI – mit kurzer Begründung | bei der Planung (Verlauf, Lektion); zu Beginn der Phase angesagt | Einstieg ohne KI · Erarbeitung mit KI für Recherche und Feedback · Übung ohne KI |
| **Aufgabe** | **Zeichen am Arbeitsschritt**, dazu im Auftrag, wie KI konkret genutzt werden darf | Arbeitsblatt, Lektion, Aufgabenkarte | siehe Abschn. 3 |

Bewährt für die Klassenebene sind **fünf Regeln** (Lektionsmuster): erst selbst versuchen ·
prüfen statt glauben · KI-Nutzung kennzeichnen · erklären können, was man übernimmt · Daten
schützen. Die Klassenregel sollte außerdem sagen, dass es ausgewiesene Phasen und Aufgaben ohne
KI gibt und dass **Ansage und Zeichen der Grundregel vorgehen** – sonst entsteht der Widerspruch
aus Abschn. 1.

## 3. Die drei Zeichen am Arbeitsschritt

Die Lernenden sehen auf einen Blick, ob und in welchem Umfang KI erlaubt ist. **Zeichen und Wort
gehören zusammen** (lesbar im Schwarzweißdruck, für Screenreader, unabhängig von der Farbe):
die Legende mit Wort steht auf derselben Seite (Blattkopf, Infokasten der Lektion), am
Arbeitsschritt genügt dann das Zeichen; wo die Aufgabe ohne Legende gelesen wird (Aufgabenkarte,
Einzelblatt), steht das Wort dabei.

| Zeichen | Wort | Bedeutung | typische Aufträge |
|---|---|---|---|
| 🚫 | **Ohne KI** | Der Arbeitsschritt wird ohne KI-Werkzeug bearbeitet. | Vorwissen und Vorhersage, Üben als Standortbestimmung, eigener Entwurf, Entscheidung und Begründung, Reflexion, Leistungsnachweis |
| 💡 | **KI zum Verstehen** | KI ist als Lernunterstützung erlaubt: Begriffe und Zusammenhänge erklären lassen, Verständnisfragen stellen. Das Ergebnis des Arbeitsschritts entsteht bei den Lernenden. | Erarbeiten neuer Begriffe, Nachfragen zu einem Fachtext, Beispiel erklären lassen |
| 🔧 | **Mit KI arbeiten** | Die Lernenden setzen KI im Auftrag für einen Teil der Arbeit ein – als Werkzeug beim Schreiben, für Recherche oder Feedback. Sie prüfen das Ergebnis, kennzeichnen es nach der Klassenregel und können erklären, was sie übernehmen. | Rohfassung einer Dokumentation überarbeiten lassen, Feedback zum eigenen Entwurf einholen, Quellen sammeln |

Regeln für den Gebrauch:
- **Wie** KI genutzt werden darf, steht zusätzlich im Arbeitsauftrag (Werkzeug, Umfang, was
  nicht). Das Zeichen sagt „ob und wie weit“, der Auftrag sagt „wie genau“.
- **Ein Zeichen je Arbeitsschritt**, wo sich die Schritte unterscheiden; ein Zeichen für das
  ganze Blatt nur, wenn es für alle Schritte gilt.
- **Wo Zeichen verwendet werden, trägt jeder Arbeitsschritt eines.** Ein fehlendes Zeichen lädt
  zur Rückfrage aus Abschn. 1 ein.
- Das Zeichen steht **vor dem Operator**: `**3.** 🚫 *Ohne KI* – Skizzieren Sie …`

Beispiel (Arbeitsblatt):

> **1.** 🚫 *Ohne KI* – Skizzieren Sie, welche Ursachen Sie für die Störung vermuten (5 min).
> **2.** 💡 *KI zum Verstehen* – Lassen Sie sich die Begriffe aus Ihrer Skizze erklären, die Sie
> nicht sicher kennen; notieren Sie je Begriff einen Satz in eigenen Worten.
> **3.** 🔧 *Mit KI arbeiten* – Lassen Sie sich Rückmeldung zu Ihrem Prüfplan geben (nur den
> Plan eingeben, keine Namen); entscheiden Sie, welche Hinweise Sie übernehmen, und halten Sie
> fest, welche nicht.

## 4. Voreinstellung je Phase

Voreinstellung für die **Unterrichtsebene**, keine Vorschrift: Wer abweicht, begründet es in
einem Satz (Abschn. 5). Sie folgt der Leitplanke der Bibliothek, dass **Entscheiden, Überprüfen und
Reflektieren Leistung der Lernenden bleiben**.

| Phase bzw. Element | Voreinstellung | Begründung (Ziel) |
|---|---|---|
| Einstieg, Vorwissen, Vorhersage | 🚫 | sichtbar machen, was schon da ist; eine Vorhersage wirkt nur, wenn sie vorher eigen war |
| Informieren, Erarbeiten | 💡; für Recherche 🔧 | Begriffe klären, Quellen finden – Quellen und Auskünfte danach prüfen |
| Planen | erster eigener Entwurf 🚫; danach 💡 oder 🔧 | der eigene Weg entsteht bei den Lernenden; KI prüft oder fragt nach, entwirft nicht vor |
| Entscheiden | 🚫 | Urteil und Begründung sind die Leistung dieser Phase |
| Durchführen, Üben | nach Ziel: Standortbestimmung 🚫 · Verstehen 💡 · Dokumentation, Text 🔧 | das Ziel der Übung bestimmt das Zeichen |
| Überprüfen (mit Überarbeitung) | 🚫; KI-Rückmeldung nur als zusätzliche Quelle (🔧), die die Lernenden selbst bewerten | die Überprüfung ist Leistung der Lernenden |
| Reflektieren | 🚫 | der eigene Lernweg lässt sich nicht auslagern |
| Leistungsnachweis | 🚫, sofern die Aufgabe nicht ausdrücklich etwas anderes vorsieht; Vorgaben der Schule gehen vor 🔎 | Nachweis der eigenen Leistung |

## 5. Begründen und ansagen

- **Eine kurze Begründung gehört zu jeder Phase ohne KI** – und zu jeder Abweichung von der
  Voreinstellung. Muster: *„Heute ohne KI, weil …“*. Mündlich zu Beginn der Phase, schriftlich
  am Blatt bzw. im Infokasten der Lektion.
- Die Begründung nennt das **Ziel**, nicht das Verbot:

| Ziel | Formulierung |
|---|---|
| Standortbestimmung | „Ich möchte sehen, was ihr schon selbst könnt – dann wissen wir, was ihr noch braucht.“ |
| eigenes Urteil | „Hier entsteht euer Urteil. Das kann euch kein Werkzeug abnehmen.“ |
| Automatisieren, Üben | „Was ihr selbst durchgeführt habt, steht euch in der Arbeit zur Verfügung.“ |
| Prüfungsnähe | „In der Klassenarbeit gibt es dieses Werkzeug auch nicht.“ |
| Zeit gewinnen | „Mit KI ist die Recherche in zehn Minuten erledigt – die Zeit brauchen wir für die Auswertung.“ |

- **Sinn der Regeln immer wieder thematisieren:** warum es sie gibt und warum eine Aufgabe mal
  ohne KI, mal mit KI zum Verstehen, mal mit KI als Werkzeug gedacht ist – zu Beginn, in der
  Reflexion (*Wo hat dir das Zeichen geholfen, wo hat es gestört?*) und bei der Rückfrage eines
  Lernenden. Regeln ohne verstandenen Sinn tragen nicht.
- In den Unterrichtsentwurf gehört die Begründung in die didaktisch-methodischen Entscheidungen
  und in die Lehrerhinweise (*KI-Einsatz in der Stunde*), nicht in den Schülertext.

## 6. Lockern: Lernende entscheiden mehr

Die Zeichen helfen besonders in Klassen, in denen sich Abläufe erst einspielen und selbstständiges
Lernen im Aufbau ist. Mit der Zeit kann die Steuerung lockerer werden. Vorschlag der Bibliothek:

1. **Lehrkraft setzt** das Zeichen je Arbeitsschritt (Beginn).
2. Zeichen **je Phase**, die Arbeitsschritte erben es; Ausnahmen werden ausgewiesen.
3. Die Lehrkraft gibt einen **Rahmen** vor („hier sind 💡 und 🔧 möglich“), die Lernenden **wählen
   und begründen** („ich nutze hier 💡, weil …“) und kennzeichnen ihre Nutzung.

Diagnose-Übungen und Leistungsnachweise (🚫) bleiben in jeder Stufe Entscheidung der Lehrkraft.
Ob eine Klasse die nächste Stufe erreicht hat, zeigen die Rückmeldungen der Lernenden und die
Kennzeichnung in den Abgaben – nicht der Kalender.

## 7. Wo das in der Planung steht

| Artefakt | Ebene | Stelle |
|---|---|---|
| Lernsituation | Klasse | KI-Regeln **einmal am Anfang** (zusammen mit Bewertungskriterien), Verweis auf die Regelseite; nicht in jeder Einheit wiederholen |
| Unterrichtsentwurf, Verlaufsplan | Unterricht | je Phase Zeichen und Begründung (Lehrerhinweise *KI-Einsatz in der Stunde*; Begründung in den didaktisch-methodischen Entscheidungen) |
| Lektion (Schülerseite) | Unterricht, Aufgabe | Infokasten *KI-Werkzeuge in dieser Lektion* vor der ersten Aufgabe; Zeichen am Arbeitsschritt |
| Arbeitsblatt, Aufgabenkarte | Aufgabe | Zeichen vor dem Operator; Hinweis zum Wie im Auftrag |
| KI-Chat im Kurs | Aufgabe | nur dort anbieten oder nennen, wo 💡 oder 🔧 gilt; in 🚫-Phasen bleibt er geschlossen bzw. wird nicht empfohlen (Einsatzort in der Beschreibung des Chats) |

## 8. Prüffragen

Für Planung und Prüfberichte. Skala ✅ · ⚠️ · ❌ · ➖ nicht naheliegend (wie bei den Querschnittsaufgaben).

| Nr. | Ebene | Prüffrage |
|---|---|---|
| K1 | Klasse | Gibt es verbindliche Regeln (Werkzeuge, Daten, Kennzeichnung) – und verweisen Lernsituation bzw. Lektion darauf, statt sie zu wiederholen? |
| K2 | Klasse | Sagt die Grundregel, dass Ansage und Zeichen vorgehen, sodass Ausnahmen kein Widerspruch sind? |
| U1 | Unterricht | Ist je Phase festgelegt, ob KI genutzt wird – mit einer Begründung, die das Ziel der Phase nennt? |
| U2 | Unterricht | Bleiben Entscheiden, Überprüfen und Reflektieren Leistung der Lernenden? |
| A1 | Aufgabe | Trägt jeder Arbeitsschritt ein Zeichen mit Wort, und steht im Auftrag, wie KI genutzt werden darf? |
| A2 | Aufgabe | Passen Zeichen und Phase zusammen (keine 🔧-Aufgabe in einer Phase ohne KI)? |

## 9. Formulierungshilfen

- *Klassenregel:* „KI darf euer Lernen unterstützen. Wann und wie, zeigen die Ansage und das
  Zeichen am Arbeitsschritt – sie gehen dieser Grundregel vor.“
- *Ansage:* „Die nächste Übung läuft ohne KI. Ich möchte sehen, was ihr schon selbst könnt.“
- *Auf die Rückfrage „Üben ist doch auch Lernen“:* „Ja – und heute übt ihr, ohne dass euch
  jemand etwas abnimmt, damit ihr seht, wo ihr steht. Deshalb steht auf dem Blatt 🚫.“
- *Infokasten (Lektion):* „🚫 **Phase 2 und 4:** ohne KI – Entscheidung, Überprüfung und Lernweg
  sind eure eigenen. 💡 **Phase 1 und 3:** KI zum Verstehen. 🔧 **Aufgabe 6:** mit KI arbeiten,
  Nutzung kennzeichnen. Warum? [ein Satz]“

## 10. Ältere Fassung: die KI-Ampel

Frühere Fassungen der Bibliothek (Lektionsmuster, Stand 1.15) kannten eine **KI-Ampel je
Phase**: 🟢 Erklärhilfe · 🟡 übernehmen nur gekennzeichnet und nur, was man erklären kann ·
🔴 ohne KI. Sie ist durch die drei Zeichen ersetzt:

| früher | jetzt |
|---|---|
| 🟢 Erklärhilfe | 💡 KI zum Verstehen |
| 🟡 übernehmen nur gekennzeichnet, nur Erklärbares | 🔧 Mit KI arbeiten (Kennzeichnen und Erklären-können sind Klassenregeln) |
| 🔴 ohne KI | 🚫 Ohne KI |

Gründe: Die Zeichen unterscheiden sich in Form und Wort, nicht nur in der Farbe; sie gelten am
**Arbeitsschritt**, nicht nur je Phase; und die Ampelfarben bleiben den Prüfberichten
(einsetzbar · nach Überarbeitung · überarbeiten) vorbehalten. Bereits erstellte Lektionen mit der
Ampel bleiben gültig und können beim nächsten Überarbeiten umgestellt werden.

## Anhang: references/lektionsmuster.md

# Lektionsmuster – Schülerseite im Kursprojekt

Gemeinsame Referenz für `unterrichtsmaterial-erstellen`, `schuelerseiten-veroeffentlichen`,
`lernsituation-dokumentieren` und `unterricht-entwickeln`. Beschreibt, wie **Lektionen**
(`lessons/NN_slug/lesson.md`, je 90 min) die vollständige Handlung einer **Lernsituation** für
Lernende umsetzen – zum **Neuerstellen** und zum **Überarbeiten** vorhandener Lektionen.
Vorlage: `vorlage-lektion.md`, falls vorhanden; Prüfung: `scripts/lektion_pruefen.py`.

Herkunft: Kursprojekt Berufliches Gymnasium, Informatik Q3 (25 Lektionen, 2026), dort aus der
Rückmeldung der Lernenden („zu viel Text“, „zeitlich zu umfangreich“) und einer Prüfung nach
SchuCu-BBS 2024 entstanden. Stand 1.16: Der Handlungskreis wird **je Lernsituation** geschlossen,
nicht je Lektion.
⚠️ Das Muster ist als Ganzes noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

## Inhalt
1. Lektion und Lernsituation
2. Aufbau (H1-Überschriften)
3. Elemente je Phase
4. Was nur in den Lehrerteil gehört
5. Kurz halten und Zeit ehrlich planen
6. Bestehende Lektionen überarbeiten
7. Prüfen

## 1. Lektion und Lernsituation

Die Lernsituation (Skill `lernsituation-dokumentieren`) ist die curriculare Planung für das
Bildungsgangteam; die Lektion ist das, was Lernende in der Hand haben. **Eine Lernsituation
umfasst eine oder mehrere Lektionen.** Der Handlungskreis wird je Lernsituation geschlossen;
eine einzelne Lektion muss nicht alle sechs Phasen enthalten. Eine Lernsituation aus nur einer
Lektion trägt alles selbst (so ist die Vorlage gebaut).

Bei mehreren Lektionen steht im Kopf `lernsituation: "<Kurzname>"` und `teil: "k/n"`. Ist
`lernsituation` gesetzt, ist `teil` Pflicht; `lernsituation: keine` gilt für Zusatzeinheiten wie
Kompaktstunden oder Klausurvorbereitung. Rollen der Lektionen:

| Rolle | Phasen (SchuCu-BBS 2024) | typische Bausteine |
|---|---|---|
| **Auftakt** (erste Lektion) | Informieren bzw. Analysieren · Planen · Entscheiden | *Vor dem Start*, Handlungssituation, Bewertungs- und KI-Kasten, Eingangsfrage mit Vorhersage, Planen, Entscheiden |
| **Erarbeitung** (mittlere Lektionen) | Durchführen (mit fachsystematischer Phase) | Input mit Lösungsbeispiel, größere Aufträge, Hilfen mit Stolpersteinen, Sicherung |
| **Abschluss** (letzte Lektion) | Überprüfen bzw. Kontrollieren · Reflektieren | Realitätstest, Rückmeldung mit Überarbeitung, Festhalten, Lernweg |

**Einmal je Lernsituation** (Auftakt bzw. Abschluss; in den übrigen Lektionen nur ein Verweis):
Handlungssituation, *Vor dem Start* und *Lernweg* (ein Selbsteinschätzungspaar), Kasten *So wird
bewertet*, Kasten *KI-Werkzeuge*, Phase Entscheiden, Realitätstest, Rückmeldung mit
Überarbeitung. **Je Lektion:** Problem bzw. Vorhersage, Fachwissen oder Input, Aufträge,
Stolpersteine, Sicherung und die Sollbruchstelle („Endet die Lektion hier, beginnt die nächste
mit …“; `lernsituationsmuster.md` Abschn. 7, falls vorhanden).

Zuordnung der Elemente zu den Phasen (Richtwerte für die Aufgaben einer Ein-Lektionen-Lernsituation):

| Phase (SchuCu-BBS 2024) | Element | Aufgaben (Richtwert) |
|---|---|---|
| Informieren bzw. Analysieren | *Vor dem Start*, Eingangsfrage mit Vorhersage, Zugang zum Fachwissen, Abgleich | – |
| Planen | Lernende planen selbst (Zerlegen, Entwerfen) | 1–2 |
| Entscheiden | Matrix mit eigenem Kriterium, Entscheidungsprotokoll – **nur bei echter Entscheidung** | 3–4 |
| Durchführen | größere Aufträge, Hilfen mit Stolperstein-Tabelle | 5–7 |
| Überprüfen bzw. Kontrollieren | Realitätstest, Rückmeldung mit Überarbeitung | 8–9 |
| Reflektieren | Festhalten (Transfer), eigener Lernweg | 10–11 |

Was in der Lernsituation als Kompetenz steht, muss in der Lektion als Auftrag vorkommen
(Rückwärtsprobe, `curriculum-abgleich.md` Abschn. 7, falls vorhanden).

## 2. Aufbau (H1-Überschriften)

Die H1-Überschriften sind fest, weil `edu-seiten split` sie über `phase_config.yaml` den
LMS-Phasen zuordnet – eine abweichende H1 fällt **still** aus der Schülerausgabe:

`Voraussetzungen und Kompetenzen` · `Fachwissen` · `Handlungssituation` · `Material` ·
`Hilfestellungen` · `Vertiefungen` · `Kompetenzcheck` · `Aufgaben zur Wiederholung und Übung` ·
`Lösungen / Handlungsergebnisse` · `Didaktische Hinweise`

Arbeitsaufträge stehen unter `Handlungssituation` als `## Arbeitsaufträge` mit
`### Phase N – Name (Sozialform, ca. X min)`.

## 3. Elemente je Phase

**Vor dem Start** (unter *Kompetenzen*, 1 min, in der Auftakt-Lektion): Lernende markieren jede
Kompetenz der Lernsituation mit ✔ / ~ / ✘. Am Ende der Lernsituation vergleichen sie damit
(Lernweg).

**Eingangsfrage mit Vorhersage** (Anfang *Fachwissen*, 3 min): ein kleiner Fall, dessen
Ergebnis die typische Fehlvorstellung der Lektion sichtbar macht. Lernende **sagen vorher**,
bevor sie lesen oder ausführen. Der Kasten **Abgleich** am Ende des Fachwissens löst auf.
Vorhersagen vor dem Ausführen gilt auch in Aufträgen: erst notieren, dann ausprobieren.

**Zugang zum Fachwissen:** Standard ist **ein** Zugang – bei neuem Verfahren oder neuer Syntax
oft ein kurzer **Lehrkraftinput mit Lösungsbeispiel** (10–15 min, im Distanzunterricht ein
Screencast; `lernsituationsmuster.md` Abschn. 12, falls vorhanden) statt langer Lektüre.
Mehrere gleichwertige Zugänge (Ausprobieren, Lesen, Fachbuch) sind nur sinnvoll, wenn
**eine** Wahl genügt und die Zeit dafür (20–30 min) in der Zeitplanung steht; ein Zugang, der
mit „danach … lesen“ endet, ist kein Zugang, sondern Mehrarbeit. Wahlmöglichkeiten (M3/M16)
entstehen besser über Hilfen, Aufgabenauswahl und Vertiefung als über Lesewege.
**Fachwissen und Hilfen enthalten nicht den Lösungscode der eigenen Aufgabe:** Das
Lösungsbeispiel zeigt einen analogen Fall. Sonst wird Durchführen zum Abschreiben, und Lesen
und Aufgabe doppeln sich.

**So wird bewertet – vor dem Start lesen** (direkt unter `## Arbeitsaufträge`, einmal je
Lernsituation): Abgabe, Kriterien mit Punkten, Summe. Gröbere Fassung des Feinrasters im
Lehrerteil mit **gleicher Summe**; die verdeckte Schwierigkeit wird hier nicht verraten.
Satz: *Bewertet wird nicht, welche Variante ihr wählt, sondern wie ihr sie begründet und
überprüft. Dein Lernweg wird nicht benotet.*

**KI-Werkzeuge in dieser Lektion** (ebenfalls vor der ersten Aufgabe): KI-Einsatz **je Phase**
mit den drei Zeichen – 🚫 Ohne KI (Vorhersagen, Entscheidung, Überprüfung, Lernweg,
Leistungsnachweise) · 💡 KI zum Verstehen · 🔧 Mit KI arbeiten (nur gekennzeichnet, nur, was
man erklären kann) – und **ein Satz Begründung** für jede Phase ohne KI. Dasselbe Zeichen steht
**am Arbeitsschritt**, vor dem Operator; wie KI genutzt werden darf, steht im Auftrag.
Weiterführende Regeln auf einer Regelseite des Kurses (fünf Regeln: erst selbst, prüfen statt
glauben, kennzeichnen, erklären können, Daten schützen); in Folgelektionen genügt ein Verweis.
Drei Ebenen, Voreinstellung je Phase, Begründungen und Prüffragen: `ki-vereinbarungen.md`, falls vorhanden.

**Planen** (Aufgaben 1–2): Lernende zerlegen und entwerfen selbst. Nicht kleinschrittig
vorgeben – ein Auftrag mit Operator und Ergebnisform statt zehn Lückenschritte. Beantwortet das
Fachwissen die Planungsaufgabe schon, ist es keine Planung, sondern Kontrolle des Gelesenen.

**Entscheiden** (Aufgaben 3–4; `lernsituationsmuster.md` Abschn. 2, falls vorhanden): **nur an
einer echten Entscheidungsstelle** der Lernsituation. Die Auftraggeberin stellt **zwei
vertretbare Varianten** A und B vor, die nicht beide gebaut werden müssen. Lernende bewerten
sie in einer Matrix (1–3 Punkte) und **ergänzen ein eigenes Kriterium**; dann halten sie die
Entscheidung fest: *Kontext · Gewählt · Verworfen, weil … · Ausschlag gab · Konsequenz*.
Lehrkraft zurückhaltend. Kleine Wahlen (Schreibweise, Parameter, Werkzeug) werden mit einem
Satz notiert – *gewählt, weil …, verworfen: …* –, nicht mit Matrix und Protokoll. Legt die
Ausstattung die Wahl fest (z. B. nur ein Werkzeug ist installierbar), setzt die Lehrkraft sie
fest, statt eine Scheinentscheidung zu inszenieren.

**Durchführen** (Aufgaben 5–7): wenige, größere Aufträge. Mindestens eine **verdeckte
Schwierigkeit** je Lernsituation – eine Stelle, an der ein naheliegender Weg scheitert, ohne
dass der Auftrag darauf hinweist. Sie steht nur in den Didaktischen Hinweisen (Ort, Symptom,
wo nachgefragt wird). Vorher ggf. eine **fachsystematische Phase** (Input mit Lösungsbeispiel).

**Stolperstein-Tabelle** (in *Hilfestellungen*; `lernsituationsmuster.md` Abschn. 5, falls vorhanden):

| Das beobachtest du | Das steckt dahinter | So gehst du vor |
|---|---|---|
| Symptom (Meldung, falsches Ergebnis) | Ursache | konkrete Abhilfe |

Gehört eine Entscheidung zur Lernsituation, kommt die Zeile dazu: *In der Matrix bekommt eine
Variante überall 3 Punkte* → *die Entscheidung stand schon fest* → *ein Kriterium suchen, bei
dem die andere gewinnt*. Daneben gestufte Hilfen (Orientierung → Werkzeug → eingeklapptes
Gerüst, entspricht Impuls → Strategie → Teilschritt in `schuelermaterial.md`); das Gerüst lässt die
Kernidee zu ergänzen übrig.

**Realitätstest** (Aufgabe 8, Abschluss): zwei konkrete Fälle, **(a)** trifft Variante A,
**(b)** trifft Variante B. Lernende gleichen mit ihrer Matrix ab – die Entscheidung wird
überprüft, nicht nur das Produkt. Ohne echte Entscheidung: das Handlungsergebnis an zwei
konkreten Fällen prüfen.

**Rückmeldung** (Aufgabe 9, Abschluss; `lernsituationsmuster.md` Abschn. 3, falls vorhanden):
mit einem Team, das **anders** entschieden hat – wo das möglich ist; sonst mit einem beliebigen
Team – **zwei Stärken und ein nächster Schritt**, danach **überarbeiten**.

**Festhalten** (Aufgabe 10): Transfer – was gilt über diesen Fall hinaus?

**Dein Lernweg** (Aufgabe 11, Abschluss, allein, 3 min, unbenotet): Vergleich mit den
Markierungen vom Anfang; wo festgesteckt, was hat geholfen; **ein nächster Schritt**.

**Vertiefungen** sind ein **Zusatz außerhalb des Kernwegs**: „Wer fertig ist, wählt eine“
(weiterführen, recherchieren, vorgreifen). Sie stehen in keiner Pflichtzeit.

## 4. Was nur in den Lehrerteil gehört

Unter `# Lösungen / Handlungsergebnisse` und `# Didaktische Hinweise` (bzw. in `solutions/`):
Feinraster mit Erwartungshorizont, verdeckte Schwierigkeit, Begründung der Varianten (welche
Zahl im Realitätstest trifft welche Variante), Rolle der Lehrkraft je Phase, Zeitplanung,
Differenzierung, typische Fehler, Querverbindungen. Für die Didaktischen Hinweise feste
Spiegelstriche verwenden – `**Rolle**`, `**Verdeckte Schwierigkeit (nicht ankündigen)**`,
`**Zeitplanung**`, `**Kernweg**`, `**Fachsystematische Phase**`, `**Differenzierung**`,
`**Querverbindung**` –, dann lassen sie sich automatisch in die Dokumentation der
Lernsituation übernehmen. Beispieldateien, die eine Aufgabe lösen, gehören nicht in die
Schülerausgabe (`copy_dirs`).

## 5. Kurz halten und Zeit ehrlich planen

Lernende empfinden lange Lektionen als Hürde, und was nicht in der Zeitplanung steht, geht
über die Zeit. Regeln:

- **Kernweg:** Das, was alle in der Lektion schaffen müssen, passt in **60–65 min je 90 min**
  (im Skill `unterrichtsentwurf-erstellen`, `methodenrepertoire.md` Abschn. 3).
  Alles darüber ist Zusatz. Die Minuten des Kernwegs stehen in den Didaktischen Hinweisen.
- **Zeitplanung vollständig:** Input, Lesen, Aufbau, Übergänge und Sicherung sind
  eingerechnet; die Summe ergibt die Dauer der Lektion. Zeiten für Zugang und Aufbau, die
  „nebenbei“ anfallen, gehören hinein. Eine Planung, die nur die Aufträge zählt, geht nicht auf.
- **Länge des Schülerteils** (alles außer Lösungen und Didaktischen Hinweisen): **höchstens
  rund 1 500 Wörter ohne Code**, Codezeilen werden getrennt gezählt (Richtwert; Vorbild ist
  eine Kompaktstunde mit Syntaxkarten und Live-Coding). Mittel: Problem zuerst, ein Beispiel
  statt drei, Darstellung statt Absatz (Skizze, Diagramm, Tabelle), Details in eingeklappte
  Kästen, Wiederholungen streichen, Boilerplate je Lernsituation nur einmal.
- **Offen, anschaulich, ohne Dekoration:** Aufträge nennen Ziel und Ergebnis statt
  Einzelschritte (Schritte in die Hilfen); Fachwissen und Aufträge arbeiten mit Darstellungen;
  keine Emojis außer den KI-Zeichen, keine Floskeln oder Ankündigungen
  (`schuelermaterial.md`, falls vorhanden).
- **Selbsteinschätzung** einmal je Lernsituation (*Vor dem Start* und *Lernweg*); nicht noch
  Ich-kann-Liste, Kompetenzraster und Arbeitsblatt-Selbstcheck in jeder Lektion.
- **Übungen** (H5P, Wiederholungsaufgaben) sind Festigung außerhalb des Kernwegs.

## 6. Bestehende Lektionen überarbeiten

Reihenfolge, die sich bewährt hat:
1. `lektion_pruefen.py` laufen lassen – Ist-Stand je Element, Wortzahl, Zeitplanung.
2. **Zuschnitt prüfen:** Gehören aufeinanderfolgende Lektionen zu *einer* Handlungssituation und
   *einem* Handlungsergebnis? Dann als eine Lernsituation führen (Kopf `lernsituation`, `teil`).
   Ein neuer Zuschnitt ändert das schulische Curriculum und braucht den **Bildungsgangbeschluss**
   (`schucu-bbs-2024.md` Abschn. 6, falls vorhanden); Kompetenzcodes und Lernsituations-
   dokumente neu prüfen.
3. **Bündeln:** Bewertungs- und KI-Kasten, *Vor dem Start*, Entscheiden, Realitätstest,
   Rückmeldung mit Überarbeitung und Lernweg je Lernsituation einmal; Aufgabennummern neu zählen
   und **alle** Verweise (Lösung, Arbeitsblatt, Beispieldateien, Didaktik) mitziehen.
4. **Entscheiden nur an echter Stelle** (Abschn. 3).
5. **Doppeltes streichen:** Fachwissen, Hilfen und Arbeitsblatt dürfen sich nicht
   wiederholen; Lösungscode aus Fachwissen und Hilfen nehmen (analoges Lösungsbeispiel).
6. **Fachsystematische Phase** einsetzen, wo Selbststudium teuer ist
   (`lernsituationsmuster.md` Abschn. 12, falls vorhanden): Begründung in den Didaktischen
   Hinweisen.
7. **Kernweg und Zeitplanung** rechnen; Vertiefungen und Übungen als Zusatz kennzeichnen.
8. Wortzahl vorher und nachher festhalten.
9. Verdeckte Schwierigkeit ergänzen und nur in den Didaktischen Hinweisen beschreiben.
10. Schülerausgabe neu erzeugen und mit `ausgabe_pruefen.py` prüfen: Es darf nichts aus dem
    Lehrerteil und keine Musterlösung (auch nicht in Beispieldateien) in der Ausgabe stehen.

## 7. Prüfen

`python3 scripts/lektion_pruefen.py lessons/*/lesson.md [--max-woerter 1500] [--json]` meldet
je Lektion, welche Elemente erkennbar sind, ob die Bewertungssumme aufgeht, ob die Phasenzeiten
und der Zugang zur Dauer passen, wie lang der Schülerteil ist (Code getrennt), ob ein Kernweg
ausgewiesen ist und ob eine Lehrkraftinput-Phase begründet und kurz genug ist
(Auftragslänge, Kleinschrittigkeit, Darstellungen und Dekoration prüft
`schuelermaterial_pruefen.py`, falls vorhanden). Tragen mehrere
Lektionen dieselbe `lernsituation`, prüft das Skript zusätzlich je Lernsituation, ob der
Handlungskreis geschlossen ist (Entscheiden, Überprüfen, Reflektieren irgendwo in der
Lernsituation). „Nicht gefunden“ heißt „von Hand nachsehen“ – das Skript sucht nach
Signalwörtern und ersetzt keine fachliche Durchsicht.

## Anhang: references/lernsituationsmuster.md

# Lernsituationsmuster – Diagnose, Entscheiden, Überprüfen, Reflektieren, Projekt, Experiment, Urteilsbildung

Bauformen, mit denen eine Handlungssituation **alle sechs Phasen** trägt. Gewonnen aus dem
Abgleich mit Lernsituationen aus der Fortbildung (u. a. SHK, LF 7) und mit NLQ-Mustern des
Beruflichen Gymnasiums Technik (ING3–ING5), verallgemeinert und in eigenen Worten. Die Muster ergänzen die Leitlinie (`schucu-bbs-2024.md`, falls vorhanden); sie sind **kein
Bestandteil der Leitlinie**. Beispiele: Gurtförderer GF-2 (fiktiv).

## Inhalt
1. Diagnose-Lernsituation
2. Entscheiden gestalten
3. Überprüfen gestalten
4. Reflektieren gestalten
5. Lernhürden planen
6. Roter Faden durch die Lernsituation
7. Zeitvarianten und Ersatzwege
8. Phasencheck (Ergänzung zum Analysebogen)
9. Projekt-Lernsituation mit Lastenheft
10. Hypothesen- und Experiment-Lernsituation
11. Urteilsbildung und Technikfolgenabschätzung
12. Lernzeit effizient nutzen – fachsystematische und lehrkraftgeführte Lernphasen

---

## 1. Diagnose-Lernsituation

Für Kundendienst-, Instandhaltungs- und Fehlersuchaufträge: Störmeldung, Reklamation,
Fehlerbild an Anlage, Netzwerk oder Software. Kern: **Die Lernenden finden die Ursache selbst.**

| Phase | Baustein | Material |
|---|---|---|
| Informieren | Vermutungen sammeln (mind. drei, die wahrscheinlichste markieren), auf einem Plakat festhalten, das hängen bleibt; System erfassen (Schema, Checkliste); Fachwissen in fachsystematischen Phasen, jeweils mit Rückbindungsfrage (Abschn. 6) | Situationsmaterial, Checkliste, Infotexte |
| Planen | Prüfplan: Prüfschritt, geprüfte Vermutung, erwartetes Ergebnis; Befunde auf Anforderung; Ursachen begründet ausschließen; Nachweis durch Rechnung, Messung oder Norm | Prüfplan und Befundkarten, Übung mit Kontrollwert |
| Entscheiden | Maßnahmen gegen die Ursache, nicht gegen das Symptom | Entscheidungsmatrix (Abschn. 2) |
| Durchführen | Handlungsergebnis, z. B. Störungsbericht mit Empfehlung; Umsetzung an Übungsanlage oder Ersatzweg | Berichtsvorlage, Arbeitsbericht |
| Überprüfen | Peer-Check; Abgleich mit den Anfangsvermutungen | Peer-Feedback-Bogen |
| Reflektieren | Transfer auf ein verändertes Fehlerbild | Reflexionsauftrag (Abschn. 4) |

Regeln:
- **Nichts verraten.** Kein Auftrag, keine Überschrift und keine Hilfe nennt die Ursache
  („Sie vermuten, dass das Lager …" nimmt die Diagnose vorweg). In einer Expertenphase ist die
  Ursache ein Thema unter mehreren.
- **Information gegen Planung.** Befunde gibt es nur zu Prüfschritten, die im eigenen Prüfplan
  stehen. Die Lehrkraft gibt sie in einer Rolle aus (Meisterin, Schichtleitung). Wer gründlich
  plant, erfährt mehr – das differenziert von selbst.
- **Stimmiges Befundbild.** Die Befunde ergeben eine Ursachenkette (oder bewusst zwei
  unabhängige Fehler). Einige schließen Vermutungen aus. Mindestens ein Befund ist auffällig,
  aber nicht die Ursache (falsche Fährte). Alle Werte passen zur Handlungssituation.
- **Ursache statt Symptom** als Maßstab: Im Bewertungsraster erreicht eine reine
  Symptombehandlung höchstens die unterste Stufe; in der Entscheidungsmatrix hat „Wirksamkeit
  gegen die Ursache" das höchste Gewicht.
- **Prüfreihenfolge im Erwartungshorizont:** vom Einfachen und Zerstörungsfreien zum
  Aufwendigen (befragen → ablesen → ansehen → messen → zerlegen). Andere begründete
  Reihenfolgen gelten.
- Die **Wirkungskette** (Ursache → Folgen → Symptom) steht im Erwartungshorizont und im Raster;
  als Bild mit `fachdiagramm-erstellen` (Ablauf).

## 2. Entscheiden gestalten

Die Leitlinie verlangt, dass die Lernenden sich für einen Lösungsweg entscheiden. Damit das eine
Leistung ist und kein Abnicken:
- **Mindestens zwei vertretbare Alternativen** vorgeben, Platz für eigene; in der
  Diagnose-Lernsituation **drei**, darunter die naheliegende, billige Teil- oder
  Symptomlösung. Eine Entscheidung gehört nur dorthin, wo es echte Alternativen gibt: Müssen
  beide Varianten ohnehin gebaut werden oder legt die Ausstattung die Wahl fest, ist es eine
  Scheinentscheidung und kostet Zeit ohne Lernzuwachs.
- **Kriterien mit Gewichtung** offenlegen (z. B. Wirksamkeit gegen die Ursache ×3,
  Sicherheit bzw. Norm- und Herstellervorgabe ×2, Kosten ×1, Aufwand oder Stillstand ×1).
  Die Gewichtung dürfen die Lernenden **begründet ändern** – die Begründung zählt mit.
- **Zielkonflikt** aus der Handlungssituation: Budget, Stillstandszeit oder Termin gegen
  fachliche Notwendigkeit.
- **Nachweis**, dass die naheliegende Lösung nicht reicht (Befund, Messung oder Rechnung). So
  wird die Analyse zur Entscheidungsgrundlage.
- Die Entscheidung wird **schriftlich begründet** und geht als Abschnitt in das
  Handlungsergebnis ein.
- Die Lehrkraft gibt Rückmeldung zu Kriterien und Begründung, nicht zur „richtigen" Maßnahme.

Kleinere Form: Pro-Contra-Tabelle zweier Lösungen oder Planbesprechung mit der Lehrkraft in
einer Rolle.

## 3. Überprüfen gestalten

- **Kriterien = offengelegtes Bewertungsraster** des Handlungsergebnisses, dazu Kontrollwerte.
- **Peer-Check:** Ergebnis mit einer Partnergruppe tauschen, mit dem Raster prüfen,
  Rückmeldung „zwei Stärken, ein nächster Schritt", **danach das eigene Ergebnis
  überarbeiten**. Ohne eingeplante Überarbeitungszeit bleibt Feedback folgenlos.
- **Feedbackregeln** vorab: Beobachtetes beschreiben, nicht die Person; der nächste Schritt ist
  konkret und machbar; wer Feedback bekommt, hört zu und fragt höchstens nach.
- **Abgleich mit den Anfangsvermutungen:** Was hat sich bestätigt, woran war es zu erkennen?
- **Gesprächsleistungen** (Beratung, Übergabe, Einweisung) in einer Simulation mit
  Rollenkarten und Beobachtungsbogen prüfen; wer die Kundenrolle spielt, beobachtet mit.

## 4. Reflektieren gestalten

Reflexionsfragen nach vier Typen; je Lernsituation mindestens eine **Transfer-** und eine
**Selbstbezugsfrage**:

| Typ | fragt nach | Beispiel (GF-2) |
|---|---|---|
| Ergebnis | Was ist erreicht, was hat sich bestätigt? | Welche Vermutung hat sich bestätigt – an welchem Befund haben Sie es erkannt? |
| Vorgehen | Wie bin ich vorgegangen, wo hakte es? | An welcher Stelle kamen Sie nicht weiter, und was hat geholfen? |
| Transfer | Was tue ich in einer veränderten Lage? | Wie gehen Sie vor, wenn der Gurt nach dem Rollentausch weiter schief läuft? |
| Selbstbezug | Was ist mein nächster Schritt? | Was prüfen Sie beim nächsten Störungsauftrag als Erstes? |

- **Selbsteinschätzung am Anfang und am Ende** (Kompetenzraster oder Kannliste) vergleichen:
  „Wo haben Sie sich verbessert, wo noch nicht?" Die Bögen bleiben bei den Lernenden – keine
  Auswertung je Person (Leitplanke: Lernstände nur für die Lerngruppe).
- Transfer in den Ausbildungsbetrieb über einen Erkundungsauftrag (Methodenrepertoire,
  „Mein Betrieb").
- Abschluss im Plenum, z. B. Blitzlicht.

## 5. Lernhürden planen

Vor dem Material drei bis sieben Hürden benennen: Fehlvorstellungen, Verwechslung ähnlicher
Begriffe, Rechenfallen (Vorzeichen, Einheit, Bezugsgröße, Über- und Absolutwert), Symptom statt
Ursache, Vermischung benachbarter Themen. Je Hürde Gegenmaßnahme und **Ort im Material**:

| Lernhürde | Gegenmaßnahme | Ort im Material |
|---|---|---|
| „Mehr Fett schmiert besser" | Herstellerangabe zur Füllmenge auswerten; Folgen der Überfettung im Infotext | Infoblatt Schmierung, Aufgabe 2 |
| Wartungsintervall in Tagen statt Betriebsstunden gerechnet | Stolperstein-Kasten, Kontrollwert | Arbeitsblatt 3 |

- **Gegenmaßnahmen:** Stolperstein-Kasten für Lernende auf dem Arbeitsblatt, Hilfekarte,
  Kontrollwert mit Diagnosehinweis („Wenn nicht: Einheit prüfen"), Befundkarte, Diagramm oder
  Versuch, Kriterium in Matrix oder Raster.
- **Fehlvorstellungen aufgreifen, nicht nur benennen:** Vorhersage notieren → mit Diagramm,
  Messung oder Versuch konfrontieren → Erklärung selbst formulieren → in der Sicherung
  ausdrücklich klären.
- Dokumentieren in den *didaktisch-methodischen Kommentaren* der Lernsituation und unter
  *Stolpersteine* in der Lehrerhandreichung.

## 6. Roter Faden durch die Lernsituation

- **Rückbindungsfrage:** Jede fachsystematische Phase (Expertengruppe, Infotext, Lehrgang)
  endet mit „Was bedeutet das für [Anlage, Kundin, Auftrag der Handlungssituation]?". In der
  Sicherung bekommt die Frage eine eigene Spalte, im Erwartungshorizont je Thema eine Antwort.
- **Ein Handlungsergebnis bündelt.** Teilprodukte (Plakat, Steckbrief, Prüfplan, Matrix) sind
  Arbeitsschritte und Informationsquellen, **keine eigenen Bewertungsgegenstände**. Das hält
  die Bewertung schlank. Wird das Ergebnis in einem Gespräch vertreten, bekommt das Gespräch
  eine Rückmeldung nach Kriterien.
  **Ausnahme:** Nennen die curriculare Vorgabe, die Leistungsbewertung der LS oder ein
  Beschluss des Bildungsgangs **Teilleistungen** ausdrücklich (z. B. Dokumentation,
  Präsentation, Projektprozess, Umsetzung in Projekten des BG), werden sie getrennt bewertet:
  mit offengelegten Kriterien und Gewichten, **ohne Doppelbewertung** desselben Kriteriums und
  mit ausgewiesenem Einzelanteil bei Gruppenarbeit.
- **Wiederkehrende Elemente:** Was der Einstieg aufwirft (Vermutungen, Behauptung der Kundin),
  wird beim Überprüfen wieder aufgegriffen und kann im Gespräch als Einwand zurückkommen.
- **KI-Auskunft als Situationsmaterial:** Die Kundin bringt den Rat eines KI-Chatbots mit.
  Die Lernenden prüfen ihn: Was stimmt, was fehlt, was wäre die Folge, wenn sie danach handelt?
  Lernziel (Medienbildung): Allgemeine Auskünfte ohne Anlagendaten ersetzen keine Diagnose;
  geprüft wird an Befunden, Herstellerangaben und Normen. Die Auskunft selbst formulieren
  (fiktiv, teils richtig, teils unvollständig), keine echte Chatbot-Ausgabe übernehmen.
- **Wahl** von Thema und Produktform (Plakat, Steckbrief, Erklärvideo) – Ziel und
  Handlungsergebnis bleiben für alle gleich.

## 7. Zeitvarianten und Ersatzwege

- **Puffer** in der Phasenplanung ausweisen; Phasenzeiten plus Puffer = Zeitrichtwert.
- **Kürzungsoption:** Für den Fall weniger Stunden festlegen, was gekürzt wird, mit Minuten je
  Baustein (z. B. Steckbrief statt Plakat −20 min, eine Gesprächsrunde statt zwei −10 min).
  Nie gekürzt werden **Entscheiden, Überprüfen (mit Überarbeitung) und Reflektieren der
  Lernsituation** sowie die Sicherung des Handlungsergebnisses – je Lernsituation, nicht je
  Unterrichtseinheit.
- **Handlungskreis über mehrere Einheiten**: Der
  Kreis wird je Lernsituation geschlossen, nicht je 90 Minuten. Die Phasen werden auf die
  Einheiten verteilt (z. B. Einheit 1: Informieren, Planen, Entscheiden · Einheit 2:
  Durchführen · Einheit 3: Überprüfen, Reflektieren). Jede Einheit endet an einer
  Sollbruchstelle mit einem gesicherten Zwischenergebnis und sagt, womit die nächste beginnt.
  Die letzte Einheit überprüft und reflektiert das Handlungsergebnis der **ganzen**
  Lernsituation; Bewertungskriterien, KI-Regeln und Selbsteinschätzung stehen einmal am
  Anfang der Lernsituation. Die KI-Regeln legen den Rahmen (Klassenebene); je Einheit und
  Aufgabe sagen Zeichen und kurze Begründung, wo KI genutzt wird und wo nicht
  (`ki-vereinbarungen.md`, falls vorhanden).
- **Sollbruchstelle zwischen Phasen** auch im Schülermaterial markieren („Endet der Block hier,
  beginnt die nächste Stunde mit …").
- **Ersatzweg bei fehlender Ausstattung:** Ist keine Übungsanlage frei, läuft der praktische Teil
  als Planspiel oder Simulation mit derselben Dokumentation (z. B. Arbeitsbericht). So bleibt
  das Handlungsergebnis erreichbar – das hilft auch bei den Prüffragen zum Distanzunterricht.

## 8. Phasencheck (Ergänzung zum Analysebogen)

Die 16 Kriterien des Analysebogens prüfen die Phasen nicht einzeln. Der Phasencheck ergänzt
sie. Er ist **kein Kriterium der Leitlinie** und wird getrennt vom Analysebogen ausgewiesen.
Skala: ✅ erkennbar · ⚠️ angelegt, aber dünn · ❌ fehlt.

| Nr. | Bereich | Prüffrage | bei ⚠️/❌ |
|---|---|---|---|
| 1 | Informieren | Werden Vorwissen oder Vermutungen aktiviert und wird Fachwissen an die Handlungssituation zurückgebunden? | Abschn. 6 |
| 2 | Planen | Planen die Lernenden selbst (Vorgehen, Prüfplan, Kriterien), und verrät kein Auftrag die Lösung? | Abschn. 1 |
| 3 | Entscheiden | Werden mindestens zwei Alternativen nach offengelegten Kriterien abgewogen und wird die Entscheidung schriftlich begründet? | Abschn. 2 |
| 4 | Durchführen | Entsteht das Handlungsergebnis – mit praktischem Anteil oder Ersatzweg, wo der Beruf es verlangt? | Abschn. 7 |
| 5 | Überprüfen | Prüfen die Lernenden nach Kriterien (Raster, Kontrollwerte), mit Zeit zum Überarbeiten? | Abschn. 3 |
| 6 | Reflektieren | Gibt es mindestens eine Transfer- und eine Selbstbezugsfrage und einen Anlass, den eigenen Lernfortschritt zu sehen? | Abschn. 4 |
| 7 | Lernhürden | Sind Lernhürden mit Gegenmaßnahme und Ort im Material dokumentiert? | Abschn. 5 |
| 8 | Leistungsbewertung | Sind Bewertungsgegenstände, Kriterien, Gewichte und – bei Gruppenarbeit – der Einzelanteil offengelegt, bevor die Lernenden arbeiten? | Abschn. 6 |
| 9 | Leitidee | Ist eine didaktische Leitidee der Lernsituation formuliert (unter *didaktisch-methodische Kommentare*), exemplarisch und bedeutsam, und lassen sich die Phasen auf sie beziehen? | `didaktische-leitidee.md`, falls vorhanden |
| 10 | Lernzeit | Ist der Kreis innerhalb der Lernsituation geschlossen (auch über mehrere Einheiten)? Ist die Zeitplanung vollständig (Input, Lesen, Aufbau, Übergänge), der Kernweg ausgewiesen, und jede fachsystematische Phase begründet und zurückgebunden? | Abschn. 7 und 12 |

## 9. Projekt-Lernsituation mit Lastenheft

Für längere Lernsituationen (20–60 h), typisch im Beruflichen Gymnasium und in Fachschulen:
Ein fiktiver Auftraggeber übergibt ein **Lastenheft** (was und wofür, Randbedingungen), die
Lernenden antworten mit einem **Pflichtenheft** (wie) und liefern ein Handlungsergebnis
(Dokumentation, Prototyp, Simulation, Präsentation).

| Phase | Baustein | Material |
|---|---|---|
| Informieren | Lastenheft analysieren: Anforderungen, Randbedingungen (Budget, Normen, Termine), offene Fragen an den Auftraggeber | Lastenheft, Fragenliste |
| Planen | Pflichtenheft mit Lösungsideen; Projektstrukturplan, Arbeitspakete mit Verantwortlichen, Meilensteine; Kriterien für das Ergebnis | Vorlage Pflichtenheft, Projektplan |
| Entscheiden | Lösungsvarianten nach technischen, ökologischen und ökonomischen Kriterien (Abschn. 2); Freigabe des Pflichtenhefts in einem Meilensteingespräch | Entscheidungsmatrix |
| Durchführen | Arbeitspakete umsetzen (Rechnung, Konstruktion, Programm, Experiment, Simulation); Projektjournal | Infomaterial, Hilfekarten, Projektjournal |
| Überprüfen | Soll-Ist-Abgleich mit Lastenheft und Pflichtenheft; Test, Peer-Review, Zwischenpräsentation | Prüfliste aus dem Lastenheft |
| Reflektieren | Projekt-Retrospektive: Vorgehen, Zusammenarbeit, Annahmen, die das Ergebnis bestimmt haben | Reflexionsauftrag |

Regeln:
- **Das Lastenheft nennt Ziele, nicht die Lösung.** „Ganzjährige Versorgung aus eigener
  PV-Erzeugung“ lässt Alternativen zu; „mittels Wasserstoffs“ legt die Technik fest. Soll die
  Technik vorgegeben sein, wenigstens Varianten innerhalb der Technik offenlassen.
- **Jede Anforderung führt zu einem Teil des Handlungsergebnisses** und zu einem Erwartungsteil
  im Erwartungshorizont. Fachkompetenzen ohne Lastenheftpunkt (z. B. „Nachhaltigkeit
  beurteilen“) laufen ins Leere.
- **Ein roter Faden statt sechs Inseln:** heterogene Anforderungen (Baustelle, CNC-Teil, App)
  über eine Systemfrage verbinden; künstlich angehängte Teilaufgaben als solche begründen.
- **Projektmanagement lernen, nicht nur verlangen:** Meilensteine, Rollen, Journal einführen
  (im BG mit ING2 und Fach Praxis abstimmen).
- **Fiktiver Auftraggeber:** erkennbar fiktiv, keine echten Telefonnummern, E-Mail mit
  `example.org`. Platzhalter für die Lehrkraft vor der Ausgabe entfernen.
- **Der Erwartungshorizont zeigt mehrere vertretbare Lösungen** oder die Kriterien, an denen
  jede Lösung gemessen wird – nicht nur „eine mögliche Lösung“.
- **Bewertung:** Teilleistungen (Dokumentation, Präsentation, Prozess) nach Abschn. 6;
  Fachgespräch je Arbeitspaket für den Einzelanteil.

## 10. Hypothesen- und Experiment-Lernsituation

Die Lernenden stellen eine prüfbare Vermutung auf, planen einen Versuch oder eine Messung,
werten aus und vergleichen mit der Vermutung. Geeignet für Wirkungsgrade, Kennlinien,
Werkstoffeigenschaften, Sensorik.

- **Vorhersage vor dem Versuch** schriftlich (Hypothese mit Begründung), danach Abgleich:
  bestätigt, widerlegt, offen – mit Erklärung.
- **Variablen** benennen (unabhängig, abhängig, konstant gehalten); mindestens eine Variable
  wählen die Lernenden selbst.
- **Erwartungswerte aus Vorversuch oder Rechnung mit physikalischer Grenze**
  (`experimentsicherheit.md` Abschn. 5, falls vorhanden): Ein „mögliches Ergebnis“, das gegen Energieerhaltung
  oder Faraday verstößt, lehrt das Falsche.
- **Fehlerbetrachtung** mit Messunsicherheit und Vergleich Labor ↔ Technik („Warum liegt der
  Wirkungsgrad im Versuch bei 30 %, in der Anlage bei 70 %?“) – das ist die Rückbindungsfrage.
- **Sicherheit vor Ausgabe:** Gefährdungsbeurteilung, Vorversuch, Freigabezeile der Lehrkraft
  (`experiment-planen`).

## 11. Urteilsbildung und Technikfolgenabschätzung

Für gesellschaftlich umstrittene Technik (Energieanlagen, Mobilität, KI, Automatisierung):
Die Lernenden schätzen Folgen ab, prüfen Hypothesen an Quellen und bilden ein eigenes Urteil.

| Phase | Baustein |
|---|---|
| Informieren | Technik und Systemgrenze (Lebenszyklus: Herstellung, Betrieb, Rückbau); Beteiligte und Betroffene sammeln |
| Planen | Hypothesen zu Folgen formulieren (positiv und negativ), Prüfverfahren je Hypothese festlegen (Daten, Rechnung, Literatur, Befragung) |
| Entscheiden | Hypothesen auswählen, Bewertungsmethode und Wertbereiche festlegen (in Anlehnung an VDI 3780) |
| Durchführen | Hypothesen prüfen mit Quellenmappe (Typ und Interessenlage, `quellenbewertung.md`, falls vorhanden); Ergebnis je Hypothese: bestätigt, widerlegt, offen |
| Überprüfen | Anhörung bzw. Bürgerdialog als Rollenspiel mit mehreren Perspektiven (`rollenspiel.md`, falls vorhanden); Abgleich der Ergebnisse mit den Hypothesen |
| Reflektieren | eigenes Urteil und eigene Rolle (z. B. Ingenieurteam im Auftrag eines Unternehmens) reflektieren |

Regeln:
- **Ergebnisoffen rahmen** (Beutelsbacher Konsens, `querschnittsaufgaben.md`, falls vorhanden). Ein Auftrag
  „Einwände entkräften“ oder „Akzeptanz schaffen“ gibt das Urteil vor. Besser: Auftraggeber
  wünscht eine **ehrliche** Folgenabschätzung, weil er Vertrauen braucht.
- **Hypothese ≠ Meinung:** prüfbar formulieren („Der Schallpegel überschreitet am nächsten
  Wohnhaus nachts den Richtwert“ statt „Windräder machen krank“).
- **Bestätigte Bedenken bleiben bestätigt** und führen zu Maßnahmen, die negative Folgen
  verringern; Zielkonflikte werden benannt, nicht aufgelöst.
- **Musterlösungen** (Schulungsunterlagen, Transkripte) sind selbst ausgewogen und fachlich
  geprüft; KI-erzeugte Muster werden gekennzeichnet und wie ein Erwartungshorizont geprüft.
- Werkzeug: `technikfolgen-abschaetzen` (Dossier, Quellenmappe, Rollenkarten, Prüfskript).

## 12. Lernzeit effizient nutzen – fachsystematische und lehrkraftgeführte Lernphasen

Wo es zweckdienlich und gut begründet ist, darf
fachsystematisch und lehrkraftgeführt (auch frontal) unterrichtet werden. Die Leitlinie sieht
das ausdrücklich vor (Lernsituation „kann fachsystematische Lernphasen enthalten“, Lehrkraft
in informierender Rolle, „Unterrichtszeit effizient nutzen“;
`schucu-bbs-2024.md` Abschn. 2, falls vorhanden). Eigenständiges Entdecken ersetzt Anleitung nicht überall: Bei geringem
Vorwissen belastet vollständig offenes Erarbeiten das Arbeitsgedächtnis, ausgearbeitete
Beispiele wirken dann besser; mit wachsender Erfahrung kehrt sich das um (Fading,
`gestaltungsprinzipien.md` im Skill `unterrichtsmaterial-erstellen`).

**Zweckdienlich, wenn …**

| Anlass | Beispiel |
|---|---|
| neues Verfahren oder neue Syntax bei wenig Vorwissen | Lösungsbeispiel mit lautem Denken („Vormachen“), erste Zeilen Code live |
| Werkzeug- oder Sicherheitsunterweisung | Aufbau einer Messschaltung, Einrichtung des Testwerkzeugs |
| gemeinsame Notation oder Fachsprache nötig | Schreibweise einer Tabelle, Bezeichner, Norm |
| Fehlvorstellung nach einer Vorhersage klären | die Lösung der Eingangsfrage am Fall zeigen |
| deutlicher Zeitgewinn gegenüber Selbststudium | zehn Minuten Demonstration statt 25 Minuten Lesen |

**Form**
- **Höchstens 15–20 Minuten am Stück**, danach sofort Anwendung durch die Lernenden an einem
  **anderen** Fall als dem vorgemachten (vormachen → gemeinsam → selbst).
- Eine **Rückbindungsfrage** (Abschn. 6) an die Handlungssituation und ein **gesichertes
  Ergebnis** (Merkkarte, Tafelbild, Beispieldatei) – nicht nur Zuhören.
- Im Distanzunterricht als kurzer Screencast oder Live-Impuls; die Lernenden können anhalten
  und nachfragen.
- Das Lösungsbeispiel zeigt einen **analogen** Fall, nicht die Lösung der eigenen Aufgabe.

**Nicht zulässig**
- Die **Entscheidung**, die **Überprüfung** oder die **Reflexion** der Lernenden ersetzen:
  Sie bleiben deren Leistung (Abschn. 2–4).
- Ein Unterrichtsgespräch oder einen Vortrag zur Hauptphase machen.
- Die Begründung weglassen: „weil es schneller geht“ genügt nicht, wenn die Lernenden den
  Weg selbst finden könnten und dies das Lernziel ist.

**Dokumentieren**
- In den *didaktisch-methodischen Kommentaren* der Lernsituation bzw. den Didaktischen
  Hinweisen der Lektion eine Zeile: `**Fachsystematische Phase**: … (Dauer), weil …`.
- Im Phasencheck Zeile 10 prüfen. Für Entwürfe zum Unterrichtsbesuch und Prüfungsunterricht
  gelten die Kriterien des Entwurfsbogens weiter (u. a. überwiegend aktive Lernzeit); die
  fachsystematische Phase wird dort wie gewohnt begründet (Skill `unterrichtsentwurf-erstellen`).

## Anhang: references/materialtypen.md

# Materialtypen – Bauschemata und Beispiele

## Inhalt
1. Situationsmaterial
2. Informationstext
3. Arbeitsauftrag (Kern jedes Arbeitsblatts)
4. Vorlagen: Arbeitsplan, Prüfprotokoll, Checkliste
5. Übungsaufgaben mit Lösungsweg
6. Tafelbild / Strukturbild
7. Glossar / Wortspeicher
8. Erwartungshorizont
9. Lehrerhandreichung zur Lernsituation
10. Prüfplan und Befundkarten
11. Entscheidungsmatrix mit Kosteninfo
12. Rollenkarten für Gesprächssimulation
13. Peer-Feedback-Bogen
14. Kompetenzraster und Kannliste
15. Reflexionsauftrag
16. Lastenheft und Pflichtenheft-Vorlage
17. Projektplan mit Meilensteinen
18. Projektjournal
19. Quellenmappe

Die Bauformen 10–15 tragen die Phasen Planen (Diagnose), Entscheiden, Überprüfen und
Reflektieren, die Bauformen 16–19 Projekt-Lernsituationen; die didaktischen Muster dazu stehen
in `lernsituationsmuster.md`.

---

## 1. Situationsmaterial

Macht die Handlungssituation greifbar. Formen: Kundenauftrag, Störmeldung, E-Mail der
Meisterin, Gesprächsnotiz, Auszug aus Anlagenbuch, Foto einer Schadstelle.

Bauschema: Absender/Kontext (fiktiv) · Anlass · Erwartung · Rahmenbedingungen (Zeit, Kosten,
Sicherheit) · offene Frage. Keine Lösungshinweise einbauen, die das Problem vorwegnehmen.
**Bild vor Text:** Foto der Schadstelle, Anlagenbild mit Positionsnummern oder Ausschnitt einer
Störungsanzeige zeigen, was sonst beschrieben würde; der Text bleibt bei ≤ ~150 Wörtern
(`schuelermaterial.md`).

```markdown
**Störmeldung Nr. 117** · Versand, Gurtförderer GF-2 · Meldung: Schichtleitung (fiktiv)
Seit Dienstag läuft der Gurt nach links aus, am Antrieb quietscht es. Die Kartons kommen
schräg an der Rampe an. Bitte bis Montag prüfen – maximal 2 Stunden Stillstand möglich.
```

**Behauptung oder KI-Auskunft der Kundschaft:** Die Kundin oder die Schichtleitung bringt eine
Meinung mit („Der Chatbot sagt, wir sollen den Gurt einfach nachspannen. Reicht das?"). Die
Auskunft selbst formulieren – fiktiv, teils richtig, teils unvollständig, nicht absurd falsch.
Sie öffnet im Einstieg das Problem, wird beim Überprüfen fachlich geprüft („Was stimmt, was
fehlt, was wäre die Folge?") und kann im Gespräch als Einwand zurückkommen.

## 2. Informationstext

Bauschema (eine Seite, ≤ ~300 Wörter Fließtext):
1. Überschrift als Frage oder Handlung („Wie wähle ich den richtigen Schmierstoff?")
2. Kernaussage in 1–2 Sätzen vorweg (Advance Organizer)
3. **Eine Darstellung, die den Kern trägt** (Schnittbild, Kennlinie, Vergleichstabelle,
   Ablauf) – der Text erklärt sie, nicht umgekehrt; Abbildung bzw. Platzhalter direkt an der
   Textstelle
4. Abschnitte mit Zwischenüberschriften, je ein Gedanke; Fachbegriffe **fett** bei
   Einführung, sofort erklärt
5. Tabelle/Schema statt Fließtext, wo Vergleiche oder Abläufe dargestellt werden
6. Kein Schlussresümee, das wiederholt, was eben dastand – die Kernaussage steht vorn
7. Quelle(n) – nur echte; sonst „eigene Darstellung"

Was kein Auftrag braucht, gehört nicht ins Infoblatt (Exkurse, Geschichte, „Wussten Sie
schon?“).

## 3. Arbeitsauftrag

Sechs Bestandteile:

| Bestandteil | Beispiel |
|---|---|
| Kontext | „Frau Demir will Ihre Planung vor Montag sehen." |
| Operator + Inhalt + Bedingung | „Erstellen Sie einen Arbeitsplan für die Wartung des GF-2 auf Grundlage des Wartungsplans (M1)." |
| Ergebnisform | „… in der Vorlage Arbeitsplan (M3)." |
| Sozialform + Zeit | „Tandem, 30 min" |
| Material, Darstellung, Hilfen | „Anlagenbild M2, Wartungsplan M1, Tabellenbuch; Hilfekarten am Lehrertisch" |
| Erfolgskriterien | „Sie sind fertig, wenn jeder Schritt ein Werkzeug und eine Sicherheitsmaßnahme hat und die Gesamtzeit unter 2 h liegt." |

**Offen statt kleinschrittig** (`schuelermaterial.md` Abschn. 3): Endprodukt benennen,
Lösungsweg den SuS überlassen, Schritte als gestufte Hilfen anbieten; höchstens drei
Teilaufgaben, keine Folge kurzer Einzelaufträge („Lesen Sie … Unterstreichen Sie …
Übertragen Sie …“). Der Kontext steht einmal in der Ausgangslage, nicht in jedem Auftrag – der
Auftrag selbst hat ein bis zwei Sätze. Bei Diagnoseaufgaben nennt kein Auftrag die Ursache.

**Stolperstein-Kasten (Schülerfassung):** Bei Rechen- und Verfahrensaufträgen drei bis vier
typische Fehler als Hinweis direkt am Auftrag („Achten Sie auf …"), ohne die Lösung zu verraten,
dazu ein **Kontrollwert mit Diagnosehinweis**:

```markdown
**3 Berechnen Sie,** nach wie vielen Arbeitstagen die nächste Schmierung des GF-2 fällig ist
(Intervall laut Wartungsplan: 500 Betriebsstunden; Zweischichtbetrieb). *(EA, 10 min)*

> **Stolpersteine – darauf achten!**
> - Das Intervall gilt in **Betriebsstunden**, nicht in Kalendertagen.
> - Im Zweischichtbetrieb läuft die Anlage 16 h je Arbeitstag, nicht 24 h.
>
> **Selbstkontrolle:** Ihr Ergebnis liegt zwischen 30 und 35 Arbeitstagen. Wenn nicht:
> Schichtmodell und Einheit prüfen.
```

Die Stolpersteine stammen aus den Lernhürden der Lernsituation (`lernsituationsmuster.md`
Abschn. 5); im Lehrerteil stehen Begründung und Gegenmaßnahme.

## 4. Vorlagen: Arbeitsplan, Prüfprotokoll, Checkliste

Strukturieren Planung und Dokumentation, ohne die Lösung vorzugeben.

```markdown
| Nr. | Arbeitsschritt | Werkzeug / Hilfsmittel | Sicherheitsmaßnahme | Zeit (min) | erledigt |
|---|---|---|---|---|---|
| 1 | | | | | ☐ |
```

Prüfprotokoll: Prüfmerkmal | Soll | Ist | Messmittel | i. O./n. i. O. | Maßnahme.
Bei Lernenden mit wenig Vorerfahrung erste Zeile als Beispiel ausfüllen (Lösungsbeispiel),
bei Fortgeschrittenen leer lassen.

**Betriebsdokumente** als Vorlage, wo der Beruf sie kennt: Arbeits- bzw. Servicebericht
(Tätigkeiten, Material, Arbeitszeit nach Fachkraft und Auszubildenden getrennt, „Kunde
eingewiesen: ja/nein", Unterschriften), Wartungsnachweis oder Anlagenbuch, Störungs- bzw.
Prüfbericht mit Empfehlung (Störungsbild · Prüfungen und Befunde · Ursache mit Nachweis ·
Empfehlung mit Begründung · Inbetriebnahme · Kosten und Nutzen · Hinweise für den Betreiber).
Kontaktdaten fiktiv (`example.org`, kein Telefon).

## 5. Übungsaufgaben mit Lösungsweg

- Aufsteigend: vertraute Aufgabe → Variation → Transfer in neuen Kontext → Fehleranalyse.
- Jede Rechenaufgabe vollständig lösen: Gegeben/Gesucht · Formel · Einsetzen mit Einheiten ·
  Ergebnis mit sinnvoller Rundung · Plausibilitätssatz („Die Kraft liegt im Bereich
  typischer Kleinzylinder").
- **Nachrechnen** (mit Code, wenn verfügbar) und Größenordnung prüfen.
- Lösungsbeispiel (worked example) vor die erste Übung stellen, wenn das Verfahren neu ist.
- Aufgabentext kurz; Angaben, wo möglich, als Skizze oder Tabelle statt als Textaufgabe.
- **Übungsdichte:** Zu jeder Routine genügend gleichartige Aufgaben zum Einschleifen –
  lieber eine Routine gründlich als viele Themen angetippt. Folge: gelöstes Beispiel →
  gleichartige Aufgaben steigend → eingekleidete Aufgabe aus der Handlungssituation. Am
  stärksten in einführenden Bildungsgängen (BES, BVJ, Grundstufe).

## 6. Tafelbild / Strukturbild

Sichert das Stundenergebnis in einer Struktur, die das Stundenziel spiegelt.
- Überschrift = Stundenfrage
- 3–7 Elemente, Beziehungen durch Pfeile/Tabelle
- Als Tabelle oder eingerückte Liste; als Bild ein Strukturbild bzw. Ablauf mit
  `fachdiagramm-erstellen` (Bauart `flow`, SVG) – nie als Zeichnung aus Zeichen oder Mermaid.
  Beispiel-Spec (Ablauf der Wartung mit Freigabeschleife):

```yaml
title: "Tafelbild: Vom Wartungsplan zur Übergabe"
type: flow
out: abbildungen/42_flow_tafelbild_wartung
nodes:
  plan:      { x: 0, y: 0, label: "Wartungsplan auswerten" }
  arbeit:    { x: 1, y: 0, label: "Arbeitsplan erstellen" }
  freigabe:  { x: 2, y: 0, label: "Freigabe?", shape: raute }
  wartung:   { x: 3, y: 0, label: "Wartung durchführen" }
  pruefen:   { x: 3, y: 1, label: "Funktion prüfen" }
  uebergabe: { x: 2, y: 1, label: "Übergabe mit Empfehlung" }
edges:
  - { from: plan, to: arbeit }
  - { from: arbeit, to: freigabe }
  - { from: freigabe, to: wartung, label: "ja" }
  - { from: freigabe, to: arbeit, label: "nein", route: oben }
  - { from: wartung, to: pruefen }
  - { from: pruefen, to: uebergabe }
```

## 7. Glossar / Wortspeicher

Tabelle: Fachbegriff (mit Artikel und Plural) · Erklärung in einfachen Worten · Beispiel/Bild ·
ggf. typische Verbindung („die Gurtspannung **prüfen** / **einstellen**"). Für sprachliche
Unterstützung siehe Skill `sprachsensibel-ueberarbeiten`.

Enthält die Lernsituation Beratung, Übergabe oder Einweisung von Laien, bekommt der Wortspeicher
eine Spalte **„So sage ich es der Kundin / dem Kunden"** („die Tragrolle" → „die kleinen Rollen,
auf denen das Band läuft"). Der Fachbegriff bleibt im schriftlichen Bericht.

## 8. Erwartungshorizont

| Aufgabe | Operator/AFB | Erwartete Leistung (Aspekte) | Punkte | Hinweise zur Bewertung |
|---|---|---|---|---|
| 1 | erläutern / II | (1) … (2) … | 4 (je 2) | gleichwertige Lösungen anerkennen |

- Aspekte so konkret, dass zwei Lehrkräfte gleich bewerten würden.
- Bei offenen Aufgaben Niveaustufen beschreiben (z. B. SOLO: ein Aspekt / mehrere / verknüpft
  / übertragen) statt Musterlösung.
- Punktzahl folgt dem Operator (nennen ≈ 1 je Aspekt, erläutern ≈ 2, beurteilen =
  Kriterium + Urteil + Begründung).

## 9. Lehrerhandreichung zur Lernsituation

Für Kolleginnen und Kollegen, die die Lernsituation übernehmen – gelesen **vor** der ersten
Stunde. Übernommen und verdichtet aus der `lernfeld-werkstatt`. Umfang 2–6
Seiten; kollegialer, knapper Ton; erklärt **Entscheidungen**, nicht Selbstverständliches.

| # | Abschnitt | Inhalt |
|---|---|---|
| 1 | Einordnung | Lernsituation, Stunden, Platz im Lernfeld; woran die vorige LS endet |
| 2 | Handlungssituation, Handlungsergebnis und Leitidee | Kurzfassung, zentrale Problemstellung; didaktische Leitidee der Lernsituation (1–2 Sätze, aus den didaktisch-methodischen Kommentaren – `didaktische-leitidee.md`) |
| 3 | Curricularer Bezug | Kompetenzen bzw. K-Codes dieser LS; was davon Konkretisierung ist |
| 4 | Stunden im Überblick | Tabelle: Stunde · Thema · Methodenschwerpunkt · Ergebnis · Kernweg (min) |
| 5 | Methoden und Sozialformen | wo welche Methode – **mit Begründung** |
| 6 | Material und Vorbereitung | was bereitliegen muss (Artefakte, Geräte, Räume, LMS) |
| 7 | Differenzierung | Hilfen, Zusatzaufgaben, Umgang mit sehr unterschiedlichen Betrieben |
| 8 | Bewertung | Kriterienraster im Wortlaut; Selbst-/Peer-Bewertung; ggf. Leistungsüberprüfung danach |
| 9 | Stolpersteine | Lernhürden mit Gegenmaßnahme und Ort im Material, fachliche Fehlvorstellungen, Zeitfallen |
| 10 | Erwartungsspielräume | wo mehrere Antworten richtig sind – keine Musterlösungen (die stehen im Erwartungshorizont) |
| 11 | Anschluss | was die nächste LS braucht |

Nicht hinein: Musterlösungen (→ Erwartungshorizont je Blatt), minutengenauer Verlauf
(→ Verlaufsplan), Wiederholung der Lernsituation (→ verweisen).

## 10. Prüfplan und Befundkarten

Für Diagnoseaufgaben (Muster: `lernsituationsmuster.md` Abschn. 1). Die Lernenden planen die
Prüfung selbst und erhalten Befunde nur zu geplanten Prüfschritten.

**Prüfplan (Schülerfassung):**

```markdown
| Nr. | Prüfschritt (was, womit?) | prüft Vermutung … | erwartetes Ergebnis, wenn zutreffend | Befund (Karte) |
|---|---|---|---|---|
| 1 | | | | |

Fordern Sie bei der Schichtleitung die Befunde zu Ihren Prüfschritten an. Sie erhalten nur
Befunde zu Schritten, die in Ihrem Plan stehen.
```

**Befundkarten (Lehrerfassung, zum Ausschneiden):** 8–12 Karten, je Karte die Prüfung (wie,
womit) und der Befund (Messwert oder Beobachtung), Werte passend zur Handlungssituation:

```markdown
**B3 Tragrollen Obertrum** · Prüfung: Anlage gesichert, Rollen von Hand drehen.
**Befund:** Rolle 4 links dreht sich nicht, Lauffläche einseitig abgeschliffen.

**B5 Spannstation** · Prüfung: Spannweg links und rechts messen.
**Befund:** links 6 mm kürzer als rechts.

**B8 Gurtkante** · Prüfung: Sichtprüfung über die ganze Länge.
**Befund:** Abrieb an der linken Kante auf etwa 2 m.
```

**Lehrerübersicht:** Karte | stützt | schließt aus | Hinweis (z. B. B8: falsche Fährte – Folge
des Schieflaufs, nicht seine Ursache).

Regeln:
- Keine Karte nennt die Ursache; das Befundbild ist stimmig; mindestens eine falsche Fährte.
- Ungeplante Karten bleiben liegen. Wer gründlich plant, erfährt mehr; Leistungsstarke
  begründen zusätzlich, welche Ursachen ausgeschlossen sind.
- Im LMS: Befunde erst nach Abgabe des Prüfplans freischalten (Voraussetzung der Aktivität).
- Erwartungshorizont: sinnvolle Prüfreihenfolge (einfach und zerstörungsfrei zuerst), Zuordnung
  Befund → Vermutung, Ursachenhypothese in zwei bis drei Sätzen, Wirkungskette.

## 11. Entscheidungsmatrix mit Kosteninfo

Für die Phase Entscheiden (Muster: `lernsituationsmuster.md` Abschn. 2).

```markdown
Punkte je Kriterium: 0 = gar nicht · 1 = wenig · 2 = gut · 3 = sehr gut
(bei Kosten und Stillstand: 3 = gering). Punkte × Gewicht = gewichtete Punkte.

| Maßnahme | Wirksamkeit gegen die Ursache (×3) | Sicherheit, Herstellervorgabe (×2) | Kosten (×1) | Stillstand (×1) | Summe |
|---|---|---|---|---|---|
| M1 Tragrolle tauschen, Gurt an der Spannstation gleichmäßig einstellen | | | | | |
| M2 Gurt nur nachspannen | | | | | |
| M3 Antriebslager schmieren, bei Lagerschaden tauschen | | | | | |
| M4 seitliche Führungsrollen nachrüsten | | | | | |
| M5 eigene Idee: | | | | | |

Sie dürfen die Gewichtung ändern, wenn Sie das mit den Wünschen der Schichtleitung begründen.

**Kosteninfo (Rechenannahmen für den Unterricht, keine Herstellerangaben):**
| Maßnahme | Material ca. | Arbeitszeit ca. |
|---|---|---|
| M1 | … € | … h |
Stundensatz: … €/h
```

Regeln:
- Mindestens drei Alternativen, darunter die naheliegende Symptomlösung (hier M2, M4); Platz für
  eigene Ideen.
- Ein **Nachweisauftrag** prüft die naheliegende Lösung („Prüfen Sie mit den Befunden, ob M2
  allein reicht.").
- Zielkonflikt aus der Situation sichtbar machen (Budget, höchstens 2 h Stillstand).
- Erwartungshorizont: Musterbewertung mit Summen; „andere fachlich begründete Punktwerte sind
  richtig"; Ausschlüsse benennen (welche Maßnahme nie allein reicht); **Pakete nachrechnen** –
  Summe gegen Budget und Zeitrahmen, Grenzfälle („knapp über Budget") als Gesprächsanlass
  benennen.
- Das Ergebnis geht als schriftliche Empfehlung in das Handlungsergebnis ein.

## 12. Rollenkarten für Gesprächssimulation

Für Beratung, Übergabe, Einweisung und Reklamation. Je Karte (≤ ~60 Wörter): Typ der Figur,
zwei bis drei Sätze, die sie einbringt, und ggf. eine Information, die sie nur auf gute
Nachfrage preisgibt.

| Typ | bringt ein | Beispiel (Schichtleitung Frau Demir, fiktiv) |
|---|---|---|
| sparsam | Kosten, Billiglösung | „Können wir nicht einfach nachspannen? Das kostet nichts." |
| vorinformiert | Internet, KI-Auskunft, Kollegen | „Der Chatbot sagt, Nachspannen reicht." |
| besorgt | Sicherheit, Folgen | „Ist das gefährlich für die Leute an der Rampe?" |
| planend | Zukunft, Erweiterung | „Wir verlängern das Band nächstes Jahr. Passt Ihre Lösung dann noch?" |
| eilig | Zeitdruck | „Ich habe fünf Minuten. Was muss ich wissen?" |

Regeln:
- Jeder Einwand verlangt eine fachliche Antwort aus der Lernsituation (Ursache, Kosten,
  Sicherheit, Zukunft); die Karte „planend" kann an das Additum anschließen.
- Wer die Rolle spielt, füllt danach den Beobachtungsbogen Gespräch aus
  (`assets/vorlage-bewertungsraster.md` Teil C); dann Rollenwechsel.
- Organisation im Kugellager oder im Trio (Fachkraft, Kundin, Beobachtung); Methode im
  Skill `unterrichtsentwurf-erstellen` (Methodenrepertoire).
- Üben zu Hause mit einem KI-Dialogpartner: Skill `agiles-lernen-mit-ki` (Rollenspiel), mit
  denselben Figuren.
- Redemittel und Kundensprache: Skill `sprachsensibel-ueberarbeiten`.

## 13. Peer-Feedback-Bogen

Vorlage: `assets/vorlage-bewertungsraster.md` Teil D. Bausteine: die Kriterien des Rasters als
Prüffragen, Kontrollwerte, zwei Stärken und ein nächster Schritt, Feedbackregeln und ein
**Überarbeitungsauftrag mit Zeit** („Überarbeiten Sie Ihren Bericht in 10 min und markieren Sie
die Änderungen."). Peer-Feedback ist Rückmeldung, keine Note.

## 14. Kompetenzraster und Kannliste

Selbsteinschätzung am Anfang und am Ende der Lernsituation, in zwei Formen.

**Kannliste:** je Kompetenz der Lernsituation eine Zeile in Schülersprache.

```markdown
| Ich kann … | vorher: sicher · überwiegend · eher unsicher · nicht | nachher: sicher · überwiegend · eher unsicher · nicht | Nachweis (Aufgabe, Material) |
|---|---|---|---|
| … einen Prüfplan mit Reihenfolge und erwartetem Ergebnis erstellen. | ☐ ☐ ☐ ☐ | ☐ ☐ ☐ ☐ | AB 2, Aufg. 6 |
```

**Kompetenzraster:** zwei bis vier Bereiche × drei beschreibende Stufen; Kreuz mit S (Start)
und E (Ende).

```markdown
| Bereich | Einsteiger | sicher | Expertin/Experte |
|---|---|---|---|
| Fehlersuche | Ich nenne mögliche Ursachen, wenn ich Hinweise bekomme. | Ich erstelle einen Prüfplan und werte Befunde aus. | Ich schließe Ursachen begründet aus und finde auch versteckte Fehler. |
```

Regeln:
- Zeilen aus den Kompetenzen der Lernsituation ableiten; die Spalte *Nachweis* verbindet sie mit
  den Aufgaben. Aufgaben einer Leistungsüberprüfung können sich auf dieselben Zeilen
  beziehen.
- Am Ende vergleichen (Abschn. 15).
- Die Bögen bleiben bei den Lernenden; keine Sammlung oder Auswertung je Person.

## 15. Reflexionsauftrag

Schriftlich, Einzelarbeit, 10–20 min; Fragetypen aus `lernsituationsmuster.md` Abschn. 4,
mindestens Transfer und Selbstbezug.

```markdown
**Reflexion**
a) **Transfer:** Wie gehen Sie vor, wenn der Gurt nach dem Rollentausch weiter schief läuft?
b) **Vorgehen:** Wo waren Sie bei der Fehlersuche unsicher? Was hat geholfen?
c) **Selbstbezug:** Was prüfen Sie beim nächsten Störungsauftrag als Erstes?
d) Schätzen Sie sich in der Kannliste erneut ein. Wo haben Sie sich verbessert?
```

Erwartungshorizont: Für Transferfragen fachliche Aspekte (weitere Ursachen und Prüfschritte,
z. B. Trommeln fluchten nicht, Gurtverbindung schief, einseitige Beladung); für Selbstbezug
Kriterien statt Musterlösung („nennt eine konkrete Situation und eine konkrete nächste
Handlung").

## 16. Lastenheft und Pflichtenheft-Vorlage

**Lastenheft** (Situationsmaterial des fiktiven Auftraggebers): *Was* und *wofür*, nicht *wie*.

```markdown
# Lastenheft – [Projekt] · [Auftraggeber (fiktiv)] · Version 1.0, [Datum]
1. Ausgangslage – [zwei bis vier Sätze aus Sicht des Auftraggebers]
2. Ziele – [messbar: „ganzjährige Versorgung von 4 Personen“, „Taktzeit ≤ 30 s“]
3. Randbedingungen – [Budget netto, Normen und Vorschriften, Termine, Fläche, vorhandene Anlagen]
4. Anforderungen – A) … B) … [je Anforderung ein Teil des Handlungsergebnisses; Ziel statt Technik]
5. Abnahme – [woran der Auftraggeber die Erfüllung erkennt]
6. Ansprechpersonen – [Rolle, Name (fiktiv), E-Mail @example.org; keine Telefonnummern]
```

- Jede Anforderung hat im Erwartungshorizont einen Erwartungsteil und im Bewertungsplan ein
  Kriterium; Fachkompetenzen ohne Anforderung laufen ins Leere.
- Lehrkräftehinweise („hier schulspezifische Ressourcen eintragen“) gehören nicht in die
  Fassung für Lernende.

**Pflichtenheft-Vorlage** (die Lernenden antworten): Anforderung → Lösungsidee → Begründung
(Kriterien) → Nachweis (Rechnung, Simulation, Messung) → verantwortlich → Termin.

## 17. Projektplan mit Meilensteinen

| Arbeitspaket | Ergebnis | verantwortlich | Abhängigkeit | Termin | Meilenstein-Gespräch |
|---|---|---|---|---|---|
| AP1 Lastenheft analysieren | Fragenliste, Pflichtenheft-Entwurf | [Rolle] | – | [Datum] | M1 Freigabe Pflichtenheft |

- Meilensteine = kurze Gespräche mit der Lehrkraft in einer Rolle (z. B. Projektleitung des
  Auftraggebers): Stand, Entscheidung, nächste Schritte. Sie sind Rückkopplungsschleifen im Sinne
  der Phase Entscheiden.
- Für Gruppen: Rollen (Projektleitung, Dokumentation, Fachverantwortliche je Arbeitspaket)
  wechseln je Projekt.

## 18. Projektjournal

Je Sitzung eine Zeile, je Person ausgefüllt, von der Gruppe gegengezeichnet:

| Datum | geplant | erledigt (eigener Anteil) | Entscheidung / Problem | nächster Schritt | Zeit |
|---|---|---|---|---|---|

- Grundlage für den **Einzelanteil** in der Bewertung einer Gruppenleistung und für die Reflexion.
  Nur die Lernenden selbst führen es; es wird nicht
  als Kontrollinstrument über Personen ausgewertet.

## 19. Quellenmappe

Tabelle nach `quellenbewertung.md` (falls vorhanden): Nr. · Quelle mit Fundstelle · **Typ**
(amtlich, wissenschaft, norm, verband, unternehmen, initiative, presse, sekundaer,
einzelmeinung, ki) · Interessenlage · Kernaussage · gestützt durch. Regel für Lernende: Eine
Sachaussage braucht mindestens eine Quelle ohne Interessenlage; Positionen von Verbänden und
Initiativen werden als Positionen zitiert.

## Anhang: references/operatoren-afb.md

# Operatoren, Anforderungsbereiche (AFB) und Taxonomiestufen

Arbeitsliste für berufsbildende Schulen. Die Zuordnung ist ein **Regelfall, kein Automatismus**:
Welche Stufe eine Aufgabe tatsächlich fordert, hängt vom Unterricht davor ab (Ist das
Verfahren geübt → Anwenden; ist es neu → Analysieren/Erschaffen). Ordnet ein Lehrplan,
eine Prüfungsordnung oder die Fachgruppe Operatoren anders zu, gilt deren Liste.

**Abweichende Liste im Beruflichen Gymnasium (Abitur, Klausuren der Qualifikationsphase):** Dort
gelten die Operatoren der EPA Technik mit eigener AFB-Zuordnung (`operatoren-epa-technik.md`, falls vorhanden).
Wichtigste Unterschiede: *begründen* nur AFB II, *dokumentieren* AFB III, *beschreiben* und
*nennen* nur AFB I; *erstellen*, *programmieren*, *implementieren*, *testen* sind keine
EPA-Operatoren (dort *entwickeln*, *entwerfen*, *überprüfen* verwenden oder als erweiterte
Operatoren im Lehrermaterial ausweisen).
**Im Fach Berufliche Informatik** gilt die EPA Berufliche Informatik mit eigener Liste (dort sind
*erstellen*, *implementieren*, *testen*, *erweitern*, *vervollständigen* Operatoren; Abschnitt
*Berufliche Informatik* in `operatoren-epa-technik.md`, falls vorhanden).

Spalten: **AFB** = Anforderungsbereich I (Reproduktion), II (Reorganisation und Transfer),
III (Reflexion und Problemlösung). **Bloom** = Stufe der revidierten Taxonomie nach
Anderson/Krathwohl (1 Erinnern · 2 Verstehen · 3 Anwenden · 4 Analysieren · 5 Bewerten ·
6 Erschaffen).

## AFB I – Reproduktion

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| nennen, angeben, aufzählen | Begriffe, Daten, Fakten ohne Erläuterung wiedergeben | 1 |
| bezeichnen, benennen | Bauteile, Größen, Symbole korrekt mit Fachbegriff versehen | 1 |
| wiedergeben | Inhalte sachlich zutreffend in eigenen Worten formulieren | 1–2 |
| beschreiben | Sachverhalt, Ablauf oder Aufbau strukturiert und fachsprachlich wiedergeben | 2 |
| darstellen | Zusammenhänge geordnet wiedergeben, auch grafisch (Skizze, Tabelle, Schema) | 2 |
| zusammenfassen | Kernaussagen komprimiert und strukturiert wiedergeben | 2 |
| skizzieren | Wesentliches vereinfacht grafisch oder in Stichpunkten darstellen | 2 |

## AFB II – Reorganisation und Transfer

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| erklären | Ursache–Wirkung bzw. Funktionsweise nachvollziehbar machen | 2 |
| erläutern | Sachverhalt beschreiben **und** durch Zusatzinformationen/Beispiele verständlich machen | 2–3 |
| zuordnen, einordnen | Sachverhalte begründet in einen Zusammenhang oder eine Systematik stellen | 2–3 |
| anwenden | Bekanntes Verfahren auf einen neuen, ähnlichen Fall übertragen | 3 |
| berechnen, bestimmen, ermitteln | Ergebnis mit nachvollziehbarem Lösungsweg und Einheiten gewinnen | 3 |
| auswählen | aus Alternativen kriteriengeleitet das Passende festlegen (Tabellenbuch, Katalog, Datenblatt) | 3–4 |
| erstellen, anfertigen | Produkt nach Vorgaben anfertigen (Schaltplan, Arbeitsplan, Prüfprotokoll, Stückliste) | 3 |
| durchführen | Verfahren, Messung, Prüfung fachgerecht ausführen und dokumentieren | 3 |
| auswerten | Daten, Messwerte, Diagramme interpretieren und Schlüsse ziehen | 4 |
| analysieren, untersuchen | Bestandteile, Strukturen, Fehlerursachen systematisch herausarbeiten | 4 |
| vergleichen, gegenüberstellen | Gemeinsamkeiten und Unterschiede kriteriengeleitet herausarbeiten | 4 |
| herausarbeiten | aus Material bestimmte Sachverhalte erkennen und darstellen | 4 |
| ableiten | aus Gegebenem begründet eine Folgerung oder Größe gewinnen | 4 |
| modellieren | Sachverhalt in ein Modell überführen (Ablaufplan, GRAFCET, Struktogramm, Ersatzschaltbild) | 4–6 |
| implementieren, programmieren | Modell/Konzept in einer konkreten Umgebung lauffähig umsetzen | 3–6 |

## AFB III – Reflexion und Problemlösung

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| prüfen, überprüfen | Aussagen, Ergebnisse oder Lösungen an Kriterien/Normen messen und Abweichungen begründen | 5 |
| beurteilen | zu einem Sachverhalt ein begründetes **Sachurteil** nach Kriterien fällen | 5 |
| bewerten | wie beurteilen, zusätzlich mit begründetem eigenem Standpunkt bzw. Wertmaßstab | 5 |
| begründen | Aussage oder Entscheidung durch Argumente und Fachwissen stützen | 4–5 |
| Stellung nehmen, erörtern, diskutieren | Argumente abwägen und zu einem begründeten Ergebnis kommen | 5 |
| reflektieren | eigenes Vorgehen/Ergebnis kriteriengeleitet kritisch prüfen, Konsequenzen ableiten | 5 |
| entwickeln, entwerfen, konzipieren | für ein neues Problem eine eigenständige Lösung erarbeiten | 6 |
| gestalten | eigenständig und kreativ eine Lösung oder ein Produkt ausformen | 6 |
| optimieren | bestehende Lösung begründet verbessern (Kosten, Sicherheit, Energie, Qualität) | 5–6 |
| planen (offen) | Vorgehen für eine offene Problemstellung eigenständig festlegen | 6 |

## Berufspraktische Operatoren in schriftlichen Aufträgen

Für Aufträge, die eine berufliche Handlung vorbereiten, dokumentieren oder kommunizieren. Der
AFB hängt davon ab, ob Form und Verfahren vorgegeben sind (I–II) oder selbst gewählt und
begründet werden müssen (II–III).

| Operator | Erwartete Leistung | AFB | Bloom |
|---|---|---|---|
| berichtigen | falsche Aussage erkennen und fachlich richtigstellen | I–II | 2–3 |
| dokumentieren, protokollieren | Vorgehen, Messwerte und Ergebnisse vollständig und nachvollziehbar festhalten | I–II | 2–3 |
| messen | Größe mit geeignetem Messmittel bestimmen, Messwert mit Einheit angeben | I–II | 3 |
| formulieren, verfassen | adressatengerechten Text verfassen (Kundeninformation, E-Mail, Übergabenotiz) | II | 3 |
| präsentieren | Ergebnis adressatengerecht, strukturiert und fachsprachlich vorstellen | II | 3–4 |
| simulieren | Verhalten eines Systems mit Software oder Modell nachbilden und die Ergebnisse deuten | II | 3–4 |
| experimentieren, einen Versuch durchführen | nach Plan messen, beobachten, dokumentieren und Sicherheitsregeln einhalten | II | 3 |
| eine Hypothese aufstellen, formulieren | eine prüfbare Vermutung mit Begründung formulieren | III | 6 |
| nachweisen | rechnerisch oder experimentell zeigen, dass eine Anforderung erfüllt ist | II–III | 4–5 |

## Wissensarten und Anforderungsbereiche

| Wissensart | Leitfrage | typischer AFB |
|---|---|---|
| Sachwissen | Was muss man kennen? | I – nennen, beschreiben, zuordnen |
| Prozesswissen | Wie geht man vor? | II – anwenden, durchführen, erstellen, analysieren |
| Reflexionswissen | Warum so, mit welcher Wirkung? | III – beurteilen, bewerten, begründen, entwickeln |

Material und Prüfungen sollten über Sachwissen hinausgehen: kein Arbeitsblatt nur mit AFB I,
kein erster Auftrag auf AFB III. Verteilungen werden **ausgezählt**, nicht geschätzt.

## Praktische Operatoren (Werkstatt, Labor) – psychomotorische Stufen nach Dave

| Operator (Beispiele) | Stufe nach Dave (1970) |
|---|---|
| nachmachen, unter Anleitung ausführen | 1 Imitation |
| nach Anleitung montieren, einstellen, messen | 2 Manipulation |
| genau, sicher und ohne Hilfe fertigen, prüfen, justieren | 3 Präzision |
| mehrere Arbeitsschritte koordiniert ausführen, Abläufe kombinieren, in Betrieb nehmen | 4 Handlungsgliederung |
| routiniert, situationsangepasst und effizient arbeiten, instand setzen unter Zeitdruck | 5 Naturalisierung |

## Verben für Personale Kompetenz (SchuCu-BBS)

Sozialkompetenz: *stimmen sich ab, wirken mit, beraten, präsentieren adressatengerecht,
geben und nehmen Rückmeldung, übernehmen Verantwortung im Team, vertreten Ergebnisse,
lösen Konflikte sachlich*.
Selbständigkeit: *planen ihr Vorgehen eigenständig, schätzen ein, reflektieren, handeln in
Verantwortung, setzen sich selbstkritisch auseinander, identifizieren Verbesserungspotenziale,
wählen Lernhilfen aus, beachten Arbeitssicherheit eigenverantwortlich*.

## Nicht verwenden (nicht beobachtbar)

*verstehen, kennen, wissen, lernen, begreifen, sich bewusst sein, vertraut sein mit,
Einblick gewinnen, die Bereitschaft entwickeln, die Fähigkeit verbessern*. Ersatz: Was tun die SuS sichtbar, **woran** erkennt man es?

## Faustregeln für Aufgaben

- **Operator + Inhalt + Bedingung:** „Berechnen Sie die erforderliche Kolbenkraft **für
  den Ausschiebezylinder** unter Berücksichtigung eines Wirkungsgrads von 0,85."
- Keine W-Fragen („Was ist …?") in Aufgaben – immer einen Operator.
- Pro Teilaufgabe **ein** Operator; Mehrfachoperatoren („nennen und erläutern") nur, wenn
  beide Leistungen bewertet werden.
- Der Operator legt die Bewertung mit fest: nennen ≈ 1 Punkt je Aspekt, erläutern ≈ 2 Punkte
  je Aspekt, beurteilen = Kriterium + Urteil + Begründung.

## Anhang: references/quellenbewertung.md

# Quellen bewerten – Typ, Interessenlage, Belegkraft

Für Lehrkräfte (Material prüfen) und für Lernende (Quellenmappe, Technikfolgenabschätzung,
Recherche). Ergänzt die Quellenhierarchie im Faktencheck (`faktencheck-methode.md`, nur in
`material-pruefen`): Diese fragt *wie verlässlich*, die Quellenbewertung fragt zusätzlich
*wer spricht mit welchem Interesse*.

## 1. Quellentypen (Kürzel verbindlich für Quellenmappen und `tfa_pruefen.py`)

| Kürzel | Typ | Beispiele | Interessenlage | Belegkraft für Sachaussagen |
|---|---|---|---|---|
| `amtlich` | Gesetz, Verordnung, Behörde, amtliche Statistik | Gesetze im Internet, Umweltbundesamt, Bundesamt für Strahlenschutz, BSI, Destatis | gering (staatlicher Auftrag) | hoch |
| `wissenschaft` | begutachtete Studie, Forschungsinstitut, Hochschule | Fachzeitschrift mit Peer-Review, Fraunhofer, KIT-ITAS | gering bis mittel (Auftraggeber prüfen) | hoch |
| `norm` | Norm, technische Regel, Richtlinie | DIN/EN/ISO, VDI-Richtlinie, DGUV-Regel | gering | hoch (Inhalt nur im Normtext) |
| `verband` | Branchen- oder Fachverband, Kammer | Bundesverband WindEnergie, Bundesverband Ziegel, VDZ | **ja** (Branche) | mittel – Zahlen oft korrekt, Auswahl und Deutung interessengeleitet |
| `unternehmen` | Hersteller, Betreiber, Dienstleister | Herstellerdatenblatt, Unternehmensbroschüre | **ja** (Verkauf) | mittel – für eigene Produktdaten hoch, für Vergleiche niedrig |
| `initiative` | NGO, Bürgerinitiative, Lobbyorganisation | Umweltverband, Bürgerinitiative gegen …, Verbraucherorganisation | **ja** (Anliegen) | mittel bis niedrig – Positionen, keine neutrale Datenbasis |
| `presse` | Qualitätsjournalismus, Fachpresse | Tageszeitung, öffentlich-rechtlicher Rundfunk, Fachmagazin | gering bis mittel | mittel – als Hinweis, Primärquelle suchen |
| `sekundaer` | Lexikon, Lehrbuch, Fachportal, Tutorial | Wikipedia, Tabellenbuch, Fachportal | gering | mittel – Einstieg, kein Beleg für Grenzwerte |
| `einzelmeinung` | Blog, Streitschrift, Video einer Einzelperson, Social Media | privater Blog, Reader „… schwere Schäden!“ | **ja** oder unbekannt | niedrig |
| `ki` | KI-generierter Text | Chatbot-Auskunft, KI-erstelltes Transkript | unbekannt | **kein Beleg** – nur Material zum Prüfen |

**Regeln:**
- **Interessengeleitete Quellen** (`verband`, `unternehmen`, `initiative`, `einzelmeinung`)
  sind erlaubt und für Kontroversen sogar nötig. Sie werden als Position gekennzeichnet und
  **nie als einziger Beleg** einer Sachaussage verwendet; daneben steht mindestens eine Quelle
  vom Typ `amtlich`, `wissenschaft` oder `norm`.
- **Desinformation** oder wissenschaftlich widerlegte Aussagen nur als ausdrücklich
  gekennzeichneter **Analysegegenstand** („Prüfen Sie diese Behauptung“), nie als Information.
- **KI-Text** ist nie Beleg. Ein KI-erstelltes Muster (z. B. Rollenspieltranskript) wird wie
  ein Erwartungshorizont fachlich geprüft und gekennzeichnet.
- Für sicherheitsrelevante Werte nur `amtlich`, `norm` oder Herstellerangabe zum konkreten
  Produkt.

## 2. Prüffragen je Quelle (für Lernende)

1. **Wer** steht dahinter (Impressum, Herausgeber, Finanzierung)?
2. **Welches Interesse** könnte die Darstellung prägen?
3. **Wann** erschienen, noch aktuell?
4. **Worauf** stützt sich die Aussage (Daten, Studie, Meinung)? Ist die Originalquelle
   auffindbar?
5. **Was sagen andere** verlässliche Quellen? (lateral lesen)

## 3. Quellenmappe – Format

| Nr. | Quelle (Titel, Herausgeber, Jahr, URL bzw. Fundstelle) | Typ | Interessenlage | Kernaussage | gestützt durch |
|---|---|---|---|---|---|
| Q1 | UBA (2021): Ökobilanzen Windenergie und Photovoltaik, Kap. 7 | amtlich | gering | energetische Amortisation unter einem Jahr | – |
| Q2 | Branchenverband (Jahr): Hintergrundpapier Ökobilanz | verband | Branche Windenergie | 30- bis 40-fache Energierückgewinnung | Q1 |

Die Spalte *Typ* enthält genau ein Kürzel aus Abschn. 1.

## 4. Typische Fehler in Material und Schülerprodukten

- Branchen- oder Aktivistenpapier als neutraler Beleg zitiert.
- Linktext widerspricht dem Inhalt (Titel „Gefahr …“, Seite „Entwarnung …“).
- Lange wörtliche Übernahmen ohne Belegfunktion (Zitatrecht: nur so viel wie nötig, mit Quelle).
- Zahl ohne Quelle und ohne Definition („Netzzugänge stiegen von … auf …“).
- KI-Text mit erfundenen Studien („Laut einer Studie des Instituts X … bis zu 15 %“).

## Anhang: references/schucu-bbs-2024.md

# SchuCu-BBS 2024 – Kompaktreferenz

Quelle: Niedersächsisches Kultusministerium, *Leitlinie Schulisches Curriculum berufsbildende
Schulen (SchuCu-BBS) 2024*, Stand Juli 2024; ergänzend die unverbindliche „Leermaske für
Lernsituationen" (NLQ, Stand 08/2023) und der Analysebogen für Lernsituationen.
Wortlaute in Anführungszeichen sind der Leitlinie entnommen.

## Inhalt
1. Handlungskompetenz
2. Vollständige Handlung (6 Phasen) und Rolle der Lehrkraft
3. Bestandteile einer Lernsituation
4. Anforderungen an die Handlungssituation
5. Analysebogen (16 Kriterien)
6. Schulisches Curriculum: Planungsablauf
7. Begriffswechsel gegenüber älteren Vorlagen

---

## 1. Handlungskompetenz

- „Ziel des handlungsorientierten Unterrichts ist die Entwicklung von Handlungskompetenz" –
  im berufsbezogenen **und** berufsübergreifenden Lernbereich.
- Handlungskompetenz entfaltet sich laut DQR in den Dimensionen
  - **Fachkompetenz** = Wissen und Fertigkeiten
  - **Personale Kompetenz** = Sozialkompetenz und Selbständigkeit
- „In Handlungskompetenz sind Kommunikations-, Methoden-, Lern- und Medienkompetenz
  immanent." → Sie werden **nicht als eigene Spalte** ausgewiesen, sondern in Fach- bzw.
  Personaler Kompetenz mitformuliert.
- Kompetenzen werden **aktiv** beschrieben: „Die Schülerinnen und Schüler … erfassen …,
  planen …, analysieren und beheben …". Für Personale Kompetenz eignen sich Verben wie
  *begründen, wirken mit, gestalten, schätzen ein, handeln in Verantwortung, reflektieren,
  setzen sich (selbst)kritisch auseinander, identifizieren Verbesserungspotenziale*.

## 2. Vollständige Handlung und Rolle der Lehrkraft

Die Phasen „können je nach Kompetenz der Schülerinnen und Schüler unterschiedlich ausgedehnt
und gewichtet sein", sind nicht immer trennscharf; Üben und Wiederholen ist in jeder Phase
möglich. Fachgruppen dürfen fachdidaktische Vorgehensweisen ausweisen.

| Phase | Leitfrage | Was die SuS tun | Typische Aufgaben der Lehrkraft |
|---|---|---|---|
| **Informieren bzw. Analysieren** | Was soll getan werden? | erfassen und analysieren die zentrale Aufgaben-, Frage- bzw. Problemstellung der Handlungssituation | SuS in die Situation versetzen, selbstgesteuerte Lernprozesse initiieren, Materialien bereitstellen (impulsgebende Rolle) |
| **Planen** | Wie kann die Umsetzung erfolgen? | planen Vorgehen und Dokumentation, beschaffen Informationen, erstellen Arbeits- und Zeitplan, schlagen Handlungsergebnisse vor, legen Kontrollkriterien fest | kooperative Lernprozesse fördern, Vorwissen aktivieren, ggf. weiteres Material bereitstellen |
| **Entscheiden** | Welcher Lösungsweg wird gewählt? | entscheiden sich für Lösungsweg(e), legen Handlungsergebnis, Vorgehen, Rückkopplungsschleifen, Zeitrahmen, Verantwortlichkeiten und Einschätzungskriterien fest | Rückmeldung geben, Fragen beantworten, Entscheidungsprozesse moderieren |
| **Durchführen** | Der gewählte Lösungsweg wird umgesetzt. | bearbeiten die Problemstellung gemäß Entscheidung, berücksichtigen sich ändernde Rahmenbedingungen | Hilfestellungen geben, Materialien/Medien bereitstellen, Unterrichtszeit effizient nutzen, Handlungsergebnis sichern |
| **Überprüfen bzw. Kontrollieren** | Ist das Handlungsergebnis sach- und fachgerecht? | überprüfen das Ergebnis gemäß festgelegten Kriterien, schätzen seine Eignung als Lösung ein | Gesprächsanlässe schaffen, Rückmeldung nach Beurteilungskriterien, Hinweise zur Gewichtung in der Leistungsbewertung |
| **Reflektieren** | Was kann zukünftig verbessert werden? | reflektieren die Bearbeitung, identifizieren Stärken und Verbesserungspotenziale von Lernprozess und Ergebnis | individuelle Reflexion anleiten, mehrperspektivische Unterrichtsbeobachtung nutzen (UB-BBS im Portal PIE-BBS) |

Die Lehrkraft wechselt zwischen **informierender, moderierender, impulsgebender, beratender
und bewertender** Rolle. Lernumgebung: kognitives (Kopf), affektives (Herz) und
psychomotorisches (Hand) Lernen; Ausstattung muss Wechsel von Methoden, Medien und
Sozialformen zulassen. Leistungsbewertung nach „verbindlichen und offengelegten Kriterien".

*Hinweis der Bibliothek (keine Aussage der Leitlinie; Entscheidung der Fachberatung, 23.10.2026):*
Die Leitlinie lässt zu, dass der Handlungskreis mehrere Unterrichtseinheiten umfasst: Die
Phasen „können je nach Kompetenz der Schülerinnen und Schüler unterschiedlich ausgedehnt und
gewichtet sein“, der Zeitrichtwert einer Lernsituation ist die **Summe** der eingeplanten
Stunden, und eine Lernsituation „kann fachsystematische Lernphasen enthalten“. Die Lehrkraft
wechselt auch in die informierende Rolle und soll „Unterrichtszeit effizient nutzen“. Daraus
folgt für die Bibliothek: Der Kreis wird **je Lernsituation** geschlossen, nicht je 90-Minuten-
Einheit; fachsystematische, lehrkraftgeführte Phasen sind zulässig, wenn sie zweckdienlich und
begründet sind und an die Handlungssituation zurückgebunden werden
(`lernsituationsmuster.md` Abschn. 12, falls vorhanden).

## 3. Bestandteile einer Lernsituation

| Element | Anforderung laut Leitlinie |
|---|---|
| **Curriculare Vorgaben** | ausweisen: RRL, RLP (Lernfeld/Lerngebiet/Modul/Qualifizierungsbaustein **mit Titel**), KC |
| **Titel** | „kurz, prägnant und beschreibt die Handlung" (Leermaske: kompetenzorientiert, z. B. „Beton herstellen", „Going green") |
| **Zeitrichtwert** | Summe der eingeplanten Unterrichtsstunden; Bezugspunkt ist der Zeitrichtwert der curricularen Vorgabe |
| **Handlungskompetenz** | Fachkompetenz und Personale Kompetenz konkretisiert (Aktualität, Komplexität, Bearbeitungstiefe, regionale Spezifika); **Inhalte** erschließen sich aus den Kompetenzen und können gesondert ausgewiesen werden |
| **Handlungssituation** | **genau eine pro Lernsituation**; Kern der Lernsituation (Anforderungen s. Abschn. 4) |
| **Handlungsergebnis** | mögliche Lösung der zentralen Aufgaben-, Frage- bzw. Problemstellung; materiell oder nicht-materiell (digitales Produkt, Werkstück, Handlungskonzept, Stellungnahme, Pro-und-Kontra-Diskussion, Beratungsgespräch …); finale Festlegung je nach Kompetenzniveau durch SuS, ggf. Lehrkraft |
| **Vereinbarungen und Hinweise zur Umsetzung** | dokumentieren: didaktisch-methodische Kommentare, Distanzunterricht, Leistungsfeststellung und -bewertung, Materialien, ergänzende Quellen, Lernumgebung |

Eine Lernsituation „kann fachsystematische Lernphasen enthalten", um den Lernprozess zu
unterstützen. Die Handlungssituation darf für die SuS „inhaltlich-sprachlich" angepasst
werden.

## 4. Anforderungen an die Handlungssituation

Die Handlungssituation …
1. initiiert und trägt einen Lernprozess über die **gesamte** Lernsituation,
2. ist bedeutsam – berufsbezogen für die Berufsausübung und/oder Lebenswelt, berufsübergreifend
   für die Lebenswelt und/oder Berufsausübung (ggf. inkl. Studienorientierung),
3. greift mögliche berufliche, persönliche oder gesellschaftliche Erfahrungen der SuS auf,
4. wirft **eine zentrale** Aufgaben-, Frage- bzw. Problemstellung auf,
5. ist exemplarisch,
6. benennt den Rahmen (Modellunternehmen, Einrichtung, Praxis, technisches System, Fall,
   Szenario, reale Situation),
7. berücksichtigt in der Regel soziale Interaktion (Beratungsgespräch, Zusammenarbeit mit
   anderen Auszubildenden …),
8. ermöglicht verschiedene, nach Möglichkeit **offene** Bearbeitungs- bzw. Lösungswege.

*Hinweis der Bibliothek (keine Aussage der Leitlinie):* In vollzeitschulischen Bildungsgängen,
besonders im **Beruflichen Gymnasium**, liest sich Anforderung 2 auch als Studienorientierung
und wissenschaftspropädeutischer Anspruch; Anforderung 7 meint dort Zusammenarbeit in der
Projektgruppe, mit fiktiven Auftraggebern, Expertinnen und Experten oder Stakeholdern
(`berufliches-gymnasium.md`, falls vorhanden).

## 5. Analysebogen für Lernsituationen (16 Kriterien)

Skala: trifft zu · trifft eher zu · trifft eher nicht zu · trifft nicht zu.

**Handlungskompetenz**
1. Die Kompetenzen leiten sich aus den curricularen Vorgaben ab.
2. Die Personale Kompetenz ist konkretisiert (Aktualität, Komplexität, Bearbeitungstiefe,
   regionale Spezifika).
3. Die Fachkompetenz ist konkretisiert (ebenso).
4. Die Inhalte leiten sich aus den curricularen Vorgaben ab.
5. Die Inhalte sind analysiert (Aktualität, Komplexität, Bearbeitungstiefe, regionale
   Spezifika).

**Handlungssituation**
6. initiiert einen Lernprozess.
7. trägt einen Lernprozess über die gesamte Lernsituation.
8. ist für die Berufsausübung und/oder die Lebenswelt der SuS bedeutsam (Lernbereich angeben:
   berufsbezogen/berufsübergreifend). *(BG: Profilfach = berufsbezogener Lernbereich; Studienorientierung mitbewerten.)*
9. greift mögliche berufliche, persönliche und/oder gesellschaftliche Erfahrungen auf.
10. wirft eine zentrale Aufgaben-, Frage- bzw. Problemstellung auf.
11. ist exemplarisch.
12. benennt den Rahmen.
13. berücksichtigt soziale Interaktion.
14. ermöglicht verschiedene und nach Möglichkeit offene Bearbeitungs- bzw. Lösungswege.

**Handlungsergebnis**
15. Das mögliche Handlungsergebnis stellt eine Lösung einer zentralen Aufgaben-, Frage- bzw.
    Problemstellung dar.

**Vereinbarungen und Hinweise zur Umsetzung**
16. Vereinbarungen und Hinweise zur Umsetzung der Lernsituation sind vollständig dokumentiert.

## 6. Schulisches Curriculum: Planungsablauf

Schulisches Curriculum = **didaktisch-methodische Planung** + **Jahresplanung**; Aufgabe
aller im Bildungsgang tätigen Lehrkräfte.

1. Schulspezifische Entscheidungen und Vorgaben berücksichtigen (z. B. Blockmodell,
   Lernumgebung, Präsenz/Distanz, Grundsätze der Leistungsbewertung, Lernortkooperation).
2. Curriculare Vorgaben analysieren (Lerngebiete, Lernfelder, Module, Qualifizierungsbausteine).
3. Inhaltliche Abstimmung über alle Lernsituationen: Titel skizzieren, Personale Kompetenzen,
   Fachkompetenzen und Inhalte zuordnen, Handlungssituationen skizzieren, Zeitrichtwerte
   schätzen, Überschneidungen erfassen, Reihenfolge und Parallelität festlegen, Einführung
   und Vertiefung von Lern- und Arbeitstechniken abstimmen.
4. Lernsituationen planen und dokumentieren (ggf. didaktische Reduktion, Exemplarität);
   **Bildungsgangbeschluss** dokumentieren, bevor Materialien ausgestaltet werden.
5. Materialien und Medien gemeinsam entwickeln bzw. beschaffen, regelmäßig evaluieren.
6. Jahresplanung: zeitliche Reihenfolge, organisatorische Vereinbarungen (Prüfungstermine,
   Praktika …), jährlich anpassen und kommunizieren.
7. Unterricht durchführen und evaluieren (z. B. Instrumente aus PIE-BBS); Curriculum
   regelmäßig überprüfen.

Einordnung in das Qualitätsmanagement: Kernaufgabenmodell KAM-BBS, Qualitätsbereich B
„Bildungsangebote gestalten".

## 7. Begriffswechsel gegenüber älteren Vorlagen

| Ältere Vorlagen / andere Länder | SchuCu-BBS 2024 |
|---|---|
| Handlungsprodukt, Lernergebnis | **Handlungsergebnis** (materiell oder nicht-materiell) |
| Einstiegsszenario, Lernsituationsbeschreibung | **Handlungssituation** (eine pro LS) |
| Selbstkompetenz, Humankompetenz | **Selbständigkeit** (Teil der Personalen Kompetenz) |
| Methoden-/Lernkompetenz als eigene Spalte | immanent in Fach- und Personaler Kompetenz |
| vier Dimensionen Fach-, Methoden-, Sozial-, Selbstkompetenz (KMK-Raster) | **Fachkompetenz** (Wissen, Fertigkeiten) und **Personale Kompetenz** (Sozialkompetenz, Selbständigkeit); Methodenkompetenz wird eingebettet |
| Phasen „Ausführen" und „Bewerten/Reflektieren" | **Durchführen** bzw. **Reflektieren** (Bewertungsanteile ggf. unter Überprüfen bzw. Kontrollieren) |
| Felder „Leistungsbewertung", „Differenzierung", „Anknüpfung LMS/Moodle", „Material & Medien" | unter **Vereinbarungen und Hinweise** (Leistungsfeststellung und -bewertung · didaktisch-methodische Kommentare · Lernumgebung · Materialien und Quellen) |
| 7 Phasen: (Problem-)Analyse, Information, Planung, Entscheidung, Ausführung, Kontrolle/Bewertung, Reflexion/Transfer | **6 Phasen**: Informieren bzw. Analysieren, Planen, Entscheiden, Durchführen, Überprüfen bzw. Kontrollieren, Reflektieren |
| Lern- und Arbeitstechniken, Unterrichtsmaterialien/Fundstelle, organisatorische Hinweise (je eigenes Feld) | gebündelt unter **Vereinbarungen und Hinweise zur Umsetzung der Lernsituation** |
| nur Präsenzunterricht | **Präsenz- und Distanzunterricht** mitdenken |

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.

## Inhalt
1. Vier Regeln
2. Darstellungen statt Text
3. Aufträge offen statt kleinschrittig
4. Was entfällt
5. Richtwerte
6. Rückwärtsprobe vor der Ausgabe

## 1. Vier Regeln

1. **Kurz.** Lernende lesen nur, was sie für den Auftrag brauchen. Kein Satz ohne Aufgabe,
   keine Wiederholung, kein Exkurs.
2. **Offen gestellt.** Ein Auftrag nennt Ziel (Operator), Gegenstand, Ergebnisform und woran
   man merkt, dass man fertig ist. Den Weg finden die Lernenden; Schritte und Gerüste stehen in
   gestuften Hilfen, die man bei Bedarf zieht.
3. **Anschaulich.** Aufgaben arbeiten mit Zeichnungen, Darstellungen und Grafiken: ablesen,
   auswerten, ergänzen, Fehler finden, selbst zeichnen. Was eine Darstellung zeigt, wird nicht
   zusätzlich beschrieben.
4. **Ohne Dekoration.** Nur, was dem Ziel dient (Abschn. 4).

Gekürzt wird Überflüssiges, nicht Fachinhalt: Fachbegriffe, Sicherheitshinweise und
Erfolgskriterien bleiben vollständig.

## 2. Darstellungen statt Text

| Inhalt | Darstellung | so entsteht sie |
|---|---|---|
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen` |
| System, Energie- und Datenfluss, Regelkreis | Blockschaltbild | `fachdiagramm-erstellen` |
| Zusammenhang zweier Größen | Diagramm, Kennlinie mit beschrifteten Achsen | aus gerechneten Werten oder dem Datenblatt als SVG erzeugen (Code), nie geschätzt |
| Vergleich, Kriterien, Kenndaten | Tabelle, Matrix | Markdown-Tabelle |
| Begriffe und ihre Beziehungen | Strukturbild | `fachdiagramm-erstellen` (Bauart `flow`), Tabelle |
| Daten und Software | ER-, Klassen-, Sequenzdiagramm | `fachdiagramm-erstellen` |
| Schaltung, Werkstück | Schaltplan, technische Zeichnung nach Norm | Herstellerunterlage, Tabellenbuch, eigene Zeichnung (Platzhalter mit Quelle) |

Jede Zeichnung entsteht als **SVG aus einer Spec** – nie als Zeichnung aus Zeichen (ASCII-Art) und
nie als Mermaid in der Ausgabe (Skill-Vertrag Abschn. 3).

**Die Darstellung ist Arbeitsgegenstand, nicht Beigabe.** Aufträge, die mit ihr arbeiten
(Beispiele am Gurtförderer GF-2, fiktiv):

| Auftrag | Beispiel |
|---|---|
| ablesen, auswerten | „Ermitteln Sie aus der Kennlinie die Drehzahl bei 80 % Last.“ |
| ergänzen | „Benennen Sie im Anlagenbild die Bauteile ① bis ④.“ |
| Fehler finden | „Der Arbeitsplan in Abb. 2 enthält zwei Fehler. Berichtigen Sie sie.“ |
| selbst zeichnen | „Skizzieren Sie, wie die Spannstation verstellt werden muss.“ |
| vergleichen | „Vergleichen Sie die Gurtlaufbilder A und B.“ |

Regeln:
- **Am Auftrag:** Abbildung direkt bei dem Auftrag, der sie braucht; Beschriftung in die
  Abbildung, Positionsnummern statt Legendentext, wo möglich.
- **Fachlich richtig und normgerecht:** Schaltzeichen, Kennzeichen und Formelzeichen nach
  Norm; Werte hinter Diagrammen sind gerechnet.
- **Schwarzweiß lesbar:** Farbe nur mit Bedeutung und nie allein (zusätzlich Linienart oder
  Beschriftung).
- **Nie erfinden:** keine KI-Bilder, die Fotos, echte Anlagen oder Messkurven vortäuschen. Was
  nicht selbst gezeichnet werden kann (Foto, Herstellerzeichnung, Normauszug), steht als
  Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz]` und ist ein Prüfauftrag.
- **Barrierearm:** Alternativtext (ein Satz) je Abbildung.
- **Platz für Zeichnungen der Lernenden:** in der Druckfassung Kasten oder Raster statt Linien.

Nicht jede Aufgabe braucht ein Bild (Begründung, Gespräch, Reflexion). Ein Arbeitsblatt oder
Infoblatt ganz ohne Darstellung ist aber zu begründen.

## 3. Aufträge offen statt kleinschrittig

**Kleinschrittig – so nicht:**

> 1. Lesen Sie den Wartungsplan (M1).
> 2. Unterstreichen Sie alle Arbeiten, die nach 500 Betriebsstunden fällig sind.
> 3. Übertragen Sie die Arbeiten in die erste Spalte der Tabelle.
> 4. Ergänzen Sie in der zweiten Spalte das Werkzeug.
> 5. Ergänzen Sie in der dritten Spalte die Sicherheitsmaßnahme.
> 6. Addieren Sie die Zeiten.

**Offen – so:**

> **1 Erstellen Sie** den Arbeitsplan für die 500-h-Wartung des GF-2 (Wartungsplan M1,
> Vorlage M3). Fertig, wenn jeder Schritt Werkzeug und Sicherheitsmaßnahme hat und die
> Gesamtzeit unter 2 h liegt.

Die Schritte stehen – kürzer – in den gestuften Hilfen (Impuls → Strategie → Teilschritt →
Kontrolle; Skill `differenzierung-erstellen`). Wer sie braucht, zieht sie. Formate mit weniger
Stufen ordnen zu: Lernlandkarte – Kontrolle ist der Selbstcheck des Lernpostens; Lektion –
Orientierung, Werkzeug, Gerüst entsprechen Impuls, Strategie, Teilschritt, die Kontrolle leisten
Realitätstest und Rückmeldung.

Signale für Kleinschrittigkeit:
- mehr als drei Teilaufgaben a), b), c) an einem Auftrag;
- eine Schrittfolge im Auftrag, die den Lösungsweg vorgibt („zunächst …, dann …,
  anschließend …“) oder eine Reihe kurzer Einzelaufträge, die zusammen einen Auftrag ergeben;
- Lesen, Unterstreichen, Abschreiben oder Übertragen als eigener Auftrag – das sind Mittel,
  kein Ziel;
- Lücken, die sich durch Abschreiben aus dem Text füllen lassen;
- Teilaufgaben, deren Ergebnis die nächste schon verrät.

**Zulässig und nicht kleinschrittig:**
- **Sicherheitsrelevante Schritte** (Freischalten, Stoffe, Mengen, Reihenfolge an der
  Maschine) stehen vollständig und in Reihenfolge – auch in einer offenen Anleitung.
- **Bedienschritte**, die nicht Lernziel sind (Messgerät einstellen, Software starten): kurz,
  am besten als Bildfolge oder Hinweis, nicht als Auftrag.
- **Übungsfolgen** zum Einschleifen einer Routine: gleichartige, je für sich vollständige
  Aufgaben (gelöstes Beispiel → steigend → eingekleidet).
- **Lösungsbeispiel mit Ausblenden:** steht als Beispiel, nicht als Auftrag.
- **Einführende Bildungsgänge** (Berufseinstieg, BVJ): enger geführt über Lösungsbeispiele,
  Hilfen und hohen Anschauungsgrad – nicht über zerlegte Aufträge.

## 4. Was entfällt

| entfällt | stattdessen |
|---|---|
| Schmuckbilder, Cliparts, Symbol- und Stockfotos, Illustrationen ohne Fachinhalt | Abbildung mit Fachinhalt – oder keine |
| Emojis und Symbole ohne Funktion (auch farbige Punkte als Stufenkennung) | Wort; zulässig sind die KI-Zeichen 🚫 💡 🔧 (`ki-vereinbarungen.md`, falls vorhanden), Warn- und Gefahrenzeichen, Ankreuzkästchen ☐ und ✔ ~ ✘ zur Selbsteinschätzung |
| Begrüßung, Motivationssätze („Viel Spaß!“, „Los geht’s!“), Ankündigungen („In diesem Arbeitsblatt lernen Sie …“) | gleich mit Situation oder Auftrag beginnen |
| Einleitung, die den Auftrag vorwegnimmt; Zusammenfassung dessen, was eben dastand | Kernaussage einmal, vorn |
| Exkurse, Anekdoten, Technikgeschichte, „Wussten Sie schon?“-Kästen | als Vertiefung, wenn sie zum Ziel beitragen – sonst streichen |
| dasselbe in Fachwissen, Hilfe und Auftrag | einmal, dort, wo es gebraucht wird |
| Zierrahmen, Farbflächen, Schmuckschriften | klare Überschriften; Kästen nur mit Funktion (Hilfe, Stolperstein, Sicherheit) |
| Angaben für die Lehrkraft (AFB, Kompetenzcodes, Annahmen, Prüfvermerke) | im Lehrerteil |
| Information, die kein Auftrag braucht | streichen |

Keine Dekoration, also bleibend: Kopfzeile (Lernsituation, Zeit, Sozialform), Name und Datum
auf Druckblättern, Erfolgskriterien, Bewertungskasten, KI-Zeichen, Quellen- und
Lizenzangaben, KI-Transparenzhinweis.

## 5. Richtwerte

Orientierung, kein Urteil. ⚠️ Noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

| Element | Richtwert |
|---|---|
| Ausgangslage, Bezug zur Situation | höchstens drei Sätze; besser Situationsmaterial (Störmeldung, Foto, Anlagenbild) |
| Arbeitsauftrag | ein bis zwei Sätze, ≤ ~25 Wörter, Operator zuerst; der Kontext steht einmal in der Ausgangslage |
| Teilaufgaben je Auftrag | höchstens drei |
| Satz | meist unter 15 Wörtern, keiner über 25; die sprachsensible Fassung ist bewusst strenger (über 20 Wörter teilen, `lesbarkeit.py`) |
| Infoblatt | eine Seite, ≤ ~300 Wörter Fließtext, mindestens eine tragende Darstellung |
| Arbeitsblatt (Teil für Lernende) | ≤ ~350 Wörter Fließtext (ohne Tabellen, Code, Abbildungen), mindestens eine Darstellung |
| Situationsmaterial | ≤ ~150 Wörter |
| Hilfekarte | je Stufe ≤ ~40 Wörter, gern als Teilbild oder Skizze |
| Rollenkarte | ≤ ~60 Wörter |
| Lektion (90 min) | ≤ ~1 500 Wörter ohne Code (`lektionsmuster.md`, falls vorhanden) |
| Lernlandkarte (eine Unterrichtseinheit) | ≤ ~1 500 Wörter wie eine Lektion; je Karte nur Auftrag, Material, Hilfen, Selbstcheck |
| sonstiges Material | ≤ ~400 Wörter Fließtext je Datei |

Authentische Dokumente (Betriebsanleitung, Datenblatt, Norm, Quelle der Quellenmappe) bleiben
im Original und zählen nicht mit – sie liegen als Auszug mit Fundstelle bei, nicht
abgeschrieben.

## 6. Rückwärtsprobe vor der Ausgabe

1. **Jeder Absatz, jede Abbildung:** Welcher Auftrag braucht das? Keiner → streichen.
2. **Jeder Auftrag:** Operator, Ergebnisform, Erfolgskriterium – und kein vorgegebener
   Lösungsweg? Schritte → in die Hilfen.
3. **Jede Aufgabe:** Mit welcher Darstellung wird gearbeitet? Keine → ergänzen, wo eine trägt.
4. **Dekoration** (Abschn. 4) gestrichen?
5. **Skript:** `python3 scripts/schuelermaterial_pruefen.py DATEI.md` – Fließtext, lange Sätze
   und Aufträge, Teilaufgaben und Schrittfolgen, Darstellungen je Auftrag, Dekoration,
   Lehrerangaben, doppelte Sätze. Wortzahl und Befunde im Qualitätscheck festhalten.

## Anhang: references/skill-vertrag.md

# Skill-Vertrag der Bibliothek „Unterrichtsentwicklung BBS"

Gemeinsamer Standard für alle Skills dieser Bibliothek. Er sorgt dafür, dass jeder Skill
**allein** funktioniert und trotzdem **mit jedem anderen kombinierbar** ist. Die Quelle liegt
in `_gemeinsam/skill-vertrag.md`; jeder Skill trägt eine Kopie unter `references/`.

---

## 1. Eigenständig arbeiten – Entwurf vor Rückfrage

1. Der Skill braucht nur den Auftrag der Lehrkraft. Fehlende Angaben werden durch
   **begründete, fachtypische Annahmen** ersetzt und sichtbar markiert:
   `⚠️ Annahme: 2. Ausbildungsjahr, 24 SuS, heterogen.` bzw. im Beruflichen Gymnasium
   `⚠️ Annahme: Jg. 13 (Qualifikationsphase), 22 SuS, Lerngebiet ING3.`
2. **Rückfragen nur, wenn ohne Antwort der ganze Entwurf unbrauchbar wäre** (z. B. Beruf
   bzw. Fach völlig unbekannt). Dann höchstens drei gebündelte Fragen, jeweils mit Vorschlag
   als Standardantwort.
3. Ziel ist ein **vollständiger erster Entwurf** (alle Abschnitte gefüllt), nicht ein
   perfekter Teil. Die Lehrkraft schärft nach.
4. Ein Skill ruft **keinen anderen Skill selbst auf**. Er empfiehlt am Ende sinnvolle
   Folge-Skills. Das Verketten übernimmt der Orchestrator `unterricht-entwickeln`.

## 2. Kontext übernehmen – die Planungsakte

Liegt eine **Planungsakte** vor (Datei `00_planungsakte.md` im Arbeitsordner oder ein
Planungsakte-Block im Gespräch), übernimmt der Skill daraus alle passenden Angaben und fragt
nichts erneut ab. Nach getaner Arbeit trägt er sein Artefakt in die Akte ein und ergänzt
leere Felder, die er festgelegt hat. Widersprüche zur Akte werden gemeldet, nicht still
überschrieben.

```markdown
---
projekt: "LS 4 – Förderband nach Störung wieder in Betrieb nehmen"
bundesland: Niedersachsen
schulform: Berufsschule (Teilzeit)
bildungsgang: Industriemechaniker/-in
ausbildungsjahr: 2          # vollzeitschulisch (z. B. BG) stattdessen: schuljahrgang, phase, schwerpunkt, lerngebiet
curriculare_vorgabe: "Rahmenlehrplan Industriemechaniker/-in, LF 6"
dqr: 4
zeitrichtwert_ls: 16
lerngruppe: "22 SuS, heterogen, 3 SuS mit Deutsch als Zweitsprache (ca. B1)"
rahmen: "Fachraum Steuerungstechnik, Moodle, 90-Minuten-Blöcke"
handlungssituation: "…"
handlungsergebnis: "…"
leitidee_ls: "…"            # didaktische Leitidee der Lernsituation (1–2 Sätze)
---

## Artefakte
| Nr. | Artefakt | Skill | Status | Datei |
|---|---|---|---|---|
| 10 | DQR-Einordnung | dqr-zuordnen | Entwurf | 10_dqr-einordnung.md |

## Entscheidungen
- …

## Annahmen und Prüfaufträge (gesammelt)
- …
```

## 3. Ausgabe – einheitlich und weiterverwendbar

**Format:** Markdown. Mit Dateizugriff wird als Datei gespeichert, sonst im Chat ausgegeben.
Ein bestehendes Dokument wird **nie überschrieben**; Überarbeitungen erhalten ein Suffix
(`…_sprachsensibel.md`, `…_v2.md`).

**Text zum Einfügen** (Systemanweisung, Moodle-Textfeld, Hinweistext, Importquelle) steht als
eigener Block im Format des Ziels – ohne Erläuterungen darin; Erläuterungen stehen davor oder
danach. **Vorschläge zu Vorhandenem** (Begutachtung, Überarbeitung, Einstellungen) nennen je
Vorschlag Stelle, neuen Wert und Begründung; was schon passt, wird zusammengefasst bestätigt
statt wiederholt.

**Material für Lernende** (alles, was Lernende in die Hand bekommen; Vorgabe der Fachberatung,
31.10.2026): **kurz** – kein Satz ohne Aufgabe; **offen gestellt** – Ziel, Ergebnis und
Erfolgskriterium statt Lösungsweg, Schritte in gestufte Hilfen; **anschaulich** – Aufgaben
arbeiten mit Zeichnungen, Darstellungen und Grafiken; **ohne Dekoration** – keine Schmuckbilder,
Emojis ohne Funktion, Floskeln oder Inhalte, die kein Auftrag braucht. Richtwerte und Beispiele:
`schuelermaterial.md`, falls vorhanden. Die Pflichtabschnitte (unten) stehen im Teil für die
Lehrkraft (nach `# Lösungen und Erwartungshorizont` bzw. `# Didaktische Hinweise`), nie im Teil für
Lernende.

**Zeichnungen** (Vorgabe der Fachberatung, 01.11.2026): Jede Zeichnung in einem Artefakt – Material
für Lernende, Lösung, Erwartungshorizont, Tafelbild, Entwurf, Begleitblatt – entsteht als **SVG aus
einer Spec** mit dem passenden Zeichen-Skill, dazu eine in diagrams.net bearbeitbare `.drawio.svg`,
eingebunden mit `![Alternativtext](abbildungen/….svg)` und kursiver Bildunterschrift. **Nie** als
Zeichnung aus Zeichen (ASCII-Art: Kästen aus ┌─┐ oder +---+, Pfeilketten, Struktogramm oder GRAFCET
im Codeblock), nie als Mermaid in der Ausgabe, nie als von Hand geschriebenes SVG.

| Zeichnung | Skill bzw. Weg |
|---|---|
| Blockschaltbild, Anlagen- und Systemübersicht, Ablauf, Regelkreis, Struktogramm, ER-Modell, UML, Relationenschema | `fachdiagramm-erstellen` |
| Kennlinie, Messwertdiagramm | aus den Werten per Code als SVG (z. B. matplotlib), Wertetabelle daneben |
| Foto, Werkstückzeichnung, fremde Abbildung | Datei mit Quelle und Lizenz, sonst Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle]` |
| GRAFCET, Funktionsplan, Schaltplan | Fachsoftware; im Text zusätzlich als Tabelle (Schritt, Aktion, Transition) |

Erlaubt bleiben Text-Tabellen derselben Inhalte (GRAFCET in Textform, Zuordnungsliste) für die
Zweitkorrektur und die Barrierefreiheit; Verzeichnisbäume und Programmcode sind keine Zeichnungen.
Lösungsbilder tragen `_loesung` im Namen und stehen nur im Teil für die Lehrkraft. **Ohne
Skriptausführung** (Assistent ohne Code) liefert der Skill die Spec und an der Stelle des Bildes den
Platzhalter `[ABBILDUNG: Inhalt – Spec <datei>.yaml]`; die Lehrkraft erzeugt das SVG lokal.
Vorhandenes Material mit Zeichnungen aus Zeichen wird beim Überarbeiten umgestellt. Prüfung:
`zeichnungen_pruefen.py`, falls vorhanden (❌ Zeichnung aus Zeichen, ⚠ Mermaid). Es öffnet auch jede
eingebundene SVG: ❌ Text über Text, Form oder Linie über Text, Text ragt aus seinem Kasten oder aus
dem Bild; ⚠ SVG ohne Spec und Werkzeugkennung (von Hand?), schräge Leitungen, Datei fehlt. Ein Skill,
der Zeichnungen braucht, ruft dafür das Zeichen-Skill auf oder bringt dessen Werkzeug mit
(`metadata.eduwerkzeuge`) – `pruefen` meldet einen `edu-*`-Befehl ohne beides.

**Dateinamen** (Nummer = Platz in der Planungskette):

| Nr. | Artefakt | Skill |
|---|---|---|
| 00 | Planungsakte | unterricht-entwickeln |
| 10 | DQR-Einordnung | dqr-zuordnen |
| 20 | Lernsituation | lernsituation-dokumentieren |
| 21 | LS-Analyse (Prüfbericht: Analysebogen, Phasencheck, Querschnitt, weitere Aspekte) | lernsituation-analysieren |
| 30 | Unterrichtsentwurf | unterrichtsentwurf-erstellen |
| 35 | Entwurfscheck (Selbstcheck/Beratung) | unterrichtsentwurf-analysieren |
| 36 | Unterrichtsreflexion (nach der Stunde: Selbstreflexion, Nachbesprechung) | unterricht-reflektieren |
| 40 | Unterrichtsmaterial | unterrichtsmaterial-erstellen |
| 41 | Experiment (Versuchsanleitung, Lehrerfassung, Gefährdungsbeurteilung) | experiment-planen |
| 42 | Fachdiagramm (Diagrammblatt, Specs unter `diagramme/`, SVG unter `abbildungen/`) | fachdiagramm-erstellen |
| 43 | Programmieraufgabe (Aufgabe, Codeordner `43_code/`, Erwartungshorizont) | programmieraufgabe-erstellen |
| 44 | Technikfolgenabschätzung (Dossier, Quellenmappe, Rollenkarten) | technikfolgen-abschaetzen |
| 45 | Taxonomie-Analyse | bloom-taxonomie |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

**Werkzeug-Skills** (Nr. 42, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
Artefakt mit Pflichtabschnitten – diese hätten in der Quelle Folgen für die Ausgabe –, sondern
Kopf und Pflichtabschnitte stehen in einem **Begleitblatt** (`…_begleitblatt.md`,
Diagrammblatt). Nummern 92–96 (Ausspielen) folgen auf den Prüfbericht: veröffentlicht wird
geprüftes Material. Nr. 93 (agiles Lernen) kann auch für sich stehen, wenn eine Lehrkraft
selbst lernt; die Lernakte gehört dann der lernenden Person.

**Kopf jedes Artefakts:**

```yaml
---
artefakt: Lernsituation
titel: "Förderband nach Störung wieder in Betrieb nehmen"
skill: lernsituation-dokumentieren
skill_version: "1.0"
stand: 2026-10-08
bildungsgang: "Industriemechaniker/-in"
curriculare_vorgabe: "RLP Industriemechaniker/-in, LF 6"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
# optional:
bereich: planung            # planung | pruefen
vertraulich: false          # true bei unveröffentlichten Prüfungsvorschlägen o. Ä.
---
```

**Pflichtabschnitte am Ende jedes Artefakts:**

1. `## Qualitätscheck` – Tabelle *Kriterium | Ergebnis (✅/⚠️/❌) | Hinweis*. Ein ❌ wird vor
   der Ausgabe behoben; was sich nicht beheben lässt, wird zu ⚠️ mit Begründung.
2. `## Annahmen und Prüfaufträge` – alle `⚠️ Annahme:` und alle `🔎 Prüfen:` (Normen,
   Grenzwerte, Rechtsvorgaben, Herstellerangaben, regionale Besonderheiten).
3. `## Übergabe` – kurze Stichpunkte für Folge-Skills (z. B. Handlungsergebnis, zentrale
   Kompetenzen, Dateinamen) und **empfohlene nächste Skills**.
4. Transparenzhinweis als letzte Zeile:
   `> KI-gestützt erstellt (Skill <name> v<version>). Fachliche Prüfung und Verantwortung: Lehrkraft.`
   Die verantwortliche Rolle darf passend zum Artefakt abweichen (z. B. Lehrkraft bzw.
   Bildungsgangteam, Lernende und Fachexpertin); die Zeile beginnt immer mit `> KI-gestützt`, nennt
   Skill und aktuelle Version und steht in **einer** Zeile.

Ausnahmen: **Teilartefakte** tragen Kopf und Pflichtabschnitte im zugehörigen Begleitblatt bzw.
Erwartungshorizont;
**Akten** (Planungsakte) führen einen Verlauf;
**Lektionen** im Kursprojekt folgen `vorlage-lektion.md`, falls vorhanden (Kopf für die Seitenausgabe).

## 4. Fachliche Redlichkeit

- **Nichts erfinden:** keine ausgedachten Normnummern, Paragrafen, Zitate, Studien,
  Grenzwerte, URLs oder Quellen. Unsicheres wird markiert: `[🔎 Norm prüfen]`,
  `[🔎 Wert prüfen]`. „Weiß ich nicht sicher" ist ein gültiges Ergebnis.
- **Rechnen statt schätzen:** Zahlenwerte in Aufgaben und Lösungen werden nachgerechnet,
  Einheiten mitgeführt. Ist ein Code-Werkzeug verfügbar, wird es dafür benutzt.
- **Quellenlage offenlegen:** Unterscheiden zwischen *aus gelieferten Unterlagen* und *aus
  allgemeinem Fachwissen*. Gelieferte Ordnungsmittel haben Vorrang.
- **Fiktive Akteure klar fiktiv:** Firmen, Personen und Adressen in Handlungssituationen
  sind erkennbar ausgedacht („(fiktiv)“ beim ersten Auftreten); keine echten Telefonnummern,
  keine realen Personen; E-Mail-Adressen nur mit Beispiel-Domains (`example.org`, RFC 2606).

## 5. Datenschutz

- Für Begutachtungen, Rückmeldungen und KI-Chatbots gelten zusätzlich die **Leitplanken**
  (`references/leitplanken-bewertung.md`, falls vorhanden): Datenschutzstufen 0–2, keine
  Bewertung einzelner Lernender durch KI, Freigabe durch die Lehrkraft.
- Für Planung und Material werden **keine personenbezogenen Daten** gebraucht.
- Gibt die Lehrkraft Namen oder Leistungsdaten von Lernenden an, werden sie im Artefakt
  pseudonymisiert (S01, S02 …) und es folgt ein kurzer Hinweis.
- Keine Gesundheits-, Förder- oder Herkunftsangaben zu einzelnen Lernenden in Artefakten;
  Lerngruppen werden nur zusammenfassend beschrieben.

## 6. Begriffe und Bezugsrahmen

- Standard ist das **berufsbildende Schulwesen in Niedersachsen**. Für vollzeitschulische
  Bildungsgänge, besonders das **Berufliche Gymnasium** (Lerngebiete, Schuljahrgang,
  Notenpunkte, EPA), gilt zusätzlich `berufliches-gymnasium.md`, falls vorhanden. Verbindliche
  Begriffe nach **Leitlinie SchuCu-BBS 2024**: Handlungssituation, Handlungsergebnis,
  Handlungskompetenz mit **Fachkompetenz** (Wissen, Fertigkeiten) und **Personaler
  Kompetenz** (Sozialkompetenz, Selbständigkeit); vollständige Handlung in sechs Phasen
  (Informieren bzw. Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw.
  Kontrollieren · Reflektieren).
- **SchuCu-BBS 2024 ist verbindlich** (Entscheidung der Fachberatung, 19.10.2026): kein
  anderes Kompetenzmodell (etwa vier Dimensionen), keine anderen Phasen oder Begriffe. Eine
  Gliederung des Studienseminars oder der Schule darf gelten; ihre Abschnitte werden mit den
  Begriffen der Leitlinie gefüllt. Vorgaben anderer Länder übernehmen die Skills nicht.
- **Vollständige Handlung und Lernzeit**: Der
  Handlungskreis wird je Lernsituation geschlossen, aber nicht zwingend in 90 Minuten – er
  darf mehrere Unterrichtseinheiten umfassen (Entscheiden, Überprüfen mit Überarbeitung und
  Reflektieren der Lernsituation bleiben immer). Fachsystematische, lehrkraftgeführte
  Lernphasen sind zulässig, wo zweckdienlich und begründet; die Begründung wird dokumentiert
  (`lernsituationsmuster.md` Abschn. 12, falls vorhanden).
- **Didaktische Leitidee** (Planungshilfe der Bibliothek):
  `didaktische-leitidee.md`, falls vorhanden. Ein bis zwei Sätze, welche übertragbare Einsicht
  die Lernenden am exemplarischen Fall gewinnen und warum sie bedeutsam ist – für die
  Lernsituation (unter *didaktisch-methodische Kommentare*) und für die Stunde (vor dem
  Stundenziel). Sie ergänzt die Begriffe der Leitlinie und ersetzt keinen.
- Sprache: sachlich, geschlechtergerecht („Schülerinnen und Schüler", Abkürzung „SuS").
- Kompetenzen und Ziele werden mit **beobachtbaren Operatoren** formuliert
  (`references/operatoren-afb.md`, falls vorhanden). Nicht verwenden: *verstehen, kennen,
  wissen, lernen, sich bewusst sein*.

## 7. Selbstprüfung

Vor der Ausgabe prüft der Skill sein Ergebnis gegen die eigene Checkliste **und** gegen
diesen Vertrag (Annahmen markiert? Nichts erfunden? Pflichtabschnitte vorhanden? Material für
Lernende kurz, offen gestellt, anschaulich, ohne Dekoration? Jede Zeichnung als SVG aus einer
Spec, keine Zeichnung aus Zeichen – `zeichnungen_pruefen.py`, falls vorhanden?), behebt Mängel und
gibt erst dann aus.

## 8. Plattformen

- **Claude (Skills aktiviert):** Ordner als Skill installieren; Claude lädt ihn bei Bedarf.
- **Assistenten ohne Skill-Funktion (z. B. AIS-Chat.schule, fobizz):** Inhalt von
  `SKILL.md` als Anweisung des Assistenten einfügen, Dateien aus `references/` und
  `assets/` als Wissensbasis hochladen. Die Planungsakte wird dann von Hand zwischen den
  Assistenten weitergegeben.
- **Chatbots für Lernende** (Moodle-KI-Chat, AIS.chat-Lernszenario) bekommen keine
  Skill-Fassung, sondern eine eigene kurze Systemanweisung mit Probelauf (`ki-chatbot-einrichten`,
  im AIS-Paket `agiles-lernen-mit-ki`).

## Anhang: references/vorlage-lektion.md

---
title: "[Titel der Lektion als Handlung]"
lesson_id: "[NN]"
duration: "90 min"
learning_goals:
  - "[Kompetenz mit Operator, aus der Lernsituation]"
  - "[begründet entscheiden, … – je Lernsituation, nur bei echter Entscheidung]"
kompetenz_codes: ["[FK1]", "[PK2]"]   # optional: Codes der Zielformulierung (Kompetenzraster)
lernsituation: ""   # optional: Kurzname, wenn die Lernsituation mehrere Lektionen umfasst; "keine" für Zusatzeinheiten
teil: ""            # "k/n" (z. B. "2/3") – Pflicht, sobald lernsituation gesetzt ist
---

<!-- Lektionsmuster: references/lektionsmuster.md. H1-Überschriften nicht ändern – sie müssen
     exakt den sections in phase_config.yaml entsprechen. Schülerteil kurz halten (≤ ~1 500 Wörter
     ohne Code). Diese Vorlage ist eine Lernsituation aus EINER Lektion. Umfasst die Lernsituation
     mehrere Lektionen: Bewertungs- und KI-Kasten, Vor dem Start, Entscheiden nur in der ersten,
     Realitätstest, Rückmeldung mit Überarbeitung und Lernweg nur in der letzten Lektion; in den
     übrigen Lektionen steht dort ein Verweis und am Ende die Sollbruchstelle („Nächstes Mal …“).
     Ein Lehrkraftinput (Lösungsbeispiel, höchstens 15–20 min, dann Anwendung an anderem Fall)
     ersetzt den Zugang, wo Selbststudium teuer wäre – siehe Didaktische Hinweise.
     Teil für Lernende nach schuelermaterial.md: kurz, offene Aufträge, mit Darstellungen,
     ohne Dekoration (keine Emojis außer den KI-Zeichen). -->

# Voraussetzungen und Kompetenzen

## Voraussetzungen

- **LE [XX]**: [was genau gebraucht wird – auch Ergebnisse früherer Lektionen]

## Kompetenzen

**Fachkompetenz** – Die Schülerinnen und Schüler …

- [Operator … – Wortlaut der Vorgabe, auf diese Situation bezogen],
- [… ].

**Personale Kompetenz** – Die Schülerinnen und Schüler …

- [… – im Unterricht beobachtbar].

!!! question "Vor dem Start – 1 Minute"
    Markiere jede Zeile: **✔** kann ich schon · **~** teilweise · **✘** noch nicht.
    Am Ende vergleichst du (Aufgabe 11).

---

# Fachwissen

!!! question "Bevor du weiterliest – 3 Minuten"
    **Sage vorher**, [was bei diesem kleinen Fall herauskommt]. Notiere deine Vorhersage –
    aufgelöst wird im *Abgleich* am Ende.

## Zugänge – such dir einen aus

<!-- Standard ist EIN Zugang. Mehrere Zugänge nur, wenn ihre Zeit in der Zeitplanung steht und
     keiner mit „danach lesen“ endet. Kein Lösungscode der eigenen Aufgabe im Fachwissen. -->

**Ein** Zugang genügt – alle drei führen zu denselben Inhalten.

| Zugang | So gehst du vor |
|---|---|
| **Ausprobieren** (25 min) | [kleines Experiment: erst vorhersagen, dann prüfen – führt allein zum Ziel] |
| **Lesen** (20 min) | die Abschnitte unten der Reihe nach |
| **Fachbuch** (30 min) | [Kapitel aus *Material*] |

## [Abschnitt: Problem zuerst – dann Konzept, Beispiel, Fallen]

[ABBILDUNG: Darstellung, die den Kern trägt – Skizze, Diagramm, Ablauf oder Tabelle; Quelle, Alternativtext]

[Kurz: Der Text erklärt die Darstellung. Ein Beispiel statt drei. Tabellen statt langer Absätze.]

!!! success "Abgleich – was hattest du vorhergesagt?"
    [Ergebnis, Grund, wo es später wichtig wird – drei bis vier Sätze.]

---

# Handlungssituation

> **Kontext:** [fiktiver Betrieb (fiktiv), Ansprechperson (fiktiv)]
>
> *„[wörtliche Rede – ein echtes betriebliches Problem]“*

[ABBILDUNG: die Situation im Bild – Anlagenbild, Foto, Bildschirmausschnitt; Quelle, Alternativtext]

## Arbeitsaufträge

!!! abstract "So wird bewertet – vor dem Start lesen"
    **Abgabe:** [Handlungsergebnis] und Entscheidungsprotokoll

    | Worauf es ankommt | Punkte |
    |---|---:|
    | [Kriterium – gröbere Fassung des Feinrasters] | [P] |
    | Entscheidung begründet und in Aufgabe 8 überprüft | [P] |
    | **Summe** | **[Σ – gleiche Summe wie im Feinraster]** |

    Bewertet wird **nicht**, welche Variante ihr wählt, sondern wie ihr sie begründet und
    überprüft. Dein Lernweg wird nicht benotet.

!!! info "KI-Werkzeuge in dieser Lektion"
    🚫 **Phase 1, 2 und 4 sowie Aufgabe 6:** ohne KI – Entwurf, Entscheidung, Vorhersage,
    Überprüfung und Lernweg sind eure eigenen · 💡 **Aufgabe 5:** KI zum Verstehen ·
    🔧 **Aufgabe 7:** mit KI arbeiten – nur gekennzeichnet und nur, was du erklären kannst.
    Warum: [ein Satz, der das Ziel nennt]. [Regeln für KI-Werkzeuge]([Pfad zur Regelseite])

### Phase 1 – Informieren & Planen (Einzelarbeit, ca. 10 min)

1. 🚫 **[Analysiert]** [… – Lernende planen selbst].
2. 🚫 **[Entwerft]** [… – zwei Wege, die in Phase 2 verglichen werden].

### Phase 2 – Entscheiden (Partnerarbeit, ca. 10 min)

!!! question "[Auftraggeberin]: „[Frage, die eine Entscheidung verlangt]“"

- **A – [Variante]:** [kurz]
- **B – [Variante]:** [kurz]

3. 🚫 **Bewertet** A und B mit 1 bis 3 Punkten und **ergänzt ein eigenes Kriterium**:

    | Kriterium | A | B |
    |---|---|---|
    | [Kriterium] | | |
    | *euer Kriterium:* | | |

4. 🚫 **Legt fest** und haltet die Entscheidung fest: *Kontext · Gewählt · Verworfen, weil … ·
   Ausschlag gab · Konsequenz*.

### Phase 3 – Durchführen (Partnerarbeit, ca. 30 min)

5. 💡 **[Setzt um]** [… – größerer Auftrag mit einer Stelle, an der der naheliegende Weg
   scheitert; beschrieben wird sie nur im Lehrerteil].
6. 🚫 **[Prüft]** [… – erst Ergebnis vorhersagen, dann ausführen].
7. 🔧 **[Dokumentiert]** [… ].

### Phase 4 – Überprüfen & Reflektieren (ca. 15 min)

8. 🚫 **Prüft eure Entscheidung an der Wirklichkeit:** **(a)** [Fall, der Variante A trifft],
   **(b)** [Fall, der Variante B trifft]. **Gleicht** mit eurer Matrix **ab**.
9. 🚫 **Rückmeldung:** mit einem Team, das **anders** entschieden hat – **zwei Stärken und einen
   nächsten Schritt**, dann **überarbeitet** ihr.
10. 🚫 **Haltet fest:** [Transfer – was gilt über diesen Fall hinaus?]
11. 🚫 **Dein Lernweg** (allein, 3 min): Vergleiche mit deinen Markierungen vom Anfang. Was kannst
    du jetzt? Wo hast du festgesteckt, und was hat geholfen? **Notiere einen nächsten Schritt.**

---

# Material

- **Fachbuch**: [Titel, Kapitel, Link]
- **Werkzeug**: [ohne Installation bzw. lokal]
- **Arbeitsblatt**: [Datei]

---

# Hilfestellungen

!!! tip "Gestufte Hilfe 1 – Orientierung"
    [Hinweis, der den Weg zeigt, ohne die Lösung zu nennen]

!!! tip "Gestufte Hilfe 2 – Werkzeug"
    [konkrete Schreibweise, Formel oder Checkliste]

??? note "Gerüst (nur bei Bedarf öffnen)"
    [teilweise ausgefüllt – die Kernidee bleibt zu ergänzen]

!!! warning "Häufige Stolpersteine – und woran du sie erkennst"

    | Das beobachtest du | Das steckt dahinter | So gehst du vor |
    |---|---|---|
    | [Symptom] | [Ursache] | [Abhilfe] |
    | In der Matrix bekommt eine Variante überall 3 Punkte | Die Entscheidung stand schon fest | Sucht **ein** Kriterium, bei dem die andere gewinnt |

---

# Vertiefungen

!!! tip "Zusatz – wer fertig ist"
    **Wähle eine Vertiefung** – nach Interesse. Sie gehört nicht zum Pflichtweg.

1. **[Titel]:** [weiterführen]
2. **[Titel]:** [recherchieren mit Leitfrage]
3. **[Titel]:** [Vorgriff auf eine spätere Lektion]

---

# Kompetenzcheck

- [ ] Ich kann [Kompetenz] …
- [ ] Ich kann mich begründet zwischen [A] und [B] entscheiden.

---

# Aufgaben zur Wiederholung und Übung

[Verweis auf die Übungen – Skill quizfragen-erstellen]

---

# Lösungen / Handlungsergebnisse

[Feinraster mit Erwartungshorizont, gleiche Summe wie im Kasten *So wird bewertet* – wird NICHT veröffentlicht]

---

# Didaktische Hinweise

- **Rolle**: [je Phase] – **zurückhaltend in Phase 2 – Entscheiden**
- **Zur Phase „Entscheiden“**: [warum beide Varianten vertretbar sind; welcher Fall in Aufgabe 8 (a) A trifft, welcher (b) B]
- **Verdeckte Schwierigkeit (nicht ankündigen)**: [Aufgabe, Stelle, Symptom, wo nachgefragt wird]
- **Zeitplanung**: Einstieg 5 min | Zugang 20 min | Planen 10 min | **Entscheiden 10 min** | Durchführen 30 min | Überprüfen und Reflektieren 15 min (Σ 90 – Zugang auch als vorbereitende Selbstlernphase möglich)
- **Kernweg**: [60–65 min] – [welche Phasen und Aufgaben alle schaffen müssen]; Vertiefungen und Übungen sind Zusatz
- **Fachsystematische Phase** (falls vorhanden): [Lehrkraftinput bzw. Screencast, Dauer ≤ 15–20 min], weil [Anlass: neues Verfahren bei wenig Vorwissen, Werkzeugunterweisung, gemeinsame Notation …]; Lösungsbeispiel an [analogem Fall]; danach [Anwendung], Rückbindungsfrage: [Was bedeutet das für …?]
- **Differenzierung**:
    - *Schwächere Lernende*: [Gerüste, was entfällt]
    - *Stärkere Lernende*: [welche Vertiefung]
- **Querverbindung**:
    - **LE [XX]**: [worauf zurückgegriffen wird]
