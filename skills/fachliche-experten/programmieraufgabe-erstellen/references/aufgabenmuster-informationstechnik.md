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
