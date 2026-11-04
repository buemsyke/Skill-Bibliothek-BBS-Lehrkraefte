# Experimentdidaktik – kurz und praktisch

## 1. Vorhersage – Beobachtung – Erklärung

Vor dem Versuch schreiben die Lernenden eine **Vorhersage mit Begründung** auf (Hypothese).
Nach dem Versuch vergleichen sie: bestätigt, widerlegt oder offen – und erklären die
Abweichung. Ohne Vorhersage wird aus dem Experiment eine Vorführung.

**Prüfbare Hypothese:** nennt eine Größe und eine Richtung oder einen Wert („Mit Kupfer statt
Stahl entsteht bei gleicher Ladung mehr Wasserstoff.“ ist prüfbar; „Kupfer ist besser.“ nicht).

## 2. Variablen

| Variable | Bedeutung | Beispiel Elektrolyse |
|---|---|---|
| unabhängig | wird gezielt verändert | Elektrodenmaterial oder Stromstärke |
| abhängig | wird gemessen | Gasvolumen je Zeit, Spannung |
| konstant gehalten | darf sich nicht ändern | Elektrolyt, Konzentration, Elektrodenabstand, Temperatur |

Nur **eine** unabhängige Variable je Versuchsreihe – sonst ist der Einfluss nicht zuzuordnen.

## 3. Öffnungsgrad

| Stufe | Was vorgegeben ist | passend für |
|---|---|---|
| geschlossen | Frage, Aufbau, Durchführung, Tabelle | Einführung, Sicherheit im Vordergrund |
| angeleitet | Frage und Material; Durchführung und Tabelle planen die Lernenden | Regelfall DQR 3–4 |
| offen | nur die Frage aus der Handlungssituation | Projekt, Facharbeit, DQR 4 nahe Abschluss |

Sicherheitsrelevante Teile (Spannung, Stoffe, Mengen) bleiben immer vorgegeben. Vorgegebene
Schritte sind kurz, am besten als Bildfolge am Aufbau; die beschriftete Skizze des Aufbaus
gehört auf jeder Stufe dazu (`schuelermaterial.md`).

## 4. Lehrer- oder Schülerversuch

Entscheidet die Gefährdungsbeurteilung, nicht die Bequemlichkeit. Wo ein Schülerversuch nicht
vertretbar ist: Lehrerversuch mit Beobachtungsauftrag, Video mit echten Messwerten oder
Simulation – und die Auswertung bleibt bei den Lernenden.

## 5. Auswertung

- Messwerttabelle mit **Größe in Einheit** im Kopf („U in V“, „V(H₂) in ml“).
- Wiederholungen (mindestens drei Messungen je Einstellung) und Mittelwert.
- Diagramm mit beschrifteten Achsen; Ausgleichsgerade nur, wenn ein linearer Zusammenhang
  erwartet wird.
- Rechnung mit Formel, eingesetzten Werten und Einheit.
- **Rückbindungsfrage:** Was bedeutet das Ergebnis für die Anlage der Handlungssituation?
  („Warum liegt der Wirkungsgrad im Versuch bei etwa 20 %, beim Elektrolyseur bei 60–80 %?“)

## 6. Messunsicherheit (Schulniveau)

- **Geräteunsicherheit** aus der Anleitung des Messgeräts (z. B. ±(1 % + 2 Digit)) oder
  Ablesegenauigkeit (halber Skalenteil).
- **Zufällige Streuung** aus Wiederholungen (Spannweite oder Standardabweichung).
- **Fortpflanzung:** Summe und Differenz → absolute Unsicherheiten addieren; Produkt und
  Quotient → relative Unsicherheiten addieren (Größtfehler) bzw. quadratisch addieren (Gauß).
  Rechenhilfe: `messwerte_pruefen.py unsicherheit "U*I*t" U=…:… I=…:… t=…:…`.
- **Systematische Fehler** benennen (Gas entweicht, Elektroden reagieren, Temperatur, Druck).
- Ergebnis mit sinnvoller Stellenzahl: Unsicherheit mit einer, höchstens zwei geltenden Ziffern.

## 7. Physikalische Grenzen für Erwartungswerte

- Faraday: V = I·t/(z·F)·R·T/p – Angaben darüber sind unmöglich.
- Energieerhaltung: Nutzen ≤ Aufwand; in Wirkungsgradketten rückwärts **dividieren**.
- Stoffwerte in der richtigen Einheit (Heizwert MJ/m³ oder kWh/kg).
- Größenordnung prüfen: Ein Schülerversuch liefert Milliliter und Joule, keine Liter und
  Kilowattstunden.
