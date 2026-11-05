---
artefakt: Abiturvorschlag – Schülermaterial
titel: "[Thema]"
skill: abiturvorschlag-erstellen
skill_version: "1.22"
stand: JJJJ-MM-TT
bildungsgang: "Berufliches Gymnasium Technik"
fach: "Technik"                 # Technik | Berufliche Informatik
schwerpunkt: "[Schwerpunkt]"
pruefungsjahr: "[JJJJ]"
vorschlag: "A"
niveau: eA
bearbeitungszeit: 300
gesamt_be: 120
curriculare_vorgabe: "RRL Technik im Beruflichen Gymnasium – Technik – (Erweiterung 06/2025)"
dqr: 4
vertraulich: true
status: "KI-Entwurf – fachlich zu prüfen"
---

<!-- Formathinweise (nicht Teil des Drucks). abitur_check.py und die regelbasierte Begutachtung
     lesen dieses Format:
     - Aufgaben „## N. Aufgabe – Titel (insgesamt n BE)“, Teilaufgaben „### N.n Titel (n BE)“.
     - Auftragssatz: Operator zuerst, Imperativ „Sie“, ein Operator je Satz, Umfang als Zahlwort,
       Bedingungen statt „ggf.“, Kriterien statt „geeignet“ (references/aufgabenqualitaet.md).
     - Werte mit Einheit; Kennwerte, die die Lösung bestimmen, in einer Anlage; Ersatzwert bei
       abhängigen Teilaufgaben (plausibel, aber nicht das richtige Ergebnis).
     - Steuerungstechnik: Technologieschema mit Text-Legende und Funktionsbeschreibung mit allen
       Betriebsmittelkennzeichen, Kontaktart, Grundstellung, Start und Stopp. Kennbuchstaben nach
       DIN EN IEC 81346-2:2020 immer mit Klasse und Unterklasse (-SJ1, -BG1, -MA1, -MM1, -EA1;
       references/normen-technik.md). Ohne Steuerung beide Abschnitte und
       den Hinweis zur Kennzeichnung löschen und die Ausgangslage unter „Handlungssituation“
       beschreiben.
     - Anlagen „## Anlage N – Titel (zu Aufgabe n)“; jede angekündigte Anlage ist vorhanden.
     - Umfang: bis „B. Material“ höchstens 12 Seiten in der Word-Fassung (abitur_check.py U.1 schätzt,
       abitur_docx.py --seiten zählt); Anlagen kommen dazu. Situationsabsätze kurz, Material, das nicht
       jeder Auftrag braucht, in eine Anlage.
     - Word-Fassung (Dokumentvorlage MK): Kopfzeile jeder Seite „Abitur JJJJ · Technik – Schwerpunkt – ·
       Schülermaterial · Vorschlag A · eA · Bearbeitungszeit: 300 min“, Fußzeile „Schule – Berufliches
       Gymnasium – Technik –, Seite x von n“. -->

| Abitur [JJJJ] | Technik – [Schwerpunkt] – | Schülermaterial |
|---|---|---|
| Vorschlag A | eA | Bearbeitungszeit: 300 min |

## Hinweise

- Insgesamt sind 120 Bewertungseinheiten (BE) erreichbar; die BE stehen bei jeder Aufgabe und
  Teilaufgabe.
- Die Teilaufgaben sind unabhängig voneinander lösbar. Wo ein Ergebnis weiterverwendet wird, ist
  ein Ersatzwert angegeben.
- Die zugelassenen Hilfsmittel stehen in Abschnitt C.
- [Nur bei Steuerungstechnik: Die Betriebsmittel sind nach DIN EN IEC 81346-2:2020 gekennzeichnet.
  Kennzeichen, Zuordnungsliste und GRAFCET folgen der Notation in Anlage [N]. Die Steuerungsaufgaben
  sind mit SPS, Kleinsteuerung oder Mikrocontroller lösbar.]
- [Nur bei PC-Arbeit: Arbeitsplatz und Software mit Version, Ablageort, Dateinamen nach Muster
  „Nachname_A23“ (Aufgabe 2.3), Sichern und Abgabe, kein Netzzugriff.]

| Aufgabe | Inhalt | BE |
|---|---|---:|
| 1 | [Titel] | [40] |
| 2 | [Titel] | [40] |
| 3 | [Titel] | [40] |
| | **Summe** | **120** |

# A. Prüfungsaufgabe

**Thema:** [Thema]

## Handlungssituation

[Drei bis sechs Sätze: Rolle der Prüflinge, fiktiver Betrieb „(fiktiv)“, Projektauftrag. Alle
Aufgaben sind Arbeitsschritte dieses Projekts.]

## Technologieschema

![Abbildung 1](abbildungen/75_abitur_[kurztitel]_A_abb1_technologieschema.svg)

*Abbildung 1: [Titel] – mit `fachdiagramm-erstellen`, in Schwarzweiß lesbar*

| BMK | Betriebsmittel | Lage bzw. Aufgabe |
|---|---|---|
| -SJ1 | [Taster Start] | [Bedienpult] |
| -BG1 | [Näherungsschalter …] | [Position …] |

## Funktionsbeschreibung

**Grundstellung:** [alle Aktoren aus; -BG1 (NC) meldet 0, wenn …]

[Ablauf in Sätzen. Jedes Betriebsmittel mit Kennzeichen; Geber mit Kontaktart (NO/NC) und Bedeutung
des Signals, Aktoren mit Wirkung („-MA1 = 1: …“), Zeiten und Zählwerte als Zahlen.]

**Stopp und Not-Halt:** [Verhalten – oder „Der Not-Halt ist hardwaremäßig gelöst und nicht Teil der
Aufgabe.“]

## 1. Aufgabe – [Titel] (insgesamt [40] BE)

### 1.1 [Titel der Teilaufgabe] ([4] BE)

[Situationsabsatz: neue Information, Werte mit Einheit.]

[Nennen] Sie [zwei …].

[Erläutern] Sie [… für …].

### 1.2 [Titel der Teilaufgabe] ([10] BE)

[ … ]

[Berechnen] Sie [ … ]. Runden Sie auf [zwei Nachkommastellen].

## 2. Aufgabe – [Titel] (insgesamt [40] BE)

### 2.1 [Titel der Teilaufgabe] ([6] BE)

[Ermitteln] Sie [ … ] (Anlage 1).

### 2.2 [Titel der Teilaufgabe] ([12] BE)

[Entwickeln] Sie [einen GRAFCET nach DIN EN 60848 für …]. Verwenden Sie die Kennzeichen der
Funktionsbeschreibung und die Notation in Anlage [N].

## 3. Aufgabe – [Titel] (insgesamt [40] BE)

### 3.1 [Titel der Teilaufgabe] ([8] BE)

[Bestimmen] Sie [ … ]. Rechnen Sie mit [Ersatzwert] weiter, falls Sie [Teilaufgabe] nicht lösen
konnten.

### 3.2 [Titel der Teilaufgabe] ([8] BE)

[Beurteilen] Sie [ … ] anhand der Kriterien [ … ] und [ … ].

# B. Material

## Anlage 1 – [Titel] (zu Aufgabe [2])

[Tabelle oder Datenblattauszug mit Quelle; nur die nötigen Werte.]

## Anlage [N] – Ein- und Ausgänge der Steuerung (zu Aufgabe [2])

<!-- Nur bei Steuerungstechnik. Je Plattform bzw. Board des Unterrichts eine Zeile; beim
     Mikrocontroller Board, Pegel, Bürde und den Wertebereich im Programm nennen (Siemens unipolar
     0 … 27 648, bipolar ±27 648; WAGO 0 … 32 760; LOGO! 4 … 20 mA → 200 … 1000; Eaton easyE4
     4 … 20 mA → 819 … 4095; Uno 0 … 1023; ESP32 mV über analogReadMilliVolts; STM32 und Pico
     12 bit 0 … 4095, MicroPython read_u16 0 … 65 535 – references/normen-technik.md, Abschn. 4).
     WAGO: Adressen nach Modulreihenfolge, Analogmodule zuerst. -->

| Plattform | Digitaleingänge | Digitalausgänge | Analogeingänge (Signal → Wert) |
|---|---|---|---|
| SPS (Siemens) | [%I0.0 … %I0.7] | [%Q0.0 … %Q0.7] | [%IW64: 4 … 20 mA → 0 … 27 648; ±10 V → −27 648 … +27 648] |
| SPS (WAGO PFC200 mit 750-466, 750-430, 750-530) | [%IX4.0 … %IX4.7] | [%QX0.0 … %QX0.7] | [%IW0, %IW1: 4 … 20 mA → 0 … 32 760] |
| Kleinsteuerung (Siemens LOGO!) | [I1 … I8] | [Q1 … Q4] | [AI1: 4 … 20 mA → 200 … 1000] |
| Kleinsteuerung (Eaton easyE4 mit Erweiterungen) | [I1 … I8] | [Q1 … Q4, ab Q17] | [ab IA5: 4 … 20 mA → 819 … 4095] |
| Arduino Uno (5 V) auf E/A-Platine | [D2 … D7] | [D8 … D12] | [A0: 4 … 20 mA über 250 Ω → 1 … 5 V → 205 … 1023] |
| ESP32 (3,3 V) auf E/A-Platine | [GPIO16 … GPIO19] | [GPIO25 … GPIO27] | [GPIO34: 120 Ω → 0,48 … 2,4 V → 480 … 2400 mV] |
| STM32 (3,3 V) auf E/A-Platine | [PB12 … PB15] | [PC6 … PC10] | [PA0: 120 Ω → 0,48 … 2,4 V → 596 … 2978] |
| Raspberry Pi Pico (3,3 V) auf E/A-Platine | [GP2 … GP7] | [GP10 … GP15] | [GP26: 120 Ω → 0,48 … 2,4 V → 596 … 2978 bzw. read_u16 9 532 … 47 662] |

| BMK | Betriebsmittel | Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |
|---|---|---|---|---|---|---|
| -SJ1 | [Taster Start] | [%I0.0] | [I1] | [D2] | [Start betätigt] | NO |

## Anlage [N] – Notation Steuerungstechnik (zu Aufgabe [2])

<!-- Teil „Anlage“ aus references/notation-steuerungstechnik.md einfügen, nicht benötigte Abschnitte
     streichen. Das Wort „Notation“ in der Überschrift behalten (bmk_pruefen.py überspringt die
     Beispiel-Kennzeichen), keine Unterüberschriften. -->

# C. Hilfsmittel

- [Tabellenbuch …, Verlag, Auflage]
- [eingeführter Taschenrechner; Speicher vor Beginn löschen]
- Zeichengerät
