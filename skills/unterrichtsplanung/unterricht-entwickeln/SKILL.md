---
name: unterricht-entwickeln
description: Orchestriert agentische Unterrichtsentwicklung für berufsbildende Schulen und das Berufliche Gymnasium – analysiert das Anliegen, wählt Skills der Bibliothek (Planung – DQR, Lernsituation nach SchuCu-BBS 2024, Entwurf, Material, Experiment, Programmieraufgabe, Technikfolgenabschätzung, Bloom, Differenzierung, Sprache, Quiz, Diagramme; Ausspielen – Lernlandkarte, Schülerseiten, KI-Kennzeichnung, AIS.chat, KI-Chatbots; Prüfen – LS-Analyse, Faktencheck, Entwurfs-Selbstcheck, Reflexion) und verkettet sie über eine Planungsakte mit Qualitäts-, Experiment- und Freigabe-Gates zu einem Gesamtpaket mit Abschlussbericht. Verwenden für mehrschrittige Vorhaben wie „Lernsituation mit Material", „UB vorbereiten", „Projekt-LS im BG", „Technikfolgenabschätzung mit Rollenspiel", „Material verbessern", „Material digital ausspielen" – oder wenn unklar ist, welcher Skill passt.
metadata:
  version: "1.23"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Unterricht entwickeln (Orchestrator)

## Zweck
Aus einem Anliegen der Lehrkraft ein **abgestimmtes, geprüftes Gesamtergebnis** machen, indem
die richtigen Skills in der richtigen Reihenfolge arbeiten – und die Lehrkraft am Ende genau
weiß, was sie noch prüfen und entscheiden muss.

## Wann dieser Skill – und wann nicht
- **Ja:** Vorhaben mit mehreren Produkten oder Arbeitsschritten; unklarer Bedarf; Qualitäts-
  sicherung über mehrere Dokumente.
- **Nein, direkt den Einzel-Skill nutzen:** wenn genau ein Produkt gewünscht ist („nur ein
  Arbeitsblatt", „nur Bloom-Analyse") – der Orchestrator nennt dann den Skill und übergibt.
- **Nein, anderer Orchestrator:** ein **ganzes Lernfeld** als gedruckter Materialkosmos mit
  Folien, Lerntool und Schülerpaket im Corporate Design einer Schule → `lernfeld-werkstatt`
  (falls installiert); große Blattserien in diesem Design → `serien-werkstatt` (falls
  installiert).

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · Planungsakte führen · einheitlicher Kopf und Pflichtabschnitte in jedem Artefakt.
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Ablauf

### 1. Anliegen klären (kurz)
Bestimme: **Ziel-Produkte** (was soll am Ende vorliegen?), **Ausgangsmaterial** (was liegt
vor?), **Kontext** (Beruf/Bildungsgang, Lernfeld, Jahr, Lerngruppe, Zeit, Rahmen).
Rückfragen nur, wenn Beruf/Fach **und** Thema fehlen – dann höchstens drei Fragen mit
Vorschlägen. Alles andere: Annahmen.

### 2. Planungsakte anlegen
Arbeitsordner wählen (vom Nutzer genannt, sonst `unterrichtsentwicklung/<projekt-kurzname>/`)
und `00_planungsakte.md` nach `references/planungsakte-vorlage.md` anlegen. Ohne Dateizugriff:
Planungsakte als Block im Gespräch führen und bei jedem Schritt aktualisiert mitgeben.

### 3. Rezept wählen und Plan zeigen
Passendes Rezept aus `references/rezepte.md` wählen oder aus dem Katalog
(`references/skill-katalog.md`) zusammensetzen – Abhängigkeiten beachten (unten). Den Plan in
**höchstens acht Zeilen** zeigen: Schritte, Skills, Produkte, wichtigste Annahmen.

- **Modus Durchlauf (Standard):** nach dem Plan sofort beginnen; Lehrkraft kann jederzeit
  stoppen.
- **Modus Schrittweise:** wenn gewünscht oder bei prüfungsrelevanten Vorhaben (UB/PU) –
  nach Gate G1 auf Freigabe warten.
- **Veröffentlichen (R14): vor GV immer Schrittweise.** Erzeugen und Prüfen laufen durch;
  Push, Upload oder Freigabe im LMS nur nach Freigabezeile und ausdrücklichem Auftrag.

### 4. Schritte ausführen
Für jeden Schritt:
1. Skill laden (installierter Skill; sonst dessen `SKILL.md` aus dem Bibliotheksordner lesen;
   fehlt beides → Minimalanleitung aus `references/skill-katalog.md` + Skill-Vertrag).
2. Eingaben übergeben: Planungsakte + nur die **relevanten** Artefakte.
3. Artefakt unter dem Dateinamen laut Skill-Vertrag speichern.
4. Planungsakte fortschreiben: Artefakt-Tabelle, Entscheidungen, neue Annahmen und
   Prüfaufträge.
5. Qualitätscheck des Skills lesen; ❌ einmal nachbessern lassen; bleibt es, in der Akte
   vermerken.
6. Eine Zeile Fortschritt an die Lehrkraft („✔ 20 Lernsituation – Analysebogen 15× trifft
   (eher) zu, 1× eher nicht: offene Lösungswege → nachgeschärft").

**Große Vorhaben** (mehr als rund acht Artefakte oder mehrere Lernsituationen): blockweise
arbeiten – eine Lernsituation bzw. ein Materialpaket je Durchgang –, Fortschritt in der
Planungsakte festhalten (fertig · offen · als Nächstes), damit über mehrere Sitzungen
weitergearbeitet werden kann. Vor dem Abschluss die **Vollständigkeit des Materialsatzes**
prüfen: je Arbeitsblatt Erwartungshorizont, je geplanter Stunde Verlaufsplan, je Lernsituation
mit mehreren Materialien eine Lehrerhandreichung.

**Parallel arbeiten**, wo die Umgebung Subagenten erlaubt und Schritte unabhängig sind (z. B.
Differenzierung zu AB 1 und AB 2; Linkcheck parallel zum Faktencheck). Jeder Subagent erhält:
Pfad zur SKILL.md, Planungsakte, Eingabedatei, Zieldateiname. Abhängige Schritte bleiben
nacheinander.

### 5. Qualitäts-Gates

| Gate | nach | Bestanden, wenn … | sonst |
|---|---|---|---|
| **G1 Planung** | Lernsituation bzw. Entwurf | Analysebogen ohne „trifft nicht zu", höchstens 2× „trifft eher nicht zu"; Kompetenzen niveaugerecht; Zeitsumme stimmt; Zeichnungen als SVG aus Spec (`zeichnungen_pruefen.py` ohne ❌); im BG zusätzlich Lerngebiet und Schuljahrgang/Phase richtig, Rückwärtsprobe des Kompetenzrasters ohne Lücke, Querschnittscheck (`references/berufliches-gymnasium.md`) | nachschärfen, dann weiter; im Modus Schrittweise Freigabe einholen |
| **G2 Material** | Material, Bloom, Differenzierung | jede Aufgabe mit Operator und Erwartungshorizont; Taxonomie-Verteilung im Ziel oder begründet; Ziel in allen Varianten gleich; Material für Lernende kurz, offen gestellt, mit Darstellungen, ohne Dekoration (`schuelermaterial_pruefen.py` ohne ❌, `references/schuelermaterial.md`); Zeichnungen auch in Lösung und Lehrerteil als SVG (`zeichnungen_pruefen.py` ohne ❌) | betroffenes Material überarbeiten |
| **GE Experiment** | experiment-planen (vor jedem Schülerversuch) | `versuch_pruefen.py` ohne ❌; Gefährdungsbeurteilung als Entwurf mit Entsorgung, Notfall, Vorversuch; Freigabezeile vorhanden | kein Einsatz – die Lehrkraft prüft, führt den Vorversuch durch und trägt die Freigabe selbst ein; der Skill gibt nie frei |
| **G3 Abschluss** | material-pruefen | kein offener ❌-Befund der Schwere „kritisch"; Ampel mindestens 🟡; Artefakte untereinander konsistent | korrigieren oder als Prüfauftrag ganz oben im Abschlussbericht |
| **GV Veröffentlichung** | schuelerseiten-veroeffentlichen, ki-kennzeichnung, ki-chatbot-einrichten (vor jeder Weitergabe an Lernende oder Öffentlichkeit) | `ausgabe_pruefen.py` ohne ❌ (keine Lösungen, Lehrerhinweise, Planungsnotizen, Personendaten); jede Seite gekennzeichnet; Chatbot: `anweisung_pruefen.py` ohne ❌ und alle Pflichttests des Probelaufs ✓; Freigabezeile der Lehrkraft (`freigabe_pruefen.py` ✅ bzw. `Freigabe Chatbot: erteilt`) | nicht veröffentlichen; Quelle korrigieren, neu erzeugen |

### 6. Konsistenz über alle Artefakte
Vor dem Abschluss abgleichen: gleiche Handlungssituation, Leitidee, Namen, Zahlen,
Zeitrichtwerte, Kompetenzen und Begriffe in Lernsituation, Entwurf und Material. Die Leitidee
der Stunde konkretisiert die der Lernsituation (`leitidee_ls` in der Planungsakte) und
widerspricht ihr nicht. Abweichungen beheben.

### 7. Abschlussbericht
`99_abschlussbericht.md` nach `references/abschlussbericht-vorlage.md`: Paketübersicht
(Datei, Zweck, Status), Ampel, Empfehlung für Bildungsgangteam (Abstimmung, Beschluss,
Evaluation), Qualitätscheck (Gates, Konsistenz), **konsolidierte Prüfaufträge nach Priorität**
mit zentralen Annahmen, Übergabe mit nächsten Schritten. In der Antwort an die Lehrkraft: 5–10 Zeilen Zusammenfassung + Link/Pfad zum
Ordner.

## Abhängigkeiten (Reihenfolgeregeln)
1. `dqr-zuordnen` vor allem anderen – **nur**, wenn das Niveau unklar ist oder geprüft werden soll.
2. `lernsituation-dokumentieren` vor `unterrichtsentwurf-erstellen` und
   `unterrichtsmaterial-erstellen`, wenn neu geplant wird.
3. `unterrichtsmaterial-erstellen` vor `bloom-taxonomie` (Analyse), `sprachsensibel-ueberarbeiten`
   und `differenzierung-erstellen`.
4. `sprachsensibel-ueberarbeiten` vor `differenzierung-erstellen` (Hilfen bauen auf dem
   überarbeiteten Text auf).
5. `material-pruefen` immer **zuletzt**; bei vorhandenem Material zusätzlich **zuerst**.
6. Kein Schritt doppelt, kein Schritt ohne Abnehmer: Jedes Artefakt muss im Ziel-Paket gebraucht
   werden.
7. `unterrichtsentwurf-analysieren` nach `unterrichtsentwurf-erstellen`;
   `unterricht-reflektieren` nach der gehaltenen Stunde – seine Konsequenzen gehen in die
   Planung der Folgestunde (`unterrichtsentwurf-erstellen`).
8. Werkzeug-Skills: `fachdiagramm-erstellen` und `quizfragen-erstellen` nach dem Material
   (jede Zeichnung eines Artefakts entsteht dort als SVG, nie als Zeichnung aus Zeichen)
   und vor `material-pruefen`; Ausspielen (`lernlandkarte-erstellen`,
   `schuelerseiten-veroeffentlichen`) nach G3; `ki-kennzeichnung` erst nach der Prüfung durch
   die Lehrkraft, vor bzw. mit `schuelerseiten-veroeffentlichen`; Weitergabe nur nach GV.
9. `agiles-lernen-mit-ki`: Lernpfad für Lernende nach Lernsituation und Material (Quellen =
   geprüftes Material, Fragenpool aus `quizfragen-erstellen`); AIS-Paket wie Ausspielen erst
   nach G3 und Weitergabe nur nach GV. Lernt die Lehrkraft selbst, steht der Skill allein.
10. `experiment-planen`, `programmieraufgabe-erstellen`, `technikfolgen-abschaetzen` wie
    `unterrichtsmaterial-erstellen`: nach Lernsituation bzw. Entwurf, vor `bloom-taxonomie` und
    `material-pruefen`; Experimente zusätzlich durch **GE** vor dem Einsatz.
11. Berufliches Gymnasium: Lerngebiet statt Lernfeld, Schuljahrgang und Phase statt
    Ausbildungsjahr, Notenpunkte
    (`references/berufliches-gymnasium.md`).
12. `ki-chatbot-einrichten`: Chatbot für Lernende nach G3 (Hintergrundwissen = geprüftes
    Material ohne Musterlösungen); Freischalten nur nach Probelauf und GV. Modus C (vorhandenen
    Systemprompt begutachten) steht allein. Nie auf Seiten mit Schülerdaten, nie zum Bewerten.
13. Vorhandene Lernsituation: `lernsituation-analysieren` zuerst (Ausgangsbefund 21), überarbeitet
    wird danach mit `lernsituation-dokumentieren` B – nicht im Prüfbericht.

## Grenzen und Verantwortung
- Ergebnisse sind **Entwürfe**. Fachliche Richtigkeit, Rechtskonformität und Einsatz
  verantwortet die Lehrkraft bzw. das Bildungsgangteam.
- Keine Schülerdaten in der Planungsakte; Lerngruppen nur zusammenfassend.
- **Keine Bewertung durch KI:** Leistungen einzelner Lernender bewertet die Lehrkraft, nicht
  die KI (DSGVO Art. 22, KI-Verordnung Anhang III Nr. 3 🔎); keine Schülerarbeiten mit Namen in
  die Sitzung (`references/leitplanken-bewertung.md`).
- **Begutachtung von Entwürfen und Unterrichtsreflexion** nur als Selbstcheck oder kollegiale
  Beratung – nicht für Auswahlverfahren, dienstliche Beurteilung oder die Benotung von
  Prüfungsunterricht.
- Prüfungsrelevante Entwürfe (Vorbereitungsdienst): Selbstcheck erlaubt, **gekennzeichnet**
  (`pruefungsrelevant: true`, Hinweise statt fertiger Formulierungen, KI-Nutzung im Entwurf als
  Hilfsmittel); Regeln des Studienseminars zur KI-Nutzung beachten – der Abschlussbericht weist
  darauf hin.
- **SchuCu-BBS 2024 ist verbindlich:** Begriffe, Kompetenzmodell und Phasen der Leitlinie in
  allen Artefakten; Vorgaben anderer Länder werden nicht übernommen.
- **KI-Einsatz der Lernenden ist geregelt und begründet:** Klassenregeln (einmal am Anfang),
  KI-Phasen je Einheit mit einem Satz Begründung, Zeichen 🚫 Ohne KI · 💡 KI zum Verstehen ·
  🔧 Mit KI arbeiten am Arbeitsschritt (`references/ki-vereinbarungen.md`). Entscheiden,
  Überprüfen und Reflektieren bleiben Leistung der Lernenden.

## Beispielaufrufe
> „Ich brauche für Industriemechaniker im 1. Jahr eine Lernsituation zur Wartung eines
> Förderbands nach SchuCu 2024 – mit Material für die erste Doppelstunde. In der Klasse sind
> drei SuS mit Deutsch als Zweitsprache."

> „Hier ist unser Ordner mit Material zu LF 6 (Anhang). Mach alles einsatzfertig und sag mir,
> was ich noch prüfen muss."

> „BG Technik, Jg. 13, Lerngebiet ING3: Projekt-LS Wasserstoffanlage für ein Einfamilienhaus mit
> Lastenheft, Elektrolyse-Versuch und ESP32-Messwerterfassung."

## Referenzen – wann lesen
- `references/rezepte.md` – **immer** in Schritt 3.
- `references/skill-katalog.md` – Ein-/Ausgaben, Minimalanleitungen, optionale Fremd-Skills.
- `references/planungsakte-vorlage.md` – Schritt 2.
- `references/abschlussbericht-vorlage.md` – Schritt 7.
- `references/skill-vertrag.md` – gemeinsamer Standard aller Skills.
- `references/schucu-bbs-2024.md` – Bezugsrahmen für Gates und Konsistenz.
- `references/didaktische-leitidee.md` – Leitidee von Lernsituation und Stunde abgleichen (Schritt 6).
- `references/leitplanken-bewertung.md` – bei Rezepten R10, R18 und R19 sowie prüfungsrelevanten Entwürfen (Datenschutzstufen, Freigabe, Kennzeichnung, Recht).
- `references/curriculum-abgleich.md` – bei R8 (Teilkompetenzen, Abdeckungsmatrix, Kern vs. Konkretisierung).
- `references/berufliches-gymnasium.md` – bei Vorhaben im Beruflichen Gymnasium (R16, R17, G1).
- `references/querschnittsaufgaben.md` – BNE, Demokratie-, Europa- und Medienbildung (G1, R17).
- `references/lektionsmuster.md` – bei R20 (Kursprojekt überarbeiten: Elemente einer Lektion, Reihenfolge, Prüfung).
- `references/ki-vereinbarungen.md` – wenn Lernende KI nutzen oder bewusst nicht nutzen sollen: drei Ebenen (Klasse, Unterricht, Aufgabe), Zeichen, Voreinstellung je Phase, Begründungen, Prüffragen.
- `references/schuelermaterial.md` – Gate G2: Material für Lernende kurz, offen, anschaulich, ohne Dekoration (Prüfung mit `scripts/schuelermaterial_pruefen.py`).
