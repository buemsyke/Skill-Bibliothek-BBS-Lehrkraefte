---
artefakt: Lernsituation
titel: "Ticket-Tool für den IT-Support entwickeln und dem Team übergeben"
skill: lernsituation-dokumentieren
skill_version: "1.1"
stand: 2026-10-09
bildungsgang: "Fachinformatiker/-in, Fachrichtung Anwendungsentwicklung"
curriculare_vorgabe: "KMK-Rahmenlehrplan IT-Berufe, LF 5 Software zur Verwaltung von Daten anpassen 🔎"
dqr: 4
status: "Beispiel Modus B – überführt aus einer Lernsituation im KMK-Raster (Skill lernsituation-erstellen, eduwerkzeuge); fachlich zu prüfen"
---

# Lernsituation 5.2: Ticket-Tool für den IT-Support entwickeln und dem Team übergeben

## Rahmen

| Feld | Eintrag |
|---|---|
| Schule | BBS Musterstadt ⚠️ Annahme |
| Ausbildungsberuf / Bildungsgang | Fachinformatiker/-in, Fachrichtung Anwendungsentwicklung, Berufsschule (Teilzeit); berufsbezogener Lernbereich |
| Ansprechpartner/-in | [von der Lehrkraft einzutragen] |
| Curriculare Vorgaben | KMK-Rahmenlehrplan für die IT-Berufe, Lernfeld 5 |
| Ausbildungsjahr | 1. Ausbildungsjahr (die Vorlage nannte irrtümlich das 2. Jahr) |
| Zeitrichtwert Lernfeld | [laut RLP] 🔎 |
| Lernfeld | LF 5 „Software zur Verwaltung von Daten anpassen" 🔎 Titel wörtlich abgleichen |
| DQR-Niveau | Abschluss: Niveau 4 (3-jährige duale Ausbildung, DQR-Liste). Planungsentscheidung für das 1. Jahr: Entwurf und Umsetzung mit Code-Gerüst und Infoblättern weitgehend selbständig, Beurteilen nach vorgegebenen Testkriterien (Merkmale Niveau 3), Übergang zu Niveau 4 beim Begründen der Entwurfsentscheidungen. |
| Schulspezifische Entscheidungen | Blockunterricht; Leistungsbewertung je LS über Handlungsergebnis (Kriterienraster) und Präsentation ⚠️ Annahme |
| Lernumgebung | PC-Raum mit Python 3 und SQLite, Moodle-Kurs „LF 5" ⚠️ Annahme |

## Lernsituation

| Feld | Eintrag |
|---|---|
| Lernsituation | 5.2 – **Ticket-Tool für den IT-Support entwickeln und dem Team übergeben** |
| Zeitrichtwert Lernsituation | 20 Unterrichtsstunden |

### Handlungskompetenz

| Fachkompetenz | Personale Kompetenz |
|---|---|
| Die Schülerinnen und Schüler … | Die Schülerinnen und Schüler … |
| – analysieren den Auftrag und leiten funktionale Anforderungen an die Ticketverwaltung ab. | – teilen die Arbeit im Team nach Rollen auf und stimmen Schnittstellen verbindlich ab. |
| – entwerfen aus den Anforderungen ein relationales Datenmodell mit Datentypen und Primärschlüssel. | – planen ihr Vorgehen in Teilschritten und halten Absprachen zum Zwischenstand ein. |
| – legen eine SQLite-Datenbank an und führen Datenoperationen (anlegen, lesen, ändern, löschen) mit SQL aus. | – begründen ihre Entwurfsentscheidungen gegenüber der Auftraggeberin. |
| – implementieren die geforderten Funktionen in Python mit `sqlite3`, Funktionen, Verzweigungen und Fehlerbehandlung. | – reflektieren ihren Lösungsweg und leiten Verbesserungen für das nächste Projekt ab. |
| – testen die Anwendung systematisch mit selbst erstellten Testfällen und dokumentieren die Ergebnisse im Testprotokoll. | |
| – beurteilen ihre Lösung anhand der Anforderungen und benennen Erweiterungsmöglichkeiten. | |

*Methodische Fertigkeiten (Auftrag zerlegen, Testfälle entwerfen), Kommunikation und
Mediennutzung stecken in den Formulierungen von Fachkompetenz (Fertigkeiten) und Personaler
Kompetenz – keine eigenen Dimensionen (SchuCu-BBS 2024).*

### Handlungssituation

Sie sind Auszubildende oder Auszubildender bei der Nordlicht IT-Systeme GmbH (fiktiv). Der
Support nimmt Anfragen der Kundinnen und Kunden bisher per E-Mail an und führt eine
Excel-Liste. Anfragen gehen verloren, niemand weiß, welche Anfrage gerade wer bearbeitet, und
in der Teambesprechung gibt es regelmäßig Streit darüber, was „dringend" ist.

Die Teamleiterin Support, Frau Lindqvist, beauftragt Ihr Azubi-Team, ein einfaches Ticket-Tool
zu entwickeln: Mitarbeitende sollen Tickets anlegen, suchen und ihren Status ändern können;
die Daten sollen dauerhaft gespeichert werden. Welche Funktionen zuerst kommen und wie die
Bedienung aussieht, legen Sie im Team fest. In drei Wochen stellen Sie in der Teambesprechung
einen lauffähigen Prototyp vor und übergeben ihn mit einer Kurzdokumentation.

> **Ihr Auftrag:** Entwickeln Sie ein Ticket-Tool, das die Anfragen des Supports zuverlässig
> verwaltet, und übergeben Sie es so, dass das Team damit arbeiten kann.

*Material zur Situation:* E-Mail von Frau Lindqvist mit Anforderungen, anonymisierte
Beispiel-Anfragen (erfunden), Auszug aus der bisherigen Excel-Liste (erfunden).

### Handlungsergebnis

- lauffähige Python-Konsolenanwendung mit SQLite-Datenbank
- Kurzdokumentation (Datenmodell, Bedienung, bekannte Grenzen)
- Testprotokoll mit Testfällen, Soll- und Ist-Ergebnis
- Präsentation in der „Teambesprechung" mit begründeten Entscheidungen

Funktionsumfang und Bedienkonzept legen die Teams in der Phase „Entscheiden" selbst fest;
Mindestfunktionen: Ticket anlegen, Tickets anzeigen und suchen, Status ändern.

### Inhalte

- Anforderungsanalyse (vereinfachtes Lastenheft), funktionale Anforderungen
- relationales Datenmodell: Entität, Attribut, Datentyp, Primärschlüssel
- SQL: `CREATE TABLE`, `INSERT`, `SELECT … WHERE`, `UPDATE`, `DELETE`
- Python: Modul `sqlite3`, Funktionen, Menüführung, Fehlerbehandlung mit `try/except`
- parametrisierte Abfragen statt Zeichenkettenverkettung (Schutz vor SQL-Injection) –
  *didaktische Konkretisierung*
- Testfälle und Testprotokoll (Soll-Ist-Vergleich)
- Datenschutz bei Ticketdaten: nur erfundene Testdaten, Datensparsamkeit – *didaktische
  Konkretisierung*

*Auswahl und Reduktion:* Eine Tabelle `tickets` genügt für den Prototyp; Beziehungen zwischen
mehreren Tabellen (Mitarbeitende, Kunden) sind Erweiterung für schnelle Teams. Grafische
Oberflächen und Mehrbenutzerbetrieb werden bewusst ausgeklammert. 🔎 Abgleich, welche Inhalte
LF 5 und welche Nachbar-Lernfelder (z. B. Datenbereitstellung, Serviceanfragen) vorsehen
(`references/curriculum-abgleich.md`).

### Distanzunterricht

| Prüffrage (Leermaske) | Einschätzung |
|---|---|
| Ist die Handlungssituation für DU eindeutig, verständlich und ausreichend konkret? | ja – E-Mail und Beispieldaten liegen im Moodle-Kurs |
| Ist ggf. eine (modulare) Anpassung beschrieben? | Teamabsprachen per Videokonferenz; Code über eine schulische Plattform teilen |
| Kann das Handlungsergebnis im DU erreicht werden? | ja, wenn alle SuS Zugang zu einem Rechner mit Python haben 🔎 |
| Wurde das Handlungsergebnis angepasst? | im DU Präsentation als aufgezeichnete Kurzvorstellung (3 min) |

## Vereinbarungen und Hinweise zur Umsetzung

| … für | Hinweise |
|---|---|
| die Bildungsgangs- oder Fachgruppe | knüpft an Grundlagen der Programmierung an; Datenmodell wird in späteren Lernfeldern zu mehreren Tabellen erweitert 🔎 |
| Leistungsfeststellung und -bewertung | Kriterienraster (100 P): Datenmodell 10 · Funktionsumfang 25 · Datenbankzugriff 15 · Robustheit 10 · Code-Qualität 10 · Test und Doku 15 · Präsentation und Reflexion 15; Raster wird in der Phase Entscheiden offengelegt |
| Materialien und Quellen | Infoblatt SQL-Grundbefehle, Infoblatt `sqlite3` in Python, Vorlage Datenmodell, Vorlage Testprotokoll; offizielle Python-Dokumentation |
| Lernumgebung | PC-Raum; Moodle-Kurs „LF 5 – Ticket-Tool": Situation und Infoblätter als *Seite*, Vorlagen als *Datei*, Abgabe `ticket_tool.py` + Testprotokoll als *Aufgabe*, Sicherungsquiz SQL/Python als *Test*, *Forum* für technische Rückfragen |
| didaktisch-methodische Kommentare | **Leitidee:** Software wird für Menschen gebaut – erst wenn die Anforderungen des Supports als Testfälle feststehen, lässt sich zeigen, dass das Werkzeug zuverlässig hilft. · Teamarbeit mit Rollen (Datenbank, Programmlogik, Test/Doku), Rollenwechsel nach der Hälfte; Lehrkraft in der Rolle der Teamleiterin bei der Planbesprechung; Differenzierung: Code-Gerüst mit Funktionssignaturen und SQL-Bausteinen bzw. Zusatzauswertungen (Tickets je Status, älteste offene Tickets, CSV-Export); Stolperstein: SQL per Zeichenkettenverkettung |

## Phasenplanung (vollständige Handlung)

| Zeitrichtwert | Handlungsphase | Fachkompetenz | Personale Kompetenz | Medien/Materialien/Hinweise |
|---|---|---|---|---|
| ca. 4 Std. | Informieren bzw. Analysieren | analysieren den Auftrag, leiten Anforderungen ab; erarbeiten SQL- und `sqlite3`-Grundlagen | planen ihr Vorgehen in Teilschritten | E-Mail, Beispieldaten, Infoblätter, Sicherungsquiz |
| ca. 3 Std. | Planen | entwerfen Datenmodell, Funktionsliste und Menüstruktur | teilen die Arbeit nach Rollen auf | Vorlage Datenmodell |
| ca. 1 Std. | Entscheiden | legen Datenmodell, Funktionsumfang und Testkriterien fest | begründen Entscheidungen gegenüber der Teamleiterin | Planbesprechung, Kriterienraster |
| ca. 8 Std. | Durchführen | legen Datenbank an, implementieren Funktionen schrittweise | stimmen Schnittstellen ab, halten Zwischenstände ein | Editor/IDE, Python, SQLite, Code-Gerüst (optional) |
| ca. 2 Std. | Überprüfen bzw. Kontrollieren | testen mit eigenen Testfällen, beheben Fehler, beurteilen die Lösung an den Anforderungen | geben einem anderen Team kriteriengeleitet Rückmeldung | Vorlage Testprotokoll, Peer-Test |
| ca. 2 Std. | Reflektieren | benennen Erweiterungsmöglichkeiten | präsentieren den Prototyp, reflektieren Lösungsweg und Teamarbeit | Präsentation, Reflexionsbogen |
| **Σ 20 Std.** | | | | |

## Analysebogen – Selbstcheck

| Nr. | Kriterium | Einschätzung | Beleg / Hinweis |
|---|---|---|---|
| 1 | Kompetenzen aus curricularen Vorgaben | trifft eher zu | Abgleich mit dem Wortlaut der LF-5-Zielformulierung steht aus 🔎 |
| 2 | Personale Kompetenz konkretisiert | trifft zu | vier situationsbezogene Formulierungen |
| 3 | Fachkompetenz konkretisiert | trifft zu | sechs Formulierungen mit Gegenstand und Handlung |
| 4 | Inhalte aus curricularen Vorgaben | trifft eher zu | Konkretisierungen gekennzeichnet |
| 5 | Inhalte analysiert | trifft zu | Reduktion auf eine Tabelle begründet |
| 6 | initiiert Lernprozess | trifft zu | verlorene Anfragen, Streit um Dringlichkeit |
| 7 | trägt über die gesamte LS | trifft zu | Prototyp und Übergabe sind Teil der Situation |
| 8 | bedeutsam (berufsbezogen) | trifft zu | typischer interner Auftrag |
| 9 | greift Erfahrungen auf | trifft eher zu | eigene Erfahrungen mit Supportanfragen im Betrieb als Einstieg nutzen |
| 10 | zentrale Problemstellung | trifft zu | Anfragen zuverlässig verwalten |
| 11 | exemplarisch | trifft zu | übertragbar auf andere Datenverwaltungen |
| 12 | Rahmen benannt | trifft zu | fiktiver Betrieb, Support, Prototyp in drei Wochen |
| 13 | soziale Interaktion | trifft zu | Team, Planbesprechung, Präsentation |
| 14 | offene Lösungswege | trifft zu | Funktionsumfang, Bedienkonzept und Datenmodell offen |
| 15 | Ergebnis löst Problemstellung | trifft zu | lauffähiges Tool + Übergabe |
| 16 | Vereinbarungen vollständig | trifft zu | alle fünf Bereiche gefüllt |

## Änderungsliste (Modus B – Überführung)

| Vorher (KMK-Raster mit 11 Feldern) | Nachher (SchuCu-BBS 2024) |
|---|---|
| Handlungsprodukt | Handlungsergebnis (Prototyp, Doku, Testprotokoll, Präsentation) |
| Fach-, Methoden-, Sozial-, Selbstkompetenz | Fachkompetenz und Personale Kompetenz; Methodenkompetenz eingebettet |
| Ausgangssituation („euer Azubi-Team …") | Handlungssituation in Sie-Ansprache, mit Konflikt (Dringlichkeit), offener Funktionsauswahl und Übergabe |
| Phasen „Ausführen", „Bewerten/Reflektieren" | Durchführen · Überprüfen bzw. Kontrollieren · Reflektieren |
| Felder Material, Leistungsbewertung, Differenzierung, Anknüpfung Moodle | Vereinbarungen und Hinweise zur Umsetzung |
| – | neu: Distanzunterricht, Analysebogen, Kennzeichnung didaktischer Konkretisierungen |
| „2. Ausbildungsjahr", LF-Titel aus dem Gedächtnis | Ausbildungsjahr korrigiert (1. Jahr, von der Fachberatung bestätigt); Titel und Zeitrichtwert als Prüfauftrag markiert |
| Verweis auf eine Quiz-Datei außerhalb der Bibliothek | entfernt; Quiz als Moodle-Element beschrieben |

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Begriffe SchuCu-BBS 2024 | ✅ | Handlungsergebnis, 6 Phasen, Personale Kompetenz |
| Eine tragende Handlungssituation mit offenen Lösungswegen | ✅ | |
| Kompetenzen aktiv, niveaugerecht | ✅ | |
| Jede Kompetenz in einer Phase | ✅ | |
| Phasensumme = Zeitrichtwert | ✅ | 20 Std. |
| Bewertung mit offengelegten Kriterien | ✅ | Raster mit Punkten |
| Lernfeldangaben belegt | ⚠️ | Ausbildungsjahr bestätigt; Titel und Zeitrichtwert gegen den gültigen RLP prüfen |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: Blockunterricht, PC-Raum mit Python 3 und SQLite, Moodle-Kurs vorhanden.
- 🔎 Prüfen: Lernfeldtitel und Zeitrichtwert von LF 5 im gültigen RLP der IT-Berufe (Ausbildungsjahr: 1. Jahr, bestätigt).
- 🔎 Prüfen: Wortlaut der Zielformulierung; Kompetenzen ggf. an den Wortlaut angleichen.
- 🔎 Prüfen: Zugang aller SuS zu einem Rechner im Distanzunterricht.

## Übergabe

- Titel / Zeitrichtwert: Ticket-Tool für den IT-Support entwickeln und dem Team übergeben / 20 Std.
- Handlungssituation: Supportanfragen gehen verloren; Azubi-Team entwickelt einen Prototyp und übergibt ihn.
- Handlungsergebnis: Python-Anwendung mit SQLite, Kurzdoku, Testprotokoll, Präsentation.
- Kernkompetenzen: Anforderungen ableiten, Datenmodell entwerfen, SQL und `sqlite3` anwenden, systematisch testen, Entscheidungen begründen.
- Phasen: Inf 4 · Plan 3 · Entsch 1 · Durchf 8 · Überpr 2 · Refl 2.
- Empfohlene nächste Skills: `unterrichtsentwurf-erstellen` (Doppelstunde Planen: Datenmodell), `unterrichtsmaterial-erstellen` (Infoblätter, Vorlagen), `differenzierung-erstellen` (Hilfekarten Datenmodell), `klausur-erstellen` (Klassenarbeit am Ende des Lernfelds).

> KI-gestützt erstellt (Skill lernsituation-dokumentieren v1.1). Fachliche Prüfung und Verantwortung: Lehrkraft.
