---
artefakt: Abiturvorschlag – Begleitblatt
titel: "[Thema A] / [Thema B]"
skill: abiturvorschlag-erstellen
skill_version: "1.22"
stand: JJJJ-MM-TT
bildungsgang: "Berufliches Gymnasium Technik"
fach: "Technik"
schwerpunkt: "[Schwerpunkt]"
pruefungsjahr: "[JJJJ]"
curriculare_vorgabe: "RRL Technik im Beruflichen Gymnasium – Technik – (Erweiterung 06/2025)"
dqr: 4
vertraulich: true
status: "KI-Entwurf – fachlich zu prüfen"
---

# Begleitblatt: Abiturvorschläge [Fach – Schwerpunkt], Abitur [JJJJ]

Dieses Blatt gehört **nicht** zu den Einreichungsunterlagen. Es dokumentiert Bauplan, Prüfungen und
offene Punkte für die Lehrkraft und die Fachgruppe.

## Dateien

| Datei | Inhalt |
|---|---|
| `75_abitur_[kurztitel]_A_schuelermaterial.md` | Vorschlag A, Schülermaterial |
| `75_abitur_[kurztitel]_A_lehrermaterial.md` | Vorschlag A, Lehrermaterial |
| `75_abitur_[kurztitel]_A_bewertungsraster.md` | Vorschlag A, Bewertungsraster: Merkmale je Teilaufgabe mit Kurztext und Regeln (für die Korrektur, nicht Teil des Lehrermaterials) |
| `75_abitur_[kurztitel]_A_bewertungsbogen.md` | Vorschlag A, Bewertungsbogen (erzeugt) |
| `75_abitur_[kurztitel]_A_bewertungsmappe.xlsx` | Vorschlag A, Bewertungsmappe für Korrektur und Gutachten (erzeugt, leer) |
| `75_abitur_[kurztitel]_B_…` | Vorschlag B, entsprechend |

## Bauplan Vorschlag A

| Teilaufg. | Gegenstand | Operator(en) | I | II | III | BE | Min. | Lerngebiet | Unterrichtsbezug | Material |
|---|---|---|---:|---:|---:|---:|---:|---|---|---|
| 1.1 | [ … ] | [nennen, erläutern] | [4] | | | [4] | [10] | [IT2] | [12.1: …] | – |
| **Σ** | | | **[36]** | **[48]** | **[36]** | **[120]** | **[300]** | | | |

## Bauplan Vorschlag B

[wie A]

## Gleichwertigkeit A und B

| Merkmal | A | B | Bewertung |
|---|---|---|---|
| Bearbeitungszeit / BE | [300 / 120] | [300 / 120] | [gleich] |
| AFB I/II/III in % | [30/40/30] | [ … ] | [Abstand ≤ 5 Punkte (Ziel), ≤ 10 (Grenze, Katalog 4.6)] |
| Lerngebiete je Aufgabe | [ … ] | [ … ] | [gleich] |
| Thema, Anlage | [ … ] | [ … ] | [verschieden] |
| Teilaufgaben, Zeichenaufwand | [ … ] | [ … ] | [ … ] |

## Ergebnisse der Prüfskripte

- `abitur_check.py` Vorschlag A: [keine ❌; ⚠ mit Begründung] – Zeile
  `Gesamtsummen (AFB I, AFB II, AFB III, gesamt) …`
- `abitur_check.py` Vorschlag B: [ … ]
- Vergleich (`--vergleich`): [ … ]
- `bmk_pruefen.py` (nur Steuerungstechnik): [ … ]

## Lösbarkeitsprobe (Rollenwechsel)

| Teilaufgabe | lösbar mit den Angaben? | Konfidenz | Begründung bzw. fehlende Angabe |
|---|---|---:|---|
| [1.1] | [ja] | [90] | [ … ] |

## Korrekturprobe

Je Teilaufgabe mit Merkmalen der Art *Kriterium* oder *Urteil*: drei erfundene Antworten, bewertet
mit der Merkmaltabelle des Bewertungsrasters.

| Teilaufgabe | erfundene Antwort | BE nach Merkmalen | eindeutig? | Folge |
|---|---|---|---|---|
| [2.2] | vollständig richtig | [12 / 12] | [ja] | – |
| [2.2] | typischer Fehler: [ … ] | [ … / 12] | [ja] | – |
| [2.2] | zulässige Alternative: [ … ] | [ … / 12] | [nein] | [Merkmal 3 geschärft: …] |

## Einreichungscheckliste

| Kennung | Kriterium (Kurzform) | Nachweis bzw. Fundstelle | Status |
|---|---|---|---|
| 1.1–1.3, X.6 | Schriftbild, Dokumentvorlage, Kopf mit Schwerpunkt | [Word-Fassung] | [ … ] |
| 2.1 | zwei Vorschläge | [A und B] | |
| 2.2, 2.3 | Lerngebiete, Unterrichtszusammenhang konkret | [LM, Unterrichtliche Voraussetzungen] | |
| 2.4–2.8 | Erwartungshorizont, Musterlösung, Bewertungsmaßstab, Hilfsmittel, Formelsammlung | [LM; SM Abschn. C] | |
| 3.1–3.5 | übergeordnete Kompetenzen, Lerngebiete, Situation, Handlungskompetenz, alle AFB | [Bauplan] | |
| 4.1–4.7 | klare Aufträge, unabhängig, Zeit, Operatoren, AFB, BE | [Skript, Abschn. oben] | |
| X.1–X.14 | Zusatzkriterien | [Skript; X.11 Korrekturlesen] | |
| S.1–S.4 | Platzhalter, Anlagen, Dateien, Nummerierung | [Skript] | |
| K.1–K.9 | Korrigierbarkeit | [Skript, Korrekturprobe] | |
| T.1–T.9 | Betriebsmittelkennzeichen und GRAFCET-Notation | [`bmk_pruefen.py`] | |

## Vor der Einreichung (Lehrkraft, Fachgruppe)

- [ ] Probebearbeitung durch eine Fachkollegin oder einen Fachkollegen mit Zeitmessung
- [ ] optional: unabhängige Bewertung der erfundenen Antworten der Korrekturprobe
- [ ] Kursfolge durch Beschluss der Fachgruppe belegt; Unterrichtsbezug mit den Kursen abgeglichen
- [ ] Dokumentvorlage, Kopf- und Fußzeilen, Seitenzahlen (`abitur_docx.py --vorlage … --seiten`), Word-Fassung gesichtet; Abbildungen an der richtigen Stelle und in Schwarzweiß lesbar
- [ ] Schülermaterial ohne Anlagen höchstens 12 Seiten (Word-Fassung) – A: [ ] Seiten, B: [ ] Seiten
- [ ] Endfassung (DOCX/PDF) erneut geprüft (`bmk_pruefen.py`)
- [ ] Rechte an Abbildungen und Datenblattauszügen geklärt, Quellen angegeben
- [ ] Dateien für PC-Aufgaben in den Prüfungsunterlagen, Ausfallregel bekannt
- [ ] Vertraulichkeit: Ablage, Weitergabe und KI-Umgebung nach Vorgabe der Schule bzw. Behörde
- [ ] Angabe zur KI-Nutzung bei der Erstellung nach Vorgabe der Dienststelle 🔎

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Nur Unterrichtetes, Bezug je Aufgabe konkret | | |
| Aufträge eindeutig (K.7), BMK und GRAFCET einheitlich (T.1–T.9) | | |
| Jede BE an einem Merkmal im Bewertungsraster, Summen stimmen (K.1, K.2) | | |
| Kurztexte knapp, ohne Werte (K.10) | | |
| Umfang: Schülermaterial ≤ 12 Seiten ohne Anlagen, Lehrermaterial ohne Merkmaltabellen (U.1, U.2) | | |
| Korrekturprobe ohne Mehrdeutigkeit | | |
| AFB gesamt und je Aufgabe, Takt | | |
| Musterlösung mit Code nachgerechnet | | |
| A und B gleichwertig, nicht austauschbar | | |
| `abitur_check.py` ohne ❌ | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: [ … ]
- 🔎 Prüfen: [ … ]

## Übergabe

- Vorschläge, Zeit, BE, AFB: [ … ]
- Empfohlene nächste Skills: 
  `fachdiagramm-erstellen` (Technologieschema,
  Lösungsbilder), `programmieraufgabe-erstellen` (Code-Material und Testfälle)
- Nach der Genehmigung: Bewertungsmappe aus dem endgültigen Bewertungsbogen neu erzeugen
  (`bewertungsmappe.py`), Kurztexte mit der Fachgruppe abstimmen, dann korrigieren.

> KI-gestützt erstellt (Skill abiturvorschlag-erstellen v1.22). Fachliche Prüfung und Verantwortung: Lehrkraft.
