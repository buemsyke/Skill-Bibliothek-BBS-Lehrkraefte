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
