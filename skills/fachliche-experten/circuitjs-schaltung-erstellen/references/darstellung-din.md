# Darstellung nach DIN und Messgeräte

## Bezugsrahmen
- Schaltzeichen nach **DIN EN 60617**, Bezeichner nach **DIN EN 81346** (R1, C1, L1, V1, S1) 🔎 Norm
  im Einzelfall prüfen. Gleiche Darstellung wie die Versuche des Simulationsprojekts: weißer Hintergrund,
  Widerstand als Rechteck, Stromrichtung technisch (Plus nach Minus).
- Das setzt der Aufruf der Seite, nicht der Schaltungstext: `CircuitLoader` im Simulationsprojekt
  (`js/circuit-loader.js`) übergibt `euroResistors=true`, `whiteBackground=true`,
  `conventionalCurrent=true`. Die Seite `schaltung.py url` verwendet dieselben Parameter.
- Kondensator, Spule, Diode, Z-Diode, MOSFET, Transformator, Masse und Quellen zeichnet Falstad
  normnah; Quelle für Gleichspannung als Plattenpaar, für Wechselspannung als Kreis mit Sinus.

## Messgeräte (Pflicht, wo sie sinnvoll sind)
| Größe | Gerät | Anschluss |
|---|---|---|
| Strom | Amperemeter (Kreis mit A, `370`, Flags 3) | **in Reihe** in die Leitung |
| Spannung | Voltmeter (Kreis mit V, `p`, Flags 3) | **parallel** zum Bauteil, erster Anschluss am höheren Potential |

Regeln der Vorlagen:
1. Gesamtstrom in der Zuleitung (links hinter der Quelle), Zweigströme je Zweig bei Parallelschaltung.
2. Je Bauteil, dessen Spannung die Aufgabe braucht, ein Voltmeter; zusätzlich die Gesamtspannung.
3. Gleichstrom Modus 0 (Anzeige), Wechselgrößen und Gleichrichterströme Modus 1 (Effektivwert).
4. Amperemeter nie parallel zu einem Bauteil oder einer Quelle (Kurzschluss, Prüfung `MESS_KURZ`);
   Voltmeter nie in Reihe.
5. Positiver Anzeigewert bei Normalbetrieb; sonst Anschlüsse tauschen (Prüfung `POLUNG`).
6. Bezeichner an jedem Bauteil und Messgerät (`R1`, `U1`, `I`), damit Lernende Messwert und Bauteil
   zuordnen.

## Layoutregeln
- Quelle links, Verbraucher rechts, obere Schiene Plus, untere Minus; Ströme fließen von oben nach
  unten durch senkrechte Zweige. Bauteile mindestens 3 Rasterpunkte (48 px), Messgeräte 4 (64 px) lang.
- Alle Leitungen rechtwinklig; Abzweige nur an gemeinsamen Endpunkten (an jedem Abzweig eine
  Leitung teilen). Kreuzungen sind erlaubt, wenn sie bewusst ohne Punkt gezeichnet werden.
- Halbleiterschalter: Masse `g` setzen, sonst konvergiert die Simulation nicht.
- Texte klein halten (Größe 12); keine Dekoration, keine Pfeile ohne Messfunktion.

## Einbau in das Simulationsprojekt
Die Versuche liegen unter `uebungen/NN-name.html` und laden die Schaltung als JavaScript-Text:

```js
const circuit = `$ 1 0.000005 …
v …
`;
CircuitLoader.loadCircuit('simulator', circuit);
```

`schaltung.py vorlage <name> --js` liefert genau diesen Block. Die Aufgabenstellung gehört in die Seite
(Theorie, Aufgaben, Messhinweis), nicht in die Schaltung; die Erwartungswerte des Begleitblatts liefern
die Beispiellösung.
