---
artefakt: Fachdiagramm – Diagrammblatt
titel: "[Thema der Diagramme]"
skill: fachdiagramm-erstellen
skill_version: "1.8"
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

> KI-gestützt erstellt (Skill fachdiagramm-erstellen v1.8). Fachliche Prüfung und Verantwortung: Lehrkraft.
