---
artefakt: Lernlandkarte (edumaps) – Begleitblatt
titel: "[Titel der Karte]"
skill: lernlandkarte-erstellen
skill_version: "1.6"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
muster: "[A Lernlandkarte zur LS | B Stundenablauf | C Klausurvorbereitung | D Lernfeldübersicht | E Workshop]"
status: "KI-Entwurf – fachlich zu prüfen"
---

# Lernlandkarte: [Titel]

**Dateien:** `92_lernlandkarte_[kurztitel].md` (Quelle, hier ändern) ·
`92_lernlandkarte_[kurztitel].json` (Import-Datei, erzeugt mit edu-edumap – nicht von Hand ändern)
**Bezug:** [Lernsituation / Entwurf / Material, Dateinamen]
**Einsatz:** [Lerngruppe zusammenfassend, Zeitraum, Präsenz/Distanz, Endgerät]
**Farbgebung:** [Standard (`theme: tageslicht`) / aus Material: Datei → `92_lernlandkarte_[kurztitel]_farben.yaml`]

## Aufbau

| Pfad | Zweck | Karten | Farbe | Hinweis |
|---|---|---|---|---|
| Start | Handlungssituation, Ablauf, Arbeitsweise | 3 | ozeanblau | Auftrag angepinnt |
| ① Selbstdiagnose | Ich-kann-Sätze, Abstimmung, Empfehlung | 3 | tuerkis | |
| [Lernposten A] | [ … ] | [ ] | [ ] | [Hilfen gestuft, Lösung zum Aufdecken] |

Gesamt: [n] Pfade, [m] Karten, davon [k] ausgeklappt.

## Hochzuladende Dateien

Dateien in edumaps über die Büroklammer hochladen und die erzeugte Adresse in der Quelle
eintragen (`https://nds.edumaps.de/file/…`), dann die Import-Datei neu erzeugen.

| Karte | Datei | Quelle im Projekt |
|---|---|---|
| Material A | Arbeitsblatt A (PDF) | `40_material_[ … ].md` → PDF |

## In edumaps einrichten

1. In [nds.edumaps.de](https://nds.edumaps.de) anmelden.
2. Neue Map über den JSON-Import anlegen und `92_lernlandkarte_[kurztitel].json` hochladen.
   🔎 Prüfen: Bezeichnung der Import-Funktion in der aktuellen Oberfläche.
3. Hochzuladende Dateien ergänzen (Tabelle oben), Adressen in die Quelle übernehmen,
   Import-Datei neu erzeugen – oder die Adressen direkt in edumaps eintragen und die Quelle
   nachziehen.
4. Rechte setzen: [Lernende dürfen Karten im Pfad „Ergebnis sichern" anlegen, nicht löschen].
5. Als Lernende bzw. Lernender testen: Karten aufklappen, Quiz, Abstimmung, Lösungskarten.
6. Link oder QR-Code an die Lerngruppe geben.

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| `edumap_pruefen.py` ohne ❌, Platzhalter ersetzt | | |
| Import-Datei gegengeprüft (`--json`: Pfade/Karten gleich, Farben aufgelöst) | | |
| Handlungssituation und Handlungsergebnis wie in der Lernsituation | | |
| Jeder Lernposten: Auftrag mit Operator, Ergebnisform, Sozialform, Zeit, Erfolgskriterien | | |
| Selbstdiagnose führt zu einer Empfehlung | | |
| Hilfen gestuft, verraten die Lösung nicht | | |
| Lösungen nur zur Selbstkontrolle und nur zum Aufdecken; keine Lösungen zu Leistungsüberprüfungen | | |
| Keine Personendaten, kein Kennwort in der Quelle | | |
| Links und Dateien erreichbar (Linkcheck) | | |
| Ansprache einheitlich (du/Sie), Sprache sprachsensibel | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: Verhalten der Karten-Flags (eingeklappt, Aufdecken, Buchung) nach dem Import testen.

## Übergabe

- Quelle und Import-Datei: …
- Offene Uploads: …
- Empfohlene nächste Skills: `material-pruefen` (Links, Fakten in den Karten),
  `quizfragen-erstellen` (H5P-Übungen für die Lernposten), `fachdiagramm-erstellen`
  (Abbildungen), `differenzierung-erstellen` (weitere Hilfekarten)

> KI-gestützt erstellt (Skill lernlandkarte-erstellen v1.6). Fachliche Prüfung und Verantwortung: Lehrkraft.
