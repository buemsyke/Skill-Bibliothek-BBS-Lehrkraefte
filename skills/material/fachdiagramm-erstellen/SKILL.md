---
name: fachdiagramm-erstellen
description: Erstellt Fachdiagramme für Unterrichtsmaterial und Klausuren aus einer kurzen YAML-Beschreibung – Blockschaltbild, Anlagen- und Systemübersicht, Energie- und Datenfluss, Regelkreis, Arbeits- und Prozessablauf, Struktogramm nach Nassi-Shneiderman, ER-Modell nach Chen, UML-Klassendiagramm und Relationenschema, auch als Klausurabbildung (Lückenbild, Fremdlösung mit Fehler, Lösungsbild). Das mitgelieferte Werkzeug edu-diagramm erzeugt daraus SVG und in diagrams.net bearbeitbare drawio-Dateien; ein Prüfskript findet vorher stille Fehler, dazu PNG-Vorschau und ein Diagrammblatt mit Alternativtext. Verwenden bei „Diagramm erstellen", „Blockschaltbild", „Ablaufdiagramm", „Struktogramm", „ER-Diagramm", „UML", „Regelkreis zeichnen", „Tafelbild als Grafik", „ASCII-Skizze ersetzen". Nicht für Technologieschema (Anlagenbild), GRAFCET, Funktionsplan, Netzwerkplan, genormte Stromlauf-, Pneumatik- oder Hydraulikpläne und technische Zeichnungen.
metadata:
  version: "1.6"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  eduwerkzeuge: "diagramme"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

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
