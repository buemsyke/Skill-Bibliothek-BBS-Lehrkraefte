# Schaltungskatalog – geprüfte Vorlagen

Aufruf: `python3 scripts/schaltung.py vorlage <name> --parameter wert … -o 47_schaltung_<kurztitel>.txt`.
Katalog mit Parametern und Standardwerten: `python3 scripts/schaltung.py vorlagen`.
Jede Vorlage ist statisch geprüft (Raster, Anschlüsse, Messgeräte), gegen die Formelwerte nachgerechnet
(lineare Schaltungen) und in der Falstad-Engine gemessen (`schaltung.py vergleich <name>`).

Messgerätenamen in den Vorlagen: `I`, `I1` … Amperemeter; `U`, `U1` … Voltmeter. Wechselstrom: alle
Messgeräte zeigen Effektivwerte. Die Erwartungswerte stammen aus Formeln, nicht aus der Simulation.

## Gleichstrom

| Vorlage | Zweck | Parameter (Standard) | Messgeräte |
|---|---|---|---|
| `ohmsches-gesetz` | U, I, R messen | `u` 10 V, `r` 220 Ω | I, U_R |
| `reihenschaltung` | Spannungsteilung, Maschenregel | `u` 10, `r1` 220, `r2` 470, `r3` 680 | I; U1, U2, U3, U |
| `parallelschaltung` | Stromteilung, Knotenregel | `u` 10, `r1` 220, `r2` 470, `r3` 680 | I, I1–I3; U |
| `gemischte-schaltung` | Gruppenschaltung R1 + (R2 ∥ R3) | `u` 12, `r1` 100, `r2` 220, `r3` 330 | I, I2, I3; U1, U23 |
| `spannungsteiler` | unbelastet (rl 0) und belastet | `u` 12, `r1` 1000, `r2` 1000, `rl` 0 | I, (IL); U1, U2 |
| `bruecke` | Wheatstone, Abgleich | `u` 10, `r1` 100, `r2` 200, `r3` 300, `r4` 600 | I; U_B |
| `quelle-belastet` | Innenwiderstand, Klemmenspannung, Leistungsanpassung | `u0` 12, `ri` 2, `ra` 10 | I; Ui, Uk |
| `rc-schaltvorgang` | Laden/Entladen (S1, S2) | `u` 10, `r` 1000, `c` 100e-6, `re` 1000 | I; Uc |
| `rl-schaltvorgang` | Einschalten einer Spule | `u` 12, `r` 100, `l` 1 | I; U_R, U_L |

Zeitkonstanten: RC τ = R·C (Standard 0,1 s), RL τ = L/R (Standard 10 ms). Die Endwerte der Erwartung
gelten nach 10 τ.

## Wechselstrom

| Vorlage | Zweck | Parameter (Standard) |
|---|---|---|
| `ac-r` | Wirkwiderstand, u und i in Phase | `u_eff` 12, `f` 50, `r` 100 |
| `ac-l` | induktiver Blindwiderstand | `u_eff` 12, `f` 50, `l` 0,2 |
| `ac-c` | kapazitiver Blindwiderstand | `u_eff` 12, `f` 50, `c` 47e-6 |
| `ac-rl` / `ac-rc` | Scheinwiderstand, Phasenverschiebung | `r` 50, `l` 0,2 bzw. `c` 47e-6 |
| `ac-rlc` | Reihenschwingkreis; `f` 0 setzt f0 | `r` 20, `l` 0,2, `c` 47e-6 |
| `ac-parallel` | R, L, C parallel; Zweigströme | `r` 100, `l` 0,2, `c` 47e-6 |
| `ac-kompensation` | Blindstromkompensation (Schalter S) | `u_eff` 230, `r` 40, `l` 0,1, `c` 0 = Optimum, `kompensiert` true |
| `ac-transformator` | belasteter Transformator | `u1_eff` 24, `l1` 5 H, `ratio` 0,5 (N2/N1), `r_last` 10 |
| `ac-tiefpass` / `ac-hochpass` | RC-Filter, Grenzfrequenz | `u_eff` 5, `f` 1000, `r` 1000, `c` 100e-9 |
| `drehstrom-stern` | Strang-/Außenleiterspannung, Neutralleiter | `u_str` 230, `r1`–`r3` 100, `neutralleiter` true |

Reihenschaltungen zeigen U an jedem Bauteil (`U_R`, `U_L`, `U_C`) und die Gesamtspannung `U`; das
Oszilloskop liegt an der Quelle (Spannung grün, Strom gelb).

## Elektronik (Gleichrichter, Gleichspannungswandler)

| Vorlage | Zweck | Parameter (Standard) |
|---|---|---|
| `einweggleichrichter` | M1U, optional Glättung | `u_eff` 12, `f` 50, `r` 100, `c` 0, `mittelwert` true |
| `brueckengleichrichter` | B2U, optional Glättung | wie oben |
| `zdiode-stabilisierung` | Z-Diode, Vorwiderstand | `u_ein` 12, `r_v` 100, `u_z` 5,1, `r_l` 470 |
| `tiefsetzsteller` | Buck-Wandler, MOSFET + Freilaufdiode | `u_ein` 24, `tastgrad` 0,5, `f_s` 5000, `l` 2e-3, `c` 100e-6, `r` 10 |
| `hochsetzsteller` | Boost-Wandler | `u_ein` 12, `tastgrad` 0,5, `f_s` 5000, `l` 5e-3, `c` 100e-6, `r` 50 |

Bei Dioden und MOSFETs sind die Erwartungswerte Näherungen (Durchlassspannung 0,7 V, Verluste);
maßgeblich ist die Engine (`schaltung.py vergleich <name>`). Gleichrichter: `U_a` ist der Effektivwert,
`U_av` der Mittelwert (RC-Mittelwertmesser „Drehspul-Ersatz“; Falstad hat kein Mittelwertgerät).
Schaltwandler: Ansteuerung des MOSFET mit potentialfreier Rechteckquelle 0 … 10 V; Oszilloskop an der
Speicherdrossel.

## Eigene Schaltungen
Gibt es keine passende Vorlage: Vorlage mit ähnlicher Topologie wählen und `scripts/falstad_bau.py`
verwenden (Rasterkoordinaten, Messgeräte mit Namen), dann `schaltung.py pruefen --engine`. Die
Layoutregeln stehen in `references/darstellung-din.md`.

## Noch nicht abgedeckt (offen benennen)
Wechselrichter (Vollbrücke), Drehstrom-Brückengleichrichter B6U, Thyristor-/Triac-Steller,
Operationsverstärker, digitale Schaltungen. Dafür Falstad-Beispiele (`falstad/circuitjs1/circuits/`)
als Ausgangspunkt nehmen und mit `schaltung.py pruefen` auf Raster, Anschlüsse und Messgeräte prüfen.
