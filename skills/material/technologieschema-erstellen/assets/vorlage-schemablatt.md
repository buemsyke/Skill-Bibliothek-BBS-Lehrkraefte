---
artefakt: Technologieschema – Schemablatt
titel: "[Anlage / Aufgabe]"
skill: technologieschema-erstellen
skill_version: "1.7"
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
| -SJ1 | Taster | [Start …] |

| Feld | Eintrag |
|---|---|
| Spec (hier ändern) | `schema/46_[kurztitel].yaml` |
| Dateien | `.drawio.svg` (bearbeitbar in diagrams.net, zugleich Bild) · `.svg` (Bild) · `.png` (Word, aus `vorschau_png.py`) |
| Kennzeichnung | DIN EN IEC 81346-2:2020 (immer); [Entsprechungen einer Vorlage, z. B. S1 → -SJ1, Y1 → -MB1] |
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

> KI-gestützt erstellt (Skill technologieschema-erstellen v1.7). Fachliche Prüfung und Verantwortung: Lehrkraft.
