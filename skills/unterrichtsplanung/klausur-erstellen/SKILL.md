---
name: klausur-erstellen
description: Erstellt schriftliche Leistungsüberprüfungen für berufsbildende Schulen – Klassenarbeit, Klausur (auch Qualifikationsphase des Beruflichen Gymnasiums mit EPA-Operatoren, BE und Notenpunkten), Kurzklausur, Lernzielkontrolle (auch Single Choice), Nachschreib- und A/B-Variante – aus Lernsituation, Material oder Lernfeld-Auszug. Kurze Operator-Aufträge, wenig Schreiblast, Abbildungen als Material, Antwortraum je Operator; Erwartungshorizont mit Korrekturschablone, Punkten je Aspekt, Alternativen, Folgefehlern, AFB-Nachweis und Notenschlüssel; Selbstprüfung per Skript, geprüft wird nur Unterrichtetes. Verwenden bei „Klassenarbeit erstellen", „Klausur mit Erwartungshorizont", „Lernzielkontrolle", „Nachschreibarbeit", „B-Gruppe". Nicht für Moodle-Quizze (quizfragen-erstellen) und Abiturvorschläge (abiturvorschlag-erstellen).
metadata:
  version: "1.12"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  ersetzt: "klausur-erstellen 1.x (eduwerkzeuge)"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Klassenarbeit und Lernzielkontrolle erstellen

## Zweck
Eine schriftliche Leistungsüberprüfung bauen, die **prüft, was unterrichtet wurde**, in der
Bearbeitungszeit **ohne Tempo als heimliches Kriterium** lösbar ist und deren Erwartungshorizont
so konkret ist, dass eine Vertretung oder Zweitkorrektur zum selben Ergebnis kommt.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

**Vertraulichkeit:** Aufgabenteil und Erwartungshorizont tragen `vertraulich: true` im Kopf.
Keine Schülerdaten nötig (Datenschutzstufe 0); Schülerantworten gehören nie in diese Sitzung.

## Arten

| Art | Einsatz | Standard (sonst Annahme) |
|---|---|---|
| **Klassenarbeit / Klausur** | Ende einer Lernsituation oder des Lernfelds | 90 min Bearbeitungszeit, 60 Punkte, höchstens 10 Hauptaufgaben, AFB 30/40/30 |
| **Klausur im Beruflichen Gymnasium** (Qualifikationsphase) | Ende eines Lerngebiets oder Halbjahrs | 90–135 min 🔎 Fachkonferenz, Bewertungseinheiten (BE), Takt ≥ 2,0 min/BE, höchstens 6 Aufgaben, EPA-Operatoren, AFB 30/40/30, Notenpunkte; Angabe zum Unterrichtszusammenhang; ggf. PC-Software als Hilfsmittel (`references/berufliches-gymnasium.md`); dezentrale Abiturvorschläge: `abiturvorschlag-erstellen` |
| **Kurzklausur** | Ende einer Lernsituation | 45 min, 30 Punkte, 4–6 Aufgaben |
| **Lernzielkontrolle (LZK)** | unterwegs, Grundlagen sichern | 20–25 min, 20–25 Single-Choice- oder Kurzantwortfragen à 1 P, AFB 40/50/10 (sichert Grundlagen, daher wenig AFB III; anders als das Übungsquiz mit 40/40/20) |
| **Nachschreib- / B-Variante** | Nachschreiben, Sitznachbarn | gleiche Operatoren, AFB, Punkte und Struktur; anderer Kontext oder andere Zahlen |

## Eingaben
- **Pflicht (sonst Rückfrage):** Grundlage – Lernsituation, Material, Lernfeld-Auszug oder
  Themenliste **mit dem tatsächlichen Unterrichtsstand** (was wurde behandelt?).
- **Wichtig, sonst Annahme:** Art, Bearbeitungszeit, Gesamtpunkte, AFB-Verteilung,
  Hilfsmittel (Tabellenbuch, Formelsammlung, Taschenrechner), Anrede (Sie/du nach Schulregel),
  Notenschlüssel der Schule, Varianten.
- **Papierklausur, sonst Annahme:** Antworten von Hand im Aufgabenblatt oder digital; eigene
  oder fremde Aufsicht (dann Aufsichtsblatt); Operatoren im Unterricht besprochen oder auf
  Seite 1 zu erklären; Fach Informatik im BG → Operatoren der EPA Berufliche Informatik.
- **Optional:** Planungsakte, Erwartungshorizonte der Arbeitsblätter (typische Fehler als
  Ablenker), Abdeckungsmatrix des Lernfelds, frühere Arbeit zum Überarbeiten.

## Leitlinien (verbindlich)
1. **Erst unterrichten, dann prüfen.** Jede Teilaufgabe ist einer Lernsituation und einer
   Kompetenz zugeordnet (Spalte *Bezug*). Kein Stoff, der nicht – oder erst später –
   unterrichtet wird. Mit Abdeckungsmatrix: Spalte „geprüft in" füllen
   (`references/curriculum-abgleich.md` Abschn. 7).
2. **Ein durchgehender Fall.** Alle Aufgaben spielen in der Handlungssituation bzw. im
   Modellbetrieb, möglichst an **einem** Vorgang – neue Teilaufgabe, nicht die Aufgabe aus dem
   Unterricht. Keine neue Firma erfinden, die erst verstanden werden muss.
3. **Operator und AFB je Teilaufgabe** (`references/operatoren-afb.md`; im Beruflichen Gymnasium
   die EPA-Liste `references/operatoren-epa-technik.md`), genau ein AFB je Teilaufgabe. Einstieg mit AFB I (Sicherheit), Kern AFB II, Abschluss
   AFB III – **auch innerhalb jeder Aufgabe**: leichteste Teilaufgabe zuerst, AFB III am Ende;
   die Aufgabenfolge folgt dem Unterricht. **AFB III ist Beurteilung, nicht Umfang** („Beurteilen Sie … und begründen
   Sie" mit 6–8 P, kein Aufsatz); es geht auch kurz: alle Werte bestimmen, Testfall entwerfen,
   Lösung erweitern.
4. **Zeit in Minuten je Punkt auslegen, nicht in Punkten je Minute.** Richtwert ≥ 1,5 min/P
   (Klassenarbeit), Untergrenze 1,0; Klausur BG ≥ 2,0 min/BE (Abitur 2,5). Höchstens rund 10 Hauptaufgaben – jede weitere ist ein
   Kontextwechsel und prüft Schreibtempo mit. Minutensumme der Aufgaben < Bearbeitungszeit.
5. **Formate mischen:** Richtig/Falsch mit Berichtigung · Zuordnung · Kurzantwort · Rechnung
   mit Lösungsweg · Skizze/Schema · Text für einen Adressaten · Beurteilung mit Begründung.
6. **Punkte folgen der Leistung:** nennen ≈ 1 P je Aspekt, erläutern ≈ 2 P je Aspekt,
   beurteilen = Kriterium + Urteil + Begründung; halbe Punkte vermeiden.
7. **Teilaufgaben unabhängig lösbar:** Am besten aus den **Vorgaben** lösbar (Rechnung aus den
   Regeln, nicht aus dem selbst ergänzten Ergebnis). Baut eine Rechnung dennoch auf einem
   Ergebnis auf, einen Ersatzwert angeben („Rechnen Sie mit 12 kW weiter, falls …"). Der Ersatzwert ist **plausibel,
   aber nicht das richtige Ergebnis** – sonst verrät er die vorige Teilaufgabe; der
   Erwartungshorizont rechnet beide Wege. Keinen Ersatzwert für einen Schritt derselben
   Teilaufgabe. Folgefehler nicht doppelt bestrafen.
8. **Rechnen statt schätzen:** Musterlösung nachrechnen (mit Code, wenn verfügbar), Einheiten
   mitführen; AFB-Anteile und Notenschlüssel **rechnen**, nie abschreiben.
9. **Single Choice:** Lösungsbuchstaben gleich verteilt (Zielbuchstaben vorgeben), Ablenker
   falsch, aber denkbar; sachlich geordnete Optionen (Zahlen, Fristen) nicht umsortieren.
10. **Kurzer Auftrag, Denken in der Aufgabe.** Operator zuerst und fett, ein Auftrag je
    Teilaufgabe, Antwortumfang als Zahlwort („zwei Kriterien“, „alle Startwerte“), Vorgaben als
    Liste auslagern; Richtwert bis rund 40 Wörter (eigener Richtwert der Klausur, nicht die ~25 Wörter
    aus `references/schuelermaterial.md` – dessen vier Regeln gelten sinngemäß). Die Schwierigkeit liegt im Verfahren
    (Randfall, verneinte Bedingung, Fehlersuche), nicht in Lesemenge, Rechnen oder Schreiben;
    Zahlen kopfrechenbar, wenn kein Taschenrechner erlaubt ist. **Freitext höchstens rund 30 %
    der Punkte** (Spalte *Antwort*, vom Skript gerechnet).
11. **Antwortraum im Blatt, Format je Operator** (Feld, Tabelle, Rechenweg-Kasten,
    Zeichenkasten mit Maß, Linien nach Punkten); Punkte hinter dem Auftrag; Name auf jeder Seite;
    eine Aufgabe je Seite.
12. **Abbildung trägt die Aufgabe:** Material zum Lesen, Lückenbild (①–⑤ im Bild, Tabelle
    daneben), fehlerhafte Fremdlösung, Zeichenkasten – in der Notation des Unterrichts, auf
    derselben Seite wie die Teilaufgaben, in Schwarzweiß lesbar; Lösungsbild nur im
    Erwartungshorizont. Jede Abbildung und jedes Lösungsbild als SVG aus einer Spec, nie als
    Zeichnung aus Zeichen: Abläufe, Struktogramme, Datenmodelle mit `fachdiagramm-erstellen`,
    Anlagenbilder, Schaltplanauszüge, GRAFCET, Funktionspläne und Netzpläne ebenso als SVG aus einer Spec
    ; einen GRAFCET zusätzlich als Text-Tabelle.
13. **Ein Material, drei Zugriffe, ein Prüfstein.** Jede Aufgabe arbeitet an einem Material
    (lesen/ausführen → bewerten → verändern) und enthält eine benannte Denkfalle; der
    Erwartungshorizont nennt sie und die Antworten, die 0 P. ergeben.
14. **Steuerungstechnik: dieselben Betriebsmittelkennzeichen überall.** Die Funktionsbeschreibung
    nennt jedes Betriebsmittel mit Kennzeichen (-SJ1, -BG2), Geber mit Kontaktart (NO/NC), dazu
    Grundstellung und Stopp; Legende des Technologieschemas, Zuordnungsliste, Aufgaben und
    Erwartungshorizont verwenden dieselben Kennzeichen – keine Kennung erst in der Lösung.
    Kennbuchstaben nach DIN EN IEC 81346-2:2020 immer mit Klasse und Unterklasse (-SJ1, -KE1,
    -QA1, -MA1, -MM1, -EA1; nie die Klasse allein); Ausgabe 2009 nur,
    wenn so unterrichtet und genannt; GRAFCET nach DIN EN 60848 (`references/normen-technik.md`).
    Einheitliche Notation nach `references/notation-steuerungstechnik.md` (als Anlage beifügen);
    Steuerungsaufgaben mit SPS, Kleinsteuerung oder Mikrocontroller lösbar (Zuordnungsliste mit
    einer Spalte je Plattform, Analogwerte im GRAFCET als physikalische Größe). Prüfen mit
    `python3 scripts/bmk_pruefen.py AUFGABEN.md ERWARTUNGSHORIZONT.md` (T.1–T.9).

Begründungen, Beispiele und Anti-Muster: `references/klausur-gutepraxis.md`; Auftrag, Antwortraum,
Abbildung, Seitenaufbau, Aufsicht: `references/druckfassung-antwortformate.md`.

## Vorgehen
1. **Grundlage sichten:** Lernsituation(en), Material, Unterrichtsstand; Kompetenzen und
   Inhalte listen, die geprüft werden dürfen. Mit Planungsakte: Handlungssituation, Namen und
   Zahlen übernehmen.
2. **Bauplan:** Tabelle Aufgabe · Gegenstand · Operator · AFB · Antwort · Punkte · Min. · Bezug –
   zuerst den Bauplan, dann die Texte. AFB-Soll, Takt und Freitextanteil hier schon einhalten;
   je Aufgabe das Material und den Prüfstein festlegen. In Informationstechnik und Informatik je
   Teilaufgabe ein Muster aus `references/aufgabenmuster-informationstechnik.md` (Kennung in den
   Bauplan; Festlegungen B1–B14 ins Aufgabenblatt).
3. **Aufgabenteil schreiben** nach `assets/vorlage-klausur.md`: Kopf mit Bearbeitungszeit,
   Hilfsmitteln und Gesamtpunkten, Hinweise auf dem Blatt, Fallschilderung, Aufgaben im Format
   `Aufgabe N – Titel (insgesamt P Punkte)` und Teilaufgaben `N.n **Operator** … (p P)` mit
   kursiver Zeile `*Antwortraum: …*`, Anlagen mit eigener Überschrift. Abbildungen mit
   `fachdiagramm-erstellen` als SVG erzeugen (Aufgaben- und
   Lösungsbild getrennt, Lösungsbilder `…_loesung_…`).
4. **Erwartungshorizont schreiben** nach `assets/vorlage-erwartungshorizont.md`: je
   Teilaufgabe erwartete Leistung als bepunktbare Aspekte, zulässige Alternativen,
   Toleranz- und Folgefehlerhinweis, Prüfstein; **Korrekturschablone** (eine Seite);
   Punkteübersicht mit Antwortformat; AFB-Nachweis; Notenschlüssel; Hinweise zur Korrektur;
   bei Single Choice der Lösungsspiegel mit Begründung je Frage.
5. **Selbstprüfung (lokal):**
   `python3 scripts/klausur_check.py ERWARTUNGSHORIZONT.md [--typ klassenarbeit|klausur-bg|lzk] [--system 15|ihk] [--sc …]`
   – alle ❌ beheben, ⚠ beheben oder im Qualitätscheck begründen; dazu
   `python3 scripts/zeichnungen_pruefen.py AUFGABEN.md ERWARTUNGSHORIZONT.md` (keine Zeichnung aus
   Zeichen). Die ausgegebene
   Notenschlüsseltabelle und die Zeile „Gesamtsummen …" in den Erwartungshorizont übernehmen.
   Alternativ Notenschlüssel mit `edu-bewertung schluessel --max N [--system ihk]`.
   **Ohne Skriptausführung** (Assistent ohne Code): dieselben Prüfungen von Hand rechnen –
   Summen, Takt, AFB-Anteile, Grenzen = Prozent × Gesamtpunkte, auf halbe Punkte aufgerundet –
   und die Rechnung im Qualitätscheck zeigen.
6. **Aufsichtsblatt** bei fremder Aufsicht nach `assets/vorlage-aufsichtsblatt.md`.
7. **Varianten** (falls gewünscht): gleiche Bauplantabelle, anderer Kontext bzw. andere Zahlen;
   eigener Erwartungshorizont; Selbstprüfung für jede Variante.
8. Qualitätscheck, dann ausgeben. Gegenlesen durch eine zweite Lehrkraft
   empfehlen (Lösbarkeit Schritt für Schritt).

## Ausgabe
- **Dateien:** `70_klausur_<kurztitel>.md` und `70_klausur_<kurztitel>_erwartungshorizont.md`;
  Varianten mit Suffix `_B`, `_nachschreiben`.
- Bei fremder Aufsicht zusätzlich `70_klausur_<kurztitel>_aufsicht.md` (bzw.
  `01_vorgabe/<kurztitel>_aufsicht.md`); die Prüflinge erhalten nur das Aufgabenblatt.
- Kopf nach Skill-Vertrag mit `vertraulich: true`; Pflichtabschnitte stehen im
  Erwartungshorizont (der Aufgabenteil bleibt druckfertig).
- Weiterverarbeitung: `pandoc DATEI.md -o DATEI.docx`; Layout-Skills wie `bbs2-arbeitsblatt`,
  falls installiert. Die Zeilen *Antwortraum: …* in der Word-Fassung als Felder, Linien und
  Kästen umsetzen, Name in die Kopfzeile jeder Seite, Seitenumbrüche vor den Aufgaben.

## Qualitätscheck
- [ ] Jede Teilaufgabe mit Bezug zu Lernsituation/Kompetenz; nichts Ununterrichtetes?
- [ ] Ein durchgehender Fall; Aufgaben neu, nicht aus dem Unterricht kopiert?
- [ ] Operator und genau ein AFB je Teilaufgabe; erste Aufgabe nicht AFB III?
- [ ] AFB-Verteilung gerechnet und im Soll (oder begründet); AFB steigt innerhalb jeder Aufgabe?
- [ ] Aufträge kurz (Operator zuerst, Zahlwort für den Umfang); Freitextanteil gerechnet (≤ rund 30 %)?
- [ ] Antwortraum je Operator; Abbildungen auf derselben Seite wie ihre Teilaufgaben; Prüfstein je Aufgabe benannt?
- [ ] Takt ≥ 1,5 min/P bzw. ≥ 2,0 min/BE im BG (oder begründet); ≤ 10 Hauptaufgaben; Minutensumme mit Reserve?
- [ ] Punktsumme = Gesamtpunkte (Aufgabenteil = Erwartungshorizont)?
- [ ] Erwartungshorizont mit Aspekten, Punkten, Alternativen, Toleranz, Folgefehlerregel, Korrekturschablone?
- [ ] Musterlösung nachgerechnet; Ersatzwerte für abhängige Teilaufgaben, abweichend vom richtigen Ergebnis?
- [ ] Notenschlüssel aus der Gesamtpunktzahl gerechnet; Schulregel benannt?
- [ ] Varianten gleich schwer (gleiche Operatoren, AFB, Punkte)?
- [ ] Steuerungstechnik: Kennzeichen in Funktionsbeschreibung, Liste, Aufgaben und Lösung gleich (`bmk_pruefen.py`)?
- [ ] `klausur_check.py` ohne ❌?
- [ ] Abbildungen und Lösungsbilder als SVG, `zeichnungen_pruefen.py` ohne ❌?

## Beispielaufrufe
> „Erstelle aus `20_lernsituation_gurtfoerderer.md` eine Klassenarbeit, 90 Minuten, 60 Punkte,
> Hilfsmittel Tabellenbuch und Taschenrechner, mit Erwartungshorizont und B-Variante."

> „Lernzielkontrolle nach LS 2: 20 Single-Choice-Fragen zu Schmierstoffen und Wartungsplan,
> 20 Minuten, Kammer-Schlüssel."

> „Klausur Technik, Jg. 13, Lerngebiet ING4, 135 Minuten, 60 BE, EPA-Operatoren, Notenpunkte."

## Referenzen – wann lesen
- `assets/vorlage-klausur.md`, `assets/vorlage-erwartungshorizont.md` – **immer** (Ausgabeformat).
- `references/klausur-gutepraxis.md` – Zeitauslegung, Formate, Single Choice, Varianten, Anti-Muster.
- `references/druckfassung-antwortformate.md` – **bei jeder Papierklausur**: Auftragstext, Antwortraum
  je Operator, Abbildungen, Seitenaufbau, Operatoren für Lernende, Aufsichtsblatt.
- `references/aufgabenmuster-informationstechnik.md` – **bei Informationstechnik und Informatik**:
  Aufgabentypen und Fragestellungen als Schablonen mit Festlegungen, Prüfstein und Merkmalen
  (Mikrocontroller, Modellierung, Algorithmen, Netzwerke/IoT, KI, SQL).
- `assets/vorlage-aufsichtsblatt.md` – bei fremder Aufsicht.
- `references/operatoren-afb.md` – Operatoren und AFB; `references/operatoren-epa-technik.md` – BG und Abitur.
- `references/berufliches-gymnasium.md` – Klausur im BG: Lerngebiete, BE, Notenpunkte, Hilfsmittel.
- `references/normen-technik.md` – Steuerungs-, Netzwerk-, Mess- und Softwareaufgaben: Kennbuchstaben,
  GRAFCET, IEC 61131-3, Mikrocontroller, Schaltzeichen, Sicherheit, Sensorik, Adressen, UML, Einheiten.
- `references/notation-steuerungstechnik.md` – Notationsblatt Steuerungstechnik (Anlage für Prüflinge).
- `references/notenschluessel.md` – Schlüssel und Rechtsrahmen.
- `references/curriculum-abgleich.md` – Bezug und Abdeckungsmatrix.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/klausur_check.py` – Selbstprüfung (lokal, nur Python-Standardbibliothek); `scripts/bmk_pruefen.py`
  (mit `scripts/text_lesen.py`) – Betriebsmittelkennzeichen in Steuerungsaufgaben abgleichen.
