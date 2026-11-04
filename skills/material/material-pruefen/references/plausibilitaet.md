# Plausibilitätscheck – Prüfliste

## Inhalt
1. Rechnungen
2. Einheiten und Größenordnungen
3. Lösbarkeit
4. Konsistenz
5. Realitätsnähe und Sicherheit
6. Zeitbedarf
7. Überschlagswerte Technik (Orientierung)
8. Energie, Wirkungsgrade, Experimente

---

## 1. Rechnungen
- Jede Rechnung **unabhängig neu** rechnen (mit Code, wenn verfügbar), nicht die vorhandene
  Lösung nachvollziehen.
- Formel richtig gewählt? Umstellung korrekt? Werte richtig eingesetzt?
- Rundung sinnvoll und angegeben; Zwischenergebnisse nicht doppelt gerundet.
- Bei Abweichung: eigene Rechnung vollständig im Bericht zeigen.

```text
Gegeben: p = 6 bar = 0,6 N/mm², d = 32 mm, η = 0,85
A = π · d² / 4 = π · 32² / 4 mm² = 804,2 mm²
F = p · A · η = 0,6 N/mm² · 804,2 mm² · 0,85 = 410,2 N  ≈ 410 N
```

## 2. Einheiten und Größenordnungen
- Dimensionsprüfung: Passen die Einheiten links und rechts?
- Einheiten konsistent (mm vs. m, bar vs. Pa vs. N/mm², min⁻¹ vs. s⁻¹)?
- Überschlag: Liegt das Ergebnis in einer realistischen Größenordnung (Abschn. 7)?
- Vorzeichen, Komma, Zehnerpotenz.

## 3. Lösbarkeit
- Sind **alle nötigen Angaben** in Aufgabe oder Material enthalten (oder als Tabellenbuchwert
  ausdrücklich erlaubt)?
- Ist die Aufgabe eindeutig? Gibt es mehrere vertretbare Lösungen – deckt der
  Erwartungshorizont sie ab?
- Passt der Operator zur erwarteten Leistung?
- Ist die Aufgabe ohne Abbildung lösbar, wenn die Abbildung nur als Platzhalter existiert?
- **Ablesungen aus Diagrammen:** Hängt das Ergebnis an einer gerundeten Ablesung (z. B. „0,4 m³“
  statt 0,42 m³), sodass genaues Ablesen zu einem anderen Urteil führt? Dann Wert vorgeben oder
  die Aufgabe so stellen, dass das Urteil robust ist.
- **Gescannte PDF und Bilder** (kein Text mit `pdftotext`): Seiten rendern
  (`pdftoppm -r 150 -png`) und Werte, Diagramme und Beschriftungen in der Abbildung selbst prüfen.

## 4. Konsistenz
- Aufgabe ↔ Lösung ↔ Abbildung ↔ Tabelle: gleiche Werte, Bezeichnungen, Einheiten?
- Material ↔ Lernsituation ↔ Unterrichtsentwurf: gleiche Handlungssituation, Namen, Zahlen,
  Zeitrichtwerte (Planungsakte heranziehen)?
- Begriffe durchgängig gleich (kein Wechsel „Gurt"/„Band"/„Riemen")?
- **Datei- und Anhangsverweise:** Gibt es jede genannte Datei, Anlage und Abbildung unter genau
  diesem Namen bzw. dieser Nummer (z. B. „04_Infoblatt" im Text, „03_Infoblatt" im Ordner)?
  Werden alle Dateien des Ordners irgendwo eingebunden? Verweisen Import-Dateien (Moodle,
  Classtime) auf Bilddateien, die beiliegen?
- **Änderungsprotokoll ↔ Dokument:** Ist jede als erledigt gemeldete Korrektur im Dokument
  tatsächlich angekommen (Stichprobe am Text, nicht am Protokoll)?
- Zahlen- und Kostenpakete gegen die genannten Grenzen prüfen (Budget, Grenzwerte) – auch die
  „gleichwertigen“ Alternativen im Erwartungshorizont.
- Punktsummen im Erwartungshorizont stimmen; Bewertungsraster passt zu den Kompetenzen?

## 5. Realitätsnähe und Sicherheit
- Entspricht die Situation betrieblicher Praxis (Rollen, Abläufe, Zuständigkeiten,
  Auszubildende im entsprechenden Ausbildungsjahr)? Im Beruflichen Gymnasium: Ist die Rolle
  („Ingenieurteam“) mit Schulmitteln einlösbar, und ist die Reduktion ausgewiesen (z. B.
  Genehmigungsunterlagen, IT-Grundschutz, Flüssigwasserstoff im Einfamilienhaus)? Typische Schieflagen: Auszubildende
  „kalibrieren" Messgeräte (Aufgabe eines Prüflabors – sie prüfen den Kalibrierstatus);
  werkseitig eingestellte Sicherheitseinrichtungen werden „eingestellt" (sie werden auf
  Funktion geprüft); Arbeiten, die erst bei der Inbetriebnahme möglich sind, gelten im
  Szenario schon als erledigt.
- Passt der Umfang des Szenarios zur Unterrichtszeit (z. B. ganzes Mehrfamilienhaus in drei
  Stunden)? Didaktische Reduktion muss **ausdrücklich** benannt sein.
- Werden Sicherheitsmaßnahmen genannt, wo nötig (Stillsetzen, Sichern, Freischalten,
  PSA, Gefährdungsbeurteilung)? Dürfen Auszubildende die Tätigkeit so ausführen?
- Elektrotechnische Arbeiten: Hinweis auf Qualifikation (Elektrofachkraft/elektrotechnisch
  unterwiesene Person) 🔎 nach geltender DGUV-Vorschrift prüfen.
- Werte aus der Praxis (Drücke, Drehmomente, Intervalle) nur mit Herstellerangabe.
- **Fiktive Kontaktdaten:** Vorwahl und Postleitzahl passen zusammen oder fehlen; E-Mail-Adressen
  mit reservierten Beispiel-Domains (`example.org`, `example.com`, `.example` – RFC 2606);
  keine realistisch wirkenden Telefonnummern.
- **Übernommene Fremdtexte:** Wörtlich übernommene Absätze (Herstellerbroschüre, Fachportal)
  brauchen eine Quellenangabe; bei Normaussagen die Primärquelle prüfen.

## 6. Zeitbedarf
- Reicht die angegebene Zeit für Lesen, Bearbeiten, Sichern? Faustregel: Lesen ~1 min je
  halbe Seite für geübte Leser, bei Deutsch als Zweitsprache deutlich mehr.
- Summiert sich der Verlaufsplan zur Stundenlänge (mit Puffer)?
- Ist der Umfang einer Lernsituation mit dem Zeitrichtwert vereinbar?

## 7. Überschlagswerte Technik (Orientierung, keine Bemessungswerte)

| Größe | typischer Bereich |
|---|---|
| Betriebsdruck Pneumatik (Industrie) | ca. 4–8 bar, häufig 6 bar |
| Netzspannung Niederspannung | 230 V / 400 V, 50 Hz |
| Dichte Stahl / Aluminium / Kupfer | ca. 7,85 / 2,7 / 8,9 g/cm³ |
| E-Modul Stahl | ca. 210 000 N/mm² |
| Normalgravitation | 9,81 m/s² |
| Schnittgeschwindigkeit Stahl mit HSS / Hartmetall | Größenordnung einige 10 m/min / einige 100 m/min (Werkstoff- und Herstellertabellen nutzen) |

Abweichungen von diesen Bereichen sind kein Fehler, aber ein Anlass zum Nachprüfen.

## 8. Energie, Wirkungsgrade, Experimente

- **Wirkungsgradketten rückwärts dividieren:** Vom Nutzen zum Aufwand gilt E_auf = E_nutz / η.
  Typische Fehler: *× η* statt *÷ η* oder ein „Aufschlag“ *× (1 + (1 − η))* – bei η = 0,9 nur
  1 % daneben und deshalb leicht übersehen (`scripts/messwerte_pruefen.py kette --schritt
  NUTZEN:ETA:ANGABE`).
- **Physikalische Grenzen** für Beispielmesswerte im Erwartungshorizont: Gasvolumen nach Faraday
  (`messwerte_pruefen.py faraday`), η ≤ 1, Energieerhaltung, Leistung = Kraft × Geschwindigkeit.
- **Einheiten von Stoffwerten:** Heizwert in MJ/m³, kWh/m³ oder kWh/kg; Dichte in kg/m³;
  vertauschte Einheiten erkennt `messwerte_pruefen.py einheit`.
- **Messkette mit Mikrocontroller:** ADC-Auflösung (z. B. 10 oder 12 bit), Referenzspannung,
  Sensorkennlinie mit Einheit – eine Rohzahl geteilt durch einen Faktor ist noch kein Messwert
  🔎 Datenblatt.
- **Laborwert ↔ Anlage:** Liegt ein Versuchsergebnis weit unter dem technischen Wert, gehört die
  Erklärung (Verluste, Messaufbau) in den Erwartungshorizont.
- **Sicherheit bei Versuchen:** Gefährdungsbeurteilung, Ersatzstoffe, Gase, Netzspannung
  (`experimentsicherheit.md`, falls vorhanden).

