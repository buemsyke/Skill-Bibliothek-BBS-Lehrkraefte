# Aufgabenmuster Steuerungstechnik und Mechatronik – die Anlagenaufgabe

Wiederverwendbare Muster für Prüfungs- und Übungsaufgaben, in denen **eine Anlage** (Technologieschema
und Funktionsbeschreibung) alle Teilaufgaben trägt: Steuerungstechnik, Pneumatik, Elektrotechnik,
Mechanik und Sensorik an einem Projekt. Gilt für Abiturvorschläge (Berufliches Gymnasium Technik) und
sinngemäß für Klausuren der Qualifikationsphase und Klassenarbeiten der Fachschule und Berufsschule.
**Herkunft:** Auswertung der zentralen Abituraufgaben Technik – Mechatronik (eA) in Niedersachsen,
Vorbild ist die Aufgabe I des Haupttermins 2025 (Stand 05.11.2026) – in eigenen Worten, keine
Aufgabentexte, Abbildungen oder Datenblätter übernommen, alle Beispiele erfunden. Verbindlich bleiben
Format, Operatorenliste, Kennzeichnung nach DIN EN IEC 81346-2:2020 und Erwartungshorizont mit
Bewertungsmerkmalen (`aufgabenqualitaet.md`, `notation-steuerungstechnik.md`, falls vorhanden).
Die Muster sind Baupläne, keine Texte zum Abschreiben.

## Inhalt
1. Gebrauch
2. Was die Vorbildaufgabe gut macht – Befund
3. Bauprinzipien der Anlage (BA1–BA8)
4. Das Technologieschema als Datenquelle
5. Authentisches Material – Datenblatt, Katalog, Tabellenbuch (DM1–DM6)
6. Aufgabentypen an der Anlage (TA1–TA10)
7. Muster verketten – Aufgabenfluss und Querbezüge
8. Was nicht übernommen wird
9. Kurzprüfung

---

## 1. Gebrauch

- **Erst die Anlage, dann die Aufgaben:** Situation, Schema, Funktionsbeschreibung und Material so
  planen, dass jede Teilaufgabe daraus ihre Angaben bezieht (BA1, Abschn. 4). Danach je Teilaufgabe
  ein Muster aus Abschn. 6 wählen und die Kennung in den Bauplan schreiben (`TA3`, `DM2` …).
- **Aufbau jedes Musters:** *Schablone* (Auftrag mit Platzhaltern ‹…›) · *Festlegen* (was im
  Material stehen muss, damit die Lösung eindeutig ist oder die gleichwertigen Lösungen klar
  umrissen sind) · *Prüfstein* (die eingebaute Denkfalle) · *Merkmale* (beobachtbar, je BE) ·
  *AFB und BE* als Richtwerte nach den zentralen Aufgaben (Teilaufgaben 4–15 BE).
- **Notation:** Kennzeichen nach DIN EN IEC 81346-2:2020 in Kurzform (-S1, -B1, -MA1, -MM1, -P1);
  die zentralen Aufgaben nutzen noch die Ausgabe 2009 (-SF, -BG, -AZ) – die Muster gelten für beide,
  die Beispiele hier stehen in der Ausgabe 2020.

## 2. Was die Vorbildaufgabe gut macht – Befund

| Merkmal | Ausprägung in der Vorbildaufgabe (in eigenen Worten) | Wirkung |
|---|---|---|
| **Eine Anlage trägt alles** | ein Sortier- und Transportsystem mit Bandstrecken, Weiche (Hubzylinder), Bildsensor, Abräumstationen und Rollspeichern; zwei Aufgaben mit sechs bzw. drei Teilaufgaben | Prüflinge arbeiten sich einmal ein; jede Teilaufgabe hat einen Zweck im Projekt |
| **Schema als Datenquelle** | ein Bild mit allen Antrieben, Sensoren, Bedienelementen (als Legendenfeld mit Funktion), Signalleuchte, Zylinder am Gelenk, Rampe in zweiter Stellung gestrichelt, vier Stationen als Kästen | Zuordnungsliste, GRAFCET, Hebelgeometrie, Pneumatikplan, LED-Zahl und Sensorauswahl beziehen sich auf dasselbe Bild |
| **Knappe Funktionsbeschreibung mit echter Steuerungslogik** | Start/Stopp, Weiche nach Prüfergebnis (Alternativverzweigung), Halt an einer Station mit Quittierung durch das Personal, Sperre bei vollem Speicher, Betriebsart *Halt* mit Meldeleuchte, Fortsetzen ohne Neustart | ein GRAFCET mit AFB III aus wenigen Sätzen, ohne Kleinschritt |
| **Umfang begrenzt** | Testbetrieb mit genau einem Werkstück | der Ablauf bleibt in 14 BE beherrschbar, Mehrfachbelegung fällt weg |
| **Zuordnungsliste als Vorlage** | Spaltenkopf mit Operanden für SPS **und** Kleinsteuerung, Kontaktart, zwei ausgefüllte Beispielzeilen (Stopp als Öffner) | Format und Plattform offen, Kontaktart als Denkanstoß |
| **Rechnen am eigenen Bauteil** | Hebel mit Zylinder nahe am Drehpunkt (Kraft und Hub über das Hebelverhältnis), Abscherung einer Radachse mit Sicherheitszahl, Federrate aus Hub je entnommenem Teil | Mechanik ist kein Anhang, sondern Teil der Anlage |
| **Bestand prüfen statt frei wählen** | „im Lager nur ‹Bauform› mit ‹Durchmesser›“ → überprüfen, ob Kraft und Hub reichen, nötigenfalls anpassen und nachweisen | eindeutige Rechnung (AFB II) mit eigener Entscheidung (AFB III) |
| **Befund aus der Erprobung** | Probelauf zeigt eine Störung (harter Anschlag in der Endlage), eine einfache Abhilfe hat nicht gereicht → Bauart wechseln, Wirkung erläutern, Schaltplan entwerfen | Anlass statt Behauptung; die zweite Aufgabe knüpft an die erste an |
| **Echte Unterlagen** | Originalauszug eines Herstellerdatenblatts (zwei Seiten, mit Quelle), Federtabelle aus einem Katalog, Zylindertabelle aus dem Tabellenbuch | Kennwerte entnehmen und deuten wird geprüft, wie im Beruf |
| **Normreihe** | errechneter Vorwiderstand → Wert aus der E24-Reihe festlegen | Rechnung endet in einer realen Bauteilentscheidung |
| **Handlungsergebnisse** | Liste am Ende, je Teilaufgabe ein Ergebnis im Partizip („Druckfedern bestimmt“) | Prüflinge sehen, was abzugeben ist |

Schwächen derselben Aufgabe, die eigene Aufgaben nicht übernehmen: Abschn. 8.

## 3. Bauprinzipien der Anlage

| Nr. | Prinzip | So umgesetzt |
|---|---|---|
| BA1 | **Jede Angabe hat einen Abnehmer** | Bauplan-Spalte *Quelle*: Für jede Teilaufgabe steht fest, aus welchem Bildelement, Satz der Funktionsbeschreibung oder Material sie ihre Angaben bezieht; umgekehrt braucht jedes Element im Schema mindestens eine Teilaufgabe (sonst weglassen) |
| BA2 | **Situation mit Auftrag und Grenze** | Fachkraft in einem fiktiven Betrieb, ein Projekt mit Ziel (automatisieren, umrüsten, erproben) und einer **Begrenzung** des Umfangs („Testbetrieb mit einem Werkstück“, „Not-Halt ist hardwaremäßig gelöst“, „Wartungsbetrieb nicht betrachtet“) |
| BA3 | **Logik in wenigen Sätzen** | die Funktionsbeschreibung enthält die steuerungstechnisch tragenden Elemente als Text, nicht als Schrittliste: Startbedingung, **Verzweigung** nach einem Prüfergebnis, **Warten auf Quittierung** durch eine Person, **Sperre** (Speicher voll, Tür offen), **Betriebsart** (Halt/Einrichten mit Meldeleuchte, Fortsetzen an der Unterbrechungsstelle), Stopp |
| BA4 | **Mehrere Fachgebiete am selben Bauteil** | der Zylinder der Steuerung ist auch der Zylinder der Kraftrechnung und des Pneumatikplans; die Stationen im Bild bestimmen die Zahl der Meldeleuchten; die Sensorpositionen sind die Positionen der Sensorauswahl |
| BA5 | **Vereinfachungen ausdrücklich** | „Masse des Bandes mittig angreifend“, „Zylinder stets senkrecht zum Band“, „Reibung vernachlässigt“ – als eigener Satz oder „Hinweis:“-Zeile, damit die Rechnung eindeutig wird |
| BA6 | **Werte mit Einheit und Herkunft** | Maße, Massen, Druck, Wirkungsgrad, Sicherheitszahl im Text; Werkstoffkennwerte, Normreihen und Bauteildaten im Material (DM1–DM6), nie „aus dem Tabellenbuch“ ohne festen Wert |
| BA7 | **Steigerung über das Projekt** | Einarbeitung (AFB I) → Zuordnungsliste, Ablauf (II/III) → Dimensionieren und Überprüfen (II/III) → Befund aus der Erprobung, Umbau, Auswahl begründen (III) |
| BA8 | **Teilaufgaben entkoppelt** | jede Teilaufgabe ist ohne das Ergebnis der vorigen lösbar (Ersatzwert oder eigene Angabe); Querbezüge über die Anlage, nicht über Zwischenergebnisse – sonst Folgefehlerregel |

## 4. Das Technologieschema als Datenquelle

Das Schema ist in der Anlagenaufgabe kein Titelbild, sondern Material, aus dem gearbeitet wird.
Zeichnen mit dem Zeichen-Skill für Technologieschemata (Spec, SVG, bearbeitbare `.drawio.svg`).

1. **Vollständig für alle Teilaufgaben:** jeder Antrieb, Sensor, Aktor, jedes Bedien- und
   Meldeelement mit Kennzeichen im Bild **und** in der Text-Legende; dazu, was gerechnet oder
   gezählt wird: Drehpunkt und Angriffspunkt eines Hebels, Stationen (Anzahl sichtbar), Speicher
   mit Voll-Sensor.
2. **Geometrie für Rechnungen:** Längen und Abstände, die eine Rechnung braucht, stehen im Text
   der Teilaufgabe (BA6); das Bild zeigt die Lage (Gelenk, Zylinder, Band) und darf Maßpfeile
   tragen – keine Maßstabsmessung im Bild verlangen.
3. **Bewegungsbereich zeigen, nicht den Ablauf:** die zweite Stellung eines schwenkenden Teils
   (gehobene Rampe, ausgefahrene Weiche) als gestrichelter Umriss; Grundstellung durchgezogen und
   in der Fußzeile genannt. Keine Schrittnummern, Pfeile der Reihenfolge oder Signalzustände.
4. **Bedienfeld als eigener Bereich** mit Funktion je Element (Start, Stopp, Halt, Quittieren,
   Meldeleuchte); Farbe nur zusätzlich zum Text, nie allein bedeutungstragend.
5. **Stofffluss lesbar:** Werkstückfluss von links nach rechts, Verzweigung sichtbar (zwei Strecken
   übereinander), Ende jeder Strecke mit Speicher und Sensor.
6. **Umfang:** Eine Prüfungsanlage hat oft 15–25 Elemente. Über etwa 15 Bauteile wird nach
   Bereichen gegliedert (Bedienfeld, Zuführung, Weiche, Strecken, Speicher) oder in zwei Bilder
   geteilt (Anlage, Bedienfeld) – Lesbarkeit im Schwarzweißdruck prüfen.
7. **Begleitbild für die Mechanik:** Für ein Zusatzbauteil (Transportwagen mit Federboden,
   Halterung, Achse) eine eigene schematische Ansicht im Material, die die Wirkungsweise zeigt
   (Federn unter dem Boden, Achse mit Rad) – keine Normzeichnung vortäuschen.

## 5. Authentisches Material – Datenblatt, Katalog, Tabellenbuch

| Nr. | Prinzip | So umgesetzt |
|---|---|---|
| DM1 | **Original statt Abschrift**, wenn das Entnehmen geprüft wird | Datenblatt als Auszug im Original (die Seiten mit Kenndaten und Grenzwerten), Quelle mit Fundstelle; die Prüflinge suchen die nötigen Werte selbst heraus (typisch/maximal, Messbedingung) – das ist Teil der erwarteten Leistung (AFB II). Wird das Entnehmen **nicht** geprüft: nur die nötigen Werte als Tabelle mit Quelle |
| DM2 | **Auszug begrenzen** | höchstens zwei Seiten je Datenblatt; Seiten ohne Bezug weglassen; Lesbarkeit im Druck prüfen (Schriftgröße der Tabellen) – lieber eine Seite in voller Breite als zwei verkleinerte |
| DM3 | **Eindeutig auffindbar** | der benötigte Kennwert kommt im Auszug mit genau einer passenden Messbedingung vor; gibt es typisch und maximal, legt die Teilaufgabe fest, womit gerechnet wird, oder beide Wege sind *Gleichwertig* mit Toleranz |
| DM4 | **Katalogtabelle mit Auswahlregel** | Auswahl aus einer Tabelle (Federn, Zylinder, Motoren, Normreihe) mit Regel: „kleinste ausreichende …“, „nächstgrößerer Normwert“, „mit Reserve ≥ 20 %“; die Tabelle enthält mindestens eine knapp unpassende Zeile (Prüfstein) |
| DM5 | **Bestandsliste als Einschränkung** | „Verfügbar sind nur ‹Bauform› mit ‹Kenngröße›“: die Tabelle zeigt, dass eine Anforderung (Kraft oder Hub) damit nicht erfüllt ist – die Anpassung ist erwartet und hat ein Kriterium (Abschn. 6, TA5) |
| DM6 | **Rechte und Quelle** | Herstellerunterlagen, Katalog- und Tabellenbuchauszüge nur mit Quelle und geklärten Rechten (Begleitblatt); Tabellen aus dem eingeführten Tabellenbuch dürfen alternativ als Verweis auf Tabelle und Seite stehen, wenn alle Prüflinge dieselbe Ausgabe haben |

Im Lehrermaterial: je Datenblattwert die Fundstelle (Seite, Tabelle, Zeile) und der Wert, mit dem
die Musterlösung rechnet.

## 6. Aufgabentypen an der Anlage

**TA1 Anlage erschließen** · AFB I · 3–4 BE
- Schablone: „Nennen Sie die ‹Zahl› Teilsysteme der Anlage.“ – „Beschreiben Sie die Aufgabe jedes
  Teilsystems im Gesamtablauf.“
- Festlegen: Zahl der Teilsysteme oder Gliederungskriterium (Zuführen, Prüfen, Weiche, Abräumen,
  Speichern); ein Operator je Satz.
- Merkmale: je Teilsystem Name (½) und Aufgabe (½) bzw. je Paar 1 BE.

**TA2 Zuordnungsliste aus Schema und Text** · AFB II · 5–6 BE
- Schablone: „Analysieren Sie das Technologieschema (Abbildung N) und die Funktionsbeschreibung.
  Entwickeln Sie die Zuordnungsliste in Anlage N weiter.“
- Festlegen: Vorlage mit Kopf (Kennzeichen | Betriebsmittel | Operand SPS | Operand Kleinsteuerung
  | Signal 1 bedeutet | Kontaktart), zwei ausgefüllte Beispielzeilen, ausreichend Leerzeilen; Zahl
  der Ein- und Ausgänge der Plattform; Regel für die Kontaktart (Stopp und Halt drahtbruchsicher als
  Öffner, Sensoren als Schließer, sofern nicht anders angegeben).
- Prüfstein: ein Betriebsmittel, das nur im Bild steht (Sensor am Speicher, Meldeleuchte), und ein
  Ausgang, der zwei Richtungen braucht (Zylinder doppeltwirkend: zwei Spulen).
- Merkmale: Eingänge vollständig (2), Ausgänge vollständig (2), Kontaktart richtig begründet (1–2).
  *Gleichwertig*: andere Operandenreihenfolge, andere Plattform. Folgefehler: spätere Teilaufgaben
  gelten als richtig, wenn sie zur eigenen Liste passen.

**TA3 Ablauf als GRAFCET entwickeln** · AFB II/III · 12–15 BE
- Schablone: „Entwickeln Sie für den ‹Testbetrieb› einen GRAFCET nach der Funktionsbeschreibung.“
- Festlegen: Umfang (BA2: ein Werkstück, ohne Not-Halt), Kennzeichen aus Zuordnungsliste oder
  Vorgabe, Notationsblatt als Anlage.
- Prüfstein: drei Strukturen, die über eine Kette hinausgehen – **Alternativverzweigung** nach
  einem Prüfsignal mit Zusammenführung, **Warteschritt auf Quittierung** durch eine Person,
  **Betriebsart Halt** (Einfrieren über Zwangssteuerung bzw. einschließenden Schritt, Meldeleuchte
  im Halt) und eine **Sperre** (Speicher voll) in der Startbedingung.
- Merkmale funktional, nie an Schrittnummern: Grundstellung und Start (2), Verzweigung mit
  exklusiven Bedingungen (2), Zusammenführung (1), Quittierung (2), Sperre (1), Halt mit
  Fortsetzen ohne Neustart (2–3), Normform (Initialschritt, Rücksprung, Aktionsarten; 2).
- AFB: Kette und Verzweigung II, Halt und Sperre III.

**TA4 Bauteil am Hebel dimensionieren** · AFB II · 6–8 BE
- Schablone: „Berechnen Sie die Kraft, die ‹Zylinder› am Angriffspunkt aufbringen muss.“ –
  „Berechnen Sie den Hub, den ‹Zylinder› für ‹Höhenunterschied› ausführen muss.“
- Festlegen: Längen (Gesamtlänge, Abstand Angriffspunkt–Drehpunkt), Massen und ihr Angriffspunkt
  (BA5), Zusatzlast (Werkstück am Ende oder in der Mitte), Vereinfachung der Kraftrichtung.
- Prüfstein: Der Angriffspunkt nahe am Drehpunkt vervielfacht die Kraft und verkleinert den Hub
  (Hebelverhältnis wirkt gegenläufig).
- Merkmale: Momentengleichgewicht aufgestellt (2), Kraft (1–2), Hub über Strahlensatz bzw.
  Winkel (2), Einheiten und Rundung (1).

**TA5 Vorhandenes Bauteil überprüfen und anpassen** · AFB II/III · 4–6 BE (oft mit TA4 in einer Teilaufgabe)
- Schablone: „Überprüfen Sie mit Material N, ob ‹vorhandenes Bauteil› ‹Kraft› und ‹Hub›
  erreicht.“ – „Entwickeln Sie eine Anpassung, mit der beide Anforderungen erfüllt sind, und weisen
  Sie sie rechnerisch nach.“
- Festlegen: Bestand (DM5), Systemdruck, Wirkungsgrad bzw. Kraft je Druck aus der Tabelle,
  Fußnoten der Tabelle (Rückstellfeder bei einfachwirkenden Zylindern schon abgezogen?), **mögliche
  Stellgrößen** (Druck, Anlenkpunkt, Bauart, Durchmesser) und das Kriterium der Anpassung.
- Prüfstein: eine Anforderung ist erfüllt, die andere nicht (Kraft reicht, Hub nicht – oder
  umgekehrt); die Anpassung der einen verschiebt die andere.
- Merkmale: Vergleich Kraft (1–2), Vergleich Hub (1), Anpassung mit Nachweis beider Größen (2–3).
  *Gleichwertig*: jede Anpassung, die beide Nachweise besteht und den Bestand berücksichtigt.

**TA6 Festigkeits- oder Federnachweis** · AFB II · 6–8 BE
- Schablone: „Berechnen Sie den erforderlichen Durchmesser ‹der Achse› auf ‹Abscherung› mit
  ‹Sicherheitszahl›.“ · „Bestimmen Sie aus Material N eine Druckfeder, mit der ‹Bauteil› sich je
  ‹entnommenes Teil› um ‹Weg› hebt.“
- Festlegen: Lastfall (Gesamtmasse, Zahl der tragenden Elemente, Zahl der Scherflächen),
  Werkstoffkennwert **im Material** (BA6), Sicherheitszahl, Auswahlregel der Tabelle (DM4).
- Prüfstein: Last auf mehrere Achsen bzw. Federn verteilen; ein- oder zweischnittig; bei der Feder
  die Kraft **eines** Teils je Federweg, geteilt durch die Zahl der Federn.
- Merkmale: Lastannahme (2), Formel und Rechnung (2–3), Auswahl bzw. Normwert nach Regel (1–2).

**TA7 Befund aus der Erprobung beheben** · AFB II/III · 6–8 BE
- Schablone: Befund mit Ursache und gescheiterter Erstmaßnahme schildern (‹Beim Einfahren schlägt
  die Klappe hart an; Puffer aus Gummi haben nicht geholfen.›) → „Erläutern Sie, wie ‹andere
  Bauart› die Störung behebt.“ – „Entwerfen Sie den ‹pneumatischen› Schaltplan für ‹Zylinder›.“
- Festlegen: Kennzeichen des Bauteils, Vorgaben zum Plan (Ventilart, Ansteuerung, Notation),
  Schaltplanvorlage oder freies Blatt.
- Prüfstein: die Wirkung entsteht nicht durch die neue Bauart allein, sondern durch das, was sie
  ermöglicht (Abluftdrosselung, Endlagendämpfung, Gegendruck in beide Richtungen).
- Merkmale: Ursache und Wirkprinzip (2), Plan funktionsfähig (2–3), Drossel richtig eingebaut und
  gerichtet (1–2), Normform und Kennzeichen (1).

**TA8 Anzeige- oder Anpassschaltung mit Datenblatt** · AFB II · 5–6 BE
- Schablone: „Zeichnen Sie die Schaltung für ‹Zahl› Meldeleuchten an ‹Kontakten› mit ‹Spannung›.“ –
  „Berechnen Sie mit Material N den Vorwiderstand.“ – „Bestimmen Sie einen Widerstand aus der
  ‹E-Reihe›.“
- Festlegen: Zahl der Leuchten aus dem Schema (BA4), Versorgungsspannung, Kontaktart der Geber,
  Datenblatt im Original (DM1), Regel für den Normwert (nächstgrößer, damit der Strom nicht
  überschritten wird), Normreihe als Material oder Verweis.
- Prüfstein: richtiger Datenblattwert (Durchlassspannung bei der Messbedingung, Dauerstrom statt
  Spitzenstrom); Abrunden auf den Normwert überschreitet den Strom; Verlustleistung des Widerstands.
- Merkmale: Schaltung (2), Werte aus dem Datenblatt mit Fundstelle (1), Rechnung (1–2),
  Normwert nach Regel (1). *Gleichwertig*: andere Messbedingung mit Begründung.

**TA9 Sensoren auswählen und begründen** · AFB II/III · 4–6 BE
- Schablone: „Bestimmen Sie für die Positionen ‹-B1 bis -B8› je einen Sensortyp.“ – „Begründen Sie
  jede Wahl mit ‹Werkstoff, Abstand, Umgebung› aus der Anlagenbeschreibung.“
- Festlegen: Zahl der Positionen und je Position, was erfasst wird (Werkstoff, Abstand,
  Verschmutzung, Durchlicht möglich?); Kriterien als Liste. **Kein** „mindestens drei“: die Zahl
  der verschiedenen Typen folgt aus den Positionen oder wird genau genannt.
- Prüfstein: eine Position, an der der naheliegende Typ versagt (Kunststoff vor induktivem Sensor,
  transparentes Teil vor Einweglichtschranke).
- Merkmale: je Position Typ passend (½–1) und Begründung mit Bezug auf das Kriterium (½–1).

**TA10 Fremde Entscheidung überprüfen** · AFB III · 3–5 BE
- Schablone: „‹Ein Kollege› hat für ‹Aufgabe› ‹Bauteil› vorgesehen. Überprüfen Sie die Auswahl mit
  Material N und nehmen Sie Stellung.“
- Festlegen: Kriterien und Daten, an denen geprüft wird.
- Prüfstein: die Auswahl erfüllt das offensichtliche Kriterium und scheitert an einem zweiten
  (Hub, Temperatur, Schutzart, Strom).
- Merkmale: Nachweis je Kriterium (1–2), Urteil (1), Alternative mit Nachweis (1–2).

## 7. Muster verketten – Aufgabenfluss und Querbezüge

| Aufgabe | Kette (Kennungen) | Querbezug über die Anlage |
|---|---|---|
| 1 (≈ 45–50 BE) | TA1 → TA2 → TA3 → TA4/TA5 → TA6 (ein oder zwei Bauteile) | Zylinder aus TA3 ist Gegenstand von TA4/TA5; Wagen bzw. Halterung aus dem Material |
| 2 (≈ 20–25 BE) | TA7 → TA8 → TA9 bzw. TA10 | TA7 greift die Bauart aus TA5 auf (Befund der Erprobung), TA8 zählt die Stationen im Schema, TA9 nutzt die Sensorpositionen |

Am Ende des Schülermaterials: **Handlungsergebnisse** (je Teilaufgabe ein Ergebnis, gleich
lautend mit der Zeile im Erwartungshorizont), **Material** (M1 … Mn, je mit Titel, Bezug zur
Teilaufgabe und Quelle), **Hilfsmittel** (Tabellenbuch des Bereichs, eingeführter Taschenrechner).

## 8. Was nicht übernommen wird

- **Wortlaut, Szenario, Abbildungen und Datenblätter** der Vorbildaufgabe – nur die Muster.
- **Kennzeichen der Ausgabe 2009**, wenn der Unterricht die Ausgabe 2020 nutzt; nie mischen.
- **Schwächen** der Vorbildaufgabe (Befunde in den Begutachtungskriterien):
  - zwei Operatoren in einem Satz („Nennen … und erläutern …“) – zwei Sätze, zwei Merkmale;
  - Operatoren außerhalb der Liste (*erstellen*, *benennen*) – *entwickeln*, *nennen*;
  - offene Mengen und Wertungen ohne Kriterium („mindestens drei“, „geeignete“, „passende“) –
    Zahlwort und Kriterienliste;
  - „gegebenenfalls Anpassungen vornehmen“ – sagen, ob eine Anpassung erwartet ist und woran sie
    gemessen wird (TA5);
  - Werkstoffkennwert nur „aus dem Tabellenbuch“ – Wert ins Material (BA6);
  - Kennzeichen nur im Bild oder nur im Lehrermaterial, Geber ohne Kontaktart – Legende und
    Funktionsbeschreibung vollständig (`aufgabenqualitaet.md` Abschn. 4, falls vorhanden);
  - Erwartungshorizont mit Sammelzeilen ohne Merkmale („Entwickeln eines GRAFCET“ 14 BE) –
    Merkmale je BE wie in TA3;
  - Datenblattseiten verkleinert bis an die Lesbarkeitsgrenze (DM2).

## 9. Kurzprüfung

- [ ] Eine Anlage trägt alle Teilaufgaben; Bauplan-Spalte *Quelle* je Teilaufgabe gefüllt (BA1)?
- [ ] Funktionsbeschreibung mit Verzweigung, Quittierung, Sperre bzw. Betriebsart – und einer Grenze des Umfangs (BA2, BA3)?
- [ ] Schema vollständig für alle Teilaufgaben, Bewegungsbereich gestrichelt, keine Ablaufhinweise (Abschn. 4)?
- [ ] Rechengrößen mit Einheit, Vereinfachungen als eigener Satz, Kennwerte im Material (BA5, BA6)?
- [ ] Datenblatt im Original nur dort, wo das Entnehmen geprüft wird; Kennwert eindeutig auffindbar; Quelle und Rechte (DM1–DM3, DM6)?
- [ ] Auswahl aus Tabellen mit Regel; Bestandsprüfung mit erwarteter Anpassung und Kriterium (DM4, DM5, TA5)?
- [ ] Je Teilaufgabe Muster-Kennung, Prüfstein und funktionale Merkmale; ein Operator je Satz?
- [ ] Handlungsergebnisse und Erwartungshorizont gleich lautend; Teilaufgaben ohne Vorergebnis lösbar (BA8)?
