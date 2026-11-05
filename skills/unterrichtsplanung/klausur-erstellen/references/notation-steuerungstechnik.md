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
