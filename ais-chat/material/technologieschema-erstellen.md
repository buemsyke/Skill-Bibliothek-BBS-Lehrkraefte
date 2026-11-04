<!-- Assistenten-Fassung des Skills 'technologieschema-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
# Technologieschema erstellen

## Zweck
Das Bild zur Steuerungsaufgabe: **die Anlage, wie Lernende sie vor sich sehen** – Zylinder, Sensoren,
Ventile, Bedienelemente, Werkstück und Bewegungsrichtungen. Es ersetzt weder Schaltplan noch
Pneumatikplan; es zeigt, **was wo sitzt**, damit Funktionsbeschreibung, Zuordnungsliste und
Programm darauf Bezug nehmen können. Claude beschreibt die Anlage in einer YAML-Spec; Zeichnung,
Anker, Prüfung und Legende übernimmt `edu-technologieschema`. Kein von Hand geschriebenes SVG.
Jede Abbildung gibt es **zweimal**: als Bild (`.svg`) und als **bearbeitbare Zeichnung**
(`.drawio.svg`), die die Lehrkraft in diagrams.net weiterbearbeitet – Bauteile verschieben,
Kennzeichen und Texte ändern, Bauteile kopieren, ohne dass Linien abreißen.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Schemablatt). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Wann dieser Skill, wann ein anderer
| Inhalt | Skill |
|---|---|
| Bild der **Anlage** mit Betriebsmitteln (Technologieschema) | dieser Skill |
| Blockschaltbild, Ablauf, Regelkreis, Struktogramm, ER, UML | `fachdiagramm-erstellen` |
| Auszug eines Stromlaufplans mit Schaltzeichen (Steuerstromkreis, Sensoranschluss) | dieser Skill (`typ: symbol`) |
| GRAFCET (Ablaufkette mit Aktionen, Transitionen, Rücksprung) | dieser Skill, eigenes Bauteil `typ: grafcet` nach `assets/spec-grafcet.yaml` |
| Funktionsplan (FUP, Logikplan mit &, ≥1, Vergleicher) | dieser Skill, Grundformen nach `assets/spec-fup.yaml` |
| Netzplan (Gebäude, Switches, Router, LWL/Kupfer/VPN) | dieser Skill, Grundformen (`rechteck`, `text`, `linie`) |
| vollständiger Stromlaufplan, Pneumatik-/Hydraulikplan, technische Zeichnung | Fachsoftware – hier nicht |

Zeichnungen aus Zeichen (ASCII-Art) gibt es in der Bibliothek nicht (Skill-Vertrag Abschn. 3): Auch
Lösungsbilder im Erwartungshorizont – GRAFCET, FUP, Netzplan – entstehen hier als SVG.

## Eingaben
- **Pflicht (sonst Rückfrage):** welche Anlage – Aufgabentext, Skizze, Foto, ASCII-Zeichnung oder
  Beschreibung der Teile und Bewegungen.
- **Wichtig, sonst Annahme:** Verwendung (Übung, Klassenarbeit, Abitur, Tafelbild), Grundstellung,
  Bildgröße, Aufgabenbild oder Lösungsbild. Kennzeichen sind **immer** nach DIN EN IEC 81346-2:2020;
  Vorlagen mit anderer Schreibweise (S1, Y1) werden umgestellt (Entsprechungen in der Legende nennen).
- **Optional:** Planungsakte, vorhandene Funktionsbeschreibung und Zuordnungsliste (Kennzeichen
  übernehmen), Abbildungsnummer.

## Leitlinien (verbindlich)
1. **Nur zeigen, was die Aufgabe nennt.** Jedes Betriebsmittel der Aufgabe steht im Bild und in der
   Legende, nichts darüber hinaus. Fehlt eine Angabe (Lage eines Sensors, Wirkrichtung), Annahme
   markieren oder `🔎 Prüfen:`.
2. **Bild plus Text-Legende.** Kennzeichen im Bild sind für Prüfskripte und Zweitkorrektur
   unsichtbar; die Legende (Referenzkennzeichen | Betriebsmittel | Lage/Aufgabe) kommt aus
   `edu-technologieschema legende` und steht neben dem Bild. Kontaktart (NO/NC) und
   Bedeutung der Signale stehen in Funktionsbeschreibung und Zuordnungsliste, nicht im Bild.
3. **Referenzkennzeichen immer nach aktueller Norm** (DIN EN IEC 81346-2:2020; Form -S1, -MA1,
   -BR1; Notationsblatt `references/notation-steuerungstechnik.md`). Das Werkzeug lässt keine
   andere Schreibweise zu: Form, Klasse und Unterklasse nach Tabelle 2, **Klasse passend zum
   Bauteil** (Taster S, Sensor B, Zylinder M, Leuchtmelder P), Kennzeichen der Ausgabe 2009 sind
   ❌, **eine Tiefe je Klasse** (nur Klasse, solange sie eine Art Betriebsmittel enthält; sonst
   überall Unterklasse: -MA1 Motor neben -MM1 Zylinder, nie -M1 neben -MM1). Dieselben
   Kennzeichen wie in Legende, Aufgaben und Musterlösung.
4. **Wirkungslinien rechtwinklig.** Linien und Rohre verlaufen waagerecht oder senkrecht; das
   Werkzeug fügt bei schrägen Punktpaaren einen Knick ein und warnt bei kleinem Versatz
   (Positionen angleichen). Schräg nur mit `schraeg: true` und gutem Grund; geneigte Teile
   (Förderband) sind erlaubt, die Verbindungen dazu bleiben rechtwinklig.
5. **Schaltzeichen nach DIN EN 60617**, wo ein Bauteil als Zeichen statt als Bild dargestellt
   wird (`typ: symbol`, Liste mit `edu-technologieschema symbole`). Zeichen mit der Herkunft
   *abgleichen* stehen in der Liste mit 🔎: vor dem Einsatz mit Norm oder eingeführtem Tabellenbuch
   vergleichen und im Schemablatt vermerken. Zeichen nicht erfinden und nicht von Hand in Pfaden
   nachbauen.
6. **Grundstellung zeigen** und in der Fußzeile nennen (Zylinder eingefahren, Werkstück am
   Anschlag, Füllstand zwischen -B1 und -B2). Bild und Text stimmen überein.
7. **Das Bild verrät die Lösung nicht:** keine Soll-Abläufe, Schrittnummern, Signalzustände oder
   beschriftete Wirkungen. Lösungsbilder (Zustand nach einem Schritt, Markierungen) sind eigene
   Specs mit Namen `…_loesung` und gehören nur ins Lehrermaterial.
8. **Fachlich richtig vor schön:** Bauteile, Bewegungsrichtungen und Lage wie in der Aufgabe oder
   in Herstellerunterlagen; Vereinfachungen im Schemablatt benennen („ohne Sicherheitseinrichtungen“).
   Keine Normzeichnung vortäuschen.
9. **Lesbar im Druck:** nur Graustufen (Farbe trägt nie die Bedeutung), kurze Beschriftungen,
   Schrift 11–13 Pixel bei 720–780 Pixel Breite, höchstens etwa 15 Bauteile je Bild – sonst zwei
   Bilder (Anlage und Bedienfeld).
10. **Barrierefrei:** Alternativtext (ein Satz mit den Kennzeichen), Bildunterschrift und
   `<title>` „Abbildung N – Titel“ sind Pflicht.
11. **Vorlagen Dritter:** Eine Abbildung aus Buch, Webseite oder Aufgabensammlung wird nur
   nachgezeichnet, wenn die Rechte geklärt sind; die Quelle steht im Schemablatt. Besser: eigene
   Anlage aus der Aufgabenbeschreibung entwerfen. Kopien fremder Bilder gehören nicht in den Skill.
12. **Die Spec ist die Quelle:** Änderungen in der YAML, dann neu erzeugen. Hat die Lehrkraft die
   `.drawio.svg` in diagrams.net bearbeitet, ist **diese Datei** die Quelle: nicht ungefragt neu
   erzeugen (ihre Änderungen gingen verloren); geänderte Kennzeichen prüft dort kein Werkzeug – Legende
   und Zuordnungsliste von Hand abgleichen.
13. **Bearbeitbar ausliefern:** immer `.drawio.svg` mitgeben (nicht `--ohne-drawio`), außer die Lehrkraft
   will nur das Bild. Eine `.drawio.svg` ist zugleich SVG – Browser, Word und Markdown zeigen sie als Bild.
14. **GRAFCET nur als `typ: grafcet`** (nie aus Rechtecken und Linien): Die Spec nennt die Struktur, das
   Werkzeug zeichnet die Normsymbole (`references/technologieschema-specs.md` Abschn. 5a, Schreibweise
   `references/notation-steuerungstechnik.md`). **Speichernde Aktionen haben immer beides:** die
   **Zuweisung** im Rechteck (`-Q1 := 1`, nicht `-Q1`) und den **Auslöser** am Rechteck (Pfeil bei
   Aktivierung oder Deaktivierung, Fähnchen bei Ereignis); `pruefen` meldet sonst ❌. Negation erscheint als
   Überstrich, Kommentare in Anführungszeichen. Immer `zuordnung` angeben, wenn eine Zuordnungsliste
   vorliegt; gibt eine fremde Aufgabe ältere Kennzeichen vor (`-SF1`), bleiben sie darüber erhalten (⚠).
   Als Lösungsbild (`…_loesung_…`) nur im Lehrerteil; die Text-Tabelle für die Zweitkorrektur kommt aus
   `edu-technologieschema textform`, nicht von Hand.
15. **FUP und Netzplan aus Grundformen** (Bausteine wie DIN EN 61131-3; Spec-Referenz Abschn. 5b): Elemente
   ohne Betriebsmittel tragen `ref` und `legende: false`.

## Vorgehen
1. **Anlage klären:** Bauteile, Bewegungen, Sensoren und Bedienelemente mit Kennzeichen sammeln
   (Aufgabentext Satz für Satz durchgehen); Verwendung und Notation festlegen.
2. **Anordnen:** Bereiche planen (Bedienfeld oben links, Prozess in der Mitte, Werkstückfluss von
   links nach rechts), Raster von 10 Pixeln, Rand mindestens 40 Pixel. Maße und Teile in
   `references/technologieschema-specs.md`, Muster in `assets/`.
3. **Spec schreiben:** `schema/46_<kurztitel>.yaml` mit `out: abbildungen/46_<kurztitel>`; im
   Abitur-Projekt die Namen des Projekts übernehmen (z. B. `…_abbN_<thema>`). Ausgangspunkt ist
   das passende Muster: `assets/spec-biegestation.yaml` (Zylinder), `assets/spec-tankanlage.yaml`
   (Behälter, Rohre, Pumpe), `assets/spec-foerderstation.yaml` (Band, Lichtschranke),
   `assets/spec-steuerstromkreis.yaml` (Schaltzeichen, Taster, Verbindungspunkte),
   `assets/spec-naeherungsschalter.yaml` (Näherungsschalter an Relais), `assets/spec-grafcet.yaml`
   (GRAFCET-Kette), `assets/spec-grafcet-verzweigung.yaml` (parallel, alternativ, alle Aktionsarten),
   `assets/spec-grafcet-teil.yaml` (einschließender Schritt, Zwangssteuerung), `assets/spec-fup.yaml`
   (Funktionsplan). Alle GRAFCET-Symbole: `assets/spec-grafcet-symbole.yaml`.
   Schaltzeichen: `references/schaltzeichen.md` bzw. `python3 scripts/edu.py technologieschema symbole`.
4. **Prüfen:** `python3 scripts/edu.py technologieschema pruefen schema/46_<kurztitel>.yaml` –
   alle ❌ beheben, jedes ⚠ ansehen (überlappende Beschriftungen, Linien durch Texte).
5. **Erzeugen:** `python3 scripts/edu.py technologieschema svg schema/46_<kurztitel>.yaml`
   (oder installiert `edu-technologieschema svg …`) – schreibt `.svg` und `.drawio.svg`.
6. **Ansehen:** `python3 scripts/vorschau_png.py abbildungen/46_<kurztitel>.svg` und die PNG
   betrachten – Teile am richtigen Ort, Pfeile in der richtigen Richtung, Beschriftungen frei,
   Grundstellung wie in der Fußzeile? Spec anpassen, neu erzeugen.
7. **Legende:** `python3 scripts/edu.py technologieschema legende schema/46_<kurztitel>.yaml`;
   Spalte *Lage / Aufgabe* ergänzen, wo die Aufgabe mehr sagt. Beim GRAFCET stattdessen die **Textform**:
   `python3 scripts/edu.py technologieschema textform schema/46_<kurztitel>.yaml`.
8. **Schemablatt** nach `assets/vorlage-schemablatt.md`: Einbindung, Alternativtext, Legende,
   Grundstellung, Vereinfachungen, Quelle, Qualitätscheck, Annahmen, Übergabe.

**Ohne Skriptausführung** (Assistent ohne Code): Spec, Legende (von Hand nach der Spec) und
Schemablatt ausgeben; die Lehrkraft erzeugt lokal mit `edu-technologieschema` (Aufruf wie oben)
und prüft die Vorschau. Kein SVG von Hand schreiben.

## Ausgabe
- `schema/46_<kurztitel>.yaml` – Spec (hier ändern)
- `abbildungen/46_<kurztitel>.drawio.svg` – **bearbeitbar** (app.diagrams.net, draw.io Desktop,
  draw.io-Erweiterung in VS Code; Datei öffnen bzw. hineinziehen): jedes Bauteil eine Form mit
  Andockpunkten an den Ankern (`unten`, `an1` …), Kennzeichen/Betriebsmittel/Aufgabe als Formdaten
  (*Bearbeiten → Daten bearbeiten*), Beschriftungen als Text zum Bauteil gruppiert (Doppelklick in die
  Gruppe), Linien und Rohre als Verbinder, die beim Verschieben angeschlossen bleiben
- `abbildungen/46_<kurztitel>.svg` (Bild, eine Gruppe `<g id="eN">` je Element, auch für Inkscape),
  `.png` (Word) – erzeugt
- `46_schema_<kurztitel>.md` – Schemablatt (Artefakt nach Skill-Vertrag) mit Legende
- Planungsakte: Artefakt 46 eintragen.

## Qualitätscheck
- [ ] `technologieschema pruefen` ohne ❌, Warnungen angesehen?
- [ ] PNG-Vorschau angesehen, nichts überlagert, Pfeile und Lage stimmen?
- [ ] Jedes Betriebsmittel der Aufgabe im Bild und in der Legende, nichts zusätzlich?
- [ ] Kennzeichen in Bild, Legende, Text und Zuordnungsliste gleich, eine Notation?
- [ ] Grundstellung in Bild und Fußzeile gleich; Bild verrät die Lösung nicht?
- [ ] Alternativtext, Bildunterschrift, Graustufen; keine Normzeichnung vorgetäuscht?
- [ ] Vorlage eines Dritten nur mit geklärten Rechten und Quelle?
- [ ] GRAFCET als `typ: grafcet`: speichernde Aktionen mit `:=` und Pfeil oder Fähnchen, Negation als Überstrich,
      Rücksprung mit Pfeil, `zuordnung` angegeben, Text-Tabelle aus `textform`?
- [ ] Bearbeitbare `.drawio.svg` mitgeliefert und in der Übergabe erklärt?
- [ ] Schemablatt für Lernende ohne Lösung und ohne Erklärtext, den das Bild schon zeigt
      (`references/schuelermaterial.md` Abschn. 2); keine Zeichnung aus Zeichen
      (`python3 scripts/zeichnungen_pruefen.py 46_*.md` ohne ❌)?

## Beispielaufrufe
> „Zeichne das Technologieschema zur Aufgabe: Ein Förderband bringt Werkstücke zu einer
> Lichtschranke, ein Zylinder schiebt sie in einen Behälter. Notation nach 81346.“

> „Die Biegestation in der Klausur braucht ein Bild: drei Zylinder mit je zwei Endlagensensoren,
> Start- und Stopptaster, Meldeleuchte. Dazu die Legende für das Schülermaterial.“

> „Ich habe eine Skizze der Tankanlage mit drei Füllstandsschaltern – mach daraus ein sauberes
> Schema und eine Lösungsfassung mit eingezeichnetem Füllstand.“

> „Im Erwartungshorizont stehen GRAFCET und FUP als ASCII-Skizze – zeichne beide als Lösungsbild.“

> „GRAFCET zur Funktionsbeschreibung: Die Warnleuchte wird im Schritt 4 gesetzt und im Schritt 1 wieder
> zurückgesetzt, dazu die Tabelle für die Zweitkorrektur.“

## Referenzen – wann lesen
- `references/technologieschema-specs.md` – **immer** (Spec-Aufbau, Bauteile, Anker, Maße, Fehler).
- `assets/spec-biegestation.yaml`, `assets/spec-tankanlage.yaml`, `assets/spec-foerderstation.yaml`,
  `assets/spec-steuerstromkreis.yaml`, `assets/spec-naeherungsschalter.yaml`, `assets/spec-grafcet.yaml`,
  `assets/spec-grafcet-verzweigung.yaml`, `assets/spec-grafcet-teil.yaml`, `assets/spec-fup.yaml` – Muster; das
  passende als Ausgangspunkt nehmen. `assets/spec-grafcet-symbole.yaml` – alle GRAFCET-Symbole auf einer Tafel.
- `references/schaltzeichen.md` – alle Schaltzeichen mit Klassen, Anschlüssen und Herkunft (bei `typ: symbol`).
- `assets/vorlage-schemablatt.md` – **immer** (Ausgabeformat).
- `references/notation-steuerungstechnik.md` – Kennzeichen und Schreibweise (Anlage zum Material).
- `references/normen-technik.md` – Hintergrund zu Kennzeichen und Normen (Abschn. 2 und 5), bei Fragen zur Notation.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/edu.py` – startet `edu-technologieschema` aus der mitgelieferten Kopie
  (`scripts/eduwerkzeuge/`); `scripts/vorschau_png.py` – PNG-Vorschau für Sichtprüfung und Word.

# ANHÄNGE

## Anhang: assets/vorlage-schemablatt.md

---
artefakt: Technologieschema – Schemablatt
titel: "[Anlage / Aufgabe]"
skill: technologieschema-erstellen
skill_version: "1.6"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld bzw. Lerngebiet mit Titel]"
dqr: 0
status: "KI-Entwurf – fachlich zu prüfen"
---

# Technologieschema: [Anlage]

**Bezug:** [Lernsituation / Aufgabe / Klassenarbeit / Abiturvorschlag, Dateinamen] · **Ablage:** `schema/`, `abbildungen/`

## S1 – [Titel des Schemas]

![[Alternativtext: was das Bild zeigt, mit den Kennzeichen, in einem Satz]](abbildungen/46_[kurztitel].svg)

*Abbildung 1: [Bildunterschrift – Grundstellung, Pfeile, Abkürzungen]*

### Legende

[Ausgabe von `edu-technologieschema legende schema/46_[kurztitel].yaml`; Spalte *Lage / Aufgabe* ergänzen.
Beim GRAFCET statt der Legende die Tabelle aus `edu-technologieschema textform schema/46_[kurztitel].yaml`.]

| Referenzkennzeichen | Betriebsmittel | Lage / Aufgabe |
|---|---|---|
| -S1 | Taster | [Start …] |

| Feld | Eintrag |
|---|---|
| Spec (hier ändern) | `schema/46_[kurztitel].yaml` |
| Dateien | `.drawio.svg` (bearbeitbar in diagrams.net, zugleich Bild) · `.svg` (Bild) · `.png` (Word, aus `vorschau_png.py`) |
| Kennzeichnung | DIN EN IEC 81346-2:2020 (immer); [Entsprechungen einer Vorlage, z. B. S1 → -S1, Y1 → -Q1] |
| Schaltzeichen | [keine · DIN EN 60617, alle mit Herkunft *Liste* · mit 🔎 abgleichen: Name, mit Norm oder Tabellenbuch geprüft am …] |
| Grundstellung | [Zylinder, Ventile, Füllstand, Werkstück – wie im Bild] |
| Verwendung | [Aufgabenmaterial · Lösungsbild (getrennt ablegen) · Arbeitsblatt] |
| fachliche Vereinfachung | [z. B. „ohne Sicherheitseinrichtungen“ – sonst „keine“] |
| Vorlage / Quelle | [eigene Anlage · Skizze der Lehrkraft · fremde Abbildung mit Quelle und geklärten Rechten] |

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| `edu.py technologieschema pruefen` ohne ❌, Warnungen angesehen | | |
| PNG-Vorschau angesehen: Bauteile am richtigen Ort, nichts überlagert oder abgeschnitten | | |
| Jedes Betriebsmittel der Aufgabe im Bild und in der Legende, nichts Zusätzliches | | |
| Kennzeichen im Bild, in der Legende und im Text gleich; nur nach DIN EN IEC 81346-2:2020, Klasse passt zum Bauteil | | |
| Linien rechtwinklig; keine Warnung „knickt nur um …“ offen | | |
| GRAFCET: `typ: grafcet`, speichernde Aktionen mit Zuweisung und Pfeil oder Fähnchen, Negation als Überstrich | | |
| Schaltzeichen: Herkunft geprüft, 🔎-Zeichen mit Norm oder Tabellenbuch abgeglichen | | |
| Grundstellung im Bild und in der Beschreibung gleich | | |
| Bild verrät die Lösung nicht (keine Soll-Abläufe, Zustände, Schrittfolgen) | | |
| Alternativtext und Bildunterschrift vorhanden; nur Graustufen, in Schwarzweiß lesbar | | |
| Keine Normzeichnung vorgetäuscht (kein Schalt- oder Pneumatikplan) | | |
| Lösungsbild getrennt vom Aufgabenbild abgelegt | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Einbindung: `![…](abbildungen/46_….svg)`; für Word die PNG
- Bearbeiten: `abbildungen/46_….drawio.svg` in app.diagrams.net öffnen; danach ist diese Datei die
  Quelle (nicht aus der Spec neu erzeugen), Kennzeichen in Legende und Zuordnungsliste nachziehen
- Legende und Funktionsbeschreibung nennen jedes Betriebsmittel mit demselben Kennzeichen
- Empfohlene nächste Skills: `unterrichtsmaterial-erstellen` (Schema im Arbeitsblatt),
  `material-pruefen`, `schuelerseiten-veroeffentlichen`

> KI-gestützt erstellt (Skill technologieschema-erstellen v1.6). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: references/normen-technik.md

# Normen für Prüfungsaufgaben Technik (Informationstechnik, Mechatronik)

**Wozu:** Was eine Lösung festlegt, folgt einer Norm oder der Notation des Unterrichts. Diese
Referenz fasst zusammen, was Aufgaben, Musterlösungen und Bewertungsmerkmale in den Lerngebieten
*Technische Prozesse steuern* (IT1, METRO 2, ET2), *Netzwerke* (IT2), *Messwerte erfassen* (IT4,
METRO 3), Software (IT3, IT5) und Antriebe (METRO 5) aus den Normen brauchen. Normtexte sind nicht
frei zugänglich: Die Angaben sind in eigenen Worten nach Leseproben, Merkblättern der PAL und
Sekundärquellen zusammengefasst (Abschn. 11, Stand der Recherche 2026-10). Unsicheres ist mit 🔎
markiert – vor der Einreichung mit dem Normtext oder dem eingeführten Tabellenbuch abgleichen.

**Einheitliche Schreibweise:** Wo die Normen Spielraum lassen (Tiefe der Kennbuchstaben, getippte
Negation, Zeitschreibweise, Zuordnungsliste, GRAFCET in Textform, Bezeichner im Programm), legt das
**Notationsblatt** `notation-steuerungstechnik.md` eine Form fest; es geht als Anlage ins
Schülermaterial.

## Inhalt
1. Grundregeln für Aufgaben
2. Referenzkennzeichen – DIN EN IEC 81346-1 und -2
3. GRAFCET – DIN EN 60848
4. Steuerungsprogramme – IEC 61131-3 und Mikrocontroller
5. Schaltpläne, Schaltzeichen, Anschlussbezeichnungen
6. Sicherheit an Maschinen – Bedienteile, Farben, Stopp, Not-Halt
7. Sensorik, Einheitssignale, Regelungstechnik
8. Netzwerke
9. Software – UML, Struktogramm, Programmablaufplan
10. Größen, Einheiten, Schreibweise
11. Quellen

---

## 1. Grundregeln für Aufgaben

1. **Norm und Ausgabe nennen**, wo eine Notation bewertet wird – im Schülermaterial (Hinweise oder
   Teilaufgabe): „Die Betriebsmittel sind nach DIN EN IEC 81346-2:2020 gekennzeichnet.“, „Entwickeln
   Sie einen GRAFCET nach DIN EN 60848.“ `bmk_pruefen.py` liest die genannte Ausgabe (T.8).
2. **Eine Notation je Vorschlag.** Weicht der Unterricht ab (ältere Ausgabe, Hauskonvention,
   Herstellernotation), gilt sie für Aufgabe, Anlagen und Musterlösung gleichermaßen; im
   Schülermaterial nennen, im Begleitblatt begründen. Nie mischen.
3. **„Normgerecht“ im Merkmal auflösen.** Das Lehrermaterial nennt die Normelemente, die zählen
   (z. B. „Initialschritt doppelt umrandet, Rücksprung mit Pfeil, Transitionen mit Bedingung“) –
   eigenes Merkmal mit 1–2 BE, getrennt von der Funktion.
4. **Tabellenbuch beachten.** Ältere Ausgaben (etwa vor 2021 🔎) zeigen Kennbuchstaben der
   Ausgabe 2009. Steht die Lösung nur im Tabellenbuch, den benutzten Stand im Erwartungshorizont
   angeben.
5. **Was nicht genormt ist** – Technologieschema, Zuordnungsliste, Pseudocode – legt die Aufgabe
   selbst fest (Legende, Tabellenkopf mit Beispielzeile, Hilfsmitteldokument).

## 2. Referenzkennzeichen – DIN EN IEC 81346-1 und -2

**Ausgaben**

| Teil | gültige Ausgabe | Inhalt |
|---|---|---|
| Teil 1 | DIN EN IEC 81346-1:2024-07 (IEC 81346-1:2022) | Strukturierung, Aspekte und Vorzeichen |
| Teil 2 | **DIN EN IEC 81346-2:2020-10** (IEC 81346-2:2019) | Klassen und Kennbuchstaben |
| Teil 2, Vorgänger | DIN EN 81346-2:2010-05 (IEC 81346-2:2009) | zurückgezogen; danach noch die zentralen Mechatronik-Prüfungen in Niedersachsen 2020–2026 (z. B. -SF elektrischer Taster, -SJ pneumatischer Taster, -RZ, -AZ) |

Die PAL setzt die Ausgabe 2020 in den IHK-Prüfungen um (Merkblatt Stand Juni 2024). Für neue
Vorschläge gilt **die Ausgabe 2020**; die Ausgabe 2009 nur, wenn der Unterricht sie verwendet – dann
im Schülermaterial nennen (Abschn. 1).

**Aufbau eines Kennzeichens:** Vorzeichen, Kennbuchstaben, Zählnummer, ohne Leerzeichen: `-S1`,
`-BT2`, `-Q1`.
- Vorzeichen (Teil 1): `-` Produkt (in Aufgaben üblich), `=` Funktion, `+` Ort, `%` Typ (neu seit
  2022), `#` andere Aspekte. Kombinationen wie `+S1-K1` nur, wenn im Unterricht eingeführt.
- **Ein bis drei Kennbuchstaben** (Teil 2): Klasse (`-B1`), Unterklasse (`-BG1`), Unter-Unterklasse
  (`-BGB1`). Die Norm lässt jede Tiefe zu; die PAL zeigt Schaltpläne nur mit Klassen und mit
  Unterklassen.
- **So kurz wie möglich** (didaktische Reduktion, Festlegung der Fachberatung 31.10.2026): Standard
  ist die **Klasse allein** (-S1, -B1, -K1, -Q1, -M1, -P1). Eine **Unterklasse** nur, wenn eine Klasse
  in der Aufgabe **verschiedenartige Betriebsmittel** enthält, die das Kennzeichen unterscheiden soll –
  dann für **alle** Kennzeichen dieser Klasse (nicht -B1 neben -BT2); die übrigen Klassen bleiben kurz.
  Die dritte Ebene (-BGB1) nur, wenn der Unterricht sie verlangt. `bmk_pruefen.py` (T.8) meldet
  überflüssige Unterklassen und gemischte Tiefe innerhalb einer Klasse.
- Beispiel Bewässerung: Taster, Schütz, SPS und Leuchtmelder je nur einer Art → -S1, -S2, -Q1, -K1,
  -P1, -P2; Sensoren für Füllstand, Bodenfeuchte und Temperatur → -BL1, -BM1, -BM2, -BT1; Pumpenmotor
  und Magnetventile → -MA1, -MB1, -MB2.
- Nebeneffekt: Die Klassenbuchstaben B, S, K, Q, M, P, R, G, T sind in den Ausgaben 2009 und 2020
  gleich – die Kurzform vermeidet die meisten Unterschiede der Ausgaben (-SF/-SJ, -KF/-KE, -RZ/-RN).
- **A, I und O** sind keine Klassen; **D, J, L, V, Y, Z** sind reserviert. Eine Klasse „Sonstiges“
  gibt es nicht: Passt keine Unterklasse, nimmt man die Klasse darüber.
- Klassifiziert wird nach der **inhärenten Funktion** – was das Objekt erfasst oder bewirkt, nicht
  nach Bauart oder Einbauort: Der Druckschalter am Zylinder ist -BP, der Endlagenschalter daneben
  -BG. Bei mehrdeutigen Fällen die Aufgabe des Betriebsmittels in der Legende nennen.
- Die Zählnummer zählt je Kennbuchstaben: -B1, -B2 bzw. -BG1, -BG2, -BP1.

**Klassen – Standard in Aufgaben**

| BMK | Klasse | typische Betriebsmittel |
|---|---|---|
| -B | Information erfassen | Sensoren und Geber: Näherungs-, End-, Druck-, Schwimmerschalter, Temperaturfühler |
| -S | menschliche Betätigung erfassen | Taster, Schalter, Wahl- und Schlüsselschalter, handbetätigtes Ventil |
| -K | Signale verarbeiten | SPS, Kleinsteuerung, Mikrocontroller, Relais, Zeitrelais, pneumatisches UND/ODER |
| -Q | Fluss steuern | Schütz, Leistungs- und Motorschutzschalter, Wegeventil |
| -M | Antreiben | Motor, Ventilspule, Elektromagnet, Zylinder |
| -P | Information darstellen | Leuchtmelder, Hupe, Anzeige, Manometer |
| -R | Begrenzen | Drossel- und Drosselrückschlagventil, Rückschlagventil, Widerstand, Diode |
| -G | Fluss erzeugen | Pumpe, Kompressor, Lüfter, Generator; Wartungseinheit (PAL) 🔎 |
| -T | Umwandeln | Netzteil, Frequenzumrichter, Messumformer |
| -F | Schützen | Sicherung, Leitungsschutzschalter, thermisches Überlastrelais |
| -E | Aussenden | Leuchte, Heizung |
| -X, -W | Verbinden, Leiten | Klemme, Steckdose, Patchfeld; Kabel, Leitung |
| -C | Speichern | Kondensator, Akku, Tank |

**Unterklassen – nur, wenn eine Klasse verschiedenartige Betriebsmittel enthält** (Auswahl der
Ausgabe 2020; deutsche Benennungen sinngemäß; in Klammern Beispiele der dritten Ebene)

| BMK | Bedeutung | typische Betriebsmittel | Ausgabe 2009 |
|---|---|---|---|
| **B** | **Information erfassen** | | |
| -BG | Lage, Abstand, Winkel | Näherungsschalter (induktiv, kapazitiv, optisch), Endlagen-/Positionsschalter (BGB), Zylinderschalter, Abstandssensor (BGC), Drehgeber/Winkel (BGE) | gleich |
| -BP | **Druck** | Druckschalter (BPB), Drucktransmitter (BPA), Differenzdruck (BPC, BPD), Vakuumschalter | gleich |
| -BM | **Feuchte** | Feuchtesensor (BMA), Hygrostat (BMB); Bodenfeuchte 🔎 (2009: „Wassergehalt, Feuchte“) | gleich |
| -BT | Temperatur | Pt100, Thermoelement (BTA), Thermostat/Temperaturschalter (BTB) | gleich |
| -BL | Füllstand | Schwimmerschalter (BLB), Füllstandsensor (BLA) | gleich |
| -BF | Durchfluss | Durchflusssensor, Strömungswächter | gleich |
| -BS | Drehzahl, Geschwindigkeit, Beschleunigung | Tachogenerator, Drehzahlwächter, Beschleunigungssensor | gleich |
| -BW | Kraft, Gewicht, Drehmoment | Wägezelle, DMS-Kraftaufnehmer, Drehmomentsensor | gleich |
| -BR | Strahlung, Licht | Lichtsensor, Lichtschranke/Lichtgitter, Fotozelle, IR- und UV-Sensor | gleich |
| -BQ | Stoffkonzentration | Gas-, Rauch-, CO₂-, Trübungssensor | gleich |
| -BA / -BC | elektrische Spannung / Strom | Spannungs-, Stromwandler, Überlastrelais (elektronisch, BC) | 🔎 |
| -BE | elektrisches oder magnetisches Feld | Reedkontakt, Magnetfeldsensor | 🔎 |
| -BJ / -BH | Leistung / Energie | Leistungsmesser, Energiezähler | 🔎 |
| -BK | Zeit | Uhr, Zeitschaltuhr | 🔎 |
| -BX | Bild und Ton | Kamera, Mikrofon | 🔎 |
| -BY | gespeicherte Information | RFID-, Barcode-, Kartenleser | 🔎 |
| -BZ | Ereignisse, Anzahl | Zähler, Präsenz- und Personenmelder | 🔎 |
| **S** | **menschliche Betätigung erfassen** | | |
| -SJ | Fingerbetätigung | **Drucktaster (SJB)**, Kippschalter (SJA), Touch-Taster (SJC); handbetätigte Ventile | **-SF** (elektrisch); -SJ war nur das handbetätigte Ventil |
| -SG | Handbetätigung | Drehknopf/Knebel (SGA), Handhebel, Schlüsselschalter (SGF) | 🔎 |
| -SH | Fußbetätigung | Fußschalter, Pedal | 🔎 |
| -SK | Bewegung | Joystick, Maus | 🔎 |
| -SF | Gesichtserkennung | (in Prüfungsaufgaben kaum) | **Taster, Schalter elektrisch** |
| **K** | **Signale verarbeiten** | | |
| -KE | elektrische Signale verarbeiten | **SPS, Kleinsteuerung, Mikrocontroller (KEB)**, PC (KEA), E/A- und Kommunikationsbaugruppe (KEC), Router, Firewall (KED) | -KF 🔎 |
| -KF | elektrische Signale weiterleiten | Relais, Hilfsschütz (KFA), Zeitrelais (KFB), Repeater, Netzwerk-Switch (KFE) | gleich (2009 auch SPS) |
| -KH | fluidische Signale verarbeiten | Zweidruck- und Wechselventil (UND/ODER), Vorsteuerventil (KHB) | gleich |
| **M** | **Antreiben** | | |
| -MA | elektromagnetisch, drehend | Elektromotor (MAA), Schrittmotor (MAB) | gleich |
| -MB | elektromagnetisch, linear | **Ventilspule, Elektromagnet (MBB)**, Linearmotor (MBA) | gleich |
| -MM | fluidisch | Pneumatik-/Hydraulikzylinder (MMB/MMA), Druckluft-/Hydraulikmotor | gleich |
| **P** | **Information darstellen** | | |
| -PF | Zustand sichtbar | Leuchtmelder, Signalleuchte (PFA), Stellungsanzeige | gleich |
| -PG | Wert anzeigen | Manometer (PGP), Thermometer (PGT), Volt-/Amperemeter, Zähleranzeige | gleich |
| -PH | grafisch anzeigen | Display, Bildschirm | 🔎 |
| -PJ | akustisch | Hupe (PJB), Summer, Klingel, Lautsprecher | gleich |
| **Q** | **Fluss steuern** | | |
| -QA | elektrische Energie schalten | **Schütz (QAA)**, Leistungs- und Motorschutzschalter (QAB), Halbleiterschalter/SSR (QAC) | gleich |
| -QB | elektrisch trennen | Lasttrennschalter, Hauptschalter (QBA) 🔎 (PAL nennt den Hauptschalter unter QA) | gleich |
| -QM | Fluid schalten (geschlossen) | **Wegeventil**, Absperr-, Schnellentlüftungsventil | gleich |
| -QN | Fluid stetig verstellen | Proportional-, Stellventil | 🔎 |
| **R** | **Begrenzen, stabilisieren** | | |
| -RA | elektrisch begrenzen | Diode (RAA), Widerstand (RAC), Drossel (RAB) | gleich |
| -RM | Rückfluss sperren | Rückschlagventil (RMA) | gleich |
| -RN | Durchfluss begrenzen | **Drosselventil, Drosselrückschlagventil**, Stromregelventil | **-RZ** für das Drosselrückschlagventil (-RN war nur die Drossel) |
| **G** | **Fluss erzeugen** | | |
| -GQ | Gasstrom | Kompressor (GQA), Lüfter (GQB); Wartungseinheit: Klasse G laut PAL 🔎 | 2009: Wartungseinheit oft -AZ (Klasse A entfällt) |
| -GP | Flüssigkeitsstrom | Pumpe (GPA Verdränger-, GPB Kreiselpumpe) | gleich |
| -GA / -GB | Generator / Batterie (Primärzelle) | Generator, Batterie; Akku: -CC | 🔎 |
| **T** | **Umwandeln** | | |
| -TA | Energie, gleiche Stromart | Transformator (TAA), Frequenzumrichter (TAC) | 🔎 |
| -TB | AC ↔ DC | Gleichrichter (TBA), Wechselrichter (TBB) | gleich |
| -TC | Stromversorgung | Netzteil 24 V DC (TCB) | 🔎 |
| -TF | Signal umwandeln | Messumformer (TFC), Verstärker (TFA) | gleich |
| **E, F, C, W, X** | | | |
| -EA / -EB | Licht / elektrische Heizung | Leuchte, Lampe / Heizstab, Heizkabel | gleich |
| -FC | Überstrom schützen | Sicherung (FCA), Leitungsschutzschalter (FCB), Bimetall-Überlastrelais (FCC) | gleich |
| -FB | Fehlerstrom schützen | Fehlerstrom-Schutzschalter (RCD) 🔎 | gleich |
| -CA / -CC / -CM | speichern | Kondensator / Akku / Tank, Behälter | 🔎 |
| -WD / -WG / -WH | leiten | Energiekabel / Signal-, Datenleitung (WGB) / Lichtwellenleiter | gleich |
| -XD / -XG | verbinden | Klemme, Steckdose / Signalklemme, Anschlussdose, Patchfeld (XGC) | gleich |

„gleich“ heißt: Kennbuchstabe und Bedeutung decken sich in Prüfungsaufgaben; die Unterklassen der
Ausgabe 2009 sind nur teilweise belegt (🔎). Belegte Änderungen 2009 → 2020: Taster -SF → **-SJ**,
Drosselrückschlagventil -RZ → **-RN**, Klasse A (z. B. -AZ) entfällt, SPS -KF → **-KE** 🔎.

**Für die Aufgabe**
- Erst die Klassen festlegen, dann je Klasse prüfen: eine Art → nur die Klasse; mehrere Arten →
  Unterklassen aus der Tabelle für die ganze Klasse. Ein nicht aufgeführter Code wird mit Tabelle 2
  der Norm geprüft.
- Legende: BMK | Betriebsmittel | Lage bzw. Aufgabe (T.3); bei mehrdeutigen Fällen (Lichtschranke
  als Objektmelder: -BR oder -BG) die Aufgabe des Betriebsmittels nennen.
- In Netzplänen sind Gerätenamen wie „SW1“, „R1“ üblich; Referenzkennzeichen (-KFE, -KED) nur, wenn
  eingeführt.
- Fluidtechnik: Die Kennzeichnung nach ISO 1219-2 (z. B. „1V1“, „1A1“) ist eine andere Systematik –
  nicht mit -QM1/-MM1 mischen.

## 3. GRAFCET – DIN EN 60848

**Ausgabe:** DIN EN 60848:2014-12 (IEC 60848:2013, 3. Ausgabe; keine neuere bekannt). GRAFCET ist
eine **herstellerunabhängige Spezifikation** des Ablaufs; die Ablaufsprache (AS) der IEC 61131-3 und
Herstellersprachen (z. B. S7-GRAPH) sind Programmiersprachen. Im Auftrag unterscheiden:
„Entwickeln Sie einen GRAFCET“ ≠ „Programmieren Sie die Schrittkette in AS“. Weil GRAFCET nichts über
die Plattform sagt, ist er die gemeinsame Spezifikation für SPS, Kleinsteuerung und Mikrocontroller.
Festlegungen der Bibliothek (Notationsblatt): Initialschritt 0, getippte Negation „¬“, Zeit „5s/X3“
ohne Leerzeichen, Analogbedingungen mit physikalischem Wert und Einheit („[-BT1 > −16 °C]“), Textform
als Tabelle Schritt | Aktion | Transition zum Folgeschritt (`bmk_pruefen.py`, T.9).

| Element | Darstellung und Regel |
|---|---|
| Schritt | Quadrat mit Name (Zahl, auch 9a); Schrittvariable **X** + Name (X3) ist 1, solange der Schritt aktiv ist |
| Initialschritt | **doppelt umrandet**; aktiv beim Start ohne Bedingung; entspricht der Grundstellung |
| Transition | Querstrich auf der Wirkverbindung, **Bedingung rechts**, optional Name links in Klammern „(T3)“; Quelltransition ohne Verbindung nach oben, Schlusstransition ohne Verbindung nach unten |
| Wirkverbindung | Schritt und Transition wechseln sich ab; von oben nach unten ohne Pfeil, **aufwärts mit Pfeil** (Rücksprung) |
| Logik | UND „·“ (auch „*“), ODER „+“, NICHT als Überstrich; UND vor ODER, sonst Klammern; „1“ unterstrichen = immer erfüllt (Aufgaben schreiben es auch ohne Strich) |
| Flanke | ↑a steigend, ↓a fallend (Pfeil vor der Variablen) |
| Zeit | „t1/Variable/t2“, meist „5s/X3“ = 5 s nach Aktivierung von Schritt 3; „3s/-BG1“ = -BG1 seit 3 s ununterbrochen 1 |
| Vergleich | Bedingungen aus Zahlenwerten in eckigen Klammern, z. B. [C = 3], [-BT1 > −16 °C] 🔎 |
| Kommentar | in Anführungszeichen: „Zylinder fährt aus“ |
| Alternativverzweigung | ein Schritt, mehrere Transitionen; Bedingungen **schließen sich gegenseitig aus** |
| Parallelverzweigung | eine Transition aktiviert mehrere Schritte; Beginn und Ende mit **Doppelstrich**; die Transition nach der Zusammenführung schaltet erst, wenn alle letzten Schritte aktiv sind (Synchronisation) |
| Strukturierung | Makroschritt (Querlinien oben und unten, M…), einschließender Schritt (abgeschrägte Ecken; Rahmen um die eingeschlossene Kette, oben sein Name, zuerst aktiver Schritt mit *), Teil-GRAFCET (G…), Zwangssteuerung im Doppelrahmen: G5 {INIT}, { } leer, {3,4,8} bestimmte Schritte, {*} eingefroren – nur, wenn im Unterricht eingeführt (Betriebsarten, Not-Halt) |

**Aktionen** (Rechteck rechts am Schritt; mehrere Aktionen wirken gleichzeitig)

| Art | Darstellung | Wirkung |
|---|---|---|
| kontinuierlich wirkend | Variable im Rechteck: „-M1“ | 1, solange der Schritt aktiv ist; danach 0 |
| mit Zuweisungsbedingung | Bedingung an einem Strich über dem Rechteck | 1, solange Schritt aktiv **und** Bedingung erfüllt |
| zeitabhängig | Zuweisungsbedingung mit Zeit („2s/X6“), mit Überstrich zeitbegrenzt | verzögert bzw. zeitbegrenzt |
| speichernd wirkend | **im Rechteck immer die Zuweisung** („-Q1 := 1“), **am Rechteck der Auslöser**: Pfeil nach oben an der linken Kante bei Aktivierung, nach unten bei Deaktivierung, Strich mit Fähnchen und Ereignis („↑-B1“) bei Ereignis | Wert bleibt bis zur nächsten Zuweisung („-Q1 := 1“ … „-Q1 := 0“) |

Regeln für Musterlösung und Merkmale:
- Kontinuierlich und speichernd wirkende Aktionen **nie auf dieselbe Variable**; speichernde
  Aktionen vor allem für interne Variablen und Zähler („C := C + 1“), Rücksetzen nicht vergessen.
- **Kontaktart** steckt in der Bedingung: Ein Öffner (NC) liefert unbetätigt 1 – „Stopp betätigt“ ist
  dann der negierte Wert. Die Kontaktart steht deshalb im Schülermaterial (T.4).
- Gleichwertig sind: andere Schrittnummern und Kommentare, zusätzliche Leerschritte, gleichwertige
  Bedingungen (z. B. Klammern), kontinuierliche statt speichernde Aktion bei gleicher Wirkung –
  Merkmale funktional formulieren.
- Typische Fehler (Prüfsteine, 0 BE für das Normmerkmal): Schritt an Schritt ohne Transition,
  Rücksprung ohne Pfeil, kein Initialschritt, Alternativzweige nicht ausschließend, speichernde Aktion
  ohne Zuweisung („-Q1“ statt „-Q1 := 1“) oder ohne Pfeil am Rechteck, speichernd gesetzt und nie
  zurückgesetzt, Zeit auf den falschen Schritt bezogen, Öffner nicht negiert.
- **Positionssensor beim Weiterdrehen:** Meldet ein Sensor die Ruhelage und bleibt beim Anlaufen noch
  belegt, schaltet die Transition „-B1“ sofort, der Antrieb läuft nie. Richtig: Flanke „↑-B1“ oder
  zwei Schritte mit „¬-B1“ (Position verlassen) und „-B1“ (nächste Position erreicht); beide gleichwertig.

## 4. Steuerungsprogramme – IEC 61131-3 und Mikrocontroller

**Ausgabe:** IEC 61131-3:2025 (4. Ausgabe, Mai 2025) ersetzt die Ausgabe 2013 (DIN EN 61131-3:2014-06);
deutsche Fassung 🔎. Wichtigste Änderung für Aufgaben: **AWL (Anweisungsliste, IL) ist gestrichen**
(seit 2013 als veraltet gekennzeichnet). Hersteller bieten AWL/STL zum Teil weiter an – in neuen
Aufgaben nicht verlangen.

| Sprache | Art | Hinweis für Aufgaben |
|---|---|---|
| KOP – Kontaktplan (LD) | grafisch | Öffner/Schließer der **Programmlogik**, nicht der Geberkontakte: Ein NC-Geber wird mit Schließerabfrage auf 1 geprüft |
| FUP – Funktionsbausteinsprache (FBD) | grafisch | Logiksymbole &, ≥1, =1; Negation als Kreis |
| ST – Strukturierter Text | textuell | IF/CASE/FOR; Zuweisung „:=“, Vergleich „=“ |
| AS – Ablaufsprache (SFC) | Struktur | Schritte, Transitionen, Aktionen; nicht mit GRAFCET gleichsetzen |

- **Standardbausteine:** TON (Einschaltverzögerung), TOF (Ausschaltverzögerung), TP (Impuls), CTU,
  CTD, CTUD (Zähler), R_TRIG/F_TRIG (Flanken), SR (**setzdominant**), RS (**rücksetzdominant**).
- **Operanden:** Normform „%IX0.0“, „%QX0.1“, „%MW10“ (Eingang, Ausgang, Merker; X Bit, W Wort);
  Herstellerformen wie „%I0.0“, „E0.0“, „I1“ (LOGO). Die Schreibweise der eingesetzten Steuerung
  im Schülermaterial festlegen (Zuordnungsliste mit Beispielzeile, T.5).
- **Datentypen und Literale:** BOOL, INT, REAL, TIME („T#5s“). Analogwerte: Zahlbereich der
  Baugruppe angeben (Abschn. 7).

**Mikrocontroller als Steuerung** (RRL: IT1 „Steuerungseinheiten“, IT4 „Mikrocontroller für die
Messhardware“). Für Mikrocontroller gibt es keine Norm wie IEC 61131-3; die Aufgabe legt fest, was
die Lösung bestimmt:

| Punkt | Festlegen in der Aufgabe bzw. Anlage | Hintergrund |
|---|---|---|
| Board und Pegel | Board, Logikpegel, ob eine Ein-/Ausgabeplatine 24-V-Geber anpasst | Arduino Uno 5 V; ESP32, STM32 und Raspberry Pi Pico 3,3 V (Tabelle unten); 24-V-Geber nur über Optokoppler oder Spannungsteiler |
| Eingangslogik | Spalte „Signal 1 bedeutet“; Pull-up oder Pull-down | Mit internem Pull-up und Taster gegen Masse liefert ein **betätigter Schließer 0** – die Kontaktart allein bestimmt das Signal nicht mehr |
| Ausgänge | Treiber (Transistor, Relaismodul), ggf. invertierend | Ein Pin liefert nur wenige Milliampere (Uno: 20 mA empfohlen, 40 mA absolut; andere Boards laut Datenblatt 🔎); viele Relaismodule schalten bei Low |
| Analogeingang | Wertebereich **im Programm**, Bürdenwiderstand | hängt von Board, Bibliothek und Einstellung ab (Tabelle unten) – nie nur „12 bit“ angeben |
| Taster | ob Entprellen zur Aufgabe gehört | mechanische Kontakte prellen einige Millisekunden; Software-Entprellung z. B. 20 ms 🔎 |
| Zeiten | Zeit seit Schrittbeginn statt Warteschleife | `delay()` blockiert den Zyklus; Zeitbedingung „5s/X3“ als Vergleich mit der beim Schrittwechsel gespeicherten Zeit (`millis()`) |
| Programmstruktur | Zyklus wie bei der SPS | Eingänge lesen → Transitionen prüfen, Schritt wechseln → Ausgänge aus dem aktiven Schritt setzen; GRAFCET als Zustandsautomat (Variable für den aktiven Schritt, `switch`/`if`) |
| Sprache | „in der im Unterricht verwendeten Sprache“ | C/C++ (Arduino-Umgebung) oder Python (MicroPython); Bezeichner `PIN_S1`, `s1` nach Notationsblatt |
| Sicherheit | Not-Halt und Schutzfunktionen ausklammern | Ein Mikrocontroller ist wie eine Standard-SPS keine Sicherheitssteuerung (Abschn. 6) |

**Analogwerte je Plattform** – den Wertebereich, mit dem das Programm rechnet, in der Anlage nennen;
sonst hat eine Umrechnung mehrere richtige Ergebnisse (K.4).

*Siemens SPS (S7-1200/1500; Analogbaugruppen und -signalboards):*

| Signal | Nennbereich | Übersteuerung bis | Untersteuerung bis | Überlauf / Unterlauf |
|---|---|---|---|---|
| ±10 V, ±5 V, ±20 mA (bipolar) | **−27 648 … +27 648** | 32 511 | −32 512 | 32 767 / −32 768 |
| 0 … 10 V, 0 … 20 mA (unipolar) | 0 … 27 648 | 32 511 (11,76 V bzw. 23,52 mA) | – 🔎 | 32 767 / −32 768 |
| 4 … 20 mA, 1 … 5 V (lebender Nullpunkt) | 0 … 27 648 (4 mA ↦ 0) | 32 511 (22,81 mA) | −4 864 (1,185 mA) | 32 767 / −32 768 (Drahtbruch) |

Umrechnen mit NORM_X (Rohwert → 0,0 … 1,0; bei bipolaren Signalen MIN = −27 648) und SCALE_X
(→ physikalischer Wert); ältere Steuerungen mit dem Baustein SCALE. Analogausgänge nutzen dieselben
Bereiche.

*Kleinsteuerungen und weitere Steuerungen:*

| System | Operanden | Analogwert 0 … 10 V | Analogwert 4 … 20 mA | Hinweise |
|---|---|---|---|---|
| **Siemens LOGO!** (8) | I1 …, Q1 …, AI1 … AI8, AQ1 … AQ8, Merker M1 …, Analogmerker AM1 … 🔎 Anzahl je Modell | 0 … 1000 (über 10 V bleibt 1000) | **200 … 1000** – das Analogmodul rechnet auf 0 … 20 mA, 4 mA ergibt 200 | Basisgeräte 12/24 V: I1, I2, I7, I8 als Analogeingänge (0 … 10 V) nutzbar 🔎; Analogverstärker: Wert · Gain + Offset, für 4 … 20 mA → 0 … 1000 **Gain 1,25, Offset −250**; Analogausgang 0 … 1000 |
| **Eaton easyE4** | Basisgerät I1 … I16, Q1 … Q16; Erweiterungen ab I17, Q17; Analog IA1 … IA4 (Basisgerät, = I5 … I8), ab IA5 bzw. QA5 (Erweiterung); Merker M, MB, MW, MD | 0 … 4095 (12 bit, Datentyp DINT); Basisgerät DC/UC nur 0 … 10 V | **819 … 4095** (Erweiterung EASY-E4-DC-6AE1; bezogen auf 0 … 20 mA) | 0 … 20 mA → 0 … 4095; Pt100- und Ni1000-Erweiterungen liefern skalierte Temperaturen; ältere easy500/700/800: 10 bit, 0 … 1023 🔎 |
| **WAGO** 750 mit PFC100/PFC200 (CODESYS, e!COCKPIT) | IEC 61131-3: %IX, %QX (Byte.Bit), %IW, %QW; im Prozessabbild **zuerst Analog- und Sondermodule wortweise, dann die Digitalbits** – die Adresse hängt von der Modulreihenfolge ab | 0 … **32 760** (0x7FF8), 5 V ↦ 16 384 (750-459) | 0 … **32 760** (750-466, neuere 750-455; ältere Handbücher 0x7FFC) | Messwert in Bit 14 … 3 (12 bit), Bit 2 … 0 Status – für 0 … 4095 drei Bit nach rechts schieben; Über-/Unterbereich: nächster darstellbarer Wert und Statusbyte 0x42 bzw. 0x41; Varianten mit anderem Bereich (z. B. /000-003: 3,8 … 20,5 mA) laut Handbuch 🔎 |

LOGO! und easyE4 beziehen 4 … 20 mA auf den Bereich 0 … 20 mA: Der Rohwert beginnt **nicht** bei 0. In
Aufgaben deshalb den Rohwertbereich für 4 mA und 20 mA ausdrücklich nennen oder die Skalierung
(Gain/Offset bzw. Skalierungsbaustein) vorgeben.

*Mikrocontroller:*

| Board | Pegel | ADC | Wert im Programm | Pins | 4 … 20 mA über Bürde |
|---|---|---|---|---|---|
| Arduino Uno (ATmega328P) | 5 V | 10 bit, Referenz 5 V | `analogRead`: 0 … 1023 | D2 … D13, A0 … A5 | 250 Ω → 1 … 5 V → 205 … 1023 |
| ESP32 | 3,3 V, nicht 5-V-fest | 12 bit, nichtlinear an den Bereichsgrenzen; Messbereich je Dämpfung (bei 11 dB laut Espressif etwa 0,15 … 2,45 V genau 🔎) | Arduino-Kern `analogRead`: 0 … 4095 (Rohwert), `analogReadMilliVolts`: kalibrierte mV; MicroPython `read_u16`: 0 … 65 535 | GPIO-Nummer (GPIO34); bei aktivem WLAN nur ADC1-Pins (GPIO32 … GPIO39) | 120 Ω → 0,48 … 2,4 V → 480 … 2400 mV |
| STM32 (z. B. Nucleo-Boards) | 3,3 V; viele Pins 5-V-fest, nicht im Analogbetrieb 🔎 | meist 12 bit, Referenz 3,3 V (einige Familien bis 16 bit) | Arduino-Kern: `analogRead` 10 bit, mit `analogReadResolution(12)` 0 … 4095; MicroPython `read_u16`: 0 … 65 535 | Port und Nummer (PA0, PB12) | 120 Ω → 0,48 … 2,4 V → 596 … 2978 (12 bit) |
| Raspberry Pi Pico (RP2040, RP2350) | 3,3 V | 12 bit, Referenz 3,3 V; Analog an GP26 … GP28 | MicroPython `read_u16`: 0 … 65 535 (12 bit hochskaliert); Arduino-Kern: `analogRead` 10 bit, mit `analogReadResolution(12)` 0 … 4095 | GP0 … GP28 | 120 Ω → 0,48 … 2,4 V → 596 … 2978 bzw. 9 532 … 47 662 |

- Bürde so wählen, dass 20 mA unter dem genauen Eingangsbereich bleiben (3,3-V-Boards: 120 Ω, 5-V-Board:
  250 Ω) und die Platine einen Schutz gegen Überspannung hat.
- Umrechnung Spannung → Wert als Wert = U / U_ref · (2ⁿ − 1) vorgeben (manche Lehrbücher teilen durch
  2ⁿ) und die Rundung festlegen; beim ESP32 besser die kalibrierte Spannung in mV verwenden.

**Plattformneutrale Steuerungsaufgaben** (wenn die Schule mehrere Plattformen nutzt):
- Funktion als GRAFCET bzw. Logikplan verlangen; Analogwerte im GRAFCET als physikalische Größe.
- Zuordnungsliste mit Spalten „Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller“ und einer
  Anlage mit den verfügbaren Ein- und Ausgängen je Plattform; Rohwert-Rechnungen nur, wenn die
  Plattform feststeht – sonst Stromstärke bzw. Spannung als plattformneutrale Größe rechnen lassen.
- Programmaufträge „in der im Unterricht verwendeten Sprache“; Merkmale prüfen das Verhalten
  (Schrittwechsel, Ausgänge, Zeiten), nicht eine Plattform.

## 5. Schaltpläne, Schaltzeichen, Anschlussbezeichnungen

| Gegenstand | Norm | Kern für Aufgaben |
|---|---|---|
| Schaltzeichen Elektrotechnik | IEC 60617 (Datenbank), DIN EN 60617 🔎 | Kontakte, Spulen, Geber, Melder; binäre Logik &, ≥1, =1, 1 mit Negationskreis |
| Dokumente der Elektrotechnik | DIN EN 61082-1:2015 (IEC 61082-1:2014) | Übersichtsschaltplan, Stromlaufplan (aufgelöste Darstellung, Strompfade nummeriert), Anschlussplan; Betriebsmittel unbetätigt und spannungslos dargestellt 🔎 |
| Anschlüsse an Schaltgeräten | DIN EN 60947-1 und -5-1 🔎 | Spule A1/A2; Hauptkontakte 1-2, 3-4, 5-6; Hilfskontakte: erste Ziffer Ordnungsziffer, zweite Funktionsziffer – **1-2 Öffner, 3-4 Schließer**, 5-6/7-8 Öffner/Schließer mit Sonderfunktion (z. B. verzögert) |
| Leiter und Motoranschlüsse | DIN EN 60445 🔎 | L1, L2, L3, N, PE; Motorwicklung U1-U2, V1-V2, W1-W2 |
| Schaltzeichen Fluidtechnik | DIN ISO 1219-1:2019-01 (ISO 1219-1:2012 + Amd 1:2016) | Wegeventil „5/2“ (Anschlüsse/Schaltstellungen), Betätigungsarten, Zylinder, Drossel |
| Fluidtechnische Schaltpläne | ISO 1219-2:2012 🔎 | eigene Kennzeichnung (z. B. 1V1) – nicht mit 81346 mischen (Abschn. 2) |
| Ventilanschlüsse pneumatisch | ISO 11727 🔎 | 1 Druckluft, 2 und 4 Arbeitsanschlüsse, 3 und 5 Entlüftung, 12 bzw. 14 Steueranschluss (verbindet 1 mit 2 bzw. 1 mit 4) |

Für Aufgaben: Vorlagen (Anschlussplan, Schaltplanausschnitt) als Anlage mit Schaltzeichen des
Unterrichts; die Musterlösung verwendet dieselben Zeichen und Anschlussbezeichnungen.

## 6. Sicherheit an Maschinen – Bedienteile, Farben, Stopp, Not-Halt

**Ausgaben:** DIN EN 60204-1 (VDE 0113-1):2019-06 (IEC 60204-1:2016; Änderung A1 🔎), DIN EN ISO
13850:2016 (Not-Halt), DIN EN 60073 (Farbbedeutung), DIN EN ISO 13849-1:2023 (sicherheitsbezogene
Steuerungsteile, Performance Level).

| Bedienteil | Farbe |
|---|---|
| Start/Ein | **weiß** (bevorzugt), grau, schwarz, grün – **nicht rot** |
| Stopp/Aus | **schwarz** (bevorzugt), grau, weiß; rot erlaubt, aber nicht nahe dem Not-Halt – **nicht grün** |
| abwechselnd Start/Stopp, Tippen | weiß, grau, schwarz – nicht rot, gelb, grün |
| Rücksetzen (Quittieren) | blau, weiß, grau, schwarz – nicht grün |
| Not-Halt | **rot auf gelbem Grund**, nur für Not-Halt |

| Leuchtmelder | Bedeutung |
|---|---|
| rot | Notfall, gefährlicher Zustand – sofort handeln |
| gelb | anormal, kritischer Zustand steht bevor |
| grün | normal, sicherer Betrieb |
| blau | zwingend – Bedienperson muss handeln |
| weiß | neutral, Bestätigung |

- **Stopp-Kategorien:** 0 = Energie sofort abschalten (ungesteuertes Stillsetzen); 1 = gesteuert
  stillsetzen, Energie danach abschalten; 2 = gesteuert stillsetzen, Energie bleibt. **Not-Halt nur
  Kategorie 0 oder 1.**
- **Stopp vor Start:** Ein Stoppbefehl hat Vorrang vor dem zugehörigen Start (rücksetzdominant
  speichern).
- **Not-Halt:** rastet ein; das Entriegeln darf die Maschine nicht wieder anlaufen lassen –
  Neustart nur mit eigenem Startbefehl.
- **Ruhestromprinzip:** Stopp-, Not-Halt- und Sicherheitsgeber als Öffner (drahtbruchsicher; Not-Halt
  mit Zwangsöffnung). Folge für Aufgaben: Kontaktart angeben und in Bedingungen beachten (Abschn. 3).
- **Grenze der Aufgabe:** Eine Standard-SPS ist keine Sicherheitssteuerung. Sicherheitsfunktionen
  (Not-Halt, Schutztür) ausdrücklich ausklammern („Der Not-Halt ist hardwaremäßig gelöst …“, T.7)
  oder als Beurteilungsaufgabe stellen (Risiko, Performance Level nach DIN EN ISO 13849-1 – nur wenn
  unterrichtet).

## 7. Sensorik, Einheitssignale, Regelungstechnik

**Einheitssignale** (IEC 60381 🔎): 4 … 20 mA, 0 … 20 mA, 0 … 10 V.
- 4 … 20 mA hat einen **lebenden Nullpunkt**: Ein Strom unter 4 mA zeigt Drahtbruch oder Ausfall.
  NAMUR-Empfehlung NE 43 (keine Norm): Messbereich 3,8 … 20,5 mA, Ausfall ≤ 3,6 mA oder ≥ 21 mA.
- **Lineare Umrechnung** (in der Aufgabe vorgeben oder als bekannt voraussetzen, wenn unterrichtet):
  x = x_min + (I − 4 mA) · (x_max − x_min) / 16 mA.
- **Digitalwert** der Analogbaugruppe angeben (Siemens 0 … 27 648 für 4 … 20 mA, −27 648 … +27 648 für
  ±10 V; Mikrocontroller je Board und Funktion, Abschn. 4) – sonst hat die Aufgabe mehrere richtige
  Ergebnisse (K.4).

**Pt100** – DIN EN IEC 60751 (IEC 60751:2022 🔎; vorher DIN EN 60751:2009):
- R₀ = 100 Ω bei 0 °C, R(100 °C) = 138,51 Ω, mittlerer Temperaturbeiwert α = 0,003 85 K⁻¹.
- Grenzabweichungen: Klasse AA ±(0,1 + 0,0017·|ϑ|) °C, A ±(0,15 + 0,002·|ϑ|) °C,
  B ±(0,3 + 0,005·|ϑ|) °C, C ±(0,6 + 0,01·|ϑ|) °C.
- Für Aufgaben die **lineare Näherung** R = R₀ · (1 + α · ϑ) ausdrücklich vorgeben (sonst Rechnung
  nach Callendar-Van Dusen) und die Toleranz im Erwartungshorizont nennen.

**Regelungstechnik** – DIN IEC 60050-351:2014-09 (ersetzt DIN 19226):

| Größe | Formelzeichen |
|---|---|
| Regelgröße | x |
| Führungsgröße (Sollwert) | w |
| Regeldifferenz | **e = w − x** |
| Stellgröße | y |
| Störgröße | z |
| Rückführgröße | r |

- Ältere Literatur rechnet mit der Regelabweichung x_w = x − w (umgekehrtes Vorzeichen); Lehrbücher
  der Systemtheorie nennen die Regelgröße y und die Stellgröße u. **Formelzeichen und Vorzeichen im
  Schülermaterial festlegen.**
- Wirkungsplan (Blockschaltbild): Blöcke mit Übertragungsverhalten, Vergleichsstelle als Kreis mit
  Vorzeichen.

## 8. Netzwerke

**Strukturierte Verkabelung** – DIN EN 50173-1 (VDE 0800-173-1):2018-10 (ISO/IEC 11801-1:2017); Teil 2
Bürogebäude, Teil 3 Industrie; Installation: DIN EN 50174.
- Bereiche: Primärbereich (Standort, zwischen Gebäuden) · Sekundärbereich (Gebäude, Steigbereich) ·
  Tertiärbereich (Etage, bis zur Anschlussdose); Verteiler: Standort-, Gebäude-, Etagenverteiler.
- Längen Kupfer im Tertiärbereich: Übertragungsstrecke (Channel) höchstens 100 m, davon fest
  verlegte Strecke (Permanent Link) höchstens 90 m 🔎.
- **Klasse** gilt für die Strecke, **Kategorie** für die Komponente: D / Kat. 5e (100 MHz), E / Kat. 6
  (250 MHz), E_A / Kat. 6_A (500 MHz), F / Kat. 7 (600 MHz), F_A / Kat. 7_A (1000 MHz), I und II /
  Kat. 8.1 und 8.2 (2000 MHz, höchstens 30 m).

**IEEE 802** – 802.3 Ethernet (z. B. 1000BASE-T, 10GBASE-T); PoE: 802.3af 15,4 W, 802.3at 30 W,
802.3bt 60 W bzw. 90 W (je Port an der Quelle); 802.1Q VLAN (VLAN-ID 1 … 4094, 4-Byte-Tag); 802.1X
portbasierte Authentifizierung; 802.11 WLAN.

**Adressen** (RFCs) – in fiktiven Szenarien nur diese Bereiche verwenden:

| Zweck | Bereich | RFC |
|---|---|---|
| private IPv4-Netze | 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 | 1918 |
| **„öffentliche“ Adressen in Beispielen** | 192.0.2.0/24, 198.51.100.0/24, 203.0.113.0/24 | 5737 |
| IPv6 in Beispielen | 2001:db8::/32, 3fff::/20 | 3849, 9637 |
| IPv6 privat (ULA) | fc00::/7, genutzt fd00::/8 | 4193 |
| Link-local | 169.254.0.0/16 bzw. fe80::/10 | 3927, 4291 |
| Provider-NAT | 100.64.0.0/10 | 6598 |
| Loopback | 127.0.0.0/8 bzw. ::1 | 1122, 4291 |

- **IPv6-Schreibweise** (RFC 5952): Kleinbuchstaben, führende Nullen je Block weglassen, die längste
  Folge von mindestens zwei Null-Blöcken durch „::“ ersetzen (bei Gleichstand die erste), nie für
  einen einzelnen Block. Musterlösung in dieser Form; andere gültige Kurzformen als *Gleichwertig*.
- **IPv4:** Präfix in CIDR-Schreibweise und Subnetzmaske angeben; Netz- und Broadcastadresse sind keine
  Hostadressen – in der Aufgabe sagen, ob das Gateway die erste oder die letzte nutzbare Adresse ist.

## 9. Software – UML, Struktogramm, Programmablaufplan

- **UML** – OMG UML 2.5.1 (ISO/IEC 19505-2:2012 entspricht UML 2.4.1). Klassendiagramm: Sichtbarkeit
  + public, − private, # protected, ~ package; Attribut „name : Typ“, Operation
  „name(p : Typ) : Rückgabetyp“; statisch unterstrichen, abstrakt kursiv; Assoziation mit
  Multiplizität (1, 0..1, *, 1..*), Aggregation (leere Raute), Komposition (gefüllte Raute),
  Generalisierung (geschlossene leere Pfeilspitze). Zustandsdiagramm: Transition
  „Ereignis [Wächter] / Effekt“.
- **Struktogramm** – DIN 66261:1985 (Nassi-Shneiderman); **Programmablaufplan** – DIN 66001:1983.
- **SQL** – ISO/IEC 9075; den Dialekt des Unterrichts (z. B. SQLite, MySQL) nennen.
- Pseudocode ist nicht genormt: zulässige Sprachelemente als Anlage oder Hilfsmitteldokument.

**Notationsrahmen Informatik in Niedersachsen** – Ergänzende Hinweise zum Kerncurriculum Informatik
(Neufassung Juni 2025, verbindlich für das Zentralabitur ab 2027; ein Teil ist dort als Hilfsmittel
zugelassen). Für das Fach Technik nicht verbindlich, aber das Vorbild, an dem sich Lernende und
Zweitkorrektur orientieren – für Software- und Datenbankteile übernehmen oder Abweichungen in der
Anlage festlegen:
- **Signaturen** wie im Klassendiagramm: `bezeichnung(parameter: Typ, …): Rückgabetyp`, Typnamen
  deutsch (Ganzzahl, Fließkommazahl, Zeichenkette, Wahrheitswert, „dynamische Reihung vom
  Inhaltstyp …“).
- Sprachunabhängig: **Index ab 0** (Zeichenketten, Reihungen), `/` bei zwei Ganzzahlen ganzzahlig,
  `mod` als kleinster positiver Rest, zweidimensionale Reihung `[Zeile][Spalte]`. Bei
  Implementierungen gilt die Syntax der Unterrichtssprache.
- **Zulässige Operationen** werden aufgezählt (Zeichenketten: Länge, Zeichen an Position,
  Teilzeichenkette, Verbinden, Vergleich …; Datenstrukturen mit festen Methodennamen); darüber
  hinausgehende Operationen sind nicht zulässig. Laufzeitfehler (leerer Stapel, ungültiger Index)
  muss die Lösung ausdrücklich abfangen.
- **Struktogramm:** Formulierungen sprachunabhängig, sprachlich („erhöhe anzahl um 1“) oder formal
  („anzahl ← anzahl + 1“); Kommentar mit `//`; „gib … zurück“ beendet die Operation; „erzeuge …“
  ruft den Konstruktor auf.
- **Klassendiagramm:** Sichtbarkeit `+`/`-` im Normalfall Pflicht, Konstruktor mit vorangestelltem
  `c`, nicht aufgeführte Attribute bzw. Operationen als „…“, Assoziationen als einfache Linien;
  Objektkarte `name : Klasse` mit Attributbelegung.
- **Datenbank:** Kurzschreibweise `Tabelle(Schlüssel, Attribut, ↑Fremdschlüssel)` mit
  unterstrichenem Primärschlüssel; ER-Diagramm mit Kardinalitäten (1, n, m) und Schlüsselattributen;
  **SQL-Umfang** SELECT [DISTINCT] … FROM … WHERE … GROUP BY … HAVING … ORDER BY … LIMIT,
  Verknüpfung über FROM und WHERE (kein JOIN-Schlüsselwort), Vergleiche einschließlich LIKE mit `_`
  und `%`, Aggregatfunktionen AVG, COUNT, MAX, MIN, SUM; keine verschachtelten Abfragen.
- **Automaten und Grammatiken:** Eingabealphabet Σ, Zustandsgraph; Mealy-Übergang
  „Eingabe/Ausgabe“, leere Ausgabe ε; Kellerautomat „(oberstes Kellerzeichen, Eingabe) :
  abgelegte Zeichen“ mit Vorbelegung #; Grammatik mit N, T, Startsymbol und Regeln, regulär
  rechtsregulär notiert.
- **Codierung:** Lauflängencodierung „Anzahl-Wert“; Kompressionsverhältnis = komprimiert /
  original; (7,4)-Hamming-Code in der Reihenfolge p0 p1 d0 p2 d1 d2 d3 mit gerader Parität.
- Die Vorgaben wechseln mit dem Jahrgang (2026 andere Baum-Operationen als ab 2027) – vor jedem
  Prüfungsjahr mit den aktuellen fachbezogenen Hinweisen abgleichen 🔎.
- Bezeichner aus Klassendiagramm und Code in Schüler- und Lehrermaterial gleich schreiben (K.9).

## 10. Größen, Einheiten, Schreibweise

DIN EN ISO 80000-1 (ISO 80000-1:2022 🔎), DIN 1313 (Größen), DIN 1338 (Formelsatz):
- Zahl und Einheit mit Leerzeichen: „24 V“, „45 %“, „20 °C“; ohne Leerzeichen nur der ebene Winkel
  „90°“. Dezimalkomma. Bereiche „4 mA … 20 mA“ oder „(4 … 20) mA“.
- Formelzeichen kursiv, Einheiten aufrecht. „[U] = V“ heißt „Einheit von U“ – Spaltenköpfe daher
  „U in V“ oder „U / V“, nicht „U [V]“.
- **Datenmengen** – IEC 80000-13 🔎: Bit „bit“, Byte „B“; Dezimalvorsätze k = 10³, M = 10⁶;
  Binärvorsätze Ki = 2¹⁰, Mi = 2²⁰; Datenraten in bit/s (Mbit/s). In der Aufgabe festlegen, ob mit
  1 kB = 1000 B oder 1 KiB = 1024 B gerechnet wird – sonst zwei richtige Ergebnisse (K.4).

## 11. Quellen

Recherche 2026-10-30; Normtexte nicht eingesehen, außer der Leseprobe der IEC 81346-2:2019.
- IEC 81346-2:2019, Leseprobe (Abschnitte 4–5, Tabellen 1 und 2 Klasse B und C):
  https://cdn.standards.iteh.ai/samples/21908/1b996d119d0945b2b28359332ffa9b3f/IEC-81346-2-2019.pdf
- PAL/IHK Stuttgart: „DIN EN IEC 81346-2:2020-10 – Anwendung der aktuellen Referenzkennzeichnungen in
  PAL-Prüfungen“, Stand Juni 2024 (SF → SJ, RZ → RN, Beispielschaltpläne):
  https://www.ihk.de/blueprint/servlet/resource/blob/5090560/d005ab9b73c3e45d81920e28f72b7160/din-en-iec-81346-2-2020-10-referenzkennzeichnung-data.pdf
- PAL: „ISO 1219-2 (2012-09) und DIN EN 81346-2 (2009-10)“, Stand April 2016 (Ausgabe 2009: SF, SJ, RN, RZ):
  https://grafcet-schulungen.de/wp-content/uploads/2017/02/Referenzkennzeichnung_DIN_ISO_1219_81346_PAL_Stand_Dez_2016.pdf
- Wikipedia „IEC 81346“ und „EN IEC 81346“ (Unterklassen und dritte Ebene der Ausgabe 2019; Teil 1
  2022 mit Typaspekt „%“): https://en.wikipedia.org/wiki/IEC_81346, https://de.wikipedia.org/wiki/EN_IEC_81346
- DKE: DIN EN 60848:2014-12 (aktuell): https://www.dke.de/de/normen-standards/dokument?id=7049716&type=dke%7Cdokument
- Wikipedia „GRAFCET“; Europa-Lehrmittel, Leseprobe „GRAFCET“ (Transitionen, Zeiten, speichernde Aktionen):
  https://de.wikipedia.org/wiki/GRAFCET, https://www.europa-lehrmittel.de/leseprobe/37633-4.pdf
- IEC 61131-3:2025, Änderungen gegenüber 2013 (IL gestrichen): https://stefanhenneken.net/2025/06/11/iec-61131-3-comparison-of-edition-3-and-edition-4/
- IFAN: Vergleich DIN EN 60204-1 (VDE 0113-1):2019-06 (Farben, Stopp-Kategorien):
  https://ifan-normung.de/wp-content/uploads/2019/07/Vergleich_EN-60204-1-wa14.pdf
- DKE/Wikipedia zu DIN EN 50173-1:2018-10: https://de.wikipedia.org/wiki/EN_50173
- DIN Media zu DIN IEC 60050-351:2014-09: https://www.dinmedia.de/en/standard/din-iec-60050-351/116876648
- DIN ISO 1219-1:2019-01: https://webstore.ansi.org/standards/din/diniso12192019de
- RFC 1918, 3849, 3927, 4193, 4291, 5737, 5952, 6598, 9637 (rfc-editor.org).
- Niedersächsisches Kultusministerium: Ergänzende Hinweise zum Kerncurriculum Informatik, Neufassung
  Juni 2025 (lokal unter `Klausuren/Beispielklausuren/Abiturprüfungen/Normen Hinweise Notationen/`).
- Zentrale Abiturprüfungen Mechatronik Niedersachsen 2020–2026 (nur gelesen, Kennbuchstaben
  ausgezählt): Ausgabe 2009 (-SF, -RZ, -AZ).

## Anhang: references/notation-steuerungstechnik.md

# Notationsblatt Steuerungstechnik

Einheitliche Schreibweise der Bibliothek für Kennzeichen, Signale, Zuordnungsliste, GRAFCET und
Programme – für Prüfungsaufgaben, Erwartungshorizonte und Unterricht. Grundlage: DIN EN IEC 81346-2:2020,
DIN EN 60848:2014, IEC 61131-3:2025; Hintergrund und Quellen in `normen-technik.md` (Abschn. 2–4).
Stand 03.11.2026.

## Für die Lehrkraft

- **Teil „Anlage“ unten** dem Schülermaterial beifügen („## Anlage N – Notation Steuerungstechnik“,
  das Wort *Notation* in der Überschrift behalten), Abschnitte streichen, die die Aufgabe nicht braucht.
  `bmk_pruefen.py` überspringt diese Anlage bis zur nächsten Überschrift gleicher Ebene; ihre
  Beispiel-Kennzeichen zählen nicht zur Aufgabe. Keine Unterüberschriften in der Anlage. So arbeiten Prüfling, Erst- und Zweitkorrektur
  mit derselben Schreibweise.
- **Abweichungen des Unterrichts** (andere Ausgabe der Kennzeichnung, andere Zeitschreibweise) in der
  Anlage ändern und im Begleitblatt begründen – nie innerhalb eines Vorschlags mischen.
- **Plattformneutral stellen:** Steuerungsaufgaben müssen mit SPS, Kleinsteuerung **oder**
  Mikrocontroller lösbar sein, wenn die Schule mehrere Plattformen nutzt. Dafür:
  1. Funktion als GRAFCET bzw. Logikplan spezifizieren – beides ist plattformunabhängig.
  2. Analogwerte im GRAFCET als physikalische Größe mit Einheit; Rohwerte nur in plattformgebundenen
     Teilaufgaben und immer mit dem Bereich für 4 mA bzw. 20 mA in der Anlage (Bereiche je Plattform:
     `normen-technik.md`, Abschn. 4; für die Prüflinge stehen sie in der Anlage unten).
  3. Zuordnungsliste mit je einer Spalte je Plattform; die Prüflinge füllen die Spalte ihrer
     Plattform. Die verfügbaren Ein- und Ausgänge je Plattform stehen in einer Anlage.
  4. Programmieraufträge „in der im Unterricht verwendeten Sprache“; im Lehrermaterial *Gleichwertig*
     für jede Plattform.
- **Prüfen:** `bmk_pruefen.py` – T.6 Schreibweise, T.8 Kennbuchstaben, T.9 GRAFCET-Textform.

---

## Anlage – Notation Steuerungstechnik

**1. Kennzeichen der Betriebsmittel**

- Bindestrich, Kennbuchstabe(n), Zählnummer, ohne Leerzeichen: **-S1**, **-B2**, **-Q1**
  (DIN EN IEC 81346-2:2020).
- In der Regel nur der Klassenbuchstabe. Zwei Buchstaben stehen nur, wenn eine Klasse verschiedene
  Arten enthält – dann für alle Betriebsmittel dieser Klasse (z. B. -BL1 Füllstand, -BT1 Temperatur).

| Kennbuchstabe | Betriebsmittel (Beispiele) |
|---|---|
| -S | Taster, Schalter, handbetätigtes Ventil |
| -B | Sensor, Geber (Näherungs-, End-, Druck-, Schwimmerschalter, Temperaturfühler) |
| -K | Steuerung (SPS, Kleinsteuerung, Mikrocontroller), Relais, Zeitrelais |
| -Q | Schütz, Leistungsschalter, Wegeventil |
| -M | Motor, Ventilspule, Zylinder |
| -P | Leuchtmelder, Hupe, Anzeige |
| -R | Drossel- und Rückschlagventil, Widerstand |
| -G | Pumpe, Kompressor, Lüfter, Generator |
| -T | Netzteil, Umrichter, Messumformer |

**2. Signale**

- Im Text, im GRAFCET und im Logikplan steht das Kennzeichen für **sein Signal an der Steuerung**: -B1
  ist 1 oder 0. Was 1 bedeutet, steht in der Zuordnungsliste (Spalte „Signal 1 bedeutet“).
- **Kontaktart:** NO = Schließer, NC = Öffner. Ein Öffner liefert im unbetätigten Zustand 1.
- **Analogwerte** stehen in Bedingungen als physikalischer Wert mit Einheit: [-BT1 > −16 °C],
  [-BL1 ≥ 80 %]. Die Umrechnung aus dem Rohwert ist Teil des Programms.
- **Interne Variablen** (Merker, Zähler) tragen einen sprechenden Namen ohne Bindestrich in
  Code-Schrift: `M_Pumpe`, `C_Teile`.

**3. Zuordnungsliste**

| BMK | Betriebsmittel | Operand SPS | Operand Kleinsteuerung | Pin Mikrocontroller | Signal 1 bedeutet | Kontaktart |
|---|---|---|---|---|---|---|
| -S1 | Taster Start | %I0.0 | I1 | D2 | Start betätigt | NO |
| -S2 | Taster Stopp | %I0.1 | I2 | D3 | Stopp nicht betätigt | NC |

- Ausgefüllt wird nur die Spalte der Plattform aus dem Unterricht; die anderen Spalten bleiben
  leer.
- Jeder Operand bzw. Pin wird genau einmal belegt. Analoggeber mit Messbereich und Signal
  („4 … 20 mA für 10 … 60 %“).
- Operanden wie in der Programmiersoftware: Siemens-SPS %I0.0, %IW64; WAGO %IX4.0, %IW0; LOGO! I1, AI1;
  Eaton easyE4 I1, IA1. Pins wie auf dem Board bezeichnet: D2 (Arduino), GPIO16 (ESP32), PB12 (STM32),
  GP2 (Raspberry Pi Pico).

**4. GRAFCET (DIN EN 60848)**

- **Schritt:** Quadrat mit Nummer; **Initialschritt doppelt umrandet** (Nummer 0). Schrittvariable
  X3 = 1, solange Schritt 3 aktiv ist.
- **Transition:** Querstrich, Bedingung rechts daneben, Name wenn nötig links in Klammern: (T2).
  Schritt und Transition wechseln sich ab; Verbindungen nach oben (Rücksprung) mit Pfeil.
- **Verzweigungen:** Alternativ mit einfacher Linie und einer Transition je Ast (die Bedingungen schließen
  sich gegenseitig aus); parallel mit Doppellinie unter der gemeinsamen Transition, zusammengeführt mit
  Doppellinie über der gemeinsamen Transition.
- **Bedingungen:**

  | Bedeutung | Schreibweise |
  |---|---|
  | UND | -S1 · -B1 |
  | ODER | -B2 + -B3 |
  | NICHT | Überstrich über dem Kennzeichen; getippt **¬-S2** |
  | steigende bzw. fallende Flanke | ↑-B1, ↓-B1 |
  | Zeit seit Aktivierung von Schritt 3 | **5s/X3** |
  | Vergleich eines Zahlenwerts | **[-BT1 > −16 °C]**, [C_Teile = 10] |
  | immer erfüllt | 1 (unterstrichen) |

- **Aktionen** im Rechteck rechts am Schritt. Mehrere Aktionen stehen nebeneinander oder lückenlos untereinander:

  | Art | im Rechteck | am Rechteck | Wirkung |
  |---|---|---|---|
  | kontinuierlich | -M1 | – | 1, solange der Schritt aktiv ist |
  | mit Zuweisungsbedingung | -M1 | Strich oben, daran die Bedingung | 1, solange Schritt aktiv und Bedingung erfüllt |
  | verzögert | -M1 | Strich oben, daran 5s/X3 | 1 ab 5 s nach Aktivierung, solange der Schritt aktiv ist |
  | zeitbegrenzt | -M1 | Strich oben, daran 5s/X3 mit Überstrich | 1 in den ersten 5 s nach Aktivierung |
  | speichernd bei Aktivierung | -Q1 := 1 | Pfeil nach oben an der linken Kante | Wert bleibt bis zur nächsten Zuweisung |
  | speichernd bei Deaktivierung | -Q1 := 0 | Pfeil nach unten an der linken Kante | Wert bleibt bis zur nächsten Zuweisung |
  | speichernd bei Ereignis | -Q1 := 1 | Strich oben mit Fähnchen nach links, daran ↑-B1 | Zuweisung beim Ereignis, solange der Schritt aktiv ist |
  | Zähler | C_Teile := C_Teile + 1 | Pfeil nach oben an der linken Kante | zählt bei jeder Aktivierung |
  | Zwangssteuerung | G5 {INIT} im Doppelrahmen | – | setzt Teil-GRAFCET G5: {INIT} Anfangssituation, { } leer, {3,4,8} diese Schritte, {*} eingefroren |

- **Speichernd wirkende Aktionen** tragen immer beides: die **Zuweisung** mit := im Rechteck und den
  **Auslöser** am Rechteck. „-Q1“ allein ist kontinuierlich. Dieselbe Variable wirkt nie zugleich
  kontinuierlich und speichernd; was mit := 1 gesetzt wird, wird auch mit := 0 zurückgesetzt.
- **Strukturierung**, wenn im Unterricht eingeführt: Makroschritt (Querlinien oben und unten im Quadrat, M4),
  einschließender Schritt (abgeschrägte Ecken) mit Rahmen um die eingeschlossene Kette, oben der Name
  des einschließenden Schritts; der zuerst aktive Schritt darin trägt links ein *. Quelltransition ohne
  Verbindung nach oben, Schlusstransition ohne Verbindung nach unten.
- **Kommentare** in Anführungszeichen: „Zylinder fährt aus“.

**5. GRAFCET in Textform**

Wird ein GRAFCET getippt statt gezeichnet (Erwartungshorizont, PC-Aufgabe), gilt diese Tabelle:

| Schritt | Aktion | Transition zum Folgeschritt |
|---|---|---|
| 0 (Initialschritt) | – | -S1 · -B1 → 1 |
| 1 Füllen | -M1 | [-BL1 ≥ 80 %] + 30s/X1 → 2 |
| 2 Prüfen | ↑ C_Teile := C_Teile + 1 | [C_Teile < 10] → 1; [C_Teile = 10] → 3 |
| 3 Fertig | -P1 | ¬-S2 → 0 |

- Folgeschritt nach **→**; Alternativen durch **;** getrennt (sie schließen sich gegenseitig aus).
- Mehrere Aktionen durch **;** getrennt. Speichernd **↑ -Q1 := 1**, **↓ -Q1 := 0**, bei Ereignis
  **-Q1 := 1 bei ↑-B1**; mit Bedingung **-M1 wenn -B1**, verzögert **-M1 verzögert 5s/X3**, zeitbegrenzt
  **-M1 begrenzt 5s/X3**.
- Parallelverzweigung „→ 3 und 6 (parallel)“; die gemeinsame Transition danach steht bei beiden
  letzten Schritten mit dem Zusatz „(gemeinsam mit X8)“.

**6. Logikplan und Programm**

- **Logikplan (FUP):** Verknüpfungsglieder & (UND), ≥1 (ODER), =1 (XOR), Negation als Kreis am
  Eingang oder Ausgang; Eingänge und Ausgänge mit Kennzeichen beschriftet.
- **Programm** in der im Unterricht verwendeten Sprache:
  - SPS und Kleinsteuerung nach IEC 61131-3: KOP, FUP, ST oder AS (keine AWL). Zeiten mit TON, TOF,
    TP; Zähler mit CTU, CTD; SR setzdominant, RS rücksetzdominant.
  - Mikrocontroller in C/C++ oder Python: Pin-Konstante `PIN_S1`, Signalvariable `s1` (Kennzeichen
    klein, ohne Bindestrich). Zeiten über die Zeit seit Schrittbeginn (z. B. `millis()`), nicht mit
    Warteschleifen; einen GRAFCET als Zustandsautomat mit einer Variablen für den aktiven Schritt.
- **Mikrocontroller-Eingänge:** Signal 1 ist der High-Pegel am Pin. Bei internem Pull-up-Widerstand
  liefert ein betätigter Schließer 0 – die Zuordnungsliste sagt, was 1 bedeutet.
- **Analogwerte:** Der Wertebereich im Programm steht in der Anlage der Ein- und Ausgänge; er hängt
  von Steuerung, Board und Funktion ab (z. B. 4 … 20 mA: Siemens 0 … 27 648, WAGO 0 … 32 760, LOGO!
  200 … 1000, Eaton easyE4 819 … 4095; Arduino Uno 0 … 1023, 12 bit 0 … 4095, MicroPython 0 … 65 535).

## Anhang: references/schaltzeichen.md

# Schaltzeichen (DIN EN 60617) – Katalog des Werkzeugs

Aus `python3 scripts/edu.py technologieschema symbole --md` erzeugt; nicht von Hand ändern. Einsatz:
`typ: symbol`, `symbol: <Name>` (Abschn. 3c der Spec-Referenz). Katalogbogen zum Ansehen:
`python3 scripts/edu.py technologieschema symbole --svg schema/schaltzeichen.svg`.

- **Klasse** – zulässige Kennbuchstaben des Referenzkennzeichens (DIN EN IEC 81346-2:2020); ein anderes
  Kennzeichen ist ❌. Schließer: Taster -S, Sensor -B, Relaiskontakt -K, Schützkontakt -Q.
- **Anschlüsse** – `an1`, `an2` … für Anker (`"-S1@an1"`); sie folgen Drehung und Spiegelung.
- **Wirkv.** – „ja“: das Zeichen hat eine Wirkverbindung (Klingenmitte); nur dort wirkt `betaetigung:`
  (Betätigungsarten, Tabelle am Ende).
- **Herkunft** – *Liste*: Form mit einer Vorlage abgeglichen (Wikipedia-Liste der Schaltzeichen
  (Elektrik/Elektronik); Näherungsschalter und Betätigungsarten: Galerien mit Zeichennummern der EN-60617-Reihe);
  *zusammengesetzt*: aus solchen Zeichen gebildet (Taster = Kontakt mit Rückgang + Betätigung);
  *🔎 abgleichen*: nach Lehrbuch-Formensprache gezeichnet, vor dem Einsatz mit Norm oder eingeführtem
  Tabellenbuch vergleichen und im Schemablatt vermerken. Alle Vorlagen sind Sekundärquellen; maßgeblich ist die Norm.
- Die Zeichen sind eigene Zeichnungen (keine Kopien der Wikipedia-Dateien).

### Kontakte

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `schliesser` | Schließer | SBKQF | an1, an2 | ja | Liste | allgemeiner Schalter; schließt, wenn betätigt |
| `oeffner` | Öffner | SBKQF | an1, an2 | ja | Liste | öffnet, wenn betätigt |
| `schliesser_schuetz` | Schließer eines Schützes | QK | an1, an2 | ja | Liste | Halbkreis: Schaltgerät mit Schaltvermögen (Leistungskontakt) |
| `oeffner_schuetz` | Öffner eines Schützes | QK | an1, an2 | ja | Liste |  |
| `positionsschalter_schliesser` | Positionsschalter, Schließer | BS | an1, an2 |  | Liste | in der Wikipedia-Liste „Grenzschalter“; Dreieck an der Klinge: Betätigung durch die Position |
| `positionsschalter_oeffner` | Positionsschalter, Öffner | BS | an1, an2 |  | Liste |  |
| `wechsler` | Wechsler (mit Unterbrechung) | SBKQ | an1, an2, an3 | ja | Liste | an3 = Mittelanschluss; an1 Öffnerseite, an2 Schließerseite |
| `wechsler_ohne_unterbrechung` | Wechsler (ohne Unterbrechung) | SBKQ | an1, an2, an3 | ja | Liste | Querstrich an der Klinge: Überlappung, kein Unterbrechen beim Umschalten |

### Schaltgeräte

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `leistungsschalter` | Leistungsschalter | Q | an1, an2 | ja | Liste | Kreuz am Anschluss: selbsttätige Auslösung möglich (Schaltgerät) |
| `trennschalter` | Trennschalter | Q | an1, an2 | ja | Liste |  |
| `lasttrennschalter` | Lasttrennschalter | Q | an1, an2 | ja | Liste | Kreis: Schaltvermögen (Last schalten) |

### Kontakte

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `schliesser_rueckgang` | Schließer mit selbsttätigem Rückgang | SBK | an1, an2 | ja | Liste | Dreieck: Rückgang in die Ruhelage nach Loslassen (Feder), die Grundform des Tasters |
| `oeffner_rueckgang` | Öffner mit selbsttätigem Rückgang | SBK | an1, an2 | ja | Liste | das Dreieck ersetzt den Fuß des Öffners |

### Antriebe

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `spule` | Spule (Relais, Schütz, Magnetventil) | QKM | an1, an2 |  | Liste | elektromechanischer Antrieb; Relais -K, Schütz -Q, Ventilspule -MB (Zeichen 07-15-01) |
| `thermorelais` | Thermisches Überlastrelais (Bimetall) | F | an1, an2 |  | Liste | Bügel im Rechteck: Bimetall; Auslösung des Motorschutzes |

### Bauelemente

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `widerstand` | Widerstand | R | an1, an2 |  | 🔎 abgleichen |  (Zeichen 04-01-01) |
| `kondensator` | Kondensator | C | an1, an2 |  | 🔎 abgleichen |  (Zeichen 04-02-01) |
| `induktivitaet` | Induktivität (Spule, Drossel) | R | an1, an2 |  | 🔎 abgleichen | vier Halbkreise (Wicklung) |
| `diode` | Diode | R | an1, an2 |  | Liste | an1 Anode, an2 Kathode (Zeichen 05-03-01) |
| `led` | Leuchtdiode (LED) | RPE | an1, an2 |  | Liste | an1 Anode, an2 Kathode (Zeichen 05-03-02) |
| `sicherung` | Sicherung | F | an1, an2 |  | 🔎 abgleichen | Rechteck mit durchgehender Linie |

### Melden

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `meldeleuchte` | Meldeleuchte | PE | an1, an2 |  | 🔎 abgleichen | Kreis mit Kreuz |

### Antriebe

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `motor_drehstrom` | Drehstrommotor | M | an1, an2, an3 |  | 🔎 abgleichen | Kreis mit M und Stromart; an1 bis an3 = U1, V1, W1 |
| `motor_wechselstrom` | Wechselstrommotor | M | an1, an2 |  | 🔎 abgleichen |  |
| `motor_gleichstrom` | Gleichstrommotor | M | an1, an2 |  | 🔎 abgleichen |  |

### Erdung

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `masse` | Masse, Gehäuse | X | an1 |  | Liste | IEC 60417-5020 (Zeichen 02-15-04) |

### Taster

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `taster_schliesser` | Taster, Schließer (handbetätigt) | S | an1, an2 |  | zusammengesetzt | Schließer mit Rückgang plus Handbetätigung |
| `taster_oeffner` | Taster, Öffner (handbetätigt) | S | an1, an2 |  | zusammengesetzt |  |
| `drucktaster_schliesser` | Drucktaster, Schließer | S | an1, an2 |  | zusammengesetzt | Betätigung durch Drücken |
| `drucktaster_oeffner` | Drucktaster, Öffner | S | an1, an2 |  | zusammengesetzt |  |
| `notaus_taster` | Not-Halt-Taster (Pilz, Öffner) | S | an1, an2 |  | zusammengesetzt | Pilz-Betätigung; die Rastung (Verriegelung) zeigt die Quelle nicht – bei Bedarf im Text nennen |

### Näherungsschalter

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `naeherungsschalter_schliesser` | Näherungsschalter, Schließer | B | an1, an2 |  | Liste | Rhombus: Näherung; die Wirkverbindung ist kurz (Zeichen 07-20-02) |
| `naeherungsschalter_oeffner` | Näherungsschalter, Öffner | B | an1, an2 |  | zusammengesetzt | Öffner-Gegenstück zu 07-20-02 |
| `naeherungsschalter_eisen_oeffner` | Näherungsschalter, Öffner, Betätigung durch Eisen | B | an1, an2 |  | Liste |  (Zeichen 07-20-04) |
| `naeherungsschalter_magnet_schliesser` | Näherungsschalter, Schließer, Betätigung durch Magnet | B | an1, an2 |  | Liste | z. B. Reedkontakt, Zylinderschalter (Zeichen 07-20-03) |
| `naeherungssensor` | Näherungssensor | B | an1, an2 |  | Liste | allgemein; Rhombus mit zwei Linien (Zeichen 07-19-01) |
| `beruehrungssensor` | Berührungssensor | B | an1, an2 |  | Liste |  (Zeichen 07-19-04) |
| `naeherungseinrichtung_block` | Näherungsempfindliche Einrichtung (Blocksymbol) | B | an1, an2 |  | Liste | Quadrat mit Rhombus; Anschlüsse links und rechts (Zeichen 07-19-02) |

### Betätigungsarten

Zusatz `betaetigung: <Name>` bei Zeichen mit Wirkverbindung (Spalte *Wirkv.*); `wirklaenge` (Standard 2) setzt die Länge der gestrichelten Linie.

| Name | Betätigungsart | Quelle | Hinweis |
|---|---|---|---|
| `hand` | Handbetätigung, allgemein | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `kippen` | Betätigung durch Kippen | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `drucken` | Betätigung durch Drücken (Drucktaster) | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `ziehen` | Betätigung durch Ziehen | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `drehen` | Betätigung durch Drehen | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `not_aus` | Betätigung durch Drücken, Not-Aus (Pilz) | elektricks.com, Betätigungsarten nach DIN EN 60617-7 | Pilzkopf; die Rastung (Verriegelung) zeigt die Quelle nicht |
| `thermisch` | Betätigung durch thermischen Effekt | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `annaehern` | Betätigung durch Annähern | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `beruehren` | Betätigung durch Berühren | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `annaehern_eisen` | Betätigung durch Annähern von Eisen | gallery.proficad.com, Zeichen 07-20-04 der EN-60617-Reihe |  |
| `annaehern_magnet` | Betätigung durch Annähern eines Magneten | gallery.proficad.com, Zeichen 07-20-03 der EN-60617-Reihe |  |
| `handrad` | Betätigung durch Handrad | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `fuss` | Betätigung durch Fuß | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `schluessel` | Betätigung durch Schlüssel | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `nocken` | Betätigung durch Nockensteuerung | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `pegel` | Betätigung durch Flüssigkeitspegel | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `motor` | Antrieb durch Elektromotor | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `elektromagnet` | Elektromagnetischer Antrieb | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.
Klausur- und Abiturformat haben eigene Richtwerte (`klausur-erstellen`, `abiturvorschlag-erstellen`);
die vier Regeln gelten dort sinngemäß.

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
Ausgenommen von den Richtwerten sind Klausur- und Abiturformat mit eigenen Regeln
(`klausur-erstellen`, `abiturvorschlag-erstellen`: Operator-Aufträge bis rund 40 bzw. 45 Wörter,
Antwortraum je Operator); kurz, eindeutig und ohne Dekoration bleiben auch sie.

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
| Simulationsschaltung | `circuitjs-schaltung-erstellen` |

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
| 47 | Simulationsschaltung (circuit.js: Schaltungstext, Messgeräte mit Erwartungswerten, Begleitblatt) | circuitjs-schaltung-erstellen |
| 48 | Mikrocontroller-Simulation (Wokwi: Spec, Projektordner mit Sketch, Schaltung und Szenarien, Zeitablauf, Begleitblatt) | wokwi-simulation-erstellen |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 70 | Klassenarbeit / Lernzielkontrolle mit Erwartungshorizont | klausur-erstellen |
| 75 | Abiturvorschlag (dezentral): Schüler- und Lehrermaterial je Vorschlag, Bewertungsbogen, Begleitblatt | abiturvorschlag-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

`abiturvorschlag-erstellen` (Nr. 75) hält Schüler- und Lehrermaterial einreichungsfertig: Kopf und
Pflichtabschnitte stehen im **Begleitblatt** (`75_abitur_<kurztitel>_begleitblatt.md`), nicht in den
Einreichungsunterlagen.

**Werkzeug-Skills** (Nr. 42, 46, 47, 48, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-technologieschema`, `schaltung.py`, `wokwi.py`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
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

## Anhang: references/technologieschema-specs.md

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
