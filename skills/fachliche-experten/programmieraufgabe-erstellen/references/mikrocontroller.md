# Mikrocontroller-Aufgaben – Messkette und Grenzen

Eigene Zusammenfassung. Konkrete Werte (Auflösung, Referenzspannung, zulässige Pegel,
Pinbelegung) **immer aus dem Datenblatt bzw. der Board-Dokumentation** übernehmen 🔎 – sie
unterscheiden sich zwischen Boards und Firmware-Versionen.

## 1. Messkette vom Sensor zur Größe

```text
physikalische Größe → Sensor (Kennlinie) → Spannung → ADC (Auflösung, Referenz) → Rohwert
Rohwert → Spannung → Größe (Kennlinie umkehren) → Einheit → Ausgabe/Weiterrechnung
```

Beispiel mit Platzhalterwerten (Werte aus dem Datenblatt einsetzen):

```text
U = Rohwert / (2^n − 1) · U_ref            n = ADC-Auflösung in bit, U_ref = Referenzspannung
v = (U − U_0) / (U_max − U_0) · v_max      lineare Sensorkennlinie, U_0 = Ausgang bei v = 0
Q = v · A = v · π · d² / 4                 Volumenstrom aus Strömungsgeschwindigkeit und Querschnitt
```

Typische Fehler: Rohwert durch einen Faktor teilen, ohne Einheit („Value = analogRead(Pin)/K“);
Kennlinie mit Offset ignoriert; Querschnitt mit Radius statt Durchmesser; Einheit l/min mit m³/s
verwechselt.

## 2. Spannungspegel und Schutz

- Eingangsspannung nie über der zulässigen Pin-Spannung des Boards (viele Boards: 3,3 V, andere
  5 V) 🔎 Datenblatt; bei Sensoren mit höherem Ausgang Spannungsteiler planen und rechnen.
- ADC-Eingänge mancher Boards sind nichtlinear an den Rändern des Messbereichs 🔎 –
  Kalibrierung mit zwei Messpunkten als Lernanlass.
- Externe Lasten (Motoren, Relais) nie direkt an Pins; Treiber, Freilaufdiode, getrennte
  Versorgung.

## 3. Netzwerk und App

- WLAN-Zugangsdaten nicht im Code verteilen (eigene Datei, nicht ins Schülermaterial,
  nicht in KI-Werkzeuge).
- Baukastensysteme für Apps (Blockprogrammierung) brauchen oft ein Konto beim Anbieter →
  Datenschutz mit Schule klären; Alternative: serielle Ausgabe oder Webserver auf dem Board.
- Blockcode ist mit `code_pruefen.py` nicht prüfbar – Prüfliste: Ereignisse, Variablen,
  Einheiten, Fehlerfall, Test mit simulierten Werten.

## 4. Was `code_pruefen.py` prüft – und was nicht

| prüft | prüft nicht |
|---|---|
| C/C++-Syntax mit g++ und einem Stub der Arduino-Grundfunktionen | Bibliotheken (WLAN, Bluetooth, Sensorbibliotheken) – nur als ⚠ gemeldet |
| Dezimalkomma (`1,5` statt `1.5`) | Pinbelegung, Timing, Interrupts, Speicherbedarf |
| Python-Syntax | Laufzeitfehler, Logikfehler – dafür Testfälle |

Vollständig prüft nur der Upload auf die Zielhardware oder ein Simulator mit Testfällen.
