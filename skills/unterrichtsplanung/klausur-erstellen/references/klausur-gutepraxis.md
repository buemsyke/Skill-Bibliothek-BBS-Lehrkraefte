# Gute Praxis für Klassenarbeiten und Lernzielkontrollen

Zusammengeführt aus der Skill-Fassung `klausur-erstellen` 1.x (eduwerkzeuge), der Referenz
*Leistungsüberprüfungen* der `lernfeld-werkstatt`, den Prüfkriterien der Begutachtung
und einer gelungenen Papierklausur aus der Praxis (Details in
`druckfassung-antwortformate.md`). Erfahrungswerte aus realen Reihen sind als solche gekennzeichnet.

## Inhalt
1. Wo Leistungsüberprüfungen liegen
2. Zeitauslegung – die wichtigste Zahl
2a. PC-Klausuren (Abgabe als Datei)
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
| Klausur im BG (auch Einführungsphase) | ≥ 2,0 min/P bzw. BE | 90 min / 45 BE |
| **PC-Klausur** (jede Art, Abgabe als Datei) | ≥ 2,0 min/P **und** ≤ rund 10 Teilaufgaben je 60 min | 60 min / 30 P in 10 Teilaufgaben |
| Lernzielkontrolle (Single Choice) | ≈ 1 min je Frage | 25 Fragen in 20–25 min |

> **Erfahrungswert (lernfeld-werkstatt):** Eine erste Fassung mit 16 Aufgaben, 60 Punkten und
> 60 Minuten ging rechnerisch auf und war trotzdem unbearbeitbar – alle vier Minuten ein
> Kontextwechsel. Halbiert auf 8 Aufgaben und 40 Punkte bei gleicher AFB-Gewichtung und
> Abdeckung; kein Pflichtinhalt ging verloren (mehrere wanderten in Richtig/Falsch-Aussagen).

> **Erfahrungswert (PC-Klausur Textverarbeitung und Zahlensysteme, BG Einführungsphase,
> 11/2026):** 40 P in 60 min, 6 Aufgaben mit 19 Teilaufgaben, Rechenwege in Tabellenzellen der
> Word-Vorlage tippen, erste PC-Klausur der Klasse. Takt (1,5 min/P), Minutensumme (53 von 60 min),
> AFB 30/48/22 – alles im Soll. Ergebnis bei 26 Arbeiten: im Mittel 29 % der Punkte, 23 unter
> „ausreichend“, ab der dritten Umrechnung blieb rund die Hälfte der Felder leer, die letzte Aufgabe
> erreichte 9 %. Der geschätzte Probelauf der Lehrkraft (25 min) hätte mit der Faustregel unten
> schon 62–75 min ergeben. Zeit war aber nicht die einzige Ursache: Auch ohne die letzte Aufgabe
> lagen 21 von 26 unter „ausreichend“; die Hex-Umrechnung dezimal → hex löste niemand, weil das
> Material sie über Kommadivision lehrt und kein Taschenrechner erlaubt war (Abschn. 2a).

- Minutenangaben je Aufgabe im Erwartungshorizont führen; ihre Summe bleibt **unter** der
  Bearbeitungszeit (Reserve für Austeilen, Lesen, Kontrolle).
- **Faustregel: Probelösung durch die Lehrkraft × 2,5 bis 3 ≈ Zeitbedarf der Lernenden** – gemessen
  mit Stoppuhr, nicht geschätzt, und als „Probelauf: N min“ in den Erwartungshorizont;
  `klausur_check.py` rechnet × 2,5 (Papier) bzw. × 3 (PC) gegen die Bearbeitungszeit. Diese Zahl
  schlägt den Takt: Geht der Takt auf, der Probelauf aber nicht, ist die Arbeit zu lang.
- Höchstens rund 10 Hauptaufgaben. Was zusammengehört, zusammenlegen (z. B. Rechnung in die
  Auswahlaufgabe), Doppelungen streichen (zweite Beurteilungsaufgabe).

## 2a. PC-Klausuren (Abgabe als Datei)

Am PC kostet jede Teilaufgabe einen **Bedienwechsel** (Dialog suchen, Stelle finden, Zelle
anklicken, Sonderzeichen tippen) – unabhängig von ihren Punkten. Der Punkttakt allein unterschätzt
das, besonders bei Klassen, die langsam tippen oder zum ersten Mal am PC geprüft werden.

| Regel | Umsetzung |
|---|---|
| **Teilaufgaben zählen** | ≤ rund 10 je 60 min (höchstens 12); `klausur_check.py --pc` – erkennt „PC-gestützt“ auch im Kopf |
| **Takt** | ≥ 2,0 min/P (wie Klausur im BG) |
| **Probelauf in der Prüfsoftware** | Lehrkraft löst die Vorlage in genau der Software der Prüfung mit Stoppuhr; × 3, erste PC-Klausur der Klasse × 3–4 |
| **Rechenwege nicht tippen lassen** | Rechenwege auf Papier (Schmierblatt mit Namen abgeben) und nur Ergebnisse in die Datei – oder höchstens 3–4 getippte Rechenwege; Tippen von Hochzahlen, Indizes und Malpunkten prüft sonst das Schreibtempo |
| **Vorlage ohne Fallen** | vorbereitete Strukturen (Abschnittsumbrüche, Formatvorlagen, Felder) nicht zur unbeabsichtigten Hürde machen: „auf das gesamte Dokument“ ausdrücklich nennen; was nicht geprüft wird, in der Vorlage fertig |
| **Ein Werkzeug je Teilaufgabe** | nicht Rechnen und Bedienen in einem Feld mischen; Teilaufgaben, die ungeübte Funktionen erst entdecken lassen (AFB III „erweitern“), höchstens zwei |
| **Probeabgabe** | vor Beginn speichern, umbenennen, abgeben – zählt nicht zur Bearbeitungszeit |
| **Lösbarkeit** | jede Aufgabe in der Prüfsoftware nachweislich lösbar (eine Funktion, die in der Erstellungssoftware anders wirkt, nicht stellen) |
| **Verfahren und Hilfsmittel** | sind Rechner, Internet oder Tabellenkalkulation gesperrt, muss das Verfahren aus dem Material ohne sie gehen (z. B. Division mit ganzzahligem Rest statt Kommadivision) |

Vor der ersten PC-Klausur: einmal eine Übungsarbeit unter Zeit in derselben Vorlage-Art; die
Lehrkraft misst dabei, wie lange die Klasse für eine Teilaufgabe braucht, und plant mit diesem Wert.

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
- Aufgaben-IDs (A1.1 …) und Aspekte eindeutig schreiben, damit Korrekturhilfen sie übernehmen können.

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
| Takt geht auf, Probelauf geschätzt („ca. 25 min“) | Probelauf mit Stoppuhr messen, × 2,5 bzw. × 3 (PC) gegen die Bearbeitungszeit |
| PC-Klausur nach Punkten getaktet, 19 Teilaufgaben in 60 min | ≤ rund 10 Teilaufgaben je 60 min, Rechenwege auf Papier |
| Material lehrt Kommadivision, Klausur verbietet den Taschenrechner | Verfahren mit den erlaubten Hilfsmitteln üben oder Hilfsmittel erlauben |
| Falle in der Darstellung („1100 1000₂“ mit Leerzeichen, Vorlage mit Abschnitten bei „Seitenränder einstellen“) | Denkfalle im Verfahren, Darstellung wie im Unterricht, Vorlage für AFB I ohne Hürde |
| Jede Teilaufgabe „mit Falle“ in der ersten Arbeit einer Klasse | Fallen dosiert in AFB II/III, AFB I sichert Punkte |
| Qualitätscheck meldet ✅, obwohl das Skript den Wert nicht gerechnet hat | ✅ nur aus der Skriptausgabe; „Bearbeitungszeit nicht erkannt“ = ungeprüft |
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
