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
  Kennzeichen dieser Klasse (nicht -BG1 neben -BGB2). `bmk_pruefen.py` (T.8)
  meldet fehlende Unterklassen und gemischte Tiefe.
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
