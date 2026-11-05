<!-- Assistenten-Fassung des Skills 'fachdiagramm-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
# Fachdiagramm erstellen

## Zweck
Abbildungen für Arbeitsblätter, Infotexte, Tafelbilder und Klassenarbeiten, die **fachlich
stimmen, gleich aussehen und sich später ändern lassen**. Claude beschreibt das Diagramm in
einer kurzen YAML-Spec; Größen, Anschlüsse und Schachtelung berechnet `edu-diagramm`. Keine
Kastengrafik aus Zeichen, keine von Hand geschriebenen SVG.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Diagrammblatt). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Bauarten

| Inhalt | Bauart | Muster |
|---|---|---|
| Blockschaltbild, Anlagenübersicht, Energie-/Datenfluss, Regelkreis, Arbeitsablauf | `flow` | `assets/spec-flow.yaml` |
| Algorithmus, Programm- oder SPS-Ablauf (strukturiert) | `struktogramm` | `assets/spec-struktogramm.yaml` |
| Ablaufsteuerung mit Schritten und Transitionen (GRAFCET), Funktionsplan, Anlagenbild | `technologieschema-erstellen` | – |
| Datenmodell | `chen` | `assets/spec-chen.yaml` |
| Klassen, Schnittstellen / Tabellen mit Schlüsseln | `uml` / `relational` | `assets/spec-uml.yaml` |

**Grenze:** keine genormten Schaltpläne (DIN EN 60617), Pneumatik-/Hydraulikpläne
(DIN ISO 1219), GRAFCET (DIN EN 60848) oder technischen Zeichnungen – dafür Fachsoftware.
Eine vereinfachte Übersicht mit `flow` ist möglich und wird als „vereinfacht, nicht
normgerecht" betitelt.
**Keine Zeichnung aus Zeichen:** Struktogramme, Abläufe, Blockschaltbilder und Datenmodelle stehen
in keinem Artefakt als ASCII-Art oder Mermaid – auch nicht in Lösung und Erwartungshorizont
(Skill-Vertrag Abschn. 3). Findet sich eine, ersetzt dieser Skill sie durch ein SVG.

## Eingaben
- **Pflicht (sonst Rückfrage):** was dargestellt werden soll – Beschreibung, Material,
  Skizze, ASCII-Zeichnung oder Lernsituation.
- **Wichtig, sonst Annahme:** Verwendung (Arbeitsblatt, Lösung, Tafelbild), Detailgrad,
  Fachbegriffe und Schreibweisen des Unterrichts (z. B. Kardinalitäten), Zielformat (Markdown,
  Word, edumaps).
- **Optional:** Planungsakte, Projektordner mit `lessons/` (Namenskonvention übernehmen).

## Leitlinien (verbindlich)
1. **Fachlich richtig vor schön:** Bauteile, Flussrichtungen, Größen und Begriffe wie im
   Material bzw. in Herstellerunterlagen; Vereinfachungen benennen (Diagrammblatt). Nichts
   erfinden – unklare Zusammenhänge als `🔎 Prüfen:`.
2. **Eine Aussage je Diagramm;** lieber zwei Diagramme als eines mit 20 Knoten
   (Richtwert flow ≤ 12 Knoten, Struktogramm ≤ 25 Blöcke).
3. **Lesbar im Druck:** kurze Beschriftungen, Details in `lines`, Fluss links → rechts bzw.
   oben → unten, Rückführungen über eine eigene Zeile bzw. `route: unten`
   (`references/diagramm-specs.md` Abschn. 2).
4. **Farbe trägt Bedeutung, nie allein:** Bedeutung in der Bildunterschrift erklären und
   zusätzlich über Linienart oder Beschriftung unterscheiden. **Keine Dekoration:** keine Icons,
   Cliparts, Schatten oder Farbflächen ohne Bedeutung – jedes Element ist Fachinhalt
   (`references/schuelermaterial.md`).
5. **Barrierefrei:** Alternativtext (ein Satz) und Bildunterschrift zu jedem Diagramm.
6. **Lösungen getrennt:** Lösungsdiagramme eigener Name (`…_loesung`, im Projekt `NN_l01_…`
   unter `solutions/diagrams/`) – sie dürfen nicht mit dem Aufgabenmaterial ausgeliefert
   werden.
7. **Die Spec ist die Quelle:** Änderungen in der YAML, dann neu erzeugen.
8. **Klausurabbildungen** in drei Rollen, immer in der **Notation des
   Unterrichts**: *Aufgabenbild* mit nummerierten Lücken ①–⑤ statt Lösung (Einträge in einer
   Tabelle neben dem Bild), *Fremdlösung mit gewolltem Fehler* (Fehler im Diagrammblatt und im
   Erwartungshorizont vermerken, keine realen Namen), *Lösungsbild* getrennt (`…_loesung`, nur im
   Erwartungshorizont). Zweige beschriftet (*ja*/*nein*), in Schwarzweiß lesbar, schmal genug
   (`breite` ≈ 360), damit das Bild neben den Teilaufgaben auf derselben Seite steht. Das Bild
   verrät die Lösung nicht – die Denkfalle der Aufgabe bleibt sichtbar.
9. **Arbeitsgegenstand, nicht Beigabe:** Im Unterrichtsmaterial arbeitet ein Auftrag mit dem
   Diagramm (ablesen, ergänzen, Fehler finden, selbst zeichnen); das Diagrammblatt nennt den
   Auftrag. Beschriftung ins Bild statt Legendentext; das Diagramm ersetzt Erklärtext.

## Vorgehen
1. Inhalt klären, Bauart wählen; Muster aus `assets/` als Ausgangspunkt nehmen.
2. **Spec schreiben** nach `references/diagramm-specs.md`:
   `diagramme/42_<kürzel>_<kurztitel>.yaml` mit `out: abbildungen/42_<kürzel>_<kurztitel>`
   (Kürzel `flow`, `nsd`, `chen`, `uml`, `rel`): Spec unter `diagramme/`, Bilder unter `abbildungen/`
   (Skill-Vertrag Abschn. 3). In einem Projekt mit `lessons/` dessen Konvention übernehmen.
3. **Spec prüfen:** `python3 scripts/diagramm_pruefen.py diagramme/*.yaml` – alle ❌ beheben,
   Warnungen zu Umleitungen hinter Kästen und zu breiten Beschriftungen ebenfalls (sonst
   verdeckte Texte, scheinbare Doppelpfeile).
4. **Erzeugen** (aus dem Arbeitsordner): `edu-diagramm <befehl> SPEC.yaml` (installiert) oder
   `python3 scripts/edu.py diagramm <befehl> SPEC.yaml` (mitgeliefert); Befehl `flow`,
   `struktogramm`, `chen` bzw. `box` (für uml/relational).
5. **Validieren:** `python3 scripts/edu.py diagramm validate abbildungen/*.drawio.svg`.
6. **Ansehen:** `python3 scripts/vorschau_png.py abbildungen/<name>.preview.svg` und die PNG
   betrachten – überlagerte Kästen oder Attribute, abgeschnittene Texte, Kanten durch Kästen?
   Spec anpassen (Positionen, `route`, `layout`), neu erzeugen. Ohne Konverter die `.drawio.svg` im Browser
   prüfen lassen und das im Diagrammblatt vermerken.
7. **Diagrammblatt** nach `assets/vorlage-diagrammblatt.md`: Einbindung, Alternativtext,
   Bildunterschrift, Vereinfachungen, Qualitätscheck, Annahmen, Übergabe.

**Ohne Skriptausführung** (Assistent ohne Code): Spec und Diagrammblatt ausgeben; die
Lehrkraft erzeugt lokal mit `edu-diagramm`. Kein SVG von Hand.

## Ausgabe
- `diagramme/42_<kürzel>_<kurztitel>.yaml` – Spec (hier ändern)
- `abbildungen/42_<kürzel>_<kurztitel>.drawio.svg` (weitergeben), `.drawio`, `.preview.svg`,
  `.png` – erzeugt
- `42_diagramm_<kurztitel>.md` – Diagrammblatt (Artefakt nach Skill-Vertrag), mehrere
  Diagramme zu einem Thema in einem Blatt
- Planungsakte: Artefakt 42 eintragen.

## Qualitätscheck
- [ ] `diagramm_pruefen.py` und `validate` ohne Fehler?
- [ ] PNG-Vorschau angesehen, nichts überlagert oder abgeschnitten?
- [ ] Fachlich richtig, Begriffe wie im Material, Vereinfachungen benannt?
- [ ] Keine Normzeichnung vorgetäuscht?
- [ ] Alternativtext und Bildunterschrift; Farbe nicht einziges Merkmal; keine Dekoration?
- [ ] Ein Auftrag arbeitet mit dem Diagramm (im Diagrammblatt genannt)?
- [ ] Lösungsdiagramme getrennt abgelegt?
- [ ] Klausurabbildung: Aufgabenbild ohne Lösung, Notation wie im Unterricht, in Schwarzweiß lesbar?

## Beispielaufrufe
> „Zeichne den Regelkreis der Vorlauftemperatur für das Arbeitsblatt in LF 5 (Anlagenmechaniker
> SHK), mit Rückführung über den Vorlauffühler."

> „Ersetze die ASCII-Skizze in `40_material_wartung.md` durch ein Struktogramm des
> Schmierablaufs."

> „ER-Modell für Anlagen, Wartungsaufträge und Techniker mit Kardinalitäten in Min-Max-Notation."

## Referenzen – wann lesen
- `references/diagramm-specs.md` – **immer** (Bauart, Spec-Format, Layoutregeln, Einbindung).
- `assets/spec-flow.yaml`, `assets/spec-struktogramm.yaml`, `assets/spec-chen.yaml`,
  `assets/spec-uml.yaml` – Muster je Bauart; `assets/spec-struktogramm-klausur.yaml` – Lückenbild
  für die Klausur.
- `assets/vorlage-diagrammblatt.md` – **immer** (Ausgabeformat).
- `references/schuelermaterial.md` – Darstellungen im Material für Lernende (Abschn. 2), keine Dekoration.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/diagramm_pruefen.py` – Spec-Prüfung; `scripts/vorschau_png.py` – PNG-Vorschau.
- `scripts/edu.py` – startet `edu-diagramm` aus der mitgelieferten Kopie (`scripts/eduwerkzeuge/`).

# ANHÄNGE

## Anhang: assets/vorlage-diagrammblatt.md

---
artefakt: Fachdiagramm – Diagrammblatt
titel: "[Thema der Diagramme]"
skill: fachdiagramm-erstellen
skill_version: "1.7"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
status: "KI-Entwurf – fachlich zu prüfen"
---

# Diagramme: [Thema]

**Bezug:** [Lernsituation / Material / Klassenarbeit, Dateinamen] · **Ablage:** Specs `diagramme/`, Bilder `abbildungen/`

## D1 – [Titel des Diagramms]

![[Alternativtext: was das Diagramm zeigt, in einem Satz]](abbildungen/42_[kürzel]_[kurztitel].drawio.svg)

*Abb. 1: [Bildunterschrift – erklärt Farben, Linienarten, Abkürzungen]*

| Feld | Eintrag |
|---|---|
| Bauart | [flow · struktogramm · chen · uml · relational] |
| Spec (hier ändern) | `diagramme/42_[kürzel]_[kurztitel].yaml` |
| Dateien | `.drawio.svg` (weitergeben) · `.drawio` · `.preview.svg` · `.png` (Word) |
| Verwendung | [Arbeitsblatt Aufgabe 2, Infotext, Tafelbild, Lösung] |
| Auftrag, der damit arbeitet | [z. B. „Ergänzen Sie die Lücken ① bis ④.“ – ablesen, ergänzen, Fehler finden, selbst zeichnen] |
| Alternativtext | [ein Satz] |
| fachliche Vereinfachung | [z. B. „ohne Sicherheitsventil und Ausdehnungsgefäß" – sonst „keine"] |

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| `diagramm_pruefen.py` ohne ❌ | | |
| `edu-diagramm validate` ohne Fehler | | |
| PNG-Vorschau angesehen: nichts überlagert oder abgeschnitten | | |
| Fachlich richtig, Fachbegriffe wie im Material | | |
| Vereinfachungen benannt; keine Normzeichnung vorgetäuscht | | |
| Alternativtext und Bildunterschrift vorhanden; Farbe nicht einziges Merkmal | | |
| Keine Dekoration; ein Auftrag arbeitet mit dem Diagramm | | |
| Lösungsdiagramme getrennt von Aufgabendiagrammen abgelegt | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Einbindung: `![…](abbildungen/….drawio.svg)`; für Word die PNG
- Empfohlene nächste Skills: `unterrichtsmaterial-erstellen` (Diagramm im Arbeitsblatt),
  `material-pruefen`, `schuelerseiten-veroeffentlichen`

> KI-gestützt erstellt (Skill fachdiagramm-erstellen v1.7). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: references/diagramm-specs.md

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

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.

## Inhalt
1. Vier Regeln
2. Darstellungen statt Text
3. Aufträge offen statt kleinschrittig
4. Was entfällt
5. Richtwerte
6. Rückwärtsprobe vor der Ausgabe

## 1. Vier Regeln

1. **Kurz.** Lernende lesen nur, was sie für den Auftrag brauchen. Kein Satz ohne Aufgabe,
   keine Wiederholung, kein Exkurs.
2. **Offen gestellt.** Ein Auftrag nennt Ziel (Operator), Gegenstand, Ergebnisform und woran
   man merkt, dass man fertig ist. Den Weg finden die Lernenden; Schritte und Gerüste stehen in
   gestuften Hilfen, die man bei Bedarf zieht.
3. **Anschaulich.** Aufgaben arbeiten mit Zeichnungen, Darstellungen und Grafiken: ablesen,
   auswerten, ergänzen, Fehler finden, selbst zeichnen. Was eine Darstellung zeigt, wird nicht
   zusätzlich beschrieben.
4. **Ohne Dekoration.** Nur, was dem Ziel dient (Abschn. 4).

Gekürzt wird Überflüssiges, nicht Fachinhalt: Fachbegriffe, Sicherheitshinweise und
Erfolgskriterien bleiben vollständig.

## 2. Darstellungen statt Text

| Inhalt | Darstellung | so entsteht sie |
|---|---|---|
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen`; Technologieschema mit `technologieschema-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen`; GRAFCET und Funktionsplan mit `technologieschema-erstellen` |
| System, Energie- und Datenfluss, Regelkreis | Blockschaltbild | `fachdiagramm-erstellen` |
| Zusammenhang zweier Größen | Diagramm, Kennlinie mit beschrifteten Achsen | aus gerechneten Werten oder dem Datenblatt als SVG erzeugen (Code), nie geschätzt |
| Vergleich, Kriterien, Kenndaten | Tabelle, Matrix | Markdown-Tabelle |
| Begriffe und ihre Beziehungen | Strukturbild | `fachdiagramm-erstellen` (Bauart `flow`), Tabelle |
| Daten und Software | ER-, Klassen-, Sequenzdiagramm | `fachdiagramm-erstellen` |
| Schaltung, Werkstück | Schaltplan, technische Zeichnung nach Norm | Herstellerunterlage, Tabellenbuch, eigene Zeichnung (Platzhalter mit Quelle) |

Jede Zeichnung entsteht als **SVG aus einer Spec** – nie als Zeichnung aus Zeichen (ASCII-Art) und
nie als Mermaid in der Ausgabe (Skill-Vertrag Abschn. 3).

**Die Darstellung ist Arbeitsgegenstand, nicht Beigabe.** Aufträge, die mit ihr arbeiten
(Beispiele am Gurtförderer GF-2, fiktiv):

| Auftrag | Beispiel |
|---|---|
| ablesen, auswerten | „Ermitteln Sie aus der Kennlinie die Drehzahl bei 80 % Last.“ |
| ergänzen | „Benennen Sie im Anlagenbild die Bauteile ① bis ④.“ |
| Fehler finden | „Der Arbeitsplan in Abb. 2 enthält zwei Fehler. Berichtigen Sie sie.“ |
| selbst zeichnen | „Skizzieren Sie, wie die Spannstation verstellt werden muss.“ |
| vergleichen | „Vergleichen Sie die Gurtlaufbilder A und B.“ |

Regeln:
- **Am Auftrag:** Abbildung direkt bei dem Auftrag, der sie braucht; Beschriftung in die
  Abbildung, Positionsnummern statt Legendentext, wo möglich.
- **Fachlich richtig und normgerecht:** Schaltzeichen, Kennzeichen und Formelzeichen nach
  Norm; Werte hinter Diagrammen sind gerechnet.
- **Schwarzweiß lesbar:** Farbe nur mit Bedeutung und nie allein (zusätzlich Linienart oder
  Beschriftung).
- **Nie erfinden:** keine KI-Bilder, die Fotos, echte Anlagen oder Messkurven vortäuschen. Was
  nicht selbst gezeichnet werden kann (Foto, Herstellerzeichnung, Normauszug), steht als
  Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz]` und ist ein Prüfauftrag.
- **Barrierearm:** Alternativtext (ein Satz) je Abbildung.
- **Platz für Zeichnungen der Lernenden:** in der Druckfassung Kasten oder Raster statt Linien.

Nicht jede Aufgabe braucht ein Bild (Begründung, Gespräch, Reflexion). Ein Arbeitsblatt oder
Infoblatt ganz ohne Darstellung ist aber zu begründen.

## 3. Aufträge offen statt kleinschrittig

**Kleinschrittig – so nicht:**

> 1. Lesen Sie den Wartungsplan (M1).
> 2. Unterstreichen Sie alle Arbeiten, die nach 500 Betriebsstunden fällig sind.
> 3. Übertragen Sie die Arbeiten in die erste Spalte der Tabelle.
> 4. Ergänzen Sie in der zweiten Spalte das Werkzeug.
> 5. Ergänzen Sie in der dritten Spalte die Sicherheitsmaßnahme.
> 6. Addieren Sie die Zeiten.

**Offen – so:**

> **1 Erstellen Sie** den Arbeitsplan für die 500-h-Wartung des GF-2 (Wartungsplan M1,
> Vorlage M3). Fertig, wenn jeder Schritt Werkzeug und Sicherheitsmaßnahme hat und die
> Gesamtzeit unter 2 h liegt.

Die Schritte stehen – kürzer – in den gestuften Hilfen (Impuls → Strategie → Teilschritt →
Kontrolle; Skill `differenzierung-erstellen`). Wer sie braucht, zieht sie. Formate mit weniger
Stufen ordnen zu: Lernlandkarte – Kontrolle ist der Selbstcheck des Lernpostens; Lektion –
Orientierung, Werkzeug, Gerüst entsprechen Impuls, Strategie, Teilschritt, die Kontrolle leisten
Realitätstest und Rückmeldung.

Signale für Kleinschrittigkeit:
- mehr als drei Teilaufgaben a), b), c) an einem Auftrag;
- eine Schrittfolge im Auftrag, die den Lösungsweg vorgibt („zunächst …, dann …,
  anschließend …“) oder eine Reihe kurzer Einzelaufträge, die zusammen einen Auftrag ergeben;
- Lesen, Unterstreichen, Abschreiben oder Übertragen als eigener Auftrag – das sind Mittel,
  kein Ziel;
- Lücken, die sich durch Abschreiben aus dem Text füllen lassen;
- Teilaufgaben, deren Ergebnis die nächste schon verrät.

**Zulässig und nicht kleinschrittig:**
- **Sicherheitsrelevante Schritte** (Freischalten, Stoffe, Mengen, Reihenfolge an der
  Maschine) stehen vollständig und in Reihenfolge – auch in einer offenen Anleitung.
- **Bedienschritte**, die nicht Lernziel sind (Messgerät einstellen, Software starten): kurz,
  am besten als Bildfolge oder Hinweis, nicht als Auftrag.
- **Übungsfolgen** zum Einschleifen einer Routine: gleichartige, je für sich vollständige
  Aufgaben (gelöstes Beispiel → steigend → eingekleidet).
- **Lösungsbeispiel mit Ausblenden:** steht als Beispiel, nicht als Auftrag.
- **Einführende Bildungsgänge** (Berufseinstieg, BVJ): enger geführt über Lösungsbeispiele,
  Hilfen und hohen Anschauungsgrad – nicht über zerlegte Aufträge.

## 4. Was entfällt

| entfällt | stattdessen |
|---|---|
| Schmuckbilder, Cliparts, Symbol- und Stockfotos, Illustrationen ohne Fachinhalt | Abbildung mit Fachinhalt – oder keine |
| Emojis und Symbole ohne Funktion (auch farbige Punkte als Stufenkennung) | Wort; zulässig sind die KI-Zeichen 🚫 💡 🔧 (`ki-vereinbarungen.md`, falls vorhanden), Warn- und Gefahrenzeichen, Ankreuzkästchen ☐ und ✔ ~ ✘ zur Selbsteinschätzung |
| Begrüßung, Motivationssätze („Viel Spaß!“, „Los geht’s!“), Ankündigungen („In diesem Arbeitsblatt lernen Sie …“) | gleich mit Situation oder Auftrag beginnen |
| Einleitung, die den Auftrag vorwegnimmt; Zusammenfassung dessen, was eben dastand | Kernaussage einmal, vorn |
| Exkurse, Anekdoten, Technikgeschichte, „Wussten Sie schon?“-Kästen | als Vertiefung, wenn sie zum Ziel beitragen – sonst streichen |
| dasselbe in Fachwissen, Hilfe und Auftrag | einmal, dort, wo es gebraucht wird |
| Zierrahmen, Farbflächen, Schmuckschriften | klare Überschriften; Kästen nur mit Funktion (Hilfe, Stolperstein, Sicherheit) |
| Angaben für die Lehrkraft (AFB, Kompetenzcodes, Annahmen, Prüfvermerke) | im Lehrerteil |
| Information, die kein Auftrag braucht | streichen |

Keine Dekoration, also bleibend: Kopfzeile (Lernsituation, Zeit, Sozialform), Name und Datum
auf Druckblättern, Erfolgskriterien, Bewertungskasten, KI-Zeichen, Quellen- und
Lizenzangaben, KI-Transparenzhinweis.

## 5. Richtwerte

Orientierung, kein Urteil. ⚠️ Noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

| Element | Richtwert |
|---|---|
| Ausgangslage, Bezug zur Situation | höchstens drei Sätze; besser Situationsmaterial (Störmeldung, Foto, Anlagenbild) |
| Arbeitsauftrag | ein bis zwei Sätze, ≤ ~25 Wörter, Operator zuerst; der Kontext steht einmal in der Ausgangslage |
| Teilaufgaben je Auftrag | höchstens drei |
| Satz | meist unter 15 Wörtern, keiner über 25; die sprachsensible Fassung ist bewusst strenger (über 20 Wörter teilen, `lesbarkeit.py`) |
| Infoblatt | eine Seite, ≤ ~300 Wörter Fließtext, mindestens eine tragende Darstellung |
| Arbeitsblatt (Teil für Lernende) | ≤ ~350 Wörter Fließtext (ohne Tabellen, Code, Abbildungen), mindestens eine Darstellung |
| Situationsmaterial | ≤ ~150 Wörter |
| Hilfekarte | je Stufe ≤ ~40 Wörter, gern als Teilbild oder Skizze |
| Rollenkarte | ≤ ~60 Wörter |
| Lektion (90 min) | ≤ ~1 500 Wörter ohne Code (`lektionsmuster.md`, falls vorhanden) |
| Lernlandkarte (eine Unterrichtseinheit) | ≤ ~1 500 Wörter wie eine Lektion; je Karte nur Auftrag, Material, Hilfen, Selbstcheck |
| sonstiges Material | ≤ ~400 Wörter Fließtext je Datei |

Authentische Dokumente (Betriebsanleitung, Datenblatt, Norm, Quelle der Quellenmappe) bleiben
im Original und zählen nicht mit – sie liegen als Auszug mit Fundstelle bei, nicht
abgeschrieben.

## 6. Rückwärtsprobe vor der Ausgabe

1. **Jeder Absatz, jede Abbildung:** Welcher Auftrag braucht das? Keiner → streichen.
2. **Jeder Auftrag:** Operator, Ergebnisform, Erfolgskriterium – und kein vorgegebener
   Lösungsweg? Schritte → in die Hilfen.
3. **Jede Aufgabe:** Mit welcher Darstellung wird gearbeitet? Keine → ergänzen, wo eine trägt.
4. **Dekoration** (Abschn. 4) gestrichen?
5. **Skript:** `python3 scripts/schuelermaterial_pruefen.py DATEI.md` – Fließtext, lange Sätze
   und Aufträge, Teilaufgaben und Schrittfolgen, Darstellungen je Auftrag, Dekoration,
   Lehrerangaben, doppelte Sätze. Wortzahl und Befunde im Qualitätscheck festhalten.

## Anhang: references/skill-vertrag.md

# Skill-Vertrag der Bibliothek „Unterrichtsentwicklung BBS"

Gemeinsamer Standard für alle Skills dieser Bibliothek. Er sorgt dafür, dass jeder Skill
**allein** funktioniert und trotzdem **mit jedem anderen kombinierbar** ist. Die Quelle liegt
in `_gemeinsam/skill-vertrag.md`; jeder Skill trägt eine Kopie unter `references/`.

---

## 1. Eigenständig arbeiten – Entwurf vor Rückfrage

1. Der Skill braucht nur den Auftrag der Lehrkraft. Fehlende Angaben werden durch
   **begründete, fachtypische Annahmen** ersetzt und sichtbar markiert:
   `⚠️ Annahme: 2. Ausbildungsjahr, 24 SuS, heterogen.` bzw. im Beruflichen Gymnasium
   `⚠️ Annahme: Jg. 13 (Qualifikationsphase), 22 SuS, Lerngebiet ING3.`
2. **Rückfragen nur, wenn ohne Antwort der ganze Entwurf unbrauchbar wäre** (z. B. Beruf
   bzw. Fach völlig unbekannt). Dann höchstens drei gebündelte Fragen, jeweils mit Vorschlag
   als Standardantwort.
3. Ziel ist ein **vollständiger erster Entwurf** (alle Abschnitte gefüllt), nicht ein
   perfekter Teil. Die Lehrkraft schärft nach.
4. Ein Skill ruft **keinen anderen Skill selbst auf**. Er empfiehlt am Ende sinnvolle
   Folge-Skills. Das Verketten übernimmt der Orchestrator `unterricht-entwickeln`.

## 2. Kontext übernehmen – die Planungsakte

Liegt eine **Planungsakte** vor (Datei `00_planungsakte.md` im Arbeitsordner oder ein
Planungsakte-Block im Gespräch), übernimmt der Skill daraus alle passenden Angaben und fragt
nichts erneut ab. Nach getaner Arbeit trägt er sein Artefakt in die Akte ein und ergänzt
leere Felder, die er festgelegt hat. Widersprüche zur Akte werden gemeldet, nicht still
überschrieben.

```markdown
---
projekt: "LS 4 – Förderband nach Störung wieder in Betrieb nehmen"
bundesland: Niedersachsen
schulform: Berufsschule (Teilzeit)
bildungsgang: Industriemechaniker/-in
ausbildungsjahr: 2          # vollzeitschulisch (z. B. BG) stattdessen: schuljahrgang, phase, schwerpunkt, lerngebiet
curriculare_vorgabe: "Rahmenlehrplan Industriemechaniker/-in, LF 6"
dqr: 4
zeitrichtwert_ls: 16
lerngruppe: "22 SuS, heterogen, 3 SuS mit Deutsch als Zweitsprache (ca. B1)"
rahmen: "Fachraum Steuerungstechnik, Moodle, 90-Minuten-Blöcke"
handlungssituation: "…"
handlungsergebnis: "…"
leitidee_ls: "…"            # didaktische Leitidee der Lernsituation (1–2 Sätze)
---

## Artefakte
| Nr. | Artefakt | Skill | Status | Datei |
|---|---|---|---|---|
| 10 | DQR-Einordnung | dqr-zuordnen | Entwurf | 10_dqr-einordnung.md |

## Entscheidungen
- …

## Annahmen und Prüfaufträge (gesammelt)
- …
```

## 3. Ausgabe – einheitlich und weiterverwendbar

**Format:** Markdown. Mit Dateizugriff wird als Datei gespeichert, sonst im Chat ausgegeben.
Ein bestehendes Dokument wird **nie überschrieben**; Überarbeitungen erhalten ein Suffix
(`…_sprachsensibel.md`, `…_v2.md`).

**Text zum Einfügen** (Systemanweisung, Moodle-Textfeld, Hinweistext, Importquelle) steht als
eigener Block im Format des Ziels – ohne Erläuterungen darin; Erläuterungen stehen davor oder
danach. **Vorschläge zu Vorhandenem** (Begutachtung, Überarbeitung, Einstellungen) nennen je
Vorschlag Stelle, neuen Wert und Begründung; was schon passt, wird zusammengefasst bestätigt
statt wiederholt.

**Material für Lernende** (alles, was Lernende in die Hand bekommen; Vorgabe der Fachberatung,
31.10.2026): **kurz** – kein Satz ohne Aufgabe; **offen gestellt** – Ziel, Ergebnis und
Erfolgskriterium statt Lösungsweg, Schritte in gestufte Hilfen; **anschaulich** – Aufgaben
arbeiten mit Zeichnungen, Darstellungen und Grafiken; **ohne Dekoration** – keine Schmuckbilder,
Emojis ohne Funktion, Floskeln oder Inhalte, die kein Auftrag braucht. Richtwerte und Beispiele:
`schuelermaterial.md`, falls vorhanden. Die Pflichtabschnitte (unten) stehen im Teil für die
Lehrkraft (nach `# Lösungen und Erwartungshorizont` bzw. `# Didaktische Hinweise`), nie im Teil für
Lernende.

**Zeichnungen** (Vorgabe der Fachberatung, 01.11.2026): Jede Zeichnung in einem Artefakt – Material
für Lernende, Lösung, Erwartungshorizont, Tafelbild, Entwurf, Begleitblatt – entsteht als **SVG aus
einer Spec** mit dem passenden Zeichen-Skill, dazu eine in diagrams.net bearbeitbare `.drawio.svg`,
eingebunden mit `![Alternativtext](abbildungen/….svg)` und kursiver Bildunterschrift. **Nie** als
Zeichnung aus Zeichen (ASCII-Art: Kästen aus ┌─┐ oder +---+, Pfeilketten, Struktogramm oder GRAFCET
im Codeblock), nie als Mermaid in der Ausgabe, nie als von Hand geschriebenes SVG.

| Zeichnung | Skill bzw. Weg |
|---|---|
| Blockschaltbild, Anlagen- und Systemübersicht, Ablauf, Regelkreis, Struktogramm, ER-Modell, UML, Relationenschema | `fachdiagramm-erstellen` |
| Kennlinie, Messwertdiagramm | aus den Werten per Code als SVG (z. B. matplotlib), Wertetabelle daneben |
| Foto, Werkstückzeichnung, fremde Abbildung | Datei mit Quelle und Lizenz, sonst Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle]` |
| Anlagenbild (Technologieschema), Schaltplanauszug mit Schaltzeichen, GRAFCET, Funktionsplan (FUP), Netzplan | `technologieschema-erstellen` |
| GRAFCET, Funktionsplan, Schaltplan | Fachsoftware; im Text zusätzlich als Tabelle (Schritt, Aktion, Transition) |

Erlaubt bleiben Text-Tabellen derselben Inhalte (GRAFCET in Textform, Zuordnungsliste) für die
Zweitkorrektur und die Barrierefreiheit; Verzeichnisbäume und Programmcode sind keine Zeichnungen.
Lösungsbilder tragen `_loesung` im Namen und stehen nur im Teil für die Lehrkraft. **Ohne
Skriptausführung** (Assistent ohne Code) liefert der Skill die Spec und an der Stelle des Bildes den
Platzhalter `[ABBILDUNG: Inhalt – Spec <datei>.yaml]`; die Lehrkraft erzeugt das SVG lokal.
Vorhandenes Material mit Zeichnungen aus Zeichen wird beim Überarbeiten umgestellt. Prüfung:
`zeichnungen_pruefen.py`, falls vorhanden (❌ Zeichnung aus Zeichen, ⚠ Mermaid). Es öffnet auch jede
eingebundene SVG: ❌ Text über Text, Form oder Linie über Text, Text ragt aus seinem Kasten oder aus
dem Bild; ⚠ SVG ohne Spec und Werkzeugkennung (von Hand?), schräge Leitungen, Datei fehlt. Ein Skill,
der Zeichnungen braucht, ruft dafür das Zeichen-Skill auf oder bringt dessen Werkzeug mit
(`metadata.eduwerkzeuge`) – `pruefen` meldet einen `edu-*`-Befehl ohne beides.

**Dateinamen** (Nummer = Platz in der Planungskette):

| Nr. | Artefakt | Skill |
|---|---|---|
| 00 | Planungsakte | unterricht-entwickeln |
| 10 | DQR-Einordnung | dqr-zuordnen |
| 20 | Lernsituation | lernsituation-dokumentieren |
| 21 | LS-Analyse (Prüfbericht: Analysebogen, Phasencheck, Querschnitt, weitere Aspekte) | lernsituation-analysieren |
| 30 | Unterrichtsentwurf | unterrichtsentwurf-erstellen |
| 35 | Entwurfscheck (Selbstcheck/Beratung) | unterrichtsentwurf-analysieren |
| 36 | Unterrichtsreflexion (nach der Stunde: Selbstreflexion, Nachbesprechung) | unterricht-reflektieren |
| 40 | Unterrichtsmaterial | unterrichtsmaterial-erstellen |
| 41 | Experiment (Versuchsanleitung, Lehrerfassung, Gefährdungsbeurteilung) | experiment-planen |
| 42 | Fachdiagramm (Diagrammblatt, Specs unter `diagramme/`, SVG unter `abbildungen/`) | fachdiagramm-erstellen |
| 43 | Programmieraufgabe (Aufgabe, Codeordner `43_code/`, Erwartungshorizont) | programmieraufgabe-erstellen |
| 44 | Technikfolgenabschätzung (Dossier, Quellenmappe, Rollenkarten) | technikfolgen-abschaetzen |
| 45 | Taxonomie-Analyse | bloom-taxonomie |
| 46 | Technologieschema (Schemablatt mit Legende, Specs unter `schema/`, SVG unter `abbildungen/`) | technologieschema-erstellen |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

**Werkzeug-Skills** (Nr. 42, 46, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-technologieschema`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
Artefakt mit Pflichtabschnitten – diese hätten in der Quelle Folgen für die Ausgabe –, sondern
Kopf und Pflichtabschnitte stehen in einem **Begleitblatt** (`…_begleitblatt.md`,
Diagrammblatt). Nummern 92–96 (Ausspielen) folgen auf den Prüfbericht: veröffentlicht wird
geprüftes Material. Nr. 93 (agiles Lernen) kann auch für sich stehen, wenn eine Lehrkraft
selbst lernt; die Lernakte gehört dann der lernenden Person.

**Kopf jedes Artefakts:**

```yaml
---
artefakt: Lernsituation
titel: "Förderband nach Störung wieder in Betrieb nehmen"
skill: lernsituation-dokumentieren
skill_version: "1.0"
stand: 2026-10-08
bildungsgang: "Industriemechaniker/-in"
curriculare_vorgabe: "RLP Industriemechaniker/-in, LF 6"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
# optional:
bereich: planung            # planung | pruefen
vertraulich: false          # true bei unveröffentlichten Prüfungsvorschlägen o. Ä.
---
```

**Pflichtabschnitte am Ende jedes Artefakts:**

1. `## Qualitätscheck` – Tabelle *Kriterium | Ergebnis (✅/⚠️/❌) | Hinweis*. Ein ❌ wird vor
   der Ausgabe behoben; was sich nicht beheben lässt, wird zu ⚠️ mit Begründung.
2. `## Annahmen und Prüfaufträge` – alle `⚠️ Annahme:` und alle `🔎 Prüfen:` (Normen,
   Grenzwerte, Rechtsvorgaben, Herstellerangaben, regionale Besonderheiten).
3. `## Übergabe` – kurze Stichpunkte für Folge-Skills (z. B. Handlungsergebnis, zentrale
   Kompetenzen, Dateinamen) und **empfohlene nächste Skills**.
4. Transparenzhinweis als letzte Zeile:
   `> KI-gestützt erstellt (Skill <name> v<version>). Fachliche Prüfung und Verantwortung: Lehrkraft.`
   Die verantwortliche Rolle darf passend zum Artefakt abweichen (z. B. Lehrkraft bzw.
   Bildungsgangteam, Lernende und Fachexpertin); die Zeile beginnt immer mit `> KI-gestützt`, nennt
   Skill und aktuelle Version und steht in **einer** Zeile.

Ausnahmen: **Teilartefakte** tragen Kopf und Pflichtabschnitte im zugehörigen Begleitblatt bzw.
Erwartungshorizont;
**Akten** (Planungsakte) führen einen Verlauf;
**Lektionen** im Kursprojekt folgen `vorlage-lektion.md`, falls vorhanden (Kopf für die Seitenausgabe).

## 4. Fachliche Redlichkeit

- **Nichts erfinden:** keine ausgedachten Normnummern, Paragrafen, Zitate, Studien,
  Grenzwerte, URLs oder Quellen. Unsicheres wird markiert: `[🔎 Norm prüfen]`,
  `[🔎 Wert prüfen]`. „Weiß ich nicht sicher" ist ein gültiges Ergebnis.
- **Rechnen statt schätzen:** Zahlenwerte in Aufgaben und Lösungen werden nachgerechnet,
  Einheiten mitgeführt. Ist ein Code-Werkzeug verfügbar, wird es dafür benutzt.
- **Quellenlage offenlegen:** Unterscheiden zwischen *aus gelieferten Unterlagen* und *aus
  allgemeinem Fachwissen*. Gelieferte Ordnungsmittel haben Vorrang.
- **Fiktive Akteure klar fiktiv:** Firmen, Personen und Adressen in Handlungssituationen
  sind erkennbar ausgedacht („(fiktiv)“ beim ersten Auftreten); keine echten Telefonnummern,
  keine realen Personen; E-Mail-Adressen nur mit Beispiel-Domains (`example.org`, RFC 2606).

## 5. Datenschutz

- Für Begutachtungen, Rückmeldungen und KI-Chatbots gelten zusätzlich die **Leitplanken**
  (`references/leitplanken-bewertung.md`, falls vorhanden): Datenschutzstufen 0–2, keine
  Bewertung einzelner Lernender durch KI, Freigabe durch die Lehrkraft.
- Für Planung und Material werden **keine personenbezogenen Daten** gebraucht.
- Gibt die Lehrkraft Namen oder Leistungsdaten von Lernenden an, werden sie im Artefakt
  pseudonymisiert (S01, S02 …) und es folgt ein kurzer Hinweis.
- Keine Gesundheits-, Förder- oder Herkunftsangaben zu einzelnen Lernenden in Artefakten;
  Lerngruppen werden nur zusammenfassend beschrieben.

## 6. Begriffe und Bezugsrahmen

- Standard ist das **berufsbildende Schulwesen in Niedersachsen**. Für vollzeitschulische
  Bildungsgänge, besonders das **Berufliche Gymnasium** (Lerngebiete, Schuljahrgang,
  Notenpunkte, EPA), gilt zusätzlich `berufliches-gymnasium.md`, falls vorhanden. Verbindliche
  Begriffe nach **Leitlinie SchuCu-BBS 2024**: Handlungssituation, Handlungsergebnis,
  Handlungskompetenz mit **Fachkompetenz** (Wissen, Fertigkeiten) und **Personaler
  Kompetenz** (Sozialkompetenz, Selbständigkeit); vollständige Handlung in sechs Phasen
  (Informieren bzw. Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw.
  Kontrollieren · Reflektieren).
- **SchuCu-BBS 2024 ist verbindlich** (Entscheidung der Fachberatung, 19.10.2026): kein
  anderes Kompetenzmodell (etwa vier Dimensionen), keine anderen Phasen oder Begriffe. Eine
  Gliederung des Studienseminars oder der Schule darf gelten; ihre Abschnitte werden mit den
  Begriffen der Leitlinie gefüllt. Vorgaben anderer Länder übernehmen die Skills nicht.
- **Vollständige Handlung und Lernzeit**: Der
  Handlungskreis wird je Lernsituation geschlossen, aber nicht zwingend in 90 Minuten – er
  darf mehrere Unterrichtseinheiten umfassen (Entscheiden, Überprüfen mit Überarbeitung und
  Reflektieren der Lernsituation bleiben immer). Fachsystematische, lehrkraftgeführte
  Lernphasen sind zulässig, wo zweckdienlich und begründet; die Begründung wird dokumentiert
  (`lernsituationsmuster.md` Abschn. 12, falls vorhanden).
- **Didaktische Leitidee** (Planungshilfe der Bibliothek):
  `didaktische-leitidee.md`, falls vorhanden. Ein bis zwei Sätze, welche übertragbare Einsicht
  die Lernenden am exemplarischen Fall gewinnen und warum sie bedeutsam ist – für die
  Lernsituation (unter *didaktisch-methodische Kommentare*) und für die Stunde (vor dem
  Stundenziel). Sie ergänzt die Begriffe der Leitlinie und ersetzt keinen.
- Sprache: sachlich, geschlechtergerecht („Schülerinnen und Schüler", Abkürzung „SuS").
- Kompetenzen und Ziele werden mit **beobachtbaren Operatoren** formuliert
  (`references/operatoren-afb.md`, falls vorhanden). Nicht verwenden: *verstehen, kennen,
  wissen, lernen, sich bewusst sein*.

## 7. Selbstprüfung

Vor der Ausgabe prüft der Skill sein Ergebnis gegen die eigene Checkliste **und** gegen
diesen Vertrag (Annahmen markiert? Nichts erfunden? Pflichtabschnitte vorhanden? Material für
Lernende kurz, offen gestellt, anschaulich, ohne Dekoration? Jede Zeichnung als SVG aus einer
Spec, keine Zeichnung aus Zeichen – `zeichnungen_pruefen.py`, falls vorhanden?), behebt Mängel und
gibt erst dann aus.

## 8. Plattformen

- **Claude (Skills aktiviert):** Ordner als Skill installieren; Claude lädt ihn bei Bedarf.
- **Assistenten ohne Skill-Funktion (z. B. AIS-Chat.schule, fobizz):** Inhalt von
  `SKILL.md` als Anweisung des Assistenten einfügen, Dateien aus `references/` und
  `assets/` als Wissensbasis hochladen. Die Planungsakte wird dann von Hand zwischen den
  Assistenten weitergegeben.
- **Chatbots für Lernende** (Moodle-KI-Chat, AIS.chat-Lernszenario) bekommen keine
  Skill-Fassung, sondern eine eigene kurze Systemanweisung mit Probelauf (`ki-chatbot-einrichten`,
  im AIS-Paket `agiles-lernen-mit-ki`).
