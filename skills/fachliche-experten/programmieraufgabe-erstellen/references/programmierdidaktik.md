# Programmierdidaktik – Aufgabenformen, Testfälle, Hilfen

## 1. Aufgabenformen

| Form | Was die Lernenden tun | geeignet für |
|---|---|---|
| **PRIMM** | Vorhersagen (Was gibt der Code aus?) → Ausführen → Untersuchen (Zeile erklären) → Verändern → selbst Schreiben | Einführung neuer Konzepte |
| **Parsons-Aufgabe** | vorgegebene Codezeilen in die richtige Reihenfolge bringen (mit Ablenkern) | Struktur verstehen ohne Syntaxhürde |
| **Lückencode** | markierte Stellen im Startcode ergänzen | Übung, Differenzierung |
| **Fehlersuche** | dokumentierte Fehler finden, erklären, beheben | Lesen und Testen, Prüfungsvorbereitung |
| **Offene Aufgabe** | Anforderungen und Testfälle gegeben, Lösung frei | DQR 4 nahe Abschluss, Projekte |

Für G-Code zusätzlich: **Programm aus Zeichnung** (Nullpunkt, Konturpunkte, Technologie),
**Simulation deuten** (Wo kollidiert das Werkzeug?), **Programm optimieren** (Wege, Werkzeugwechsel).

## 2. Anforderungen und Testfälle

- Anforderungen messbar: Eingang (Größe, Bereich, Einheit), Ausgang (Format, Einheit, Takt),
  Grenzwerte, Fehlerverhalten.
- **Testfälle als Tabelle:** Eingabe → erwartete Ausgabe (mit Toleranz), mindestens ein
  Normalfall, ein Grenzfall, ein Fehlerfall (z. B. Sensor nicht angeschlossen, Wert außerhalb).
- Bei Mikrocontrollern ohne Hardware: Eingaben als simulierte Rohwerte (ADC-Zahl) testen.
- G-Code: Prüfmaße der Zeichnung, Simulation in der Software der Schule, Rohteilgrenzen.

## 3. Gestufte Hilfen

1. **Hinweis:** Worauf achten? („Wie groß ist der größte ADC-Wert bei 12 bit?“)
2. **Teilschritt:** Formel oder Struktur ohne Zahlen.
3. **Teillösung:** Code für einen Teil; der Rest bleibt eigene Leistung.

Hilfen werden genutzt, ohne dass Punkte verloren gehen, oder der Abzug ist vorher bekannt.

## 4. Bewertung von Code (für Raster und Erwartungshorizont)

- **Funktion** über Testfälle (wie viele bestanden?), nicht über Schönheit.
- **Struktur:** Funktionen bzw. Abschnitte, sprechende Namen, keine magischen Zahlen
  (Konstanten mit Einheit).
- **Kommentar:** Zweck, Ein- und Ausgaben, Einheiten; keine Reste aus Tutorials.
- **Fehlerbehandlung:** Grenzwerte, Plausibilitätsprüfung.
- G-Code: Maßhaltigkeit, Technologiewerte (Vorschub, Drehzahl nach Tabellenbuch), sichere
  Anfahr- und Abfahrwege, Radiuskorrektur richtig an- und abgewählt.

## 5. KI-Codeassistenten im Unterricht

- Erlaubt nur nach Regel der Lehrkraft (z. B. Erklären lassen ja, Lösung generieren nein).
- KI-Code wird wie fremder Code behandelt: kennzeichnen, testen, Zeile für Zeile erklären können.
- Im Fachgespräch zeigt die Person, dass sie den eigenen Code versteht (Variante ändern lassen).
- Keine personenbezogenen Daten und keine Zugangsdaten (WLAN-Passwörter) in KI-Werkzeuge.

## 6. Operatoren

- Berufsschule: *entwickeln, erstellen, implementieren, testen* nach Operatorenliste der Schule.
- Berufliches Gymnasium (Klausur, Abitur): EPA-Operatoren *entwickeln, entwerfen, überprüfen,
  untersuchen*; praktische Operatoren (*programmieren, testen, speichern*) nur als erweiterte
  Operatoren mit AFB im Lehrermaterial.
