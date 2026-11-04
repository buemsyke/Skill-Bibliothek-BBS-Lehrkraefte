# GIFT-Format (Moodle) – nur für den Notfall ohne edu-quiz

GIFT entsteht im Regelfall mit `edu-quiz` aus der Quizquelle. Diese Kurzreferenz dient zur
Fehlersuche beim Import und für Umgebungen ohne Skriptausführung. Von Hand geschriebenes GIFT
im Begleitblatt als `⚠️ ungeprüft (ohne edu-quiz)` kennzeichnen.

## Grundgerüst

```
::Fragetitel:: Fragetext { Antworten }
```

Eine **Leerzeile** trennt zwei Fragen; innerhalb einer Frage keine Leerzeile. Datei in UTF-8.
Kategorie einmal am Anfang: `$CATEGORY: LF4/LS 4.2`. Kommentare: `// …`.

| Zeichen | Bedeutung |
|---|---|
| `=` | richtige Antwort |
| `~` | falsche Antwort |
| `#` | Rückmeldung zur Antwort davor |
| `####` | allgemeine Rückmeldung |
| `%50%` | Gewicht in Prozent |
| `\` | maskiert `~ = # { } :` im Text |

## Typen

```
::Grundmaßnahme:: Zu welcher Grundmaßnahme gehört das Nachschmieren? {
=Wartung#Richtig.
~Inspektion#Inspektion stellt den Istzustand nur fest.
~Instandsetzung
}

::Sicherung:: Welche Maßnahmen sind vor der Wartung nötig? {
~%50%Stillsetzen
~%50%Gegen Wiedereinschalten sichern
~%-100%Gurt mit der Hand abbremsen
}

::Inspektion:: Bei der Inspektion wird der Istzustand festgestellt. {T}

::Lücke:: Die Grundmaßnahmen sind Wartung, {=Inspektion}, Instandsetzung und Verbesserung.

::Zuordnung:: Ordnen Sie zu. {
=Lager nachschmieren -> Wartung
=Gurtspannung messen -> Inspektion
}

::Empfehlung:: Beurteilen Sie, ob der Förderer weiterlaufen kann. {}
```

Mehrfachauswahl: **kein** `=`; richtige Anteile ergeben zusammen 100 %, falsche negativ.

## Häufige Importfehler

- Sonderzeichen `~ = # { } :` im Text nicht mit `\` maskiert (z. B. Uhrzeit `8\:00`) – auch
  im Fragetext. Formeln und Code: `\( \frac{W}{t} \)` wird `\\( \\frac\{W\}\{t\} \\)`,
  `loop() { … }` wird `loop() \{ … \}`.
- Klammern `{ }` nicht paarig; Leerzeile fehlt zwischen Fragen.
- Mehrere `=` bei einer Single-Choice-Frage.
- Datei nicht in UTF-8 (Umlaute).
