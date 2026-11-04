# Abiturvorschlag bauen – Konstruktionsregeln

Ergänzt `abitur-aufgabenformat.md` (wie Aufgaben aussehen) und `aufgabenqualitaet.md` (eindeutig
formulieren und bewerten). Maßstab der Genehmigung ist der Katalog
`pruefkriterien-abitur-bg-technik.md`; die Nummern in Klammern verweisen darauf.

## Inhalt
1. Rahmen und Standardwerte
2. Bauplan
3. Aufgabenfluss und Bausteine je Schwerpunkt
4. AFB je Zeile zuteilen
5. Unterrichtliche Voraussetzungen konkret schreiben
6. Vorschlag A und B
7. PC-, CAD-, SPS- und Programmieraufgaben
8. Fach Berufliche Informatik
9. Material, Quellen, Abbildungen
10. Erwartungshorizont und Musterlösung
11. Katalog → Bauregel

---

## 1. Rahmen und Standardwerte

| Größe | Standard (sonst Annahme) | Grenze |
|---|---|---|
| Niveau, Zeit | eA, 300 min | gA 🔎 Vorgabe |
| Bewertungseinheiten | 120 BE | 2,5–3,0 min/BE; vertretbar 2,0–3,5 (4.3) |
| Aufgaben | 3 × 40 BE | 2–4 Aufgaben, je 30–60 BE |
| Teilaufgaben | 4–7 je Aufgabe, 3–15 BE | 2–20 BE |
| AFB gesamt | 36/48/36 BE (30/40/30 %) | Ziel ±5, Grenze ±10 Prozentpunkte (4.6) |
| AFB je Aufgabe | ≈ 12/16/12 bei 40 BE | jeder AFB > 0 |
| Lerngebiete | beide verbindlichen + das gewählte optionale (3.2) | jede Aufgabe ≥ 2 Lerngebiete (X.14) |

- Nichts aus einem **nicht gewählten** optionalen Lerngebiet; das schulisch bestimmte Lerngebiet
  (13.2) nur, wenn es unterrichtet ist und die Vorgaben es zulassen 🔎.
- **Neu, nicht geübt:** Die konkrete Aufgabe ist im Unterricht nicht in dieser Form vorgekommen;
  Notation, Software und Verfahren sind vertraut.
- **Eine Handlungssituation** für den ganzen Vorschlag (3.3): fiktiver Betrieb „(fiktiv)“, Rolle als
  Fachkraft bzw. angehende Ingenieurin/angehender Ingenieur, ein Projektauftrag; jede Aufgabe ist ein
  Arbeitsschritt dieses Projekts (3.4). Übergeordnete Kompetenzen der RRL (3.1) gezielt ansprechen,
  z. B. Lösungsvarianten vergleichen, Modell und Geltungsbereich, Technikfolgen beurteilen.

## 2. Bauplan

Erst die Tabelle, dann die Texte. Je Vorschlag:

| Teilaufg. | Gegenstand | Operator(en) | I | II | III | BE | Min. | Lerngebiet | Unterrichtsbezug | Material |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|

- Summen je Aufgabe und gesamt **rechnen** (AFB, BE, Minuten = BE × Takt); Minutensumme ≤ Zeit.
- Je Teilaufgabe festlegen: welche Angaben sie braucht (Werte, Anlage), welches Antwortformat,
  welche Merkmale die BE tragen (`aufgabenqualitaet.md`, Abschn. 5).
- Erst wenn der Bauplan alle Soll-Werte erfüllt, Schülermaterial schreiben.

## 3. Aufgabenfluss und Bausteine je Schwerpunkt

Innerhalb jeder Aufgabe: **Einstieg AFB I** (Einarbeitung: nennen, beschreiben; 3–6 BE) → **Kern
AFB II** (berechnen, ermitteln, entwickeln mit Vorgaben) → **Abschluss AFB III** (überprüfen,
beurteilen, optimieren mit vorgegebenen Kriterien). Die erste Teilaufgabe des Vorschlags ist nie
AFB III (X.1). Regeln aus den Abiturprüfungen 2023–2026 für Informationstechnik (Aufbau, Schweregrad,
Formulierungen, Erwartungshorizont): `references/abitur-aufgabenformat.md`, Abschn. 10.

| Schwerpunkt | typische Bausteine (Beispiele, Auswahl nach Unterricht) |
|---|---|
| Informationstechnik | Netzwerk: Adressplan bestimmen, Fehler ermitteln, Konzept entwerfen, Sicherheit beurteilen · Steuerung: Zuordnungsliste, GRAFCET bzw. Programm entwickeln, Sensor anbinden, fremde Bauteilauswahl überprüfen · Software: Klassendiagramm erläutern, Struktogramm bzw. Operation entwickeln, Ablauf dokumentieren, Fehler an markierten Stellen korrigieren, Testfälle · Daten: Redundanz zeigen → Schema begründen → SQL entwerfen → gegebenes SQL analysieren; Messwerte auswerten |
| Elektrotechnik | Netzwerk berechnen, Schutzmaßnahme überprüfen, Steuerung entwickeln, Antrieb bzw. Regelung dimensionieren |
| Metalltechnik | Bauteil dimensionieren, Fertigung und Prüfung planen, Prozess automatisieren, CNC-Programm analysieren |
| Bautechnik | Tragwerk berechnen, bauphysikalischen Nachweis führen, Konstruktion entwerfen |
| Ingenieurwissenschaften | drei Disziplinen (Bau, Maschinenbau, Elektro) an einem Projekt; Software (Tabellenkalkulation, CAD, SPS) als Hilfsmittel |
| Gestaltungs- und Medientechnik | Produktionsablauf planen, Druck- bzw. AV-Produkt analysieren und entwerfen, Qualität prüfen 🔎 |
| Berufliche Informatik | Modellieren (Klassen-, Zustandsdiagramm), Algorithmus entwickeln und testen, Datenbankabfragen, Netz und Protokoll |

**Aufgabenfluss-Muster für Informationstechnik** (bewährt in den Vergleichsheften,
`references/abitur-aufgabenformat-vergleich.md`; deren veraltete Bausteine – Registerebene, Assembler,
Betriebssysteme, SQL/Datenbanken – werden nicht übernommen). Je Teilaufgabe ein Muster mit
Schablone, Festlegungen, Prüfstein und Merkmalen: `references/aufgabenmuster-informationstechnik.md`
(Kennung in den Bauplan, Ketten in Abschn. 10 dort):

- **Steuerung/Mikrocontroller:** Anlage erschließen → Zustandsmodell (UML-Zustandsdiagramm)
  analysieren bzw. ergänzen → Programmteil entwickeln (Initialisierung, Hauptprogramm,
  Interrupt/Timer, PWM/ADC, Bussystem) → Entscheidung begründen (z. B. Parameterwahl).
- **Software:** Sequenzdiagramm analysieren → Klassendiagramm ergänzen (Operationen, Multiplizitäten)
  → Konzeptfrage (z. B. Polymorphie) → Algorithmus zu einer fachlichen Regel → Objektdiagramm mit
  konkreten Werten.
- **Netzwerk/IoT:** Infrastruktur entscheiden (Medium, Entfernung) → Adressplan bzw. Subnetze
  in Tabelle → Protokoll entwerfen (Topic-Struktur, Dienstgüte begründen) → Schutzmaßnahme
  beurteilen.
- **Szenario-Themen auch neuere Felder:** vernetzte Sensorik/Aktorik (IoT, MQTT) und KI-Grundlagen
  (Lernarten unterscheiden, Distanzmaß rechnen, Verfahrensschritt nachvollziehen und einordnen) –
  immer am Lerngebiet des Unterrichts ausgerichtet.

## 4. AFB je Zeile zuteilen

- Der AFB einer Zeile liegt im **Bereich des Operators** (`operatoren-epa-technik.md`): *nennen*,
  *beschreiben* nur I; *begründen*, *ermitteln*, *skizzieren* nur II; *dokumentieren* nur III;
  *entwickeln*, *entwerfen*, *beurteilen* II oder III.
- Innerhalb des Bereichs entscheidet der **Unterricht**: Routine (im Unterricht oft geübt) → unterer
  Wert; Übertragung auf Neues, eigene Entscheidung → oberer Wert.
- Eine Zeile höchstens **zwei benachbarte AFB** (z. B. *Entwickeln eines GRAFCET*: II 8, III 4).
- Weicht die Zuteilung vom Bereich ab (Routineverfahren als AFB I), steht die Begründung im
  Lehrermaterial unter **Abweichende AFB-Zuordnungen** (X.5).

## 5. Unterrichtliche Voraussetzungen konkret schreiben (2.3)

Halbjahresthema allein reicht nicht. Je Aufgabe: Kurshalbjahr und Lerngebiet, behandelte Inhalte,
Tätigkeiten der Lernenden, Software/Geräte/Notation, und was an der Prüfungsaufgabe neu ist.

| zu knapp | konkret (erfundenes Beispiel) |
|---|---|
| „Aufgabe 2 bezieht sich auf IT1 (12.2).“ | „Aufgabe 2 (IT1, 12.2; IT4, 13.1): Die Lernenden haben Ablaufsteuerungen für zwei Anlagen als GRAFCET entwickelt und auf einer Kleinsteuerung in Betrieb genommen, Zuordnungslisten mit Kontaktart erstellt und analoge Sensoren (4 … 20 mA) linear umgerechnet. Neu ist die Anlage (Bewässerung) und die Kombination aus Füllstand- und Zeitbedingungen; Tröpfchenbewässerung war nicht Thema.“ |

## 6. Vorschlag A und B

| gleich | verschieden |
|---|---|
| Bearbeitungszeit, Gesamt-BE, Hilfsmittel | Handlungssituation und Thema |
| Lerngebiete und ihre Anteile | Anlage, Gegenstände, Zahlenwerte |
| AFB-Profil (Abstand je AFB ≤ 5 Punkte Ziel, ≤ 10 Grenze) | konkrete Aufgaben – keine Aufgabe in beiden |
| Schwierigkeit (Zahl der Teilaufgaben, Schreib- und Zeichenaufwand) | |

Prüfen: `abitur_check.py SM_A LM_A --vergleich SM_B LM_B`.

## 7. PC-, CAD-, SPS- und Programmieraufgaben

- **Deckblatt:** Ausstattung (Betriebssystem, Software mit Version), Ablageort, Dateinamen nach
  Muster (z. B. `Nachname_A23`), Sichern und Abgabe, kein Netzzugriff – keine Platzhalter wie
  „Version X.Y“ (S.1).
- **Digitales Material** im Lehrermaterial als Tabelle Datei | Zweck | zu Aufgabe; alle Dateien
  liegen den Prüfungsunterlagen bei (S.3, X.12).
- **Operator:** EPA-Operator voranstellen („Entwickeln Sie … und speichern Sie … unter …“);
  praktische Operatoren (*erstellen, speichern, anpassen, vervollständigen*) als erweiterte
  Operatoren mit AFB dokumentieren (X.2).
- **Ausfall:** Was gilt bei Software- oder Geräteausfall? 🔎 Regel der Schule bzw. Behörde.
- **Musterlösung** als Datei und als Ausdruck bzw. Auszug im Lehrermaterial; Merkmale prüfen das
  Ergebnis (Verhalten, Ausgabe), nicht eine bestimmte Codezeile.
- **Plattformneutral:** Steuerungsaufgaben sind mit SPS, Kleinsteuerung **oder Mikrocontroller**
  lösbar. Funktion als GRAFCET bzw. Logikplan; Analogwerte im GRAFCET als physikalische Größe;
  Zuordnungsliste mit je einer Spalte „Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller“
  und einer Anlage mit den Ein- und Ausgängen je Plattform (beim Mikrocontroller Board, Pegel,
  E/A-Platine, Analogbereich); Schaltplanvorlage je Plattform zur Wahl; Programm „in der im
  Unterricht verwendeten Sprache“. Rohwerte (Bereiche je Plattform: `normen-technik.md`, Abschn. 4,
  in der Anlage `notation-steuerungstechnik.md`) nur rechnen lassen, wenn
  die Plattform feststeht – sonst Stromstärke oder Spannung. Die Musterlösung zeigt eine Plattform,
  *Gleichwertig* nennt die anderen (`references/normen-technik.md`, Abschn. 4).
- **Notation** nach `references/notation-steuerungstechnik.md`; der Teil „Anlage“ geht ins
  Schülermaterial.

## 8. Fach Berufliche Informatik

- Operatorenliste der **EPA Berufliche Informatik** (`operatoren-epa-technik.md`, letzter
  Abschnitt): *testen, implementieren, erweitern, vervollständigen, bezeichnen, kennzeichnen* sind
  Operatoren; *nennen, analysieren, vergleichen* nicht.
- Formatanweisungen („Tragen Sie … in die Tabelle ein“) nur **nach** einem Operator.
- Notation wie im Unterricht (Struktogramm, Pseudocode, UML, SQL) und **als Anlage festlegen**,
  welche Sprachelemente bzw. Operationen zulässig sind – Vorbild ist der Notationsrahmen der
  Ergänzenden Hinweise Informatik (`references/normen-technik.md`, Abschn. 9; Signaturen, Index 0,
  Klassendiagramm, Struktogramm, SQL-Umfang). Gilt ebenso für Software- und Datenbankteile im
  Schwerpunkt Informationstechnik 🔎 Hilfsmittelregel der Behörde.
- Testfälle mit Eingabe und erwarteter Ausgabe vorgeben oder als Merkmal verlangen; Code-Merkmale
  funktional („liefert für leere Liste 0“), nicht als Textvergleich.

## 9. Material, Quellen, Abbildungen

- Datenblatt- und Tabellenauszüge mit **Quelle**, nur die nötigen Werte; Kennwerte, die die Lösung
  bestimmen, in die Anlage (statt „aus dem Tabellenbuch“).
- Fiktive Betriebe und Personen erkennbar „(fiktiv)“; keine echten Kontaktdaten.
- Abbildungen mit `fachdiagramm-erstellen` (Aufgaben- und Lösungsbild getrennt), Schwarzweiß
  lesbar, mit Text-Legende; jede angekündigte Anlage ist vorhanden (S.2).
- Anlagen nummeriert „Anlage N – Titel (zu Aufgabe n)“; Abbildungen mit Nummer und Titel.
- **Neues im Material erschließen:** Was nicht unterrichtet wurde (neue Anlage, Datenstruktur,
  Protokoll), steht als Definition, Beispiel und vorgeführter Ablauf in einer Anlage; die Aufgabe
  prüft die Übertragung bekannter Verfahren darauf.
- **Antwortvorlagen** (Tabellen mit Kopf und Beispielzeile, Schaltplan-, Netzplan-, Schema- und
  Dokumentationsvorlagen) mit Namensfeld, wo die Form der Antwort nicht geprüft wird.

## 10. Erwartungshorizont und Musterlösung

- **Erwartungshorizont:** eine Zeile je Operator der Teilaufgabe, substantiviert und gleich lautend
  wie im Auftrag (*Berechnen der …*) **und** wie in der Überschrift der Musterlösung – nicht „Nennen“
  im Erwartungshorizont und „Benennen“ in der Lösung (X.4, X.8); BE nach AFB; Σ in der ersten Zeile der
  Teilaufgabe; Summenzeilen „Summen N. Aufgabe“ und „Gesamtsummen (absolut)“ mit allen vier Zahlen
  (auch 0), dazu „Gesamtsummen (prozentual)“.
- **Bewertungsmaßstab:** Prozent | Notenpunkte | ab BE – gerechnet (`abitur_check.py`).
- **Hinweise zur Bewertung:** allgemeine Regeln (Folgefehler einmal, Rundung, Einheiten,
  gleichwertige Lösungen).
- **Musterlösung:** je Teilaufgabe „Lösungsvorschlag zur Teilaufgabe N.n“ – vollständiger
  Lösungsgang mit Zwischenergebnissen und Einheiten, **mit Code nachgerechnet**; darunter
  Merkmaltabelle und die Zeilen *Gleichwertig*, *Folgefehler*, *Toleranz*, *0 BE*.

## 11. Katalog → Bauregel

| Kennung | Bauregel | Nachweis |
|---|---|---|
| 1.3, X.6 | Kopf mit Jahr, Fach, Schwerpunkt, Vorschlag, eA, Bearbeitungszeit | Kopf SM/LM |
| 2.1 | Vorschläge A und B gleichwertig | `--vergleich` |
| 2.2, 2.3 | Kursfolge-Tabelle, Bezug je Aufgabe konkret | LM, Unterrichtliche Voraussetzungen |
| 2.4, X.8 | Erwartungshorizont mit AFB je Zeile, operatorbezogen | LM, Erwartungshorizont |
| 2.5 | Lösungsvorschlag je Teilaufgabe | LM, Musterlösung |
| 2.6 | Bewertungsmaßstab gerechnet | LM, Bewertungsmaßstab |
| 2.7, 2.8 | Hilfsmittel benannt, Formelsammlung beigefügt | SM, Hilfsmittel |
| 3.1–3.5 | Handlungssituation, Handlungskompetenz, übergeordnete Kompetenzen, alle AFB | Bauplan |
| 4.1 | eindeutige Aufträge; BMK einheitlich | `aufgabenqualitaet.md`, `bmk_pruefen.py` |
| 4.2 | unabhängig oder Ersatzwert | Bauplan, *Folgefehler* |
| 4.3, X.7 | Takt 2,5–3,0 min/BE | Skript |
| 4.4, 4.5, X.2, X.9 | EPA-Operator im Imperativ „Sie“, Erweiterungen dokumentiert | Skript |
| 4.6, X.1, X.5 | AFB-Verteilung, Einstieg, Zeilen-AFB im Bereich | Skript |
| 4.7, X.3, X.10, X.13 | BE überall, „BE“ statt „Punkte“, Summen SM = LM | Skript |
| X.4 | Operatoren in SM und Erwartungshorizont gleich | Skript |
| X.11 | keine Tippfehler, keine Wiederholungen | Korrekturlesen |
| X.12, S.3 | digitales Material beigelegt | LM, Digitales Material |
| X.14 | ≥ 2 Lerngebiete je Aufgabe | Bezug je Aufgabe |
| S.1, S.2, S.4 | keine Platzhalter, Anlagen vorhanden, Nummerierung lückenlos | Skript |
