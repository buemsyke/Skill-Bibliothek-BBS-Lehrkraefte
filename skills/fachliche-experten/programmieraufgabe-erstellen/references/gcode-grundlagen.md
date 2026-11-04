# G-Code – Grundlagen für Aufgaben und Prüfung

Eigene Zusammenfassung nach DIN 66025 und der verbreiteten PAL-Programmierung im
Ausbildungs- und Schulbereich. Steuerungen weichen ab (Zyklen, Adressen, Kreisparameter) 🔎 –
maßgeblich ist das Handbuch bzw. die Simulationssoftware der Schule.

## 1. Satzaufbau

`N10 G01 X25 Y22.5 F150` – Satznummer, Wegbedingung, Koordinaten, Technologiewerte. Ein Satz
enthält eine Bewegung; Werkzeugwechsel, Spindel und Bewegung möglichst in eigenen Sätzen.
Dezimaltrennzeichen ist der **Punkt**. Kommentare in Klammern.

| Adresse | Bedeutung |
|---|---|
| G | Wegbedingung (G00 Eilgang, G01 Gerade, G02/G03 Kreis im/gegen den Uhrzeigersinn) |
| X, Y, Z | Zielkoordinaten (absolut mit G90, inkrementell mit G91; PAL auch XI, YI, ZI) |
| I, J, K | Kreismittelpunkt, meist inkrementell vom Startpunkt aus 🔎 Steuerung |
| R | Radius (Alternative zu I/J) |
| F, S, T | Vorschub, Drehzahl, Werkzeug |
| M | Zusatzfunktion (M03/M04 Spindel rechts/links, M05 Spindel aus, M06 Werkzeugwechsel, M08/M09 Kühlmittel, M30 Programmende) |

## 2. Koordinaten und Nullpunkte

- Maschinennullpunkt M (fest), Werkstücknullpunkt W (wählbar, z. B. Mitte des Rohteils oder
  obere Ecke), Nullpunktverschiebung G54 ff.
- An der Fräsmaschine ist **Z die Spindelachse**, positiv vom Werkstück weg; X und Y liegen in
  der Ebene (Rechte-Hand-Regel) 🔎 DIN 66217.

## 3. Regeln, die das Prüfskript kennt

| Regel | Fehlerbild |
|---|---|
| Vorschub vor der ersten Schnittbewegung | G01/G02/G03 ohne F |
| Spindel läuft vor dem Schnitt | Schnittbewegung oder Zyklusaufruf vor M03/M04 |
| Kreis vollständig bestimmt | G02/G03 ohne I/J/K oder R |
| Kreis geometrisch möglich | Abstand Start–Mittelpunkt ≠ Abstand Ende–Mittelpunkt |
| Radiuskorrektur an- und abwählen | G41/G42 ohne Anfahrweg in X/Y; Eilgang in der Ebene bei aktiver Korrektur; kein G40 bis Programmende |
| Programmende | M30 bzw. M02 fehlt |
| Zahlen | Komma statt Punkt |
| Verfahrbereich (mit `--rohteil`) | Bahn weit außerhalb; Eilgang unterhalb der Oberfläche (Hinweis – zulässig, wenn schon zerspant) |

## 4. Zyklen (PAL, Auswahl – Parameter laut Handbuch 🔎)

- **Taschen und Zapfen** (Rechteck-, Kreistasche, Kreiszapfen): Definition mit Tiefe,
  Abmessungen, Zustellung, Sicherheitsabstand; Ausführung mit **Zyklusaufruf an einem Punkt**
  (G79) oder auf einem Lochkreis.
- **Bohrzyklen** (G81 ff.): Tiefe, Rückzugsebene, Verweilzeit.
- Das Prüfskript behandelt Zyklusdefinitionen nicht als Bahnbewegung und prüft beim Aufruf, ob
  die Spindel läuft. Die geometrische Prüfung der Zyklusbahn leistet nur die Simulation.

## 5. Typische Fehler in Aufgaben und Lösungen

- Beschreibung eines Zyklus aus einem anderen Zyklus kopiert.
- Lochkreis-Koordinaten gerundet, Punkte liegen nicht auf dem Kreis (z. B. y = 34,69 statt
  40 · sin 60° = 34,64 bei Lochkreis-Ø 80).
- Werkzeugwechsel in einem Bewegungssatz; Komma zwischen M-Wörtern.
- Achsrichtungen im Infotext vertauscht („Z von oben nach unten“).
