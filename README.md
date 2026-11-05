# Skill-Bibliothek BBS – KI-Skills für die Unterrichtsentwicklung

22 KI-Skills für Lehrkräfte an **berufsbildenden Schulen in Niedersachsen** einschließlich des
Beruflichen Gymnasiums: Lernsituationen nach der Leitlinie SchuCu-BBS 2024 entwickeln und prüfen, Unterrichtsentwürfe,
Arbeitsmaterial, Differenzierung, Quiz für Moodle, Lernlandkarten für edumaps, KI-Chatbots für den
Kurs und mehr. Die Skills sind nach den **Kategorien von AIS.chat** geordnet.

> Jeder Skill liefert einen **ersten, vollständigen und geprüften Entwurf** – keine fertige
> Entscheidung. Fachliche Richtigkeit, Einsatz und Freigabe verantwortet die Lehrkraft bzw. das
> Bildungsgangteam.

**Bezugsrahmen:** Leitlinie **SchuCu-BBS 2024** (verbindlich: Kompetenzmodell, sechs Phasen der
vollständigen Handlung, Begriffe), DQR, Rahmenrichtlinien des Beruflichen Gymnasiums, Erlasse zu
BNE und Demokratiebildung. Die Beispiele stammen aus Metalltechnik, SHK, Informationstechnik und
dem BG Technik; die Skills selbst sind berufsfeldübergreifend.

## Schnellstart

| Wo arbeiten Sie? | So geht's |
|---|---|
| **Claude** (claude.ai, Desktop-App) | Unter **Releases** das Paket eines Skills (`<skill>.zip`) oder einer Kategorie herunterladen und in Claude unter *Einstellungen → Fähigkeiten → Skills* hochladen (Kategorie-Pakete vorher entpacken: ein Skill je Upload). Claude lädt einen Skill, sobald der Auftrag passt. |
| **AIS.chat** oder andere Assistenten ohne Skill-Funktion | Datei `ais-chat/<kategorie>/<skill>.md` öffnen: den Teil **ANWEISUNG** als Anweisung eines eigenen Assistenten einfügen, die **ANHÄNGE** als Wissen bzw. Datei hochladen. Hat der Assistent ein Zeichenlimit, nur die ANWEISUNG einfügen und die Datei vollständig hochladen. |
| **Claude Code** | Skill-Ordner aus `skills/<kategorie>/` nach `~/.claude/skills/` (persönlich) oder `<projekt>/.claude/skills/` kopieren. |

**Statt Claude und AIS.chat können auch andere Anbieter wie ChatGPT/Gemini oder Fobizz/SchulKI genutzt werden.**

Für den Einstieg reichen `unterricht-entwickeln` (wählt und verkettet die übrigen Skills) und die
Skills für Ihr Vorhaben. Beispiel:

> „Erstelle eine Lernsituation nach SchuCu-BBS 2024 für Industriemechaniker im 1. Jahr zur
> Wartung eines Gurtförderers, 16 Stunden, mit Material für die erste Doppelstunde. Drei SuS
> haben Deutsch als Zweitsprache."

## Die Skills nach Kategorien

### Unterrichtsplanung

| Skill | macht | typischer Auftrag |
|---|---|---|
| `unterricht-entwickeln` | wählt passende Skills, verkettet sie über eine Planungsakte und sichert das Ergebnis mit Prüfschritten; Abschlussbericht mit offenen Prüfaufträgen | „Lernsituation mit Material für die erste Doppelstunde" |
| `dqr-zuordnen` | DQR-Niveau amtlich bestimmen und begründen, Folgen für den Unterricht, Niveauabgleich von Kompetenzen und Aufgaben | „Passt meine LS zu DQR 4?" |
| `lernsituation-dokumentieren` | Lernsituation nach SchuCu-BBS 2024 entwickeln, ältere LS überführen, mit dem Analysebogen begutachten; didaktische Leitidee, Lernhürden, Muster für Diagnose-, Projekt- und Experiment-LS | „LS zu Wartung Gurtförderer, IM 1. Jahr" |
| `unterrichtsentwurf-erstellen` | Stundenverlaufsplan, Sequenz mehrerer Stunden oder ausführlicher Entwurf für Unterrichtsbesuch und Prüfungsunterricht | „UB 90 min, Phase Planen" |
| `bloom-taxonomie` | Ziele und Aufgaben nach Bloom einordnen, Aufgabentreppen, Anspruch heben oder senken | „Sind meine Aufgaben zu leicht?" |
| `klausur-erstellen` | Klassenarbeit, Klausur, Lernzielkontrolle mit Operator-Aufträgen, Antwortraum, Erwartungshorizont, Korrekturschablone und Notenschlüssel; Selbstprüfung per Skript | „Klassenarbeit 90 min mit Erwartungshorizont“ |
| `abiturvorschlag-erstellen` | Vorschläge A und B für das dezentrale Abitur am Beruflichen Gymnasium (Technik, Berufliche Informatik): Schüler- und Lehrermaterial, Bewertungsbogen, Bewertungsmappe, Begleitblatt; Prüfung per Skript nach dem Katalog der Begutachtung | „Abiturvorschlag Informationstechnik 2028“ |

### Material

| Skill | macht | typischer Auftrag |
|---|---|---|
| `unterrichtsmaterial-erstellen` | Arbeitsblatt, Infotext, Vorlagen, Raster, Befund- und Rollenkarten, Entscheidungsmatrix, Peer-Feedback, Reflexionsauftrag, Lehrerhandreichung – mit Schüler- und Lehrerfassung | „Arbeitsblatt mit Erwartungshorizont" |
| `differenzierung-erstellen` | Hilfekarten, Fundamentum/Additum, Sprinter- und Wahlaufgaben, Organisation | „Hilfekarten für Schwächere" |
| `quizfragen-erstellen` | Quizfragen aus einer Markdown-Quelle nach GIFT (Moodle) und H5P, mit Prüfung von Aufbau und Anforderungsbereichen | „Zehn Übungsfragen zur LS für Moodle" |
| `fachdiagramm-erstellen` | Blockschaltbild, Ablauf, Regelkreis, Struktogramm, ER- und UML-Diagramm als draw.io/SVG mit Alternativtext | „Regelkreis für das Arbeitsblatt zeichnen" |
| `technologieschema-erstellen` | Technologieschema (Anlagenbild), Schaltplanauszug mit Schaltzeichen, GRAFCET nach DIN EN 60848, Funktionsplan und Netzplan als SVG und draw.io aus einer YAML-Spec; Kennzeichen nach DIN EN IEC 81346-2 geprüft, Legende als Text | „Technologieschema der Biegestation mit GRAFCET“ |
| `lernlandkarte-erstellen` | Lernlandkarte für edumaps (nds.edumaps.de) mit Selbstdiagnose, Lernposten, Hilfen und Quiz; Stundenablauf als Zeitstrahl | „Mach aus der LS eine Edumap mit Selbstdiagnose" |
| `schuelerseiten-veroeffentlichen` | Schülerfassung ohne Lösungen und Lehrerhinweise, MkDocs-Seiten je LMS-Phase; Ausgabeprüfung, Freigabe vor dem Veröffentlichen | „Schülerfassung ohne Lösungen für Moodle" |
| `material-pruefen` | Fakten-, Plausibilitäts-, Code-, Form- (Material für Lernende), Link- und Metadatencheck mit Prüfbericht und Ampel | „Prüf diesen KI-Entwurf" |

### Feedback

| Skill | macht | typischer Auftrag |
|---|---|---|
| `lernsituation-analysieren` | prüft vorhandene Lernsituationen (Word, PDF, Markdown; auch alle LS eines Lernfelds): Vorbefund per Skript, Analysebogen der Leitlinie, Phasencheck, Leitidee, Querschnittsaufgaben und weitere Aspekte mit Belegen – Prüfbericht mit Ampel, Stärken und den drei wirksamsten Verbesserungen | „Prüf diese Lernsituation, wir wollen sie im Team übernehmen" |
| `unterrichtsentwurf-analysieren` | Selbstcheck oder kollegiale Beratung zum eigenen Entwurf: Stärken, Entwicklungsfelder mit Belegen, Reflexionsfragen – **ohne Note, ohne Niveaustufe**; prüfungsrelevante Entwürfe nur als gekennzeichneter Selbstcheck | „Schau über meinen UB-Entwurf" |
| `unterricht-reflektieren` | Reflexion nach der Stunde: Plan und Verlauf, Zielerreichung mit Belegen, höchstens drei Schwerpunkte, Konsequenzen für die Folgestunde; Nachbesprechung nach Hospitation – **ohne Note** | „Reflexion für die Nachbesprechung meines UB" |

### KI und Prompting

| Skill | macht | typischer Auftrag |
|---|---|---|
| `ki-chatbot-einrichten` | Chatbot für Lernende oder Lehrkräfte (Moodle-KI-Chat, AIS.chat): Systemanweisung aus Bausteinen, Begrüßung, Probelauf mit Pflichttests, Freigabe; Gutachten zu vorhandenen Systemprompts – **bewertet nie Schülerleistungen** | „Chatbot für meinen Moodle-Kurs, der nicht vorsagt" |
| `ki-kennzeichnung` | KI-Transparenzhinweis auf jeder Seite, Transparenzerklärung, Hinweistexte für Word, Moodle, edumaps | „Kennzeichne das Material als KI-unterstützt" |

### Lernbegleitung und Coaching

| Skill | macht | typischer Auftrag |
|---|---|---|
| `agiles-lernen-mit-ki` | agiles Lernen mit KI für Lehrkräfte und Lernende: Kickoff, Lernpfad aus Sprints, Probeprüfung, Rollenspiel, Retro; Paket für AIS.chat (Lernszenarien, Dialogpartner) | „Meine Azubis sollen sich mit AIS.chat auf die Klassenarbeit vorbereiten" |

### Schreiben und Texte

| Skill | macht | typischer Auftrag |
|---|---|---|
| `sprachsensibel-ueberarbeiten` | Material sprachsensibel überarbeiten, Wortspeicher, Satzbausteine, Lesbarkeitswerte; Kundensprache für Beratung und Einweisung | „Für DaZ-SuS, Fachbegriffe bleiben" |

### Fachliche Experten

| Skill | macht | typischer Auftrag |
|---|---|---|
| `experiment-planen` | Versuchsanleitung, Lehrerfassung mit Erwartungswerten, Gefährdungsbeurteilung **als Entwurf** – gibt nie einen Versuch frei | „Schülerversuch Elektrolyse mit Wirkungsgrad" |
| `wokwi-simulation-erstellen` | setzt eine Steuerungsaufgabe als Wokwi-Simulation für Arduino Uno oder ESP32 um: Sketch, Schaltung, Testszenarien, Zeitablauf, Begleitblatt | „Ampelsteuerung als Wokwi-Projekt mit Lösung" |
| `circuitjs-schaltung-erstellen` | Schaltungen als CircuitJS-Simulation (Falstad) mit Messpunkten, Erwartungswerten und Prüfung in der Engine | „Spannungsteiler mit Poti zum Ausprobieren" |
| `programmieraufgabe-erstellen` | Programmieraufgaben für Mikrocontroller (C/C++, Arduino, ESP32), Python und G-Code mit Startcode, Testfällen, Hilfen und Musterlösung; Codeprüfung per Skript | „ESP32 soll den Volumenstrom eines Sensors anzeigen" |

### Projekte

| Skill | macht | typischer Auftrag |
|---|---|---|
| `technikfolgen-abschaetzen` | Technikfolgenabschätzung mit Hypothesen, Quellenmappe, Perspektiven, Zielkonflikt und Urteil; Rollenkarten für eine Anhörung; ergebnisoffen (Beutelsbacher Konsens) | „TFA zum Windpark mit Rollenspiel im Gemeinderat" |

## So arbeiten die Skills zusammen

- **Unabhängig:** Jeder Skill funktioniert allein. Fehlende Angaben ersetzt er durch markierte
  Annahmen (`⚠️ Annahme:`), statt lange nachzufragen; Unsicheres markiert er mit `🔎 Prüfen:`.
- **Kombinierbar:** Alle Skills folgen demselben Skill-Vertrag (`references/skill-vertrag.md` in
  jedem Skill): gleiche Begriffe, gleicher Dateikopf, nummerierte Dateinamen und eine gemeinsame
  **Planungsakte** (`00_planungsakte.md`), über die Ergebnisse weitergereicht werden.
- **Orchestriert:** `unterricht-entwickeln` wählt ein passendes Rezept (z. B. *neue LS mit
  Material*, *LS prüfen*, *Unterrichtsbesuch vorbereiten*, *Material digital ausspielen*, *KI-Chatbot im Kurs*,
  *Unterricht reflektieren*) und prüft an festen Stellen: Planung, Material, Abschluss, vor jedem
  Schülerversuch und vor jeder Veröffentlichung.
- **Ohne Skill-Funktion** (z. B. AIS.chat) wird die Planungsakte von Hand zwischen den Assistenten
  weitergegeben.

## Datenschutz und Verantwortung

- **Keine personenbezogenen Daten von Lernenden** in den Chat geben (Namen, Noten, Abgaben,
  Förderbedarfe). Lerngruppen werden nur zusammenfassend beschrieben.
- **Keine Bewertung durch KI:** Die Skills erstellen Material und Rückmeldungen zu Entwürfen,
  aber keine Noten und keine Urteile über einzelne Lernende oder Lehrkräfte.
- **Entwürfe für Unterrichtsbesuch oder Prüfungsunterricht:** Selbstcheck ist erlaubt und wird
  gekennzeichnet; die Regeln des Studienseminars zur KI-Nutzung gelten.
- **Experimente:** Gefährdungsbeurteilung nur als Entwurf; Vorversuch und Freigabe verantwortet
  die Lehrkraft.
- **Veröffentlichen und Kennzeichnen:** Material für Lernende erst nach eigener Prüfung
  freigeben und als KI-unterstützt kennzeichnen (`ki-kennzeichnung`).
- Vor dem Einsatz von KI-Chatbots mit Lernenden die Vorgaben der Schule (Schulleitung,
  Datenschutzbeauftragte bzw. Datenschutzbeauftragter) beachten.

## Technische Hinweise

- Einige Skills prüfen ihre Ergebnisse mit **Python-Skripten** (`scripts/`). In Claude mit
  Code-Ausführung laufen sie von selbst; nötig ist nur Python 3 (für die Werkzeug-Skills mit
  PyYAML). Ohne Code-Ausführung – etwa in AIS.chat – arbeiten die Skills ohne diese Prüfung.
- Die Werkzeug-Skills `quizfragen-erstellen`, `lernlandkarte-erstellen`,
  `fachdiagramm-erstellen`, `schuelerseiten-veroeffentlichen` und `ki-kennzeichnung` bringen die
  nötigen Module der *eduwerkzeuge* mit (`scripts/eduwerkzeuge/`, MIT-0). Das Umwandeln in
  die Zielformate (GIFT, H5P, edumaps-Import, draw.io) braucht Code-Ausführung.
- Optional: `g++` für die Prüfung von C/C++-Code, `pdftotext` (poppler) für PDF-Dateien.

## Ordnerstruktur

```
skills/<kategorie>/<skill>/     Skill für Claude: SKILL.md, references/, assets/, scripts/
ais-chat/<kategorie>/<skill>.md Fassung für AIS.chat und andere Assistenten (ANWEISUNG + ANHÄNGE)
LICENSE.md                      Lizenz
```

## Rückmeldung

Fehler, Wünsche und Erfahrungen bitte als **Issue** in diesem Repository. Das Repository wird
automatisch erzeugt; Vorschläge per Pull Request werden von Hand übernommen.

## Lizenz

Texte, Anleitungen und Vorlagen: **CC0 1.0** (gemeinfrei); Skripte: **MIT-0**. Eine Namensnennung ist
nicht erforderlich. Material, das Sie mit den Skills erstellen, gehört Ihnen – Einzelheiten in
[`LICENSE.md`](LICENSE.md).
