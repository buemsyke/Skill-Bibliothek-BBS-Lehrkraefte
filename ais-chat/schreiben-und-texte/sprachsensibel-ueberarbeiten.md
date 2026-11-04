<!-- Assistenten-Fassung des Skills 'sprachsensibel-ueberarbeiten'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
# Material sprachsensibel überarbeiten

## Zweck
Sprache darf nicht zur Hürde für Fachlernen werden – und Fachsprache bleibt Lernziel.
Der Skill macht Material **zugänglich** und baut gleichzeitig **sprachliche Handlungsfähigkeit
im Beruf** auf.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Drei Modi

| Modus | Wann | Ergebnis |
|---|---|---|
| **A Überarbeiten** (Standard) | selbst erstelltes Material (Arbeitsblatt, Infotext, Aufgabe) | sprachsensible Fassung + Sprachhilfen + Änderungsprotokoll |
| **B Hilfen ergänzen** | authentische Dokumente (Betriebsanleitung, Norm, Datenblatt, Prüfungsaufgabe) oder Original soll bleiben | Original unverändert + Lesehilfen, Wortspeicher, Leseauftrag |
| **C Analysieren** | „Wo sind die sprachlichen Hürden?" | Hürdenbericht mit Lesbarkeitswerten und Prioritäten |

## Eingaben
- **Pflicht:** das Material (Datei/Text).
- **Wichtig, sonst Annahme:** Zielgruppe (Standard: heterogene Berufsschulklasse mit
  einzelnen SuS mit Deutsch als Zweitsprache, Orientierung etwa GER B1), Fachbegriffe, die
  verbindlich gelernt werden sollen, Einsatzform (Papier, LMS, mündlich).
- **Optional:** Sprachstandsinformationen (zusammengefasst, ohne Namen), Vorgaben der Schule.

## Leitlinien (verbindlich)
1. **Fachinhalt bleibt identisch.** Keine fachliche Aussage geht verloren oder wird ungenau.
2. **Fachsprache bleibt – wird aber eingeführt.** Fachbegriffe nicht durch Alltagswörter
   ersetzen, sondern beim ersten Auftreten erklären und im Wortspeicher sichern.
3. **Einfache Sprache, nicht Leichte Sprache.** Leichte Sprache (eigenes Regelwerk) nur auf
   ausdrücklichen Wunsch.
4. **Authentisches bleibt authentisch** (Modus B). Im Beruf zählt das Original.
5. **Operatoren bleiben** (prüfungsrelevant) und werden über Operatorkarten erschlossen.
6. **Unterstützen statt ersetzen (Scaffolding):** Hilfen so bauen, dass sie später wegfallen
   können (Makro-Scaffolding: Aufgabenfolge, Mikro-Scaffolding: Impulse, Satzmuster).
7. **Darstellungsformen wechseln:** Text ↔ Tabelle ↔ Bild ↔ Schema – ein Wechsel ist oft die
   beste Vereinfachung (Leisen).
8. **Für Laien übersetzen, wo der Beruf es verlangt.** Enthält das Material Beratung, Übergabe
   oder Einweisung, kommt die Gegenrichtung hinzu: Fachsprache → Kundensprache, richtig und ohne
   Fachjargon (Leitfaden Abschn. 7). Im schriftlichen Bericht bleibt der Fachbegriff. Dasselbe
   gilt für **Laienpublikum** in Schulungsunterlagen, Bürgerdialog, Anhörung oder Präsentation
   vor Auftraggebern (z. B. Technikfolgenabschätzung im Beruflichen Gymnasium): verständlich,
   belegt, Unsicherheiten offen benannt.
9. **Kürzen vor Ergänzen** (`references/schuelermaterial.md`): Die sprachsensible Fassung ist
   nicht länger und nicht kleinschrittiger als das Original. Eine Darstellung ersetzt Absätze;
   Sprachhilfen sind kompakt (Wortspeicher als Tabelle, gern mit Bild; je Operator ein
   Satzmuster) und erklären nicht in Prosa; keine Dekoration.

## Vorgehen (Modus A)
1. **Analysieren:** Hürden auf Wort-, Satz-, Text- und Aufgabenebene markieren
   (`references/sprachsensibel-leitfaden.md`). Optional Lesbarkeit messen:
   `python3 scripts/lesbarkeit.py DATEI.md` (auch .docx, .odt, .pdf; LIX, Satzlängen, lange Sätze, Nominalstil,
   Passiv-Hinweise).
2. **Fachbegriffe festlegen:** Welche müssen gelernt werden (bleiben + Wortspeicher), welche
   sind nur Ballast (ersetzen)?
3. **Überarbeiten** nach Leitfaden: kurze Sätze, ein Gedanke pro Satz, Aktiv, Verben statt
   Nominalketten, Partizipialattribute auflösen, Komposita bei Einführung gliedern, klare
   Gliederung, Operator hervorheben, eine Handlung pro Auftragssatz – ohne den Auftrag in
   Einzelschritte zu zerlegen (Schritte gehören in Hilfen); Überflüssiges streichen.
4. **Sprachhilfen ergänzen** (`references/sprachhilfen.md`): Wortspeicher (Artikel, Plural,
   typische Verbverbindungen), Satzbausteine zu den verwendeten Operatoren, ggf. Leseauftrag,
   Redemittel für Gespräche (Kundengespräch, Übergabe, Präsentation). Bei Beratung oder
   Einweisung: Wortspeicher mit Spalte Kundensprache und Redemittel für Einwände, Kosten und
   Einweisung; bei Anhörung und Bürgerdialog Redemittel, die **Bedenken ernst nehmen** statt sie
   „zu behandeln“ (Abwägen, Unsicherheit benennen, Gegenposition wiedergeben).
5. **Abgleichen:** Fachinhalt vorher/nachher vergleichen; Lesbarkeit erneut messen; Wortzahl
   und Form vorher/nachher mit `python3 scripts/schuelermaterial_pruefen.py ORIGINAL.md
   50_…_sprachsensibel.md` (Fließtext, Aufträge, Darstellungen).
6. **Protokoll** der wesentlichen Änderungen schreiben.

## Ausgabe
Datei `50_<originalname>_sprachsensibel.md` (Original nie überschreiben), Kopf nach
Skill-Vertrag. **Aufbau so, dass `schuelerseiten-veroeffentlichen` (`edu-seiten strip`) die
Schülerfassung ohne Nacharbeit erzeugt:**
1. `# <Titel>` – **Überarbeitete Fassung** (gleiche Struktur wie das Original) und
   **Sprachhilfen** (Wortspeicher, Satzbausteine, ggf. Leseauftrag, Redemittel) – Teil für Lernende,
   ohne `⚠️ Annahme:`
2. `# Lösungen und Erwartungshorizont` – Lehrerteil des Originals (überarbeitet oder Verweis)
3. `# Didaktische Hinweise` – **Änderungsprotokoll** (Stelle | vorher | nachher | Begründung),
   **Lesbarkeit** vorher/nachher mit Einordnung, **Hinweise für die Lehrkraft** (sprachliches
   Lernziel, Fachbegriffe zum Üben, mündliche Unterstützung), Annahmen zur Zielgruppe, danach
   die Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis)

## Qualitätscheck
- [ ] Fachliche Aussagen vollständig und unverändert korrekt?
- [ ] Verbindliche Fachbegriffe erhalten, eingeführt und im Wortspeicher?
- [ ] Sätze überwiegend kurz; keine Nominalketten und Schachtelsätze im Schülerteil?
- [ ] Jede Aufgabe: Operator hervorgehoben, eine Handlung pro Satz, Ergebnisform klar?
- [ ] Satzbausteine passen zu den verwendeten Operatoren?
- [ ] Authentische Dokumente im Original belassen (Modus B)?
- [ ] Bei Beratung/Einweisung: Kundensprache und Redemittel für Einwände vorhanden, fachlich
      nicht falsch vereinfacht?
- [ ] Keine Verniedlichung, kein Kindersprachton – erwachsenengerecht?
- [ ] Fassung nicht länger als das Original (Fließtext), Aufträge nicht kleinschrittiger,
      Sprachhilfen kompakt, keine Dekoration – `schuelermaterial_pruefen.py` ohne ❌?

## Beispielaufrufe
> „Überarbeite `40_material_arbeitsblatt-1_arbeitsplan.md` sprachsensibel. In der Klasse sind
> vier SuS mit Deutsch als Zweitsprache (ca. B1). Fachbegriffe Wartung, Inspektion,
> Instandsetzung müssen bleiben."

> „Hier ein Auszug aus der Betriebsanleitung. Nicht ändern – aber Lesehilfen und Wortspeicher
> dazu."

## Referenzen – wann lesen
- `references/sprachsensibel-leitfaden.md` – Hürden und Regeln auf Wort-, Satz-, Text-,
  Aufgabenebene mit Vorher/Nachher-Beispielen; Kundensprache (Abschn. 7). **Immer.**
- `references/sprachhilfen.md` – Wortspeicher (auch mit Kundensprache), Satzbausteine je
  Operator, Leseaufträge, Redemittel (auch Einwände, Kosten, Einweisung), Methodenwerkzeuge.
- `references/operatoren-afb.md` – Operatoren und Erwartungen.
- `references/schuelermaterial.md` – Material für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `scripts/schuelermaterial_pruefen.py` – Wortzahl und Form vorher/nachher.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
- `scripts/lesbarkeit.py` – optionale Messung (Python 3, ohne Zusatzpakete); liest Word/PDF über
  `scripts/text_lesen.py`.

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

## Anhang: references/sprachhilfen.md

# Sprachhilfen – Bausteine zum Einsetzen

## Inhalt
1. Wortspeicher
2. Satzbausteine je Operator
3. Leseauftrag und Lesestrategien
4. Redemittel für berufliche Gespräche
5. Methodenwerkzeuge (Auswahl nach Leisen)
6. Operatorkarte

---

## 1. Wortspeicher

| Fachbegriff | Artikel / Plural | Erklärung (einfach) | typische Verbindung | Bild/Symbol |
|---|---|---|---|---|
| Wartung | die / die Wartungen | Arbeiten, damit eine Anlage gut weiterläuft (reinigen, schmieren, nachstellen) | eine Wartung durchführen | [ABBILDUNG] |
| Inspektion | die / die Inspektionen | prüfen und messen, in welchem Zustand die Anlage ist | eine Inspektion machen | |
| Schmierstoff | der / die Schmierstoffe | Öl oder Fett, das die Reibung verringert | den Schmierstoff auftragen | |

Regeln: höchstens 8–12 Begriffe pro Material; nur Begriffe, die wirklich gebraucht werden;
Verb-Verbindungen sind oft wichtiger als Einzelwörter.

**Wortspeicher mit Kundensprache** (für Beratung, Übergabe, Einweisung; Leitfaden Abschn. 7):

| Fachbegriff | Bedeutung | So sage ich es der Kundin / dem Kunden |
|---|---|---|
| die Tragrolle, die Tragrollen | Rolle, die den Gurt im Obertrum trägt | „die kleinen Rollen, auf denen das Band läuft" |
| die Spannstation, die Spannstationen | Einrichtung, mit der die Gurtspannung eingestellt wird | „die Stelle, an der wir das Band straffer oder lockerer stellen" |

## 2. Satzbausteine je Operator

| Operator | Satzbausteine |
|---|---|
| beschreiben | Das Bauteil besteht aus … · Zuerst …, danach …, zum Schluss … · Auf dem Bild sieht man … |
| erklären | …, weil … · Das liegt daran, dass … · Dadurch … · Wenn …, dann … |
| erläutern | Ein Beispiel dafür ist … · Das bedeutet für die Praxis, dass … |
| vergleichen | Im Unterschied zu … ist … · Beide … · …, während … · Der wichtigste Unterschied ist … |
| begründen | Ich habe … gewählt, weil … · Dafür spricht, dass … · Deshalb … |
| beurteilen | Nach dem Kriterium … ist … besser geeignet, weil … · Insgesamt komme ich zu dem Ergebnis, dass … |
| prüfen | Der Sollwert ist …, der Istwert ist … · Die Abweichung beträgt … · Das Ergebnis ist (nicht) in Ordnung, weil … |
| analysieren (Fehlersuche) | Wir haben … geprüft. Ergebnis: … · Die Vermutung … ist ausgeschlossen, weil … · Dafür spricht der Befund … · Die Ursache ist …, denn … |
| reflektieren | Gut gelungen ist mir … · Schwierig war … · Beim nächsten Mal werde ich … |
| dokumentieren | Am [Datum] wurde … durchgeführt. · Festgestellter Mangel: … · Empfohlene Maßnahme: … |

## 3. Leseauftrag und Lesestrategien

**Vor dem Lesen:** Leseauftrag mit Ziel („Finden Sie im Wartungsplan alle Arbeiten, die nach
500 Stunden fällig sind.") · Überschriften und Bilder überfliegen · Vorwissen sammeln.
**Beim Lesen:** Schlüsselwörter markieren (max. 1 pro Satz) · unbekannte Wörter am Rand
notieren · Abschnitte mit eigenen Überschriften versehen.
**Nach dem Lesen:** Informationen in Tabelle übertragen · Kernaussagen in 3 Sätzen · Partner
fragt, Leser erklärt.

Für authentische Dokumente (Betriebsanleitung, Norm): Lesepfad angeben („Lesen Sie nur
Kapitel 7.2 und Tabelle 3"), Wortspeicher zum Auszug, Markierungshilfe.

## 4. Redemittel für berufliche Gespräche

**Übergabe an die Schichtleitung:** Ich übergebe Ihnen … · Wir haben folgende Arbeiten
durchgeführt: … · Dabei ist uns aufgefallen, dass … · Wir empfehlen …, weil … · Haben Sie noch
Fragen?
**Kundengespräch:** Guten Tag, ich bin … von der Firma … · Darf ich kurz erklären, was wir
gemacht haben? · Für Sie bedeutet das … · Achten Sie bitte darauf, dass …
**Präsentation:** Unser Auftrag war … · Wir sind so vorgegangen: … · Unser Ergebnis ist … ·
Offen ist noch …
**Rückfrage/Klärung:** Habe ich richtig verstanden, dass …? · Können Sie das bitte noch einmal
erklären?
**Ursache für Laien erklären:** Wir haben herausgefunden, warum … · Stellen Sie sich das so
vor: … · Das merken Sie daran, dass …
**Einwände aufgreifen:** Ich verstehe, dass Sie … möchten. · Das ist eine berechtigte Frage. ·
Wenn wir nur …, dann … · Deshalb schlagen wir vor, …
**Kosten und Nutzen:** Das kostet ungefähr … Dafür … · Nötig ist …, empfehlenswert ist
zusätzlich …
**Bedenken ernst nehmen (Anhörung, Bürgerdialog, Schulung):** Ihr Einwand trifft einen Punkt,
den auch unsere Prüfung bestätigt: … · Hier sind die Fachleute uneins: Die einen …, die anderen
… · Sicher wissen wir …; offen ist noch … · Damit die Folgen kleiner werden, schlagen wir vor …
· Wenn ich Sie richtig verstehe, ist Ihnen vor allem … wichtig. · Das sehe ich anders, weil …
– aber Ihr Argument zu … nehme ich mit.
**Fachsprache für Laien übertragen:** Fachbegriff + Alltagswort + Größenordnung im Vergleich
(„Infraschall – Töne unterhalb der Hörgrenze; am Wohnhaus so leise wie …“) – nur mit belegter
Zahl.
**Einweisen:** Bitte schauen Sie regelmäßig auf … Der Wert sollte … sein. · Wenn …, dann rufen
Sie uns bitte an, statt selbst … · Wir markieren Ihnen …

## 5. Methodenwerkzeuge (Auswahl nach Leisen)

| Werkzeug | Funktion | Beispiel |
|---|---|---|
| Wortgeländer | Stichwörter in richtiger Reihenfolge als Gerüst für eigene Sätze | Ablauf der Wartung beschreiben |
| Satzpuzzle | Satzteile zusammensetzen | Sicherheitsregeln formulieren |
| Bildsequenz | Bilder ordnen und beschriften | Arbeitsschritte der Montage |
| Lückentext (mit Wortkasten) | Fachbegriffe im Kontext anwenden | Infotext Schmierung |
| Kärtchentisch | Begriffe strukturieren und erklären | Grundmaßnahmen der Instandhaltung |
| Fragemuster | strukturierte Fragen an einen Text | Betriebsanleitung erschließen |
| Thesentopf | Aussagen bewerten, Meinung begründen | Weiterbetrieb oder Reparatur? |
| Filmleiste/Ablaufdiagramm | Prozess darstellen | Inbetriebnahme |

## 6. Operatorkarte

```markdown
**ERLÄUTERN** – Sie beschreiben etwas **und** machen es mit einem Beispiel oder einer
Begründung verständlich.
Beispiel: „Erläutern Sie, warum die Anlage vor dem Schmieren gesichert werden muss."
So kann Ihre Antwort beginnen: „Die Anlage muss gesichert werden, weil … Zum Beispiel …"
```

## Anhang: references/sprachsensibel-leitfaden.md

# Leitfaden: Sprachliche Hürden erkennen und abbauen

Grundlagen: J. Leisen (sprachsensibler Fachunterricht, Methoden-Werkzeuge, Darstellungsformen),
P. Gibbons (Scaffolding), Makro-/Mikro-Scaffolding (Kniffka). Sprachebenen: Alltagssprache →
Bildungssprache → Fachsprache. Ziel ist der Weg zur Fachsprache, nicht ihre Vermeidung. In
Beratung, Übergabe und Einweisung von Laien kommt die Gegenrichtung als berufliche Kompetenz
hinzu: Fachsprache → Kundensprache (Abschn. 7).

## Inhalt
1. Wortebene
2. Satzebene
3. Textebene
4. Aufgabenebene
5. Darstellungsformen wechseln
6. Lesbarkeit messen und einordnen
7. Fachsprache für Laien übersetzen (Kundensprache)
8. Grenzen

---

## 1. Wortebene

| Hürde | Vorher | Nachher |
|---|---|---|
| Fachbegriff ohne Einführung | Prüfen Sie die Gurtspannung. | Prüfen Sie die **Gurtspannung** (= wie straff der Gurt gespannt ist). |
| lange Komposita | Gurtspannstationseinstellung | Einstellung an der Spannstation des Gurtes · bei Einführung gliedern: Gurt·spann·station |
| Nominalisierung | Nach erfolgter Durchführung der Schmierung … | Nachdem Sie geschmiert haben, … |
| Funktionsverbgefüge | Die Maschine ist zum Stillstand zu bringen. | Schalten Sie die Maschine aus. |
| Abkürzungen | lt. BA ggf. n. i. O. melden | laut Betriebsanleitung; wenn nötig „nicht in Ordnung" melden |
| Synonymwechsel | Gurt … Band … Förderriemen | **einen** Begriff durchhalten |
| bildliche Wendungen | Das ist das A und O. | Das ist am wichtigsten. |

Fachwörter immer **mit Artikel und Plural** einführen: *die Spannstation, die Spannstationen*.
Typische Verbindungen mitlernen: *den Gurt spannen, die Spannung prüfen, den Schmierstoff
auftragen*.

## 2. Satzebene

Die Grenze von 20 Wörtern (`lesbarkeit.py`) ist bewusst strenger als der allgemeine Richtwert für
Material für Lernende (keiner über 25 Wörter, `schuelermaterial.md`): Die sprachsensible Fassung
soll unter beiden bleiben.

| Hürde | Vorher | Nachher |
|---|---|---|
| Satzlänge > 20 Wörter, Schachtelsatz | Bevor Sie mit der Wartung, die laut Herstellerangabe alle 500 Betriebsstunden durchzuführen ist, beginnen, sichern Sie … | Die Wartung ist alle 500 Betriebsstunden fällig. Sichern Sie die Anlage, bevor Sie beginnen. |
| Partizipialattribut | die vom Hersteller vorgeschriebene, regelmäßig durchzuführende Schmierung | die Schmierung. Der Hersteller schreibt sie vor. Sie muss regelmäßig erfolgen. |
| unpersönliches Passiv | Es ist zu prüfen, ob … | Prüfen Sie, ob … |
| Negationshäufung | Nicht ohne vorherige Sicherung beginnen. | Sichern Sie zuerst die Anlage. Beginnen Sie dann. |
| Konjunktiv/Modal unklar | Man sollte ggf. … | Wenn …, dann … |

Fachtextpassiv („Die Lager werden gefettet.") gehört zur Berufssprache: im Infotext
bewusst verwenden und im Wortspeicher als Muster zeigen – in Arbeitsaufträgen aktiv formulieren.

## 3. Textebene
- Überschrift als Frage oder Handlung; Kernaussage vorweg (2 Sätze).
- Ein Absatz = ein Gedanke; Zwischenüberschriften alle 3–5 Sätze.
- Reihenfolge im Text = Reihenfolge der Handlung.
- Signalwörter für Zusammenhänge: *zuerst, danach, deshalb, weil, im Unterschied zu*.
- Wichtiges als Liste oder Tabelle; Abbildung neben der zugehörigen Stelle.

## 4. Aufgabenebene
- **Operator** an den Satzanfang und fett: „**Erstellen** Sie …".
- Eine Handlung pro Satz; Teilaufgaben nummerieren – höchstens drei. Den Auftrag dabei nicht
  in Einzelschritte zerlegen: Ziel und Ergebnis bleiben ein Auftrag, Schritte gehören in die
  gestuften Hilfen (`schuelermaterial.md` Abschn. 3).
- Ergebnisform nennen: „… in die Tabelle", „… in 3 Sätzen", „… als Skizze".
- Keine versteckten Doppelaufträge („Nennen und begründen Sie …" → zwei Teilaufgaben, wenn
  beides bewertet wird).
- Bei Erstbegegnung mit einem Operator: Operatorkarte mit Beispiel bereitstellen.

## 5. Darstellungsformen wechseln (Leisen)
Bild ↔ Text ↔ Tabelle ↔ Diagramm ↔ Symbol/Formel ↔ gegenständliche Handlung. Ein Fließtext
über Schmierstoffe wird als Vergleichstabelle oft verständlicher; ein Ablauf als nummerierte
Bildfolge. Der Wechsel zurück (Tabelle → eigener Text) ist selbst eine sprachliche Übung.

## 6. Lesbarkeit messen und einordnen
`scripts/lesbarkeit.py` liefert u. a. den **Lesbarkeitsindex LIX** (Björnsson):
LIX = durchschnittliche Satzlänge in Wörtern + Anteil langer Wörter (mehr als 6 Buchstaben)
in Prozent.

| LIX | Einordnung (Richtwerte für deutsche Texte) |
|---|---|
| unter 40 | leicht |
| 40–50 | mittel |
| 50–60 | schwer (typische Sachtexte) |
| über 60 | sehr schwer (Fachliteratur) |

Fachtexte haben wegen langer Fachwörter immer einen erhöhten LIX. Aussagekräftiger ist die
**Veränderung** vorher/nachher und die **Liste langer Sätze**. Zahlen ersetzen nicht das Lesen.

## 7. Fachsprache für Laien übersetzen (Kundensprache)

Wo Lernende Kundschaft beraten, Anlagen übergeben oder Betreiber einweisen, müssen sie ihr
Fachwissen **ohne Fachjargon** erklären – eine eigene sprachliche Leistung, die geübt werden
will. Sie ersetzt die Fachsprache nicht: Im schriftlichen Bericht und im Fachgespräch bleibt der
Fachbegriff.

| Regel | Fachsprache | Kundensprache |
|---|---|---|
| Bild oder Vergleich statt Fachbegriff | Die Tragrolle ist festgegangen. | Eine der kleinen Rollen, auf denen das Band läuft, dreht sich nicht mehr. |
| Wirkung statt Funktionsprinzip | Ungleiche Spannung führt zu Schieflauf. | Das Band ist auf einer Seite lockerer und wandert deshalb zur Seite. |
| Zahl mit Bezug und Handlung | Prüfintervall 500 Bh | Alle sechs bis sieben Wochen schauen wir wieder nach. |
| Handlungsanweisung statt Norm | gemäß Betriebsanleitung Abschn. 7.2 | Bitte schalten Sie das Band aus, bevor Sie etwas daran anfassen. |
| Einwand ernst nehmen, dann Folge zeigen | – | Ich verstehe, dass es schnell gehen soll. Wenn wir nur nachspannen, läuft das Band in ein paar Tagen wieder schief. |

- **Nicht falsch vereinfachen:** Die Erklärung darf einfacher sein, aber nicht falsch.
- **Wortspeicher mit dritter Spalte** „So sage ich es der Kundin / dem Kunden"
  (`sprachhilfen.md` Abschn. 1); Redemittel für Einwände, Kosten und Einweisung
  (`sprachhilfen.md` Abschn. 4).
- Bewertungskriterium im Gespräch: „richtig und ohne Fachjargon erklärt".

## 8. Grenzen
- Leichte Sprache ist ein eigenes Regelwerk für bestimmte Zielgruppen – nur auf Wunsch.
- Prüfungsaufgaben der Kammern werden nicht vereinfacht; stattdessen Prüfungssprache üben.
- Übersetzungen in Herkunftssprachen können als zusätzliche Brücke dienen (Glossar
  zweisprachig), ersetzen aber nicht die deutsche Fachsprache. 🔎 Übersetzungen prüfen lassen.
