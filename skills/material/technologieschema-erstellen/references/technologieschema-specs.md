# Technologieschema – Spec-Referenz

Eine Spec (YAML) beschreibt die Anlage; `edu-technologieschema` zeichnet sie. Diese Seite ist die
vollständige Referenz: Kopf, Bauteile, Anker, Maße, Rezepte, typische Fehler. Die Liste aller
Bauteile mit ihren Schlüsseln gibt auch `python3 scripts/edu.py technologieschema typen` aus.

## 1. Kopf der Spec

```yaml
titel: "Abbildung 1 – Technologieschema der Biegestation"   # → <title> im SVG (Pflicht)
alt: "Ein Satz: was das Bild zeigt, mit den Kennzeichen."    # → <desc> (Pflicht)
out: abbildungen/46_biegestation                              # ohne Endung → .svg und .drawio.svg
breite: 720                                                   # Bildbreite in Pixeln (Pflicht, außer mit typ: grafcet)
hoehe: 530                                                    # Höhe des Bildes ohne Fußzeile (Pflicht, außer mit typ: grafcet)
fusszeile:                                                    # optional, unter dem Bild
  - "Grundstellung: alle Zylinder eingefahren."
hinweis: "Quelle der Vorlage …"                               # optional, als Kommentar im SVG
elemente: [ … ]                                               # Liste der Bauteile (Pflicht)
```

- **Breite 720–780, Höhe 450–600** passt neben Teilaufgaben auf eine A4-Seite. Das Bild
  skaliert; Schriftgröße im Bild 11–13 Pixel bei dieser Breite.
- **Kennzeichen** (`id`) sind immer Referenzkennzeichen nach DIN EN IEC 81346-2:2020, ein Schalter
  für andere Schreibweisen gibt es nicht (siehe Abschn. 3a).
- Zeichenreihenfolge = Listenreihenfolge: später genannte Teile liegen **oben**. Rohre und
  Linien nach den Teilen nennen, an die sie anschließen.

## 2. Koordinaten

- Ursprung links oben, x nach rechts, y nach unten.
- **Rechteckige Teile** (`rechteck`, `behaelter`, `band`, `bedienfeld`, `ampel`, `zylinder`):
  `x, y` = obere linke Ecke. **Runde Teile** (`kreis`, `sensor`, `taster`, `leuchte`, `motor`,
  `pumpe`, `ventil`): `x, y` = Mittelpunkt.
- Raster von 10 Pixeln einhalten, mindestens 40 Pixel Rand, 24 Pixel Abstand zwischen
  Beschriftungen. Bauteile nach **Bereichen** ordnen (Bedienfeld oben links, Antriebe unten,
  Werkstückfluss von links nach rechts); Prozess und Bedienung nicht mischen.
- Typische Größen: Zylinder 36 × 110 (Stange 60), Taster r 14–17, Leuchtmelder r 13–17, Motor
  r 22–24, Sensor-Block 8 × 12, Rohr 12–14 breit, Ventil Halbbreite 9.

## 3. Bauteile

Gemeinsame Schlüssel (jedes Bauteil): `id` (Kennzeichen, fett im Bild und in der Legende),
`name` (Kurzbezeichnung, kursiv im Bild: „Spannen“), `lage` (Beschriftung `oben | unten | links |
rechts | keine`), `abstand`, `ref` (Name nur für Anker, ohne Legende), `betriebsmittel` und
`funktion` (nur für die Legende, nicht im Bild), `legende: false` (nicht in die Legende).

| typ | Pflicht | wichtige optionale Schlüssel |
|---|---|---|
| `zylinder` | x, y | `ausfahrt` unten/oben/rechts/links, `laenge` 110, `breite` 36, `stange` 56, `feder`, `werkzeug` keine/platte/keil, `werkzeug_b`, `sensoren` |
| `ventil` | x, y | `achse` senkrecht/waagerecht, `groesse` 9, `spule` rechts/links/oben/unten/keine |
| `sensor` | x, y | `art` block/rolle/lichtschranke/kontakt/initiator, `stiel` |
| `taster` | x, y | `r`, `symbol` keins/pfeil_auf/pfeil_ab/doppelpfeil_auf/ring/not_halt, `farbe`, `text` |
| `leuchte` | x, y | `r`, `farbe`, `text` (statt X, z. B. `rt`, `gn`) |
| `motor` | x, y | `r`, `phasen` („3~“, „1~“, „=“) |
| `pumpe` | x, y | `r`, `richtung` (Förderrichtung) |
| `behaelter` | x, y, b, h | `form` tank/silo/trichter, `offen`, `fuellstand` 0–1 (nur tank), `kopf`, `auslass`, `fuellung` |
| `band` | x, y, b, h | `winkel` (negativ = steigt nach rechts), `rollen` |
| `bedienfeld` | x, y, b, h, eintraege | `titel`, `spalten` 3 |
| `ampel` | x, y, b, h, lampen | Liste von Lampentexten, z. B. `[rt, ge, gn]` |
| `rohr` | punkte | `weite` 14, `radius` 12 (gerundete Ecken), `route` |
| `linie` | punkte | `stil` normal/duenn/dick/gestrichelt, `pfeil` kein/ende/anfang/beide, `radius`, `route` auto/hv/vh, `schraeg` |
| `rechteck` | x, y, b, h | `fuellung`, `linie`, `rundung`, `text` |
| `kreis` | x, y, r | `fuellung`, `linie`, `text` |
| `polygon` | punkte | `fuellung`, `linie`, `offen` |
| `symbol` | x, y, symbol | `drehung` 0/90/180/270, `spiegeln`, `groesse` (1 = 10 px je Rasterschritt), `text` – Schaltzeichen, Abschn. 3c |
| `knoten` | punkt | `r` – Verbindungspunkt (ausgefüllt) an einem Anker oder bei [x, y] |
| `grafcet` | kette | `x`, `y`, `zuordnung`, `rahmen` – GRAFCET nach DIN EN 60848, Abschn. 5a |
| `text` | x, y, text | `groesse`, `ausrichtung` links/mitte/rechts, `fett`, `kursiv` |
| `etikett` | x, y, text | `ziel` (Anker oder [x, y]; zeichnet die Hinweislinie), `ausrichtung`, `kursiv` |

**Füllungen** (nur Graustufen, in Schwarzweiß lesbar): `weiss`, `hellgrau`, `grau`, `mittelgrau`,
`dunkelgrau`, `schwarz`, `keine`; Muster `schraffur`, `punkte`, `ziegel`.

### Zylinder und Sensoren

```yaml
- typ: zylinder
  id: "-MM1"
  name: Spannen
  funktion: "Spannzylinder, spannt den Zuschnitt"
  x: 556          # obere linke Ecke des Gehäuses
  y: 150
  ausfahrt: unten # Stange fährt nach unten aus (Standard)
  stange: 60      # Stange zwischen Gehäuse und Werkzeug
  werkzeug: platte
  werkzeug_b: 56
  sensoren:
    - {id: "-B1", pos: 0.08, seite: rechts, funktion: "meldet: eingefahren"}
    - {id: "-B2", pos: 0.41, seite: rechts, funktion: "meldet: ausgefahren"}
```

`pos` liegt zwischen 0 (Boden) und 1 (Stangenseite). `seite` ist die Seite im Bild
(`links/rechts` bei senkrechtem, `oben/unten` bei waagerechtem Zylinder). Die Beschriftung des
Zylinders weicht den Sensoren aus. `feder: true` zeichnet die Rückstellfeder
(einfachwirkend; die Legende nennt es dann so).

### Bedienfeld

Die Einträge ordnet das Werkzeug selbst in einem Raster an (`spalten`, Standard 3); ein Eintrag
`{typ: leer}` lässt eine Zelle frei. Erlaubt sind `taster` und `leuchte` ohne `x`, `y`.

```yaml
- typ: bedienfeld
  x: 40
  y: 40
  b: 230
  h: 112
  titel: Bedienpult
  eintraege:
    - {typ: taster, id: "-S1", name: Start, r: 17}
    - {typ: taster, id: "-S2", name: Not-Halt, symbol: not_halt, r: 17}
    - {typ: leuchte, id: "-P1", name: Betrieb, r: 17}
```

Not-Halt: `symbol: not_halt` zeichnet den Pilz; die Farbregeln (rot/gelb) stehen in der Legende
oder im Text, nicht im Bild (Graustufen).

### 3a. Referenzkennzeichen – DIN EN IEC 81346-2:2020

Form `-` + 1 bis 3 Großbuchstaben + Zählnummer, ohne Leerzeichen, in Anführungszeichen:
`id: "-S1"`. Das Werkzeug prüft jedes Kennzeichen:

| Prüfung | Beispiel für ❌ |
|---|---|
| Form | `S1`, `- S1`, `-s1` (Hinweis: gemeint ist wohl `-S1`) |
| Klasse und Unterklasse in Tabelle 2 der Norm | `-AZ1` (Klasse A entfällt), `-MX1`, `-Y1` (reserviert) |
| Ausgabe 2009 | `-SF1` (heißt -SJ), `-RZ1` (heißt -RN) |
| Klasse passt zum Bauteil | Taster nur **S**, Sensor **B**, Zylinder und Motor **M**, Pumpe **G**, Ventil **Q/R/S**, Leuchtmelder und Ampel **P**, Behälter **C** |
| Unterklasse passt zum Bauteil | Zylinder -MM, Motor -MA/-MB, Pumpe -GP/-GQ, Leuchtmelder -PF |
| **eine Tiefe je Klasse** | `-M1` neben `-MM1` ❌; `-MA1` neben `-MM1` ✔ |

Hinweis ⚠ bei zu langer Schreibweise: `-MM1`, `-MM2` ohne zweite Art in der Klasse → `-M1`, `-M2`.
Die Entscheidung: **Klasse allein**, solange sie nur eine Art Betriebsmittel enthält (Fachberatung
31.10.2026); verschiedenartige Betriebsmittel einer Klasse (Motor und Zylinder, Lichtschranke und
Zylinderschalter) bekommen überall die Unterklasse. Typische Unterklassen: -MA Motor, -MM
Zylinder, -MB Ventilspule, -BR Lichtschranke, -BG Zylinderschalter und Näherungsschalter, -BL
Füllstand, -QM Wegeventil, -QA Schütz, -PF Leuchtmelder, -SJ Drucktaster (Tabelle in
`references/normen-technik.md`, Abschn. 2). Entsprechungen einer fremden Vorlage (S1, Y1 → -S1,
-Q1) im Schemablatt nennen.

### 3b. Linien und Rohre – rechtwinklig

Wirkungslinien, Rohre und Hinweislinien verlaufen **waagerecht oder senkrecht**. Gibt die Spec zwei
Punkte, die weder auf einer Höhe noch auf einer Achse liegen, führt das Werkzeug die Linie mit
**einem Knick**: `route: hv` erst waagerecht, `vh` erst senkrecht, `auto` (Standard) richtet sich nach
dem Anker (`links`/`rechts` → waagerecht heraus, `oben`/`unten` → senkrecht heraus, am Ziel
entsprechend). Ist der Versatz kleiner als 15 Pixel, meldet `pruefen` ⚠ – meist stehen zwei Teile
nicht auf einer Achse; besser Position oder Anker angleichen (`"Y3@rechts"` zu `"Z2@oben_links:0,0"`
nur, wenn y gleich ist). Eine Schräge gibt es nur mit `schraeg: true` bei `linie`. Geneigte Bauteile
(`band` mit `winkel`) bleiben möglich; Linien zu ihnen laufen trotzdem rechtwinklig.

### 3c. Schaltzeichen nach DIN EN 60617

`typ: symbol` setzt ein genormtes Schaltzeichen. Namen, Klassen, Anschlusspunkte und Herkunft aller
Zeichen: `references/schaltzeichen.md` (aktuell mit `edu-technologieschema symbole`).

```yaml
- {typ: symbol, symbol: schliesser_rueckgang, id: "-S1", name: Start, funktion: "startet", x: 120, y: 200, lage: links}
- {typ: symbol, symbol: schliesser, ref: kontakt, gehoert_zu: "-Q1", x: 220, y: 200}   # Hilfskontakt des Schützes -Q1
- {typ: symbol, symbol: motor_drehstrom, id: "-M1", x: 300, y: 300, drehung: 180}
- {typ: linie, punkte: ["-S1@an1", "kontakt@an1"]}       # Anschlüsse an1, an2 … folgen Drehung und Spiegelung
- {typ: knoten, punkt: "-S1@an1"}                        # Verbindungspunkt
```

- **Lage:** Die Zeichen stehen in ihrer natürlichen Lage (Kontakte, Spulen, Meldeleuchte senkrecht;
  Widerstand, Kondensator, Diode waagerecht); `drehung` dreht im Uhrzeigersinn, `spiegeln` kehrt
  links und rechts um. Texte im Zeichen (M, 3~) bleiben aufrecht.
- **Kennzeichen:** Jedes Zeichen kennt die Klassen, die zu ihm passen (Schließer als Taster -S, als
  Sensor -B, als Relaiskontakt -K, als Schützkontakt -Q). Ein unpassendes Kennzeichen ist ❌.
- **Mehrere Zeichen, ein Betriebsmittel:** Spule und Kontakte eines Schützes tragen dasselbe
  Kennzeichen. Das erste Teil bekommt `id` (Legendenzeile), jedes weitere `gehoert_zu: "-Q1"`;
  für Anker bekommt es ein `ref`.
- **Herkunft:** *Liste* = Form mit einer Vorlage abgeglichen (Wikipedia-Liste der Schaltzeichen
  (Elektrik/Elektronik); Näherungsschalter und Betätigungsarten: Zeichengalerien mit Nummern der
  EN-60617-Reihe). *zusammengesetzt* = aus solchen Zeichen gebildet (Taster = Kontakt mit Rückgang +
  Betätigung). *🔎 abgleichen* = nach Lehrbuch-Formensprache gezeichnet; vor dem Einsatz in Aufgaben mit der
  Norm oder dem eingeführten Tabellenbuch vergleichen und im Schemablatt vermerken. Alle Vorlagen sind
  Sekundärquellen – für Prüfungsaufgaben gilt die Norm (🔎 Normtext prüfen).
- **Taster und Betätigungsarten:** Fertige Zeichen: `taster_schliesser`, `taster_oeffner`,
  `drucktaster_schliesser`, `drucktaster_oeffner`, `notaus_taster`. Für jede andere Betätigung ein
  Kontakt mit Zusatz: `{typ: symbol, symbol: schliesser, betaetigung: ziehen}`. `betaetigung` zeichnet die
  gestrichelte **Wirkverbindung** von der Klingenmitte nach links (`wirklaenge`, Standard 2) mit dem
  Endzeichen: `hand`, `kippen`, `drucken`, `ziehen`, `drehen`, `not_aus` (Pilz), `thermisch`, `annaehern`,
  `beruehren`, `annaehern_eisen`, `annaehern_magnet`, `handrad`, `fuss`, `schluessel`, `nocken`, `pegel`,
  `motor`, `elektromagnet`. Nur Zeichen mit Wirkverbindung (Spalte *Wirkv.* in `schaltzeichen.md`: Schließer,
  Öffner, Wechsler, Schütz-, Leistungs- und Trennschalter) nehmen einen Zusatz; die Rastung (Verriegelung) des
  Not-Halt-Tasters zeigt die Quelle nicht – im Text nennen.
- **Näherungsschalter:** `naeherungsschalter_schliesser` (07-20-02), `…_magnet_schliesser` (07-20-03),
  `…_eisen_oeffner` (07-20-04), `naeherungsschalter_oeffner`, dazu die Sensoren `naeherungssensor`
  (07-19-01), `beruehrungssensor` (07-19-04) und das Blocksymbol `naeherungseinrichtung_block` (07-19-02).
  Kennzeichen Klasse B (Zylinderschalter und Näherungsschalter -BG, Lichtschranke -BR). Induktiv,
  kapazitiv oder optisch unterscheidet das Zeichen nicht – in der Legende nennen (`betriebsmittel`).
- **Nicht enthalten:** Pneumatik- und Hydraulikzeichen (ISO 1219-1), Rastung und Handbetätigung
  *mit Schutz gegen zufällige Berührung* (Zeichen nicht eindeutig lesbar), Rolle (Endschalter).
- Ein vollständiger Stromlaufplan nach DIN EN 61082 ist nicht Ziel dieses Skills; Auszüge
  (Steuerstromkreis, Anschluss von Sensoren) sind möglich (Muster `assets/spec-steuerstromkreis.yaml`,
  `assets/spec-naeherungsschalter.yaml`).

## 4. Anker – Linien und Rohre an Bauteile hängen

Statt Koordinaten auszurechnen, steht in `punkte` (oder `ziel`) ein Verweis auf ein Bauteil:

```yaml
punkte: ["-G1@links", "-Q1@rechts"]         # von der Pumpe zum Ventil
punkte: ["-Q1@links", [350, 70], [350, 200]] # Anker, dann feste Punkte
punkte: ["-MM1@spitze:64,-32", "-MM1@spitze:64,0"]  # Versatz dx,dy nach dem Doppelpunkt
```

Form `"ID@punkt"` (immer in Anführungszeichen; `ID` ist `id` oder `ref`). Punkte: `mitte`,
`oben`, `unten`, `links`, `rechts`, `oben_links`, `oben_rechts`, `unten_links`, `unten_rechts`.
Zusätzlich: Zylinder `hinten` (Boden) und `spitze` (Ende der Stange samt Werkzeug; die übrigen
Punkte liegen am Gehäuse, nicht am Werkzeug); Ventil
`oben/unten/links/rechts` liegen am Symbol, nicht an der Spule; Band `links/rechts` an den
Rollen. Verweise dürfen auf Teile zeigen, die **später** in der Liste stehen.

## 5. Rezepte

- **Bewegungsrichtung:** `linie` mit `pfeil: ende` neben dem Werkzeug, dazu Satz in der Fußzeile
  („Pfeile: Bewegung beim Ausfahren“).
- **Lichtschranke:** zwei `sensor`-Teile `art: lichtschranke` (Sender mit `id`, Empfänger mit
  `legende: false`) und eine `linie` `stil: gestrichelt` dazwischen.
- **Schwimmerschalter an der Behälterwand:** `sensor` `art: kontakt`, `stiel: links`, `x` auf der
  Wandlinie des Behälters.
- **Füllstand zeigen:** `behaelter` `fuellstand: 0.45`; Sensoren darüber/darunter passend setzen.
- **Rohr durch Ventil und Pumpe:** mehrere `rohr`-Stücke zwischen den Ankern; die Pumpe zeigt
  mit `richtung` die Förderrichtung.
- **Hinweis auf ein Teil ohne Kennzeichen:** `etikett` mit `ziel`.
- **Hintergrund:** `rechteck` mit `fuellung: schraffur` (Boden), `behaelter` mit `ziegel` o. Ä.

## 5a. GRAFCET – eigenes Bauteil (`typ: grafcet`)

GRAFCET wird **nie aus Rechtecken und Linien zusammengesetzt**. Die Spec nennt die Struktur; Lage und
Normsymbole kommen aus dem Werkzeug, die Prüfung kennt die Regeln der DIN EN 60848. `breite` und `hoehe`
dürfen fehlen (werden berechnet). Muster: `assets/spec-grafcet.yaml` (Kette, speichernd),
`assets/spec-grafcet-verzweigung.yaml` (parallel, alternativ, alle Aktionsarten, Zähler),
`assets/spec-grafcet-teil.yaml` (einschließender Schritt, Zwangssteuerung),
`assets/spec-grafcet-symbole.yaml` (Symboltafel aus Einzelteilen).

```yaml
elemente:
  - typ: grafcet
    zuordnung:                       # optional, sehr empfohlen: Zuordnungsliste der Aufgabe
      eingaenge: ["-S1", "-B1"]
      ausgaenge: ["-M1", "-P1"]
    kette:
      - {schritt: 0, art: initial, aktionen: ["↑ -P1 := 0"]}
      - {transition: "-S1 · ¬-B1", kommentar: "Start, Platz frei"}
      - schritt: 1
        aktionen:
          - ["↑ -P1 := 1", {text: "-M1", kommentar: "Band läuft"}]   # eine Zeile, nebeneinander
          - {text: "C_Teile := 1", art: ereignis, bedingung: "↑-B2"}  # zweite Zeile
      - {transition: "5s/X1"}
      - sprung: 0
```

**Bestandteile der `kette`** (Schritt und Transition wechseln sich ab):

| Eintrag | Schlüssel |
|---|---|
| `schritt: 3` (Name auch `1.1`, `M4`, `9a`) | `art` normal/initial/makro/einschliessend, `aktivierung: true` (das `*`), `aktionen`, `kommentar`, `bezeichnung` (nur Textform: „1 Fördern“) |
| `transition: "-B1"` (`1` = immer erfüllt, unterstrichen) | `art` normal/quelle/schluss, `name` (links in Klammern), `kommentar` |
| `alternativ: [[…], […]]` | Liste der Äste; jeder Ast beginnt mit seiner Transition und endet mit einer Transition oder einem `sprung` |
| `parallel: [[…], […]]` | Liste der Äste unter der gemeinsamen Transition; jeder Ast beginnt und endet mit einem Schritt, danach folgt die gemeinsame Transition |
| `sprung: 0` | Rücksprung: Linie mit Pfeil nach oben, neben dem eigenen Ast |

Am Bauteil selbst: `x`, `y` (linke obere Ecke; fehlt `x`, steht der nächste GRAFCET rechts neben dem vorigen),
`zuordnung`, `rahmen: {oben: "2", unten: "Bezeichnung"}` (Rahmen des einschließenden Schritts bzw. Teil-GRAFCET).

**Aktionen:** Eine flache Liste steht **nebeneinander**; enthält sie Listen, ist jeder Eintrag eine eigene Zeile.

| Schreibweise | Art | Zeichnung |
|---|---|---|
| `"-M1"` | kontinuierlich | Rechteck |
| `{text: "-M1", bedingung: "-B1 · -B2"}` | mit Zuweisungsbedingung | Strich oben, Bedingung daneben |
| `{text: "-M1", art: verzoegert, bedingung: "5s/X3"}` | verzögert | wie oben |
| `{text: "-M1", art: zeitbegrenzt, bedingung: "5s/X3"}` | zeitbegrenzt | wie oben, Zeit mit Überstrich |
| `"↑ -Q1 := 1"` | speichernd bei Aktivierung | im Rechteck `-Q1 := 1`, **Pfeil nach oben** an der linken Kante |
| `"↓ -Q1 := 0"` | speichernd bei Deaktivierung | im Rechteck `-Q1 := 0`, **Pfeil nach unten** an der linken Kante |
| `{text: "-Q1 := 1", art: ereignis, bedingung: "↑-B1"}` | speichernd bei Ereignis | Strich mit **Fähnchen** nach links, Ereignis daneben |
| `"G5 {INIT}"`, `"G5 { }"`, `"G5 {3,4,8}"`, `"G5 {*}"` | Zwangssteuerung | Doppelrahmen |

Jede Aktion kann `kommentar` tragen (höchstens einer je Zeile). **Kommentare** erscheinen in Anführungszeichen
nach DIN EN 60848, einzeilig oder umbrochen (eigener Umbruch mit `\n`); Rechtecke einer senkrechten Linie
werden gleich breit, ihre Kommentare stehen in einer Spalte.

**Bedingungen:** `·` oder `*` UND, `+` ODER, `¬-B1` oder `!-B1` NICHT (**als Überstrich gezeichnet**, auch
`¬(-B1 + -B2)`), `↑-B1`/`↓-B1` Flanke, `5s/X3` Zeit, `[C_Teile > 9]` Vergleich. Schreibweise wird vereinheitlicht
(`0.5s / X2` → `0,5s/X2`). Überstrich und Unterstrich sind im Bild echte Linien, damit eine Negation in jedem Programm
sichtbar bleibt (Word stellt `text-decoration` in SVG nicht verlässlich dar); in draw.io sind sie Textformat.

**Was `pruefen` beim GRAFCET meldet:**

| Stufe | Befund |
|---|---|
| ❌ | speichernde Aktion **ohne Zuweisung** (`↑ -M1`), `:=` **ohne Auslöser** (`-Q1 := 1`); Schritt an Schritt, Transition an Transition, Transition ohne Folgeschritt; Astanfang und -ende passen nicht; `sprung` ins Leere; doppelter Schrittname; dieselbe Variable kontinuierlich und speichernd; Kennzeichen nicht nach Norm (Ausnahme unten); mit `zuordnung`: Kennzeichen nicht in der Liste, Eingang als Aktion |
| ⚠ | Alternativbedingungen schließen sich nicht aus (reine Logik: mit Beispielbelegung); zugewiesen, aber nie auf 0 gesetzt; `5s/X7` ohne Schritt 7; Schritt nie aktiv; kein Initialschritt; Eintrag der `zuordnung` nicht verwendet; `S1` ohne Bindestrich; Linien kreuzen sich; GRAFCET aus Grundformen |

**Kennzeichen einer fremden Aufgabe:** Gibt eine vorhandene Aufgabe Kennzeichen vor, die nicht der Ausgabe 2020
entsprechen (`-SF1`), gehören sie in `zuordnung`: Dann bleiben sie und `pruefen` meldet ⚠ statt ❌.

**Textform:** `edu-technologieschema textform schema/….yaml` erzeugt die Tabelle Schritt | Aktion | Transition
(Notationsblatt Abschn. 5, `bmk_pruefen.py` T.9) aus derselben Quelle – nicht von Hand zusätzlich schreiben.

**Einzelteile** (`grafcet_schritt`, `grafcet_transition`, `grafcet_balken`, `grafcet_rahmen`, Schlüssel mit
`edu-technologieschema typen`): nur für Symboltafeln und Einzelzeichen mit festen Koordinaten, nie für Ketten.

## 5b. Funktionsplan und Netzplan aus Grundformen

Für diese Zeichnungen gibt es keinen eigenen Bauteiltyp; sie entstehen aus `rechteck`, `text` und
`linie` (rechtwinklig, Anker oder Koordinaten). Alle Teile tragen `ref` und `legende: false`, denn
sie sind keine Betriebsmittel. Muster: `assets/spec-fup.yaml`.

**Funktionsplan** (Bausteine wie DIN EN 61131-3): Baustein `rechteck` (Breite 70–80), Funktionszeichen
als `text` oben im Baustein (`&`, `>=1`, `>=`, `=1`; ⚠ „liegt auf Element“ gewollt); Eingänge als
waagerechte `linie` von links mit Operand als `text` (`ausrichtung: rechts`) davor, Ausgang rechts mit
Operand dahinter; Negation als `kreis` r 4 am Bausteinrand; Signalfluss von links nach rechts,
Verbindungen zwischen Bausteinen ohne Knick, wo die Höhen sich angleichen lassen. Analogwerte als
Vergleicher mit physikalischem Wert und Einheit („30 °C“), nicht als Rohwert.

**Netzplan:** Gebäude als `rechteck` mit `rundung: 6`, Titel als fetter `text` über dem Rahmen,
Geräte als `rechteck` mit `text`; Linienarten mit Bedeutung in der Fußzeile (z. B. dick =
Lichtwellenleiter, dünn = Kupfer, gestrichelt = VPN-Tunnel bis zum Endpunkt); Verbindungen enden am
Gerät (Switch), nicht an der Gebäudewand; IP-Adressen besser in einer Tabelle als im Bild.

## 6. Prüfung – was `pruefen` meldet

| Stufe | Befund |
|---|---|
| ❌ | unbekannter `typ` oder Schlüssel (mit Vorschlag bei Tippfehlern), fehlende Pflichtangabe, falscher Wert, doppeltes Kennzeichen, Kennzeichen nicht nach 81346, unbekannter Anker, Teil außerhalb des Bildes, Sensorseite passt nicht zur Zylinderachse |
| ⚠ | überlappende Beschriftungen, Beschriftung auf einem Bauteil, Linie durch eine Beschriftung, Text ragt über den Rand, Kennzeichen ohne `funktion`/`name` in der Legende |

Jedes ❌ beheben, jedes ⚠ ansehen (Spec anpassen: `lage`, `abstand`, Position). Die Rahmen der
Texte sind geschätzt; die PNG-Vorschau bleibt die letzte Instanz.

## 6a. Bearbeitbare Fassung (`.drawio.svg`)

`svg` schreibt neben dem Bild eine `.drawio.svg`: dasselbe Bild, dazu im Attribut `content` das
draw.io-Modell. So wird aus der Spec:

| Spec | in diagrams.net |
|---|---|
| Bauteil (`zylinder`, `ventil`, `symbol` …) | eine Form (Stencil); Andockpunkte = Anker (`unten`, `an1`, `spitze` …) |
| Sensor am Zylinder, Eintrag im Bedienfeld | eigene Form in der Gruppe des Zylinders bzw. Bedienfelds |
| `id`, `betriebsmittel`, `funktion` | Formdaten *Referenzkennzeichen*, *Betriebsmittel*, *Aufgabe* (Tooltip) |
| Kennzeichen, Kurzname, Innentext | Textzellen, mit dem Bauteil gruppiert |
| `linie` (Pfeil, gestrichelt) | Verbinder, rechtwinklig, an den Ankern angeschlossen |
| GRAFCET: Schritt mit Aktionen und Kommentaren, Transition mit Bedingung | je eine Gruppe; Wirkverbindungen als Verbinder an den Formen, Verzweigungsbalken mit Andockpunkten je Ast, Überstrich als Textformat |
| `rohr` | Verbinder als Doppellinie (`shape=link`), angeschlossen |
| `etikett` mit `ziel` | Text plus Hinweislinie zum Ziel |
| `band` mit `winkel` | gedrehte Form |
| Füllung `schraffur`, `ziegel` | Linien in der Form (bei Rechtecken); sonst Grau |

`knoten` (Verbindungspunkte) sind eigene Formen und wandern beim Verschieben nicht mit – nach dem
Umbau nachziehen. Der Export ist gegen den draw.io-Viewer geprüft (Lage wie im SVG, keine Versätze an
Anschlüssen); eigene Formen der Lehrkraft lassen sich danach frei ergänzen.

## 7. Häufige Fehler

- Kennzeichen ohne Anführungszeichen (`id: -S1` ist in YAML eine Liste): immer `id: "-S1"`.
- `x, y` bei runden Teilen als Ecke gelesen: sie sind der **Mittelpunkt**.
- Sensor `seite` passt nicht zur Achse: bei `ausfahrt: rechts` nur `oben` oder `unten`.
- Bild zeigt eine andere Grundstellung als die Fußzeile (Füllstand, Zylinderstellung).
- Linie knickt ⚠: Teile liegen nicht auf einer Achse – Koordinaten angleichen statt den Knick hinzunehmen.
- Zu viele Teile: lieber zwei Bilder (Anlage, Bedienfeld) als eines mit mehr als etwa 15 Bauteilen.
