# Spec einer Wokwi-Simulation (`48_wokwi_<kurztitel>.yaml`)

Die Spec bildet die Steuerungsaufgabe so ab, wie sie im Material steht. Aus ihr erzeugt
`scripts/wokwi.py` Sketch, Schaltung, Szenarien und Begleitblatt. Bedingungen stehen in der Schreibweise
des Notationsblatts (`notation-steuerungstechnik.md`). Vollständiges Beispiel mit Zähler, Flanke und
Alternativverzweigung: `assets/spec-muster.yaml`; Testlauf an einer Abituraufgabe: Beispiel
`beispiele/abitur-biogas-v2/48_wokwi_biogas-beschickung.yaml` der Bibliothek.

## 1. Kopf

| Schlüssel | Bedeutung | Standard |
|---|---|---|
| `titel` | Titel der Steuerung | „Steuerung“ |
| `kurztitel` | Dateiname `48_wokwi_<kurztitel>` (Kleinbuchstaben, Bindestriche) | aus dem Titel |
| `quelle` | Aufgabe, aus der die Spec stammt | – |
| `plattform` | `arduino-uno` oder `esp32` | `arduino-uno` |
| `zeitraffer` | `{faktor: 60, ab: 1min}` – Zeiten ab `ab` laufen 1:faktor, kürzere in Echtzeit; `{faktor: 1}` = Echtzeit | Echtzeit |
| `bildungsgang`, `curriculare_vorgabe`, `dqr`, `status`, `vertraulich` | Kopf des Begleitblatts | Platzhalter |
| `annahmen`, `pruefauftraege` | Listen; erscheinen im Begleitblatt als `⚠️ Annahme:` bzw. `🔎 Prüfen:` | leer |
| `einsatz` | Liste mit Einsatzideen für das Begleitblatt | drei Standardideen |

## 2. Zuordnungsliste

```yaml
eingaenge:          # digitale Geber
  - {bmk: -S1, name: "Taster Start", pin: D2, kontakt: "NO", bauteil: taster, signal_1: "Start betätigt"}
  - {bmk: -S2, name: "Taster Stopp", pin: D3, kontakt: "NC", bauteil: taster, signal_1: "Stopp nicht betätigt"}
  - {bmk: -BL1, name: "Schwimmerschalter", pin: D4, kontakt: "NC", bauteil: schalter,
     signal_1: "Füllstand über Mindesthöhe", start: 1, kurz: "Füllstand"}
analogeingaenge:    # 4 … 20 mA, Wert im Programm als physikalische Größe
  - {bmk: -BT1, name: "Temperaturfühler", pin: A0, bereich: [0, 100], einheit: "°C", start: 38, stellen: 1}
ausgaenge:
  - {bmk: -QA1, name: "Schütz Förderpumpe -M1", pin: D8, signal_1: "Pumpe ein", kurz: "Pumpe"}
```

- **Pins** wie auf dem Board: `D2` … `D13`, `A0` … `A5` (Uno); `GPIO16` … (ESP32). E/A-Platine (Anlage der
  Bibliothek): Uno D2 … D7 Eingänge, D8 … D13 Ausgänge, A0/A1 analog; ESP32 GPIO16 … 19, GPIO25 … 27/32/33,
  GPIO34/35. Andere Pins sind erlaubt (Hinweis), D0/D1 bzw. GPIO1/3/6 … 11 nicht.
- **`kontakt`** NO oder NC, **immer in Anführungszeichen** (YAML 1.1 liest `NO` als falsch). Das Signal folgt der
  Spalte „Signal 1 bedeutet“; der Öffner liefert unbetätigt 1.
- **`bauteil`**: `taster` (tastend, in Szenarien steuerbar) oder `schalter` (Schiebeschalter für dauerhafte
  Signale – Schwimmer-, End-, Näherungsschalter; in Wokwi-Szenarien nicht steuerbar). `start`: Signal beim
  Start (Taster immer unbetätigt).
- **Analoggeber:** `bereich` [Anfang, Ende] des Messbereichs, `einheit`, `start` (Wert beim Start),
  `stellen` (Nachkommastellen in der Meldung), optional `rohbereich: [r4mA, r20mA]` (Standard der Plattform:
  Uno 205 … 1023, ESP32 480 … 2400 mV).
- **`kurz`** (optional): Kurzname für die Beschriftung in Wokwi (höchstens 9 bis 12 Zeichen); sonst erstes
  Wort aus `signal_1` bzw. `name`. **`farbe`** überschreibt die Farbe (green, black, red, white, blue, orange).
- **`taste`** (optional, Taster): Taste der Tastatur, die den Taster in Wokwi betätigt.

## 3. Merker

```yaml
merker:
  - {name: M_Pumpe, text: "Schrittkette fordert die Pumpe an"}            # aus GRAFCET-Aktion
  - {name: M_TempSperre, setzen: "[-BT1 < 30 °C]", ruecksetzen: "[-BT1 ≥ 32 °C]"}   # Speicher
  - {name: C_Teile, typ: int, text: "Zähler"}                             # Zähler (speichernde Aktion)
```

Ein Merker hat genau eine Quelle: GRAFCET-Aktion, Speicher (`setzen`/`ruecksetzen`, Standard rücksetzdominant;
`dominant: setzen` für SR) oder Verknüpfung. `typ: int` für Zähler; Zähler stehen nur in Vergleichen.

## 4. GRAFCET

```yaml
grafcet:
  - {schritt: 0, name: "Grundstellung", aktionen: [], transition: "-S1 · -BL1 → 1"}
  - {schritt: 3, name: "Beschicken", aktionen: [-P2, -QA2, -QM1, M_Pumpe], transition: "[-BL2 ≥ 4,5 m] + 10min/X3 → 4"}
  - {schritt: 2, name: "Prüfen", aktionen: ["↑ C_Teile := C_Teile + 1"], transition: "[C_Teile < 10] → 1; [C_Teile = 10] → 3"}
```

- Initialschritt ist Schritt 0 (sonst `initial: true` am Schritt). Ein Schritt ist aktiv; je Zyklus höchstens ein
  Schrittwechsel.
- **Aktionen:** `-QA2` (kontinuierlich), `-M1 wenn <Bedingung>` (mit Zuweisungsbedingung),
  `"↑ X := Wert"` bzw. `"↑ C := C + 1"` (speichernd bei Aktivierung), `"↓ X := 0"` (bei Deaktivierung). Speichernde
  Aktionen in Anführungszeichen.
- **Transition:** `Bedingung → Folgeschritt`; Alternativen mit `;` getrennt, die erste erfüllte gilt (Bedingungen
  müssen sich ausschließen). Parallelverzweigungen („→ 3 und 6“) simuliert der Skill nicht.
- **Zeit** nur am eigenen Schritt: `5min/X1` an der Transition aus X1.

## 5. Zwangssteuerung und Verknüpfungen

```yaml
erzwingen:      # vor den Transitionen, in dieser Reihenfolge; solange die Bedingung gilt, steht die Kette in `nach`
  - {bedingung: "¬-S2", nach: 0, grund: "Stopp: alle Ausgänge sofort 0"}
zuweisungen:    # nach den Aktionen; ein Ziel je Eintrag
  - {ziel: -QA1, bedingung: "M_Pumpe · -BL1 · -S2 · [-BT1 ≥ 30 °C]", grund: "Freigabe der Pumpe"}
```

Ein Ausgang kommt **entweder** aus GRAFCET-Aktionen **oder** aus einer Verknüpfung. Soll die Schrittkette einen
Aktor anfordern und ein Logikplan ihn freigeben, fordert die Kette einen Merker an (`M_Pumpe`), die Verknüpfung
setzt den Ausgang.

**Zyklus** (Sketch und Logikmodell gleich): Eingänge lesen → Speicher → Zwangssteuerung → Transitionen
(nur ohne Zwang) → Aktionen → Verknüpfungen → Ausgänge schreiben → Flanken merken.

## 6. Testfälle

```yaml
testfaelle:
  - nr: T1
    name: "Zyklus"
    zweck: "Schritte X1 … X6, 3 s zwischen Ventil und Pumpe"
    start: {-BL2: 3.0}                       # optional: Startwerte abweichend von der Zuordnungsliste
    ablauf:
      - {erwarte: {X: 0, -QA1: 0}}
      - {tippe: -S1, erwarte: {X: 1, -QA2: 1}}
      - {schrittzeit: 5min, vorher: {X: 1}, erwarte: {X: 2, -QM1: 1}}
      - {setze: {-BL2: 4.6}, erwarte: {X: 4, -QA1: 0}}
      - {druecke: -S2, erwarte: {X: 0}}
      - {loese: -S2, warte: 1s, erwarte: {X: 0}}
```

| Schlüssel | Wirkung |
|---|---|
| `setze` | Signale setzen: Digitalgeber 0/1 (Signal nach Zuordnungsliste), Analoggeber als Wert in der Einheit |
| `tippe` | Taster 200 ms betätigen und lösen (beim Öffner: Signal 0, dann 1) |
| `druecke`, `loese` | Taster betätigen bzw. lösen |
| `warte` | Aufgabenzeit warten (im Zeitraffer umgerechnet wie die Zeiten des GRAFCET) |
| `schrittzeit` | bis zur Zeitschwelle des aktiven Schritts: `vorher` 100 ms davor, `erwarte` 100 ms danach prüfen |
| `erwarte` | nach den Aktionen (bzw. 50 ms danach) prüfen: `X` (aktiver Schritt), Ausgänge, Merker, Eingänge |
| `text` | Kommentar |

**Abdeckung** (Erwartungen aus der Funktionsbeschreibung, nicht aus dem Programm):
1. Grundstellung (alle Ausgänge 0).
2. Normalablauf mit **jeder** Zeit (`schrittzeit` mit `vorher`) und dem Rücksprung.
3. Jede Verzweigung und jedes Ende über ODER (beide Wege, z. B. Füllstand **und** Zeit).
4. Stopp in einem laufenden Schritt, gehaltener Stopp sperrt den Start.
5. **Jede** Schutzfunktion: Wirkung sofort, Meldung, Neustart erst nach Wegfall (Hysterese an beiden Schwellen).
6. Startsperren (Start ohne Freigabe bleibt in X0, keine Störmeldung in der Grundstellung).

Analogwerte nicht genau auf eine Schwelle setzen (4,6 m statt 4,5 m) – der Rohwert ist gerundet.

## 7. Bedingungen

| Bedeutung | Schreibweise | im Sketch |
|---|---|---|
| UND, ODER, NICHT | `-S1 · -B1`, `-B2 + -B3`, `¬-S2` (NICHT vor UND vor ODER, Klammern erlaubt) | `&&`, `||`, `!` |
| Flanke | `↑-S1`, `↓-B1` | `(s1 && !s1_vorher)` |
| Zeit | `5s/X3` (ms, s, min, h; Komma erlaubt: `5,5h/X6`) | `schrittzeit() >= T_X3` |
| Schrittvariable | `X3`, `¬X0` | `schritt == 3`, `schritt != 0` |
| Vergleich | `[-BT1 ≥ 30 °C]`, `[C_Teile = 10]` (≥ ≤ > < = ≠; auch >= <= !=) | `bt1 >= 30.0` |
| immer | `1` | `true` |

Zahlen mit Dezimalkomma, Minus auch als „−“. Kennzeichen und Merker müssen in der Spec stehen; Einheiten im
Vergleich müssen zur Einheit des Messbereichs passen.

## 8. Befehle

```text
wokwi.py entwurf MATERIAL.md [--plattform …] -o SPEC.yaml   Gerüst aus Zuordnungsliste und GRAFCET-Textform
wokwi.py pruefen SPEC.yaml                                    Spec und Schaltung prüfen
wokwi.py erzeugen SPEC.yaml [-o ORDNER] [--ueberschreiben]    Projektordner schreiben
wokwi.py testen SPEC.yaml [--nur-logik] [--zeitablauf B.svg] [--test T1] [--serial] [--protokoll P.md]
wokwi.py blatt SPEC.yaml [-o BLATT.md] [--ueberschreiben]     Begleitblatt
wokwi.py vorschau SPEC.yaml [--png BILD.png]                  Bauteile mit @wokwi/elements, Pinprüfung
wokwi.py wokwi ORDNER [--timeout MS]                          Szenarien mit wokwi-cli
wokwi.py alles SPEC.yaml [--ueberschreiben]                   pruefen → erzeugen → testen → Zeitablauf → blatt
```
