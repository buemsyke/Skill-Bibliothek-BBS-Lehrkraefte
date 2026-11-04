# Falstad-Textformat (circuit.js) – geprüfte Zeilenformate

Alle Angaben wurden an der Falstad-Webversion des Simulationsprojekts (`falstad/circuitjs.html`)
mit der echten Engine nachgemessen; Abweichungen stehen unter *Fallen*. Koordinaten sind Pixel,
Anschlüsse liegen im **16-px-Raster**. Der Baukasten `scripts/falstad_bau.py` rechnet in Rasterpunkten
(1 Einheit = 16 px) und schreibt die Pixelwerte.

## Aufbau
- Zeile 1: `$ flags zeitschritt iterationen stromgeschwindigkeit spannungsbereich leistungshelligkeit minimalschritt`.
  Standard der Versuche: `$ 1 0.000005 10.20027730826997 50 5 43 5e-11` (Flags 1 = Stromrichtung zeigen).
  Zeitschritt anpassen: Netzfrequenz 50 Hz ≈ `2e-5`, RC mit τ ≈ 0,1 s `1e-4`, Schaltwandler `1e-6`.
- Danach je Zeile ein Element: `typ x1 y1 x2 y2 flags werte…`; am Ende Oszilloskope `o …`.
- Elemente verbinden sich **nur über gemeinsame Anschlusspunkte** (Endpunkt auf Endpunkt). Ein
  Anschluss, der mitten auf einer Leitung liegt, ist **nicht** verbunden. Kreuzen sich Leitungen
  ohne gemeinsamen Endpunkt, sind sie nicht verbunden (DIN: Kreuzung ohne Punkt).
- Reihenfolge der Zeilen = Reihenfolge der Elementliste der Engine (Textzeilen `x` zählen mit,
  Oszilloskopzeilen `o` nicht).

## Elemente (Standard der Vorlagen)

| Zeile | Bedeutung | Bemerkung |
|---|---|---|
| `w x1 y1 x2 y2 0` | Leitung | rechtwinklig; an jeder Abzweigstelle enden/beginnen Leitungen |
| `r x1 y1 x2 y2 0 ohm` | Widerstand | Rechteck nach DIN durch URL-Parameter `euroResistors=true` |
| `c x1 y1 x2 y2 0 farad u0 0.001` | Kondensator | u0 = Anfangsspannung U(Anschluss 1) − U(Anschluss 2); letzter Wert Serienwiderstand |
| `l x1 y1 x2 y2 0 henry i0` | Spule | i0 = Anfangsstrom |
| `v x1 y1 x2 y2 0 0 40 volt 0 0 0.5` | Gleichspannungsquelle | **Plus am zweiten Punkt** |
| `v x1 y1 x2 y2 0 1 f û 0 phase 0` | Wechselspannungsquelle | û = Scheitelwert (= √2 · U_eff); `phase` im Bogenmaß, u = û·sin(ωt + phase) |
| `v x1 y1 x2 y2 0 2 f û/2 û/2 phase tastgrad` | Rechteck 0 … û | Tastgrad = Anteil „high“ |
| `s x1 y1 x2 y2 0 pos false` | Schalter | pos 0 = **geschlossen**, 1 = offen |
| `d x1 y1 x2 y2 2 default` | Diode | Anode = erster Punkt, Kathode = zweiter |
| `z x1 y1 x2 y2 1 0.805904783 uz` | Z-Diode | Anode erster, Kathode zweiter Punkt |
| `T x1 y1 x2 y1 0 l1 ü 0 0 k` | Transformator | Anschlüsse (x1,y1), (x1,y1+32), (x2,y1), (x2,y1+32); `ü` = N2/N1; k = Kopplung 0,999 |
| `f x1 y1 x2 y1 0 vt beta` | n-Kanal-MOSFET waagerecht | Gate (x1,y1), Drain (x2,y1−16), Source (x2,y1+16) |
| `g x1 y1 x1 y1+16 0` | Masse | ein Anschluss (x1,y1) |
| `p x1 y1 x2 y2 3 modus` | **Voltmeter** (Kreis mit V) | zeigt U(1) − U(2); Modus 0 Momentanwert, 1 Effektivwert, 2 Spitzenwert |
| `370 x1 y1 x2 y2 3 modus` | **Amperemeter** (Kreis mit A) | Strom von 1 nach 2 positiv; Modus 1 Effektivwert |
| `x x1 y1 x2 y2 4 größe text` | Beschriftung | Leerzeichen als `\s` |
| `o index tempo 0 3 skala zeitmaß pos` | Oszilloskop für Element `index` | zeigt Spannung und Strom des Elements |

Flags 3 bei `p` und `370` schalten das **DIN-Kreissymbol** ein (Flags 1 zeigt nur Wert und Pfeil).
Falstad hat **kein** Mittelwert-Messgerät; für gleichgerichtete Größen dient der RC-Mittelwertmesser der
Vorlagen (Drehspul-Ersatz).

## Fallen (alle am Simulator gemessen)
1. **Einschalttransient:** Eine reine Spule an einer Sinusquelle, die bei u = 0 startet, hat ein
   Gleichstromglied, das nie abklingt (Strom-Effektivwert um rund 70 % zu hoch). Abhilfe: Kosinus-
   Start (`phase = π/2`), Kondensatoren dann mit u0 = û vorladen.
2. **Ohne Masse hängt die Simulation** bei Schaltern mit MOSFET (Konvergenz). Jede Schaltung mit
   Halbleiterschalter bekommt ein `g`. Der MOSFET braucht `β` (siebter Wert): der Standard 0,02 A/V²
   ergibt rund 6 Ω Durchlasswiderstand und verfälscht Wandler; die Vorlagen setzen β = 1.
3. **Schalter:** `pos 0` ist geschlossen. Quellen und Messgeräte haben eine Zählrichtung; ein
   negativ angezeigter Wert bedeutet vertauschte Anschlüsse, kein Fehler der Schaltung.
4. **Ideale Messgeräte:** Das Amperemeter hat 0 Ω, das Voltmeter ∞ Ω – es gibt keine
   Messabweichung (stromrichtig/spannungsrichtig). Für Messfehlerversuche Innenwiderstände als `r`
   ergänzen (Amperemeter in Reihe 1 Ω, Voltmeter parallel 10 kΩ) und kennzeichnen.
5. **Effektivwert** zeigen `p`/`370` nur mit Modus 1; Modus 0 flackert bei Wechselgrößen.
6. **Zeitschritt:** Ein zu großer Zeitschritt verfälscht Schaltwandler; ein zu kleiner macht die
   Simulation auf langsamen Rechnern unbenutzbar. Vorlagenwerte beibehalten.
7. **`R` (Rail)** ist kein DIN-Schaltzeichen: Spannungsquelle `v` mit Leitungen verwenden.
