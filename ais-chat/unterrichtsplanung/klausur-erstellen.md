<!-- Assistenten-Fassung des Skills 'klausur-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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
    Anlagenbilder, Schaltplanauszüge, GRAFCET, Funktionspläne und Netzpläne mit
    `technologieschema-erstellen`; einen GRAFCET zusätzlich als Text-Tabelle.
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
   `fachdiagramm-erstellen` bzw. `technologieschema-erstellen` als SVG erzeugen (Aufgaben- und
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

# ANHÄNGE

## Anhang: assets/vorlage-aufsichtsblatt.md

---
artefakt: Klassenarbeit – Aufsichtsblatt
titel: "[Thema der Arbeit]"
skill: klausur-erstellen
skill_version: "1.13"
stand: JJJJ-MM-TT
vertraulich: true
status: "KI-Entwurf – fachlich zu prüfen"
---

<!-- Nur für Arbeiten unter fremder Aufsicht. Die Prüflinge erhalten ausschließlich das
     Aufgabenblatt. Begründung und Regeln: references/druckfassung-antwortformate.md, Abschn. 9. -->

# Blatt für die aufsichtführende Lehrkraft

> **Bleibt bei der Aufsicht.** Die Prüflinge erhalten nur das [N]-seitige Aufgabenblatt.

**Fach:** [Fach] · **Klasse:** [Kurzbezeichnung] · **Thema:** [Thema] ·
**Dauer:** [90] Minuten · **Punkte:** [60]

| Zeit | Handlung |
|---|---|
| vor Beginn | Tische leerräumen, Handys in die Tasche vorne im Raum, Ersatzpapier bereitlegen |
| 0 min | Aufgabenblätter austeilen, Namen auf Seite 1 eintragen lassen, Vollständigkeit prüfen lassen ([N] Seiten) |
| 0–[90] min | Bearbeitungszeit |
| [90] min | Alle Aufgabenblätter einsammeln – mit allen Seiten und etwaigen Zusatzblättern |

**Zugelassen:** [Schreibzeug (Kugelschreiber oder Füller, nicht rot), Lineal].
**Nicht zugelassen:** [Taschenrechner, Handy, eigene Unterlagen].

Die Fachlehrkraft ist nicht im Raum. Bitte **keine inhaltlichen Auskünfte** geben – auch nicht
bei scheinbar harmlosen Rückfragen wie „[Muss der Nein-Zweig gezeichnet werden?]“ oder „[Was heißt
*Beurteilen*?]“ ([die Operatoren sind auf Seite 1 erklärt | vorab im Unterricht besprochen]).

| Situation | So verfahren |
|---|---|
| Frage zur Aufgabenstellung (Druckfehler, unleserlich) | Klären und unten notieren |
| Inhaltliche Frage | „Das ist Teil der Aufgabe.“ Notieren, wer wonach gefragt hat |
| Platz im Aufgabenblatt reicht nicht | Rückseite nutzen lassen oder Zusatzblatt ausgeben; Name und Aufgabennummer draufschreiben lassen, mit dem Aufgabenblatt einsammeln |
| Ein Prüfling wird krank | Abbruch und Uhrzeit notieren, Arbeit einsammeln |
| Täuschungsversuch | Sachverhalt notieren, Arbeit **nicht** abbrechen, der Fachlehrkraft melden |

**Notizen der Aufsicht:**

```
_____________________________________________________________________

_____________________________________________________________________
```

Aufgabenblätter bitte gesammelt im Fach der Fachlehrkraft ablegen: [Ort].

> KI-gestützt erstellt (Skill klausur-erstellen v1.13). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: assets/vorlage-erwartungshorizont.md

---
artefakt: Klassenarbeit – Erwartungshorizont
titel: "[Thema der Arbeit]"
skill: klausur-erstellen
skill_version: "1.13"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
art: "Klassenarbeit"
variante: "A"
vertraulich: true
status: "KI-Entwurf – fachlich zu prüfen"
---

# Erwartungshorizont: [Thema]

Bearbeitungszeit: [90] min · Gesamtpunkte: [60] · Bezug: [Lernsituation(en) Nr./Titel]

So konkret, dass eine Vertretung oder Zweitkorrektur zum selben Ergebnis kommt. Jeder Aspekt
ist einzeln bepunktbar.

## Korrekturschablone

Eine Seite zum Abhaken: [N] der [60] Punkte ([Items]) lassen sich direkt mit dieser Tabelle
korrigieren. Bei [Items mit Ermessen] gibt es mehrere richtige Antworten oder Teilpunkte; die
Regeln stehen in den Abschnitten darunter.

| Item | Lösung | P. |
|---|---|---:|
| 1.1 | 1 **A** · 2 **D** · 3 **B** · 4 **E** · 5 **F** | je 1 |
| 1.2 | [Beispiel mit Varianten siehe unten] | 1 + 1 |
| 2.1 | [ … ] | [ … ] |

## Aufgabe 1.1 – [Operator], AFB [I] – [2] P

| # | Erwartete Leistung | Punkte |
|---|---|---|
| 1 | [konkrete, beobachtbare Teilleistung] | 1 |
| 2 | [ … ] | 1 |

**Zulässige Alternativen:** [fachlich gleichwertige Antworten oder Wege mit voller Punktzahl]
**Toleranz:** [z. B. „auch … werten, wenn begründet"; Rundung ±…; Einheit fehlt → −… P]
**Typische Fehler / Teilpunkte:** [woran Teilleistungen erkennbar sind; Antworten, die **0 P.** ergeben]
**Prüfstein:** [Denkfalle der Aufgabe, z. B. Randfall, verneinte Bedingung – oder „keiner“]

Bei Kurzantworten mit mehreren Feldern (Buchstaben, Ausdrücke) je Feld eine Zeile:

| Feld | Lösung | Ebenfalls richtig | Falsch (0 P.) |
|---|---|---|---|
| ① | [ … ] | [gleichwertige Schreibweise] | [typischer Fehler] |

## Aufgabe 2.1 – [Berechnen], AFB [II] – [6] P

| # | Erwartete Leistung | Punkte |
|---|---|---|
| 1 | Formel: [ … ] | 1 |
| 2 | Werte mit Einheiten eingesetzt: [ … ] | 2 |
| 3 | Ergebnis: [Wert mit Einheit, sinnvoll gerundet] | 2 |
| 4 | Plausibilität / Antwortsatz | 1 |

**Folgefehler:** Rechenweg mit falschem Zwischenwert aus [ … ] richtig fortgeführt → volle
Punkte für die Folgeschritte (Folgefehler **einmal** werten).
**Teilpunkte:** richtiges Ergebnis **ohne** Rechenweg höchstens [1 von 2] P.; Soll und Ist
vertauscht (Testen) höchstens [die Hälfte].

## Aufgabe [n] – [Beurteilen], AFB [III] – [8] P

| # | Erwartete Leistung | Punkte |
|---|---|---|
| 1 | Kriterium 1 benannt und auf den Fall angewendet | 2 |
| 2 | Kriterium 2 benannt und auf den Fall angewendet | 2 |
| 3 | Urteil eindeutig | 1 |
| 4 | Begründung schlüssig, Gegenargument abgewogen | 3 |

**Erwartungsspielraum:** [beide Entscheidungen sind vertretbar, wenn …]
**Keine Punkte:** [Kriterien ohne Bezug zum Adressaten; Kriterium genannt, aber nicht angewendet]

## Punkteübersicht

| Aufgabe | Gegenstand | Operator | AFB | Antwort | Punkte | Min. | Bezug |
|---|---|---|---|---|---:|---:|---|
| 1.1 | [ … ] | [nennen] | I | Kurz | 2 | 3 | [LS 1 · K1] |
| 1.2 | | | I | Kurz | 4 | 6 | |
| 2.1 | | [berechnen] | II | Rechnung | 6 | 9 | |
| 2.2 | | | II | Kurz | 6 | 9 | |
| [n].1 | | [beurteilen] | III | Text | 8 | 12 | |
| **Σ** | | | | | **[60]** | **[≤ 85]** | |

*Antwort* = Format der Antwort im Blatt: `Kurz` (Buchstabe, Zahl, Ausdruck, Tabellenzelle),
`Rechnung`, `Skizze`, `Text` (Schreiblinien). `klausur_check.py` rechnet daraus den
Freitextanteil.

## AFB-Nachweis (gerechnet mit `scripts/klausur_check.py`)

| AFB | verlangt wird | Punkte | Anteil |
|---|---|---|---|
| I | [wiedergeben, beschreiben] | [18] | [30 %] |
| II | [anwenden, berechnen, auswählen] | [24] | [40 %] |
| III | [beurteilen, begründen] | [18] | [30 %] |

    Gesamtsummen (AFB I, AFB II, AFB III, gesamt) [18] [24] [18] [60]

## Notenschlüssel ([15-Punkte-System | Kammer-Schlüssel | Schulregel])

[Tabelle aus `klausur_check.py` bzw. `edu-bewertung schluessel --max [60]` einsetzen]

## Lösungsspiegel Single Choice (nur Lernzielkontrolle)

| Frage | Lösung | warum richtig | AFB | Bezug |
|---|---|---|---|---|
| 1 | [C] | [Begründung in einem Satz] | I | [LS 1] |

## Hinweise zur Durchführung und Korrektur

- **Vorher ankündigen:** [Seiten, Aufgaben, Antworten direkt ins Blatt, Hilfsmittel]. Operatoren
  vorab besprechen (besonders *Beurteilen*, *Entwerfen*, *Erweitern*) – oder auf Seite 1 erklärt.
- **Korrektur:** erst alle Arbeiten mit der Schablone, danach die Items mit Ermessen ([ … ]).
  Folgefehler werden einmal gewertet ([z. B. 5.1 → 5.2]).
- **Nach der Korrektur:** Punkte je Teilaufgabe erfassen;
  besonders aussagekräftig sind die Items mit Prüfstein ([ … ]).
- **Bewusst nicht geprüft:** [Themen, die unterrichtet werden, aber nicht Gegenstand dieser
  Arbeit sind – verhindert Streit bei der Rückgabe].
- **Aufsicht:** [eigene Aufsicht → `vorlage-aufsichtsblatt.md`; sonst „Fachlehrkraft“]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Bezug jeder Teilaufgabe zu LS/Kompetenz | | |
| AFB-Verteilung (gerechnet) | | |
| Aufträge kurz, Antwortraum je Operator, Freitextanteil (gerechnet) | | |
| Takt und Minutensumme | | |
| Punktsumme Aufgabenteil = Erwartungshorizont | | |
| Musterlösung nachgerechnet | | |
| `klausur_check.py` ohne ❌ | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Art, Zeit, Punkte, Notenschlüssel: …
- Aufsichtsblatt (bei fremder Aufsicht): `vorlage-aufsichtsblatt.md`
- Empfohlen: Gegenlesen durch eine zweite Lehrkraft (Lösbarkeit Schritt für Schritt)

> KI-gestützt erstellt (Skill klausur-erstellen v1.13). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: assets/vorlage-klausur.md

---
artefakt: Klassenarbeit – Aufgabenteil
titel: "[Thema der Arbeit]"
skill: klausur-erstellen
skill_version: "1.13"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
art: "Klassenarbeit | Kurzklausur | Lernzielkontrolle | Nachschreibarbeit"
variante: "A"
vertraulich: true
status: "KI-Entwurf – fachlich zu prüfen"
---

<!-- Format so lassen: „Aufgabe N – Titel (insgesamt P Punkte)" und Teilaufgaben „N.n … (p P)".
     Daran erkennen klausur_check.py und die regelbasierte Begutachtung
     Punkte und Struktur. Anlagen bekommen eine eigene Überschrift „Anlage N – …".
     Kursive Zeile *Antwortraum: …* unter einer Teilaufgabe = Vorgabe für die Druckfassung
     (Formate nach references/druckfassung-antwortformate.md, Abschn. 5). Name in die Kopfzeile
     jeder Seite, „Seite x von n“ in die Fußzeile. Auftrag: Operator zuerst, fett, höchstens
     rund 40 Wörter. -->

# [Art]: [Thema]

| Klasse | Fach / Lernfeld | Datum | Name |
|---|---|---|---|
| [Kurzbezeichnung] | [LF-Nr. – Titel] | __________ | ______________________ |

Bearbeitungszeit: [90] min · Gesamtpunkte: [60] · Hilfsmittel: [Tabellenbuch, nicht
programmierbarer Taschenrechner]

**Hinweise:**

- Schreiben Sie Ihre Lösungen **direkt in dieses Aufgabenblatt** – in die Kästen, Tabellen und auf
  die Linien bei der jeweiligen Aufgabe. Reicht der Platz nicht, schreiben Sie auf der Rückseite
  weiter und notieren dort die Aufgabennummer.
- Schreiben Sie mit Kugelschreiber oder Füller, nicht mit Rot. [Zeichnungen mit **Lineal**.]
- Wo ein Buchstabe verlangt ist, tragen Sie **genau einen** Buchstaben je Feld ein.
- [Alle Rechnungen gehen ohne Taschenrechner.] Beim Berechnen und Testen gehört der **Rechenweg**
  zur Lösung.
- Der **fett gedruckte Operator** am Anfang jeder Teilaufgabe legt fest, was Ihre Antwort
  enthalten muss. [Operatorentabelle hier oder vorab im Unterricht besprochen.]
- Die Teilaufgaben sind unabhängig voneinander lösbar; wo ein Ergebnis weiterverwendet wird, ist
  ein Ersatzwert angegeben.

| Aufgabe | 1 | 2 | … | Summe |
|---|---|---|---|---|
| **Punkte** | [6] | [12] | | **[60]** |

## Ausgangslage

[3–6 Sätze: derselbe Betrieb bzw. dieselbe Handlungssituation wie im Unterricht, ein neuer
Vorgang. Personen und Firma erkennbar fiktiv.]

## Aufgabe 1 – [Titel] (insgesamt [6] Punkte)

1.1 **[Bezeichnen]** Sie [Inhalt] [Bedingung: genau eine / zwei / alle …]. ([2] P)
*Antwortraum: Buchstabenfeld je Zeile (ein Buchstabe bleibt übrig)*

1.2 **[Bestimmen]** Sie … ([4] P)
*Antwortraum: Lückensatz „Die Zahl ___ wird ersetzt durch ___.“*

## Aufgabe 2 – [Titel] (insgesamt [12] Punkte)

2.1 **[Berechnen]** Sie … ([6] P)
*Antwortraum: Kasten „Rechenweg“, Ergebnisfeld mit Einheit*

2.2 **[Auswählen]** Sie … Rechnen Sie mit [Ersatzwert] weiter, falls Sie 2.1 nicht lösen konnten. ([6] P)
*Antwortraum: Ankreuzfelder*

## Aufgabe [n] – [Titel] (insgesamt [8] Punkte)

[n].1 **[Beurteilen]** Sie … Stützen Sie Ihr Urteil auf zwei Kriterien. ([8] P)
*Antwortraum: Feld für das Urteil, [8–10] Schreiblinien*

## Anlage 1 – [Titel]

[Tabelle, Datenblattauszug (mit Quelle) oder `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz]`.
Abbildung auf derselben Seite wie ihre Teilaufgaben; Lücken nummeriert ①–⑤ im Bild, Tabelle
daneben – Muster in `fachdiagramm-erstellen`.]

---

| Aufgabe | 1 | 2 | … | Σ |
|---|---|---|---|---|
| Punkte erreicht | | | | |
| Punkte möglich | [6] | [12] | | [60] |

Note: ________ · Datum, Kürzel: ________

## Anhang: references/aufgabenmuster-informationstechnik.md

# Aufgabenmuster Informationstechnik – Aufgabentypen, Fragestellungen, Bauprinzipien

Wiederverwendbare Muster für Prüfungs- und Übungsaufgaben in Informationstechnik und Informatik –
Berufliches Gymnasium (Schwerpunkt Informationstechnik, Berufliche Informatik) und IT-Bildungsgänge
der Berufsschule. **Herkunft:** Auswertung der Abiturprüfungen Informationstechnik am Beruflichen
Gymnasium eines anderen Landes 2018/19–2023/24 (Aufgabenhefte und Musterlösungen), Stand 01.11.2026 –
in eigenen Worten, keine Aufgabentexte übernommen, alle Beispiele erfunden. Verbindlich bleiben die
Vorgaben Niedersachsens: Format, Operatorenliste des Fachs, Erwartungshorizont mit
Bewertungsmerkmalen. Die Muster sind Baupläne für Fragestellungen, keine Texte zum Abschreiben.

## Inhalt
1. Gebrauch
2. Operatoren für die Schablonen
3. Bauprinzipien – was die Lösung eindeutig macht (B1–B14)
4. Denkmuster – Fragestellungen für jedes Themenfeld (F1–F10)
5. Hardwarenahe Informationsverarbeitung und Mikrocontroller (H1–H10)
6. Software und objektorientierte Modellierung (S1–S10)
7. Netzwerke und vernetzte Systeme (N1–N10)
8. KI-Grundlagen (K1–K5)
9. Daten: ER-Modell und SQL (D1–D2)
10. Muster verketten – Aufgabenfluss
11. Was nicht übernommen wird
12. Kurzprüfung je Teilaufgabe

---

## 1. Gebrauch

- **Bauplan:** Je Teilaufgabe ein Muster wählen und seine Kennung notieren (`S1`, `F2` …), dann die
  Schablone auf den eigenen Fall übertragen.
- **Aufbau jedes Musters:** *Schablone* – Auftrag mit Platzhaltern ‹…›; *Festlegen* – was im
  Material stehen muss, damit es genau eine richtige Lösung oder klar umrissene gleichwertige
  Lösungen gibt; *Prüfstein* – die eingebaute Denkfalle, die Können von Raten trennt (gehört mit
  den Antworten, die 0 BE erhalten, in den Erwartungshorizont); *Merkmale* – beobachtbare
  Bewertungsmerkmale und *Gleichwertig*.
- **AFB und BE sind Richtwerte:** Der AFB liegt im Bereich des Operators und hängt vom Unterricht
  ab; die BE folgen den Vergleichsheften (Teilaufgaben meist 1–8 Punkte) und werden am Takt des
  eigenen Formats geprüft.
- **Material für Lernende:** Die Muster liefern Spezifikation, Beispiele und Testfälle; Teilschritte
  gehören in gestufte Hilfen, nicht in den Auftrag (`schuelermaterial.md`, falls vorhanden).

## 2. Operatoren für die Schablonen

Die Schablonen nutzen Operatoren, die in beiden EPA-Listen stehen (`operatoren-epa-technik.md`):
*beschreiben, berechnen, bestimmen, darstellen, erläutern, ermitteln, zeichnen, skizzieren,
begründen, entwerfen, entwickeln, beurteilen, Stellung nehmen*. Wo die Listen sich unterscheiden:

| Leistung | Fach Technik | Berufliche Informatik |
|---|---|---|
| fehlende Teile in eine Vorlage eintragen | „Entwickeln Sie ‹Diagramm› in Anlage N weiter.“ – *ergänzen* und *vervollständigen* sind keine EPA-Operatoren | „Vervollständigen Sie …“ |
| gegebene Lösung um eine Anforderung erweitern | „Entwickeln Sie ‹Lösung› so weiter, dass …“ | „Erweitern Sie …“ |
| Fachbegriff oder Wert angeben | „Nennen Sie …“ | „Bezeichnen Sie …“, „Benennen Sie …“ |
| Ablauf an einem Diagramm nachvollziehen | „Beschreiben Sie …“ (I), „Ermitteln Sie …“ (II) | „Ermitteln Sie …“ |
| Lösung mit einem Testfall prüfen | „Überprüfen Sie ‹Operation› mit dem Testfall …“ | „Testen Sie …“ |
| Programmteil schreiben | „Entwickeln Sie ‹Operation› in Pseudocode oder in der im Unterricht verwendeten Programmiersprache.“ | ebenso, oder „Implementieren Sie …“ |
| Begriff am Beispiel klären | „Erläutern Sie …“ (*erklären* ebenfalls zulässig) | „Erläutern Sie …“ |
| zwei Lösungen gegenüberstellen | „Vergleichen Sie … anhand von ‹Kriterium›.“ | „Diskutieren Sie … anhand von ‹Kriterium›.“ |

Formatanweisungen („Tragen Sie … in Anlage N ein.“) stehen hinter dem Operator, nie an seiner
Stelle. Fragen als Auftrag („Was bedeutet …?“, „Hat sie recht?“) werden zu „Nennen Sie …“ bzw.
„Beurteilen Sie die Aussage …“.

## 3. Bauprinzipien – was die Lösung eindeutig macht

| Nr. | Prinzip | So umgesetzt |
|---|---|---|
| B1 | **Signale vollständig beschreiben** | je Eingang Aktivpegel (high- oder low-aktiv), prellfrei ja/nein, Flanke des Interrupts; je Ausgang die Wirkung; Anzeigetexte nummeriert („Text 2 = ‹Tor offen›“); Takt bzw. Zykluszeit |
| B2 | **Bezeichner vorgeben und durchziehen** | Namen von Zuständen, Operationen (mit Signatur), Variablen und Rollen stehen im Material; „die Zustände tragen die Namen aus Anlage N“; Abweichungen regelt eine Folgefehlerregel |
| B3 | **Plattform und Notation offen, Kenndaten verlangt** | „Pins frei wählbar; geben Sie die gewählten Pins an“, „Pseudocode oder die im Unterricht verwendete Programmiersprache“, „Struktogramm oder Programmablaufplan“; wer eine andere Plattform nutzt, nennt deren Kenndaten (Timertakt) |
| B4 | **Umfang begrenzen** | „Konstruktoren müssen nicht angegeben werden“, „Endzustände sind nicht gefordert“, „nur ‹Objekt› und die direkt verbundenen Objekte“, „Aufrufe innerhalb von ‹Operation› werden nicht dargestellt“ |
| B5 | **Zahl der gesuchten Elemente nennen** | „die fünf fehlenden Operationen“, „zwei Vorteile und einen Nachteil“, „alle Assoziationen“ |
| B6 | **Beispiel und Gegenbeispiel** | je zu entwickelnder Operation ein Aufruf mit Ergebnis *wahr* und einer mit *falsch* bzw. ein Aufruf, der das Format der Rückgabe zeigt („liefert [4.5, 12.0]“) – zugleich der erste Testfall im Erwartungshorizont |
| B7 | **Randfall regeln** | ausschließen („Gehen Sie davon aus, dass die Liste mindestens ein Element enthält.“) oder festlegen („Ohne Einträge liefert die Operation 0.0.“) – nie offen lassen |
| B8 | **Erlaubte Mittel festlegen** | zulässige Operationen der Datenstruktur (Notationsrahmen), bereitgestellte Hilfsoperation mit Signatur („`max(zahlen: Liste<GZ>): GZ` darf verwendet werden“), verbotene Sprachfunktionen („keine eingebauten Summen- oder Mittelwertfunktionen“) – sonst löst ein Bibliotheksaufruf die Aufgabe |
| B9 | **Konkrete Werte verlangen** | Sequenzdiagramm mit konkreten Werten für Parameter und Rückgabewerte; Objektdiagramm mit allen Attributwerten des Szenarios |
| B10 | **Geschlossenes Vokabular** | bei Modellierungen Zustände, Ereignisse, Wächter und Aktivitäten als Liste vorgeben („Verwenden Sie nur …“) – bewertet wird die Struktur, nicht die Wortwahl |
| B11 | **Teilvorgabe statt leeres Blatt** | Anfang des Sequenzdiagramms, Zustände mit unbeschrifteten Übergängen, Startzustand, Tabellenkopf mit Beispielzeile, Klassendiagramm ohne Operationen, Impulsdiagramm mit Achsen |
| B12 | **Konventionen setzen** | Router erhält die höchste (bzw. niedrigste) nutzbare Adresse; Teilnetze lückenlos ab ‹Adresse› nach absteigender Größe; Datumsformat; Indexbasis; Regel bei Gleichstand |
| B13 | **Abkürzen erlauben** | lange Rückgabetexte nachvollziehbar abkürzen, Parameter weglassen – wo Schreiben nichts prüft |
| B14 | **Erweiterung entkoppeln** | jede Erweiterung der Anlage (zweite Anzeige am Bus, Not-Halt-Zustand, Funkmodul) bringt ihre Angaben mit und braucht kein Ergebnis der Vorgängerin |

## 4. Denkmuster – Fragestellungen für jedes Themenfeld

**F1 Erst von Hand rechnen, dann den Algorithmus entwickeln** · AFB I/II, dann II/III · 2 + 5–7 BE
- Schablone: a) „Ermitteln Sie mit einer Rechnung, ob ‹Fall› die Regel ‹…› erfüllt.“
  b) „Entwickeln Sie die Operation ‹name(…): Typ›, die die Regel für beliebige ‹…› prüft.“
- Festlegen: Regel als Liste, Daten für a), Signatur und Rückgabe für b), Randfall (B7).
- Prüfstein: Filter oder Gewichtung der Regel (nur bestimmte Elemente zählen, Faktor).
- Merkmale: a) Rechenweg und Entscheidung; b) funktional wie S5. Der Datensatz aus a) ist der
  Testfall für b).

**F2 Aussage einer Person beurteilen** · AFB II/III · 2–3 BE
- Schablone: „‹Person› behauptet: ‚…‘ Beurteilen Sie die Aussage. Begründen Sie Ihr Urteil mit
  ‹einer Rechnung / Abbildung N›.“
- Festlegen: die Aussage als Zitat; womit begründet wird.
- Prüfstein: eine verbreitete Fehlvorstellung (höhere Dienstgüte ist immer besser; die Einheit
  eines Merkmals ist gleichgültig; Twisted Pair reicht für jede Strecke). Nicht jede Aussage ist
  falsch – sonst wird geraten (Kelvin statt °C verschiebt alle Werte gleich und ändert keine
  Distanz; Millimeter statt Meter ändert sie).
- Merkmale: Urteil (1), Begründung mit Beleg aus Rechnung oder Abbildung (1–2).

**F3 Vorschlag oder Lösung eines Kollegen beurteilen** · AFB III · 2–3 BE
- Schablone: „Ein Kollege schlägt vor, ‹…›. Beurteilen Sie den Vorschlag anhand von ‹Kriterium,
  Daten›.“
- Festlegen: Kriterium und Daten, die das Urteil tragen.
- Prüfstein: Der Vorschlag scheitert an einer Nebenwirkung, die erst beim Nachrechnen oder
  Durchspielen auffällt (Adressbedarf größer als das Netz; der Bandstopp verhindert, dass das
  letzte Teil gezählt wird; der Ablauf spricht ein Gerät an, das vorher nicht eingeschaltet wurde).
- Merkmale: Nachweis durch Rechnung bzw. Ablauf (1–2), Urteil (1).

**F4 Ablauf an einem Zustand durchspielen** · AFB I/II · 1–2 BE
- Schablone: „Das System befindet sich im Zustand ‹A›; ‹Ereignis› tritt ein. Beschreiben Sie die
  Aktionen im Folgezustand.“
- Prüfstein: entry- und do-Aktionen unterscheiden; ein Wächter, der nicht erfüllt ist.
- Merkmale: Folgezustand (1), alle Aktionen (1). Guter Einstieg in eine Aufgabe.

**F5 Realisierung begründen oder vergleichen** · AFB II/III · 2 BE
- Schablone: „Begründen Sie, warum ‹eine Lösung ohne Speicher› ‹die Drehrichtung› nicht erkennen
  kann.“ · „Vergleichen Sie ‹Warten durch Abfragen› und ‹Warten mit Timer-Interrupt› anhand der
  Prozessorauslastung.“
- Festlegen: das Vergleichskriterium.
- Prüfstein: gleiche Eingangssignale bedeuten je nach Vorgeschichte Verschiedenes → Gedächtnis.

**F6 Auswirkung einer Entwurfsentscheidung beschreiben** · AFB II/III · 1–3 BE
- Schablone: „In einem alternativen Entwurf ‹…›. Beschreiben Sie, wie sich dadurch ‹Reihenfolge,
  Last, Ergebnis› ändert.“
- Beispiele: Einträge je Person statt in einer gemeinsamen Liste → Anzeigereihenfolge; höhere
  Dienstgüte → Nachrichten am Broker; andere Skalierung → andere Gruppen.

**F7 Erweiterung beschreiben statt programmieren** · AFB III · 2 BE
- Schablone: „Beschreiben Sie, wie ‹die Interrupt-Service-Routine› erweitert werden muss, damit
  zusätzlich ‹Größe› bestimmt wird.“
- Merkmale: zu messende Größe und Ort der Messung (1), Umrechnung in die Zielgröße (1) – z. B. Zeit
  zwischen zwei Impulsen → Umdrehungen je Minute.
- Nutzen: Transfer am Ende einer Programmieraufgabe ohne zweiten langen Code.

**F8 Störung aus dem Betrieb beheben** · AFB III · 2 BE
- Schablone: Störung mit Ursache und Zahl schildern (‹Die Absaugung schaltet mit der Maschine ab;
  Späne im Rohr brauchen 3 s bis zum Behälter und setzen das Rohr zu.›) → „Beschreiben Sie eine
  Änderung des Zustandsmodells, die die Störung behebt.“
- Prüfstein: Die Zahl in der Schilderung führt zur Lösung (Nachlaufzustand mit Zeit).

**F9 Begriff am eigenen Fall erläutern** · AFB I/II · 1–2 BE je Begriff
- Schablone: „Erläutern Sie ‹Begriff› am Beispiel von ‹Klasse/Operation aus Anlage N›.“ ·
  „Begründen Sie mit dem Fachbegriff, warum ‹scheinbarer Fehler› kein Fehler ist.“
- Merkmale: Begriff fachlich richtig (1), Bezug auf ein Element des Materials (1). Eine auswendig
  gelernte Definition ohne Bezug erfüllt nur das erste Merkmal.

**F10 Rückwärts: Ergebnis gegeben, Ursache gesucht** · AFB II · 2–4 BE
- Schablone: „Bestimmen Sie aus ‹Routingtabelle / Impulsdiagramm / Ausgabe› ‹die Netzadressen /
  den Tastgrad / die Eingabewerte›.“
- Prüfstein: Erst eine Konvention (B12) macht die Umkehrung eindeutig.

## 5. Hardwarenahe Informationsverarbeitung und Mikrocontroller

**Material:** Blockdiagramm (Bedienelemente → Mikrocontroller → Aktoren) mit Signalnamen,
Signalbeschreibung nach B1, bei Bedarf UML-Zustandsdiagramm (oder GRAFCET, wenn so unterrichtet) –
als SVG aus einer Spec (Skill-Vertrag Abschn. 3).

**H1 Zustandsdiagramm um einen Ausnahmezustand erweitern** · AFB III · 3–4 BE
- Schablone: „Entwickeln Sie das Zustandsdiagramm in Anlage N weiter: Meldet ‹Sicherheitssensor›,
  geht die Steuerung aus jedem Bewegungszustand in den Zustand ‹HALT›; dort ‹Aktionen›. Mit ‹Taste›
  wird ‹…› fortgesetzt.“
- Festlegen: auslösendes Ereignis (Interrupt mit Flanke), Aktionen im neuen Zustand, Rückkehr.
- Prüfstein: Übergänge aus **allen** betroffenen Zuständen; der Rückweg.
- Merkmale: neuer Zustand mit Aktionen (1), Übergang aus jedem Bewegungszustand (1–2), Rückkehr mit
  Bedingung (1).

**H2 Zustandsdiagramm in ein Programm übertragen** · AFB II · 2 + 4–6 BE
- Schablone: a) „Stellen Sie die Zustandsdefinitionen und die Zustandsvariable mit Startwert dar.“
  b) „Entwickeln Sie die Hauptschleife nach dem Zustandsdiagramm in Anlage N; die Zustände tragen
  dessen Namen.“
- Festlegen: Startzustand, Aktivpegel der Geber (B1), vorhandene Operationen (‹motorStopp()›).
  b) arbeitet am vorgegebenen Diagramm, nicht an einem selbst erweiterten (B14).
- Prüfstein: low-aktive Endschalter werden auf 0 abgefragt; Aktion im Zustand oder beim Übergang.
- Merkmale: je Zustand Aktionen und Übergangsbedingung (1), Startzustand (1). Gleichwertig:
  Fallunterscheidung oder Verzweigungskette, Aufzählungstyp oder Konstanten, jede Nummerierung.

**H3 Initialisierung nach Liste** · AFB II · 2–3 BE
- Schablone: „Entwickeln Sie die Operation ‹init()› für: ‹externer Interrupt an Signal X, low-aktiv,
  fallende Flanke, freigegeben› · ‹PWM-Ausgang mit 1 kHz›.“
- Prüfstein: Flanke passend zum Aktivpegel, Pull-up bei low-aktivem Geber, Periodendauer aus der
  Frequenz.
- Merkmale: je Listenpunkt 1 BE. Gleichwertig: jede Plattform und Bibliothek des Unterrichts; nicht
  geforderte Angaben (Auflösung) frei.

**H4 Timer einstellen** · AFB II · 2 BE
- Schablone: „Bestimmen Sie Vorteiler und Endwert des Timers für ‹Blinken mit 2 Hz› bei ‹16 MHz
  Takt›.“
- Prüfstein: Beim Blinken wird zweimal je Periode umgeschaltet (2 Hz → alle 250 ms); Zählung ab 0
  (Endwert − 1, plattformabhängig).
- Merkmale: Zeitbasis aus dem Vorteiler (1), Endwert mit Rechenweg (1). Toleranz: jede Kombination
  mit exakter Zeit. *0 BE:* nur die Frequenz an eine Bibliotheksfunktion übergeben – die Frage nach
  den Werten ist damit nicht beantwortet.

**H5 Interrupt-Service-Routine** · AFB II · 1–4 BE
- Schablone: „Entwickeln Sie die Interrupt-Service-Routine, die ‹die Warnleuchte umschaltet / den
  Zähler erhöht / die Zeitmessung neu startet›.“
- Prüfstein: keine Warteschleife in der Routine; Statusbit zurücksetzen, wo die Plattform es
  verlangt (Gleichwertig: ohne, wo die Bibliothek es übernimmt).
- Merkmale: Wirkung (1), Rücksetzen bzw. Neustart (1).

**H6 Impulsdiagramm zeichnen** · AFB I/II · 2–3 BE
- Schablone: „Zeichnen Sie in Anlage N drei Perioden eines PWM-Signals mit ‹500 Hz› und Tastgrad
  ‹25 %›. Tragen Sie Periodendauer und Pulsdauer mit Wert ein.“
- Festlegen: Achsen mit Teilung (B11).
- Prüfstein: Tastgrad ungleich 50 % wählen – sonst sind Puls- und Pausendauer nicht unterscheidbar.
- Merkmale: Periodendauer mit Wert (1), Pulsdauer mit Wert (1), drei gleiche Perioden (1).

**H7 Wertebereich, Umrechnung, Begrenzung** · AFB II · 2–4 BE
- Schablone: „Berechnen Sie ‹die Winkeländerung je Raste / die Spannung je Digit›.“ · „Entwickeln
  Sie ‹die Hauptschleife›, die ‹die Pulsdauer› je Raste um ‹0,1 ms› ändert, höchstens bis ‹2 ms›
  und mindestens bis ‹1 ms›.“
- Prüfstein: Sättigung an beiden Grenzen; Umrechnung über den ganzen Bereich (Messkette).
- Merkmale: Rechnung (1), Begrenzung oben und unten (je 1).

**H8 Bus-Teilnehmer adressieren** · AFB I–III · 1–4 BE je Teilaufgabe
- Material: Datenblattauszug als Anlage (feste Adressbits, Adresspins, Datenrahmen).
- Schablonen: „Ermitteln Sie zwei mögliche Adressen in Binärdarstellung.“ · „Erläutern Sie, warum
  jeder Teilnehmer eine eigene Adresse braucht.“ · „Ermitteln Sie das Datenbyte für ‹Zustand› in
  Hexadezimaldarstellung.“ · „Entwickeln Sie ‹senden(wert)›.“
- Festlegen: **Schreibweise der Adresse** (7 Bit ohne Lese-/Schreibbit oder 8 Bit mit), Belegung
  der Ausgänge.
- Merkmale: je Adresse (1), je Datenbyte (1). Gleichwertig: jede Belegung der Adresspins, solange
  die Adressen verschieden sind.

**H9 Kurzaufgaben mit genau einer Antwort** · AFB I · je 1 BE
- Paritätsbit (gerade oder ungerade) zu zwei Bytes – eines mit gerader, eines mit ungerader
  Einsenzahl · Periodendauer aus der Frequenz · Dualdarstellung von Grenzwerten und größter
  darstellbarer Wert bei ‹n› Leitungen · Mindestdauer eines Tastendrucks bei Abtastung mit ‹f›
  bzw. Zykluszeit ‹t› (eine volle Periode).
- Nutzen: sicherer Einstieg, eindeutige Korrektur.

**H10 Schaltung oder Programm protokollieren, dann deuten** · AFB II · 2 + 2 BE
- Schablone: „Ermitteln Sie die Zählerstände (Variablenwerte) für die nächsten ‹n› Takte ab
  ‹Ereignis›; tragen Sie sie in Anlage N ein.“ – „Beschreiben Sie die Funktion der Schaltung (des
  Programms).“
- Festlegen: Startzustand, Protokolltabelle mit Kopf.
- Merkmale: Protokoll (je Abschnitt 1), Deutung mit Bezug zum Protokoll (1–2). Variante:
  Signalwechsel eines Drehgebers in beiden Richtungen tabellieren, danach F5.

## 6. Software und objektorientierte Modellierung

**Material:** Szenario mit Skizze der Oberfläche, unvollständiges Klassendiagramm als Anlage, ein
bis zwei Sequenzdiagramme zu benannten Szenarien („‹Kundin› leiht ‹Werkzeug› aus“),
Notationsrahmen (Datentypen, Signaturen, Listenoperationen).

**S1 Klassendiagramm aus Sequenzdiagramm vervollständigen** · AFB II · 2–4 BE je Teilaufgabe
- Schablone: „Das Sequenzdiagramm in Anlage N zeigt ‹Szenario›. Entwickeln Sie das Klassendiagramm
  in Anlage M weiter: Tragen Sie die ‹vier› fehlenden Operationen mit Sichtbarkeit, Parametern und
  Rückgabetyp ein.“ – eigene Teilaufgabe für Assoziationen mit Richtung, Multiplizität und
  Rollenname, bei Bedarf temporäre Beziehungen.
- Festlegen: Zahl der fehlenden Elemente (B5); Sichtbarkeitsregel (z. B. öffentlich nur, was eine
  andere Klasse aufruft); ob Konstruktoren und temporäre Beziehungen gefordert sind.
- Prüfstein: Die Operation gehört zur Klasse des **Empfängers**; der Rückgabetyp folgt aus der
  Antwortnachricht; Konstruktorparameter und Schleifen über Indizes verraten Assoziationen und
  Multiplizität *.
- Merkmale: je Operation (Name, Parameter, Rückgabetyp beim richtigen Empfänger) 1 BE oder je zwei
  Operationen 1 BE; Sichtbarkeit als eigenes Merkmal. Gleichwertig: Parameternamen.

**S2 Multiplizität und Einschränkung aus dem Fachtext** · AFB II · 1–2 BE
- Schablone: „Bestimmen Sie die Multiplizitäten der Assoziationen ‹rolleA› und ‹rolleB›.“ ·
  „Entwickeln Sie die Klasse ‹X› so weiter, dass ‹Attribut› nur Werte von ‹0› bis ‹15› annehmen
  kann.“
- Festlegen: Formulierungen im Fachtext, die die Grenze tragen („nicht jede …“, „genau vier …“).
- Prüfstein: 0..1 statt 1; feste Anzahl statt *.
- Merkmale: je Multiplizität 1. Gleichwertig: eine Alternative, die der Text zulässt (1..4, wenn
  auch weniger Belegungen erlaubt sind), im Erwartungshorizont nennen.

**S3 Sequenzdiagramm aus einer Beschreibung weiterentwickeln** · AFB II/III · 6–8 BE
- Schablone: „Entwickeln Sie das Sequenzdiagramm ‹Szenario› in Anlage N weiter. Verwenden Sie
  konkrete Werte für Parameter und Rückgabewerte.“
- Festlegen: Anfang vorgegeben (B11); Ablauf als nummerierte Schritte oder als Liste, was welche
  Operation liefert; Daten des Falls; was nicht dargestellt wird (B4); Abkürzungen (B13).
- Prüfstein: Schleife mit Grenze, Bedingung (opt, alt), Rückgabewert, der weitergereicht wird; ein
  Zwischenergebnis, das gerechnet werden muss (Durchschnitt aus vier Werten).
- Merkmale: Nachrichten an den richtigen Empfänger in richtiger Reihenfolge, je Fragment mit
  Wächter, Rückgabewerte mit konkreten Werten.

**S4 Struktogramm aus Sequenzdiagramm** · AFB II · 3–4 BE
- Schablone: „Entwickeln Sie aus dem Sequenzdiagramm in Anlage N das Struktogramm der Operation
  ‹op›.“
- Prüfstein: loop → Zählschleife mit richtigen Grenzen (0 bis Anzahl − 1); opt → einseitige
  Verzweigung; Rückgaben in lokale Variablen.
- Merkmale: Schleife (1), Bedingung (1), Aufrufe am richtigen Objekt (1–2).

**S5 Algorithmus zu einer Fachregel** · AFB II/III · 5–7 BE
- Schablone: „Entwickeln Sie die Operation ‹name(p: Typ): Typ› in Pseudocode oder in der im
  Unterricht verwendeten Programmiersprache.“ Davor die Regel als Liste, Beispiel und Gegenbeispiel,
  Randfall, erlaubte Mittel (B6–B8).
- Bewährte Regeltypen und ihr Prüfstein:

| Regeltyp | Prüfstein |
|---|---|
| Staffel mit Schwellen (Gebühr ab 14, 28, 42 Tagen) | Reihenfolge der Abfragen; „mehr als“ heißt echt größer |
| gefilterte Summe mit Gewicht (nur Pflichtmodule, doppelt gezählt) | Filter vergessen |
| Durchschnitt einer Teilmenge, die leer sein kann | Division durch 0 (B7) |
| Maximum und Mittelwert in einem Durchlauf | Startwert des Maximums aus dem ersten Element |
| nächsten passenden Eintrag ab der aktuellen Position suchen | Start bei Position + 1; Rückgabe *falsch*, wenn keiner folgt |
| zyklische Reihenfolge (… 8 – 9 – 1 – 2 …) | Umbruch nach dem letzten Wert; Abbruch, wenn keiner mehr passt |
| Häufigkeiten zählen, Mehrheit prüfen | Zählliste fester Länge; „mehr als die Hälfte“ heißt echt größer |
| verkettete Liste: hinten anhängen | leere Liste; bis zum letzten Knoten laufen |

- Merkmale funktional, unabhängig von Variablennamen: Initialisierung (1), Schleife über alle
  Elemente (1), Bedingung bzw. Filter (1–2), Aktualisierung (1), Rückgabe (1), Randfall (1).
  Gleichwertig: Pseudocode oder Sprache des Unterrichts, Zähl- oder Iteratorschleife.

**S6 Objektdiagramm aus einem Szenario** · AFB II · 3–4 BE
- Schablone: „Entwickeln Sie das Objektdiagramm für ‹Ausschnitt des Szenarios›. Die Objekte heißen
  ‹werkzeug[3]› …“
- Festlegen: Ausschnitt (B4), Objektnamen, geforderte Attributwerte.
- Prüfstein: Objekt der Unterklasse mit geerbten Attributen; Verbindung statt kopiertem Wert; zwei
  Objekte derselben Klasse.
- Merkmale: je Objekt mit Klasse (1), Attributwerte (1), Verbindungen (1).

**S7 Zustandsdiagramm aus einem Text** · AFB II/III · 5–7 BE
- Schablone: „Entwickeln Sie das Zustandsdiagramm für ‹ein Objekt der Klasse X›. Verwenden Sie nur
  die genannten Zustände, Ereignisse, Wächterbedingungen und Aktivitäten.“ (Listen nach B10.)
- Prüfstein: Selbstübergang bei andauernder Aktivität (Kontrolle wiederholen); Übergang ohne
  äußeres Ereignis nach Ende der Aktivität; Wächter mit Gegenwächter.
- Merkmale: je Übergang mit Ereignis und Wächter (1). Variante Designsicht: Zustände und Pfeile
  vorgegeben, Operationen und entry-Verhalten eintragen.

**S8 Klasse instanziierbar machen** · AFB II · 2 BE
- Schablone: „Entwickeln Sie die Klasse ‹Unterklasse› so weiter, dass Objekte von ihr erzeugt
  werden können.“ (abstrakte Oberklasse gegeben)
- Prüfstein: Konstruktor **und** Implementierung jeder abstrakten Operation.

**S9 OOP-Konzept am Diagramm** (Form F9) · AFB I/II · 1–2 BE je Begriff
- Bewährte Begriffe: abstrakte Klasse und Operation; Klassenattribut (unterstrichen) und wie es
  eindeutige Nummern erzeugt; Überladen (zwei Konstruktoren, zwei gleichnamige Operationen);
  dynamische Polymorphie an einer überschriebenen Operation; Sichtbarkeit *geschützt* und ihre
  Wirkung auf Unterklassen; warum eine Klasse abstrakt sein muss (sie erbt eine abstrakte Operation,
  ohne sie zu implementieren).

**S10 Datenstruktur entwerfen** · AFB II/III · 4–5 BE
- Schablone: „Entwerfen Sie ein Klassendiagramm, das ‹die Merkliste jeder Person› als verkettete
  Liste speichert. Gespeichert werden ‹Attribute›.“
- Festlegen: Pflichtattribute; ob Operationen entfallen (B4); ob generisch.
- Prüfstein: Knoten mit Selbstassoziation 0..1; die Liste kennt den ersten Knoten; der Inhalt ist
  eine eigene Klasse.

## 7. Netzwerke und vernetzte Systeme

**Material:** Netzplan mit Routern, Segmenten und vorhandenen Adressen; Lageplan mit Entfernungen;
Bedarfstabelle. Adressen nur aus privaten Bereichen und Dokumentationsbereichen (192.0.2.0/24,
198.51.100.0/24, 203.0.113.0/24, 2001:db8::/32).

**N1 Übertragungsmedium bestimmen und begründen** · AFB II · 2–3 BE
- Schablone: „Bestimmen Sie für die Verbindungen ‹A–B›, ‹B–C› und ‹im Gebäude› je ein
  Übertragungsmedium. Begründen Sie jede Entscheidung mit Entfernung und Kosten.“
- Prüfstein: eine Strecke an der Grenze (rund 100 m bei Twisted Pair) → *Gleichwertig:* beide
  Medien mit passender Begründung.
- Merkmale: je Strecke Medium mit Begründung (1).

**N2 Vorschlag am Adressbedarf prüfen** (Form F3) · AFB III · 2–3 BE
- Schablone: „Ein Mitarbeiter schlägt vor, alle ‹Geräte› in einem Netz /24 zu betreiben. Beurteilen
  Sie den Vorschlag unter Berücksichtigung aller Sensoren und Aktoren.“
- Festlegen: Mengen im Lageplan (Hallen × Plätze × Sensoren, dazu Aktoren).
- Prüfstein: Aktoren mitzählen; Netz- und Broadcastadresse abziehen.
- Merkmale: Bedarf gerechnet (1), Kapazität gerechnet (1), Urteil (1).

**N3 Subnetting mit Auflagen** · AFB II/III · 5–7 BE
- Schablone: „Ermitteln Sie die Teilnetze für die Bereiche der Tabelle. Jeder Bereich soll ‹die
  doppelte Geräteanzahl› aufnehmen können; die Teilnetze sollen möglichst klein sein. Tragen Sie
  alle Werte in Anlage N ein.“
- Festlegen: Bedarf je Bereich, Reserve, Transitnetz zwischen den Routern, ob die Router-Adresse
  mitzählt, Vergabe (lückenlos ab ‹Adresse› nach absteigender Größe) – sonst sind viele Tabellen
  richtig.
- Varianten: gleich große Teilnetze, in denen vorhandene Adressen gültig bleiben · „Zeigen Sie mit
  einer Rechnung, dass sich ‹Netz› in ‹n› Teilnetze mit ‹Bedarf› aufteilen lässt.“ · ein Teilnetz
  nachträglich vergrößern, ohne die anderen zu ändern (erläutern).
- Prüfstein: Die Reserve verschiebt das Präfix; das Transitnetz wird vergessen.
- Merkmale je Zeile: Präfix passend zum Bedarf (1), Adressen konsistent (1). Gleichwertig, falls die
  Vergabe nicht festgelegt ist: jede lückenlose, überschneidungsfreie Aufteilung mit passenden
  Präfixen.

**N4 Routingtabelle entwickeln** · AFB II · 3–4 BE
- Schablone: „Entwickeln Sie die Routingtabelle des Routers ‹R2›.“ (Antworttabelle Zielnetz |
  Präfix | nächster Router; direkt verbunden = *)
- Festlegen: Netze mit Präfix, Lage der Router, Adresskonvention (B12).
- Prüfstein: Standardroute; Netze hinter dem anderen Router mit dessen Adresse im Transitnetz.
- Merkmale: direkt verbundene Netze (1), entfernte Netze mit nächstem Router (1–2), Standardroute
  (1). Gleichwertig: korrekt zusammengefasste Netze.

**N5 Aus der Routingtabelle auf den Netzplan schließen** (Form F10) · AFB II · 3–4 BE
- Schablone: „Bestimmen Sie aus der Routingtabelle in Anlage N die Netzadressen und die Adressen
  der Router-Schnittstellen. Die Router erhalten jeweils die kleinste nutzbare Adresse.“

**N6 Adressen auf dem Weg eines Pakets** · AFB II · 2–3 BE
- Schablone: „Beschreiben Sie, welche Angaben des Pakets sich auf dem Weg über den Router ändern.“ –
  „Ermitteln Sie die Angaben im Antwortpaket des Servers; tragen Sie sie in Anlage N ein.“
- Festlegen: ob NAT beteiligt ist; MAC- und IP-Adressen aller Stationen im Netzplan.
- Prüfstein: MAC-Adressen wechseln je Abschnitt, IP-Adressen bleiben; im Antwortpaket tauschen
  Quelle und Ziel, auch die Ports.

**N7 Eigenschaften mit Zahlwort** · AFB I · 1–3 BE
- Schablonen: „Nennen Sie zwei Vorteile und einen Nachteil von ‹5-GHz-WLAN / IPv6›.“ · „Bestimmen
  Sie eine Link-Local-Adresse für ‹Schnittstelle› in Kurzschreibweise.“ · „Erläutern Sie den
  Gültigkeitsbereich einer Link-Local-Adresse.“ · „Beschreiben Sie zwei Möglichkeiten, den Zugang
  zum ‹Broker› auf berechtigte Geräte zu beschränken.“
- Merkmale: Liste zulässiger Antworten im Erwartungshorizont; *Gleichwertig:* jede weitere fachlich
  richtige Antwort.

**N8 Topic-Struktur entwerfen** · AFB II/III · 3 BE
- Schablone: „Entwerfen Sie eine Topic-Struktur für die Sensoren, aus der ‹Halle, Regal, Fach›
  hervorgeht.“
- Festlegen: Lage und Mengen im Material.
- Prüfstein: Hierarchie von grob nach fein; Wertebereich je Ebene.
- Merkmale: alle Ebenen (1), Reihenfolge und Eindeutigkeit (1), Wertebereiche (1). Gleichwertig:
  Namen der Ebenen.

**N9 Dienstgüte als Kontrastpaar** · AFB II/III · 3–4 BE
- Schablone: „Bestimmen Sie eine QoS-Stufe für ‹Messwerte, die jede Minute gesendet werden› und eine
  für ‹Schaltbefehle an Aktoren›. Begründen Sie beide Entscheidungen.“ – „Beschreiben Sie die
  Auswirkung einer höheren Stufe auf Broker und Netz.“ – „Beschreiben Sie, wie verbundene Clients
  vom Ausfall eines Geräts erfahren.“ (Last Will)
- Prüfstein: Viele gleichartige Messwerte vertragen Verlust; ein Schaltbefehl braucht Bestätigung.
- Merkmale: je Fall Stufe mit Begründung (1–2).

**N10 Schutzmaßnahme am Netzplan** · AFB I/II · 2 BE
- Schablone: „Beschreiben Sie eine Maßnahme, die ‹das Firmennetz› vor Angriffen aus dem Internet
  schützt. Ordnen Sie sie im Netzplan ein.“
- Merkmale: Maßnahme (1), Ort im Netzplan (1) – z. B. Firewall bzw. DMZ zwischen ‹R1› und ‹R2›.

## 8. KI-Grundlagen

**Material:** Streudiagramm mit zwei Merkmalen (Achsen beschriftet), einige Punkte mit Namen und
Werten (kleine ganze Zahlen); Clusterbild mit markierten Zentren.

**K1 Lernarten an zwei genannten Verfahren unterscheiden** · AFB I/II · 3 BE
- Schablone: „Erläutern Sie am Beispiel von ‹k-nächste-Nachbarn› und ‹k-Means› den Unterschied
  zwischen überwachtem und unüberwachtem Lernen.“
- Merkmale: gelabelte bzw. ungelabelte Trainingsdaten (1), Zuordnung beider Verfahren (1), Ergebnis
  – bekannte Klasse bzw. gefundene Gruppe (1).

**K2 Distanzen rechnen** · AFB I/II · 2–3 BE
- Schablone: „Berechnen Sie die paarweisen Manhattan-Distanzen zwischen ‹A›, ‹B› und ‹C›.“ –
  „Nennen Sie das Distanzmaß, das beim Messen mit dem Lineal entsteht.“
- Prüfstein: Beträge; Werte so wählen, dass zwei Distanzen gleich sind (Grundlage für K3).

**K3 Skalierung beurteilen** (Form F2) · AFB III · 2–3 BE
- Schablone: „‹Person› will ‹Abstand› in Millimetern statt in Metern erfassen und meint, die Gruppen
  blieben gleich. Beurteilen Sie die Aussage. Begründen Sie mit den Werten aus ‹K2›.“
- Prüfstein: Umskalieren eines Merkmals macht gleiche Distanzen ungleich, das Merkmal dominiert;
  eine reine Verschiebung (Kelvin statt °C) ändert dagegen nichts.
- Merkmale: Urteil (1), Rechnung mit umgerechneten Werten (1), Folge für die Gruppierung (1).

**K4 Verfahrensschritt am Bild nachvollziehen** · AFB II/III · 2 BE
- Schablone: „‹Person› behauptet, im nächsten Durchlauf ‹wandern alle Zentren nach oben›. Beurteilen
  Sie die Aussage anhand von Abbildung N.“
- Prüfstein: Das neue Zentrum ist der Schwerpunkt der zugeordneten Punkte.

**K5 Baustein des Verfahrens entwickeln** (Form S5) · AFB II/III · 5 BE
- Schwerpunkt einer Punktliste ohne eingebaute Mittelwertfunktion (B6, B8); Mehrheitsprüfung der
  Labels eines Clusters; Zuordnung eines Punkts zum nächsten Zentrum.

## 9. Daten: ER-Modell und SQL


**D1 ER-Modell aus einer Anforderungsliste** · AFB II/III · 7–9 BE
- Schablone: „Entwerfen Sie das ER-Modell in dritter Normalform; kennzeichnen Sie die
  Kardinalitäten und lösen Sie n:m-Beziehungen auf.“ – „Stellen Sie die Relationen mit Primär- und
  Fremdschlüsseln dar.“
- Festlegen: je Spiegelstrich eine Anforderung; Notation des ER-Modells; Kennzeichnung der Schlüssel
  (fett, kursiv).
- Prüfstein: Ein Attribut der Beziehung (Menge je Bestellung, Datum der Anmeldung) erzwingt eine
  eigene Relation; ein Wert, der vom Typ abhängt (Preis je Zimmertyp), gehört in eine eigene
  Entität.
- Merkmale: je Entität mit Attributen (1), je Beziehung mit Kardinalität (1), je aufgelöste
  n:m-Beziehung (1), Schlüssel (1–2).

**D2 SQL-Abfrage mit festgelegter Ausgabe** · AFB II · 3–4 BE je Abfrage
- Schablone: „Entwickeln Sie eine SQL-Abfrage, die ‹…› ausgibt. Spalten der Ausgabe: ‹A | B |
  Anzahl›. Sortierung: ‹…›.“
- Festlegen: Schema mit Schlüsselkennzeichnung, Datumsformat, Spaltennamen der Ausgabe, Umgang mit
  Duplikaten, Sortierung.
- Steigerung in drei Abfragen: Auswahl und Sortierung → Verbund mehrerer Tabellen mit Bedingung →
  Gruppierung mit Aggregat und Gruppenbedingung.
- Prüfsteine: zwei Spalten derselben Zeile vergleichen (Start = Ziel); „das erste“ über eine
  Ordnungszahl; mehrfach erfasste Mengen summieren statt zählen (ein Hinweis im Fachtext trägt das);
  „nicht mehrfach“ → DISTINCT; Bedingung auf die Gruppe statt auf die Zeile.
- Merkmale: je Klausel (Spalten, Verbund, Bedingung, Gruppierung, Sortierung) 1 BE. Gleichwertig:
  JOIN … ON oder Verbund in WHERE, Aliasnamen, BETWEEN oder ≥ und ≤.

## 10. Muster verketten – Aufgabenfluss

Eine Aufgabe arbeitet an einem Szenario; die Teilaufgaben steigen im AFB und sind aus den Vorgaben
lösbar (B11, B14). Die erste Teilaufgabe ist kurz und eindeutig (F4, H9, N7). Bewährte Ketten:

| Themenfeld | Kette (Kennungen) |
|---|---|
| Mikrocontroller | F4 Zustand durchspielen → H3 Initialisierung → H2 Hauptschleife → H4/H5 Timer und ISR → H8 Erweiterung am Bus → H1 Ausnahmezustand → F7 Erweiterung beschreiben |
| Software | S1 Klassendiagramm → S2 Multiplizität → S9 Konzept → S6 Objektdiagramm → F1 von Hand rechnen → S5 Algorithmus → S3 Sequenzdiagramm bzw. S7 Zustandsdiagramm |
| Netzwerk und IoT | N1 Medium → N7 Eigenschaften → N3 Subnetting → N4 Routing → N10 Schutz → N8 Topic → N9 Dienstgüte → N2 Vorschlag prüfen |
| KI | K1 Lernarten → K2 Distanzen → K5 Baustein → K4 Verfahrensschritt → K3 Skalierung |
| Daten | D1 ER-Modell → D2 drei Abfragen mit steigender Anforderung |

## 11. Was nicht übernommen wird

- **Wortlaut, Szenarien und Abbildungen** der Vorlagen – nur die Muster.
- **Veraltete Bausteine:** Registerebene einer bestimmten Controllerfamilie, Assembler, Wartezeiten
  durch Zählen von Befehlszyklen; klassische Schaltwerkssynthese (codierte Zustandstabelle,
  Flipflop-Gleichungen), soweit der Lehrplan sie nicht verlangt; Betriebssystem-Interna (Scheduling,
  Seitentabellen, Dateisystem-Cluster, Verklemmungen). Das Formmuster dahinter bleibt nutzbar: einen
  Ablauf nach einem Regelwerk in einer vorgegebenen Tabelle protokollieren (H10).
- **Schwächen der Vorlagen**, die eigene Aufgaben vermeiden:
  - zwei Operatoren in einem Satz („Ermitteln … und erläutern …“) – zwei Sätze, zwei Merkmale;
  - Fragen statt Aufträge („Was bedeutet dies?“, „Hat sie recht?“);
  - Operatoren außerhalb der Liste des Fachs (*wählen*, *schreiben*, *unterscheiden*; im Fach
    Technik auch *ergänzen*, *erstellen*);
  - offene Mengen ohne Zahlwort („Nennen Sie Vorteile“) und Musterlösungen, die mehr Antworten
    auflisten als verlangt, ohne Regel für die Bewertung;
  - öffentliche IP-Adressen außerhalb der Dokumentationsbereiche;
  - Adressschreibweise am Bus offen (7 oder 8 Bit) – dann sind mehrere Lösungen richtig;
  - Tastgrad 50 % im Impulsdiagramm – Puls- und Pausendauer sind nicht unterscheidbar;
  - Musterlösungen ohne Punkteschema, Merkmale und AFB – der Erwartungshorizont wird immer neu
    gebaut.

## 12. Kurzprüfung je Teilaufgabe

- [ ] Muster-Kennung im Bauplan; Schablone auf den eigenen Fall übertragen, kein Wortlaut aus Vorlagen?
- [ ] Alles festgelegt, was mehrere Lösungen erzeugen würde (B1–B14: Pegel, Namen, Umfang, Zahl, Randfall, erlaubte Mittel, Konventionen)?
- [ ] Jede zu entwickelnde Operation mit Beispiel und Gegenbeispiel (B6)?
- [ ] Prüfstein benannt; im Erwartungshorizont mit den Antworten, die 0 BE erhalten?
- [ ] *Gleichwertig* nennt Plattform-, Sprach- und Notationsfreiheit (B3)?
- [ ] Operator aus der Liste des Fachs (Abschn. 2), ein Operator je Satz?

## Anhang: references/berufliches-gymnasium.md

# Berufliches Gymnasium (BG) – was für Planung, Prüfung und Bewertung anders ist

Die Bibliothek ist ursprünglich für die duale Berufsausbildung (Lernfelder, Ausbildungsjahr,
Betrieb, Kammerprüfung) gebaut. Diese Datei sagt, was im **Beruflichen Gymnasium**
(Niedersachsen, vollzeitschulisch, Abschluss Allgemeine Hochschulreife, DQR 4) anders gilt.
Beispiel ist das BG **Technik**. Für die Fachrichtungen Wirtschaft, Gesundheit und Soziales
gilt die Struktur sinngemäß; Lerngebiete und Fächer aus der jeweiligen RRL einsetzen.

Bezug: Rahmenrichtlinien für das Fach Technik im Beruflichen Gymnasium – Technik –
(Stand Mai 2008, Erweiterungen August 2014, 2016 und Juni 2025); Rahmenrichtlinien für das
Fach Praxis (Stand August 2009); EPA Technik (KMK) mit Aufgabenbeispiel Ingenieurwissenschaften
(Beschluss 16.12.2021). 🔎 Stand vor jeder Planung prüfen (NiBiS, KMK).

## Inhalt
1. Begriffe: was im BG anders heißt
2. Aufbau der Rahmenrichtlinien
3. Lerngebiete im BG Technik (Übersicht)
4. Fach Praxis und Projektarbeit
5. Leistungsbewertung und Abitur
6. Lernsituationen im BG – Hinweise
7. Kopffelder und Planungsakte

---

## 1. Begriffe: was im BG anders heißt

| duale Ausbildung | Berufliches Gymnasium |
|---|---|
| Rahmenlehrplan (KMK), Lernfeld (LF) | Rahmenrichtlinien (RRL, Land), **Lerngebiet** (z. B. ING3) |
| Ausbildungsjahr 1–3(½) | **Schuljahrgang 11–13**; Jg. 11 = **Einführungsphase**, Jg. 12–13 = **Qualifikationsphase** (Halbjahre 12.1 … 13.2) |
| Beruf, Ausbildungsbetrieb, Lernortkooperation | **Fachrichtung** und **Schwerpunkt** (z. B. Technik/Ingenieurwissenschaften); Profilfach Technik, Fach Praxis; Kooperation mit Hochschulen, Unternehmen, außerschulischen Lernorten |
| Kammerprüfung, Notenskala 1–6 | **Abiturprüfung** (EPA), **Notenpunkte 15–0** |
| Auszubildende | Schülerinnen und Schüler (meist ohne Berufserfahrung; oft angesprochen als „angehende Ingenieurinnen und Ingenieure“) |
| Kunde, Betrieb als Rahmen | **fiktiver Auftraggeber** (Ingenieurbüro, Unternehmen, Kommune), Lastenheft |
| Ziel: berufliche Handlungskompetenz | zusätzlich **Studierfähigkeit** und **wissenschaftspropädeutisches Arbeiten** |

Die Leitlinie SchuCu-BBS 2024 gilt auch für das BG: Lernsituationen, Handlungssituation,
Handlungsergebnis, sechs Phasen, Analysebogen. Sie nennt ausdrücklich *Lerngebiete* und die
*Studienorientierung* als Bedeutsamkeit der Handlungssituation.

## 2. Aufbau der Rahmenrichtlinien

Jedes Lerngebiet hat
- **Titel** – charakterisiert Ziele und Inhalte;
- **Zeitrichtwert** – eingeplante Unterrichtsstunden, als Anregung verbindlich gemeint;
- **Zielformulierung** – das, was am **Ende des Bildungsgangs** erreicht sein soll. Sie
  definiert das Lerngebiet; mehrere Lernsituationen teilen sich die Ziele;
- **Inhalte** – Mindestanforderungen (bei den neuen Lerngebieten Ingenieurwissenschaften
  stattdessen nur **Anwendungsbezüge** als Beispiele);
- **Unterrichtshinweise** – Anregungen für die didaktischen Teams.

Daneben nennt die RRL **übergeordnete Kompetenzen** des Fachs (Abschn. 1.3), die alle
Lerngebiete konkretisieren, u. a.: Probleme analysieren und Lösungen beurteilen, Folgen
technischer Lösungen unter humanen, ökonomischen und ökologischen Aspekten bewerten,
Lösungsvarianten vergleichen und den Kompromiss darstellen, Modelle bilden und ihren
Geltungsbereich beachten, **Experimente** durchführen, **Hypothesen formulieren und prüfen**,
Fachsprache in Umgangssprache übertragen, Technik als ambivalent beurteilen.

**Konsequenz für die Planung:**
- Kompetenzen der LS aus der Zielformulierung ableiten; deren Wortlaut im Artefakt mit Quelle
  zitieren, nie glätten (`curriculum-abgleich.md`, falls vorhanden).
- Bei Lerngebieten ohne Inhaltsliste sind alle Inhalte **Konkretisierung** der Schule und so
  zu kennzeichnen.
- Die übergeordneten Kompetenzen sind ein Prüfmaßstab für die ganze Lerngebietsfolge
  (z. B. „Wo wird experimentiert? Wo werden Hypothesen geprüft?“).

## 3. Lerngebiete im BG Technik (Übersicht, Stand RRL 06/2025)

**Einführungsphase (Jg. 11), alle Schwerpunkte:** T1 Technische Informationen nutzen und
erstellen (40 h) · T2 Technische Systeme hinsichtlich Aufbau und Funktion analysieren (60 h) ·
T3 Technische Produkte entwerfen und deren Herstellung planen (60 h).

**Qualifikationsphase (Jg. 12–13):** je Schwerpunkt zwei verbindliche Lerngebiete, ein
optionales (**eins aus drei**, Wahl der Schule) und ein schulisch bestimmtes Lerngebiet in 13.2;
je 80 h. Die Reihenfolge legt die Schule fest.

| Schwerpunkt | verbindlich | optional (eins aus drei) | 13.2 schulisch |
|---|---|---|---|
| Bautechnik | BT1 Fertigung einfacher Baukörper planen · BT2 Einfache Tragwerke konstruieren und berechnen | BT3 Gebäude unter bauphysikalischen Aspekten planen · BT4 Ebene Stabwerke planen · BT5 Wohngebäude planen | BT6 |
| Elektrotechnik | ET1 Gleich- und Wechselspannungsnetzwerke analysieren · ET2 Technische Prozesse steuern | ET3 Elektrische Antriebe auswählen und deren Leistungselektronik dimensionieren · ET4 Technische Prozesse regeln · ET5 Schaltungen der Kommunikationstechnik analysieren und erstellen | ET6 |
| Informationstechnik | IT1 Technische Prozesse steuern · IT2 Netzwerke analysieren, planen und konfigurieren | IT3 Software zur Prozessdatenverarbeitung entwickeln · IT4 Messwerte erfassen und verarbeiten · IT5 Software zur grafischen Darstellung technischer Prozesse entwickeln | IT6 |
| Metalltechnik | MT1 Technische Produkte gestalten und dimensionieren · MT2 Herstellung und Prüfung technischer Produkte planen | MT3 Technische Prozesse automatisieren · MT4 Bauelemente mit CNC-Maschinen in Serie fertigen · MT5 Bauelemente optimieren | MT6 |
| Mechatronik | METRO 1 Mechatronische Systeme analysieren und erweitern · METRO 2 Technische Prozesse steuern | METRO 3 Messwerte erfassen und verarbeiten · METRO 4 Handhabungssysteme programmieren und optimieren · METRO 5 Antriebslösungen für mechatronische Systeme entwickeln | METRO 6 |
| Gestaltungs- und Medientechnik | GMT1 Druckprodukte erstellen · GMT2 Audiovisuelle Produkte erstellen | GMT3 Designprodukte entwickeln · GMT4 Komplexe mehrseitige Druckprodukte herstellen · GMT5 Komplexe audiovisuelle Produktionen erstellen | GMT6 |
| **Ingenieurwissenschaften** | **ING1** Technische Systeme erweitern · **ING2** Technische Systeme konstruieren | **ING3** Technische Systeme zukunftsorientiert entwickeln · **ING4** Optimierungsvorschläge für technische Systeme bewerten und realisieren · **ING5** Technikfolgenabschätzungen durchführen | **ING6** |

**Ingenieurwissenschaften – Besonderheiten (eigene Zusammenfassung):**
- Für ING1–ING6 gilt ein gemeinsamer Hinweis: Themen ganzheitlich und **interdisziplinär**
  (Bau-, Maschinenbau-, Elektro- und Informationstechnik) in praxis- oder lebensnahen
  **Projekten** bearbeiten.
- ING2 soll parallel zum Fach Praxis (Lerngebiet „Projekte durchführen“) laufen und das
  **Projektmanagement** einbeziehen.
- ING5 orientiert sich an Verfahren der Technikfolgenabschätzung (z. B. VDI 3780) und kann den
  ganzen Produktlebenszyklus betrachten.
- Weil ING3–ING5 *eins aus drei* sind, darf eine LS **kein Vorwissen aus einem anderen
  optionalen Lerngebiet** voraussetzen; aufbauen darf sie auf ING1/ING2 und der
  Einführungsphase.

## 4. Fach Praxis und Projektarbeit

- Das Fach Praxis (RRL 2009) hat eigene Lerngebiete über Jg. 11–13, u. a. *Projekte durchführen*
  (Jg. 12) und in Jg. 13 ein Lerngebiet, das sich am gleichzeitig unterrichteten Lerngebiet des
  Profilfachs Technik ausrichtet.
- In einem Halbjahr von Jg. 12 entsteht eine **Projektarbeit mit beruflichem Bezug**
  (wissenschaftspropädeutisch, Einzel- oder Gruppenarbeit), betreut im Fach Praxis.
- **Konsequenz:** Fertigung, Inbetriebnahme und Versuche einer Profilfach-LS gehören oft in den
  Praxisunterricht. Die LS weist die Verzahnung aus (Vereinbarungen → Verknüpfungen zu anderen
  Fächern/Lerngebieten).

## 5. Leistungsbewertung und Abitur

- **Notenpunkte 15–0**; Umrechnung prozentualer Leistung: `notenschluessel.md` (falls vorhanden). Unter 05 Punkten
  gilt ein Kurs als **unterpunktet** (Unterkurs) – Folgen für die Gesamtqualifikation 🔎 nach der
  geltenden Verordnung (BbS-VO, Ergänzende Bestimmungen) prüfen.
- **Klausuren** in der Qualifikationsphase: Aufgaben mit **EPA-Operatoren**, Bewertungseinheiten
  (**BE**), Anforderungsbereiche **30/40/30** (±10), Erwartungshorizont je Teilaufgabe mit AFB
  (`operatoren-epa-technik.md`, falls vorhanden).
- **Abiturprüfung Technik:** eA-Fach; das KMK-Aufgabenbeispiel Ingenieurwissenschaften rechnet
  mit 300 min für 120 BE (2,5 min/BE) und mit PC-Software (CAD, Tabellenkalkulation,
  SPS-Entwicklungsumgebung) als Hilfsmittel.
- **Dezentrale Abiturprüfung:** Für Schwerpunkte ohne zentrale Aufgaben reicht die Schule
  Abiturvorschläge (in der Regel zwei, A und B) zur Genehmigung ein – je Schülermaterial und
  Lehrermaterial mit unterrichtlichen Voraussetzungen (Kursfolge, Bezug jeder Aufgabe zum
  Unterricht), Erwartungshorizont mit Anforderungsbereichen je Teilaufgabe, Bewertungsmaßstab
  und vollständiger Musterlösung 🔎 Verfahren und Fristen der Schulbehörde. Mechatronik wird
  seit 2021 zentral geprüft (allgemeiner Teil zu METRO 1 und 2, dazu ein schuleigener Teil)
  🔎 aktuellen Stand prüfen.
- **Sonstige Leistungen / Mitarbeit:** Projekte, Dokumentationen, Präsentationen, Kolloquien,
  Versuchsprotokolle. Gewichtung gegenüber Klausuren legt die Fachkonferenz fest 🔎. Kriterien
  offenlegen, Einzelanteil bei Gruppenarbeit ausweisen.
- Keine Kammer, kein Ausbildungsbetrieb: Rückmeldungen gehen an Schülerinnen und Schüler und –
  bei Minderjährigen – an Erziehungsberechtigte, nicht an Betriebe.

## 6. Lernsituationen im BG – Hinweise

- **Handlungssituation:** Rolle (z. B. internes Ingenieurteam, Ingenieurbüro), fiktiver
  Auftraggeber, Lastenheft. Bedeutsam heißt hier auch **studien- und gesellschaftsbezogen**
  (Energiewende, Automatisierung, Technikfolgen).
- **Soziale Interaktion:** Projektgruppe, Auftraggeber, Expertinnen und Experten,
  Stakeholder-Rollenspiel, Fachgespräch – nicht „andere Auszubildende“.
- **Offenheit:** Lastenheft nennt Ziele und Randbedingungen, nicht die Technik; Alternativen
  werden nach technischen, ökologischen und ökonomischen Kriterien abgewogen.
- **Wissenschaftspropädeutik:** Hypothesen, Modelle und ihr Geltungsbereich, Quellenkritik,
  Zitieren, Experiment mit Fehlerbetrachtung, Dokumentation.
- **Projekt-LS:** Muster in `lernsituationsmuster.md`, falls vorhanden (Projekt mit Lastenheft, Experiment,
  Urteilsbildung/TFA).
- **Querschnittsaufgaben** (BNE, Demokratiebildung, Europabildung, Medienbildung):
  `querschnittsaufgaben.md`, falls vorhanden.
- **Kompetenzraster zur Lerngebietsanalyse** (in NLQ-Mustern oft noch „Lernfeldanalyse“
  genannt): Zielformulierung des Lerngebiets × Lernsituationen, mit Rückwärtsprobe
  (`curriculum-abgleich.md` Abschn. 7, falls vorhanden).

## 7. Kopffelder und Planungsakte

Statt `ausbildungsjahr` im BG:

```yaml
schulform: "Berufliches Gymnasium Technik"
schwerpunkt: "Ingenieurwissenschaften"
schuljahrgang: 13            # 11 | 12 | 13
phase: "Qualifikationsphase" # Einführungsphase | Qualifikationsphase
lerngebiet: "ING3 Technische Systeme zukunftsorientiert entwickeln"
zeitrichtwert_lerngebiet: 80
curriculare_vorgabe: "RRL Technik im Beruflichen Gymnasium – Technik – (Erweiterung 06/2025)"
dqr: 4
```

Typische Fehler: „Lernfeld“ statt „Lerngebiet“; veralteter RRL-Stand im Kopf; Ausbildungsjahr
statt Schuljahrgang; reale Kontaktdaten des fiktiven Auftraggebers.

## Anhang: references/curriculum-abgleich.md

# Curriculare Vorgaben abgleichen – nachschlagen, zerlegen, Abdeckung nachweisen

Gemeinsame Referenz für Lernsituationen, Lernfeldplanung und Leistungsüberprüfungen. Quelle:
`_gemeinsam/curriculum-abgleich.md` (übernommen und verdichtet aus der *lernfeld-werkstatt*,
Abschnitt Curriculum-Recherche).

## Inhalt
1. Grundsatz: nachschlagen, nicht erinnern
2. Ebenen der Vorgaben
3. Wo nachschlagen
4. Was aus dem Ordnungsmittel übernommen wird
5. Teilkompetenzen (K-Codes)
6. Vier Töpfe: Kern, Konkretisierung, Erweiterung, Ausschluss
7. Abdeckungsmatrix – der Vollständigkeitsnachweis
8. Häufige Fehler

---

## 1. Grundsatz: nachschlagen, nicht erinnern

- Lernfeld- bzw. Lerngebietsnummer, amtlicher Titel, Ausbildungsjahr bzw. Schuljahrgang,
  Zeitrichtwert und **Zielformulierung** stehen im Ordnungsmittel. Sie werden **wörtlich** übernommen – nicht geglättet, gekürzt
  oder aus dem Gedächtnis rekonstruiert.
- Liegt das Dokument nicht vor und ist es nicht beschaffbar: **nicht raten.** Platzhalter
  setzen (`[LF-Nr./Titel laut RLP]`, `[Zeitrichtwert laut RLP]`), `🔎 Prüfen: Abgleich mit
  RLP/RRL` vermerken und an allem weiterarbeiten, was nicht davon abhängt.
- Ohne Ordnungsmittel entsteht nur ein **begründeter Entwurf** – das wird im Artefakt gesagt.

## 2. Ebenen der Vorgaben

| Ebene | regelt | Verbindlichkeit |
|---|---|---|
| **KMK-Rahmenlehrplan** des Ausbildungsberufs | Lernfelder mit Nummer, Titel, Zeitrichtwert, Ausbildungsjahr, Zielformulierung | verbindlich für den berufsbezogenen Unterricht |
| **Ausbildungsordnung / Ausbildungsrahmenplan** | betriebliche Ausbildung | für den Unterricht Kontext und Abgleich (Lernortkooperation) |
| **Landesvorgaben** (Niedersachsen: Rahmenrichtlinien, curriculare Vorgaben, Leitlinie SchuCu-BBS) | Umsetzung im Land, schulische Bildungsgänge, berufsübergreifender Lernbereich | landesverbindlich |
| **Rahmenrichtlinien vollzeitschulischer Bildungsgänge** (Berufliches Gymnasium, Fachoberschule, Berufsfachschule) | **Lerngebiete** mit Titel, Zeitrichtwert, Zielformulierung, Inhalten bzw. Anwendungsbezügen, Unterrichtshinweisen; im BG Einführungs- und Qualifikationsphase, verbindliche und optionale Lerngebiete | landesverbindlich; ersetzt dort den KMK-Rahmenlehrplan (`berufliches-gymnasium.md`, falls vorhanden) |
| **Erlasse zu Querschnittsaufgaben** (BNE, Demokratiebildung) und KMK-Empfehlungen (Europabildung, Bildung in der digitalen Welt) | Aufgaben aller Bildungsgänge, umgesetzt in Lernsituationen | verbindlich bzw. empfohlen; Geltungsdauer prüfen (`querschnittsaufgaben.md`, falls vorhanden) |
| **Handreichungen** anderer Länder, Verlage, Kammern | Umsetzungsideen, Lernsituationsvorschläge | **nicht bindend** – Anregung |
| **Schulisches Curriculum** (Bildungsgangteam) | Verteilung, Lernsituationen, Leistungsbewertung | schulverbindlich |

Reihenfolge beim Nachschlagen (duale Ausbildung): Rahmenlehrplan → Ausbildungsrahmenplan
(Abgleich) → Landesvorgaben → Handreichungen. Vollzeitschulisch: Rahmenrichtlinien → ggf.
EPA/Prüfungsvorgaben → Handreichungen (z. B. NLQ-Musterlernsituationen). Bei Widerspruch gilt
die höhere Ebene; Musterlernsituationen sind Anregung, keine Vorgabe.

## 3. Wo nachschlagen

- **KMK-Rahmenlehrpläne:** Website der KMK (Bereich Berufliche Bildung, Rahmenlehrpläne) 🔎 aktuelle Fassung und Beschlussdatum prüfen.
- **Ausbildungsordnungen:** BIBB; Verordnungstext über das Bundesgesetzblatt bzw. gesetze-im-internet.
- **Niedersachsen:** curriculare Vorgaben und Rahmenrichtlinien (BG, FOS, BFS) über den
  Niedersächsischen Bildungsserver (NiBiS, Bereich BBS) 🔎; Stand im Kopf der RRL
  (z. B. „Stand Mai 2008, Erweiterungen … Juni 2025“) ins Artefakt übernehmen.
- Mit Websuche: Rahmenlehrplan als PDF suchen, Seite des Lernfelds notieren (kommt in die
  Quellenangabe). Ohne Websuche: Lehrkraft um das PDF oder den Wortlaut bitten.

## 4. Was aus dem Ordnungsmittel übernommen wird

1. **Eckdaten:** Lernfeld- bzw. Lerngebietskürzel, amtlicher Titel (wörtlich), Ausbildungsjahr
   bzw. Schuljahrgang/Phase, Zeitrichtwert, Stand des Ordnungsmittels.
2. **Zielformulierung im Wortlaut** (der ganze Block „Die Schülerinnen und Schüler …").
3. **Vorbemerkungen**, soweit sie das Lernfeld betreffen (z. B. Bezug zu Teil 1 der gestreckten
   Abschlussprüfung, Fachrichtungen, gemeinsame Kernqualifikationen).
4. **Nachbar-Lernfelder bzw. -Lerngebiete** – Titel und Ziele mitlesen, **um abzugrenzen**:
   Was dort steht, gehört nicht in diese Lernsituation. Bei **optionalen** Lerngebieten
   („eins aus drei“) darf eine LS kein Vorwissen aus einem der anderen optionalen voraussetzen.
5. **Lerngebiete ohne Inhaltsliste** (z. B. BG Ingenieurwissenschaften: nur Zielformulierung
   und Anwendungsbezüge): Alle Inhalte der LS sind Konkretisierung (Abschn. 6) und werden so
   gekennzeichnet; die Anwendungsbezüge sind Beispiele, keine Pflicht.

## 5. Teilkompetenzen (K-Codes)

Die Zielformulierung wird in nummerierte Teilkompetenzen zerlegt – **sinngleich, mit den
Wörtern des Originals**, in dessen Reihenfolge:

- **K0** = Leitkompetenz (erster Satz, „verfügen über die Kompetenz, …"); worauf das Lernfeld zuläuft.
- **K1 … Kn** = weitere Sätze bzw. Halbsätze; ein Halbsatz mit eigener Handlung wird ein eigener K-Code.
- Jeder K-Code erhält ein Schlagwort und den Originalwortlaut.

```markdown
- **(K2) Wartungsplan:** … die Wartungsarbeiten **nach Herstellerangaben planen** … [Wortlaut laut RLP]
```

Lieber ein K-Code zu viel als eine Kompetenz, die in einem Sammelcode verschwindet.

## 6. Vier Töpfe: Kern, Konkretisierung, Erweiterung, Ausschluss

Verhindert den häufigsten Fehler: **didaktische Konkretisierung als amtliche Vorgabe ausgeben.**

| Topf | Inhalt | Kennzeichnung im Artefakt |
|---|---|---|
| **Kern** | nur, was die Zielformulierung bzw. die Inhalte des Ordnungsmittels ausdrücklich nennen | darf als Vorgabe zitiert werden |
| **Konkretisierung** | übliche Fachsystematik, Verfahren, Normen, Werkzeuge, die das Ordnungsmittel nicht nennt | „didaktische Ausgestaltung", nie „laut RLP gefordert" |
| **Erweiterung** | bewusst zusätzliche Inhalte über den Zeitrichtwert hinaus | ausdrücklich als Erweiterung mit Stundenzahl |
| **Ausschluss** | gehört in ein anderes Lernfeld oder Fach | als bewusste Entscheidung begründet |

## 7. Abdeckungsmatrix – der Vollständigkeitsnachweis

Im BG heißt diese Matrix in NLQ-Mustern **„Kompetenzraster zur Lerngebietsanalyse“** (dort oft
noch „Lernfeldanalyse“): Zeilen = Sätze der Zielformulierung, Spalten = Lernsituationen des
Lerngebiets, Kreuze = federführend eingelöst. Die Prüfregeln unten gelten unverändert; die
**Rückwärtsprobe** prüft in beide Richtungen: Hat jedes Kreuz einen Auftrag? Ist jeder
eingelöste Satz angekreuzt?

Für die Planung mehrerer Lernsituationen eines Lernfelds (Bildungsgangteam, didaktische
Jahresplanung) und für Leistungsüberprüfungen:

| K-Code | Schlagwort | LS 1 | LS 2 | LS 3 | … | geprüft in |
|---|---|---|---|---|---|---|
| K0 | Leitkompetenz | (vorb.) | | ✅ | | KA Aufg. 6 |
| K1 | … | ✅ | (Wdh.) | | | LZK 1 F. 3 |

**Prüfregeln**
1. Keine leere Zeile – jeder K-Code ist mindestens einer Lernsituation federführend (✅) zugeordnet.
2. Keine leere Spalte – jede Lernsituation löst mindestens einen K-Code ein.
3. Jeder Pflichtinhalt genau einmal federführend; Wiederholungen als „(Wdh.)", Vorbereitung als „(vorb.)".
4. **Rückwärtsprobe:** Zu jedem ✅ lässt sich ein konkreter Auftrag bzw. eine Phase benennen.
5. **Stundenbilanz:** Summe der Lernsituationen = Zeitrichtwert des Lernfelds (+ ausgewiesene Erweiterung).
6. **„geprüft in":** Jeder Kern-K-Code kommt in mindestens einer Leistungsüberprüfung vor –
   und keine Leistungsüberprüfung fragt Stoff ab, der erst **nach** ihr unterrichtet wird.

## 8. Häufige Fehler

- Kompetenzen erfinden, die gut klingen, aber nicht im Ordnungsmittel stehen.
- „Lernfeld“ statt „Lerngebiet“ in vollzeitschulischen Bildungsgängen; veralteter Stand des
  Ordnungsmittels im Kopf der LS.
- **Wortlaut-Regel:** Artefakte (Lernsituation, Analysebogen) zitieren die Zielformulierung mit
  Quelle; die Dateien der Skill-Bibliothek selbst geben keine Ordnungsmittel im Wortlaut wieder.
- Wortlaut glätten, weil er sperrig ist.
- Handreichungen anderer Länder wie Vorgaben behandeln.
- Inhalte des Nachbar-Lernfelds hineinziehen.
- Zeitrichtwert ignorieren – mehr Material ist kein besseres Material, sondern nicht unterrichtbar.
- Die Leitkompetenz K0 nirgends einlösen.
- Leistungsüberprüfungen ohne Bezug zur Matrix schreiben.

## Anhang: references/druckfassung-antwortformate.md

# Papierklausur: kurzer Auftrag, Antwortraum, Abbildung, Seitenaufbau

Erfahrungswerte aus einer gelungenen Klausur (Praxisbeispiel BINFQ3, Informatik, Algorithmen und
Struktogramme, 90 min, 50 P, Papier, Antworten von Hand im Aufgabenblatt, fremde Aufsicht).
Lernende und Lehrkraft kamen gut damit zurecht. Die Werte sind **Richtwerte der Bibliothek** aus
diesem einen Beispiel, keine amtlichen Vorgaben – abweichen ist erlaubt, wenn begründet.

## Inhalt
1. Grundsatz: Denken in der Aufgabe, nicht im Schreiben
2. Der Auftragstext
3. Aufgabenmuster mit viel Denken und kurzer Antwort
4. Ein Material, drei Zugriffe: Aufbau einer Aufgabe
5. Antwortformat je Operator
6. Abbildungen als Aufgabenmaterial
7. Seitenaufbau der Druckfassung
8. Operatoren für Lernende erklären
9. Aufsichtsblatt

---

## 1. Grundsatz: Denken in der Aufgabe, nicht im Schreiben

Die Schwierigkeit entsteht aus dem Verfahren (Randfall, verneinte Bedingung, Fehlersuche), nicht
aus Lesemenge, Rechenaufwand oder Schreibmenge. Die Antwort ist meist ein Buchstabe, eine Zahl,
ein Ausdruck oder eine Zeichnung. Damit prüft die Arbeit das Können statt das Schreibtempo, und
die Korrektur bleibt eindeutig.

Gemessen am Beispiel (16 Teilaufgaben, 50 P):

| Antwortformat | Punkte | Anteil |
|---|---:|---:|
| Kurzantwort: Buchstabe, Zahl, Ausdruck, Tabellenzelle, Lückensatz | 33 | 66 % |
| Rechnung mit Rechenweg (Berechnen, Testen) | 6 | 12 % |
| Zeichnung im Zeichenkasten (Erweitern) | 3 | 6 % |
| **Freitext auf Schreiblinien** (zwei Beurteilungen) | 8 | **16 %** |

- **Richtwert:** höchstens rund 30 % der Punkte als Freitext. `klausur_check.py` rechnet den Anteil
  aus, wenn die Punkteübersicht die Spalte *Antwort* hat (Werte `Kurz`, `Rechnung`, `Skizze`,
  `Text`); ein höherer Anteil ist ein ⚠ Hinweis, kein Fehler.
- **AFB III heißt nicht Aufsatz:** Von den 15 Punkten AFB III waren nur 8 Freitext; 7 waren
  kurz (alle Startwerte bestimmen, Testfall ohne Befund entwerfen, Struktogramm erweitern).
- **Schreiblinien nach Punkten:** 4 P Beurteilung = 5–6 Linien, also gut ein bis eineinhalb
  Linien je Punkt. Mehr Linien laden zum Abschreiben der Aufgabe ein.
- **Zahlen kopfrechenbar**, wenn kein Taschenrechner erlaubt ist (1,5 · 68,00 = 102,00;
  149,00 + 8,00 + 45,00 = 202,00; · 0,80). Der Erwartungshorizont rechnet jeden Weg nach.

## 2. Der Auftragstext

Im Beispiel: Median 20 Wörter, 15 von 16 Aufträgen höchstens 37 Wörter; nur die Beurteilung mit
neuem Leserkontext hatte 59.

- **Operator zuerst, fett:** „**4.1 Vervollständigen** Sie das Struktogramm.“ Danach höchstens
  ein Satz Bedingung.
- **Ein Auftrag je Teilaufgabe.** Zwei Operatoren nur, wenn beide Leistungen Punkte bringen
  (1.2: eine Änderung *bestimmen* 1 P, die Anzahl *ermitteln* 1 P).
- **Antwortumfang im Auftrag nennen:** „genau eine Zahl“, „zwei Kriterien“, „einen Nachteil“,
  „alle Startwerte“, „Ein Buchstabe bleibt übrig“. Das ersetzt Hinweise im Erwartungshorizont,
  die die Lernenden nicht sehen.
- **Vorgaben auslagern:** Regeln, Preise und Randbedingungen stehen als kurze Liste neben oder
  über dem Auftrag (Aufgabe 4 und 5), nicht im Auftragssatz.
- **Richtwert:** bis rund 40 Wörter; darüber teilen oder Vorgaben auslagern. Ein neuer
  Leserkontext (Kunden statt Programmierer) darf bis rund 60 Wörter brauchen.
- Fallbezug in einem Satz; der Fall steht in der Ausgangslage, nicht in jedem Auftrag.

## 3. Aufgabenmuster mit viel Denken und kurzer Antwort

| Muster | Beispiel | Prüft |
|---|---|---|
| **Erkennen statt Aufzählen** – welche Eigenschaft wird verletzt? | 1.1 | Begriffe an Gegenbeispielen (AFB I, kurz) |
| **Überhang** – eine Option mehr als Zuordnungen | 1.1, 2.1 | verhindert Ausschlussraten |
| **Randfall** – Grenze der Schleifenbedingung | 3.1 | Durchspielen statt Schätzen |
| **Rückwärts denken, alle Lösungen** | 3.3 | Intervall mit beiden Grenzen (AFB III, ein Feld) |
| **Verneinte Bedingung** – Zweige vorgegeben, Bedingung muss dazu passen | 4.1 ④ | Denkfalle |
| **Fremdlösung mit Fehler** – testen, Ursache nennen, Korrektur angeben | 5.1, 5.2 | Soll-Ist-Vergleich, Fehlerursache |
| **Testfall ohne Befund** – welcher Fall findet den Fehler nicht? | 5.3 | Verständnis der Fehlerstelle |
| **Regel ändern** – gegebene Lösung erweitern | 4.3 | Transfer (AFB III, gezeichnet) |
| **Lückensatz** – „Die Zahl ___ wird ersetzt durch ___.“ | 1.2 | zwingt zur eindeutigen Kurzantwort |

Für Informationstechnik und Informatik gibt es weitere Muster mit Schablone, Festlegungen und
Prüfstein (Mikrocontroller, Modellierung, Algorithmen, Netzwerke, KI, SQL):
`aufgabenmuster-informationstechnik.md`.

**Prüfstein je Aufgabe:** Plane in jede Aufgabe mindestens eine Stelle, an der ein typischer
Denkfehler sichtbar wird, und benenne sie im Erwartungshorizont („Denkfalle der Aufgabe“).
Sie dient der Korrektur (typische Fehler → 0 P.) und nach der Arbeit der Diagnose: Die Items
mit Prüfstein sagen am meisten über die nächste Lektion.

## 4. Ein Material, drei Zugriffe: Aufbau einer Aufgabe

Eine Aufgabe arbeitet an **einem** Material (Struktogramm, Schaltung, Tabelle, Code) und greift
in steigender Anforderung darauf zu:

| Aufgabe | Zugriff 1 (leicht) | Zugriff 2 | Zugriff 3 (schwer) |
|---|---|---|---|
| 3 Struktogramm lesen | Ausgabe ermitteln (II) | Durchläufe bei neuem Startwert (II) | alle Startwerte bestimmen (III) |
| 4 Algorithmus entwickeln | Lücken vervollständigen (II) | Preis berechnen (II) | um neue Regel erweitern (III) |
| 5 Struktogramm testen | Testfall durchrechnen (II) | Fehler beurteilen (III) | Testfall ohne Befund entwerfen (III) |

- **Innerhalb jeder Aufgabe steigt der AFB** – jede Aufgabe beginnt mit einem Erfolg, die
  AFB-III-Anteile stehen am Ende. Die Reihenfolge der Aufgaben folgt dem Unterricht, nicht
  dem AFB.
- **Vertrautes Format, neuer Inhalt:** Notation und Protokollform sind aus dem Unterricht
  bekannt (Struktogramm, Testprotokoll); neu ist nur der Fall. Keine neue Darstellung erst in
  der Arbeit einführen.
- **Entkoppeln statt Ersatzwert:** Besser als ein Ersatzwert ist eine Teilaufgabe, die aus den
  **Vorgaben** lösbar ist, nicht aus dem Ergebnis der Vorgängerin. 4.2 rechnet aus den
  Preisregeln, nicht aus dem selbst vervollständigten Struktogramm; die Beurteilung 5.2
  braucht nicht die Zahlen aus 5.1. Dann gibt es keine Folgefehlerkette.

## 5. Antwortformat je Operator

Der Antwortraum steht **direkt bei der Teilaufgabe** im Blatt und zeigt, was verlangt ist.

| Operator | Antwortraum im Blatt |
|---|---|
| Bezeichnen, Zuordnen | Feld je Zeile in einer Tabelle; „genau ein Buchstabe je Feld“; Überhang einplanen |
| Ermitteln, Bestimmen | Wertfeld mit Einheit oder Lückensatz; bei Denkarbeit zusätzlich Kasten *Platz für Nebenrechnungen (wird nicht bewertet)* |
| Berechnen | Kasten *Rechenweg* **und** Ergebnisfeld mit Einheit (der Rechenweg ist bepunktet) |
| Vervollständigen | nummerierte Lücken ①–⑤ im Bild und Tabelle *Feld · Eintrag* daneben |
| Kennzeichnen | Markierung im abgedruckten Original (einkreisen) und Tabelle *Zeile · korrigierte Zeile* |
| Testen | Testprotokoll *Testfall · erwartet (nach Vorgabe) · tatsächlich (nach Lösung)* und Rechenweg-Kasten |
| Erweitern, Entwerfen, Zeichnen | leerer **Zeichenkasten mit Maßangabe** (z. B. 17 × 6 cm), Seitenverhältnis wie die erwartete Zeichnung; Lineal als Hilfsmittel |
| Beurteilen, Begründen | Feld für das Urteil und Schreiblinien (1–1,5 je Punkt) |
| Auswählen, Ankreuzen | Ankreuzfeld je Option |

- Platz = erwartete Antwort plus Reserve; für Überlänge steht die Rückseite oder ein Zusatzblatt
  mit Name und Aufgabennummer zur Verfügung (Hinweis auf Seite 1).
- **Punkte stehen hinter dem Auftrag**, klein: „(4 P)“ – vor dem Antwortraum, nicht darin.
- Rechenweg verlangen bei *Berechnen* und *Testen*; dann ermöglicht er Teilpunkte.

## 6. Abbildungen als Aufgabenmaterial

Eine gute Abbildung ersetzt zehn Zeilen Beschreibung. Im Beispiel trugen drei Struktogramme die
Aufgaben 3, 4 und 5; die Lösungsbilder stehen im Erwartungshorizont.

| Rolle | Beispiel | Hinweis |
|---|---|---|
| Material zum Lesen | Struktogramm durchspielen (3) | Bedingung und Zweige beschriftet (*ja*/*nein*) |
| Lückenbild | Einträge ①–⑤ im Bild, Tabelle daneben (4.1) | Die Lösung darf nicht im Bild stehen; die Denkfalle bleibt erhalten |
| Fremdlösung mit Fehler | Entwurf „eines Kollegen“ (5) | Fehler fachlich gewollt, im Erwartungshorizont markiert; keine realen Namen |
| Zeichenkasten | Struktogramm erweitern (4.3) | Größe angeben |
| Lösungsbild | Musterlösung im Erwartungshorizont (4.1, 4.3, 5.2) | getrennt vom Aufgabenbild abgelegt |

- **Dieselbe Notation wie im Unterricht**; neu ist nur der Inhalt.
- **Bild und Teilaufgaben auf derselben Seite:** Bild links oder oben (höchstens eine halbe Seite),
  Auftrag und Antwortfeld rechts oder darunter. Niemand muss blättern.
- **In Schwarzweiß lesbar**, Schrift im Druck gut lesbar, Farbe nie als einziger Träger.
- Erzeugen mit `fachdiagramm-erstellen` (Spec, Prüfung, PNG-Ansicht); Muster
  `assets/spec-struktogramm-klausur.yaml` dort. Aufgabenbild und Lösungsbild bekommen eigene
  Dateien (`…_loesung`).

## 7. Seitenaufbau der Druckfassung

- **Seite 1:** Feld für Name und Datum, Titel, Klasse · Zeit · Punkte · Hilfsmittel, vier bis fünf
  Hinweise, Punktetabelle, Fallschilderung. Aufgaben beginnen wahlweise hier oder auf Seite 2.
- **Name in der Kopfzeile jeder Seite**, „Seite x von n“ in der Fußzeile: lose Blätter bleiben
  zuordenbar, die Aufsicht prüft die Vollständigkeit (im Beispiel 6 Seiten).
- **Eine Aufgabe je Seite** (kurze Aufgaben zu zweit). Seitenumbruch vor einer Aufgabe, die
  nicht mehr ganz passt; keine Aufgabe, deren Bild und Antwortraum getrennt werden.
- **Hinweise auf dem Blatt:** direkt im Blatt schreiben (Kästen, Tabellen, Linien); Stift, nicht
  rot; Struktogramme mit Lineal, Zweige mit *ja*/*nein*; ein Buchstabe je Feld; Rechenweg gehört
  zur Lösung; reicht der Platz nicht, Rückseite mit Aufgabennummer.
- Aufgabenkopf: „Aufgabe 3 – Titel (6 Punkte)“; Teilaufgabe „3.1 **Ermitteln** Sie … (2 P)“.
- Nicht an Schriftgraden drehen, um Platz zu gewinnen; lieber eine Teilaufgabe streichen.

## 8. Operatoren für Lernende erklären

Entscheide vorher, wie die Lernenden die Operatoren kennen, und halte es im Erwartungshorizont
fest: **entweder** Tabelle auf Seite 1 des Blatts **oder** vorab im Unterricht besprochen. Im
Praxisbeispiel wurden sie vorab geübt, besonders die drei aus AFB III (*Beurteilen*: Urteil
**und** Begründung, *Entwerfen*, *Erweitern*). Die Erklärung beschreibt, was die **Antwort
enthalten muss**, nicht, was der Operator „bedeutet“:

| Operator | Was Ihre Antwort enthalten muss |
|---|---|
| **Bezeichnen** | den zutreffenden Fachbegriff bzw. seinen Buchstaben – ohne Erklärung |
| **Ermitteln** | ein Ergebnis (Wert, Ausgabe), das Sie aus den Angaben schrittweise gewinnen |
| **Berechnen** | ein Ergebnis mit nachvollziehbarem Rechenweg |
| **Vervollständigen** | die fehlenden Teile einer vorgegebenen Darstellung |
| **Kennzeichnen** | die gesuchten Stellen in einer Vorlage, deutlich markiert (z. B. eingekreist) |
| **Bestimmen** | einen Wert oder Sachverhalt, den Sie durch eigene Überlegung eindeutig festlegen |
| **Testen** | das Ergebnis eines Testfalls, verglichen mit dem erwarteten Ergebnis |
| **Erweitern** | eine gegebene Lösung, ergänzt um eine neue Anforderung |
| **Entwerfen** | eine eigene Lösung, die eine vorgegebene Bedingung erfüllt |
| **Beurteilen** | ein eigenes Urteil mit fachlicher Begründung |

Weitere Operatoren der Arbeit nach demselben Muster ergänzen. Operatoren in Blatt und
Erwartungshorizont stimmen überein (Bibliothek: `operatoren-epa-technik.md`, Abschnitt
*Berufliche Informatik*).

## 9. Aufsichtsblatt

Schreibt die Fachlehrkraft **nicht selbst Aufsicht**, gehört ein eigenes Blatt für die Aufsicht
dazu (`assets/vorlage-aufsichtsblatt.md`). Die Prüflinge erhalten nur das Aufgabenblatt.

- **Ablauf in Minuten:** vor Beginn (Tische leer, Handys im Raum vorne, Ersatzpapier), 0 min
  (Blätter austeilen, Namen eintragen, Seiten zählen lassen), Bearbeitungszeit, Ende (alle Seiten
  und Zusatzblätter einsammeln).
- **Zugelassen und nicht zugelassen** wörtlich wie im Kopf der Arbeit.
- **Keine inhaltlichen Auskünfte**, auch nicht bei scheinbar harmlosen Fragen („Muss der Nein-Zweig
  gezeichnet werden?“, „Was heißt *Beurteilen*?“). Deshalb stehen die Operatoren auf dem Blatt
  oder sind vorab geübt.
- **Situationen mit Handlungsanweisung:** Druckfehler, inhaltliche Frage (notieren, wer wonach
  fragte), Platz reicht nicht, Krankheit (Uhrzeit notieren, einsammeln), Täuschungsversuch
  (Sachverhalt notieren, **nicht** abbrechen, der Fachlehrkraft melden).
- Notizfeld für die Aufsicht; Hinweis, wo die Blätter abgelegt werden. Keine Namen von
  Prüflingen im Blatt selbst.

## Anhang: references/klausur-gutepraxis.md

# Gute Praxis für Klassenarbeiten und Lernzielkontrollen

Zusammengeführt aus der Skill-Fassung `klausur-erstellen` 1.x (eduwerkzeuge), der Referenz
*Leistungsüberprüfungen* der `lernfeld-werkstatt`, den Prüfkriterien der Begutachtung
und einer gelungenen Papierklausur aus der Praxis (Details in
`druckfassung-antwortformate.md`). Erfahrungswerte aus realen Reihen sind als solche gekennzeichnet.

## Inhalt
1. Wo Leistungsüberprüfungen liegen
2. Zeitauslegung – die wichtigste Zahl
3. Aufbau einer Klassenarbeit
4. Anforderungsbereiche – gerechnet, nicht behauptet
5. Erwartungshorizont
6. Single Choice – die Fallen
7. Varianten (A/B, Nachschreiben)
8. Erste Seite und Layout
9. Anti-Muster

---

## 1. Wo Leistungsüberprüfungen liegen

- **Nach** dem Material und **aus** ihm – nie parallel dazu, sonst prüfen sie den Plan statt
  des Unterrichts.
- Am **Ende einer Lernsituation**, nie mitten hinein. Bewährter Satz je Lernfeld: zwei
  Lernzielkontrollen (nach rund einem Viertel und rund zwei Dritteln) und eine Klassenarbeit am
  Ende; größere Lernfelder (ab ca. 80 Std.) vertragen eine dritte Lernzielkontrolle.
- Leistungsüberprüfungen gehören keiner einzelnen Lernsituation an, sondern dem Lernfeld: Die
  Klassenarbeit prüft das Lernfeld, nicht nur die zuletzt unterrichtete Lernsituation.
- Bausteinbewertung (Handlungsergebnis mit offengelegtem Raster) und schriftliche
  Leistungsüberprüfung ergänzen sich: Die eine prüft Handlungskompetenz am Produkt (oft in der
  Gruppe), die andere individuelles Können unter Prüfbedingungen.

## 2. Zeitauslegung – die wichtigste Zahl

**Minuten je Punkt** statt „ein Punkt je Minute":

| Art | Richtwert | Beispiel |
|---|---|---|
| Klassenarbeit | ≥ 1,5 min/P | 90 min / 60 P · 60 min / 40 P |
| Kurzklausur | ≥ 1,5 min/P | 45 min / 30 P |
| Lernzielkontrolle (Single Choice) | ≈ 1 min je Frage | 25 Fragen in 20–25 min |

> **Erfahrungswert (lernfeld-werkstatt):** Eine erste Fassung mit 16 Aufgaben, 60 Punkten und
> 60 Minuten ging rechnerisch auf und war trotzdem unbearbeitbar – alle vier Minuten ein
> Kontextwechsel. Halbiert auf 8 Aufgaben und 40 Punkte bei gleicher AFB-Gewichtung und
> Abdeckung; kein Pflichtinhalt ging verloren (mehrere wanderten in Richtig/Falsch-Aussagen).

- Minutenangaben je Aufgabe im Erwartungshorizont führen; ihre Summe bleibt **unter** der
  Bearbeitungszeit (Reserve für Austeilen, Lesen, Kontrolle).
- Faustregel der Begutachtung: Probelösung durch die Lehrkraft × 2,5 bis 3 ≈ Zeitbedarf der SuS.
- Höchstens rund 10 Hauptaufgaben. Was zusammengehört, zusammenlegen (z. B. Rechnung in die
  Auswahlaufgabe), Doppelungen streichen (zweite Beurteilungsaufgabe).

## 3. Aufbau einer Klassenarbeit

| Element | Regel |
|---|---|
| **Ein durchgehender Fall** | alle Aufgaben in derselben Handlungssituation, möglichst ein Vorgang; acht unverbundene Fälle sind acht Kontextwechsel |
| **Handlungsbogen** | der Fall läuft entlang der vollständigen Handlung (Informieren bzw. Analysieren bis Überprüfen und Reflektieren): aufnehmen, einordnen, bearbeiten, kommunizieren, auswerten |
| **Formate mischen** | Richtig/Falsch mit Berichtigung · Zuordnung · Kurzantwort · Rechnung · Skizze · Textproduktion (Kundeninformation, Übergabenotiz) · Beurteilung mit Begründung |
| **Operator + AFB** | je Teilaufgabe, Operator aus der Liste; Einstieg AFB I |
| **AFB III** | Beurteilung mit Kriterien, Urteil und Begründung – 6–8 P, kein Aufsatz |
| **Unabhängig lösbar** | besser als ein Ersatzwert: Teilaufgabe aus den **Vorgaben** lösbar machen, nicht aus dem Ergebnis der Vorgängerin; sonst Ersatzwert – plausibel, aber **nicht** das richtige Ergebnis (verrät sonst die vorige Teilaufgabe); Erwartungshorizont für beide Wege |
| **Kurzer Auftrag** | Operator zuerst (fett), ein Auftrag je Teilaufgabe, Antwortumfang als Zahlwort („zwei Kriterien“, „alle Startwerte“), Vorgaben als Liste auslagern; Richtwert bis rund 40 Wörter |
| **Denken statt Schreiben** | Schwierigkeit im Verfahren (Randfall, verneinte Bedingung, Fehlersuche), Antwort kurz: Buchstabe, Zahl, Ausdruck, Zeichnung; Freitext höchstens rund 30 % der Punkte, auch AFB III oft kurz |
| **Ein Material, steigender AFB** | jede Aufgabe an **einem** Material mit drei Zugriffen (lesen/ausführen → bewerten → verändern); AFB steigt innerhalb jeder Aufgabe; Aufgabenfolge = Unterrichtsfolge; vertrautes Format, neuer Inhalt |
| **Abbildung trägt die Aufgabe** | Material zum Lesen, Lückenbild, fehlerhafte Fremdlösung, Zeichenkasten; Notation wie im Unterricht; auf derselben Seite wie die Teilaufgaben |
| **Antwortraum im Blatt** | je Operator ein festes Antwortformat (Feld, Tabelle, Rechenweg-Kasten, Zeichenkasten, Linien nach Punkten) |
| **Hilfsmittel** | auf Seite 1 benannt (Tabellenbuch? Taschenrechner? Formelsammlung?) |
| **Anlagen** | jede angekündigte Anlage mit eigener Überschrift; Fremdmaterial mit Quelle |

Aufgabenformulierung: **Operator + Inhalt + Bedingung** – „Erläutern Sie **zwei** Vorteile der
Zentralschmierung **am Beispiel des Gurtförderers GF-2**." Keine W-Fragen; pro Teilaufgabe ein
Operator; Mehrfachoperatoren nur, wenn beide Leistungen bewertet werden.

## 4. Anforderungsbereiche – gerechnet, nicht behauptet

| Art | AFB I | AFB II | AFB III | Begründung |
|---|---|---|---|---|
| Klassenarbeit | 30 % | 40 % | 30 % | Entscheidung der Fachberatung (10/2026): einheitlich wie EPA |
| Klausur im Beruflichen Gymnasium | 30 % | 40 % | 30 % | EPA Technik |
| Lernzielkontrolle | 40 % | 50 % | 10 % | sichert Grundlagen unterwegs, überwiegend geschlossene Formate |

- Prozente aus den Punkten **rechnen** (`klausur_check.py`), nie abschreiben – nach der ersten
  Umfangsänderung sind abgeschriebene Werte falsch.
- Toleranz ±10 Prozentpunkte.
- DQR 2–3 bzw. Einstiegsklassen: mehr AFB I/II begründbar; FOS/BG/Fachschule: mehr AFB III.

## 5. Erwartungshorizont

- Je Teilaufgabe: erwartete Leistung als **einzeln bepunktbare Aspekte**, Punktevergabe,
  **zulässige Alternativen**, **Toleranzhinweis** („auch X werten, wenn begründet"),
  typische Fehler und woran Teilleistungen erkennbar sind.
- **Folgefehler** nicht doppelt bestrafen – Regel ausdrücklich nennen.
- Offene Aufgaben: Niveaustufen beschreiben (ein Aspekt / mehrere / verknüpft / übertragen)
  statt einer einzigen Musterlösung; **Erwartungsspielraum** benennen.
- **Punkteübersicht** mit Bezug je Zeile (Lernsituation · Kompetenz/K-Code) – Nachweis nach
  außen (Einspruch, Nachteilsausgleich, Vertretung) und Kontrolle nach innen (prüft die Arbeit
  das Lernfeld oder nur die letzte Lernsituation?).
- Ohne Toleranzhinweis bewertet die Vertretung anders als die Fachlehrkraft; eine
  Stichwortliste ohne Punktevergabe fällt erst bei der Rückgabe auf.
- **Korrekturschablone auf einer Seite:** Item · Lösung · Punkte für alle Kurzantworten. Im
  Praxisbeispiel waren 23 von 50 Punkten allein damit korrigierbar; für die übrigen (mehrere
  richtige Antworten, Teilpunkte) stehen die Regeln darunter. Korrektur erst mit der Schablone,
  dann die Items mit Ermessen.
- **Je Kurzantwort drei Spalten:** Lösung · ebenfalls richtig · falsch (0 P.). Die Spalte
  *falsch* nennt den typischen Denkfehler und ist die Arbeit, die eine Vertretung sonst nicht
  hat.
- **Prüfstein je Aufgabe benennen** („Denkfalle der Aufgabe“): Randfall, verneinte Bedingung,
  Fehler in der Fremdlösung. Er erklärt Punktabzüge bei der Rückgabe und zeigt nach der Arbeit,
  was die nächste Lektion braucht (Items mit Prüfstein gesondert auswerten).
- **Teilpunktregeln für Rechenwege:** richtiges Ergebnis ohne verlangten Rechenweg nur ein Teil
  der Punkte; ein Regelfehler im sonst richtigen Weg = Teilpunkt; Soll und Ist vertauscht
  (Testen) höchstens die Hälfte; Folgefehler **einmal** werten.
- **Bewusst nicht geprüft** festhalten (unterrichtet, aber nicht Gegenstand dieser Arbeit).

## 6. Single Choice – die Fallen

1. **Die richtige Antwort landet von selbst auf B und C.** Erfahrungswert: in einer ersten
   Fassung 18 von 25, in einer zweiten 24 von 25 – auf A kein einziges Mal. Abhilfe:
   Zielbuchstaben vorgeben (jeder Buchstabe gleich oft) und mit
   `klausur_check.py --sc "CADBE…"` prüfen.
2. **Sachlich geordnete Optionen** (Zahlen, Uhrzeiten, Fristen, Rangfolgen) nicht umsortieren –
   die Frage so schreiben, dass die Lösung an der Zielstelle steht.
3. **Ablenker müssen falsch, aber denkbar sein.** Quellen: typischer Denkfehler der Stunde
   (steht im Erwartungshorizont des Arbeitsblatts), benachbarter Fachbegriff, Regel, die
   anderswo gilt, umgekehrte Kausalität. Nicht: Scherzantworten, auffällig lange/kurze Optionen,
   „alle genannten", „keine der genannten".
4. **Lösungsspiegel** im Erwartungshorizont: Frage · Lösung · warum richtig · AFB · Bezug. Die
   Begründung braucht die Lehrkraft für die Besprechung – und sie zeigt beim Schreiben, ob die
   Frage eindeutig ist.
5. Notenschlüssel bei Single Choice auf **ganze** Punkte runden (`--ganze-punkte`).

## 7. Varianten (A/B, Nachschreiben)

- **Gleich schwer:** gleiche Bauplantabelle – gleiche Operatoren, AFB, Punkte und Struktur.
- **Anders:** Kontext (anderes Bauteil, anderer Kunde) oder Zahlenwerte; keine Aufgabe, die
  durch Abschauen der Nachbarvariante lösbar wird.
- Jede Variante mit eigenem Erwartungshorizont und eigener Selbstprüfung.
- Nachschreibarbeit nicht leichter machen „weil allein"; Nachteilsausgleiche (Zeit,
  Hilfsmittel) sind organisatorisch, nicht Teil der Aufgaben.

## 8. Erste Seite und Layout

- Kopf, Hinweise und Ausgangslage verbrauchen rund ein Drittel der ersten Seite; dort nur die
  Fallschilderung und **eine** Aufgabe einplanen – oder Seite 1 als Deckblatt (Hinweise,
  Punktetabelle, Fall) und die Aufgaben ab Seite 2.
- Antwortraum im Aufgabenteil vorsehen (Feld, Tabelle, Rechenkasten, Zeichenkasten, Linien) –
  Format je Operator in `druckfassung-antwortformate.md` Abschn. 5; nicht an Schriftgraden
  drehen, um Platz zu gewinnen.
- Name in der Kopfzeile **jeder** Seite; eine Aufgabe je Seite; Abbildung und Antwortraum nie
  durch einen Seitenumbruch trennen.
- Punkte je Aufgabe und Punktetabelle gehören **in die Leistungsüberprüfung** – auf
  Übungsarbeitsblätter gehören sie nicht.

## 9. Anti-Muster

| Anti-Muster | Besser |
|---|---|
| Arbeit vor dem Material bauen | erst Material und Unterricht, dann die Prüfung daraus |
| Punktsumme als Zeitmaß („60 P in 60 min") | Minuten je Punkt ≥ 1,5, Aufgabenzahl begrenzen |
| Prozentangaben abschreiben | aus den Punkten rechnen |
| neue Firma für die Prüfung erfinden | Handlungssituation des Unterrichts weiterführen |
| Erwartungshorizont als Stichwortliste ohne Punkte | Aspekte mit Punkten, Alternativen, Toleranz |
| Frage zu Stoff, der erst später kommt | Bezug je Teilaufgabe, Abdeckungsmatrix „geprüft in" |
| W-Fragen („Was ist …?") | Operator + Inhalt + Bedingung |
| B-Variante mit leichteren Operatoren | gleiche Bauplantabelle |
| Auftrag mit Nebensätzen und Kontext; Antwortlänge bleibt offen | Operator zuerst, Zahlwort für den Umfang, Vorgaben als Liste |
| AFB III als langer Aufsatz | AFB III mit kurzer Antwort: alle Werte bestimmen, Testfall entwerfen, Lösung erweitern |
| Antwortraum fehlt oder passt nicht zum Operator | Antwortformat je Operator, Linien nach Punkten |
| neue Darstellung erst in der Arbeit einführen | Notation aus dem Unterricht, neuer Inhalt |
| Bild und Antwortraum auf verschiedenen Seiten | Aufgabe auf einer Seite, Bild neben oder über den Teilaufgaben |
| Operatoren erst in der Arbeit kennenlernen | vorab besprechen oder auf Seite 1 erklären |

## Anhang: references/normen-technik.md

# Normen für Prüfungsaufgaben Technik (Informationstechnik, Mechatronik)

**Wozu:** Was eine Lösung festlegt, folgt einer Norm oder der Notation des Unterrichts. Diese
Referenz fasst zusammen, was Aufgaben, Musterlösungen und Bewertungsmerkmale in den Lerngebieten
*Technische Prozesse steuern* (IT1, METRO 2, ET2), *Netzwerke* (IT2), *Messwerte erfassen* (IT4,
METRO 3), Software (IT3, IT5) und Antriebe (METRO 5) aus den Normen brauchen. Normtexte sind nicht
frei zugänglich: Die Angaben sind in eigenen Worten nach Leseproben, Merkblättern der PAL und
Sekundärquellen zusammengefasst (Abschn. 11, Stand der Recherche 2026-10). Unsicheres ist mit 🔎
markiert – vor der Einreichung mit dem Normtext oder dem eingeführten Tabellenbuch abgleichen.

**Einheitliche Schreibweise:** Wo die Normen Spielraum lassen (Tiefe der Kennbuchstaben, getippte
Negation, Zeitschreibweise, Zuordnungsliste, GRAFCET in Textform, Bezeichner im Programm), legt das
**Notationsblatt** `notation-steuerungstechnik.md` eine Form fest; es geht als Anlage ins
Schülermaterial.

## Inhalt
1. Grundregeln für Aufgaben
2. Referenzkennzeichen – DIN EN IEC 81346-1 und -2
3. GRAFCET – DIN EN 60848
4. Steuerungsprogramme – IEC 61131-3 und Mikrocontroller
5. Schaltpläne, Schaltzeichen, Anschlussbezeichnungen
6. Sicherheit an Maschinen – Bedienteile, Farben, Stopp, Not-Halt
7. Sensorik, Einheitssignale, Regelungstechnik
8. Netzwerke
9. Software – UML, Struktogramm, Programmablaufplan
10. Größen, Einheiten, Schreibweise
11. Quellen

---

## 1. Grundregeln für Aufgaben

1. **Norm und Ausgabe nennen**, wo eine Notation bewertet wird – im Schülermaterial (Hinweise oder
   Teilaufgabe): „Die Betriebsmittel sind nach DIN EN IEC 81346-2:2020 gekennzeichnet.“, „Entwickeln
   Sie einen GRAFCET nach DIN EN 60848.“ `bmk_pruefen.py` liest die genannte Ausgabe (T.8).
2. **Eine Notation je Vorschlag.** Weicht der Unterricht ab (ältere Ausgabe, Hauskonvention,
   Herstellernotation), gilt sie für Aufgabe, Anlagen und Musterlösung gleichermaßen; im
   Schülermaterial nennen, im Begleitblatt begründen. Nie mischen.
3. **„Normgerecht“ im Merkmal auflösen.** Das Lehrermaterial nennt die Normelemente, die zählen
   (z. B. „Initialschritt doppelt umrandet, Rücksprung mit Pfeil, Transitionen mit Bedingung“) –
   eigenes Merkmal mit 1–2 BE, getrennt von der Funktion.
4. **Tabellenbuch beachten.** Ältere Ausgaben (etwa vor 2021 🔎) zeigen Kennbuchstaben der
   Ausgabe 2009. Steht die Lösung nur im Tabellenbuch, den benutzten Stand im Erwartungshorizont
   angeben.
5. **Was nicht genormt ist** – Technologieschema, Zuordnungsliste, Pseudocode – legt die Aufgabe
   selbst fest (Legende, Tabellenkopf mit Beispielzeile, Hilfsmitteldokument).

## 2. Referenzkennzeichen – DIN EN IEC 81346-1 und -2

**Ausgaben**

| Teil | gültige Ausgabe | Inhalt |
|---|---|---|
| Teil 1 | DIN EN IEC 81346-1:2024-07 (IEC 81346-1:2022) | Strukturierung, Aspekte und Vorzeichen |
| Teil 2 | **DIN EN IEC 81346-2:2020-10** (IEC 81346-2:2019) | Klassen und Kennbuchstaben |
| Teil 2, Vorgänger | DIN EN 81346-2:2010-05 (IEC 81346-2:2009) | zurückgezogen; danach noch die zentralen Mechatronik-Prüfungen in Niedersachsen 2020–2026 (z. B. -SF elektrischer Taster, -SJ pneumatischer Taster, -RZ, -AZ) |

Die PAL setzt die Ausgabe 2020 in den IHK-Prüfungen um (Merkblatt Stand Juni 2024). Für neue
Vorschläge gilt **die Ausgabe 2020**; die Ausgabe 2009 nur, wenn der Unterricht sie verwendet – dann
im Schülermaterial nennen (Abschn. 1).

**Aufbau eines Kennzeichens:** Vorzeichen, Kennbuchstaben, Zählnummer, ohne Leerzeichen: `-SJ1`,
`-BT2`, `-QA1`.
- Vorzeichen (Teil 1): `-` Produkt (in Aufgaben üblich), `=` Funktion, `+` Ort, `%` Typ (neu seit
  2022), `#` andere Aspekte. Kombinationen wie `+S1-K1` nur, wenn im Unterricht eingeführt.
- **Ein bis drei Kennbuchstaben** (Teil 2): Klasse (`-B1`), Unterklasse (`-BG1`), Unter-Unterklasse
  (`-BGB1`). Die Norm lässt jede Tiefe zu; die PAL zeigt Schaltpläne nur mit Klassen und mit
  Unterklassen.
- **Klasse und Unterklasse sind Standard** (Vorgabe der Fachberatung, 04.11.2026; ersetzt die
  Festlegung „so kurz wie möglich“ vom 31.10.2026): Jedes Betriebsmittel trägt **zwei Kennbuchstaben** –
  **-SJ1** (Taster), **-MA1** (Elektromotor), **-MM1** (Zylinder), **-EA1** (Leuchte), **-QA1** (Schütz),
  **-KE1** (SPS), **-PF1** (Leuchtmelder). Die Klasse allein (-S1, -M1) wird nicht verwendet, auch nicht,
  wenn eine Klasse nur eine Art Betriebsmittel enthält. Das gilt in **allen Dokumentationsformen**:
  Funktionsbeschreibung, Technologieschema mit Legende, Zuordnungsliste, GRAFCET, Logikplan, Programm,
  Musterlösung. Die dritte Ebene (-BGB1) nur, wenn der Unterricht sie verlangt – dann für alle
  Kennzeichen dieser Klasse (nicht -BG1 neben -BGB2). `bmk_pruefen.py` (T.8) und
  `edu-technologieschema pruefen` melden fehlende Unterklassen und gemischte Tiefe.
- Beispiel Bewässerung: Taster -SJ1, -SJ2; Schütz -QA1; SPS -KE1; Leuchtmelder -PF1, -PF2; Sensoren für
  Füllstand, Bodenfeuchte und Temperatur -BL1, -BM1, -BM2, -BT1; Pumpenmotor -MA1; Magnetventile -MB1,
  -MB2.
- Die Unterklasse macht sichtbar, welche Ausgabe gilt: -SF/-SJ, -KF/-KE, -RZ/-RN unterscheiden sich
  zwischen 2009 und 2020 (Tabelle unten). Neue Aufgaben verwenden die Unterklassen der Ausgabe 2020.
- **A, I und O** sind keine Klassen; **D, J, L, V, Y, Z** sind reserviert. Eine Klasse „Sonstiges“
  gibt es nicht: Passt keine Unterklasse genau, die nächstpassende aus Tabelle 2 wählen und die Aufgabe
  des Betriebsmittels in der Legende nennen.
- Klassifiziert wird nach der **inhärenten Funktion** – was das Objekt erfasst oder bewirkt, nicht
  nach Bauart oder Einbauort: Der Druckschalter am Zylinder ist -BP, der Endlagenschalter daneben
  -BG. Bei mehrdeutigen Fällen die Aufgabe des Betriebsmittels in der Legende nennen.
- Die Zählnummer zählt je Kennbuchstaben: -BG1, -BG2, -BP1.

**Klassen** (Übersicht; im Kennzeichen steht immer zusätzlich die Unterklasse)

| BMK | Klasse | typische Betriebsmittel |
|---|---|---|
| -B | Information erfassen | Sensoren und Geber: Näherungs-, End-, Druck-, Schwimmerschalter, Temperaturfühler |
| -S | menschliche Betätigung erfassen | Taster, Schalter, Wahl- und Schlüsselschalter, handbetätigtes Ventil |
| -K | Signale verarbeiten | SPS, Kleinsteuerung, Mikrocontroller, Relais, Zeitrelais, pneumatisches UND/ODER |
| -Q | Fluss steuern | Schütz, Leistungs- und Motorschutzschalter, Wegeventil |
| -M | Antreiben | Motor, Ventilspule, Elektromagnet, Zylinder |
| -P | Information darstellen | Leuchtmelder, Hupe, Anzeige, Manometer |
| -R | Begrenzen | Drossel- und Drosselrückschlagventil, Rückschlagventil, Widerstand, Diode |
| -G | Fluss erzeugen | Pumpe, Kompressor, Lüfter, Generator; Wartungseinheit (PAL) 🔎 |
| -T | Umwandeln | Netzteil, Frequenzumrichter, Messumformer |
| -F | Schützen | Sicherung, Leitungsschutzschalter, thermisches Überlastrelais |
| -E | Aussenden | Leuchte, Heizung |
| -X, -W | Verbinden, Leiten | Klemme, Steckdose, Patchfeld; Kabel, Leitung |
| -C | Speichern | Kondensator, Akku, Tank |

**Unterklassen – Standard in Aufgaben** (Auswahl der
Ausgabe 2020; deutsche Benennungen sinngemäß; in Klammern Beispiele der dritten Ebene)

| BMK | Bedeutung | typische Betriebsmittel | Ausgabe 2009 |
|---|---|---|---|
| **B** | **Information erfassen** | | |
| -BG | Lage, Abstand, Winkel | Näherungsschalter (induktiv, kapazitiv, optisch), Endlagen-/Positionsschalter (BGB), Zylinderschalter, Abstandssensor (BGC), Drehgeber/Winkel (BGE) | gleich |
| -BP | **Druck** | Druckschalter (BPB), Drucktransmitter (BPA), Differenzdruck (BPC, BPD), Vakuumschalter | gleich |
| -BM | **Feuchte** | Feuchtesensor (BMA), Hygrostat (BMB); Bodenfeuchte 🔎 (2009: „Wassergehalt, Feuchte“) | gleich |
| -BT | Temperatur | Pt100, Thermoelement (BTA), Thermostat/Temperaturschalter (BTB) | gleich |
| -BL | Füllstand | Schwimmerschalter (BLB), Füllstandsensor (BLA) | gleich |
| -BF | Durchfluss | Durchflusssensor, Strömungswächter | gleich |
| -BS | Drehzahl, Geschwindigkeit, Beschleunigung | Tachogenerator, Drehzahlwächter, Beschleunigungssensor | gleich |
| -BW | Kraft, Gewicht, Drehmoment | Wägezelle, DMS-Kraftaufnehmer, Drehmomentsensor | gleich |
| -BR | Strahlung, Licht | Lichtsensor, Lichtschranke/Lichtgitter, Fotozelle, IR- und UV-Sensor | gleich |
| -BQ | Stoffkonzentration | Gas-, Rauch-, CO₂-, Trübungssensor | gleich |
| -BA / -BC | elektrische Spannung / Strom | Spannungs-, Stromwandler, Überlastrelais (elektronisch, BC) | 🔎 |
| -BE | elektrisches oder magnetisches Feld | Reedkontakt, Magnetfeldsensor | 🔎 |
| -BJ / -BH | Leistung / Energie | Leistungsmesser, Energiezähler | 🔎 |
| -BK | Zeit | Uhr, Zeitschaltuhr | 🔎 |
| -BX | Bild und Ton | Kamera, Mikrofon | 🔎 |
| -BY | gespeicherte Information | RFID-, Barcode-, Kartenleser | 🔎 |
| -BZ | Ereignisse, Anzahl | Zähler, Präsenz- und Personenmelder | 🔎 |
| **S** | **menschliche Betätigung erfassen** | | |
| -SJ | Fingerbetätigung | **Drucktaster (SJB)**, Kippschalter (SJA), Touch-Taster (SJC); handbetätigte Ventile | **-SF** (elektrisch); -SJ war nur das handbetätigte Ventil |
| -SG | Handbetätigung | Drehknopf/Knebel (SGA), Handhebel, Schlüsselschalter (SGF) | 🔎 |
| -SH | Fußbetätigung | Fußschalter, Pedal | 🔎 |
| -SK | Bewegung | Joystick, Maus | 🔎 |
| -SF | Gesichtserkennung | (in Prüfungsaufgaben kaum) | **Taster, Schalter elektrisch** |
| **K** | **Signale verarbeiten** | | |
| -KE | elektrische Signale verarbeiten | **SPS, Kleinsteuerung, Mikrocontroller (KEB)**, PC (KEA), E/A- und Kommunikationsbaugruppe (KEC), Router, Firewall (KED) | -KF 🔎 |
| -KF | elektrische Signale weiterleiten | Relais, Hilfsschütz (KFA), Zeitrelais (KFB), Repeater, Netzwerk-Switch (KFE) | gleich (2009 auch SPS) |
| -KH | fluidische Signale verarbeiten | Zweidruck- und Wechselventil (UND/ODER), Vorsteuerventil (KHB) | gleich |
| **M** | **Antreiben** | | |
| -MA | elektromagnetisch, drehend | Elektromotor (MAA), Schrittmotor (MAB) | gleich |
| -MB | elektromagnetisch, linear | **Ventilspule, Elektromagnet (MBB)**, Linearmotor (MBA) | gleich |
| -MM | fluidisch | Pneumatik-/Hydraulikzylinder (MMB/MMA), Druckluft-/Hydraulikmotor | gleich |
| **P** | **Information darstellen** | | |
| -PF | Zustand sichtbar | Leuchtmelder, Signalleuchte (PFA), Stellungsanzeige | gleich |
| -PG | Wert anzeigen | Manometer (PGP), Thermometer (PGT), Volt-/Amperemeter, Zähleranzeige | gleich |
| -PH | grafisch anzeigen | Display, Bildschirm | 🔎 |
| -PJ | akustisch | Hupe (PJB), Summer, Klingel, Lautsprecher | gleich |
| **Q** | **Fluss steuern** | | |
| -QA | elektrische Energie schalten | **Schütz (QAA)**, Leistungs- und Motorschutzschalter (QAB), Halbleiterschalter/SSR (QAC) | gleich |
| -QB | elektrisch trennen | Lasttrennschalter, Hauptschalter (QBA) 🔎 (PAL nennt den Hauptschalter unter QA) | gleich |
| -QM | Fluid schalten (geschlossen) | **Wegeventil**, Absperr-, Schnellentlüftungsventil | gleich |
| -QN | Fluid stetig verstellen | Proportional-, Stellventil | 🔎 |
| **R** | **Begrenzen, stabilisieren** | | |
| -RA | elektrisch begrenzen | Diode (RAA), Widerstand (RAC), Drossel (RAB) | gleich |
| -RM | Rückfluss sperren | Rückschlagventil (RMA) | gleich |
| -RN | Durchfluss begrenzen | **Drosselventil, Drosselrückschlagventil**, Stromregelventil | **-RZ** für das Drosselrückschlagventil (-RN war nur die Drossel) |
| **G** | **Fluss erzeugen** | | |
| -GQ | Gasstrom | Kompressor (GQA), Lüfter (GQB); Wartungseinheit: Klasse G laut PAL 🔎 | 2009: Wartungseinheit oft -AZ (Klasse A entfällt) |
| -GP | Flüssigkeitsstrom | Pumpe (GPA Verdränger-, GPB Kreiselpumpe) | gleich |
| -GA / -GB | Generator / Batterie (Primärzelle) | Generator, Batterie; Akku: -CC | 🔎 |
| **T** | **Umwandeln** | | |
| -TA | Energie, gleiche Stromart | Transformator (TAA), Frequenzumrichter (TAC) | 🔎 |
| -TB | AC ↔ DC | Gleichrichter (TBA), Wechselrichter (TBB) | gleich |
| -TC | Stromversorgung | Netzteil 24 V DC (TCB) | 🔎 |
| -TF | Signal umwandeln | Messumformer (TFC), Verstärker (TFA) | gleich |
| **E, F, C, W, X** | | | |
| -EA / -EB | Licht / elektrische Heizung | Leuchte, Lampe / Heizstab, Heizkabel | gleich |
| -FC | Überstrom schützen | Sicherung (FCA), Leitungsschutzschalter (FCB), Bimetall-Überlastrelais (FCC) | gleich |
| -FB | Fehlerstrom schützen | Fehlerstrom-Schutzschalter (RCD) 🔎 | gleich |
| -CA / -CC / -CM | speichern | Kondensator / Akku / Tank, Behälter | 🔎 |
| -WD / -WG / -WH | leiten | Energiekabel / Signal-, Datenleitung (WGB) / Lichtwellenleiter | gleich |
| -XD / -XG | verbinden | Klemme, Steckdose / Signalklemme, Anschlussdose, Patchfeld (XGC) | gleich |

„gleich“ heißt: Kennbuchstabe und Bedeutung decken sich in Prüfungsaufgaben; die Unterklassen der
Ausgabe 2009 sind nur teilweise belegt (🔎). Belegte Änderungen 2009 → 2020: Taster -SF → **-SJ**,
Drosselrückschlagventil -RZ → **-RN**, Klasse A (z. B. -AZ) entfällt, SPS -KF → **-KE** 🔎.

**Für die Aufgabe**
- Je Betriebsmittel Klasse **und** Unterklasse aus der Tabelle festlegen (inhärente Funktion). Ein
  nicht aufgeführter Code wird mit Tabelle 2 der Norm geprüft.
- Legende: BMK | Betriebsmittel | Lage bzw. Aufgabe (T.3); bei mehrdeutigen Fällen (Lichtschranke
  als Objektmelder: -BR oder -BG) die Aufgabe des Betriebsmittels nennen.
- In Netzplänen sind Gerätenamen wie „SW1“, „R1“ üblich; Referenzkennzeichen (-KFE, -KED) nur, wenn
  eingeführt.
- Fluidtechnik: Die Kennzeichnung nach ISO 1219-2 (z. B. „1V1“, „1A1“) ist eine andere Systematik –
  nicht mit -QM1/-MM1 mischen.

## 3. GRAFCET – DIN EN 60848

**Ausgabe:** DIN EN 60848:2014-12 (IEC 60848:2013, 3. Ausgabe; keine neuere bekannt). GRAFCET ist
eine **herstellerunabhängige Spezifikation** des Ablaufs; die Ablaufsprache (AS) der IEC 61131-3 und
Herstellersprachen (z. B. S7-GRAPH) sind Programmiersprachen. Im Auftrag unterscheiden:
„Entwickeln Sie einen GRAFCET“ ≠ „Programmieren Sie die Schrittkette in AS“. Weil GRAFCET nichts über
die Plattform sagt, ist er die gemeinsame Spezifikation für SPS, Kleinsteuerung und Mikrocontroller.
Festlegungen der Bibliothek (Notationsblatt): Initialschritt 0, getippte Negation „¬“, Zeit „5s/X3“
ohne Leerzeichen, Analogbedingungen mit physikalischem Wert und Einheit („[-BT1 > −16 °C]“), Textform
als Tabelle Schritt | Aktion | Transition zum Folgeschritt (`bmk_pruefen.py`, T.9).

| Element | Darstellung und Regel |
|---|---|
| Schritt | Quadrat mit Name (Zahl, auch 9a); Schrittvariable **X** + Name (X3) ist 1, solange der Schritt aktiv ist |
| Initialschritt | **doppelt umrandet**; aktiv beim Start ohne Bedingung; entspricht der Grundstellung |
| Transition | Querstrich auf der Wirkverbindung, **Bedingung rechts**, optional Name links in Klammern „(T3)“; Quelltransition ohne Verbindung nach oben, Schlusstransition ohne Verbindung nach unten |
| Wirkverbindung | Schritt und Transition wechseln sich ab; von oben nach unten ohne Pfeil, **aufwärts mit Pfeil** (Rücksprung) |
| Logik | UND „·“ (auch „*“), ODER „+“, NICHT als Überstrich; UND vor ODER, sonst Klammern; „1“ unterstrichen = immer erfüllt (Aufgaben schreiben es auch ohne Strich) |
| Flanke | ↑a steigend, ↓a fallend (Pfeil vor der Variablen) |
| Zeit | „t1/Variable/t2“, meist „5s/X3“ = 5 s nach Aktivierung von Schritt 3; „3s/-BG1“ = -BG1 seit 3 s ununterbrochen 1 |
| Vergleich | Bedingungen aus Zahlenwerten in eckigen Klammern, z. B. [C = 3], [-BT1 > −16 °C] 🔎 |
| Kommentar | in Anführungszeichen: „Zylinder fährt aus“ |
| Alternativverzweigung | ein Schritt, mehrere Transitionen; Bedingungen **schließen sich gegenseitig aus** |
| Parallelverzweigung | eine Transition aktiviert mehrere Schritte; Beginn und Ende mit **Doppelstrich**; die Transition nach der Zusammenführung schaltet erst, wenn alle letzten Schritte aktiv sind (Synchronisation) |
| Strukturierung | Makroschritt (Querlinien oben und unten, M…), einschließender Schritt (abgeschrägte Ecken; Rahmen um die eingeschlossene Kette, oben sein Name, zuerst aktiver Schritt mit *), Teil-GRAFCET (G…), Zwangssteuerung im Doppelrahmen: G5 {INIT}, { } leer, {3,4,8} bestimmte Schritte, {*} eingefroren – nur, wenn im Unterricht eingeführt (Betriebsarten, Not-Halt) |

**Aktionen** (Rechteck rechts am Schritt; mehrere Aktionen wirken gleichzeitig)

| Art | Darstellung | Wirkung |
|---|---|---|
| kontinuierlich wirkend | Variable im Rechteck: „-MA1“ | 1, solange der Schritt aktiv ist; danach 0 |
| mit Zuweisungsbedingung | Bedingung an einem Strich über dem Rechteck | 1, solange Schritt aktiv **und** Bedingung erfüllt |
| zeitabhängig | Zuweisungsbedingung mit Zeit („2s/X6“), mit Überstrich zeitbegrenzt | verzögert bzw. zeitbegrenzt |
| speichernd wirkend | **im Rechteck immer die Zuweisung** („-QA1 := 1“), **am Rechteck der Auslöser**: Pfeil nach oben an der linken Kante bei Aktivierung, nach unten bei Deaktivierung, Strich mit Fähnchen und Ereignis („↑-BG1“) bei Ereignis | Wert bleibt bis zur nächsten Zuweisung („-QA1 := 1“ … „-QA1 := 0“) |

Regeln für Musterlösung und Merkmale:
- Kontinuierlich und speichernd wirkende Aktionen **nie auf dieselbe Variable**; speichernde
  Aktionen vor allem für interne Variablen und Zähler („C := C + 1“), Rücksetzen nicht vergessen.
- **Kontaktart** steckt in der Bedingung: Ein Öffner (NC) liefert unbetätigt 1 – „Stopp betätigt“ ist
  dann der negierte Wert. Die Kontaktart steht deshalb im Schülermaterial (T.4).
- Gleichwertig sind: andere Schrittnummern und Kommentare, zusätzliche Leerschritte, gleichwertige
  Bedingungen (z. B. Klammern), kontinuierliche statt speichernde Aktion bei gleicher Wirkung –
  Merkmale funktional formulieren.
- Typische Fehler (Prüfsteine, 0 BE für das Normmerkmal): Schritt an Schritt ohne Transition,
  Rücksprung ohne Pfeil, kein Initialschritt, Alternativzweige nicht ausschließend, speichernde Aktion
  ohne Zuweisung („-QA1“ statt „-QA1 := 1“) oder ohne Pfeil am Rechteck, speichernd gesetzt und nie
  zurückgesetzt, Zeit auf den falschen Schritt bezogen, Öffner nicht negiert.
- **Positionssensor beim Weiterdrehen:** Meldet ein Sensor die Ruhelage und bleibt beim Anlaufen noch
  belegt, schaltet die Transition „-BG1“ sofort, der Antrieb läuft nie. Richtig: Flanke „↑-BG1“ oder
  zwei Schritte mit „¬-BG1“ (Position verlassen) und „-BG1“ (nächste Position erreicht); beide gleichwertig.

## 4. Steuerungsprogramme – IEC 61131-3 und Mikrocontroller

**Ausgabe:** IEC 61131-3:2025 (4. Ausgabe, Mai 2025) ersetzt die Ausgabe 2013 (DIN EN 61131-3:2014-06);
deutsche Fassung 🔎. Wichtigste Änderung für Aufgaben: **AWL (Anweisungsliste, IL) ist gestrichen**
(seit 2013 als veraltet gekennzeichnet). Hersteller bieten AWL/STL zum Teil weiter an – in neuen
Aufgaben nicht verlangen.

| Sprache | Art | Hinweis für Aufgaben |
|---|---|---|
| KOP – Kontaktplan (LD) | grafisch | Öffner/Schließer der **Programmlogik**, nicht der Geberkontakte: Ein NC-Geber wird mit Schließerabfrage auf 1 geprüft |
| FUP – Funktionsbausteinsprache (FBD) | grafisch | Logiksymbole &, ≥1, =1; Negation als Kreis |
| ST – Strukturierter Text | textuell | IF/CASE/FOR; Zuweisung „:=“, Vergleich „=“ |
| AS – Ablaufsprache (SFC) | Struktur | Schritte, Transitionen, Aktionen; nicht mit GRAFCET gleichsetzen |

- **Standardbausteine:** TON (Einschaltverzögerung), TOF (Ausschaltverzögerung), TP (Impuls), CTU,
  CTD, CTUD (Zähler), R_TRIG/F_TRIG (Flanken), SR (**setzdominant**), RS (**rücksetzdominant**).
- **Operanden:** Normform „%IX0.0“, „%QX0.1“, „%MW10“ (Eingang, Ausgang, Merker; X Bit, W Wort);
  Herstellerformen wie „%I0.0“, „E0.0“, „I1“ (LOGO). Die Schreibweise der eingesetzten Steuerung
  im Schülermaterial festlegen (Zuordnungsliste mit Beispielzeile, T.5).
- **Datentypen und Literale:** BOOL, INT, REAL, TIME („T#5s“). Analogwerte: Zahlbereich der
  Baugruppe angeben (Abschn. 7).

**Mikrocontroller als Steuerung** (RRL: IT1 „Steuerungseinheiten“, IT4 „Mikrocontroller für die
Messhardware“). Für Mikrocontroller gibt es keine Norm wie IEC 61131-3; die Aufgabe legt fest, was
die Lösung bestimmt:

| Punkt | Festlegen in der Aufgabe bzw. Anlage | Hintergrund |
|---|---|---|
| Board und Pegel | Board, Logikpegel, ob eine Ein-/Ausgabeplatine 24-V-Geber anpasst | Arduino Uno 5 V; ESP32, STM32 und Raspberry Pi Pico 3,3 V (Tabelle unten); 24-V-Geber nur über Optokoppler oder Spannungsteiler |
| Eingangslogik | Spalte „Signal 1 bedeutet“; Pull-up oder Pull-down | Mit internem Pull-up und Taster gegen Masse liefert ein **betätigter Schließer 0** – die Kontaktart allein bestimmt das Signal nicht mehr |
| Ausgänge | Treiber (Transistor, Relaismodul), ggf. invertierend | Ein Pin liefert nur wenige Milliampere (Uno: 20 mA empfohlen, 40 mA absolut; andere Boards laut Datenblatt 🔎); viele Relaismodule schalten bei Low |
| Analogeingang | Wertebereich **im Programm**, Bürdenwiderstand | hängt von Board, Bibliothek und Einstellung ab (Tabelle unten) – nie nur „12 bit“ angeben |
| Taster | ob Entprellen zur Aufgabe gehört | mechanische Kontakte prellen einige Millisekunden; Software-Entprellung z. B. 20 ms 🔎 |
| Zeiten | Zeit seit Schrittbeginn statt Warteschleife | `delay()` blockiert den Zyklus; Zeitbedingung „5s/X3“ als Vergleich mit der beim Schrittwechsel gespeicherten Zeit (`millis()`) |
| Programmstruktur | Zyklus wie bei der SPS | Eingänge lesen → Transitionen prüfen, Schritt wechseln → Ausgänge aus dem aktiven Schritt setzen; GRAFCET als Zustandsautomat (Variable für den aktiven Schritt, `switch`/`if`) |
| Sprache | „in der im Unterricht verwendeten Sprache“ | C/C++ (Arduino-Umgebung) oder Python (MicroPython); Bezeichner `PIN_SJ1`, `sj1` nach Notationsblatt |
| Sicherheit | Not-Halt und Schutzfunktionen ausklammern | Ein Mikrocontroller ist wie eine Standard-SPS keine Sicherheitssteuerung (Abschn. 6) |

**Analogwerte je Plattform** – den Wertebereich, mit dem das Programm rechnet, in der Anlage nennen;
sonst hat eine Umrechnung mehrere richtige Ergebnisse (K.4).

*Siemens SPS (S7-1200/1500; Analogbaugruppen und -signalboards):*

| Signal | Nennbereich | Übersteuerung bis | Untersteuerung bis | Überlauf / Unterlauf |
|---|---|---|---|---|
| ±10 V, ±5 V, ±20 mA (bipolar) | **−27 648 … +27 648** | 32 511 | −32 512 | 32 767 / −32 768 |
| 0 … 10 V, 0 … 20 mA (unipolar) | 0 … 27 648 | 32 511 (11,76 V bzw. 23,52 mA) | – 🔎 | 32 767 / −32 768 |
| 4 … 20 mA, 1 … 5 V (lebender Nullpunkt) | 0 … 27 648 (4 mA ↦ 0) | 32 511 (22,81 mA) | −4 864 (1,185 mA) | 32 767 / −32 768 (Drahtbruch) |

Umrechnen mit NORM_X (Rohwert → 0,0 … 1,0; bei bipolaren Signalen MIN = −27 648) und SCALE_X
(→ physikalischer Wert); ältere Steuerungen mit dem Baustein SCALE. Analogausgänge nutzen dieselben
Bereiche.

*Kleinsteuerungen und weitere Steuerungen:*

| System | Operanden | Analogwert 0 … 10 V | Analogwert 4 … 20 mA | Hinweise |
|---|---|---|---|---|
| **Siemens LOGO!** (8) | I1 …, Q1 …, AI1 … AI8, AQ1 … AQ8, Merker M1 …, Analogmerker AM1 … 🔎 Anzahl je Modell | 0 … 1000 (über 10 V bleibt 1000) | **200 … 1000** – das Analogmodul rechnet auf 0 … 20 mA, 4 mA ergibt 200 | Basisgeräte 12/24 V: I1, I2, I7, I8 als Analogeingänge (0 … 10 V) nutzbar 🔎; Analogverstärker: Wert · Gain + Offset, für 4 … 20 mA → 0 … 1000 **Gain 1,25, Offset −250**; Analogausgang 0 … 1000 |
| **Eaton easyE4** | Basisgerät I1 … I16, Q1 … Q16; Erweiterungen ab I17, Q17; Analog IA1 … IA4 (Basisgerät, = I5 … I8), ab IA5 bzw. QA5 (Erweiterung); Merker M, MB, MW, MD | 0 … 4095 (12 bit, Datentyp DINT); Basisgerät DC/UC nur 0 … 10 V | **819 … 4095** (Erweiterung EASY-E4-DC-6AE1; bezogen auf 0 … 20 mA) | 0 … 20 mA → 0 … 4095; Pt100- und Ni1000-Erweiterungen liefern skalierte Temperaturen; ältere easy500/700/800: 10 bit, 0 … 1023 🔎 |
| **WAGO** 750 mit PFC100/PFC200 (CODESYS, e!COCKPIT) | IEC 61131-3: %IX, %QX (Byte.Bit), %IW, %QW; im Prozessabbild **zuerst Analog- und Sondermodule wortweise, dann die Digitalbits** – die Adresse hängt von der Modulreihenfolge ab | 0 … **32 760** (0x7FF8), 5 V ↦ 16 384 (750-459) | 0 … **32 760** (750-466, neuere 750-455; ältere Handbücher 0x7FFC) | Messwert in Bit 14 … 3 (12 bit), Bit 2 … 0 Status – für 0 … 4095 drei Bit nach rechts schieben; Über-/Unterbereich: nächster darstellbarer Wert und Statusbyte 0x42 bzw. 0x41; Varianten mit anderem Bereich (z. B. /000-003: 3,8 … 20,5 mA) laut Handbuch 🔎 |

LOGO! und easyE4 beziehen 4 … 20 mA auf den Bereich 0 … 20 mA: Der Rohwert beginnt **nicht** bei 0. In
Aufgaben deshalb den Rohwertbereich für 4 mA und 20 mA ausdrücklich nennen oder die Skalierung
(Gain/Offset bzw. Skalierungsbaustein) vorgeben.

*Mikrocontroller:*

| Board | Pegel | ADC | Wert im Programm | Pins | 4 … 20 mA über Bürde |
|---|---|---|---|---|---|
| Arduino Uno (ATmega328P) | 5 V | 10 bit, Referenz 5 V | `analogRead`: 0 … 1023 | D2 … D13, A0 … A5 | 250 Ω → 1 … 5 V → 205 … 1023 |
| ESP32 | 3,3 V, nicht 5-V-fest | 12 bit, nichtlinear an den Bereichsgrenzen; Messbereich je Dämpfung (bei 11 dB laut Espressif etwa 0,15 … 2,45 V genau 🔎) | Arduino-Kern `analogRead`: 0 … 4095 (Rohwert), `analogReadMilliVolts`: kalibrierte mV; MicroPython `read_u16`: 0 … 65 535 | GPIO-Nummer (GPIO34); bei aktivem WLAN nur ADC1-Pins (GPIO32 … GPIO39) | 120 Ω → 0,48 … 2,4 V → 480 … 2400 mV |
| STM32 (z. B. Nucleo-Boards) | 3,3 V; viele Pins 5-V-fest, nicht im Analogbetrieb 🔎 | meist 12 bit, Referenz 3,3 V (einige Familien bis 16 bit) | Arduino-Kern: `analogRead` 10 bit, mit `analogReadResolution(12)` 0 … 4095; MicroPython `read_u16`: 0 … 65 535 | Port und Nummer (PA0, PB12) | 120 Ω → 0,48 … 2,4 V → 596 … 2978 (12 bit) |
| Raspberry Pi Pico (RP2040, RP2350) | 3,3 V | 12 bit, Referenz 3,3 V; Analog an GP26 … GP28 | MicroPython `read_u16`: 0 … 65 535 (12 bit hochskaliert); Arduino-Kern: `analogRead` 10 bit, mit `analogReadResolution(12)` 0 … 4095 | GP0 … GP28 | 120 Ω → 0,48 … 2,4 V → 596 … 2978 bzw. 9 532 … 47 662 |

- Bürde so wählen, dass 20 mA unter dem genauen Eingangsbereich bleiben (3,3-V-Boards: 120 Ω, 5-V-Board:
  250 Ω) und die Platine einen Schutz gegen Überspannung hat.
- Umrechnung Spannung → Wert als Wert = U / U_ref · (2ⁿ − 1) vorgeben (manche Lehrbücher teilen durch
  2ⁿ) und die Rundung festlegen; beim ESP32 besser die kalibrierte Spannung in mV verwenden.

**Plattformneutrale Steuerungsaufgaben** (wenn die Schule mehrere Plattformen nutzt):
- Funktion als GRAFCET bzw. Logikplan verlangen; Analogwerte im GRAFCET als physikalische Größe.
- Zuordnungsliste mit Spalten „Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller“ und einer
  Anlage mit den verfügbaren Ein- und Ausgängen je Plattform; Rohwert-Rechnungen nur, wenn die
  Plattform feststeht – sonst Stromstärke bzw. Spannung als plattformneutrale Größe rechnen lassen.
- Programmaufträge „in der im Unterricht verwendeten Sprache“; Merkmale prüfen das Verhalten
  (Schrittwechsel, Ausgänge, Zeiten), nicht eine Plattform.

## 5. Schaltpläne, Schaltzeichen, Anschlussbezeichnungen

| Gegenstand | Norm | Kern für Aufgaben |
|---|---|---|
| Schaltzeichen Elektrotechnik | IEC 60617 (Datenbank), DIN EN 60617 🔎 | Kontakte, Spulen, Geber, Melder; binäre Logik &, ≥1, =1, 1 mit Negationskreis |
| Dokumente der Elektrotechnik | DIN EN 61082-1:2015 (IEC 61082-1:2014) | Übersichtsschaltplan, Stromlaufplan (aufgelöste Darstellung, Strompfade nummeriert), Anschlussplan; Betriebsmittel unbetätigt und spannungslos dargestellt 🔎 |
| Anschlüsse an Schaltgeräten | DIN EN 60947-1 und -5-1 🔎 | Spule A1/A2; Hauptkontakte 1-2, 3-4, 5-6; Hilfskontakte: erste Ziffer Ordnungsziffer, zweite Funktionsziffer – **1-2 Öffner, 3-4 Schließer**, 5-6/7-8 Öffner/Schließer mit Sonderfunktion (z. B. verzögert) |
| Leiter und Motoranschlüsse | DIN EN 60445 🔎 | L1, L2, L3, N, PE; Motorwicklung U1-U2, V1-V2, W1-W2 |
| Schaltzeichen Fluidtechnik | DIN ISO 1219-1:2019-01 (ISO 1219-1:2012 + Amd 1:2016) | Wegeventil „5/2“ (Anschlüsse/Schaltstellungen), Betätigungsarten, Zylinder, Drossel |
| Fluidtechnische Schaltpläne | ISO 1219-2:2012 🔎 | eigene Kennzeichnung (z. B. 1V1) – nicht mit 81346 mischen (Abschn. 2) |
| Ventilanschlüsse pneumatisch | ISO 11727 🔎 | 1 Druckluft, 2 und 4 Arbeitsanschlüsse, 3 und 5 Entlüftung, 12 bzw. 14 Steueranschluss (verbindet 1 mit 2 bzw. 1 mit 4) |

Für Aufgaben: Vorlagen (Anschlussplan, Schaltplanausschnitt) als Anlage mit Schaltzeichen des
Unterrichts; die Musterlösung verwendet dieselben Zeichen und Anschlussbezeichnungen.

## 6. Sicherheit an Maschinen – Bedienteile, Farben, Stopp, Not-Halt

**Ausgaben:** DIN EN 60204-1 (VDE 0113-1):2019-06 (IEC 60204-1:2016; Änderung A1 🔎), DIN EN ISO
13850:2016 (Not-Halt), DIN EN 60073 (Farbbedeutung), DIN EN ISO 13849-1:2023 (sicherheitsbezogene
Steuerungsteile, Performance Level).

| Bedienteil | Farbe |
|---|---|
| Start/Ein | **weiß** (bevorzugt), grau, schwarz, grün – **nicht rot** |
| Stopp/Aus | **schwarz** (bevorzugt), grau, weiß; rot erlaubt, aber nicht nahe dem Not-Halt – **nicht grün** |
| abwechselnd Start/Stopp, Tippen | weiß, grau, schwarz – nicht rot, gelb, grün |
| Rücksetzen (Quittieren) | blau, weiß, grau, schwarz – nicht grün |
| Not-Halt | **rot auf gelbem Grund**, nur für Not-Halt |

| Leuchtmelder | Bedeutung |
|---|---|
| rot | Notfall, gefährlicher Zustand – sofort handeln |
| gelb | anormal, kritischer Zustand steht bevor |
| grün | normal, sicherer Betrieb |
| blau | zwingend – Bedienperson muss handeln |
| weiß | neutral, Bestätigung |

- **Stopp-Kategorien:** 0 = Energie sofort abschalten (ungesteuertes Stillsetzen); 1 = gesteuert
  stillsetzen, Energie danach abschalten; 2 = gesteuert stillsetzen, Energie bleibt. **Not-Halt nur
  Kategorie 0 oder 1.**
- **Stopp vor Start:** Ein Stoppbefehl hat Vorrang vor dem zugehörigen Start (rücksetzdominant
  speichern).
- **Not-Halt:** rastet ein; das Entriegeln darf die Maschine nicht wieder anlaufen lassen –
  Neustart nur mit eigenem Startbefehl.
- **Ruhestromprinzip:** Stopp-, Not-Halt- und Sicherheitsgeber als Öffner (drahtbruchsicher; Not-Halt
  mit Zwangsöffnung). Folge für Aufgaben: Kontaktart angeben und in Bedingungen beachten (Abschn. 3).
- **Grenze der Aufgabe:** Eine Standard-SPS ist keine Sicherheitssteuerung. Sicherheitsfunktionen
  (Not-Halt, Schutztür) ausdrücklich ausklammern („Der Not-Halt ist hardwaremäßig gelöst …“, T.7)
  oder als Beurteilungsaufgabe stellen (Risiko, Performance Level nach DIN EN ISO 13849-1 – nur wenn
  unterrichtet).

## 7. Sensorik, Einheitssignale, Regelungstechnik

**Einheitssignale** (IEC 60381 🔎): 4 … 20 mA, 0 … 20 mA, 0 … 10 V.
- 4 … 20 mA hat einen **lebenden Nullpunkt**: Ein Strom unter 4 mA zeigt Drahtbruch oder Ausfall.
  NAMUR-Empfehlung NE 43 (keine Norm): Messbereich 3,8 … 20,5 mA, Ausfall ≤ 3,6 mA oder ≥ 21 mA.
- **Lineare Umrechnung** (in der Aufgabe vorgeben oder als bekannt voraussetzen, wenn unterrichtet):
  x = x_min + (I − 4 mA) · (x_max − x_min) / 16 mA.
- **Digitalwert** der Analogbaugruppe angeben (Siemens 0 … 27 648 für 4 … 20 mA, −27 648 … +27 648 für
  ±10 V; Mikrocontroller je Board und Funktion, Abschn. 4) – sonst hat die Aufgabe mehrere richtige
  Ergebnisse (K.4).

**Pt100** – DIN EN IEC 60751 (IEC 60751:2022 🔎; vorher DIN EN 60751:2009):
- R₀ = 100 Ω bei 0 °C, R(100 °C) = 138,51 Ω, mittlerer Temperaturbeiwert α = 0,003 85 K⁻¹.
- Grenzabweichungen: Klasse AA ±(0,1 + 0,0017·|ϑ|) °C, A ±(0,15 + 0,002·|ϑ|) °C,
  B ±(0,3 + 0,005·|ϑ|) °C, C ±(0,6 + 0,01·|ϑ|) °C.
- Für Aufgaben die **lineare Näherung** R = R₀ · (1 + α · ϑ) ausdrücklich vorgeben (sonst Rechnung
  nach Callendar-Van Dusen) und die Toleranz im Erwartungshorizont nennen.

**Regelungstechnik** – DIN IEC 60050-351:2014-09 (ersetzt DIN 19226):

| Größe | Formelzeichen |
|---|---|
| Regelgröße | x |
| Führungsgröße (Sollwert) | w |
| Regeldifferenz | **e = w − x** |
| Stellgröße | y |
| Störgröße | z |
| Rückführgröße | r |

- Ältere Literatur rechnet mit der Regelabweichung x_w = x − w (umgekehrtes Vorzeichen); Lehrbücher
  der Systemtheorie nennen die Regelgröße y und die Stellgröße u. **Formelzeichen und Vorzeichen im
  Schülermaterial festlegen.**
- Wirkungsplan (Blockschaltbild): Blöcke mit Übertragungsverhalten, Vergleichsstelle als Kreis mit
  Vorzeichen.

## 8. Netzwerke

**Strukturierte Verkabelung** – DIN EN 50173-1 (VDE 0800-173-1):2018-10 (ISO/IEC 11801-1:2017); Teil 2
Bürogebäude, Teil 3 Industrie; Installation: DIN EN 50174.
- Bereiche: Primärbereich (Standort, zwischen Gebäuden) · Sekundärbereich (Gebäude, Steigbereich) ·
  Tertiärbereich (Etage, bis zur Anschlussdose); Verteiler: Standort-, Gebäude-, Etagenverteiler.
- Längen Kupfer im Tertiärbereich: Übertragungsstrecke (Channel) höchstens 100 m, davon fest
  verlegte Strecke (Permanent Link) höchstens 90 m 🔎.
- **Klasse** gilt für die Strecke, **Kategorie** für die Komponente: D / Kat. 5e (100 MHz), E / Kat. 6
  (250 MHz), E_A / Kat. 6_A (500 MHz), F / Kat. 7 (600 MHz), F_A / Kat. 7_A (1000 MHz), I und II /
  Kat. 8.1 und 8.2 (2000 MHz, höchstens 30 m).

**IEEE 802** – 802.3 Ethernet (z. B. 1000BASE-T, 10GBASE-T); PoE: 802.3af 15,4 W, 802.3at 30 W,
802.3bt 60 W bzw. 90 W (je Port an der Quelle); 802.1Q VLAN (VLAN-ID 1 … 4094, 4-Byte-Tag); 802.1X
portbasierte Authentifizierung; 802.11 WLAN.

**Adressen** (RFCs) – in fiktiven Szenarien nur diese Bereiche verwenden:

| Zweck | Bereich | RFC |
|---|---|---|
| private IPv4-Netze | 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 | 1918 |
| **„öffentliche“ Adressen in Beispielen** | 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | 5737 |
| IPv6 in Beispielen | 2001:db8::/32, 3fff::/20 | 3849, 9637 |
| IPv6 privat (ULA) | fc00::/7, genutzt fd00::/8 | 4193 |
| Link-local | 169.254.0.0/16 bzw. fe80::/10 | 3927, 4291 |
| Provider-NAT | 100.64.0.0/10 | 6598 |
| Loopback | 127.0.0.0/8 bzw. ::1 | 1122, 4291 |

- **IPv6-Schreibweise** (RFC 5952): Kleinbuchstaben, führende Nullen je Block weglassen, die längste
  Folge von mindestens zwei Null-Blöcken durch „::“ ersetzen (bei Gleichstand die erste), nie für
  einen einzelnen Block. Musterlösung in dieser Form; andere gültige Kurzformen als *Gleichwertig*.
- **IPv4:** Präfix in CIDR-Schreibweise und Subnetzmaske angeben; Netz- und Broadcastadresse sind keine
  Hostadressen – in der Aufgabe sagen, ob das Gateway die erste oder die letzte nutzbare Adresse ist.

## 9. Software – UML, Struktogramm, Programmablaufplan

- **UML** – OMG UML 2.5.1 (ISO/IEC 19505-2:2012 entspricht UML 2.4.1). Klassendiagramm: Sichtbarkeit
  + public, − private, # protected, ~ package; Attribut „name : Typ“, Operation
  „name(p : Typ) : Rückgabetyp“; statisch unterstrichen, abstrakt kursiv; Assoziation mit
  Multiplizität (1, 0..1, *, 1..*), Aggregation (leere Raute), Komposition (gefüllte Raute),
  Generalisierung (geschlossene leere Pfeilspitze). Zustandsdiagramm: Transition
  „Ereignis [Wächter] / Effekt“.
- **Struktogramm** – DIN 66261:1985 (Nassi-Shneiderman); **Programmablaufplan** – DIN 66001:1983.
- **SQL** – ISO/IEC 9075; den Dialekt des Unterrichts (z. B. SQLite, MySQL) nennen.
- Pseudocode ist nicht genormt: zulässige Sprachelemente als Anlage oder Hilfsmitteldokument.

**Notationsrahmen Informatik in Niedersachsen** – Ergänzende Hinweise zum Kerncurriculum Informatik
(Neufassung Juni 2025, verbindlich für das Zentralabitur ab 2027; ein Teil ist dort als Hilfsmittel
zugelassen). Für das Fach Technik nicht verbindlich, aber das Vorbild, an dem sich Lernende und
Zweitkorrektur orientieren – für Software- und Datenbankteile übernehmen oder Abweichungen in der
Anlage festlegen:
- **Signaturen** wie im Klassendiagramm: `bezeichnung(parameter: Typ, …): Rückgabetyp`, Typnamen
  deutsch (Ganzzahl, Fließkommazahl, Zeichenkette, Wahrheitswert, „dynamische Reihung vom
  Inhaltstyp …“).
- Sprachunabhängig: **Index ab 0** (Zeichenketten, Reihungen), `/` bei zwei Ganzzahlen ganzzahlig,
  `mod` als kleinster positiver Rest, zweidimensionale Reihung `[Zeile][Spalte]`. Bei
  Implementierungen gilt die Syntax der Unterrichtssprache.
- **Zulässige Operationen** werden aufgezählt (Zeichenketten: Länge, Zeichen an Position,
  Teilzeichenkette, Verbinden, Vergleich …; Datenstrukturen mit festen Methodennamen); darüber
  hinausgehende Operationen sind nicht zulässig. Laufzeitfehler (leerer Stapel, ungültiger Index)
  muss die Lösung ausdrücklich abfangen.
- **Struktogramm:** Formulierungen sprachunabhängig, sprachlich („erhöhe anzahl um 1“) oder formal
  („anzahl ← anzahl + 1“); Kommentar mit `//`; „gib … zurück“ beendet die Operation; „erzeuge …“
  ruft den Konstruktor auf.
- **Klassendiagramm:** Sichtbarkeit `+`/`-` im Normalfall Pflicht, Konstruktor mit vorangestelltem
  `c`, nicht aufgeführte Attribute bzw. Operationen als „…“, Assoziationen als einfache Linien;
  Objektkarte `name : Klasse` mit Attributbelegung.
- **Datenbank:** Kurzschreibweise `Tabelle(Schlüssel, Attribut, ↑Fremdschlüssel)` mit
  unterstrichenem Primärschlüssel; ER-Diagramm mit Kardinalitäten (1, n, m) und Schlüsselattributen;
  **SQL-Umfang** SELECT [DISTINCT] … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT,
  Verknüpfung über FROM und WHERE (kein JOIN-Schlüsselwort), Vergleiche einschließlich LIKE mit `_`
  und `%`, Aggregatfunktionen AVG, COUNT, MAX, MIN, SUM; keine verschachtelten Abfragen.
- **Automaten und Grammatiken:** Eingabealphabet Σ, Zustandsgraph; Mealy-Übergang
  „Eingabe/Ausgabe“, leere Ausgabe ε; Kellerautomat „(oberstes Kellerzeichen, Eingabe) :
  abgelegte Zeichen“ mit Vorbelegung #; Grammatik mit N, T, Startsymbol und Regeln, regulär
  rechtsregulär notiert.
- **Codierung:** Lauflängencodierung „Anzahl-Wert“; Kompressionsverhältnis = komprimiert /
  original; (7,4)-Hamming-Code in der Reihenfolge p0 p1 d0 p2 d1 d2 d3 mit gerader Parität.
- Die Vorgaben wechseln mit dem Jahrgang (2026 andere Baum-Operationen als ab 2027) – vor jedem
  Prüfungsjahr mit den aktuellen fachbezogenen Hinweisen abgleichen 🔎.
- Bezeichner aus Klassendiagramm und Code in Schüler- und Lehrermaterial gleich schreiben (K.9).

## 10. Größen, Einheiten, Schreibweise

DIN EN ISO 80000-1 (ISO 80000-1:2022 🔎), DIN 1313 (Größen), DIN 1338 (Formelsatz):
- Zahl und Einheit mit Leerzeichen: „24 V“, „45 %“, „20 °C“; ohne Leerzeichen nur der ebene Winkel
  „90°“. Dezimalkomma. Bereiche „4 mA … 20 mA“ oder „(4 … 20) mA“.
- Formelzeichen kursiv, Einheiten aufrecht. „[U] = V“ heißt „Einheit von U“ – Spaltenköpfe daher
  „U in V“ oder „U / V“, nicht „U [V]“.
- **Datenmengen** – IEC 80000-13 🔎: Bit „bit“, Byte „B“; Dezimalvorsätze k = 10³, M = 10⁶;
  Binärvorsätze Ki = 2¹⁰, Mi = 2²⁰; Datenraten in bit/s (Mbit/s). In der Aufgabe festlegen, ob mit
  1 kB = 1000 B oder 1 KiB = 1024 B gerechnet wird – sonst zwei richtige Ergebnisse (K.4).

## 11. Quellen

Recherche 2026-10-30; Normtexte nicht eingesehen, außer der Leseprobe der IEC 81346-2:2019.
- IEC 81346-2:2019, Leseprobe (Abschnitte 4–5, Tabellen 1 und 2 Klasse B und C):
  https://cdn.standards.iteh.ai/samples/21908/1b996d119d0945b2b28359332ffa9b3f/IEC-81346-2-2019.pdf
- PAL/IHK Stuttgart: „DIN EN IEC 81346-2:2020-10 – Anwendung der aktuellen Referenzkennzeichnungen in
  PAL-Prüfungen“, Stand Juni 2024 (SF → SJ, RZ → RN, Beispielschaltpläne):
  https://www.ihk.de/blueprint/servlet/resource/blob/5090560/d005ab9b73c3e45d81920e28f72b7160/din-en-iec-81346-2-2020-10-referenzkennzeichnung-data.pdf
- PAL: „ISO 1219-2 (2012-09) und DIN EN 81346-2 (2009-10)“, Stand April 2016 (Ausgabe 2009: SF, SJ, RN, RZ):
  https://grafcet-schulungen.de/wp-content/uploads/2017/02/Referenzkennzeichnung_DIN_ISO_1219_81346_PAL_Stand_Dez_2016.pdf
- Wikipedia „IEC 81346“ und „EN IEC 81346“ (Unterklassen und dritte Ebene der Ausgabe 2019; Teil 1
  2022 mit Typaspekt „%“): https://en.wikipedia.org/wiki/IEC_81346, https://de.wikipedia.org/wiki/EN_IEC_81346
- DKE: DIN EN 60848:2014-12 (aktuell): https://www.dke.de/de/normen-standards/dokument?id=7049716&type=dke%7Cdokument
- Wikipedia „GRAFCET“; Europa-Lehrmittel, Leseprobe „GRAFCET“ (Transitionen, Zeiten, speichernde Aktionen):
  https://de.wikipedia.org/wiki/GRAFCET, https://www.europa-lehrmittel.de/leseprobe/37633-4.pdf
- IEC 61131-3:2025, Änderungen gegenüber 2013 (IL gestrichen): https://stefanhenneken.net/2025/06/11/iec-61131-3-comparison-of-edition-3-and-edition-4/
- IFAN: Vergleich DIN EN 60204-1 (VDE 0113-1):2019-06 (Farben, Stopp-Kategorien):
  https://ifan-normung.de/wp-content/uploads/2019/07/Vergleich_EN-60204-1-wa14.pdf
- DKE/Wikipedia zu DIN EN 50173-1:2018-10: https://de.wikipedia.org/wiki/EN_50173
- DIN Media zu DIN IEC 60050-351:2014-09: https://www.dinmedia.de/en/standard/din-iec-60050-351/116876648
- DIN ISO 1219-1:2019-01: https://webstore.ansi.org/standards/din/diniso12192019de
- RFC 1918, 3849, 3927, 4193, 4291, 5737, 5952, 6598, 9637 (rfc-editor.org).
- Niedersächsisches Kultusministerium: Ergänzende Hinweise zum Kerncurriculum Informatik, Neufassung
  Juni 2025 (lokal unter `Klausuren/Beispielklausuren/Abiturprüfungen/Normen Hinweise Notationen/`).
- Zentrale Abiturprüfungen Mechatronik Niedersachsen 2020–2026 (nur gelesen, Kennbuchstaben
  ausgezählt): Ausgabe 2009 (-SF, -RZ, -AZ).

## Anhang: references/notation-steuerungstechnik.md

# Notationsblatt Steuerungstechnik

Einheitliche Schreibweise der Bibliothek für Kennzeichen, Signale, Zuordnungsliste, GRAFCET und
Programme – für Prüfungsaufgaben, Erwartungshorizonte und Unterricht. Grundlage: DIN EN IEC 81346-2:2020,
DIN EN 60848:2014, IEC 61131-3:2025; Hintergrund und Quellen in `normen-technik.md` (Abschn. 2–4).
Stand 04.11.2026.

## Für die Lehrkraft

- **Teil „Anlage“ unten** dem Schülermaterial beifügen („## Anlage N – Notation Steuerungstechnik“,
  das Wort *Notation* in der Überschrift behalten), Abschnitte streichen, die die Aufgabe nicht braucht.
  `bmk_pruefen.py` überspringt diese Anlage bis zur nächsten Überschrift gleicher Ebene; ihre
  Beispiel-Kennzeichen zählen nicht zur Aufgabe. Keine Unterüberschriften in der Anlage. So arbeiten Prüfling, Erst- und Zweitkorrektur
  mit derselben Schreibweise.
- **Abweichungen des Unterrichts** (andere Ausgabe der Kennzeichnung, andere Zeitschreibweise) in der
  Anlage ändern und im Begleitblatt begründen – nie innerhalb eines Vorschlags mischen.
- **Plattformneutral stellen:** Steuerungsaufgaben müssen mit SPS, Kleinsteuerung **oder**
  Mikrocontroller lösbar sein, wenn die Schule mehrere Plattformen nutzt. Dafür:
  1. Funktion als GRAFCET bzw. Logikplan spezifizieren – beides ist plattformunabhängig.
  2. Analogwerte im GRAFCET als physikalische Größe mit Einheit; Rohwerte nur in plattformgebundenen
     Teilaufgaben und immer mit dem Bereich für 4 mA bzw. 20 mA in der Anlage (Bereiche je Plattform:
     `normen-technik.md`, Abschn. 4; für die Prüflinge stehen sie in der Anlage unten).
  3. Zuordnungsliste mit je einer Spalte je Plattform; die Prüflinge füllen die Spalte ihrer
     Plattform. Die verfügbaren Ein- und Ausgänge je Plattform stehen in einer Anlage.
  4. Programmieraufträge „in der im Unterricht verwendeten Sprache“; im Lehrermaterial *Gleichwertig*
     für jede Plattform.
- **Prüfen:** `bmk_pruefen.py` – T.6 Schreibweise, T.8 Kennbuchstaben, T.9 GRAFCET-Textform.

---

## Anlage – Notation Steuerungstechnik

**1. Kennzeichen der Betriebsmittel**

- Bindestrich, **Klasse und Unterklasse**, Zählnummer, ohne Leerzeichen: **-SJ1**, **-MA1**, **-MM1**,
  **-EA1** (DIN EN IEC 81346-2:2020). Die Klasse allein (-S1, -M1) wird nicht verwendet.
- Dieselbe Schreibweise gilt in **Funktionsbeschreibung, Technologieschema (Legende), Zuordnungsliste**,
  GRAFCET, Logikplan und Programm.
- Die Zählnummer zählt je Kennbuchstaben: -BG1, -BG2, -BP1.

| Kennbuchstaben | Betriebsmittel (Beispiele) |
|---|---|
| -SJ | Taster, Schalter, handbetätigtes Ventil |
| -BG | Näherungs-, End-, Zylinderschalter (Lage, Abstand) |
| -BP, -BL, -BT | Druckschalter; Füllstand, Schwimmerschalter; Temperaturfühler |
| -KE, -KF | Steuerung (SPS, Kleinsteuerung, Mikrocontroller); Relais, Zeitrelais |
| -QA, -QM | Schütz, Leistungsschalter; Wegeventil |
| -MA, -MB, -MM | Elektromotor; Ventilspule, Elektromagnet; Zylinder |
| -PF, -PJ | Leuchtmelder, Anzeige; Hupe, Summer |
| -EA, -EB | Leuchte, Lampe; Heizung |
| -RN, -RM | Drossel- und Drosselrückschlagventil; Rückschlagventil |
| -GP, -GQ | Pumpe; Kompressor, Lüfter |
| -TC, -TF | Netzteil; Messumformer |

**2. Signale**

- Im Text, im GRAFCET und im Logikplan steht das Kennzeichen für **sein Signal an der Steuerung**: -BG1
  ist 1 oder 0. Was 1 bedeutet, steht in der Zuordnungsliste (Spalte „Signal 1 bedeutet“).
- **Kontaktart:** NO = Schließer, NC = Öffner. Ein Öffner liefert im unbetätigten Zustand 1.
- **Analogwerte** stehen in Bedingungen als physikalischer Wert mit Einheit: [-BT1 > −16 °C],
  [-BL1 ≥ 80 %]. Die Umrechnung aus dem Rohwert ist Teil des Programms.
- **Interne Variablen** (Merker, Zähler) tragen einen sprechenden Namen ohne Bindestrich in
  Code-Schrift: `M_Pumpe`, `C_Teile`.

**3. Zuordnungsliste**

| BMK | Betriebsmittel | Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |
|---|---|---|---|---|---|---|
| -SJ1 | Taster Start | %I0.0 | I1 | D2 | Start betätigt | NO |
| -SJ2 | Taster Stopp | %I0.1 | I2 | D3 | Stopp nicht betätigt | NC |

- Ausgefüllt wird nur die Spalte der Plattform aus dem Unterricht; die anderen Spalten bleiben
  leer.
- Jeder Operand bzw. Pin wird genau einmal belegt. Analoggeber mit Messbereich und Signal
  („4 … 20 mA für 10 … 60 %“).
- Operanden wie in der Programmiersoftware: Siemens-SPS %I0.0, %IW64; WAGO %IX4.0, %IW0; LOGO! I1, AI1;
  Eaton easyE4 I1, IA1. Pins wie auf dem Board bezeichnet: D2 (Arduino), GPIO16 (ESP32), PB12 (STM32),
  GP2 (Raspberry Pi Pico).

**4. GRAFCET (DIN EN 60848)**

- **Schritt:** Quadrat mit Nummer; **Initialschritt doppelt umrandet** (Nummer 0). Schrittvariable
  X3 = 1, solange Schritt 3 aktiv ist.
- **Transition:** Querstrich, Bedingung rechts daneben, Name wenn nötig links in Klammern: (T2).
  Schritt und Transition wechseln sich ab; Verbindungen nach oben (Rücksprung) mit Pfeil.
- **Verzweigungen:** Alternativ mit einfacher Linie und einer Transition je Ast (die Bedingungen schließen
  sich gegenseitig aus); parallel mit Doppellinie unter der gemeinsamen Transition, zusammengeführt mit
  Doppellinie über der gemeinsamen Transition.
- **Bedingungen:**

  | Bedeutung | Schreibweise |
  |---|---|
  | UND | -SJ1 · -BG1 |
  | ODER | -BG2 + -BG3 |
  | NICHT | Überstrich über dem Kennzeichen; getippt **¬-SJ2** |
  | steigende bzw. fallende Flanke | ↑-BG1, ↓-BG1 |
  | Zeit seit Aktivierung von Schritt 3 | **5s/X3** |
  | Vergleich eines Zahlenwerts | **[-BT1 > −16 °C]**, [C_Teile = 10] |
  | immer erfüllt | 1 (unterstrichen) |

- **Aktionen** im Rechteck rechts am Schritt. Mehrere Aktionen stehen nebeneinander oder lückenlos untereinander:

  | Art | im Rechteck | am Rechteck | Wirkung |
  |---|---|---|---|
  | kontinuierlich | -MA1 | – | 1, solange der Schritt aktiv ist |
  | mit Zuweisungsbedingung | -MA1 | Strich oben, daran die Bedingung | 1, solange Schritt aktiv und Bedingung erfüllt |
  | verzögert | -MA1 | Strich oben, daran 5s/X3 | 1 ab 5 s nach Aktivierung, solange der Schritt aktiv ist |
  | zeitbegrenzt | -MA1 | Strich oben, daran 5s/X3 mit Überstrich | 1 in den ersten 5 s nach Aktivierung |
  | speichernd bei Aktivierung | -QA1 := 1 | Pfeil nach oben an der linken Kante | Wert bleibt bis zur nächsten Zuweisung |
  | speichernd bei Deaktivierung | -QA1 := 0 | Pfeil nach unten an der linken Kante | Wert bleibt bis zur nächsten Zuweisung |
  | speichernd bei Ereignis | -QA1 := 1 | Strich oben mit Fähnchen nach links, daran ↑-BG1 | Zuweisung beim Ereignis, solange der Schritt aktiv ist |
  | Zähler | C_Teile := C_Teile + 1 | Pfeil nach oben an der linken Kante | zählt bei jeder Aktivierung |
  | Zwangssteuerung | G5 {INIT} im Doppelrahmen | – | setzt Teil-GRAFCET G5: {INIT} Anfangssituation, { } leer, {3,4,8} diese Schritte, {*} eingefroren |

- **Speichernd wirkende Aktionen** tragen immer beides: die **Zuweisung** mit := im Rechteck und den
  **Auslöser** am Rechteck. „-QA1“ allein ist kontinuierlich. Dieselbe Variable wirkt nie zugleich
  kontinuierlich und speichernd; was mit := 1 gesetzt wird, wird auch mit := 0 zurückgesetzt.
- **Strukturierung**, wenn im Unterricht eingeführt: Makroschritt (Querlinien oben und unten im Quadrat, M4),
  einschließender Schritt (abgeschrägte Ecken) mit Rahmen um die eingeschlossene Kette, oben der Name
  des einschließenden Schritts; der zuerst aktive Schritt darin trägt links ein *. Quelltransition ohne
  Verbindung nach oben, Schlusstransition ohne Verbindung nach unten.
- **Kommentare** in Anführungszeichen: „Zylinder fährt aus“.

**5. GRAFCET in Textform**

Wird ein GRAFCET getippt statt gezeichnet (Erwartungshorizont, PC-Aufgabe), gilt diese Tabelle:

| Schritt | Aktion | Transition zum Folgeschritt |
|---|---|---|
| 0 (Initialschritt) | – | -SJ1 · -BG1 → 1 |
| 1 Füllen | -MA1 | [-BL1 ≥ 80 %] + 30s/X1 → 2 |
| 2 Prüfen | ↑ C_Teile := C_Teile + 1 | [C_Teile < 10] → 1; [C_Teile = 10] → 3 |
| 3 Fertig | -PF1 | ¬-SJ2 → 0 |

- Folgeschritt nach **→**; Alternativen durch **;** getrennt (sie schließen sich gegenseitig aus).
- Mehrere Aktionen durch **;** getrennt. Speichernd **↑ -QA1 := 1**, **↓ -QA1 := 0**, bei Ereignis
  **-QA1 := 1 bei ↑-BG1**; mit Bedingung **-MA1 wenn -BG1**, verzögert **-MA1 verzögert 5s/X3**, zeitbegrenzt
  **-MA1 begrenzt 5s/X3**.
- Parallelverzweigung „→ 3 und 6 (parallel)“; die gemeinsame Transition danach steht bei beiden
  letzten Schritten mit dem Zusatz „(gemeinsam mit X8)“.

**6. Logikplan und Programm**

- **Logikplan (FUP):** Verknüpfungsglieder & (UND), ≥1 (ODER), =1 (XOR), Negation als Kreis am
  Eingang oder Ausgang; Eingänge und Ausgänge mit Kennzeichen beschriftet.
- **Programm** in der im Unterricht verwendeten Sprache:
  - SPS und Kleinsteuerung nach IEC 61131-3: KOP, FUP, ST oder AS (keine AWL). Zeiten mit TON, TOF,
    TP; Zähler mit CTU, CTD; SR setzdominant, RS rücksetzdominant.
  - Mikrocontroller in C/C++ oder Python: Pin-Konstante `PIN_SJ1`, Signalvariable `sj1` (Kennzeichen
    klein, ohne Bindestrich). Zeiten über die Zeit seit Schrittbeginn (z. B. `millis()`), nicht mit
    Warteschleifen; einen GRAFCET als Zustandsautomat mit einer Variablen für den aktiven Schritt.
- **Mikrocontroller-Eingänge:** Signal 1 ist der High-Pegel am Pin. Bei internem Pull-up-Widerstand
  liefert ein betätigter Schließer 0 – die Zuordnungsliste sagt, was 1 bedeutet.
- **Analogwerte:** Der Wertebereich im Programm steht in der Anlage der Ein- und Ausgänge; er hängt
  von Steuerung, Board und Funktion ab (z. B. 4 … 20 mA: Siemens 0 … 27 648, WAGO 0 … 32 760, LOGO!
  200 … 1000, Eaton easyE4 819 … 4095; Arduino Uno 0 … 1023, 12 bit 0 … 4095, MicroPython 0 … 65 535).

## Anhang: references/notenschluessel.md

# Notenschlüssel

Gemeinsame Referenz für Leistungsüberprüfungen.
Quelle: `_gemeinsam/notenschluessel.md`.
Die Tabellen sind identisch mit `eduwerkzeuge.bewertung` (`edu-bewertung schluessel --max N`).

## 15-Punkte-System (Standard: `--system 15`)
| ab % | 95 | 90 | 85 | 80 | 75 | 70 | 65 | 60 | 55 | 50 | 45 | 40 | 33 | 27 | 20 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Punkte | 15 | 14 | 13 | 12 | 11 | 10 | 09 | 08 | 07 | 06 | 05 | 04 | 03 | 02 | 01 | 00 |
| Note | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 5- | 6 |

„Unter ausreichend“ = weniger als 04 Punkte (5+ und schlechter).

## Berufliches Gymnasium (Notenpunkte)
Im BG werden Leistungen in **Notenpunkten 15–00** angegeben; die Prozentgrenzen oben sind die
übliche Umrechnung (05 Punkte ab 45 %) 🔎 mit Fachkonferenzbeschluss und EPA-Hinweisen
abgleichen. Der **Bewertungsmaßstab der Abiturprüfung** (Umrechnung der BE in Notenpunkte)
folgt derselben Prozenttabelle (95 … 45/40/33/27/20 %); ältere Vorlagen nennen 34/28 % für 03/02
Punkte 🔎 mit der geltenden Vorgabe abgleichen.
Unter 05 Punkten gilt ein Kurs als unterpunktet (Unterkurs) – Folgen für die
Gesamtqualifikation nach der geltenden Verordnung 🔎. Die Gewichtung von Klausuren und
sonstigen Leistungen (Projekt, Dokumentation, Präsentation, Mitarbeit) legt die Fachkonferenz
fest 🔎.

## Kammer-Schlüssel (`--system ihk`) 🔎
92 / 81 / 67 / 50 / 30 / 0 % → Note 1 … 6. Vor Verwendung mit der zuständigen Kammer bzw. der
Prüfungsordnung abgleichen.

## Eigene Grenzen
`--grenzen "90:1,80:2,65:3,50:4,25:5,0:6"` (Prozent:Note, Stufe ab 0 % Pflicht) – z. B. nach
Fachkonferenzbeschluss. 🔎 Beschluss der Fachkonferenz bzw. Schulregelung ist maßgeblich.

## Beim Erstellen einer Klassenarbeit
- Punktegrenzen **aus der Gesamtpunktzahl rechnen**, nie aus einer anderen Arbeit abschreiben:
  `edu-bewertung schluessel --max N [--system ihk]`.
  Grenzen werden auf **halbe Punkte aufgerundet**, damit jede Grenze
  erreichbar ist (bei Single Choice auf ganze Punkte).
- Nach jeder Änderung der Gesamtpunktzahl neu rechnen.
- Welcher Schlüssel gilt, entscheidet die Schule (Fachkonferenz, Bildungsgang). Prüfungsnahe
  Arbeiten in dualen Berufen nutzen oft den Kammer-Schlüssel – 🔎 mit der Schulregel abgleichen.

## Rechtlicher Rahmen 🔎
- Notenbildung, Gewichtung schriftlich/mündlich und Genehmigungspflichten (z. B. wenn mehr
  als ein Drittel der Arbeiten unter „ausreichend“ liegt) regeln Erlasse und Schulbeschlüsse.
  
- Die Note setzt die Lehrkraft. Der Notenspiegel ist ein Hilfsmittel auf Grundlage
  freigegebener Punkte (DSGVO Art. 22: keine ausschließlich automatisierte Entscheidung).

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

## Anhang: references/operatoren-epa-technik.md

# Operatoren nach EPA Technik (Abitur Berufliches Gymnasium Technik)

Für Abiturvorschläge gilt diese Zuordnung – sie weicht in einigen Punkten von der allgemeinen
Bibliotheksliste (`operatoren-afb.md`, falls vorhanden) ab (z. B. *begründen* hier AFB II, *dokumentieren* AFB III).
Gilt auch für Klausuren der Qualifikationsphase im BG.
Abgeglichen mit der Operatorenliste des Kultusministeriums für Technik – Mechatronik (Abitur 2024,
Fassung V02): deckungsgleich. *zeichnen* verlangt dort ausdrücklich genormte Symbole, *überprüfen*
steht als „überprüfen und nachweisen“. 🔎 Vor jedem Prüfungsjahr mit der gültigen Fassung abgleichen.

**Gilt für das Fach Technik.** Für das Fach *Berufliche Informatik* hat die EPA eine eigene
Liste, in der u. a. *testen*, *erweitern*, *vervollständigen*, *erstellen*, *implementieren*,
*bezeichnen* und *kennzeichnen* Operatoren sind – siehe Abschnitt *Berufliche Informatik* am Ende.

| AFB I | AFB I/II | AFB II | AFB II/III | AFB III |
|---|---|---|---|---|
| beschreiben, nennen | berechnen, bestimmen, darstellen, erläutern, erklären, vergleichen, zeichnen | ableiten, abschätzen, auswerten, begründen, durchführen, ermitteln, konstruieren, optimieren, skizzieren, strukturieren, ordnen | analysieren, untersuchen, beurteilen, bewerten, Stellung nehmen, dimensionieren, entwickeln, entwerfen, überprüfen, nachweisen, übertragen | dokumentieren |

## Häufige Fehlzuordnungen
| Operator | richtig |
|---|---|
| begründen | nur AFB II – nie AFB I |
| dokumentieren | nur AFB III – nie AFB I oder II |
| skizzieren, ermitteln, ableiten | nur AFB II – nie AFB I |
| analysieren, beurteilen, bewerten, entwickeln, entwerfen, überprüfen | AFB II/III – nie allein AFB I |
| beschreiben, nennen | nur AFB I – nie AFB II oder III |

## Keine EPA-Operatoren (Technik)
*erstellen, kommentieren, implementieren, speichern, reduzieren, programmieren, konfigurieren,
installieren, testen, codieren, notieren, ergänzen, eintragen, ausfüllen, lesen, eingeben,
ausgeben, anpassen, erweitern, umsetzen, aufbauen, validieren, kompilieren, abbilden,
vervollständigen* – zulässig nur, wenn im Lehrermaterial als **erweiterte Operatoren mit
AFB-Zuordnung** dokumentiert („Die Operatorenliste wurde … erweitert").

**Software-, CAD- und Simulationsaufgaben:** Das KMK-Aufgabenbeispiel Ingenieurwissenschaften
(2021) verwendet für Arbeiten am PC auch *vervollständigen, erstellen, anpassen, speichern*
(Baugruppe im CAD-System). Solche Operatoren sind zulässig, wenn das Lehrermaterial sie als
erweiterte Operatoren mit AFB ausweist; die Begutachtung meldet sie dann als ⚠️ Hinweis, nicht
als Mangel. Wo möglich einen EPA-Operator voranstellen (z. B. „Entwickeln Sie … und speichern
Sie …“). Für Programmieraufgaben im BG: *entwickeln*, *entwerfen*, *überprüfen* (EPA) statt
*programmieren*, *implementieren*, *testen*.

Formulierungen ohne Operator: „Geben Sie … an" (→ Nennen/Bestimmen), „Tragen Sie … ein",
„Füllen Sie … aus", „Schreiben Sie …".

## Regeln
- Ein Operator deckt höchstens zwei aufeinanderfolgende AFB ab.
- Operatoren in Schülermaterial und Erwartungshorizont identisch.
- Arbeitsauftrag im Imperativ mit „Sie".
- Im Erwartungshorizont steht der Operator des Auftrags als substantivierter Infinitiv
  (*Berechnen der …*, *Entwickeln eines …*) – so bleiben Auftrag und Bewertung erkennbar gleich.

## Berufliche Informatik (EPA Berufliche Informatik)

Die Operatorenliste der EPA Berufliche Informatik nennt 30 Operatoren mit einem Bereich von
Anforderungsbereichen (1, 1–2, 2, 2–3, 3). Die Liste unten ist die Zuordnung der Bibliothek.
🔎 Mit der gültigen EPA-Fassung abgleichen; Fachkonferenzbeschlüsse haben Vorrang.

| AFB I | AFB I/II | AFB II | AFB II/III | AFB III |
|---|---|---|---|---|
| bezeichnen | anwenden, berechnen, beschreiben, darstellen, erläutern, ermitteln, skizzieren, vervollständigen, zeichnen | begründen, benennen, erstellen, implementieren, kennzeichnen | auswerten, bestimmen, definieren, diskutieren, dokumentieren, einordnen, entwerfen, entwickeln, erweitern, kommentieren, modellieren, testen, übertragen | beurteilen, Stellung nehmen |

- **Nicht in der Liste:** *nennen, angeben, aufzählen, vergleichen, analysieren, untersuchen,
  überprüfen, abschätzen, ableiten, optimieren, konstruieren, programmieren* – zulässig nur als
  im Lehrermaterial dokumentierter erweiterter Operator mit AFB.
- **Formatanweisungen** („Tragen Sie … in die Tabelle ein“, „Kreuzen Sie … an“) stehen **nach**
  einem Operator der Liste („**Vervollständigen** Sie das Struktogramm. Tragen Sie die Einträge
  ① bis ⑤ in die Tabelle ein.“); sie ersetzen ihn nicht.
- Der AFB einer Teilaufgabe liegt im Bereich des Operators und hängt vom Unterricht davor ab
  (*Ermitteln* 1–2: Schleife durchspielen = II; *Bestimmen* 2–3: Wert aus dem Struktogramm
  = II, alle Startwerte rückwärts = III).

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
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen`; Technologieschema mit `technologieschema-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen`; GRAFCET und Funktionsplan mit `technologieschema-erstellen` |
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
| Anlagenbild (Technologieschema), Schaltplanauszug mit Schaltzeichen, GRAFCET, Funktionsplan (FUP), Netzplan | `technologieschema-erstellen` |
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
| 46 | Technologieschema (Schemablatt mit Legende, Specs unter `schema/`, SVG unter `abbildungen/`) | technologieschema-erstellen |
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

**Werkzeug-Skills** (Nr. 42, 46, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-technologieschema`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
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
