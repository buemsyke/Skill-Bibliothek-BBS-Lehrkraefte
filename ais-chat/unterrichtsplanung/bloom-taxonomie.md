<!-- Assistenten-Fassung des Skills 'bloom-taxonomie'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
# Taxonomien nach Bloom

## Zweck
Sichtbar machen, **welche Denkleistung** Aufgaben und Ziele wirklich verlangen – und gezielt
nachsteuern, damit Unterricht kognitiv aktiviert, ohne zu überfordern.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Drei Modi

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Analysieren** | „Ordne die Aufgaben meines Arbeitsblatts nach Bloom ein." | Einordnungstabelle, Matrix, Verteilung, Empfehlungen |
| **B Erstellen** | „Erstelle zu Gewindearten Aufgaben über alle Taxonomiestufen." | Aufgabentreppe Stufe 1–6 mit Erwartungen |
| **C Umformulieren** | „Heb diese drei Aufgaben auf Analysieren/Bewerten." | Vorher/Nachher mit Begründung |

## Eingaben
- **Pflicht:** Material (Aufgaben, Ziele, Fragen) **oder** Thema.
- **Wichtig, sonst Annahme:** Was wurde vorher **geübt**? (Entscheidet, ob eine Aufgabe
  Anwenden oder Problemlösen ist.) Zielniveau (DQR) bzw. Lerngruppe.
- **Optional:** Zielverteilung, Wissensarten, Handlungssituation.

## Grundsätze der Einordnung

1. **Nach tatsächlicher Denkleistung einordnen, nicht nach dem Verb.** „Beurteilen Sie, ob
   Stahl ein Metall ist" ist Erinnern. „Beschreiben Sie den Fehler, den Sie im Messprotokoll
   finden" ist Analysieren.
2. **Vorwissen entscheidet.** Wiederholt die Aufgabe ein geübtes Beispiel → eine Stufe
   niedriger als der Operator suggeriert; verlangt sie Übertragung auf eine neue Situation →
   Anwenden oder höher. Fehlt die Information: begründete Annahme.
3. **Zwei Dimensionen.** Kognitive Prozessstufe (1–6) **und** Wissensart (A Fakten,
   B Konzepte, C Prozeduren, D Metakognition). Berufliche Handlungsaufgaben liegen oft in
   C3–C6; Reflexionsaufgaben in D.
4. **Primärstufe pro Aufgabe.** Die höchste *bewertungsrelevante* Stufe zählt; Teilschritte
   darunter sind Voraussetzungen, keine eigenen Einträge.
5. **Taxonomie ≠ Schwierigkeit.** Erinnern kann schwer sein, Bewerten leicht. Schwierigkeit
   gesondert vermerken, wenn auffällig.
6. **AFB-Bezug** über `references/operatoren-afb.md`; Bloom-Stufe und AFB nicht 1:1
   gleichsetzen (Faustregel: 1–2 ≈ AFB I, 3–4 ≈ AFB II, 5–6 ≈ AFB III).

## Vorgehen

**Modus A – Analysieren**
1. Aufgaben/Ziele extrahieren und nummerieren. Optional deterministische Zählhilfe:
   `python3 scripts/bloom_check.py DATEI.md [--ziele]` (auch .docx, .odt, .pdf; Operatoren je
   Stufe; ersetzt nicht das Urteil). Das Skript meldet Aufträge ohne Listenoperator und
   geschlossene Formate gesondert – diese von Hand einordnen. **Projekt-Lernsituationen:**
   Anforderungen im Lastenheft stehen oft als Nominalform („A) Entwicklung eines …“); das Skript
   ordnet sie über das Verb ein und kennzeichnet sie. Mit `--ziele` zählt es auch Kompetenz- und
   Zielformulierungen („bestimmen den Wirkungsgrad …“) und meldet nicht beobachtbare
   („Bereitschaft entwickeln“). Für Projekte die Aufträge nach der **Denkleistung im
   Erwartungshorizont** einordnen (vorgegebene Arbeitsschritte senken die Stufe). Bewertungsraster und Hinweiskästen nicht
   mitzählen. **„prüfen“** ist mehrdeutig: Prüfhandlung (inspizieren, messen) = Anwenden,
   Urteil an Kriterien = Bewerten.
2. Jede Aufgabe einordnen: Operator · Stufe · Wissensart · AFB · Begründung (ein Satz).
3. Matrix 6 × 4 zählen, Verteilung berechnen.
4. Mit Zielwerten vergleichen. Ohne Vorgabe gilt der **Richtwert für kognitiv aktivierenden
   Unterricht**: höchstens etwa ein Drittel Stufe 1–2, mindestens etwa ein Drittel Stufe 4–6;
   bei DQR 1–2 bzw. Einführungsstunden darf der Anteil Stufe 1–3 höher sein (begründen).
5. Lücken benennen (z. B. „keine Aufgabe in Bewerten", „Metakognition fehlt") und **je Lücke
   eine konkrete Umformulierung** liefern.

**Modus B – Erstellen**
1. Fachlichen Kern und – falls vorhanden – die Handlungssituation bestimmen.
2. Aufgabentreppe bauen: mindestens eine Aufgabe je Stufe 1–6, aufsteigend, inhaltlich
   aufeinander aufbauend, möglichst im selben beruflichen Kontext.
3. Je Aufgabe: Operator, Stufe, Wissensart, AFB, Erwartungshorizont in Stichpunkten.
   Die Treppe ist ein Werkzeug der Lehrkraft: Ins Material für Lernende gehen wenige, größere
   Aufträge daraus, keine Folge von sechs Kleinaufgaben; Stufe 1–2 nur, wo der Auftrag sie
   braucht (`references/schuelermaterial.md`).
4. Für Werkstatt-/Laborinhalte zusätzlich eine praktische Aufgabe mit Stufe nach Dave; für
   Haltungsziele (z. B. Arbeitssicherheit) eine affektive Stufe nach Krathwohl
   (`references/weitere-taxonomien.md`).

**Modus C – Umformulieren**
1. Ist-Stufe bestimmen und begründen.
2. Hebel wählen (`references/taxonomie-matrix.md`, Abschnitt „Hebel"): neue Situation statt
   bekanntes Beispiel, Kriterien selbst entwickeln lassen, Alternativen vergleichen und
   entscheiden, Fehler finden statt Lösung reproduzieren, Ergebnis begründet optimieren.
3. Vorher/Nachher-Tabelle mit Begründung und angepasstem Erwartungshorizont.

## Ausgabe
Datei `45_taxonomie-analyse.md` (Modus A/C) bzw. `45_aufgabentreppe_<thema>.md` (Modus B),
Kopf nach Skill-Vertrag, dann:
- **Einordnungstabelle**: Nr. | Aufgabe (gekürzt) | Operator | Stufe | Wissensart | AFB | Begründung
- **Matrix** (Zeilen Wissensart A–D, Spalten Stufe 1–6, Zellen = Anzahl)
- **Verteilung** (Anteile Stufe 1–2 / 3 / 4–6 sowie AFB I/II/III) mit Bewertung gegen Ziel
- **Empfehlungen** mit ausformulierten Aufgaben
- Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis)

## Qualitätscheck
- [ ] Jede Einordnung begründet und nach tatsächlicher Denkleistung (nicht nur nach Verb)?
- [ ] Annahme zum Vorwissen offengelegt?
- [ ] Beide Dimensionen (Stufe + Wissensart) erfasst?
- [ ] Verteilung gegen Ziel bzw. Richtwert bewertet, Abweichungen begründet?
- [ ] Jede Empfehlung als fertige, einsetzbare Aufgabe formuliert?
- [ ] Erwartungshorizonte passen zur neuen Stufe?

## Beispielaufrufe
> „Analysiere die Aufgaben in `40_material_arbeitsblatt-pneumatik.md` nach Bloom. Die Klasse hat
> Wegeventile bereits benannt und einfache Schaltpläne gezeichnet."

> „Erstelle eine Aufgabentreppe (Stufe 1–6) zum Thema Passungen für Industriemechaniker,
> 1. Ausbildungsjahr, DQR 4."

## Referenzen – wann lesen
- `references/taxonomie-matrix.md` – Stufen, Teilprozesse, Wissensarten, Metallbeispiele je
  Stufe, Hebel zum Anheben. **Bei jeder Einordnung.**
- `references/weitere-taxonomien.md` – Original-Bloom (1956), affektiv, psychomotorisch, SOLO.
- `references/schuelermaterial.md` – was ins Material für Lernende geht: kurz, offen gestellt, anschaulich, ohne Dekoration.
- `references/operatoren-afb.md` – Operator → AFB → Stufe.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
- `scripts/bloom_check.py` – optionale Zählhilfe (Python 3, ohne Zusatzpakete); liest Word/PDF
  über `scripts/text_lesen.py`.

# ANHÄNGE

## Anhang: references/operatoren-afb.md

# Operatoren, Anforderungsbereiche (AFB) und Taxonomiestufen

Arbeitsliste für berufsbildende Schulen. Die Zuordnung ist ein **Regelfall, kein Automatismus**:
Welche Stufe eine Aufgabe tatsächlich fordert, hängt vom Unterricht davor ab (Ist das
Verfahren geübt → Anwenden; ist es neu → Analysieren/Erschaffen). Ordnet ein Lehrplan,
eine Prüfungsordnung oder die Fachgruppe Operatoren anders zu, gilt deren Liste.

**Abweichende Liste im Beruflichen Gymnasium (Abitur, Klausuren der Qualifikationsphase):** Dort
gelten die Operatoren der EPA Technik mit eigener AFB-Zuordnung (`operatoren-epa-technik.md`, falls vorhanden).
Wichtigste Unterschiede: *begründen* nur AFB II, *dokumentieren* AFB III, *beschreiben* und
*nennen* nur AFB I; *erstellen*, *programmieren*, *implementieren*, *testen* sind keine
EPA-Operatoren (dort *entwickeln*, *entwerfen*, *überprüfen* verwenden oder als erweiterte
Operatoren im Lehrermaterial ausweisen).
**Im Fach Berufliche Informatik** gilt die EPA Berufliche Informatik mit eigener Liste (dort sind
*erstellen*, *implementieren*, *testen*, *erweitern*, *vervollständigen* Operatoren; Abschnitt
*Berufliche Informatik* in `operatoren-epa-technik.md`, falls vorhanden).

Spalten: **AFB** = Anforderungsbereich I (Reproduktion), II (Reorganisation und Transfer),
III (Reflexion und Problemlösung). **Bloom** = Stufe der revidierten Taxonomie nach
Anderson/Krathwohl (1 Erinnern · 2 Verstehen · 3 Anwenden · 4 Analysieren · 5 Bewerten ·
6 Erschaffen).

## AFB I – Reproduktion

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| nennen, angeben, aufzählen | Begriffe, Daten, Fakten ohne Erläuterung wiedergeben | 1 |
| bezeichnen, benennen | Bauteile, Größen, Symbole korrekt mit Fachbegriff versehen | 1 |
| wiedergeben | Inhalte sachlich zutreffend in eigenen Worten formulieren | 1–2 |
| beschreiben | Sachverhalt, Ablauf oder Aufbau strukturiert und fachsprachlich wiedergeben | 2 |
| darstellen | Zusammenhänge geordnet wiedergeben, auch grafisch (Skizze, Tabelle, Schema) | 2 |
| zusammenfassen | Kernaussagen komprimiert und strukturiert wiedergeben | 2 |
| skizzieren | Wesentliches vereinfacht grafisch oder in Stichpunkten darstellen | 2 |

## AFB II – Reorganisation und Transfer

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| erklären | Ursache–Wirkung bzw. Funktionsweise nachvollziehbar machen | 2 |
| erläutern | Sachverhalt beschreiben **und** durch Zusatzinformationen/Beispiele verständlich machen | 2–3 |
| zuordnen, einordnen | Sachverhalte begründet in einen Zusammenhang oder eine Systematik stellen | 2–3 |
| anwenden | Bekanntes Verfahren auf einen neuen, ähnlichen Fall übertragen | 3 |
| berechnen, bestimmen, ermitteln | Ergebnis mit nachvollziehbarem Lösungsweg und Einheiten gewinnen | 3 |
| auswählen | aus Alternativen kriteriengeleitet das Passende festlegen (Tabellenbuch, Katalog, Datenblatt) | 3–4 |
| erstellen, anfertigen | Produkt nach Vorgaben anfertigen (Schaltplan, Arbeitsplan, Prüfprotokoll, Stückliste) | 3 |
| durchführen | Verfahren, Messung, Prüfung fachgerecht ausführen und dokumentieren | 3 |
| auswerten | Daten, Messwerte, Diagramme interpretieren und Schlüsse ziehen | 4 |
| analysieren, untersuchen | Bestandteile, Strukturen, Fehlerursachen systematisch herausarbeiten | 4 |
| vergleichen, gegenüberstellen | Gemeinsamkeiten und Unterschiede kriteriengeleitet herausarbeiten | 4 |
| herausarbeiten | aus Material bestimmte Sachverhalte erkennen und darstellen | 4 |
| ableiten | aus Gegebenem begründet eine Folgerung oder Größe gewinnen | 4 |
| modellieren | Sachverhalt in ein Modell überführen (Ablaufplan, GRAFCET, Struktogramm, Ersatzschaltbild) | 4–6 |
| implementieren, programmieren | Modell/Konzept in einer konkreten Umgebung lauffähig umsetzen | 3–6 |

## AFB III – Reflexion und Problemlösung

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| prüfen, überprüfen | Aussagen, Ergebnisse oder Lösungen an Kriterien/Normen messen und Abweichungen begründen | 5 |
| beurteilen | zu einem Sachverhalt ein begründetes **Sachurteil** nach Kriterien fällen | 5 |
| bewerten | wie beurteilen, zusätzlich mit begründetem eigenem Standpunkt bzw. Wertmaßstab | 5 |
| begründen | Aussage oder Entscheidung durch Argumente und Fachwissen stützen | 4–5 |
| Stellung nehmen, erörtern, diskutieren | Argumente abwägen und zu einem begründeten Ergebnis kommen | 5 |
| reflektieren | eigenes Vorgehen/Ergebnis kriteriengeleitet kritisch prüfen, Konsequenzen ableiten | 5 |
| entwickeln, entwerfen, konzipieren | für ein neues Problem eine eigenständige Lösung erarbeiten | 6 |
| gestalten | eigenständig und kreativ eine Lösung oder ein Produkt ausformen | 6 |
| optimieren | bestehende Lösung begründet verbessern (Kosten, Sicherheit, Energie, Qualität) | 5–6 |
| planen (offen) | Vorgehen für eine offene Problemstellung eigenständig festlegen | 6 |

## Berufspraktische Operatoren in schriftlichen Aufträgen

Für Aufträge, die eine berufliche Handlung vorbereiten, dokumentieren oder kommunizieren. Der
AFB hängt davon ab, ob Form und Verfahren vorgegeben sind (I–II) oder selbst gewählt und
begründet werden müssen (II–III).

| Operator | Erwartete Leistung | AFB | Bloom |
|---|---|---|---|
| berichtigen | falsche Aussage erkennen und fachlich richtigstellen | I–II | 2–3 |
| dokumentieren, protokollieren | Vorgehen, Messwerte und Ergebnisse vollständig und nachvollziehbar festhalten | I–II | 2–3 |
| messen | Größe mit geeignetem Messmittel bestimmen, Messwert mit Einheit angeben | I–II | 3 |
| formulieren, verfassen | adressatengerechten Text verfassen (Kundeninformation, E-Mail, Übergabenotiz) | II | 3 |
| präsentieren | Ergebnis adressatengerecht, strukturiert und fachsprachlich vorstellen | II | 3–4 |
| simulieren | Verhalten eines Systems mit Software oder Modell nachbilden und die Ergebnisse deuten | II | 3–4 |
| experimentieren, einen Versuch durchführen | nach Plan messen, beobachten, dokumentieren und Sicherheitsregeln einhalten | II | 3 |
| eine Hypothese aufstellen, formulieren | eine prüfbare Vermutung mit Begründung formulieren | III | 6 |
| nachweisen | rechnerisch oder experimentell zeigen, dass eine Anforderung erfüllt ist | II–III | 4–5 |

## Wissensarten und Anforderungsbereiche

| Wissensart | Leitfrage | typischer AFB |
|---|---|---|
| Sachwissen | Was muss man kennen? | I – nennen, beschreiben, zuordnen |
| Prozesswissen | Wie geht man vor? | II – anwenden, durchführen, erstellen, analysieren |
| Reflexionswissen | Warum so, mit welcher Wirkung? | III – beurteilen, bewerten, begründen, entwickeln |

Material und Prüfungen sollten über Sachwissen hinausgehen: kein Arbeitsblatt nur mit AFB I,
kein erster Auftrag auf AFB III. Verteilungen werden **ausgezählt**, nicht geschätzt.

## Praktische Operatoren (Werkstatt, Labor) – psychomotorische Stufen nach Dave

| Operator (Beispiele) | Stufe nach Dave (1970) |
|---|---|
| nachmachen, unter Anleitung ausführen | 1 Imitation |
| nach Anleitung montieren, einstellen, messen | 2 Manipulation |
| genau, sicher und ohne Hilfe fertigen, prüfen, justieren | 3 Präzision |
| mehrere Arbeitsschritte koordiniert ausführen, Abläufe kombinieren, in Betrieb nehmen | 4 Handlungsgliederung |
| routiniert, situationsangepasst und effizient arbeiten, instand setzen unter Zeitdruck | 5 Naturalisierung |

## Verben für Personale Kompetenz (SchuCu-BBS)

Sozialkompetenz: *stimmen sich ab, wirken mit, beraten, präsentieren adressatengerecht,
geben und nehmen Rückmeldung, übernehmen Verantwortung im Team, vertreten Ergebnisse,
lösen Konflikte sachlich*.
Selbständigkeit: *planen ihr Vorgehen eigenständig, schätzen ein, reflektieren, handeln in
Verantwortung, setzen sich selbstkritisch auseinander, identifizieren Verbesserungspotenziale,
wählen Lernhilfen aus, beachten Arbeitssicherheit eigenverantwortlich*.

## Nicht verwenden (nicht beobachtbar)

*verstehen, kennen, wissen, lernen, begreifen, sich bewusst sein, vertraut sein mit,
Einblick gewinnen, die Bereitschaft entwickeln, die Fähigkeit verbessern*. Ersatz: Was tun die SuS sichtbar, **woran** erkennt man es?

## Faustregeln für Aufgaben

- **Operator + Inhalt + Bedingung:** „Berechnen Sie die erforderliche Kolbenkraft **für
  den Ausschiebezylinder** unter Berücksichtigung eines Wirkungsgrads von 0,85."
- Keine W-Fragen („Was ist …?") in Aufgaben – immer einen Operator.
- Pro Teilaufgabe **ein** Operator; Mehrfachoperatoren („nennen und erläutern") nur, wenn
  beide Leistungen bewertet werden.
- Der Operator legt die Bewertung mit fest: nennen ≈ 1 Punkt je Aspekt, erläutern ≈ 2 Punkte
  je Aspekt, beurteilen = Kriterium + Urteil + Begründung.

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.
Klausur- und Abiturformat haben eigene Richtwerte (`klausur-erstellen`, `abiturvorschlag-erstellen`);
die vier Regeln gelten dort sinngemäß.

## Inhalt
1. Vier Regeln
2. Darstellungen statt Text
3. Aufträge offen statt kleinschrittig
4. Was entfällt
5. Richtwerte
6. Rückwärtsprobe vor der Ausgabe

## 1. Vier Regeln

1. **Kurz.** Lernende lesen nur, was sie für den Auftrag brauchen. Kein Satz ohne Aufgabe,
   keine Wiederholung, kein Exkurs.
2. **Offen gestellt.** Ein Auftrag nennt Ziel (Operator), Gegenstand, Ergebnisform und woran
   man merkt, dass man fertig ist. Den Weg finden die Lernenden; Schritte und Gerüste stehen in
   gestuften Hilfen, die man bei Bedarf zieht.
3. **Anschaulich.** Aufgaben arbeiten mit Zeichnungen, Darstellungen und Grafiken: ablesen,
   auswerten, ergänzen, Fehler finden, selbst zeichnen. Was eine Darstellung zeigt, wird nicht
   zusätzlich beschrieben.
4. **Ohne Dekoration.** Nur, was dem Ziel dient (Abschn. 4).

Gekürzt wird Überflüssiges, nicht Fachinhalt: Fachbegriffe, Sicherheitshinweise und
Erfolgskriterien bleiben vollständig.

## 2. Darstellungen statt Text

| Inhalt | Darstellung | so entsteht sie |
|---|---|---|
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen`; Technologieschema mit `technologieschema-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen`; GRAFCET und Funktionsplan mit `technologieschema-erstellen` |
| System, Energie- und Datenfluss, Regelkreis | Blockschaltbild | `fachdiagramm-erstellen` |
| Zusammenhang zweier Größen | Diagramm, Kennlinie mit beschrifteten Achsen | aus gerechneten Werten oder dem Datenblatt als SVG erzeugen (Code), nie geschätzt |
| Vergleich, Kriterien, Kenndaten | Tabelle, Matrix | Markdown-Tabelle |
| Begriffe und ihre Beziehungen | Strukturbild | `fachdiagramm-erstellen` (Bauart `flow`), Tabelle |
| Daten und Software | ER-, Klassen-, Sequenzdiagramm | `fachdiagramm-erstellen` |
| Schaltung, Werkstück | Schaltplan, technische Zeichnung nach Norm | Herstellerunterlage, Tabellenbuch, eigene Zeichnung (Platzhalter mit Quelle) |

Jede Zeichnung entsteht als **SVG aus einer Spec** – nie als Zeichnung aus Zeichen (ASCII-Art) und
nie als Mermaid in der Ausgabe (Skill-Vertrag Abschn. 3).

**Die Darstellung ist Arbeitsgegenstand, nicht Beigabe.** Aufträge, die mit ihr arbeiten
(Beispiele am Gurtförderer GF-2, fiktiv):

| Auftrag | Beispiel |
|---|---|
| ablesen, auswerten | „Ermitteln Sie aus der Kennlinie die Drehzahl bei 80 % Last.“ |
| ergänzen | „Benennen Sie im Anlagenbild die Bauteile ① bis ④.“ |
| Fehler finden | „Der Arbeitsplan in Abb. 2 enthält zwei Fehler. Berichtigen Sie sie.“ |
| selbst zeichnen | „Skizzieren Sie, wie die Spannstation verstellt werden muss.“ |
| vergleichen | „Vergleichen Sie die Gurtlaufbilder A und B.“ |

Regeln:
- **Am Auftrag:** Abbildung direkt bei dem Auftrag, der sie braucht; Beschriftung in die
  Abbildung, Positionsnummern statt Legendentext, wo möglich.
- **Fachlich richtig und normgerecht:** Schaltzeichen, Kennzeichen und Formelzeichen nach
  Norm; Werte hinter Diagrammen sind gerechnet.
- **Schwarzweiß lesbar:** Farbe nur mit Bedeutung und nie allein (zusätzlich Linienart oder
  Beschriftung).
- **Nie erfinden:** keine KI-Bilder, die Fotos, echte Anlagen oder Messkurven vortäuschen. Was
  nicht selbst gezeichnet werden kann (Foto, Herstellerzeichnung, Normauszug), steht als
  Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz]` und ist ein Prüfauftrag.
- **Barrierearm:** Alternativtext (ein Satz) je Abbildung.
- **Platz für Zeichnungen der Lernenden:** in der Druckfassung Kasten oder Raster statt Linien.

Nicht jede Aufgabe braucht ein Bild (Begründung, Gespräch, Reflexion). Ein Arbeitsblatt oder
Infoblatt ganz ohne Darstellung ist aber zu begründen.

## 3. Aufträge offen statt kleinschrittig

**Kleinschrittig – so nicht:**

> 1. Lesen Sie den Wartungsplan (M1).
> 2. Unterstreichen Sie alle Arbeiten, die nach 500 Betriebsstunden fällig sind.
> 3. Übertragen Sie die Arbeiten in die erste Spalte der Tabelle.
> 4. Ergänzen Sie in der zweiten Spalte das Werkzeug.
> 5. Ergänzen Sie in der dritten Spalte die Sicherheitsmaßnahme.
> 6. Addieren Sie die Zeiten.

**Offen – so:**

> **1 Erstellen Sie** den Arbeitsplan für die 500-h-Wartung des GF-2 (Wartungsplan M1,
> Vorlage M3). Fertig, wenn jeder Schritt Werkzeug und Sicherheitsmaßnahme hat und die
> Gesamtzeit unter 2 h liegt.

Die Schritte stehen – kürzer – in den gestuften Hilfen (Impuls → Strategie → Teilschritt →
Kontrolle; Skill `differenzierung-erstellen`). Wer sie braucht, zieht sie. Formate mit weniger
Stufen ordnen zu: Lernlandkarte – Kontrolle ist der Selbstcheck des Lernpostens; Lektion –
Orientierung, Werkzeug, Gerüst entsprechen Impuls, Strategie, Teilschritt, die Kontrolle leisten
Realitätstest und Rückmeldung.

Signale für Kleinschrittigkeit:
- mehr als drei Teilaufgaben a), b), c) an einem Auftrag;
- eine Schrittfolge im Auftrag, die den Lösungsweg vorgibt („zunächst …, dann …,
  anschließend …“) oder eine Reihe kurzer Einzelaufträge, die zusammen einen Auftrag ergeben;
- Lesen, Unterstreichen, Abschreiben oder Übertragen als eigener Auftrag – das sind Mittel,
  kein Ziel;
- Lücken, die sich durch Abschreiben aus dem Text füllen lassen;
- Teilaufgaben, deren Ergebnis die nächste schon verrät.

**Zulässig und nicht kleinschrittig:**
- **Sicherheitsrelevante Schritte** (Freischalten, Stoffe, Mengen, Reihenfolge an der
  Maschine) stehen vollständig und in Reihenfolge – auch in einer offenen Anleitung.
- **Bedienschritte**, die nicht Lernziel sind (Messgerät einstellen, Software starten): kurz,
  am besten als Bildfolge oder Hinweis, nicht als Auftrag.
- **Übungsfolgen** zum Einschleifen einer Routine: gleichartige, je für sich vollständige
  Aufgaben (gelöstes Beispiel → steigend → eingekleidet).
- **Lösungsbeispiel mit Ausblenden:** steht als Beispiel, nicht als Auftrag.
- **Einführende Bildungsgänge** (Berufseinstieg, BVJ): enger geführt über Lösungsbeispiele,
  Hilfen und hohen Anschauungsgrad – nicht über zerlegte Aufträge.

## 4. Was entfällt

| entfällt | stattdessen |
|---|---|
| Schmuckbilder, Cliparts, Symbol- und Stockfotos, Illustrationen ohne Fachinhalt | Abbildung mit Fachinhalt – oder keine |
| Emojis und Symbole ohne Funktion (auch farbige Punkte als Stufenkennung) | Wort; zulässig sind die KI-Zeichen 🚫 💡 🔧 (`ki-vereinbarungen.md`, falls vorhanden), Warn- und Gefahrenzeichen, Ankreuzkästchen ☐ und ✔ ~ ✘ zur Selbsteinschätzung |
| Begrüßung, Motivationssätze („Viel Spaß!“, „Los geht’s!“), Ankündigungen („In diesem Arbeitsblatt lernen Sie …“) | gleich mit Situation oder Auftrag beginnen |
| Einleitung, die den Auftrag vorwegnimmt; Zusammenfassung dessen, was eben dastand | Kernaussage einmal, vorn |
| Exkurse, Anekdoten, Technikgeschichte, „Wussten Sie schon?“-Kästen | als Vertiefung, wenn sie zum Ziel beitragen – sonst streichen |
| dasselbe in Fachwissen, Hilfe und Auftrag | einmal, dort, wo es gebraucht wird |
| Zierrahmen, Farbflächen, Schmuckschriften | klare Überschriften; Kästen nur mit Funktion (Hilfe, Stolperstein, Sicherheit) |
| Angaben für die Lehrkraft (AFB, Kompetenzcodes, Annahmen, Prüfvermerke) | im Lehrerteil |
| Information, die kein Auftrag braucht | streichen |

Keine Dekoration, also bleibend: Kopfzeile (Lernsituation, Zeit, Sozialform), Name und Datum
auf Druckblättern, Erfolgskriterien, Bewertungskasten, KI-Zeichen, Quellen- und
Lizenzangaben, KI-Transparenzhinweis.

## 5. Richtwerte

Orientierung, kein Urteil. ⚠️ Noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

| Element | Richtwert |
|---|---|
| Ausgangslage, Bezug zur Situation | höchstens drei Sätze; besser Situationsmaterial (Störmeldung, Foto, Anlagenbild) |
| Arbeitsauftrag | ein bis zwei Sätze, ≤ ~25 Wörter, Operator zuerst; der Kontext steht einmal in der Ausgangslage |
| Teilaufgaben je Auftrag | höchstens drei |
| Satz | meist unter 15 Wörtern, keiner über 25; die sprachsensible Fassung ist bewusst strenger (über 20 Wörter teilen, `lesbarkeit.py`) |
| Infoblatt | eine Seite, ≤ ~300 Wörter Fließtext, mindestens eine tragende Darstellung |
| Arbeitsblatt (Teil für Lernende) | ≤ ~350 Wörter Fließtext (ohne Tabellen, Code, Abbildungen), mindestens eine Darstellung |
| Situationsmaterial | ≤ ~150 Wörter |
| Hilfekarte | je Stufe ≤ ~40 Wörter, gern als Teilbild oder Skizze |
| Rollenkarte | ≤ ~60 Wörter |
| Lektion (90 min) | ≤ ~1 500 Wörter ohne Code (`lektionsmuster.md`, falls vorhanden) |
| Lernlandkarte (eine Unterrichtseinheit) | ≤ ~1 500 Wörter wie eine Lektion; je Karte nur Auftrag, Material, Hilfen, Selbstcheck |
| sonstiges Material | ≤ ~400 Wörter Fließtext je Datei |

Authentische Dokumente (Betriebsanleitung, Datenblatt, Norm, Quelle der Quellenmappe) bleiben
im Original und zählen nicht mit – sie liegen als Auszug mit Fundstelle bei, nicht
abgeschrieben.

## 6. Rückwärtsprobe vor der Ausgabe

1. **Jeder Absatz, jede Abbildung:** Welcher Auftrag braucht das? Keiner → streichen.
2. **Jeder Auftrag:** Operator, Ergebnisform, Erfolgskriterium – und kein vorgegebener
   Lösungsweg? Schritte → in die Hilfen.
3. **Jede Aufgabe:** Mit welcher Darstellung wird gearbeitet? Keine → ergänzen, wo eine trägt.
4. **Dekoration** (Abschn. 4) gestrichen?
5. **Skript:** `python3 scripts/schuelermaterial_pruefen.py DATEI.md` – Fließtext, lange Sätze
   und Aufträge, Teilaufgaben und Schrittfolgen, Darstellungen je Auftrag, Dekoration,
   Lehrerangaben, doppelte Sätze. Wortzahl und Befunde im Qualitätscheck festhalten.

## Anhang: references/skill-vertrag.md

# Skill-Vertrag der Bibliothek „Unterrichtsentwicklung BBS"

Gemeinsamer Standard für alle Skills dieser Bibliothek. Er sorgt dafür, dass jeder Skill
**allein** funktioniert und trotzdem **mit jedem anderen kombinierbar** ist. Die Quelle liegt
in `_gemeinsam/skill-vertrag.md`; jeder Skill trägt eine Kopie unter `references/`.

---

## 1. Eigenständig arbeiten – Entwurf vor Rückfrage

1. Der Skill braucht nur den Auftrag der Lehrkraft. Fehlende Angaben werden durch
   **begründete, fachtypische Annahmen** ersetzt und sichtbar markiert:
   `⚠️ Annahme: 2. Ausbildungsjahr, 24 SuS, heterogen.` bzw. im Beruflichen Gymnasium
   `⚠️ Annahme: Jg. 13 (Qualifikationsphase), 22 SuS, Lerngebiet ING3.`
2. **Rückfragen nur, wenn ohne Antwort der ganze Entwurf unbrauchbar wäre** (z. B. Beruf
   bzw. Fach völlig unbekannt). Dann höchstens drei gebündelte Fragen, jeweils mit Vorschlag
   als Standardantwort.
3. Ziel ist ein **vollständiger erster Entwurf** (alle Abschnitte gefüllt), nicht ein
   perfekter Teil. Die Lehrkraft schärft nach.
4. Ein Skill ruft **keinen anderen Skill selbst auf**. Er empfiehlt am Ende sinnvolle
   Folge-Skills. Das Verketten übernimmt der Orchestrator `unterricht-entwickeln`.

## 2. Kontext übernehmen – die Planungsakte

Liegt eine **Planungsakte** vor (Datei `00_planungsakte.md` im Arbeitsordner oder ein
Planungsakte-Block im Gespräch), übernimmt der Skill daraus alle passenden Angaben und fragt
nichts erneut ab. Nach getaner Arbeit trägt er sein Artefakt in die Akte ein und ergänzt
leere Felder, die er festgelegt hat. Widersprüche zur Akte werden gemeldet, nicht still
überschrieben.

```markdown
---
projekt: "LS 4 – Förderband nach Störung wieder in Betrieb nehmen"
bundesland: Niedersachsen
schulform: Berufsschule (Teilzeit)
bildungsgang: Industriemechaniker/-in
ausbildungsjahr: 2          # vollzeitschulisch (z. B. BG) stattdessen: schuljahrgang, phase, schwerpunkt, lerngebiet
curriculare_vorgabe: "Rahmenlehrplan Industriemechaniker/-in, LF 6"
dqr: 4
zeitrichtwert_ls: 16
lerngruppe: "22 SuS, heterogen, 3 SuS mit Deutsch als Zweitsprache (ca. B1)"
rahmen: "Fachraum Steuerungstechnik, Moodle, 90-Minuten-Blöcke"
handlungssituation: "…"
handlungsergebnis: "…"
leitidee_ls: "…"            # didaktische Leitidee der Lernsituation (1–2 Sätze)
---

## Artefakte
| Nr. | Artefakt | Skill | Status | Datei |
|---|---|---|---|---|
| 10 | DQR-Einordnung | dqr-zuordnen | Entwurf | 10_dqr-einordnung.md |

## Entscheidungen
- …

## Annahmen und Prüfaufträge (gesammelt)
- …
```

## 3. Ausgabe – einheitlich und weiterverwendbar

**Format:** Markdown. Mit Dateizugriff wird als Datei gespeichert, sonst im Chat ausgegeben.
Ein bestehendes Dokument wird **nie überschrieben**; Überarbeitungen erhalten ein Suffix
(`…_sprachsensibel.md`, `…_v2.md`).

**Text zum Einfügen** (Systemanweisung, Moodle-Textfeld, Hinweistext, Importquelle) steht als
eigener Block im Format des Ziels – ohne Erläuterungen darin; Erläuterungen stehen davor oder
danach. **Vorschläge zu Vorhandenem** (Begutachtung, Überarbeitung, Einstellungen) nennen je
Vorschlag Stelle, neuen Wert und Begründung; was schon passt, wird zusammengefasst bestätigt
statt wiederholt.

**Material für Lernende** (alles, was Lernende in die Hand bekommen; Vorgabe der Fachberatung,
31.10.2026): **kurz** – kein Satz ohne Aufgabe; **offen gestellt** – Ziel, Ergebnis und
Erfolgskriterium statt Lösungsweg, Schritte in gestufte Hilfen; **anschaulich** – Aufgaben
arbeiten mit Zeichnungen, Darstellungen und Grafiken; **ohne Dekoration** – keine Schmuckbilder,
Emojis ohne Funktion, Floskeln oder Inhalte, die kein Auftrag braucht. Richtwerte und Beispiele:
`schuelermaterial.md`, falls vorhanden. Die Pflichtabschnitte (unten) stehen im Teil für die
Lehrkraft (nach `# Lösungen und Erwartungshorizont` bzw. `# Didaktische Hinweise`), nie im Teil für
Lernende.
Ausgenommen von den Richtwerten sind Klausur- und Abiturformat mit eigenen Regeln
(`klausur-erstellen`, `abiturvorschlag-erstellen`: Operator-Aufträge bis rund 40 bzw. 45 Wörter,
Antwortraum je Operator); kurz, eindeutig und ohne Dekoration bleiben auch sie.

**Zeichnungen** (Vorgabe der Fachberatung, 01.11.2026): Jede Zeichnung in einem Artefakt – Material
für Lernende, Lösung, Erwartungshorizont, Tafelbild, Entwurf, Begleitblatt – entsteht als **SVG aus
einer Spec** mit dem passenden Zeichen-Skill, dazu eine in diagrams.net bearbeitbare `.drawio.svg`,
eingebunden mit `![Alternativtext](abbildungen/….svg)` und kursiver Bildunterschrift. **Nie** als
Zeichnung aus Zeichen (ASCII-Art: Kästen aus ┌─┐ oder +---+, Pfeilketten, Struktogramm oder GRAFCET
im Codeblock), nie als Mermaid in der Ausgabe, nie als von Hand geschriebenes SVG.

| Zeichnung | Skill bzw. Weg |
|---|---|
| Blockschaltbild, Anlagen- und Systemübersicht, Ablauf, Regelkreis, Struktogramm, ER-Modell, UML, Relationenschema | `fachdiagramm-erstellen` |
| Kennlinie, Messwertdiagramm | aus den Werten per Code als SVG (z. B. matplotlib), Wertetabelle daneben |
| Foto, Werkstückzeichnung, fremde Abbildung | Datei mit Quelle und Lizenz, sonst Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle]` |
| Anlagenbild (Technologieschema), Schaltplanauszug mit Schaltzeichen, GRAFCET, Funktionsplan (FUP), Netzplan | `technologieschema-erstellen` |
| Simulationsschaltung | `circuitjs-schaltung-erstellen` |

Erlaubt bleiben Text-Tabellen derselben Inhalte (GRAFCET in Textform, Zuordnungsliste) für die
Zweitkorrektur und die Barrierefreiheit; Verzeichnisbäume und Programmcode sind keine Zeichnungen.
Lösungsbilder tragen `_loesung` im Namen und stehen nur im Teil für die Lehrkraft. **Ohne
Skriptausführung** (Assistent ohne Code) liefert der Skill die Spec und an der Stelle des Bildes den
Platzhalter `[ABBILDUNG: Inhalt – Spec <datei>.yaml]`; die Lehrkraft erzeugt das SVG lokal.
Vorhandenes Material mit Zeichnungen aus Zeichen wird beim Überarbeiten umgestellt. Prüfung:
`zeichnungen_pruefen.py`, falls vorhanden (❌ Zeichnung aus Zeichen, ⚠ Mermaid). Es öffnet auch jede
eingebundene SVG: ❌ Text über Text, Form oder Linie über Text, Text ragt aus seinem Kasten oder aus
dem Bild; ⚠ SVG ohne Spec und Werkzeugkennung (von Hand?), schräge Leitungen, Datei fehlt. Ein Skill,
der Zeichnungen braucht, ruft dafür das Zeichen-Skill auf oder bringt dessen Werkzeug mit
(`metadata.eduwerkzeuge`) – `pruefen` meldet einen `edu-*`-Befehl ohne beides.

**Dateinamen** (Nummer = Platz in der Planungskette):

| Nr. | Artefakt | Skill |
|---|---|---|
| 00 | Planungsakte | unterricht-entwickeln |
| 10 | DQR-Einordnung | dqr-zuordnen |
| 20 | Lernsituation | lernsituation-dokumentieren |
| 21 | LS-Analyse (Prüfbericht: Analysebogen, Phasencheck, Querschnitt, weitere Aspekte) | lernsituation-analysieren |
| 30 | Unterrichtsentwurf | unterrichtsentwurf-erstellen |
| 35 | Entwurfscheck (Selbstcheck/Beratung) | unterrichtsentwurf-analysieren |
| 36 | Unterrichtsreflexion (nach der Stunde: Selbstreflexion, Nachbesprechung) | unterricht-reflektieren |
| 40 | Unterrichtsmaterial | unterrichtsmaterial-erstellen |
| 41 | Experiment (Versuchsanleitung, Lehrerfassung, Gefährdungsbeurteilung) | experiment-planen |
| 42 | Fachdiagramm (Diagrammblatt, Specs unter `diagramme/`, SVG unter `abbildungen/`) | fachdiagramm-erstellen |
| 43 | Programmieraufgabe (Aufgabe, Codeordner `43_code/`, Erwartungshorizont) | programmieraufgabe-erstellen |
| 44 | Technikfolgenabschätzung (Dossier, Quellenmappe, Rollenkarten) | technikfolgen-abschaetzen |
| 45 | Taxonomie-Analyse | bloom-taxonomie |
| 46 | Technologieschema (Schemablatt mit Legende, Specs unter `schema/`, SVG unter `abbildungen/`) | technologieschema-erstellen |
| 47 | Simulationsschaltung (circuit.js: Schaltungstext, Messgeräte mit Erwartungswerten, Begleitblatt) | circuitjs-schaltung-erstellen |
| 48 | Mikrocontroller-Simulation (Wokwi: Spec, Projektordner mit Sketch, Schaltung und Szenarien, Zeitablauf, Begleitblatt) | wokwi-simulation-erstellen |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 70 | Klassenarbeit / Lernzielkontrolle mit Erwartungshorizont | klausur-erstellen |
| 75 | Abiturvorschlag (dezentral): Schüler- und Lehrermaterial je Vorschlag, Bewertungsbogen, Begleitblatt | abiturvorschlag-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

`abiturvorschlag-erstellen` (Nr. 75) hält Schüler- und Lehrermaterial einreichungsfertig: Kopf und
Pflichtabschnitte stehen im **Begleitblatt** (`75_abitur_<kurztitel>_begleitblatt.md`), nicht in den
Einreichungsunterlagen.

**Werkzeug-Skills** (Nr. 42, 46, 47, 48, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-technologieschema`, `schaltung.py`, `wokwi.py`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
Artefakt mit Pflichtabschnitten – diese hätten in der Quelle Folgen für die Ausgabe –, sondern
Kopf und Pflichtabschnitte stehen in einem **Begleitblatt** (`…_begleitblatt.md`,
Diagrammblatt). Nummern 92–96 (Ausspielen) folgen auf den Prüfbericht: veröffentlicht wird
geprüftes Material. Nr. 93 (agiles Lernen) kann auch für sich stehen, wenn eine Lehrkraft
selbst lernt; die Lernakte gehört dann der lernenden Person.

**Kopf jedes Artefakts:**

```yaml
---
artefakt: Lernsituation
titel: "Förderband nach Störung wieder in Betrieb nehmen"
skill: lernsituation-dokumentieren
skill_version: "1.0"
stand: 2026-10-08
bildungsgang: "Industriemechaniker/-in"
curriculare_vorgabe: "RLP Industriemechaniker/-in, LF 6"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
# optional:
bereich: planung            # planung | pruefen
vertraulich: false          # true bei unveröffentlichten Prüfungsvorschlägen o. Ä.
---
```

**Pflichtabschnitte am Ende jedes Artefakts:**

1. `## Qualitätscheck` – Tabelle *Kriterium | Ergebnis (✅/⚠️/❌) | Hinweis*. Ein ❌ wird vor
   der Ausgabe behoben; was sich nicht beheben lässt, wird zu ⚠️ mit Begründung.
2. `## Annahmen und Prüfaufträge` – alle `⚠️ Annahme:` und alle `🔎 Prüfen:` (Normen,
   Grenzwerte, Rechtsvorgaben, Herstellerangaben, regionale Besonderheiten).
3. `## Übergabe` – kurze Stichpunkte für Folge-Skills (z. B. Handlungsergebnis, zentrale
   Kompetenzen, Dateinamen) und **empfohlene nächste Skills**.
4. Transparenzhinweis als letzte Zeile:
   `> KI-gestützt erstellt (Skill <name> v<version>). Fachliche Prüfung und Verantwortung: Lehrkraft.`
   Die verantwortliche Rolle darf passend zum Artefakt abweichen (z. B. Lehrkraft bzw.
   Bildungsgangteam, Lernende und Fachexpertin); die Zeile beginnt immer mit `> KI-gestützt`, nennt
   Skill und aktuelle Version und steht in **einer** Zeile.

Ausnahmen: **Teilartefakte** tragen Kopf und Pflichtabschnitte im zugehörigen Begleitblatt bzw.
Erwartungshorizont;
**Akten** (Planungsakte) führen einen Verlauf;
**Lektionen** im Kursprojekt folgen `vorlage-lektion.md`, falls vorhanden (Kopf für die Seitenausgabe).

## 4. Fachliche Redlichkeit

- **Nichts erfinden:** keine ausgedachten Normnummern, Paragrafen, Zitate, Studien,
  Grenzwerte, URLs oder Quellen. Unsicheres wird markiert: `[🔎 Norm prüfen]`,
  `[🔎 Wert prüfen]`. „Weiß ich nicht sicher" ist ein gültiges Ergebnis.
- **Rechnen statt schätzen:** Zahlenwerte in Aufgaben und Lösungen werden nachgerechnet,
  Einheiten mitgeführt. Ist ein Code-Werkzeug verfügbar, wird es dafür benutzt.
- **Quellenlage offenlegen:** Unterscheiden zwischen *aus gelieferten Unterlagen* und *aus
  allgemeinem Fachwissen*. Gelieferte Ordnungsmittel haben Vorrang.
- **Fiktive Akteure klar fiktiv:** Firmen, Personen und Adressen in Handlungssituationen
  sind erkennbar ausgedacht („(fiktiv)“ beim ersten Auftreten); keine echten Telefonnummern,
  keine realen Personen; E-Mail-Adressen nur mit Beispiel-Domains (`example.org`, RFC 2606).

## 5. Datenschutz

- Für Begutachtungen, Rückmeldungen und KI-Chatbots gelten zusätzlich die **Leitplanken**
  (`references/leitplanken-bewertung.md`, falls vorhanden): Datenschutzstufen 0–2, keine
  Bewertung einzelner Lernender durch KI, Freigabe durch die Lehrkraft.
- Für Planung und Material werden **keine personenbezogenen Daten** gebraucht.
- Gibt die Lehrkraft Namen oder Leistungsdaten von Lernenden an, werden sie im Artefakt
  pseudonymisiert (S01, S02 …) und es folgt ein kurzer Hinweis.
- Keine Gesundheits-, Förder- oder Herkunftsangaben zu einzelnen Lernenden in Artefakten;
  Lerngruppen werden nur zusammenfassend beschrieben.

## 6. Begriffe und Bezugsrahmen

- Standard ist das **berufsbildende Schulwesen in Niedersachsen**. Für vollzeitschulische
  Bildungsgänge, besonders das **Berufliche Gymnasium** (Lerngebiete, Schuljahrgang,
  Notenpunkte, EPA), gilt zusätzlich `berufliches-gymnasium.md`, falls vorhanden. Verbindliche
  Begriffe nach **Leitlinie SchuCu-BBS 2024**: Handlungssituation, Handlungsergebnis,
  Handlungskompetenz mit **Fachkompetenz** (Wissen, Fertigkeiten) und **Personaler
  Kompetenz** (Sozialkompetenz, Selbständigkeit); vollständige Handlung in sechs Phasen
  (Informieren bzw. Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw.
  Kontrollieren · Reflektieren).
- **SchuCu-BBS 2024 ist verbindlich** (Entscheidung der Fachberatung, 19.10.2026): kein
  anderes Kompetenzmodell (etwa vier Dimensionen), keine anderen Phasen oder Begriffe. Eine
  Gliederung des Studienseminars oder der Schule darf gelten; ihre Abschnitte werden mit den
  Begriffen der Leitlinie gefüllt. Vorgaben anderer Länder übernehmen die Skills nicht.
- **Vollständige Handlung und Lernzeit**: Der
  Handlungskreis wird je Lernsituation geschlossen, aber nicht zwingend in 90 Minuten – er
  darf mehrere Unterrichtseinheiten umfassen (Entscheiden, Überprüfen mit Überarbeitung und
  Reflektieren der Lernsituation bleiben immer). Fachsystematische, lehrkraftgeführte
  Lernphasen sind zulässig, wo zweckdienlich und begründet; die Begründung wird dokumentiert
  (`lernsituationsmuster.md` Abschn. 12, falls vorhanden).
- **Didaktische Leitidee** (Planungshilfe der Bibliothek):
  `didaktische-leitidee.md`, falls vorhanden. Ein bis zwei Sätze, welche übertragbare Einsicht
  die Lernenden am exemplarischen Fall gewinnen und warum sie bedeutsam ist – für die
  Lernsituation (unter *didaktisch-methodische Kommentare*) und für die Stunde (vor dem
  Stundenziel). Sie ergänzt die Begriffe der Leitlinie und ersetzt keinen.
- Sprache: sachlich, geschlechtergerecht („Schülerinnen und Schüler", Abkürzung „SuS").
- Kompetenzen und Ziele werden mit **beobachtbaren Operatoren** formuliert
  (`references/operatoren-afb.md`, falls vorhanden). Nicht verwenden: *verstehen, kennen,
  wissen, lernen, sich bewusst sein*.

## 7. Selbstprüfung

Vor der Ausgabe prüft der Skill sein Ergebnis gegen die eigene Checkliste **und** gegen
diesen Vertrag (Annahmen markiert? Nichts erfunden? Pflichtabschnitte vorhanden? Material für
Lernende kurz, offen gestellt, anschaulich, ohne Dekoration? Jede Zeichnung als SVG aus einer
Spec, keine Zeichnung aus Zeichen – `zeichnungen_pruefen.py`, falls vorhanden?), behebt Mängel und
gibt erst dann aus.

## 8. Plattformen

- **Claude (Skills aktiviert):** Ordner als Skill installieren; Claude lädt ihn bei Bedarf.
- **Assistenten ohne Skill-Funktion (z. B. AIS-Chat.schule, fobizz):** Inhalt von
  `SKILL.md` als Anweisung des Assistenten einfügen, Dateien aus `references/` und
  `assets/` als Wissensbasis hochladen. Die Planungsakte wird dann von Hand zwischen den
  Assistenten weitergegeben.
- **Chatbots für Lernende** (Moodle-KI-Chat, AIS.chat-Lernszenario) bekommen keine
  Skill-Fassung, sondern eine eigene kurze Systemanweisung mit Probelauf (`ki-chatbot-einrichten`,
  im AIS-Paket `agiles-lernen-mit-ki`).

## Anhang: references/taxonomie-matrix.md

# Revidierte Bloom-Taxonomie (Anderson/Krathwohl 2001) – Arbeitsreferenz

## Inhalt
1. Kognitive Prozessdimension (6 Stufen, 19 Teilprozesse)
2. Wissensdimension (A–D)
3. Beispiele Metalltechnik je Stufe
4. Hebel: Aufgaben gezielt anheben
5. Typische Fehleinordnungen

---

## 1. Kognitive Prozessdimension

| Stufe | Teilprozesse (Anderson/Krathwohl) | Kernfrage | Typische Operatoren |
|---|---|---|---|
| **1 Erinnern** | Wiedererkennen, Abrufen | Kann ich es wiedergeben? | nennen, angeben, aufzählen, bezeichnen |
| **2 Verstehen** | Interpretieren, Veranschaulichen, Klassifizieren, Zusammenfassen, Schlussfolgern, Vergleichen, Erklären | Kann ich es mit eigenen Worten erklären? | beschreiben, erklären, erläutern, zuordnen, zusammenfassen |
| **3 Anwenden** | Ausführen (vertraute Aufgabe), Implementieren/Durchführen (neue Aufgabe mit bekanntem Verfahren) | Kann ich das Verfahren einsetzen? | berechnen, anwenden, durchführen, erstellen nach Vorgabe |
| **4 Analysieren** | Differenzieren, Organisieren, Attribuieren | Kann ich zerlegen, Ursachen finden, Strukturen erkennen? | analysieren, untersuchen, vergleichen (kriteriengeleitet), Fehler suchen, auswerten |
| **5 Bewerten** | Überprüfen, Beurteilen | Kann ich nach Kriterien urteilen? | prüfen, beurteilen, bewerten, begründet entscheiden |
| **6 Erschaffen** | Generieren (Hypothesen), Planen, Produzieren | Kann ich etwas Neues entwickeln? | entwickeln, entwerfen, konstruieren, planen (offen), optimieren |

Hinweis: Anderson/Krathwohl führen *Vergleichen* als Teilprozess von **Verstehen** (einfache
Entsprechungen erkennen). Ein **kriteriengeleiteter** Vergleich mit Schlussfolgerung
(z. B. zweier Fügeverfahren für einen Auftrag) ist **Analysieren**.

## 2. Wissensdimension

| Wissensart | Untertypen | Beispiel Metalltechnik |
|---|---|---|
| **A Faktenwissen** | Terminologie, Einzelheiten | Bezeichnung eines 5/2-Wegeventils, Kurzzeichen S235JR |
| **B Konzeptwissen** | Klassifikationen, Prinzipien, Modelle, Theorien | Prinzip der Kraftübersetzung, Gefügeumwandlung beim Härten |
| **C Prozedurales Wissen** | fachspezifische Fertigkeiten/Algorithmen, Methoden, Kriterien für den Methodeneinsatz | Fehlersuchstrategie, Prüfplan erstellen, Wahl des Messmittels |
| **D Metakognitives Wissen** | strategisches Wissen, Wissen über Aufgabenanforderungen, Selbstwissen | eigenes Vorgehen bei der Fehlersuche reflektieren und verbessern |

## 3. Beispiele Metalltechnik (Thema: Pneumatischer Ausschiebezylinder)

| Stufe | Beispielaufgabe |
|---|---|
| 1 | Nennen Sie die Anschlussbezeichnungen eines 5/2-Wegeventils. |
| 2 | Erklären Sie, warum der Zylinder bei Druckabfall nicht mehr vollständig ausfährt. |
| 3 | Berechnen Sie die Kolbenkraft bei 6 bar und 32 mm Kolbendurchmesser (Wirkungsgrad 0,85). |
| 4 | Analysieren Sie das Weg-Schritt-Diagramm und ermitteln Sie die Ursache für den ausbleibenden Rückhub. |
| 5 | Beurteilen Sie, ob ein einfachwirkender oder doppeltwirkender Zylinder für den Auftrag besser geeignet ist (Kriterien: Kraft, Luftverbrauch, Sicherheit, Kosten). |
| 6 | Entwickeln Sie eine Steuerung, die das Werkstück nur ausschiebt, wenn die Lichtschranke frei ist und der Not-Halt nicht betätigt wurde; dokumentieren Sie den Schaltplan. |

## 4. Hebel: Aufgaben gezielt anheben

| Von → nach | Hebel | Vorher | Nachher |
|---|---|---|---|
| 1 → 2 | Erklärung statt Aufzählung | Nennen Sie drei Schweißverfahren. | Erklären Sie, warum beim WIG-Schweißen kein Flussmittel nötig ist. |
| 2 → 3 | auf neuen Fall übertragen | Beschreiben Sie das Vorgehen beim Anreißen. | Reißen Sie das Werkstück nach Zeichnung Nr. 2 an und begründen Sie die Bezugskante. |
| 3 → 4 | Fehler finden statt Lösung reproduzieren | Berechnen Sie die Drehzahl. | Prüfen Sie die Berechnung des Kollegen, finden Sie den Fehler und erklären Sie seine Folge für die Standzeit. |
| 3/4 → 5 | Alternativen + Kriterien + Entscheidung | Beschreiben Sie zwei Sicherungsmittel für Schrauben. | Entscheiden Sie begründet, welches Sicherungsmittel für die vibrierende Pumpe geeignet ist. |
| 5 → 6 | Lösung selbst entwerfen / optimieren | Bewerten Sie die vorgegebene Vorrichtung. | Entwerfen Sie eine Spannvorrichtung, die die Rüstzeit halbiert, und begründen Sie Ihre Konstruktion. |
| beliebig → D | Metakognition ergänzen | – | Beschreiben Sie, an welcher Stelle Ihre Fehlersuche ins Stocken kam und was Sie beim nächsten Mal anders machen. |

Weitere Hebel: Kriterien von den SuS entwickeln lassen · unvollständige oder widersprüchliche
Informationen geben (echte Problemdefinition) · Rollenwechsel (Kunde beraten, Auftrag
ablehnen begründen) · „Was wäre, wenn …?"-Variationen.

## 5. Typische Fehleinordnungen

| Muster | Warum falsch | Richtige Einordnung |
|---|---|---|
| „Beurteilen Sie, ob …" mit eindeutig auswendig gelernter Antwort | kein Urteil nach Kriterien | 1 Erinnern |
| „Analysieren Sie" bei im Unterricht bereits besprochenem Fall | Wiedergabe der Analyse | 1–2 |
| „Entwickeln Sie" mit Schritt-für-Schritt-Anleitung | Verfahren vorgegeben | 3 Anwenden |
| „Beschreiben Sie den Fehler im Schaltplan" | Fehlersuche ist Analyse | 4 Analysieren |
| Rechenaufgabe mit unbekanntem Lösungsansatz und selbst zu wählenden Größen | Problemdefinition nötig | 4–6 |

## Anhang: references/weitere-taxonomien.md

# Weitere Taxonomien – wann welche?

| Lernziel betrifft … | Taxonomie | Einsatz in der BBS |
|---|---|---|
| Denken, Wissen | Bloom revidiert (Anderson/Krathwohl 2001) | Standard für Aufgaben und Fachkompetenz |
| Haltungen, Werte | affektiv (Krathwohl, Bloom, Masia 1964) | Arbeitssicherheit, Qualitätsbewusstsein, Kundenorientierung – Personale Kompetenz |
| Handgriffe, Werkstattpraxis | psychomotorisch (Dave 1970) | Fertigungs-, Montage-, Prüfaufgaben |
| Tiefe des Verstehens | SOLO (Biggs/Collis 1982) | Bewertung offener Antworten, Erwartungshorizonte |

## Bloom original (1956) vs. revidiert (2001)

| Original (Substantive) | Revidiert (Verben) |
|---|---|
| Wissen | Erinnern |
| Verstehen | Verstehen |
| Anwendung | Anwenden |
| Analyse | Analysieren |
| Synthese | Erschaffen (jetzt **Stufe 6**) |
| Evaluation | Bewerten (jetzt **Stufe 5**) |

Ältere Unterlagen mit „Synthese" und „Evaluation" lassen sich so umschlüsseln. Die revidierte
Fassung ergänzt die Wissensdimension (A–D).

## Affektive Taxonomie (Krathwohl, Bloom, Masia 1964)

| Stufe | Bedeutung | Beispiel Arbeitssicherheit |
|---|---|---|
| 1 Aufnehmen | aufmerksam werden, wahrnehmen | Die SuS nehmen Sicherheitshinweise an der Maschine wahr. |
| 2 Reagieren | sich aktiv beteiligen, Regeln befolgen | Die SuS tragen die vorgeschriebene PSA ohne Aufforderung. |
| 3 Werten | einem Wert Bedeutung beimessen, dafür eintreten | Die SuS weisen Mitschüler auf fehlende Schutzbrillen hin. |
| 4 Organisation | Werte ordnen, Konflikte zwischen Werten abwägen | Die SuS wägen Zeitdruck gegen Sicherheitsregeln begründet ab. |
| 5 Charakterisierung durch Werte | Wert prägt das Handeln dauerhaft | Die SuS handeln auch unbeobachtet konsequent sicherheitsbewusst. |

Affektive Ziele sind schwer prüfbar; im Unterricht über **Beobachtungsbögen, Reflexion und
Selbsteinschätzung** erfassen, nicht über Klassenarbeiten.

## Psychomotorische Taxonomie (Dave 1970)

| Stufe | Bedeutung | Beispiel Feilen/Montieren |
|---|---|---|
| 1 Imitation | Vorgemachtes nachahmen | Feilhaltung nach Vorführung einnehmen |
| 2 Manipulation | nach Anleitung selbst ausführen | Fläche nach Arbeitsplan planfeilen |
| 3 Präzision | genau, ohne Hilfe, Fehler selbst bemerken | Maß ±0,1 mm einhalten und selbst prüfen |
| 4 Handlungsgliederung | mehrere Fertigkeiten koordinieren | Baugruppe fertigen, fügen, prüfen in sinnvoller Reihenfolge |
| 5 Naturalisierung | routiniert, situationsangepasst, effizient | Montage unter Zeitvorgabe mit eigener Optimierung |

## SOLO-Taxonomie (Biggs/Collis 1982) – für Erwartungshorizonte

| Stufe | Antwortqualität |
|---|---|
| prästrukturell | Thema verfehlt, unzusammenhängend |
| unistrukturell | ein relevanter Aspekt |
| multistrukturell | mehrere Aspekte, unverbunden |
| relational | Aspekte sinnvoll verknüpft, Zusammenhang erklärt |
| erweitert abstrakt | verallgemeinert, auf neue Fälle übertragen |

SOLO eignet sich, um bei Freitextaufgaben die Punktstufen eines Erwartungshorizonts zu
beschreiben (z. B. 1 P. unistrukturell … 4 P. relational).
