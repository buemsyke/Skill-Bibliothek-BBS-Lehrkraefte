# Diagramm-Specs für edu-diagramm

Ein Diagramm entsteht aus einer kurzen YAML-Datei (Spec). `edu-diagramm` berechnet Größen,
Anschlüsse und Schachtelung selbst und schreibt drei Dateien zum Basisnamen `out`:

| Datei | Zweck |
|---|---|
| `<out>.drawio.svg` | **die eine Datei zum Weitergeben:** zeigt sich im Browser, in Markdown, Moodle und edumaps als Bild und lässt sich in app.diagrams.net weiterbearbeiten |
| `<out>.drawio` | reines draw.io-Format |
| `<out>.preview.svg` | Vorschau ohne Bearbeitungsdaten (Quelle für die PNG-Vorschau) |

`out` ist relativ zum **aktuellen Arbeitsordner** – Befehle immer aus dem Arbeitsordner
aufrufen. Muster aller vier Arten: `assets/spec-*.yaml`.

## 1. Bauart wählen

| Inhalt | Bauart | Befehl | Kürzel im Namen |
|---|---|---|---|
| Blockschaltbild, Anlagen- oder Systemübersicht, Datenfluss, Energiefluss, Regelkreis, Prozess- und Arbeitsablauf, Werkzeugkette, Zyklus | `flow` | `edu-diagramm flow` | `_flow_` |
| Algorithmus, Programmablauf, SPS-Logik als Ablauf (strukturiert, ohne Sprünge) | `struktogramm` | `edu-diagramm struktogramm` | `_nsd_` |
| Datenmodell (Entitäten, Beziehungen, Kardinalitäten) | `chen` | `edu-diagramm chen` | `_chen_` (ohne Attribute zusätzlich `_uebersicht`) |
| Klassen, Schnittstellen, Vererbung | `uml` | `edu-diagramm box` | `_uml_` |
| Tabellen mit Primär- und Fremdschlüsseln | `relational` | `edu-diagramm box` | `_rel_` |

**Nicht damit:** genormte Schaltpläne und technische Zeichnungen – Stromlaufpläne
(DIN EN 60617), Pneumatik- und Hydraulikpläne (DIN ISO 1219), GRAFCET (DIN EN 60848),
R+I-Fließschemata, Bemaßung. Dafür Fachsoftware nutzen (z. B. FluidSIM, CAD,
Herstellerwerkzeuge). Eine vereinfachte Übersicht mit `flow` ist möglich, wird dann aber im
Titel als „vereinfacht, nicht normgerecht" gekennzeichnet. Formeln sind keine Diagramme
(LaTeX bzw. Formeleditor).

Das Kürzel im Dateinamen schaltet in `edu-diagramm validate` die Notationsprüfung ein.

## 2. flow – Block- und Ablaufdiagramme

```yaml
title: "Regelkreis Vorlauftemperatur (vereinfacht)"
type: flow
out: abbildungen/42_flow_regelkreis
spalte: 320        # optional: Rasterbreite in px
zeile: 190         # optional: Rasterhöhe in px
nodes:
  regler:
    x: 0                     # Rasterspalte (auch 0.5 möglich)
    y: 1                     # Rasterzeile
    label: "Regler"          # fett
    lines: ["vergleicht Soll und Ist"]   # weitere Zeilen
    caption: "im Schaltschrank"          # Text unter dem Kasten
    shape: box               # box | rounded | ellipse | raute | note | zylinder
    color: blau              # blau | gruen | gelb | rot | lila | orange | grau | weiss | #rrggbb
  steuerung:
    x: 1
    y: 1
    label: "SPS"
    children:                # Unterkästen in einem Container
      - { id: eingabe, label: "Eingänge" }
      - { id: ausgabe, label: "Ausgänge" }
edges:
  - from: regler
    to: eingabe              # auch Unterkästen sind Ziele
    label: "Stellgröße y"
    style: solid             # solid | dashed
    arrow: single            # single | double | none
    route: direkt            # direkt | links | rechts | unten | oben
notes:
  - { x: 0, y: 2, text: "freier Text im Raster" }
```

**Layoutregeln:**
- Fluss von links nach rechts bzw. oben nach unten; eine Position je Knoten (doppelte
  Positionen überlagern sich).
- **Rückführungen** (Regelkreis, Kreislauf, Schleife) laufen außen herum:
  `route: links`/`rechts` seitlich – für Knoten in **verschiedenen Zeilen** (Muster
  `assets/spec-flow.yaml`: Rückführglied eine Zeile tiefer); `route: unten`/`oben` unter
  bzw. über dem Diagramm – für Knoten in **derselben Zeile** (z. B. Rücklauf eines
  Heizkreises). `links`/`rechts` in derselben Zeile führt edu-diagramm ab 0.2.1 selbst unten
  herum; eindeutiger ist `unten`. Mehrere Umleitungen unten bzw. oben bekommen eigene Bahnen.
- Kreisläufe (Heizkreis, Kältekreis, Hydraulikkreis): Hinweg in einer Zeile, Rückweg mit
  `route: unten` oder als Rechteck über zwei Zeilen. Wirkungsketten und Teufelskreise am
  besten als Rechteck ohne Umleitung (obere Zeile nach rechts, untere nach links, senkrechte
  Kanten an den Enden).
- Eine **seitliche Umleitung endet an der Seite ihres Kastens**: Liegen in der Zeile von Start
  oder Ziel weitere Kästen zwischen Kasten und Rand, läuft die Linie hinter ihnen durch (in der
  Vorschau oft ein scheinbarer Doppelpfeil). Ebenso führen `oben`/`unten` senkrecht durch die
  Spalte. `diagramm_pruefen.py` warnt; Knoten so setzen, dass Start und Ziel außen liegen.
- **Kantenbeschriftung** zwischen zwei Kästen derselben Zeile passt nur in den Zwischenraum
  (bei `spalte: 320` und breiten Kästen oft nur 100–150 px ≈ 15–20 Zeichen); längere Texte an
  senkrechte Kanten setzen oder `spalte` erhöhen – `diagramm_pruefen.py` warnt.
- Formen mit Bedeutung: `raute` = Entscheidung, `zylinder` = Speicher/Behälter/Datenbank,
  `ellipse` = Start/Ende oder Pumpe/Antrieb, `note` = Vorgabe/Dokument, `rounded` = Prozess.
- Farbe trägt Bedeutung (z. B. Energiefluss rot, Signale blau) und wird in der
  Bildunterschrift erklärt; nie nur Farbe als Unterscheidung (Farbsehschwäche) – zusätzlich
  Linienart oder Beschriftung.
- Beschriftungen kurz (≤ 45 Zeichen je Zeile); Details in `lines`.

## 3. struktogramm – Nassi-Shneiderman

```yaml
title: "Struktogramm: Lager nachschmieren"
type: struktogramm
out: abbildungen/42_nsd_schmierung
breite: 460
blocks:
  - "Förderer stillsetzen und sichern"           # Kurzform = Anweisung
  - { typ: anweisung, text: "Schmierplan holen" }
  - typ: verzweigung
    bedingung: "Altfett tritt aus?"
    ja:   ["Altfett auffangen"]
    nein: ["Fett nachdrücken"]                   # [] = einseitige Verzweigung
  - typ: kopfschleife                            # solange … (while)
    bedingung: "solange Schmierstellen offen"
    rumpf: ["Schmiernippel reinigen"]
  - typ: fussschleife                            # wiederhole … solange (do-while)
    bedingung: "solange Druck < 2 bar"
    rumpf: ["Pumpe einschalten"]
  - { typ: aufruf, text: "Probelauf durchführen" }   # Unterprogramm
```

Statt `ja`/`nein` auch `dann`/`sonst`; Zweigbeschriftung über `ja_label`/`nein_label`.
Bedingungen als Frage oder Vergleich formulieren; mehr als rund 25 Blöcke in Unterprogramme
(`aufruf`) aufteilen. Text bricht automatisch um.

## 4. chen – ER-Modell

```yaml
title: "ER-Modell Wartungsaufträge"
type: chen
out: abbildungen/42_chen_wartung
entities:
  Anlage:  { x: 0, y: 0, attrs: [anlagen_nr*, bezeichnung] }   # * = Schlüssel
  Auftrag: { x: 2, y: 0, attrs: [auftrags_nr*, datum] }
relations:
  - { name: betrifft, from: Auftrag, to: Anlage, cardinality: ["(1,1)", "(0,n)"] }
```

- Entitäten mit Attributen **nebeneinander** (gleiche Zeile, jede zweite Spalte); die Raute
  liegt dazwischen. Untereinander überlagern die Attribute die Raute.
- Viele Attribute nebeneinanderliegender Entitäten überlappen: Entitäten weiter auseinander
  (`x: 0, 3, 6`) oder `layout: { col_w: 340 }`. Den Bildrand passt edu-diagramm (ab 0.2.1)
  selbst an.
- Layoutwerte (`layout:`): `col_w`, `row_h`, `margin_x`, `margin_y`, `attr_offset`, `attr_spacing`.
- Kardinalitäten in der Schreibweise des Unterrichts (Min-Max `(1,n)` oder `1:n`) –
  einheitlich in allen Diagrammen einer Reihe.

## 5. uml und relational – Klassen und Tabellen (`edu-diagramm box`)

```yaml
title: "Klassen Messwerterfassung"
type: uml                       # oder: relational
out: abbildungen/42_uml_messung
classes:                        # bei relational ebenfalls classes:
  Sensor:
    x: 0
    y: 0
    stereotype: interface
    attrs: ["+ messen(): float"]
  Temperatursensor:
    x: 0
    y: 1
    attrs: ["- pin: int", "---", "+ messen(): float"]   # --- trennt Attribute und Methoden
relations:
  - { name: "", from: Temperatursensor, to: Sensor, kind: implements }
```

- UML-Kantenarten (`kind`): `association` (Standard), `inheritance`/`extends`,
  `implements`/`realization`, `dependency`, `aggregation`, `composition`;
  `cardinality: ["1", "0..*"]` an den Enden.
- Relational: Spalten als `"name: TYP"`, Primärschlüssel `*`, Fremdschlüssel `^`
  (`"kunde_id^: INT"`).

## 6. Erzeugen, prüfen, ansehen

```bash
python3 scripts/diagramm_pruefen.py diagramme/42_flow_regelkreis.yaml     # Spec prüfen
edu-diagramm flow diagramme/42_flow_regelkreis.yaml                       # installiert
python3 scripts/edu.py diagramm flow diagramme/42_flow_regelkreis.yaml    # mitgeliefert
python3 scripts/edu.py diagramm validate abbildungen/*.drawio.svg           # Notation prüfen
python3 scripts/vorschau_png.py abbildungen/42_flow_regelkreis.preview.svg  # PNG ansehen
```

Fehlermeldungen von edu-diagramm nennen den fehlenden Schlüssel bzw. die YAML-Zeile.
Änderungen immer in der Spec, dann neu erzeugen – die `.drawio.svg` kann zusätzlich in
app.diagrams.net nachbearbeitet werden, geht dann aber beim nächsten Erzeugen verloren.

## 7. Einbinden

| Ziel | so |
|---|---|
| Markdown, Schülerseiten | `![Regelkreis der Vorlauftemperatur](abbildungen/42_flow_regelkreis.drawio.svg)` |
| Projekt mit `lessons/` | Ausgabe nach `lessons/NN_slug/diagrams/NN_v01_flow_thema` (Lösungsdiagramme `NN_l01_…` nach `solutions/diagrams/` – sonst landen sie in der Schülerausgabe) |
| Word, PowerPoint | PNG aus `vorschau_png.py` einfügen (SVG nur in neueren Office-Versionen) |
| edumaps, Moodle | `.drawio.svg` oder PNG hochladen |
| Weiterbearbeiten | `.drawio.svg` in app.diagrams.net öffnen (Datei → Öffnen bzw. Drag & Drop) |

**Barrierefreiheit:** zu jedem Diagramm ein Alternativtext (was zeigt es, in einem Satz) und
eine Bildunterschrift, die Farben und Linienarten erklärt.
