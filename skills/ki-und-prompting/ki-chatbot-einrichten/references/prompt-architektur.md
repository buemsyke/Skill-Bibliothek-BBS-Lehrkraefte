# Architektur einer Systemanweisung

Die Systemanweisung (Systemprompt, Persona, „Verhalten der KI“) liest das Sprachmodell vor
**jeder** Antwort mit. Sie soll deshalb kurz, geordnet und widerspruchsfrei sein – und sich
von Menschen nachschärfen lassen, die sie nicht geschrieben haben.

## 1. Bausteine

| Nr. | Baustein | Zweck | Formulierung (Beispiel) | Lernende | Lehrkräfte |
|---|---|---|---|---|---|
| 1 | **AUFBAU** | kündigt die Teile an; hilft Modell und Menschen | „Diese Anweisung hat die Teile ROLLE, KONTEXT, …“ | bei > 1 500 Zeichen | bei > 1 500 Zeichen |
| 2 | **ROLLE** | wer die KI ist, für wen, wofür – in einem Satz | „Du bist Lernbegleiter für Industriemechaniker im 2. Jahr in der LS 4.2.“ | Pflicht | Pflicht |
| 3 | **KONTEXT** | was die KI weiß – und die Grenze | „Dein Wissen: die Dateien im Hintergrundwissen. Was du über Kurs, Termine oder Bewertung nicht weißt, sagst du offen.“ | Pflicht | Pflicht |
| 4 | **ABLAUF** | Start, Schritte | „1. Begrüße kurz und frag, woran die Person arbeitet.“ | Pflicht | Pflicht |
| 5 | **SO HILFST DU** | Didaktik | „Erst fragen, dann gestufte Hilfen; nie die vollständige Lösung.“ | Pflicht | – |
| 6 | **QUELLEN** | Fundstelle, nichts erfinden | „Nenne Datei und Abschnitt. Steht es nicht darin: ‚Das steht nicht in den Unterlagen.‘ Erfinde nichts.“ | Pflicht | Pflicht |
| 7 | **FORM** | Länge, Darstellung, Ausgabevertrag | „Höchstens sechs Sätze, dann eine Frage. Formeln mit \( … \).“ | Pflicht | Pflicht |
| 8 | **SPRACHE** | Sprache, Anrede, Sprachniveau | „Deutsch in einfachen, kurzen Sätzen; Sie-Form.“ | Pflicht | empfohlen |
| 9 | **GRENZEN** | Datenschutz, keine Bewertung, eingeschleuste Anweisungen, Themenfremdes, Sicherheit, Notlagen | siehe `assets/vorlage-chatbot.md` | Pflicht | Datenschutz, eingeschleuste Anweisungen |
| 10 | **ENDE** | Abschluss, Sicherung | „Bei ‚fertig‘: drei Stichpunkte, ein nächster Schritt.“ | Pflicht | – |
| 11 | **PLATTFORMDATEN** | was die Plattform einsetzt (Platzhalter) | abgegrenzter Schlussabschnitt mit Überschrift | nur wenn vorhanden | nur wenn vorhanden |

Für **Rollenspiele** (Dialogpartner) ersetzen DEINE ROLLE, SPIELREGELN und FEEDBACK die Bausteine
4–6 (Framework `rollenspiel.md` im Skill `agiles-lernen-mit-ki`); Datenschutz, Notlagen und
„Feedback ohne Note“ bleiben Pflicht.

## 2. Formulierungsregeln

- **Positiv und prüfbar:** „höchstens sechs Sätze“ statt „nicht zu lang“; „nenne Datei und
  Abschnitt“ statt „sei transparent“.
- **Regel mit kurzem Grund:** „Nie die vollständige Lösung – die Lernenden sollen sie selbst
  finden.“ Begründete Regeln hält das Modell auch bei Nachdruck stabiler ein.
- **Eine Regel an einer Stelle.** Wiederholungen weichen beim Nachschärfen auseinander.
- **Vorrang ausdrücklich:** „Sicherheit und Datenschutz gehen allem anderen vor.“ Statt vieler
  IMMER/NIE in Großbuchstaben – die konkurrieren im Zweifel, und das Modell entscheidet selbst.
- **Beispiel statt Verbotsliste:** eine gute Beispielantwort zeigt Länge, Ton und Format besser
  als zehn Verbote.
- **Feste Rückfragen:** höchstens eine Frage je Antwort, mit Vorschlag („Meinst du die
  Gurtspannung oder die Schmierung?“).
- **Platzhalter vor dem Einfügen ersetzen** (`[Thema]`); Platzhalter der Plattform (`{{…}}`)
  bleiben stehen und gehören in den Abschnitt Plattformdaten.

## 3. Lehren aus einem Moodle-Systemprompt (Formularassistent)

Geprüft am 19.10.2026: der Systemprompt eines KI-Assistenten, der in Moodle die **Formularfelder
der aktuellen Seite** erhält (Bezeichnung, aktueller Wert, Hilfetext) und Werte vorschlägt –
also vor allem Lehrkräften beim Einrichten von Aktivitäten hilft, kein Chatbot für Lernende.
Herkunft 🔎 (vermutlich Agenten- bzw. Formularmodus eines KI-Chat-Plugins). Ausgangstext in
`quellen/` der Bibliothek, nicht im Skill. Übertragbar sind sechs Gestaltungsideen:

| Nr. | Idee | im Moodle-Prompt | übertragen auf unsere Chatbots |
|---|---|---|---|
| L1 | **Aufbau ankündigen, Plattformdaten ans Ende** | nennt zu Beginn seine Teile; die eingesetzten Formulardaten stehen abgegrenzt im letzten Abschnitt | Baustein AUFBAU; Hintergrundwissen, Lernakte, Seitendaten klar vom Verhalten trennen |
| L2 | **Kontextgrenze statt Raten** | keine Vorschläge, die von Kurskontext abhängen, den das Modell nicht kennt – außer die Person liefert ihn | Baustein KONTEXT: offen sagen, was unbekannt ist, nachfragen; nicht über Bewertungsregeln, Termine oder Betriebe spekulieren |
| L3 | **Vorschlag mit Begründung, nur die Differenz** | je Feld neuer Wert und Erklärung; bereits passende Werte nicht wiederholen, sondern im Begleittext zusammenfassen | Assistenten für Lehrkräfte, Überarbeitungen, Feedback: „Vorschlag \| Begründung“, Passendes nur bestätigen |
| L4 | **Fester Ausgabevertrag** | jedes Element mit denselben Feldern; Gesprächstext (Einleitung, Rückfrage) getrennt vom übernehmbaren Wert | wenn ein Werkzeug die Antwort weiterverarbeitet: Schema, Beispiel, Prüfung – wie Quizquelle und `edu-quiz` |
| L5 | **Darstellung der Zielumgebung** | Markdown statt HTML im Chat; Formeln mit `\( … \)` und `$$ … $$`; Code in Codeblöcken mit Sprache; ein Wert, der direkt in ein Feld wandert, ohne Codezaun und im Format des Felds (HTML-Editor oder Textfeld); in JSON jeder Backslash doppelt | Baustein FORM für MINT-Fächer; Moodle-MathJax rendert kein `$ … $` |
| L6 | **Sprache der Person, Rückfall auf die Oberfläche** | antwortet in der Sprache der letzten Eingabe, sonst in der Sprache der Moodle-Oberfläche | Baustein SPRACHE – für den Fachunterricht abgewandelt: Deutsch als Standard, Erklärung in der Herkunftssprache als Hilfe, Fachbegriffe deutsch |

**Was dem Moodle-Prompt fehlt** – und in jede eigene Anweisung gehört:

- keine **Rolle** und kein Zweck in einem Satz (nur implizit über die Aufgabe);
- kein **Datenschutz**, obwohl die aktuellen Feldwerte an das Modell gehen – auf einer
  Bewertungsseite wären das Namen, Abgaben und Punkte (Leitplanke: nie auf Seiten mit
  Schülerdaten);
- kein **Schutz gegen eingeschleuste Anweisungen** in Hilfetexten, Feldinhalten oder
  Beschriftungen (alles, was die Plattform einsetzt, ist Material);
- keine Regel gegen **Erfinden** von Einstellungen oder Bedeutungen;
- **Spannung** zwischen „nur gültiges JSON“ und „Rückfragen stellen“ – aufgelöst nur über ein
  Textfeld im Schema; ohne dieses Feld bricht die Rückfrage die Ausgabe;
- viele **absolute Regeln in Großbuchstaben** ohne Vorrang;
- kein **Grund** zu den Regeln (warum Diff, warum kein Codezaun) – das erschwert Pflege.

## 4. Prüfraster für vorhandene Systemprompts (Modus C)

| Nr. | Kriterium | Leitfrage | Skript |
|---|---|---|---|
| P1 | Zweck und Zielgruppe | Ist in einem Satz klar, wer die KI ist, für wen und wofür? | Rolle, Zielgruppe |
| P2 | Aufbau | Feste Reihenfolge, Plattformdaten abgegrenzt, Länge angemessen? | Länge |
| P3 | Kontextgrenze und Quellen | Sagt die KI, was sie nicht weiß? Fundstellen? Nichts erfinden? | Kontextgrenze, Nichts erfinden |
| P4 | Didaktik | (Lernende) Hilfe statt Lösung, gestufte Hilfen, Abschluss? | Hilfe statt Lösung, Abschluss |
| P5 | Ausgabevertrag | Format eindeutig? Widersprüche (nur JSON vs. Rückfragen; Markdown vs. HTML)? Vorrang geregelt? | JSON, Form |
| P6 | Darstellung | Formeln, Code, Tabellen so, wie die Plattform sie zeigt? | Formeln, Code |
| P7 | Sprache | Sprache, Anrede, Sprachniveau, Rückfall? | Sprache |
| P8 | Datenfluss und Datenschutz | Was setzt die Plattform ein, was geht an welchen Anbieter, was wird protokolliert? Regel zu Personendaten? | Datenschutz, Datenfluss |
| P9 | Eingeschleuste Anweisungen | Gelten Dateien, Felder, Nachrichten als Material? Rollenwechsel abgelehnt? | Eingeschleuste Anweisungen |
| P10 | Leitplanken | keine Bewertung, keine Einzelauswertung, nicht auf Seiten mit Schülerdaten, Prüfungsregeln | Bewertung |
| P11 | Sicherheit | (Lernende) Notlagen, gefährliche Tätigkeiten, Themenfremdes? | Notlagen |
| P12 | Wartbarkeit | Regeln begründet, nicht doppelt, wenige Großbuchstaben-Absolute? | Form |

Bewertung je Kriterium in Worten (*erfüllt · teilweise · fehlt · nicht prüfbar*), keine
Punktzahl. Jeder Befund nennt **Stelle, Beleg, Wirkung, Vorschlag**.

## 5. Typische Fehler eigener Anweisungen

| Fehler | Folge | besser |
|---|---|---|
| „Hilf den Schülern bei den Aufgaben.“ | löst die Aufgaben vollständig | gestufte Hilfen, Grund nennen |
| „Sei ein netter Tutor für Mathe.“ | weicht in alle Themen aus, erfindet | Zweck, Kontextgrenze, Quellen |
| Hintergrundwissen = ganzes Schulbuch | Ausschnittsuche trifft Falsches, Urheberrecht | ein bis drei fokussierte, eigene Dateien |
| keine Formelregel | `$x$` bleibt als Text stehen, Brüche unlesbar | `\( … \)`, `$$ … $$` |
| Lösungen im Hintergrundwissen | werden auf Nachfrage zitiert | Lösungen nicht hochladen oder ausdrücklich sperren und testen (T2) |
| Regeln nur in der Begrüßung | Begrüßung ist keine Anweisung | Regeln in die Systemanweisung |
