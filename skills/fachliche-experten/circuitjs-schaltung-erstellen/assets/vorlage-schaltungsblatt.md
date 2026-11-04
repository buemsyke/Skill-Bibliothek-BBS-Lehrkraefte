---
artefakt: Simulationsschaltung
titel: "<Kurztitel der Schaltung>"
skill: circuitjs-schaltung-erstellen
skill_version: "1.3"
stand: <JJJJ-MM-TT>
bildungsgang: "<Bildungsgang>"
curriculare_vorgabe: "<Lernfeld bzw. Lerngebiet>"
dqr: <3|4|5>
status: "KI-Entwurf – fachlich zu prüfen"
bereich: planung
---

# Simulationsschaltung: <Titel>

## Schaltung
- Datei: `47_schaltung_<kurztitel>.txt` (Vorlage `<name>`, Parameter `<u=…, r1=…>`)
- Simulator: circuit.js (Falstad), Darstellung wie die Versuche des Simulationsprojekts
  (weiß, Rechteck-Widerstand, technische Stromrichtung)
- Zeitschritt und Besonderheiten: <z. B. Zeitschritt 2e-5, Schalter S1 geschlossen, Oszilloskop an der Quelle>

```
<Falstad-Text der Schaltung>
```

## Messgeräte und Erwartungswerte
Erwartung aus Rechnung; bei Dioden und Transistoren Näherung, maßgeblich ist die Engine-Messung.

| Gerät | Misst | Erwartung | Engine | Einheit | Modus |
|---|---|---|---|---|---|
| I | Gesamtstrom (Amperemeter in Reihe) | <Wert> | <Wert oder 🔎> | A | Anzeige |
| U1 | Spannung an R1 (Voltmeter parallel) | <Wert> | <Wert oder 🔎> | V | Anzeige |

## Rechenweg (für Beispiellösung)
$$<Formel>$$
<Zwischenschritte mit Einheiten>

## Beobachtungshinweise für die Aufgabe
- <Was Lernende ändern können (Bauteilwert doppelklicken) und was sich ändern soll>
- <Typischer Fehler, z. B. Voltmeter in Reihe, vertauschte Polung>

## Einbau
```js
const circuit = `<Falstad-Text>`;
CircuitLoader.loadCircuit('simulator', circuit);
```
Seite: `uebungen/<NN-name>.html` (Kopie oder neue Seite, bestehende Dateien nicht überschreiben).

## Qualitätscheck
| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Prüfung `schaltung.py pruefen` ohne ❌ | ✅/⚠️/❌ | |
| Voltmeter parallel, Amperemeter in Reihe, Anzeigen positiv | ✅/⚠️/❌ | |
| Formelwerte gegen Engine | ✅/⚠️/❌ | |
| Darstellung wie vorhandene Versuche | ✅/⚠️/❌ | |

## Annahmen und Prüfaufträge
- ⚠️ Annahme: <Bauteilwerte, Frequenz, Gleich- oder Wechselspannung>
- 🔎 Prüfen: <z. B. Engine-Messung nicht ausgeführt; Realversuch nur nach Gefährdungsbeurteilung>

## Übergabe
- Schaltungsdatei, Parameter und Erwartungswerte für das Aufgabenblatt
- Empfohlene nächste Skills: `unterrichtsmaterial-erstellen`, `experiment-planen`, `material-pruefen`

> KI-gestützt erstellt (Skill circuitjs-schaltung-erstellen v1.3). Fachliche Prüfung und Verantwortung: Lehrkraft.
