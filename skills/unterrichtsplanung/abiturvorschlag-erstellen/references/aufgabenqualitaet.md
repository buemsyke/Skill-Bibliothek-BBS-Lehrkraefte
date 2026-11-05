# Aufgabenqualität – eindeutig formulieren, eindeutig bewerten

**Grundsatz:** Eine Zweitkorrektur kommt zum selben Ergebnis. Dafür gilt zweierlei:
1. Alles, was die Lösung bestimmt, steht im Schülermaterial – Werte, Regeln, Bezeichnungen, Umfang.
2. Jede BE hängt an einem **beobachtbaren Bewertungsmerkmal** im **Bewertungsraster** – einem eigenen
   Dokument neben dem Lehrermaterial (`…_A_bewertungsraster.md`). Schüler- und Lehrermaterial bleiben so
   knapp wie möglich, damit Begutachtung und Fachgruppe wenig zu prüfen haben.

Die Kennungen K.1–K.10, U.1–U.2 und T.1–T.9 prüft das Skript (`abitur_check.py`, `bmk_pruefen.py`);
Abschnitt 9 fasst sie zusammen. Die Beispiele sind erfunden.

## Inhalt
1. Der Auftragssatz
2. Angaben, die die Lösung festlegen
3. Antwortformat vorgeben
4. Steuerungstechnik – Betriebsmittelkennzeichen
5. Bewertungsmerkmale
6. Regeln je Teilaufgabe
7. Bewertungsbogen und Gutachten
8. Korrekturprobe
9. Kennungen und Prüfregeln
10. Umfang

---

## 1. Der Auftragssatz (K.7)

- **Operator zuerst**, im Imperativ „Sie“, aus der EPA-Liste des Fachs.
- **Ein Operator je Satz.** Zwei Leistungen = zwei Sätze (dann auch zwei Zeilen im Erwartungshorizont).
- **Umfang als Zahlwort** („zwei Vorteile“, „drei Sensortypen“, „alle Teilsysteme“) – nie
  „mindestens“, nie eine Mehrzahl ohne Zahl.
- **Bedingungen ausformulieren** („Falls … , dann …“) statt „ggf.“ oder „gegebenenfalls“.
- **Kriterien nennen** statt „geeignet“, „sinnvoll“, „angemessen“: woran wird gemessen?
- Keine W-Fragen als Auftrag; keine Wörter wie „kurz“, „möglichst“, „usw.“, „evtl.“.
- Auftragssatz höchstens rund 45 Wörter; Vorgaben als Liste davor.

| statt | besser |
|---|---|
| Nennen Sie Vorteile einer Ringtopologie. | Nennen Sie zwei Vorteile der Ringtopologie für die Sensorstationen. |
| Nennen Sie mindestens drei geeignete Sensoren. | Nennen Sie drei Sensortypen für -BG3. Begründen Sie die Eignung je Sensortyp mit einem Kriterium aus Anlage 2. |
| Passen Sie ggf. den Entwurf an. | Bestimmen Sie den erforderlichen Systemdruck, falls die Kolbenkraft nicht ausreicht. |
| Wählen Sie einen geeigneten Vorwiderstand. | Bestimmen Sie den Vorwiderstand als nächstgrößeren Wert der E12-Reihe. |
| Erläutern und beurteilen Sie das Verfahren. | Erläutern Sie das Verfahren. Beurteilen Sie es anhand der Kriterien Kosten und Ausfallsicherheit. |
| Wie arbeitet der Paketfilter? | Beschreiben Sie die Arbeitsweise des Paketfilters an einem Datenpaket aus Anlage 3. |
| Beschreiben Sie kurz den Ablauf. | Beschreiben Sie den Ablauf in der Reihenfolge der Schritte. |

## 2. Angaben, die die Lösung festlegen (K.4)

- **Werte mit Einheit**, Vereinfachungen ausdrücklich („vereinfacht als Einzellast in Feldmitte“),
  Konstanten, Sicherheitszahl, Wirkungsgrad.
- **Kennwerte aus einer Anlage**, nicht aus „dem Tabellenbuch“ – Tabellenbücher unterscheiden sich.
  Kommt ein Wert doch aus dem eingeführten Tabellenbuch, steht der benutzte Wert im
  Erwartungshorizont mit Quelle und Toleranz für andere Ausgaben.
- **Auswahlregeln** („nächstgrößerer Normwert“, „kleinster Durchmesser, der … erfüllt“).
- **Genauigkeit:** Rundung im Auftrag („auf zwei Nachkommastellen“) oder Toleranz im
  Erwartungshorizont (z. B. ±2 % bzw. ±1 in der letzten Stelle).
- **Ersatzwert** für abhängige Teilaufgaben: plausibel, aber nicht das richtige Ergebnis (verrät
  sonst die vorige Teilaufgabe); der Erwartungshorizont rechnet beide Wege (K.6).

## 3. Antwortformat vorgeben

- Tabellen: Kopfzeile und ein bis zwei **Beispielzeilen** vorgeben (Zuordnungsliste, Adressplan).
- Vorlagen zum Ergänzen als Anlage („Anlage 3 – Vorlage Anschlussplan“), in Schwarzweiß lesbar.
- Ergebnisform nennen: „Ergebnis mit Einheit“, „Entscheidung (ja/nein) mit Begründung“,
  „normgerechter GRAFCET“, „Struktogramm“ – jeweils in der Notation des Unterrichts.
- Bei Beurteilungen Zahl und Art der Kriterien vorgeben („anhand von zwei Kriterien aus …“).

## 4. Steuerungstechnik – Betriebsmittelkennzeichen und Notation (T.1–T.9)

**Kennzeichnung** nach **DIN EN IEC 81346-2:2020** (IEC 81346-2:2019): Bindestrich, Kennbuchstaben,
Zählnummer – **immer Klasse und Unterklasse** (Standard der Fachberatung, 04.11.2026), in
Funktionsbeschreibung, Technologieschema, Zuordnungsliste, Aufgaben und Musterlösung gleich:
- -SJ Taster/Schalter; -BG Lage, -BL Füllstand, -BP Druck, -BM Feuchte, -BT Temperatur; -KE SPS,
  -KF Relais; -QA Schütz, -QM Wegeventil; -MA Motor, -MB Ventilspule, -MM Zylinder; -PF Leuchtmelder,
  -PJ Hupe; -EA Leuchte; -RN Drossel(rückschlag)ventil, -RM Rückschlagventil.
- Die Klasse allein (-S1, -M1) wird nicht verwendet – auch nicht, wenn eine Klasse nur eine Art
  Betriebsmittel enthält.
- Beispiel: -SJ1, -SJ2, -QA1, -KE1, -PF1, -PF2, -BL1, -BM1, -BT1, -MA1, -MB1, -MB2.
Tabellen mit Gegenüberstellung zur Ausgabe 2009: `references/normen-technik.md`, Abschn. 2.

Die zentralen Mechatronik-Prüfungen 2020–2026 nutzen noch die **Ausgabe 2009** (-SF Taster, -RZ
Drosselrückschlagventil, -KF für die SPS, -AZ). Die Unterklassen unterscheiden sich teilweise
(-SF/-SJ, -KF/-KE, -RZ/-RN). Nutzt der Unterricht Unterklassen der Ausgabe 2009, im Schülermaterial nennen („nach
DIN EN 81346-2:2009“) und im Begleitblatt begründen – nie mischen.
Andere Hauskonventionen nur, wenn im Unterricht so verwendet (dann `bmk_pruefen.py --bmk-muster`).

**Regeln**
1. **Technologieschema mit Text-Legende** (BMK | Betriebsmittel | Lage/Aufgabe). Das Bild allein
   reicht nicht: Kennzeichen im Bild sind für Prüfskripte und Zweitkorrektur unsichtbar (T.3).
2. Die **Funktionsbeschreibung** nennt jedes Betriebsmittel mit Kennzeichen („Taster Start -SJ1“),
   - jeden **Geber** mit Kontaktart und Bedeutung des Signals („-BG2 (NC) meldet 0, wenn die Mulde
     oben ist“), Analoggeber mit Messbereich und Signal („-BT1, 0 … 10 V für 0 … 50 °C“),
   - jeden **Aktor** mit Wirkung („-MB1 = 1: Zylinder -MM1 fährt aus“),
   - **Grundstellung**, **Start**, **Stopp bzw. Not-Halt** – oder ausdrücklich ausgeklammert
     („Not-Halt ist hardwaremäßig gelöst und nicht Teil der Aufgabe“),
   - Zeiten und Zählwerte als Zahlen, Verzweigungen mit Bedingung (T.2, T.4, T.7).
3. **Dieselben Kennzeichen und Bezeichnungen** in Legende, Funktionsbeschreibung, vorgegebener
   Zuordnungsliste, Aufgaben, Anlagen und Musterlösung. Ein neues Betriebsmittel wird in der
   Teilaufgabe eingeführt (Name, Kennzeichen, Kontaktart), bevor es verwendet wird (T.1).
   Keine Kennung erst in der Musterlösung.
4. **Zuordnungsliste** nach Notationsblatt: BMK | Betriebsmittel | Operand SPS | Operand
   Kleinsteuerung | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart – nur die Spalten der
   Plattformen des Unterrichts; jeder Operand bzw. Pin einmal (T.5). Ist die Liste die Aufgabe: Kopf
   und zwei Beispielzeilen vorgeben (alle Plattformspalten ausgefüllt), dazu die Anlage mit den Ein-
   und Ausgängen je Plattform; die Beispielzeilen stimmen mit der Musterlösung überein. Beim
   Mikrocontroller sagt „Signal 1 bedeutet“, ob ein Pull-up die Logik umkehrt.
5. **Einheitliche Schreibweise** – nicht „-S1“ neben „S1“, „–S1“ (Gedankenstrich) oder „S 1“ (T.6).
6. **GRAFCET** (DIN EN 60848:2014) bzw. Programm (IEC 61131-3, ohne AWL): Merkmale **funktional**
   formulieren, unabhängig von Schrittnummern und Namen der Musterlösung (Abschn. 5); die Normform
   (Initialschritt, Rücksprung mit Pfeil, Bedingungen, Aktionsarten) als eigenes Merkmal mit 1–2 BE
   (`references/normen-technik.md`, Abschn. 3–4). Notation nach Notationsblatt (Anlage im
   Schülermaterial); in Textform als Tabelle Schritt | Aktion | Transition zum Folgeschritt mit
   „·“, „+“, „¬“, „5s/X3“, „[-BT1 > −16 °C]“, „→ n“ (T.9). Analogbedingungen mit physikalischem
   Wert, damit der GRAFCET für jede Plattform gilt.
7. **Kennbuchstaben und Ausgabe** (T.8): nur Klassen und Unterklassen der Ausgabe 2020; jedes
   Kennzeichen mit Klasse **und** Unterklasse (-SJ1, nicht -S1); je Klasse eine Tiefe (nicht -BG1
   neben -BGB2); Ausgabe in den Hinweisen genannt („Die
   Betriebsmittel sind nach DIN EN IEC 81346-2:2020 gekennzeichnet.“).
8. **Folgefehler:** Eine abweichende Lösung ist richtig, wenn sie zur eigenen Zuordnungsliste passt
   – als Regel bei der Teilaufgabe, nicht als Ermessen.

Sinngemäß für andere Bezeichner: Geräte- und Schnittstellennamen in Netzplänen, Klassen-, Methoden-
und Attributnamen in Klassendiagrammen und Code (in Backticks, K.9), Positionsnummern in Zeichnungen.

## 5. Bewertungsmerkmale (K.1–K.3, K.8, K.10)

Die genaue Bepunktung steht **nicht im Lehrermaterial**, sondern im **Bewertungsraster**
(`assets/vorlage-bewertungsraster.md`): je Teilaufgabe ein Abschnitt „## Teilaufgabe N.n – Titel (n BE)“
mit Tabelle und Regeln. Das Lehrermaterial enthält Erwartungshorizont (Zeile je Operator mit BE nach AFB)
und eine knappe Musterlösung. Aus dem Raster entstehen Bewertungsbogen und Bewertungsmappe (Excel).

| Nr. | Bewertungsmerkmal | Kurztext | Art | AFB | BE |
|---|---|---|---|---|---:|
| 1 | Initialschritt entspricht der Grundstellung (alle Aktoren aus, -BG1 meldet Mulde unten) | Initialschritt | Kriterium | II | 1 |
| 2 | Start nur mit -SJ1 **und** -BG1 = 1 als Transition | Startbedingung | Kriterium | II | 1 |
| 3 | Dosieren: -MB1 für 4 s, danach -MB2 für 6 s (zwei Schritte oder Zeitglieder) | Dosierfolge | Kriterium | II | 2 |
| 4 | Rücklauf erst nach Wartezeit 3 s; Ende der Kette bei -BG1 = 1 | Rücklauf und Ende | Kriterium | III | 2 |

- **Kurztext** (K.10): Randvermerk in der Klausur und Text im Gutachten – beides wird **von Hand** in jede
  Arbeit geschrieben. Darum höchstens **vier Wörter und 30 Zeichen**, **keine Werte** (keine IPv4-/IPv6-
  oder MAC-Adressen, Präfixlängen, Zahlen mit Einheit, Formeln, Code), keine Klammern und Aufzählungen.
  Der Kurztext benennt das Merkmal, nicht die Lösung: „Broadcastadresse“ statt „Broadcastadresse
  192.168.40.191“, „Präfix“ statt „Präfix 2001:db8:40::/64“, „Ergebnis“ statt „Ergebnis 16,59 MB“. Die
  Werte stehen im Merkmal; die Korrektur sieht sie dort.
- **Art:** `fest` = genau eine richtige Antwort bzw. ein Wert; `Kriterium` = beobachtbares Merkmal
  einer offenen Lösung; `Urteil` = Entscheidung mit Begründung nach vorgegebenen Kriterien.
- **Höchstens 3 BE je Merkmal** – größere Merkmale teilen (K.3).
- **Beobachtbar:** was genau stehen muss. Nicht: „sinnvoll“, „angemessen“, „im Wesentlichen“,
  „schlüssig“, „nachvollziehbar“, „überzeugend“, „gut“ (K.3).
- **Summen:** BE der Merkmale = BE der Teilaufgabe; BE je AFB = Zeilen des Erwartungshorizonts zu
  dieser Teilaufgabe (K.2).
- **Anteile:** `Urteil` höchstens rund 30 % der BE (Richtwert 🔎, K.8) – Urteile bleiben, aber mit
  vorgegebenen Kriterien und Merkmalen für Kriterium, Anwendung und Entscheidung.

## 6. Regeln je Teilaufgabe (K.4–K.6)

Im Bewertungsraster unter der Merkmaltabelle, nur wo zutreffend (das Skript findet die Regeln auch in
der Musterlösung, dort aber nur, wenn sie für die Begutachtung nötig sind):
- *Gleichwertig:* zulässige andere Lösungen und Wege mit voller BE – Pflicht bei offenen Operatoren
  (entwickeln, entwerfen, konstruieren, optimieren, beurteilen, bewerten, Stellung nehmen,
  analysieren, untersuchen; Informatik zusätzlich implementieren, modellieren, erweitern, testen,
  diskutieren) (K.5).
- *Folgefehler:* wie ein Fehler aus einer vorigen Teilaufgabe weitergerechnet wird – Pflicht bei
  Ersatzwerten (K.6).
- *Toleranz:* Rundung und Abweichung bei Zahlenwerten, abweichende Tabellenwerte – Pflicht bei
  Rechnungen und Auswahl aus Tabellen (K.4).
- *0 BE:* Antworten, die keine BE erhalten (z. B. Ergebnis ohne Rechenweg, Kennzeichen vertauscht).

## 7. Bewertungsbogen und Gutachten

`python3 scripts/abitur_check.py SM.md LM.md --bewertungsbogen 75_…_bewertungsbogen.md` erzeugt aus
den Merkmaltabellen des Bewertungsrasters (gleicher Dateianfang neben dem Lehrermaterial, sonst
`--raster`) einen leeren Bogen mit Spalte „Kurztext“: Kopf mit Prüflingsnummer (keine Namen), je Merkmal
erreichbare und erreichte BE, Summen je Aufgabe und gesamt, Umrechnung in Notenpunkte, Felder für
Erst- und Zweitkorrektur. Das Skript überschreibt keine vorhandene Datei.

### Bewertungsmappe (Excel) – Korrektur und Gutachten aus einer Quelle

`python3 scripts/bewertungsmappe.py 75_…_A_bewertungsbogen.md` erzeugt `75_…_A_bewertungsmappe.xlsx`
(liegen Schüler-, Lehrermaterial und Bewertungsraster daneben, kommen Titel der Teilaufgaben, Art der
Merkmale, Kurztexte, Regeln und Zeilen des Erwartungshorizonts dazu; Abweichungen zwischen Bogen und
Raster meldet das Skript). Formeln statt Makros, rechnet in Excel und LibreOffice; Blätter geschützt ohne Kennwort,
Eingaben gelb.

**Grundsatz:** Erwartungshorizont, Korrektureintrag in der Klausur und Gutachtentext sind deckungsgleich.
Je Bewertungsmerkmal gibt es einen **Kurztext** (Spalte im Raster; fehlt er, schlägt das Skript einen vor –
ohne Klammern und Werte, höchstens vier Wörter; im Blatt *Korrekturschlüssel* änderbar). Die Korrektur schreibt an den Rand Merkmalnummer und
Zeichen – ✓ erfüllt, (✓) teilweise mit BE, ✗ nicht erfüllt – und bei (✓) und ✗ den Kurztext. Die
Bemerkung je Teilaufgabe entsteht aus denselben Kurztexten und nennt **standardmäßig nur die Mängel**:
„Teilnetze: weitgehend erwartungsgemäß gelöst. Teilweise erfüllt: Hostbereich (1 von 2 BE). Nicht erfüllt:
Broadcastadresse.“ (Einstellung „Erfüllte Merkmale nennen“ auf *Start*, Standard „nein“). Ergänzungen
(Folgefehler, gleichwertige Lösung) wählt die Korrektur aus einer Liste oder schreibt sie frei – kurz.

| Blatt | Inhalt |
|---|---|
| Start | Angaben (Schule, Referat, Korreferat, Fachprüfungsleitung), Einstellungen, Anleitung, Datenschutz |
| Korrekturschlüssel | Merkmale mit Art, AFB, BE und Kurztext; je Teilaufgabe Zeilen des Erwartungshorizonts und Regeln |
| Prüflinge | Prüflingsnummer (Name optional), Sprachfehler je Seite mit Abzug-Vorschlag, Abzug, Korreferat und Festsetzung bei Abweichung, Ø Kursergebnisse (optional) |
| Erfassung | BE je Merkmal, eine Spalte je Prüfling (Prüfung: 0 … erreichbar, halbe BE); Summen je Teilaufgabe, Aufgabe, AFB, Notenpunkte; offen/fertig; Ø und Lösungsquote je Merkmal |
| Übersicht | Notenpunkte nach Bewertungsmaßstab, Abzug, Ergebnis (erst bei vollständiger Bewertung), BE bis zum nächsten Notenpunkt (Grenzfall), Abweichung von den Kursergebnissen, Notenspiegel, Anteile je Aufgabe und AFB |
| P01 … | je Prüfling: Bewertungsbogen je Merkmal mit Vermerk; Gutachten mit Satz je Aufgabe, Bemerkung je Teilaufgabe, Einschätzung je AFB, Gesamturteil (Notendefinition), Abzug, Endbewertung, Unterschriften |
| Notenschlüssel, Textbausteine | Bewertungsmaßstab (wie `abitur_check.py`); alle Satzbausteine änderbar |

Die Mappe rechnet und formuliert vor; Notenpunkte setzen Referat, Korreferat und Fachprüfungsleitung.
Ausgefüllt enthält sie Prüfungsergebnisse – nur lokal, nie in eine KI-Umgebung laden. 🔎
Notendefinitionen, Abzug für Sprache und Form (EB-AVO-GOBAK) und Verfahren bei abweichender Bewertung
mit der geltenden Fassung abgleichen.

## 8. Korrekturprobe

Vor der Einreichung je Teilaufgabe mit Merkmalen der Art `Kriterium` oder `Urteil`:
1. drei **erfundene** Antworten schreiben – vollständig richtig, typischer Fehler, zulässige
   Alternative;
2. mit der Merkmaltabelle bewerten und die BE im Begleitblatt festhalten;
3. Wo die Vergabe nicht eindeutig ist, Merkmal schärfen oder Auftrag präzisieren.
Optional bewertet eine Fachkollegin bzw. ein Fachkollege dieselben Antworten unabhängig; weicht
eine Teilaufgabe um mehr als 1 BE ab, ist das Merkmal nicht eindeutig. Nur erfundene Antworten –
keine Arbeiten von Lernenden.

## 9. Kennungen und Prüfregeln

| Kennung | Regel | Status bei Verstoß | Skript |
|---|---|---|---|
| K.1 | Merkmaltabelle je Teilaufgabe (im Bewertungsraster) | ❌ | `abitur_check.py` |
| K.2 | Merkmal-BE = BE der Teilaufgabe; BE je AFB = Erwartungshorizont | ❌ | `abitur_check.py` |
| K.3 | Merkmal ≤ 3 BE, ohne Wertwörter | ⚠ | `abitur_check.py` |
| K.4 | Rechnung/Auswahl mit Toleranz bzw. Rundung | ⚠ | `abitur_check.py` |
| K.5 | offene Operatoren: *Gleichwertig* und Merkmale der Art Kriterium/Urteil | ⚠ | `abitur_check.py` |
| K.6 | Ersatzwert im Schülermaterial → *Folgefehler* im Lehrermaterial | ⚠ | `abitur_check.py` |
| K.7 | Auftragssatz: ein Operator, Zahlwort, keine vagen Wörter, keine W-Frage, ≤ 45 Wörter | ⚠ | `abitur_check.py` |
| K.8 | Anteil `Urteil` ≤ rund 30 % der BE | ⚠ | `abitur_check.py` |
| K.9 | Bezeichner in Backticks in Schüler- und Lehrermaterial gleich geschrieben | ⚠ | `abitur_check.py` |
| K.10 | Kurztext je Merkmal: ≤ 4 Wörter, ≤ 30 Zeichen, ohne Werte, Klammern, Aufzählungen | ⚠ | `abitur_check.py` |
| U.1 | Schülermaterial ohne Anlagen ≤ 12 Seiten (Schätzung; exakt mit `abitur_docx.py --seiten`) | ⚠ | `abitur_check.py` |
| U.2 | Lehrermaterial ohne Merkmaltabellen (Bepunktung im Bewertungsraster) | ⚠ | `abitur_check.py` |
| T.1 | Kennzeichen der Musterlösung im Schülermaterial eingeführt | ❌ | `bmk_pruefen.py` |
| T.2 | Kennzeichen aus Legende und Zuordnungsliste in der Funktionsbeschreibung | ❌ | `bmk_pruefen.py` |
| T.3 | Technologieschema mit Text-Legende | ⚠ | `bmk_pruefen.py` |
| T.4 | Kontaktart/Signalbedeutung je Geber, widerspruchsfrei | ⚠ / ❌ | `bmk_pruefen.py` |
| T.5 | Operanden eindeutig, Vorgabe = Musterlösung | ❌ / ⚠ | `bmk_pruefen.py` |
| T.6 | Schreibweise einheitlich | ⚠ | `bmk_pruefen.py` |
| T.7 | Grundstellung, Start, Stopp/Not-Halt beschrieben | ⚠ | `bmk_pruefen.py` |
| T.8 | Kennbuchstaben nach DIN EN IEC 81346-2:2020 (oder genannte Ausgabe 2009), immer Klasse und Unterklasse, je Klasse eine Tiefe | ⚠ | `bmk_pruefen.py` |
| T.9 | GRAFCET in Textform nach Notationsblatt (Verknüpfungen, Zeit, Vergleich, Folgeschritt, Aktionsarten) | ⚠ | `bmk_pruefen.py` |

## 10. Umfang (U.1, U.2)

**Schülermaterial:** höchstens **12 Seiten ohne Anlagen** (Vorgabe der Fachgruppe; Anlagen und
Hilfsmittel kommen dazu). Mehr Seiten machen die Klausur schnell zu umfangreich – für Prüflinge und
Korrektur. `abitur_check.py` schätzt die Seiten der Word-Fassung (A4, Arial 11 pt, Abbildungen nach dem
Seitenverhältnis der SVG; Abweichung zur LibreOffice-Fassung der Beispiele unter 10 %); exakt zählt
`abitur_docx.py … --seiten` (LibreOffice). Kürzen, in dieser Reihenfolge:
1. Situationsabsätze auf die neue Information beschränken; Handlungssituation drei bis sechs Sätze.
2. Material, das nicht jeder Auftrag braucht, in eine Anlage; Tabellen statt Fließtext.
3. Teilaufgaben zusammenlegen, die dasselbe Merkmal prüfen; Abbildungen nur, wo ein Auftrag sie braucht.

**Lehrermaterial:** Erwartungshorizont, Bewertungsmaßstab, kurze Hinweise zur Bewertung und eine
**knappe Musterlösung** (Lösungsgang mit Zwischenergebnissen, Lösungsbilder) – keine Merkmaltabellen,
keine Wiederholung der Aufgabenstellung, keine Lehrbuchtexte. Die genaue Bepunktung steht im
Bewertungsraster; ältere Fassungen mit Tabellen in der Musterlösung lagert
`abitur_check.py SM.md LM.md --auslagern 75_…_A_bewertungsraster.md` aus (Tabellen und Regeln danach
im Lehrermaterial löschen).
