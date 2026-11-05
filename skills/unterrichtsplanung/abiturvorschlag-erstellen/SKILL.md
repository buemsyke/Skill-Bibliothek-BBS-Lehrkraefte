---
name: abiturvorschlag-erstellen
description: Erstellt genehmigungsfähige Vorschläge für die dezentrale Abiturprüfung am Beruflichen Gymnasium in Niedersachsen (Technik mit Schwerpunkt, Berufliche Informatik) – Vorschlag A und B mit Schülermaterial (Handlungssituation, Funktionsbeschreibung mit Betriebsmittelkennzeichen, Aufgaben mit BE und EPA-Operatoren, Anlagen) und Lehrermaterial (unterrichtliche Voraussetzungen, Erwartungshorizont mit AFB je Zeile, Musterlösung mit Bewertungsmerkmal je BE), dazu Bewertungsbogen, Bewertungsmappe und Begleitblatt. Formuliert eindeutig und korrekturfreundlich und prüft per Skript nach dem Katalog der Begutachtung. Verwenden bei „Abiturvorschlag erstellen“, „dezentrale Abiturklausur“, „Abiturklausur Technik“, „Vorschlag A und B“, „Erwartungshorizont fürs Abitur“. Nicht für Klausuren im Halbjahr (klausur-erstellen) und nicht zum Begutachten fertiger Vorschläge.
metadata:
  version: "1.22"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Abiturvorschlag erstellen (dezentral, Berufliches Gymnasium)

## Zweck
Vorschläge für die dezentrale Abiturprüfung bauen, die
1. **die Begutachtung ohne Auflagen bestehen** – Maßstab ist derselbe Katalog wie beim Begutachten
   (`references/pruefkriterien-abitur-bg-technik.md`);
2. **eindeutig formuliert** sind – was die Lösung bestimmt, steht im Schülermaterial; in der
   Steuerungstechnik tragen alle Teile dieselben Betriebsmittelkennzeichen;
3. **nachvollziehbar und leicht zu korrigieren** sind – jede BE hängt an einem beobachtbaren
   Bewertungsmerkmal (im getrennten Bewertungsraster), sodass eine Zweitkorrektur zum selben Ergebnis
   kommt; Randvermerke und Gutachten sind kurz, weil sie von Hand in jede Arbeit geschrieben werden;
4. **knapp** sind – Schülermaterial höchstens 12 Seiten ohne Anlagen, Lehrermaterial ohne
   Bepunktungstabellen, damit Begutachtung und Fachgruppe wenig zu prüfen haben.

Ergebnis ist ein Entwurf. Verantwortung: Lehrkraft und Fachgruppe; Genehmigung: Schulbehörde.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · Kopf und Pflichtabschnitte
(Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis) **im Begleitblatt** –
Schüler- und Lehrermaterial bleiben einreichungsfertig. Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Vertraulichkeit
Unveröffentlichte Abiturvorschläge sind vertraulich: nur in der von Schule bzw. Land
freigegebenen KI-Umgebung bearbeiten, Kopf `vertraulich: true`, keine Daten von Lernenden.
Vorschläge anderer Schulen und echte Prüfungsunterlagen nicht als Vorlage einspielen – Aufbau und
Muster stehen in eigenen Worten in `references/abitur-aufgabenformat.md`.

## Geltungsbereich und Standardwerte

| | Standard (sonst ⚠️ Annahme) |
|---|---|
| Fach | Technik mit Schwerpunkt (BT, ET, IT, MT, GMT, ING); Berufliche Informatik |
| nicht | Mechatronik (zentral geprüft; der schuleigene Teil ist nicht Gegenstand 🔎), Klausuren im Halbjahr, mündliche Prüfung |
| Umfang | Vorschlag A **und** B; eA, 300 min, 120 BE (2,5 min/BE) |
| Gliederung | 3 Aufgaben à 40 BE; 4–7 Teilaufgaben je Aufgabe (3–15 BE), jede mit Titel |
| AFB | 30/40/30 (36/48/36 BE), Ziel ±5, Grenze ±10 Prozentpunkte; in jeder Aufgabe I, II und III |
| Bewertung | Notenpunkte nach Bewertungsmaßstab 95 … 45/40/33/27/20 % (`references/notenschluessel.md`) |

## Eingaben
- **Pflicht (sonst Rückfrage):** Fach und Schwerpunkt, Prüfungsjahr, **Kursfolge** 12.1–13.2
  (verbindliche Lerngebiete, gewähltes optionales, schulisches in 13.2) und der **tatsächliche
  Unterrichtsstand je Kurshalbjahr** (Inhalte, Tätigkeiten, Software, Notation).
- **Wichtig, sonst Annahme:** Hilfsmittel (Tabellenbuch mit Ausgabe, Taschenrechner,
  Formelsammlung), PC-Arbeitsplatz und Software, **Steuerungsplattformen** des Unterrichts (SPS,
  Kleinsteuerung, Mikrocontroller mit Board), Kennzeichnung und Notation (Standard: Notationsblatt,
  `references/notation-steuerungstechnik.md`; Kennbuchstaben DIN EN IEC 81346-2:2020 mit Klasse und
  Unterklasse: „-SJ1“; Ausgabe 2009 nur, wenn so unterrichtet), Themenwünsche, Unterrichtshinweise der
  Fachgruppe.
- **Optional:** Planungsakte, Lernsituationen der Kurse, Rückmeldungen früherer Begutachtungen.

## Leitlinien (verbindlich)
1. **Maßstab ist der Katalog der Begutachtung.** Jede Kennung (1.1–S.4) bekommt im Begleitblatt
   einen Nachweis. Strenger als die zentralen Vorbilder: deren Formulierungen nicht übernehmen,
   wo der Katalog sie beanstandet (`references/abitur-aufgabenformat.md`, Abschn. 7).
2. **Nur Unterrichtetes, konkret belegt** (2.3, 3.2, X.14): beide verbindlichen Lerngebiete und
   das gewählte optionale; jede Aufgabe verbindet mindestens zwei Lerngebiete; nichts aus nicht
   gewählten optionalen Lerngebieten. Der Bezug je Aufgabe nennt Inhalte, Tätigkeiten, Software und
   was neu ist – ein Halbjahresthema reicht nicht.
3. **Neu, nicht geübt:** Die konkrete Aufgabe kam im Unterricht nicht in dieser Form vor;
   Notation, Software und Verfahren sind vertraut.
4. **Eine Handlungssituation** (3.3, 3.4, 3.1): fiktiver Betrieb „(fiktiv)“, Rolle als Fachkraft,
   ein Projektauftrag; jede Aufgabe ist ein Arbeitsschritt; übergeordnete Kompetenzen der RRL
   gezielt ansprechen (Varianten vergleichen, Modellgrenzen, Technikfolgen).
5. **Teilaufgabe = Titel, BE, Situationsabsatz, Auftrag** (4.4, 4.5, X.2, X.9): Operator am
   Satzanfang im Imperativ „Sie“, nur aus der EPA-Liste des Fachs
   (`references/operatoren-epa-technik.md`); praktische Operatoren (speichern, erstellen …) nur mit
   vorangestelltem EPA-Operator und als erweiterte Operatoren mit AFB im Lehrermaterial.
6. **Eindeutiger Auftrag** (K.7, 4.1): ein Operator je Satz; Umfang als Zahlwort („zwei“,
   „alle“), nie „mindestens“; Bedingungen ausformuliert statt „ggf.“; Kriterien genannt statt
   „geeignet“/„sinnvoll“; keine W-Fragen, kein „kurz“; Antwortformat vorgegeben (Tabellenkopf mit
   Beispielzeile, Vorlage als Anlage, Ergebnisform). Muster: `references/aufgabenqualitaet.md`.
7. **Angaben, die die Lösung festlegen** (K.4, 4.2): Werte mit Einheit, Vereinfachungen
   ausdrücklich, Kennwerte in einer Anlage (nicht „aus dem Tabellenbuch“), Auswahlregel
   („nächstgrößerer Normwert“), Rundung; abhängige Teilaufgaben mit Ersatzwert – plausibel, aber
   nicht das richtige Ergebnis.
8. **Steuerungstechnik – Betriebsmittelkennzeichen** (T.1–T.9): Technologieschema mit
   Text-Legende; die Funktionsbeschreibung nennt **jedes** Betriebsmittel mit Kennzeichen, jeden
   Geber mit Kontaktart (NO/NC) und Signalbedeutung, jeden Aktor mit Wirkung, Grundstellung, Start,
   Stopp/Not-Halt (oder ausdrücklich ausgeklammert), Zeiten als Zahlen. Dieselben Kennzeichen und
   Bezeichnungen in Legende, Zuordnungsliste, Aufgaben, Anlagen und Musterlösung; ein neues
   Betriebsmittel wird in der Teilaufgabe eingeführt, nie erst in der Lösung. **Kennbuchstaben nach
   DIN EN IEC 81346-2:2020 immer mit Klasse und Unterklasse** (Standard der Fachberatung): -SJ1
   Taster, -BG1 Näherungsschalter, -KE1 SPS, -QA1 Schütz, -MA1 Motor, -MM1 Zylinder, -PF1
   Leuchtmelder, -EA1 Leuchte – nie die Klasse allein (-S1, -M1); Tabelle in
   `references/normen-technik.md`. Ausgabe in den Hinweisen genannt, eine
   Ausgabe je Vorschlag. Sinngemäß für Bezeichner in Netzplänen, Klassendiagrammen und Code (K.9).
   **Einheitliche Notation:** Kennzeichen, Signale, Zuordnungsliste und GRAFCET (gezeichnet und in
   Textform) nach dem **Notationsblatt**, das als Anlage beiliegt (`references/notation-steuerungstechnik.md`;
   T.9: UND „·“, NICHT „¬“, Zeit „5s/X3“, Vergleich „[-BT1 > −16 °C]“, Folgeschritt nach „→“).
   **Plattformneutral:** lösbar mit SPS, Kleinsteuerung oder Mikrocontroller – Funktion als GRAFCET
   bzw. Logikplan, Analogwerte als physikalische Größe, Zuordnungsliste mit einer Spalte je Plattform
   und Anlage mit den Ein- und Ausgängen, Programm „in der im Unterricht verwendeten Sprache“,
   *Gleichwertig* für jede Plattform (`references/normen-technik.md`, Abschn. 4).
9. **Normgerechte Notation** (`references/normen-technik.md`): GRAFCET nach DIN EN 60848, SPS-Sprachen
   nach IEC 61131-3 (keine AWL – 2025 gestrichen), Schaltzeichen, Farben und Stopp nach
   DIN EN 60204-1, Formelzeichen der Regelungstechnik (e = w − x), Adressen aus den Beispielbereichen
   der RFCs, Datenmengen mit eindeutigem Vorsatz (kB oder KiB). Was die Lösung bestimmt und nicht
   genormt ist, legt die Aufgabe fest; „normgerecht“ im Merkmal in zählende Normelemente auflösen.
   Software- und Datenbankteile mit **Notationsrahmen als Anlage** (Signaturen, Index 0,
   Klassendiagramm, Struktogramm, SQL-Umfang) nach dem Vorbild der Ergänzenden Hinweise Informatik.
10. **AFB** (4.6, X.1, X.5): Einstieg jeder Aufgabe AFB I, Abschluss AFB III; erste Teilaufgabe nie
    AFB III; Zeilen-AFB im Bereich des Operators, höchstens zwei benachbarte AFB je Zeile;
    Abweichungen im Lehrermaterial begründen.
11. **Zeit** (4.3, X.7): 2,5–3,0 min/BE; Zeichen- und Schreibaufwand (GRAFCET, Schaltplan,
    Programm) einrechnen; Probebearbeitung durch eine Fachkollegin bzw. einen Fachkollegen.
12. **Jede BE ein beobachtbares Merkmal – im Bewertungsraster** (K.1–K.3, K.5, K.8): eigenes Dokument
    `…_A_bewertungsraster.md` (`assets/vorlage-bewertungsraster.md`), **nicht** im Lehrermaterial.
    Merkmaltabelle je Teilaufgabe (Art `fest` | `Kriterium` | `Urteil`, höchstens 3 BE, keine
    Wertwörter); Summe = BE der Teilaufgabe, BE je AFB = Erwartungshorizont; offene Aufgaben mit
    funktionalen Merkmalen, unabhängig von Schrittnummern und Namen der Musterlösung; `Urteil` ≤ rund
    30 % der BE.
13. **Kurztext je Merkmal** (K.10): Randvermerk und Gutachtentext, von Hand in jede Klausur
    geschrieben – höchstens vier Wörter und 30 Zeichen, **keine Werte** (keine IP-Adressen, Präfixe,
    Zahlen mit Einheit, Formeln, Code). Er benennt das Merkmal: „Broadcastadresse“, nicht die Adresse;
    „Ergebnis“, nicht „Ergebnis 16,59 MB“. Das Gutachten nennt nur teilweise und nicht erfüllte Merkmale.
14. **Regeln je Teilaufgabe** (K.4–K.6), im Bewertungsraster: *Gleichwertig* (Pflicht bei offenen
    Operatoren), *Folgefehler* (Pflicht bei Ersatzwerten), *Toleranz* (Pflicht bei Rechnung und
    Auswahl), *0 BE*.
15. **Erwartungshorizont und Musterlösung** (2.4, 2.5, X.4, X.8, X.10, X.13): eine Zeile je
    Operator, substantiviert und gleich lautend wie im Auftrag („Berechnen der …“); Summenzeilen
    mit allen vier Zahlen; **knapper** Lösungsgang je Teilaufgabe (Ergebnis, Zwischenergebnisse,
    Lösungsbilder), **mit Code nachgerechnet** – ohne Merkmaltabellen, ohne Wiederholung der Aufgabe (U.2).
16. **Formalien** (X.3, S.1–S.4, 2.6, 2.7): „BE“, nie „Punkte“; keine Platzhalter (Jahr, Schule,
    Softwareversion konkret); jede angekündigte Anlage vorhanden; Nummerierung lückenlos;
    Bewertungsmaßstab und Hilfsmittel vollständig.
17. **A und B gleichwertig, nicht austauschbar** (2.1): gleiche Zeit, BE, Lerngebiete und
    AFB-Profil; verschiedene Situation, Anlage und Aufgaben.
18. **Umfang** (U.1): Schülermaterial bis „B. Material“ **höchstens 12 Seiten** in der Word-Fassung;
    Anlagen kommen dazu, sollen aber nur enthalten, was Aufträge brauchen. Kürzen: Situationsabsätze
    auf die neue Information, Material in Anlagen, Abbildungen nur mit Auftrag
    (`references/aufgabenqualitaet.md`, Abschn. 10).

## Vorgehen
1. **Rahmen klären:** Fach, Schwerpunkt, Jahr, Kursfolge, Unterrichtsstand, Hilfsmittel. Zentral
   geprüfter Schwerpunkt → Hinweis und kein Vorschlag. Mit Planungsakte: Angaben übernehmen.
2. **Lerngebietsmatrix:** Zielformulierungen der Lerngebiete × Unterrichtsinhalte → was prüfbar ist
   (`references/berufliches-gymnasium.md`, `references/curriculum-abgleich.md`).
3. **Bauplan A und B** im Begleitblatt (`assets/vorlage-begleitblatt.md`): je Teilaufgabe
   Gegenstand, Operator(en), BE je AFB, Minuten, Lerngebiet, Unterrichtsbezug, Material, Merkmale.
   Erst wenn AFB, Takt, Lerngebiete und Gleichwertigkeit stimmen, Texte schreiben
   (`references/abitur-konstruktion.md`). **Informationstechnik und Berufliche Informatik:** je
   Teilaufgabe ein Muster aus `references/aufgabenmuster-informationstechnik.md` wählen (Kennung in
   den Bauplan), dessen Festlegungen ins Schülermaterial und den Prüfstein in die Merkmale übernehmen.
   **Steuerungstechnik, Mechatronik, Elektro- und Metalltechnik:** zuerst die Anlage planen (Schema,
   Funktionsbeschreibung, Material als Datenquelle jeder Teilaufgabe, Bauplan-Spalte *Quelle*), dann je
   Teilaufgabe ein Muster aus `references/aufgabenmuster-steuerungstechnik.md` (TA1–TA10, BA1–BA8,
   Datenblätter und Kataloge nach DM1–DM6).
4. **Schülermaterial** nach `assets/vorlage-schuelermaterial.md`; Abbildungen:
   Technologieschemata mit `technologieschema-erstellen` (Legende per `edu-technologieschema legende`,
   Kennzeichen nach 81346 geprüft), Blockschaltbilder, Struktogramme und Datenmodelle mit
   `fachdiagramm-erstellen` (Aufgaben- und Lösungsbild getrennt, Text-Legende, `<title>` „Abbildung N –
   Titel“) als `abbildungen/75_abitur_<kurztitel>_A_abbN_<thema>.svg`, Lösungsbilder
   `…_A_loesung_X-Y_<thema>.svg`; an der gewünschten Stelle mit `![Abbildung N: Titel](abbildungen/…svg)`
   einbinden, darunter kursiv die Bildunterschrift (sonst setzt `abitur_docx.py` sie nach der ersten
   Erwähnung ein); bei Steuerungstechnik die Anlagen „Ein- und Ausgänge der Steuerung“ und „Notation
   Steuerungstechnik“.
5. **Lehrermaterial** nach `assets/vorlage-lehrermaterial.md`: Unterrichtliche Voraussetzungen,
   ggf. abweichende AFB und erweiterte Operatoren, Erwartungshorizont, Bewertungsmaßstab, kurze Hinweise
   zur Bewertung, knappe Lösungsvorschläge; Rechnungen mit Code prüfen. **Bewertungsraster** nach
   `assets/vorlage-bewertungsraster.md`: Merkmaltabelle mit Kurztext und Regeln je Teilaufgabe.
   **Lösungsbilder** als SVG, nie als Zeichnung aus Zeichen: GRAFCET mit `technologieschema-erstellen`
   (`typ: grafcet`, Muster `spec-grafcet.yaml`; speichernde Aktionen mit `:=` und Pfeil), Funktionsplan und
   Netzplan dort aus Grundformen (`spec-fup.yaml`),
   Struktogramm, Ablauf, Klassen- und Datenmodell mit `fachdiagramm-erstellen`; Namen
   `abbildungen/75_abitur_<kurztitel>_A_loesung_X-Y_<thema>.svg`, eingebunden vor der Merkmaltabelle
   der Teilaufgabe (bzw. ans Ende des Lösungsvorschlags) und unter „Digitales Material“ gelistet. Der GRAFCET steht zusätzlich als
   Text-Tabelle (Zweitkorrektur, T.9), erzeugt mit dem Befehl `textform` aus `technologieschema-erstellen`.
6. **Selbstprüfung (lokal):**
   `python3 scripts/abitur_check.py A_schuelermaterial.md A_lehrermaterial.md [--fach informatik] --vergleich B_schuelermaterial.md B_lehrermaterial.md`
   (das Bewertungsraster mit gleichem Dateianfang liest das Skript mit, sonst `--raster`)
   – prüft Katalog, Korrigierbarkeit (K, mit Kurztexten K.10), Umfang (U.1 Seiten des Schülermaterials
   geschätzt, U.2 Lehrermaterial ohne Merkmaltabellen), Kennzeichen (T, über `scripts/bmk_pruefen.py`) und Zeichnungen
   (Z.1/Z.2, über `scripts/zeichnungen_pruefen.py`: ❌ Zeichnung aus Zeichen, eingebundene SVG mit
   Überlagerung oder Überlauf; ⚠ Mermaid, SVG ohne Spec – von Hand? –, schräge Leitungen). Alle ❌
   beheben, ⚠ beheben oder im Begleitblatt begründen; Zeile „Gesamtsummen …“ und Bewertungsmaßstab
   übernehmen. Satzlängen im Schülermaterial optional mit `scripts/lesbarkeit.py`.
   **Ohne Skriptausführung** (Assistent ohne Code): Summen, AFB je Aufgabe, Takt und BE-Grenzen von
   Hand rechnen, Kennzeichen-Tabelle (BMK × Fundort) aufstellen und im Begleitblatt zeigen; Seiten
   grob schätzen (rund 50 Zeilen à 100 Zeichen je Seite, Abbildungen nach Höhe).
   **Ältere Entwürfe** mit Merkmaltabellen im Lehrermaterial: `… --auslagern 75_…_A_bewertungsraster.md`
   schreibt das Raster (Kurztexte als Vorschlag – schärfen), danach Tabellen und Regeln im Lehrermaterial löschen.
7. **Lösbarkeitsprobe** im Rollenwechsel nach `references/loesbarkeit-methode.md`: jede Teilaufgabe
   nur mit dem Schülermaterial lösen; fehlende Angabe → ergänzen; Konfidenz < 75 → Prüfauftrag.
8. **Korrekturprobe:** je Teilaufgabe mit Merkmalen der Art *Kriterium* oder *Urteil* drei
   erfundene Antworten (vollständig, typischer Fehler, zulässige Alternative) mit der Merkmaltabelle
   bewerten; mehrdeutige Merkmale schärfen.
9. **Bewertungsbogen:** `python3 scripts/abitur_check.py SM.md LM.md --bewertungsbogen 75_…_A_bewertungsbogen.md` (aus dem Bewertungsraster),
   danach die **Bewertungsmappe** für Korrektur und Gutachten:
   `python3 scripts/bewertungsmappe.py 75_…_A_bewertungsbogen.md` → `75_…_A_bewertungsmappe.xlsx`
   (Excel und LibreOffice, ohne Makros; Aufbau: `references/aufgabenqualitaet.md`, Abschn. 7). Je Merkmal
   ein Kurztext aus dem Raster – Randvermerk in der Klausur, Bemerkung je Teilaufgabe und Gutachten sind
   wortgleich; das Gutachten nennt standardmäßig nur teilweise und nicht erfüllte Merkmale.
   Kurztexte vor Korrekturbeginn mit der Fachgruppe abstimmen; nach Änderungen am Erwartungshorizont
   Bogen und Mappe neu erzeugen (das Skript überschreibt nie).
10. **Begleitblatt** abschließen: Einreichungscheckliste, Qualitätscheck, Annahmen und
    Prüfaufträge, Übergabe. Vorbegutachtung durch eine zweite Lehrkraft empfehlen.

## Ausgabe
- `75_abitur_<kurztitel>_A_schuelermaterial.md`, `…_A_lehrermaterial.md`, `…_A_bewertungsraster.md`,
  `…_A_bewertungsbogen.md`, `…_A_bewertungsmappe.xlsx`, dasselbe für B, und `75_abitur_<kurztitel>_begleitblatt.md`. Keine Namen
  von Schulen oder Lehrkräften in Dateinamen.
- Die Bewertungsmappe ist leer (keine Daten von Prüflingen). Ausgefüllt wird sie nur lokal von den
  Korrigierenden; eine ausgefüllte Mappe nie in die KI-Umgebung laden.
- Kopf nach Skill-Vertrag mit `vertraulich: true`; Pflichtabschnitte nur im Begleitblatt.
- **Word-Fassung** in der Dokumentvorlage der Behörde (lokal):
  `python3 scripts/abitur_docx.py 75_…_A_schuelermaterial.md 75_…_A_lehrermaterial.md --vorlage ORDNER [--schule "BBS …"] [--seiten]`
  – `ORDNER` enthält die Vorlagen für Schüler- und Lehrermaterial (DOCX der Behörde, nicht im Skill;
  auch `--vorlage DATEI.docx` oder Umgebungsvariable `ABITUR_VORLAGE`). Kopf- und Fußzeile aus dem
  Dateikopf (Jahr, Fach und Schwerpunkt, Vorschlag, Niveau, Bearbeitungszeit, Schule), BE der Aufgaben
  rechtsbündig, Erwartungshorizont im Layout der Vorlage, Seitenumbruch vor Erwartungshorizont und
  Musterlösung, Metadaten der Vorlage ersetzt. Abbildungen: `![…](…)` an Ort und Stelle, Platzhalter
  `[Abbildung N: …]` durch die Datei `…_abbN_…`, sonst nach der ersten Erwähnung im Text (gemeldet);
  Lösungsbilder vor die Merkmaltabelle der Teilaufgabe. SVG mit PNG-Ersatzbild (`rsvg-convert`).
  `--seiten` zählt die Seiten über LibreOffice (Schülermaterial ohne Anlagen ≤ 12). Überschreibt nur mit `--ueberschreiben`. Ohne Vorlage entsteht eine schlichte Fassung mit gleicher
  Kopfzeile. Die Endfassung in Word sichten und erneut prüfen – 
  `scripts/bmk_pruefen.py` liest auch DOCX und PDF.

## Qualitätscheck
- [ ] Kursfolge und Bezug je Aufgabe konkret; nur Unterrichtetes; ≥ 2 Lerngebiete je Aufgabe?
- [ ] Eine Handlungssituation; Aufgaben neu, nicht aus dem Unterricht?
- [ ] Aufträge eindeutig (ein Operator je Satz, Zahlwort, Kriterien, keine vagen Wörter)?
- [ ] Alles, was die Lösung bestimmt, im Schülermaterial (Werte, Kennwerte, Regeln)?
- [ ] Steuerungstechnik: Kennzeichen in Funktionsbeschreibung, Legende, Liste, Aufgaben und Lösung gleich?
- [ ] Kennbuchstaben nach DIN EN IEC 81346-2:2020 mit Klasse und Unterklasse (-SJ1, -MA1; Ausgabe genannt); GRAFCET, Schaltzeichen, Adressen normgerecht?
- [ ] Notationsblatt als Anlage; Steuerungsaufgaben mit SPS, Kleinsteuerung und Mikrocontroller lösbar?
- [ ] Alle Abbildungen und Lösungsbilder als SVG aus Specs (mit `.drawio.svg`), keine Zeichnung aus Zeichen (Z.1/Z.2 ✅)?
- [ ] AFB 30/40/30 (Ziel ±5, Grenze ±10 Prozentpunkte) und in jeder Aufgabe I–III; erste Teilaufgabe nicht AFB III?
- [ ] Takt 2,5–3,0 min/BE; 120 BE; Summen SM = Erwartungshorizont?
- [ ] Jede BE an einem Merkmal im Bewertungsraster; Korrekturprobe ohne Mehrdeutigkeit?
- [ ] Kurztexte höchstens vier Wörter, ohne Werte (K.10)?
- [ ] Schülermaterial ohne Anlagen ≤ 12 Seiten; Lehrermaterial knapp, ohne Merkmaltabellen (U.1, U.2)?
- [ ] Musterlösung vollständig, mit Code nachgerechnet; Bewertungsmaßstab gerechnet?
- [ ] A und B gleichwertig, nicht austauschbar; `abitur_check.py` ohne ❌?

## Beispielaufrufe
> „Erstelle zwei Abiturvorschläge für Technik – Informationstechnik, Abitur 2027. Kursfolge:
> 12.1 IT2, 12.2 IT1, 13.1 IT4, 13.2 IT6. Unterrichtsstand und Hilfsmittel im Anhang."

> „Dezentrale Abiturklausur Ingenieurwissenschaften (ING1, ING2, ING4), mit SPS-Teil und
> Tabellenkalkulation als Hilfsmittel – Vorschlag A und B mit Erwartungshorizont."

> „Abiturvorschlag Berufliche Informatik, eA: Modellierung, Algorithmen, Datenbanken."

## Referenzen – wann lesen
- `assets/vorlage-schuelermaterial.md`, `assets/vorlage-lehrermaterial.md`,
  `assets/vorlage-bewertungsraster.md`, `assets/vorlage-begleitblatt.md` – **immer** (Ausgabeformat).
- `references/aufgabenqualitaet.md` – **immer**: Auftragssatz, Angaben, Antwortformat,
  Betriebsmittelkennzeichen, Merkmale und Kurztexte, Bewertungsbogen, Korrekturprobe, Umfang
  (K.1–K.10, U.1–U.2, T.1–T.9).
- `references/notation-steuerungstechnik.md` – **bei Steuerungstechnik**: einheitliche Notation für
  Kennzeichen, Signale, Zuordnungsliste, GRAFCET und Programm; Teil „Anlage“ geht ins Schülermaterial.
- `references/normen-technik.md` – **bei Steuerungs-, Netzwerk-, Mess- und Softwareaufgaben**:
  Kennbuchstaben nach DIN EN IEC 81346-2:2020 (mit Ausgabe 2009), GRAFCET, IEC 61131-3, Schaltzeichen,
  Sicherheit und Farben, Einheitssignale und Pt100, Regelungstechnik, Verkabelung und Adressen, UML,
  Größen und Einheiten.
- `references/abitur-konstruktion.md` – Bauplan, AFB, Unterrichtsbezug, A/B, PC- und Informatikaufgaben.
- `references/abitur-aufgabenformat.md` – wie Abituraufgaben gestellt werden (Analyse, Kennzahlen, Mängel;
  Entwicklung 2023–2026 in Mathematik, Informatik, Mechatronik; **Regeln für Informationstechnik**, Abschn. 10).
- `references/aufgabenmuster-informationstechnik.md` – **bei Informationstechnik und Berufliche
  Informatik**: Aufgabentypen und Fragestellungen als Schablonen mit Festlegungen, Prüfstein und
  Merkmalen (Bauprinzipien B1–B14, Denkmuster F1–F10, Mikrocontroller, Software, Netzwerke/IoT, KI,
  Daten), Operatoren beider EPA-Listen, Aufgabenfluss.
- `references/aufgabenmuster-steuerungstechnik.md` – **bei Steuerungstechnik und Mechatronik**: die
  Anlagenaufgabe nach dem Vorbild der zentralen Mechatronik-Aufgabe 2025 I – Bauprinzipien BA1–BA8, Schema
  als Datenquelle, authentische Datenblätter und Kataloge (DM1–DM6), Aufgabentypen TA1–TA10 mit Festlegungen,
  Prüfstein und Merkmalen, Aufgabenfluss mit Querbezügen.
- `references/abitur-aufgabenformat-vergleich.md` – Vergleichsbeispiele aus einem anderen Land (2018/19–2023/24):
  Formate, Themen, Operatorenabgleich, Fundstellen der Muster; Format und Operatoren bleiben niedersächsisch.
- `references/pruefkriterien-abitur-bg-technik.md` – Katalog der Begutachtung (Einreichungscheckliste).
- `references/schuelermaterial.md` – nur zur Abgrenzung: Das Abiturformat hat eigene Richtwerte (Auftrag bis
  rund 45 Wörter, `references/aufgabenqualitaet.md`); die vier Regeln – kurz, offen statt kleinschrittig,
  anschaulich, ohne Dekoration – gelten sinngemäß.
- `references/loesbarkeit-methode.md` – Lösbarkeitsprobe (Schritt 7).
- `references/operatoren-epa-technik.md` – Operatoren und AFB (Technik, Berufliche Informatik).
- `references/berufliches-gymnasium.md` – Lerngebiete je Schwerpunkt, Abitur, Notenpunkte.
- `references/notenschluessel.md` – Bewertungsmaßstab; `references/curriculum-abgleich.md` – Lerngebietsmatrix.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte, Pflichtabschnitte.
- `scripts/abitur_check.py` (mit `scripts/bmk_pruefen.py` und `scripts/text_lesen.py`),
  `scripts/lesbarkeit.py`, `scripts/bewertungsmappe.py` (Excel-Mappe für Korrektur und Gutachten),
  `scripts/abitur_docx.py` (Word-Fassung in der Dokumentvorlage, Abbildungen an der richtigen Stelle) –
  lokal, nur Python-Standardbibliothek.
