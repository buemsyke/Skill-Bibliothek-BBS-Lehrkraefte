# Rezepte – bewährte Skill-Ketten

Jedes Rezept nennt: Anliegen (typische Formulierungen) · Schritte · Gates · Ergebnis.
Optionale Schritte in eckigen Klammern. Rezepte dürfen gekürzt oder kombiniert werden –
Reihenfolgeregeln aus der SKILL.md gelten immer.

## Auswahlhilfe

| Anliegen der Lehrkraft | Rezept |
|---|---|
| „Neue Lernsituation mit Material" | R1 |
| „Unterrichtsbesuch / Prüfungsunterricht vorbereiten" | R2 |
| „Mein Material verbessern / einsatzfertig machen" | R3 |
| „Alte LS ins SchuCu-2024-Format bringen" | R4 |
| „LS prüfen / Rückmeldung geben", „Ist unsere LS SchuCu-konform?", „alle LS des Lernfelds prüfen" (Bildungsgangteam, Fachberatung) | R5 |
| „Material für sprachlich heterogene Klasse" | R6 |
| „Aufgaben / Prüfung anspruchsvoller machen" | R7 |
| „Lernsituationen eines Lernfelds abstimmen" | R8 |
| „Meinen Entwurf vor dem UB durchsehen" (Selbstcheck, kollegiale Beratung) | R10 |
| „Material digital ausspielen" – Edumap, Quiz, Schülerseiten, Moodle, KI-Kennzeichnung | R14 |
| „Lernende sollen selbstgesteuert mit KI lernen" – Lernpfad, Probeprüfung, AIS.chat; „ich will mich einarbeiten" | R15 |
| „Projekt-LS im Beruflichen Gymnasium" – Lastenheft, Experiment, Programmierung | R16 |
| „Technikfolgenabschätzung / Urteilsbildung" – Hypothesen, Quellen, Rollenspiel, Anhörung | R17 |
| „KI-Chatbot im Kurs" – Lernbegleiter, Feedbackpartner, Kursassistent; „Systemprompt prüfen" | R18 |
| „Stunde reflektieren", „Nachbesprechung vorbereiten", „Reflexion nach dem UB", nach kollegialer Hospitation | R19 |
| „Kursprojekt überarbeiten" – vorhandene Lektionen (`lessons/*/lesson.md`) nachziehen, kürzen, zu Lernsituationen bündeln und dokumentieren | R20 |

---

## R1 – Neue Lernsituation mit Material
**Anliegen:** „Erstelle eine Lernsituation zu … mit Material für die erste Doppelstunde."
1. [`dqr-zuordnen` A – nur wenn Niveau unklar]
2. `lernsituation-dokumentieren` A → **G1**
3. `unterrichtsentwurf-erstellen` K – Einstiegsstunde (bzw. gewünschte Stunde)
4. `unterrichtsmaterial-erstellen` – Situationsmaterial, Arbeitsblatt(e), Bewertungsraster
   [`fachdiagramm-erstellen` – Abbildungen, die im Material als Platzhalter stehen]
5. `bloom-taxonomie` A – Aufgaben der Materialien; bei Abweichung C (Umformulieren)
6. [`sprachsensibel-ueberarbeiten` A – wenn DaZ/heterogen angegeben]
7. `differenzierung-erstellen` → **G2**
8. `material-pruefen` F+P+L → **G3**
9. Abschlussbericht
**Ergebnis:** 00, (10), 20, 30, 40…, 45, (50), 60, 90, 99

## R2 – Unterrichtsbesuch vorbereiten
**Anliegen:** „UB am …, 90 min, Thema …"
1. [`lernsituation-dokumentieren` A – Kurzfassung, falls keine LS vorliegt]
2. `unterrichtsentwurf-erstellen` A (ausführlich) → **G1** (Modus Schrittweise empfohlen)
3. `unterrichtsmaterial-erstellen` – Material laut Entwurf, mit Erwartungshorizont
4. `bloom-taxonomie` A – Impulse und Aufgaben (mind. eine Stufe 4–6)
5. `differenzierung-erstellen` → **G2**
6. `material-pruefen` F+P → **G3**
7. Abschlussbericht mit Hinweis auf Regeln des Studienseminars zur KI-Nutzung
8. [nach dem UB: `unterricht-reflektieren` A – Reflexion für die Nachbesprechung → 36 (R19)]
**Ergebnis:** 00, 20 (opt.), 30, 40…, 45, 60, 90, 99, (36)

## R3 – Vorhandenes Material verbessern
**Anliegen:** „Hier mein Arbeitsblatt/Ordner – mach es besser/einsatzfertig."
1. `material-pruefen` F+P+L (Ausgangsbefund)
2. `bloom-taxonomie` A (Ausgangsprofil)
3. `unterrichtsmaterial-erstellen` – Überarbeitung nach Befunden (neue Datei `…_v2.md`)
4. [`sprachsensibel-ueberarbeiten` A]
5. `differenzierung-erstellen` → **G2**
6. `material-pruefen` P (Gegenprüfung der neuen Fassung) → **G3**
7. Abschlussbericht mit Vorher/Nachher
**Ergebnis:** 90 (vorher), 45, 40…_v2, (50), 60, 90 (nachher), 99

## R4 – Lernsituation ins SchuCu-2024-Format überführen
0. [`lernsituation-analysieren` – Ausgangsbefund der alten LS, wenn erst entschieden werden soll,
   ob sich das Überführen lohnt] → 21
1. `lernsituation-dokumentieren` B (Überführen; Befunde aus 21 abarbeiten) → **G1**
2. `dqr-zuordnen` B – Kompetenzformulierungen gegen Zielniveau
3. `material-pruefen` F+L – Normen, Rechtsbezüge, Links der alten LS
4. Abschlussbericht mit Änderungsliste
**Ergebnis:** 00, 20, 10, 90, 99

## R5 – Lernsituation prüfen (Rückmeldung)
**Anliegen:** „Prüf diese LS", „Ist unsere LS SchuCu-konform?", „Prüf alle LS zu Lernfeld 7".
1. `lernsituation-analysieren` – Vorbefund per Skript (Word, PDF, Markdown), Analysebogen,
   Phasencheck, Leitidee, Querschnitt, weitere Aspekte mit geprüften Belegen; bei mehreren LS
   Kompetenzraster und Stundenbilanz → 21
2. [`dqr-zuordnen` B – wenn das Niveau fraglich ist (W3)]
3. [`bloom-taxonomie` A – wenn der Anspruch der Aufträge auffällt (W4)]
4. [`material-pruefen` F+P+L – Normen, Rechnungen und Links laut Vorbefund (W9)]
5. [`lernsituation-dokumentieren` B – überarbeiten, wenn gewünscht; Befunde den Kennungen zuordnen] → 20
6. Abschlussbericht als **wertschätzende, kriteriengeleitete Rückmeldung**: Stärken zuerst,
   drei wirksamste Verbesserungen mit Formulierungsvorschlag (aus 21)
**Ergebnis:** 21, (10), (45), (90), (20), 99

## R6 – Material für sprachlich heterogene Klasse
1. `sprachsensibel-ueberarbeiten` A (bzw. B für authentische Dokumente)
2. `differenzierung-erstellen` (inkl. sprachlicher Hilfen) → **G2**
3. `material-pruefen` P – Fachinhalt unverändert? → **G3**
4. Abschlussbericht
**Ergebnis:** 50, 60, 90, 99

## R7 – Aufgaben und Leistungsüberprüfung schärfen
1. `bloom-taxonomie` A – Ist-Profil
2. `bloom-taxonomie` C bzw. B – fehlende Stufen ergänzen
3. `unterrichtsmaterial-erstellen` – Aufgaben mit Erwartungshorizont
4. [`dqr-zuordnen` B – Niveauabgleich]
5. `material-pruefen` P (Lösbarkeit, Punkte, Rechnungen) → **G3**
**Ergebnis:** 45, 40, (10), 90, 99

## R8 – Lernsituationen eines Lernfelds abstimmen (didaktisch-methodische Planung)
Entspricht SchuCu-BBS Schritt „Inhaltliche Abstimmung über alle Lernsituationen".
1. `dqr-zuordnen` A – Niveau und Progression über die Ausbildungsjahre
2. Übersicht anlegen nach `curriculum-abgleich.md`: Zielformulierung im Wortlaut, Teilkompetenzen
   K0…Kn, Kern/Konkretisierung/Erweiterung/Ausschluss; mögliche LS-Titel, Handlungssituationen
   (Skizze), Zeitrichtwerte (Summe = Zeitrichtwert des Lernfelds), Reihenfolge,
   **Abdeckungsmatrix** K-Code × Lernsituation, Lage der Leistungsüberprüfungen (am Ende einer LS)
3. `lernsituation-dokumentieren` A – für 1–2 ausgewählte LS vollständig (Rest als Skizze)
4. `material-pruefen` P – Zeitsummen, Überschneidungen, Abdeckung aller Kompetenzen des LF
   (Prüfregeln der Abdeckungsmatrix)
5. Abschlussbericht mit Vorschlag für den Bildungsgangbeschluss
**Für vollständige Materialien eines ganzen Lernfelds:** `lernfeld-werkstatt` (falls installiert).

## R10 – Entwurfs-Selbstcheck vor dem Unterrichtsbesuch
**Anliegen:** „Schau dir meinen Entwurf an, bevor ich ihn abgebe."
1. `unterrichtsentwurf-analysieren` – Regelcheck (Skript) + Rückmeldung als Stärken,
   Entwicklungsfelder, Reflexionsfragen → 35 (keine Stufen, keine Note)
2. [`bloom-taxonomie` A – Aufgaben und Impulse]
3. [`material-pruefen` P – Material laut Entwurf]
4. Abschlussbericht mit Checkliste vor Abgabe; Hinweis auf Regeln des Studienseminars zur KI-Nutzung
**Ergebnis:** 35, (45), (90), 99 · nicht für Auswahlverfahren oder dienstliche Beurteilung ·
**Prüfungsunterricht:** nur Selbstcheck, gekennzeichnet (`pruefungsrelevant: true`, Regelcheck
`--pruefung`, Hinweise statt fertiger Formulierungen, Kennzeichnungstext für den Entwurf);
Schritte 2–3 nur als Hinweise, keine Überarbeitung durch Claude

## R14 – Material digital ausspielen
**Anliegen:** „Mach aus der LS eine Edumap mit Quiz", „Schülerseiten erzeugen und
veröffentlichen", „Material für Moodle aufbereiten".
1. [`material-pruefen` F+P+L – wenn die Lehrerfassung noch nicht geprüft ist] → **G3**
2. [`fachdiagramm-erstellen` – Abbildungen aus Platzhaltern bzw. ASCII-Skizzen] → 42
3. [`quizfragen-erstellen` – Übung, Sicherung, Selbstcheck] → 65
4. [`lernlandkarte-erstellen` – Lernweg in edumaps; verlinkt Material, Quiz, Diagramme] → 92
5. [`schuelerseiten-veroeffentlichen` – Schülerfassung (Einzeldokumente) bzw. Schülerseiten
   (Kursprojekt), Ausgabeprüfung] → 94
6. `ki-kennzeichnung` – Hinweise und Transparenzerklärung, erst nach der Prüfung → 96
7. **GV Veröffentlichung** → Abschlussbericht. Veröffentlicht (Push, Upload, Freigabe im LMS)
   wird nur auf ausdrücklichen Auftrag der Lehrkraft.
**Ergebnis:** (42), (65), (92), (94), 96, 99 · Inhalte, die in der Lernlandkarte oder im Quiz neu
entstehen, prüft `material-pruefen` vor GV (Quelle `.md`, Links).

## R15 – Selbstgesteuert lernen mit KI (Lernpfad, AIS.chat)
**Anliegen:** „Meine Azubis sollen sich mit AIS.chat auf die Klassenarbeit vorbereiten", „Lernpfad
mit Probeprüfung für die Prüfungsvorbereitung", „Ich muss mich in ein neues Thema einarbeiten".
1. [Planungsakte lesen – Lernsituation, Kompetenzen, geprüftes Material als Quellen]
2. `agiles-lernen-mit-ki` A – Kickoff und Lernpfad der Lerngruppe (Sprints, Quellen,
   Fachexpertin = Lehrkraft) → 93
3. [`quizfragen-erstellen` – Fragenpool für die Probeprüfungen, je Sprint, mit Fundstellen] → 65
4. `agiles-lernen-mit-ki` F – AIS-Paket (Lernszenarien Kickoff, Lernsprint, Probeprüfung;
   Dialogpartner Rollenspiel), Lernakte für Lernende, Fehlerjagd → 93
5. [`material-pruefen` – neue Inhalte im Paket: Rollenspiel-Steckbrief, Fragenpool] → **G3**
6. `ki-kennzeichnung` → 96; **GV** – Test mit Zweitgerät, Freigabezeile; Freigabe in AIS.chat
   nur auf ausdrücklichen Auftrag der Lehrkraft
**Ergebnis:** 93 (Lernpfad, AIS-Paket), (65), (90), 96, 99 · keine Einzelberichte über
Lernende, Lernakten bleiben bei den Lernenden.
**Lehrkraft lernt selbst:** nur `agiles-lernen-mit-ki` A (+ G für Claude Code bzw. E-Assistent in
AIS.chat); Fachexpertin aus der Fachgruppe; kein Orchestrator nötig.

## R16 – Projekt-Lernsituation im Beruflichen Gymnasium
**Anliegen:** „Projekt-LS für das BG Technik, Lerngebiet ING3, mit Lastenheft, Versuch und
Programmierung", „Unsere LS ING4.1 einsatzfertig machen".
1. [`dqr-zuordnen` B – Niveau und Progression über die Jahrgänge prüfen]
2. `lernsituation-dokumentieren` A – neue LS; vorhandene LS erst mit `lernsituation-analysieren`
   prüfen (→ 21), dann B (BG-Format: Lerngebiet, Schuljahrgang/Phase, Kompetenzraster mit
   Rückwärtsprobe, Querschnittsaufgaben) → **G1**
4. `unterrichtsentwurf-erstellen` S – Projektsequenz (Kickoff, Meilenstein-Reviews,
   Fachgespräch) → 30
5. `unterrichtsmaterial-erstellen` – Lastenheft/Pflichtenheft mit fiktiven Kontaktdaten,
   Projektplan, Projektjournal → 40
6. [`experiment-planen` – Versuch mit Gefährdungsbeurteilung als Entwurf] → 41 → **GE**
7. [`programmieraufgabe-erstellen` – Mikrocontroller, Python, G-Code mit Codeprüfung] → 43
8. [`technikfolgen-abschaetzen` – Folgen der Lösung, Quellenmappe] → 44
9. `bloom-taxonomie` A → 45 → **G2**
11. `material-pruefen` F+P+C+L+M (Rechnungen, Code, Experiment, Links, Metadaten) → 90 → **G3**
12. Abschlussbericht: Verbindlichkeit der Befunde trennen (RRL/Erlass · Leitlinie · Bibliothek)
**Ergebnis:** 00, (10), (21), 20, 30, 40…, (41), (43), (44), 45, 90, 99 · Notenpunkte,
fiktive Auftraggeber, keine Personendaten in Lastenheften.

## R17 – Technikfolgenabschätzung und Urteilsbildung
**Anliegen:** „TFA zum Windpark mit Rollenspiel", „Pro und Contra mit Quellen", „Unsere
Schulungsunterlagen auf Kontroversität prüfen".
1. [`material-pruefen` F+L – vorhandenes Material: Sachfehler, Quellen, Links] → 90
2. `technikfolgen-abschaetzen` A bzw. B – Dossier, Hypothesen, Quellenmappe; Rahmung
   ergebnisoffen (Beutelsbacher Konsens) → 44
3. `technikfolgen-abschaetzen` C – Rollenkarten für Anhörung mit Rollentausch → 44
4. [`sprachsensibel-ueberarbeiten` – Laiensprache für Schulung oder Bürgerdialog] → 50
5. [`agiles-lernen-mit-ki` – Anhörung als KI-Rollenspiel zum Üben; KI-Transkripte nur als zu
   prüfendes Material] → 93
7. `material-pruefen` → **G3**; [`ki-kennzeichnung` → **GV**, wenn Material veröffentlicht wird]
**Ergebnis:** (90), 44 (Dossier, Rollenkarten), (50), (93), 99 · Querschnitt BNE und
Demokratiebildung im Abschlussbericht ausweisen.

## R18 – KI-Chatbot im Kurs (Lernbegleiter, Feedbackpartner, Systemprompt prüfen)
**Anliegen:** „Chatbot für meinen Moodle-Kurs zur LS 4.2, der nicht vorsagt", „Feedbackpartner
für die Projektdokumentation", „Prüf den Systemprompt aus unserem Moodle-Plugin".
1. [Planungsakte lesen – Lernsituation, Phase, geprüftes Material als Hintergrundwissen,
   Erwartungshorizont für typische Fehler, Bewertungsraster für Feedback ohne Note]
2. [`material-pruefen` – Hintergrundwissen, wenn noch nicht geprüft] → **G3**
3. `ki-chatbot-einrichten` A bzw. B – Paket mit Systemanweisung, Begrüßung, Einführung,
   Probelauf → 95 · **oder** C – Gutachten zu einem vorhandenen Systemprompt (Datenfluss,
   Lücken, Einsatzorte) → 95, Rezept endet hier
4. Probelauf durch die Lehrkraft (Schüleransicht bzw. Zweitgerät); `ki-chatbot-einrichten` D
   wertet aus – ein Pflichttest ✗ → Anweisung nachschärfen, Probelauf wiederholen
5. `ki-kennzeichnung` – Text 6 „KI-Chat im Kurs" → 96; **GV** – Pflichttests ✓,
   `Freigabe Chatbot: erteilt`; Einrichten bzw. Freischalten auf der Plattform nur auf
   ausdrücklichen Auftrag der Lehrkraft
**Ergebnis:** 95, (90), 96, 99 · kein Einsatz auf Seiten mit Schülerdaten, keine Bewertung,
Chatverläufe werden nicht ausgewertet. Lernweg über Wochen mit Lernakte → R15.

## R19 – Unterricht reflektieren (Nachbesprechung, Hospitation)
**Anliegen:** „Bereite meine Reflexion für die Nachbesprechung vor", „Was lief anders als
geplant?", „Mein Kollege hat hospitiert – Nachbesprechung vorbereiten".
Entspricht SchuCu-BBS Schritt „Unterricht durchführen und evaluieren".
1. [Planungsakte lesen – Entwurf 30, Entwurfscheck 35, Lernsituation 20]
2. `unterricht-reflektieren` A (bzw. B mit Zustimmung der hospitierten Lehrkraft) – Gerüst aus
   dem Entwurf, Plan und Verlauf, Zielerreichung mit Belegen, Schwerpunkte, Konsequenzen → 36
3. [`unterrichtsentwurf-erstellen` K – Folgestunde mit den Konsequenzen] → 30
4. [`differenzierung-erstellen` bzw. `unterrichtsmaterial-erstellen` – wenn die Reflexion
   Material- oder Differenzierungsbedarf zeigt] → 60, 40
**Ergebnis:** 36, (30), (40), (60) · kein Abschlussbericht nötig, wenn nur 36 entsteht ·
Lernende nur als Lerngruppe; Prüfungsunterricht nur Modus A zur eigenen Vorbereitung,
gekennzeichnet; keine Note, keine Beurteilung von Personen.

## R20 – Kursprojekt nach dem Lektionsmuster überarbeiten
**Anliegen:** „Zieh die Lektionen 1–8 nach", „Den Lernenden ist das zu viel Text", „Eine Lektion
ist zeitlich zu aufwendig", „Die Reihe soll SchuCu-konform dokumentiert werden". Maßstab:
`lektionsmuster.md` (im Skill `unterrichtsmaterial-erstellen`). Grundsatz (Entscheidung der
Fachberatung, 23.10.2026): Der Handlungskreis wird **je Lernsituation** geschlossen, nicht je
90-Minuten-Lektion; fachsystematische, lehrkraftgeführte Phasen sind zulässig, wo begründet.
1. Ist-Stand: `lektion_pruefen.py lessons/*/lesson.md --loesungen solutions --projekt .`
   (im Skill `unterrichtsmaterial-erstellen` bzw. `schuelerseiten-veroeffentlichen`) – Elemente,
   Summen, Zeit (Phasen + Zugang), Kernweg, Wortzahl ohne Code je Lektion festhalten
2. **Zuschnitt prüfen:** Welche aufeinanderfolgenden Lektionen haben *eine* Handlungssituation und
   *ein* Handlungsergebnis? Vorschlag der Bündelung mit Begründung; ein neuer Zuschnitt ändert das
   schulische Curriculum und braucht den **Bildungsgangbeschluss** (Planungsschritt 4) – ohne
   Beschluss nur Vorschlag, kein Umbau. Echte und Scheinentscheidungen trennen
3. `unterrichtsmaterial-erstellen` – je Lernsituation nach `lektionsmuster.md` Abschn. 6:
   bündeln, Entscheiden nur an echter Stelle, Doppeltes und Lösungscode im Fachwissen streichen,
   begründete fachsystematische Phase (im Skill `lernsituation-dokumentieren`:
   `lernsituationsmuster.md` Abschn. 12, falls vorhanden) statt dreier
   Zugänge, Kernweg und vollständige Zeitplanung; Lösung, Arbeitsblatt und Beispieldateien
   mitziehen → 40 (je Lektion)
4. [`differenzierung-erstellen` – Hilfen und Vertiefungen als Zusatz, wenn sie fehlen] → 60
5. `lernsituation-dokumentieren` A je Lernsituation (Lektionen mit demselben Kopffeld
   `lernsituation` in einem Dokument), dazu eine Lerngebiets- bzw. Lernfeldübersicht mit neuer
   Stundenbilanz (Klausuren, Puffer); `lernsituation_pruefen.py` über alle LS
   (Kompetenzraster, Stundenbilanz, Querbefunde) → 20
6. [`material-pruefen` F+P+L] → **G3**
7. `schuelerseiten-veroeffentlichen` P → 94, `ki-kennzeichnung` → 96, **GV**
**Ergebnis:** 40, 20, (60), 94, 96, 99 · Wortzahl vorher/nachher und Zeitbilanz im
Abschlussbericht; Analysebogen je LS mit eigenem Beleg, nicht aus einer Vorlage.

