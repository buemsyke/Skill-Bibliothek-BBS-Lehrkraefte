---
name: schuelerseiten-veroeffentlichen
description: Erzeugt aus Unterrichtsmaterial mit Lehrerteil eine Schülerausgabe und bereitet die Veröffentlichung vor – im Kursprojekt (lessons/NN/lesson.md) als MkDocs-Schülerseiten je LMS-Phase mit dem mitgelieferten Werkzeug edu-seiten split, bei Einzeldokumenten der Bibliothek als Schülerfassung ohne Lösungen und didaktische Hinweise mit edu-seiten strip. Prüft per Skript, dass keine Lösungen, Erwartungshorizonte, Lösungsdiagramme, vertraulichen Dateien, offenen Prüfaufträge oder Kontaktdaten in die Ausgabe gelangen, dass jede Seite gekennzeichnet ist und kein Abschnitt still wegfällt; baut die Site und führt ein Veröffentlichungsprotokoll mit Freigabe durch die Lehrkraft. Veröffentlicht wird erst nach Freigabe und ausdrücklichem Auftrag. Verwenden bei „Schülerseiten erzeugen", „Schülerfassung ohne Lösungen", „Lehrerteil entfernen", „Kurs als Website veröffentlichen", „GitHub Pages", „Phasen fürs LMS freischalten".
metadata:
  version: "1.7"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  eduwerkzeuge: "seiten"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Schülerseiten veröffentlichen

## Zweck
Lernende bekommen **genau das Material, das für sie bestimmt ist** – ohne Lösungen,
Erwartungshorizonte, didaktische Hinweise und Planungsnotizen – in einer Form, die sich
phasenweise freischalten, drucken oder als Website veröffentlichen lässt. Die Zerlegung
übernimmt das getestete Werkzeug `edu-seiten`; der Skill sichert ab, dass nichts
Falsches nach außen geht.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Veröffentlichungsprotokoll). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Modi

| Modus | Quelle | Werkzeug | Ergebnis |
|---|---|---|---|
| **P Kursprojekt** | `lessons/NN_slug/lesson.md` und `phase_config.yaml` im Projekt | `edu-seiten split` | `_student_site/` (MkDocs), je Lektion eine Seite pro Phase |
| **D Einzeldokumente** | Material der Bibliothek oder andere Markdown-Dateien mit Lehrerteil | `edu-seiten strip` | `_schuelerfassung/` – gleiche Dateien ohne Lehrerteil |

Aufbau, Befehle und Stolperfallen: `references/kursprojekt.md`.

## Eingaben
- **Pflicht (sonst Rückfrage):** Quelle – Projektordner oder Dateien.
- **Wichtig, sonst Annahme:** Ziel (Lerngruppe im LMS, öffentliche Website, Druck),
  Name der Ausgabe, ob Übungs-Lösungen sichtbar sein dürfen (Standard: nein).
- **Optional:** Planungsakte, Prüfbericht der Lehrerfassung, vorhandene `phase_config.yaml`.

## Leitlinien (verbindlich)
1. **Erst prüfen, dann ausgeben:** Die Lehrerfassung ist geprüft (`material-pruefen`, Ampel
   mindestens 🟡). Ungeprüftes Material bleibt Entwurf.
2. **Nichts für Lehrkräfte in die Ausgabe:** keine Lösungen zu Leistungsüberprüfungen,
   Erwartungshorizonte, Bewertungskriterien, didaktischen Hinweise, Lösungsdiagramme,
   Planungsakten, Gutachten, Begleitblätter, vertraulichen Dateien (`vertraulich: true`).
3. **Nichts fällt still weg:** jede H1 einer Lektion ist einer Phase zugeordnet oder bewusst
   ausgeschlossen (`ausgabe_pruefen.py --projekt`).
4. **Keine offenen Planungsnotizen** (`⚠️ Annahme:`, `🔎 Prüfen:`, `[ABBILDUNG: …]`) und keine
   personenbezogenen Daten von Lernenden.
5. **Gekennzeichnet:** jede Seite trägt den KI-Transparenzhinweis, die Transparenzseite
   existiert (Skill `ki-kennzeichnung`) – der Hinweis behauptet eine Prüfung durch die
   Lehrkraft, deshalb erst nach deren Durchsicht.
6. **Bestehende Konfiguration nicht überschreiben:** `phase_config.yaml` ergänzen, nie
   ersetzen; Lehrerdateien nie verändern (außer auf Wunsch Überschriften für `strip`
   vereinheitlichen).
7. **Veröffentlichen nur nach Freigabe und Auftrag:** Freigabezeile der Lehrkraft im
   Protokoll (`freigabe_pruefen.py`), dann ausdrücklicher Auftrag für Push, Upload oder
   Deploy. Öffentlich nur, was öffentlich sein darf (Rechte an Bildern und Texten 🔎).
8. **Kurz, offen, anschaulich, ohne Dekoration** (`references/schuelermaterial.md`): Was
   veröffentlicht wird, ist Material für Lernende – lange Texte, kleinschrittige Aufträge,
   fehlende Darstellungen und Schmuck werden in der Quelle behoben, nicht in der Ausgabe.

## Vorgehen
1. **Modus bestimmen** (Ordner mit `lessons/` → P, sonst D).
2. **Modus P vorbereiten:** `<projekt>/scripts/phase_config.yaml` prüfen bzw. aus
   `assets/phase_config-vorlage.yaml` anlegen (`site:`-Block, `copy_dirs` ohne
   `solutions`, `ki_kennzeichnung:`). Neue Lektionen nach `references/vorlage-lektion.md`
   (didaktisch: `references/lektionsmuster.md`); vor dem Erzeugen
   `python3 scripts/lektion_pruefen.py lessons/*/lesson.md --projekt <projekt>` – meldet H1, die
   still wegfielen, und Hinweise auf verdeckte Schwierigkeiten im Schülerteil. Die Beispieldateien
   unter `copy_dirs` (z. B. `examples/`) werden veröffentlicht: keine Musterlösung einer Aufgabe
   dort ablegen.
   **Modus D vorbereiten:** Lehrerteil der Dateien steht unter `# Lösungen …` bzw.
   `# Didaktische Hinweise` (Bibliotheks-Material tut das).
3. **Erzeugen:**
   - P: `edu-seiten split` im Projektordner bzw.
     `python3 scripts/edu.py seiten split --project-root <projekt>`
   - D: `edu-seiten strip --teacher . --student _schuelerfassung --lf .=DATEI1.md,DATEI2.md`
     bzw. `python3 scripts/edu.py seiten strip …` (gleiche Optionen)
4. **Prüfen:** `python3 scripts/ausgabe_pruefen.py AUSGABE [--projekt <projekt>]` – jedes ❌
   in der **Quelle** beheben, neu erzeugen, erneut prüfen. Form der Seiten:
   `python3 scripts/schuelermaterial_pruefen.py QUELLE.md…` (Länge, Aufträge, Darstellungen,
   Dekoration) – ❌ in der Quelle beheben. Werden Word- oder PDF-Dateien
   mitveröffentlicht: `python3 scripts/metadaten_pruefen.py AUSGABE` – Autor- und
   Bearbeiterfelder, Kommentare und verfolgte Änderungen vorher entfernen (Werte gibt das Skript
   nicht aus).
5. **Kennzeichnen** (falls noch nicht geschehen): Skill `ki-kennzeichnung`; im Modus P setzt
   `split` die Hinweise selbst, sobald `ki_kennzeichnung:` konfiguriert ist.
6. **Bauen** (P): `cd _student_site && mkdocs build --strict`; ohne MkDocs als offenen
   Schritt vermerken. Externe Links: `material-pruefen` (bzw. `edu-linkcheck`).
7. **Protokoll** nach `assets/vorlage-veroeffentlichung.md` mit `Freigabe: ausstehend`.
8. **Nach Freigabe:** `python3 scripts/freigabe_pruefen.py 94_veroeffentlichung_<kurztitel>.md`
   – erst bei ✅ und auf ausdrücklichen Auftrag veröffentlichen.

**Ohne Skriptausführung:** Lehrerteile von Hand entfernen ist fehleranfällig – nur mit
Checkliste aus Leitlinie 2–4 und dem Hinweis, die Ausgabe lokal mit `edu-seiten` und
`ausgabe_pruefen.py` zu wiederholen.

## Ausgabe
- `_student_site/` (P) bzw. `_schuelerfassung/` (D) – erzeugt, nicht von Hand bearbeiten
- `94_veroeffentlichung_<kurztitel>.md` – Protokoll (Artefakt nach Skill-Vertrag) mit
  Prüfergebnissen und Freigabezeile
- Planungsakte: Artefakt 94 eintragen; Status „Freigabe ausstehend" bis zur Freigabe.

## Qualitätscheck
- [ ] Lehrerfassung vorher geprüft?
- [ ] `ausgabe_pruefen.py` ohne ❌ (mit `--projekt` im Modus P)?
- [ ] `schuelermaterial_pruefen.py` ohne ❌ – Seiten kurz, Aufträge offen, mit Darstellungen, ohne Dekoration?
- [ ] Jede Seite gekennzeichnet, Transparenzseite vorhanden?
- [ ] Build und Links ohne Fehler (bzw. als offen vermerkt)?
- [ ] Freigabezeile vorhanden, bevor veröffentlicht wird?

## Beispielaufrufe
> „Mach aus `40_material_wartung.md` und `60_differenzierung_wartung.md` eine Schülerfassung
> ohne Lösungen für Moodle."

> „Erzeuge für das Projekt LF4 die Schülerseiten, prüf, dass keine Lösungen drin sind, und
> bereite GitHub Pages vor – veröffentlicht wird nach meiner Freigabe."

## Referenzen – wann lesen
- `references/kursprojekt.md` – **immer** (Modi, Aufbau, Befehle, Veröffentlichung, Fehler).
- `assets/phase_config-vorlage.yaml`, `references/vorlage-lektion.md` – Modus P;
  `references/lektionsmuster.md` – Elemente einer Lektion.
- `references/ki-vereinbarungen.md` – Infokasten *KI-Werkzeuge* und Zeichen 🚫 💡 🔧 am Arbeitsschritt.
- `scripts/lektion_pruefen.py` – Lektionen vor dem Erzeugen prüfen (H1-Zuordnung, Muster).
- `assets/vorlage-veroeffentlichung.md` – **immer** (Protokoll).
- `references/schuelermaterial.md` – Form des Materials für Lernende.
- `scripts/schuelermaterial_pruefen.py` – Länge, Aufträge, Darstellungen, Dekoration der Quellen.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/ausgabe_pruefen.py` – Prüfung der Ausgabe und Projektkonfiguration.
- `scripts/metadaten_pruefen.py` – Metadaten von DOCX/ODT/PDF vor der Veröffentlichung.
- `scripts/freigabe_pruefen.py` – Freigabe-Gate vor dem Veröffentlichen.
- `scripts/edu.py` – startet `edu-seiten` (und `edu-kennzeichnung`) aus der mitgelieferten
  Kopie (`scripts/eduwerkzeuge/`).
