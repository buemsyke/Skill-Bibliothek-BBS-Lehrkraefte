# Abituraufgaben Informationstechnik aus einem anderen Land – Vergleichsbeispiele

Auswertung von Abiturprüfungen des Beruflichen Gymnasiums eines anderen Landes (2018/19 bis 2023/24),
in eigenen Worten, Stand 31.10.2026. Grundlage ist die OCR-Textfassung in `quellen/it-vergleich/`
(Inventar und Zuordnung zu den Scans: `quellen/it-vergleich/README.md`). Es sind keine Aufgabentexte
übernommen; Themen, Punktzahlen und Operatoren sind ausgezählt. OCR-Unsicherheiten sind mit 🔎
markiert. **Einordnung:** Das Vergleichsland prüft zentral und nach eigenen Vorgaben – die Hefte taugen als
**Ideen- und Musterquelle** für das Profil Informationstechnik, nicht als Formatvorlage; das
niedersächsische Format bleibt verbindlich (`references/abitur-aufgabenformat.md`).
**Wiederverwendbare Muster** (Aufgabentypen, Fragestellungen als Schablonen, Bauprinzipien,
Prüfsteine) stehen seit 01.11.2026 im geteilten Katalog
`references/aufgabenmuster-informationstechnik.md`; Abschn. 8 hier nennt die Fundstellen je Muster.

## Inhalt
1. Quellenlage
2. Prüfungsformate im Vergleichsland
3. Themenfelder und typische Aufgabenarten
4. Operatoren im Vergleich
5. Lösungshefte
6. Entwicklung 2018/19 → 2023/24
7. Was der Skill übernehmen kann – und was nicht
8. Muster und Fundstellen

---

## 1. Quellenlage

| Bestand | Art |
|---|---|
| Aufgabenhefte 2018/19, 2019/20, 2021/22 | altes Format (6 Aufgaben, 300 min) |
| Aufgabenheft 2019/20, Variante 240 min | gleiche Prüfung, gekürzt |
| Aufgabenheft 2023/24 | neues Format (2 Pflicht- + 2 Wahlaufgaben) |
| Musterlösungen 2018/19, 2019/20, 2020/21, 2023/24 | reine Lösungshefte ohne Punkteschema |

Die Deckblätter der Scans nennen teils „Angewandte Informatik", teils „Informationstechnik";
die Kopfzeilen im Text nennen kein Fach 🔎. Inhaltlich decken die Hefte das Spektrum des
niedersächsischen Profils Informationstechnik ab (Steuerungstechnik/Mikrocontroller, Software,
Netzwerke, Datenbanken).

## 2. Prüfungsformate im Vergleichsland

**Altes Format (bis 2021/22):**
- Teil 1 und 2 Pflichtbereich (Aufgaben 1–4), Teil 3 Wahlbereich (Aufgaben 5–6).
- Jede Aufgabe trägt die volle Punktzahl 30 (Summenspalte „Punkte" am Seitenrand).
- Aufgabe 1 und 2: hardwarenahe Informationsverarbeitung, jeweils zweigleisig –
  *informationslogische Lösung* (Schaltnetz/Schaltwerk) **und** *Mikrocontroller-Lösung*
  (Programm in Assembler oder C nach Wahl, 8051-Familie, 1 µs Maschinenzyklus).
- Aufgabe 3 und 4: Software (OOP/UML, Algorithmen) in je einem Anwendungskontext.
- Aufgabe 5 und 6 (Wahl): Systeme – Netzwerke, Betriebssysteme, Datenbanken mit SQL.
- Die 240-min-Variante 2019/20 enthält denselben Pflichtbereich; der Umfang im hinteren
  Heftteil ist reduziert 🔎 (genaue Auswahlregel in der OCR nicht belegt).

**Neues Format (2023/24):**
- Pflichtbereich: Aufgabe 1 hardwarenah (Schwenktor-Steuerung mit Mikrocontroller),
  Aufgabe 2 objektorientierter Entwurf (Kursstufen-App).
- Wahlbereich: Aufgabe 3 vernetzte Systeme/IoT (Pflanzenzucht mit MQTT), Aufgabe 4
  KI und Datenbanken (k-Means, Normalisierung).
- Nur noch C/C++ auf Arduino-/MBED-artiger Plattform; Schaltnetz/Schaltwerk in klassischer
  Notation entfällt, Zustandsdiagramme in UML.

**Gemeinsam:** Ein Szenario je Aufgabe (Anlage, Gerät, App), dazu Blockdiagramm bzw.
Beschreibung; Teilaufgaben im Schema N.N.N mit Punktzahl rechts; Arbeitsblätter zum
Ergänzen (Klassendiagramm-Rohlinge, Zustandstabellen, Impulsdiagramme).

## 3. Themenfelder und typische Aufgabenarten

**Hardwarenah (Aufgabe 1–2 alt, Aufgabe 1 neu):**
- Schaltwerk-Entwurf klassisch: Zustandsübergangsdiagramm (mit Ausgangscode) → codierte
  Zustandstabelle → Funktionstabelle/Funktionsgleichung des Ausgangsschaltnetzes.
- Schaltnetz: Komparator (4-Bit-Vergleicher), Multiplexer, Zähler (CTR DIV n) analysieren.
- Mikrocontroller: Port-Zuordnung wählen, Initialisierung, Hauptprogramm als PAP oder
  Struktogramm, Interrupt-Service-Routinen (externe Interrupts, Timer), Wartezeit-Unterprogramme,
  PWM (Tastgrad, Periodendauer), ADC-Werterfassung, I²C (Adressen aus A0–A2, Port-Extender),
  UART (Paritätsbit), Schrittmotor-Impulsmuster, Servo-Ansteuerung über Pulsweite.
- Kleine Rechnungen: Periodendauer aus Frequenz, Tastendruckdauer, Timer-Vorlade-/Prescaler-Werte,
  Winkel pro Raste eines Drehimpulsgebers.

**Software (Aufgabe 3–4 alt, Aufgabe 2 neu):**
- Aus **Sequenzdiagrammen** auf das Klassendiagramm schließen: Operationen mit Signatur und
  Sichtbarkeit ergänzen, Assoziationen mit Multiplizität und Rollennamen, temporäre Assoziationen.
- OOP-Konzepte: abstrakte Klasse/Operation, Klassenvariable (unterstrichen), Constraint in
  geschweiften Klammern, dynamische Polymorphie, Konstruktor-Überladung – jeweils kurz erklären
  oder anwenden.
- Algorithmus als Struktogramm/PAP/Pseudocode zu einer fachlichen Regel (Notendurchschnitt,
  Mahnstaffel, 100-Punkte-Regel, Suche in Objektstruktur).
- Objektdiagramm mit konkreten Attributwerten zu einem Szenario; UML-Zustandsdiagramm
  (Analysesicht) zu einem Bearbeitungsstatus.
- Datenstruktur: verkettete Liste (Knoten, Anhängen als Algorithmus).

**Systeme/Netzwerke (Wahl):**
- Verkabelungsentscheidung mit Entfernungen begründen (Kupfer/Glasfaser/Funk).
- Subnetting: gegebenes Netz in n Subnetze aufteilen, Tabelle mit Netzadresse, Maske,
  Hostbereich, Broadcast; Routingtabelle; IPv4→IPv6-Migration, Link-Local-Adressen.
- WLAN 2,4 vs. 5 GHz, Access-Point-Dimensionierung; Netzwerkschutz (Firewall, DMZ).
- IoT/MQTT: Topic-Struktur entwerfen, QoS-Stufen begründet zuordnen, Broker-Zugang, Last Will.
- Betriebssysteme (virtuelle Adressierung) und Dateisysteme (ältere Hefte).

**Datenbanken (Wahl):** ERM → Relationen mit Primär-/Fremdschlüsseln, Normalformen,
SQL-Abfragen mit Verbund, Aggregat und Gruppierung.

**KI (neu, 2023/24):** überwachtes vs. unüberwachtes Lernen unterscheiden, Distanzmaße
(Manhattan, euklidisch) an zwei Merkmalen rechnen, Wirkung der Skalierung beurteilen,
k-Means-Iteration nachvollziehen und einordnen.

**Punktzahlen je Teilaufgabe:** überwiegend 1–8, Implementierungen und Sequenzdiagramme bis 8;
innerhalb einer Aufgabe steigt die Anforderung von Analyse/Reproduktion zu Entwurf und Begründung.

## 4. Operatoren im Vergleich

In den Vergleichsheften verwendet (mit Beispielverwendung, eigene Worte), abgeglichen mit beiden
EPA-Listen der Bibliothek (`references/operatoren-epa-technik.md`; AFB in Klammern):

| Operator (Vergleichshefte) | typische Verwendung | EPA Technik | EPA Berufliche Informatik |
|---|---|---|---|
| entwerfen | Zustandsdiagramm, Funktionstabelle, Konzept | ✓ (II/III) | ✓ (2–3) |
| entwickeln | Algorithmus, ISR, Sequenzdiagramm, Programmteil | ✓ (II/III) | ✓ (2–3) |
| bestimmen | Speicheranzahl, Codierung, Multiplizitäten, Parität | ✓ (I/II) | ✓ (2–3) |
| berechnen | Periodendauer, Zeiten, Distanzen, Punktregel | ✓ (I/II) | ✓ (1–2) |
| beschreiben | Funktionsweise, Optimierung, Schutzmaßnahme | ✓ (I) | ✓ (1–2) |
| begründen | Plattform-/QoS-/Designentscheidung | ✓ (II) | ✓ (2) |
| ermitteln | Bitkombinationen, Adressen, Teilnetze | ✓ (II) | ✓ (1–2) |
| zeichnen, skizzieren | Schaltung, Impulsdiagramm, Prozessabfolge | ✓ | ✓ |
| erläutern | Gültigkeitsbereich, Notwendigkeit zweier Adressen | ✓ (I/II) | ✓ (1–2) |
| „Stellen Sie … dar“ (*darstellen*) | Signaturen im Diagramm, Algorithmus, Relationen | ✓ (I/II) | ✓ (1–2) |
| beurteilen | Vorschlag eines Mitarbeiters, Deadlock | ✓ (II/III) | ✓ (3) |
| analysieren | Zustand nach Tastendruck, Sequenzdiagramm | ✓ (II/III) | – → ermitteln |
| erklären | Prinzip (Überladung, abstrakte Klasse) | ✓ (I/II) | – → erläutern |
| ableiten | Zustandstabelle, Objektdiagramm aus Beschreibung | ✓ (II) | – → entwickeln |
| nennen | Bedeutung einer Notation, Vor- und Nachteile | ✓ (I) | – → bezeichnen, benennen |
| vergleichen | Timer mit und ohne Interrupt | ✓ (I/II) | – → diskutieren |
| bewerten | Praxistauglichkeit eines Vorschlags | ✓ (II/III) | – → beurteilen |
| optimieren | Netzeinteilung | ✓ (II) | – → entwickeln |
| ergänzen | Klassendiagramm, Zustandsdiagramm auf Arbeitsblatt | – → entwickeln … weiter | – → vervollständigen, erweitern |
| erstellen | Routingtabelle, SQL-Abfrage, Objektdiagramm | – → entwickeln | ✓ (2) |
| wählen, schreiben, unterscheiden | Verkabelung, Programmsequenz, Sicherungsverfahren | – | – |
| Frage („Was bedeutet …?“, „Hat sie recht?“) | Konzeptfrage, Behauptung prüfen | – → nennen, beurteilen | – → bezeichnen, beurteilen |

**Korrektur 01.11.2026:** Die erste Fassung führte *erklären*, *ableiten* und „stellen Sie dar“
als Nicht-EPA-Operatoren und *ergänzen* als EPA-Operator – im Fach Technik ist es umgekehrt. Für
niedersächsische Vorschläge werden Formulierungen der Vergleichshefte je Fach gegen die Liste umgesetzt; die
Schablonen im Katalog nutzen Operatoren beider Listen (`references/aufgabenmuster-informationstechnik.md`,
Abschn. 2).

## 5. Lösungshefte

- **Reine Musterlösungen** je Teilaufgabe im selben N.N.N-Schema: erwartete Antwort als Text,
  Tabelle, Diagramm (in der OCR nur rudimentär) oder vollständiger Code – **ohne Punkteschema,
  ohne Bewertungsbogen, ohne AFB-Verteilung, ohne Notenschlüssel**.
- **Parallele Lösungswege sind System:** Assembler **und** C, PAP **und** Struktogramm,
  später Arduino **und** MBED; Pin- und Plattformwahl ausdrücklich frei („andere Pins möglich").
- **Variantenhinweise** am Rand: „nicht unbedingt erforderlich, weil …", „auch … genügt",
  alternative Multiplizitäten mit Begründung – die Lösung begründet, welche Abweichungen
  gleichwertig sind.
- **Folge für den Skill:** Die Lösungshefte des Vergleichslands liefern gute **Musterlösungs-Inhalte**, aber keinen
  Erwartungshorizont. BE, AFB-Verteilung, Bewertungsmerkmale und der Satz zu gleichwertigen
  Lösungswegen müssen für NDS immer selbst gebaut werden
  (`references/abitur-aufgabenformat.md`, Abschn. 10; `references/aufgabenqualitaet.md`).

## 6. Entwicklung 2018/19 → 2023/24

- **Plattformwechsel:** 8051 mit Assembler-Option und konkreten Registern → abstrakte
  Arduino-/MBED-Umgebung, nur noch C/C++, dafür moderne Peripherie (ADC, PWM, I²C, UART,
  Bluetooth) und UML-Zustandsdiagramme statt klassischer Schaltwerk-Notation.
- **Themenwechsel im Wahlbereich:** Betriebssysteme/Dateisysteme und klassisches SQL →
  IoT (MQTT, QoS), IPv6, WLAN-Dimensionierung, KI-Grundlagen (k-Means, Distanzmaße).
- **Kontexte bleiben anwendungsnah:** Sortier-/Trocknungsanlage, Jalousie, Blutdruckmessgerät,
  Schwenktor, Oberstufen-Apps, Pflanzenzucht – ein durchgehendes Szenario je Aufgabe.
- **Stabil:** 30 Punkte je Aufgabe (alt), Teilaufgaben 1–8 Punkte, Arbeitsblätter zum Ergänzen,
  Doppelstrategie informationslogisch/Mikrocontroller (alt), freie Notationswahl (PAP **oder**
  Struktogramm, Assembler **oder** C).

## 7. Was der Skill übernehmen kann – und was nicht

**Geeignet als Musterquelle:**
1. **Aufgabenideen und Szenarien** für alle Felder des Profils Informationstechnik
   (Abschn. 3), inklusive der neuen Themen IoT/MQTT und KI-Grundlagen, die in den
   niedersächsischen Vorbildern noch fehlen.
2. **Aufgabenfluss-Muster:** Anlage erschließen → Zustandsmodell → Tabelle/Gleichung →
   Programmteil (Init, Hauptprogramm, ISR) → begründete Entscheidung; bzw. Software:
   Sequenzdiagramm analysieren → Klassendiagramm ergänzen → Konzeptfrage → Algorithmus →
   Objektdiagramm. Passt zum steigenden AFB innerhalb einer Aufgabe
   (`references/abitur-aufgabenformat.md`, Abschn. 10, Regel 5).
3. **Antwortvorlagen-Praxis:** Arbeitsblätter mit Rohlingen (Klassendiagramm ohne Operationen,
   leere Zustandstabelle, Impulsdiagramm-Gerüst, Subnetting-Tabelle) – entspricht Regel 3
   des Skills und liefert konkrete Vorlagenideen.
4. **Gleichwertigkeits-Praxis:** parallele Lösungswege und Variantenhinweise als Vorbild für
   die Zeile *Gleichwertig* im Erwartungshorizont (Regel 16).
5. **Kleinteilige Punktierung** (1–8 Punkte) wie im niedersächsischen Informatik-Abitur –
   gut für Software- und Datenbankteilaufgaben.

**Nicht übernehmbar (Landesvorgaben NDS bleiben verbindlich):**
1. Kein Erwartungshorizont mit BE/AFB – muss immer ergänzt werden (Abschn. 5).
2. Operatoren je Fach gegen die EPA-Liste umsetzen (Abschn. 4): im Fach Technik *ergänzen*,
   *erstellen*, *wählen*, *schreiben* und Fragen ersetzen; in Berufliche Informatik zusätzlich
   *nennen*, *erklären*, *ableiten*, *analysieren*, *vergleichen*, *bewerten*.
3. Formatvorgaben (dezentraler Vorschlag A/B, Schüler-/Lehrermaterial, Handlungsergebnisse,
   Bewertungsmaßstab) aus `references/abitur-aufgabenformat.md` und
   `references/abitur-konstruktion.md` – nicht aus den Vergleichsheften.
4. Inhalte an die niedersächsischen Lerngebiete des Profils binden
   (`references/berufliches-gymnasium.md`, `references/curriculum-abgleich.md`); z. B. ist die
   8051-/Assembler-Tiefe der älteren Hefte 🔎 gegen die RRL-Lerngebiete zu prüfen, ebenso
   UML-Vielfalt (Sequenz-/Objektdiagramm) und KI-Inhalte.
**Übernahme (Entscheidung 31.10.2026):** Übernommen in `abitur-aufgabenformat.md` (Regeln 3, 5,
16 und Folgerung 6) und `abitur-konstruktion.md` (Abschn. 3) wurden: die Aufgabenfluss-Muster,
Antwortvorlagen-Rohlinge, neuere Szenario-Themen (IoT/MQTT, KI-Grundlagen) und die
Gleichwertigkeits-Praxis als Offenheit der Lösungswege. **Nicht** übernommen: die veralteten
Aufgabenideen (Registerebene, Assembler, Betriebssysteme, SQL/Datenbanken); kleinteilige
Punktierung (1–8 BE) nur, wo jede Teilleistung ein eigenes beobachtbares Ergebnis hat.
**Ergänzung 01.11.2026:** Aufgabentypen, Fragestellungen und Bauprinzipien aller Hefte als
geteilter Katalog `references/aufgabenmuster-informationstechnik.md` (B1–B14, F1–F10, H1–H10,
S1–S10, N1–N10, K1–K5, D1–D2) – auch für Klausuren, Programmieraufgaben und die Begutachtung.
Datenbankmuster gelten dort für Klassenarbeiten und Berufliche Informatik; für Abiturvorschläge im
Schwerpunkt Informationstechnik bleibt es bei der Entscheidung oben.

## 8. Muster und Fundstellen

Wo die Muster des Katalogs in den Heften vorkommen (Jahr, Teilaufgabe; L = nur im Lösungsheft
belegt) – zum Nachprüfen am Original, nicht zum Übernehmen von Texten.

| Muster | Fundstellen |
|---|---|
| F1 von Hand rechnen, dann Algorithmus | 18/19 3.2.1→3.2.2, 4.4.1→4.4.2; 23/24 2.1.3.1→2.1.3.2 |
| F2 Aussage beurteilen | 23/24 4.1.2.1 c, 4.1.2.2 |
| F3 Vorschlag eines Kollegen | 18/19 1.1.6; 23/24 3.1.2; 20/21 4.2.3 (L) |
| F4 Zustand durchspielen | 23/24 1.1.1 |
| F5 Realisierung begründen/vergleichen | 19/20 2.2.7; 21/22 2.1.5 |
| F6 Auswirkung einer Entscheidung | 21/22 4.5.1; 23/24 3.2.4 b |
| F7 Erweiterung beschreiben | 18/19 2.2.3; 21/22 1.2.5 |
| F8 Störung beheben | 19/20 1.1.5 |
| F9/S9 Begriff am Fall | 18/19 3.1.1, 4.3.1, 4.3.2, 4.3.4; 19/20 4.1.1–4.1.3; 21/22 3.2.1, 3.2.3, 3.2.4, 4.2.1–4.2.3 |
| F10/N5 rückwärts | 19/20 6.1.1 a |
| H1 Ausnahmezustand | 23/24 1.1.2 |
| H2 Zustandsautomat im Programm | 23/24 1.3.1–1.3.2 |
| H3 Initialisierung | 18/19 1.2.1, 2.2.1.1; 19/20 1.2.2.1, 2.2.4; 21/22 1.2.3, 2.2.2; 23/24 1.2.3 |
| H4 Timer einstellen | 23/24 1.4.1 |
| H5 ISR | 19/20 2.2.6; 21/22 1.2.4, 2.2.4–2.2.5; 23/24 1.4.2 |
| H6 Impulsdiagramm | 23/24 1.2.2 |
| H7 Wertebereich, Begrenzung | 21/22 2.2.1, 2.2.3 |
| H8 Bus-Adressierung | 23/24 1.6.1–1.6.4 |
| H9 Kurzaufgaben | 19/20 1.1.3, 1.1.6.2, 2.1.1; 21/22 2.1.2; 23/24 1.5.1 |
| H10 protokollieren, deuten | 21/22 1.1.5, 2.1.1 |
| S1 Klassendiagramm aus Sequenzdiagramm | 18/19 3.1.3–3.1.4, 4.1.1–4.1.2; 19/20 3.1, 4.2.1; 21/22 3.1.1–3.1.3, 4.1.1–4.1.2; 23/24 2.1.1.1 |
| S2 Multiplizität, Einschränkung | 18/19 3.1.2; 23/24 2.1.1.2–2.1.1.3 |
| S3 Sequenzdiagramm weiterentwickeln | 18/19 3.4, 4.2; 19/20 3.5, 4.2.3; 21/22 3.3, 4.3; 23/24 2.1.2 |
| S4 Struktogramm aus Sequenzdiagramm | 19/20 4.2.2; 21/22 3.4.1 |
| S5 Algorithmus zur Fachregel | 18/19 3.2.2, 4.4.2; 19/20 3.2, 4.2.4; 21/22 3.4.2, 4.4; 23/24 2.1.3.2, 2.2.2, 4.1.3, 4.1.4 |
| S6 Objektdiagramm | 19/20 3.3; 21/22 4.5.2; 23/24 2.1.4 |
| S7 Zustandsdiagramm aus Text | 18/19 3.3 (Designsicht), 4.5; 19/20 3.4 |
| S8 Klasse instanziierbar | 18/19 4.3.3; 19/20 4.1.2; 21/22 3.2.2 |
| S10 Datenstruktur | 23/24 2.2.1 |
| N1 Übertragungsmedium | 18/19 5.1.1; 23/24 3.1.1 |
| N2 Vorschlag am Adressbedarf | 23/24 3.1.2 |
| N3 Subnetting | 18/19 6.1.4; 19/20 5.1.1, 6.1.1 b; 21/22 5.1.1; 23/24 3.1.3 |
| N4 Routingtabelle | 18/19 5.1.3, 6.1.3; 19/20 5.1.1 d; 21/22 6.1.3; 23/24 3.1.5 |
| N6 Adressen auf dem Weg | 18/19 6.1.2; 21/22 5.1.2 |
| N7 Eigenschaften mit Zahlwort | 23/24 3.1.4, 3.1.6, 3.2.2 |
| N8 Topic-Struktur | 23/24 3.2.3 |
| N9 Dienstgüte | 23/24 3.2.4–3.2.5 |
| N10 Schutzmaßnahme | 23/24 3.1.7 |
| K1–K5 KI-Grundlagen | 23/24 4.1.1, 4.1.2.1, 4.1.2.2, 4.1.3, 4.1.4 |
| D1 ER-Modell | 18/19 5.2.1, 6.2.1; 19/20 5.2.1, 6.2.1; 21/22 5.2.1, 6.2.1; 23/24 4.2.1 |
| D2 SQL mit festgelegter Ausgabe | 18/19 5.2.2, 6.2.2; 19/20 5.2.2, 6.2.2; 21/22 5.2.2, 6.2.2; 23/24 4.2.2 |