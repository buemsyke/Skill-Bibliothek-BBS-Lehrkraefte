---
name: bloom-taxonomie
description: Ordnet Lernziele, Kompetenzformulierungen, Aufgaben und Fragen nach der Taxonomie von Bloom (revidiert nach Anderson/Krathwohl – Erinnern, Verstehen, Anwenden, Analysieren, Bewerten, Erschaffen – kombiniert mit der Wissensart) ein, zeigt die Verteilung als Matrix, vergleicht sie mit AFB I–III und dem Zielniveau und schlägt konkrete Umformulierungen vor. Erzeugt außerdem Aufgabentreppen über alle Stufen zu einem Thema und hebt oder senkt das Anspruchsniveau vorhandener Aufgaben. Kennt ergänzend die affektive (Krathwohl) und psychomotorische Taxonomie (Dave) für Haltung und Werkstattpraxis. Verwenden bei „Ordne nach Bloom ein", „Sind meine Aufgaben zu leicht?", „Mach daraus eine Aufgabe auf höherem Niveau", „Erstelle Fragen über alle Taxonomiestufen", bei kognitiver Aktivierung, Aufgabenanalyse und Klausurvorbereitung.
metadata:
  version: "1.4"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Taxonomien nach Bloom

## Zweck
Sichtbar machen, **welche Denkleistung** Aufgaben und Ziele wirklich verlangen – und gezielt
nachsteuern, damit Unterricht kognitiv aktiviert, ohne zu überfordern.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Drei Modi

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Analysieren** | „Ordne die Aufgaben meines Arbeitsblatts nach Bloom ein." | Einordnungstabelle, Matrix, Verteilung, Empfehlungen |
| **B Erstellen** | „Erstelle zu Gewindearten Aufgaben über alle Taxonomiestufen." | Aufgabentreppe Stufe 1–6 mit Erwartungen |
| **C Umformulieren** | „Heb diese drei Aufgaben auf Analysieren/Bewerten." | Vorher/Nachher mit Begründung |

## Eingaben
- **Pflicht:** Material (Aufgaben, Ziele, Fragen) **oder** Thema.
- **Wichtig, sonst Annahme:** Was wurde vorher **geübt**? (Entscheidet, ob eine Aufgabe
  Anwenden oder Problemlösen ist.) Zielniveau (DQR) bzw. Lerngruppe.
- **Optional:** Zielverteilung, Wissensarten, Handlungssituation.

## Grundsätze der Einordnung

1. **Nach tatsächlicher Denkleistung einordnen, nicht nach dem Verb.** „Beurteilen Sie, ob
   Stahl ein Metall ist" ist Erinnern. „Beschreiben Sie den Fehler, den Sie im Messprotokoll
   finden" ist Analysieren.
2. **Vorwissen entscheidet.** Wiederholt die Aufgabe ein geübtes Beispiel → eine Stufe
   niedriger als der Operator suggeriert; verlangt sie Übertragung auf eine neue Situation →
   Anwenden oder höher. Fehlt die Information: begründete Annahme.
3. **Zwei Dimensionen.** Kognitive Prozessstufe (1–6) **und** Wissensart (A Fakten,
   B Konzepte, C Prozeduren, D Metakognition). Berufliche Handlungsaufgaben liegen oft in
   C3–C6; Reflexionsaufgaben in D.
4. **Primärstufe pro Aufgabe.** Die höchste *bewertungsrelevante* Stufe zählt; Teilschritte
   darunter sind Voraussetzungen, keine eigenen Einträge.
5. **Taxonomie ≠ Schwierigkeit.** Erinnern kann schwer sein, Bewerten leicht. Schwierigkeit
   gesondert vermerken, wenn auffällig.
6. **AFB-Bezug** über `references/operatoren-afb.md`; Bloom-Stufe und AFB nicht 1:1
   gleichsetzen (Faustregel: 1–2 ≈ AFB I, 3–4 ≈ AFB II, 5–6 ≈ AFB III).

## Vorgehen

**Modus A – Analysieren**
1. Aufgaben/Ziele extrahieren und nummerieren. Optional deterministische Zählhilfe:
   `python3 scripts/bloom_check.py DATEI.md [--ziele]` (auch .docx, .odt, .pdf; Operatoren je
   Stufe; ersetzt nicht das Urteil). Das Skript meldet Aufträge ohne Listenoperator und
   geschlossene Formate gesondert – diese von Hand einordnen. **Projekt-Lernsituationen:**
   Anforderungen im Lastenheft stehen oft als Nominalform („A) Entwicklung eines …“); das Skript
   ordnet sie über das Verb ein und kennzeichnet sie. Mit `--ziele` zählt es auch Kompetenz- und
   Zielformulierungen („bestimmen den Wirkungsgrad …“) und meldet nicht beobachtbare
   („Bereitschaft entwickeln“). Für Projekte die Aufträge nach der **Denkleistung im
   Erwartungshorizont** einordnen (vorgegebene Arbeitsschritte senken die Stufe). Bewertungsraster und Hinweiskästen nicht
   mitzählen. **„prüfen“** ist mehrdeutig: Prüfhandlung (inspizieren, messen) = Anwenden,
   Urteil an Kriterien = Bewerten.
2. Jede Aufgabe einordnen: Operator · Stufe · Wissensart · AFB · Begründung (ein Satz).
3. Matrix 6 × 4 zählen, Verteilung berechnen.
4. Mit Zielwerten vergleichen. Ohne Vorgabe gilt der **Richtwert für kognitiv aktivierenden
   Unterricht**: höchstens etwa ein Drittel Stufe 1–2, mindestens etwa ein Drittel Stufe 4–6;
   bei DQR 1–2 bzw. Einführungsstunden darf der Anteil Stufe 1–3 höher sein (begründen).
5. Lücken benennen (z. B. „keine Aufgabe in Bewerten", „Metakognition fehlt") und **je Lücke
   eine konkrete Umformulierung** liefern.

**Modus B – Erstellen**
1. Fachlichen Kern und – falls vorhanden – die Handlungssituation bestimmen.
2. Aufgabentreppe bauen: mindestens eine Aufgabe je Stufe 1–6, aufsteigend, inhaltlich
   aufeinander aufbauend, möglichst im selben beruflichen Kontext.
3. Je Aufgabe: Operator, Stufe, Wissensart, AFB, Erwartungshorizont in Stichpunkten.
   Die Treppe ist ein Werkzeug der Lehrkraft: Ins Material für Lernende gehen wenige, größere
   Aufträge daraus, keine Folge von sechs Kleinaufgaben; Stufe 1–2 nur, wo der Auftrag sie
   braucht (`references/schuelermaterial.md`).
4. Für Werkstatt-/Laborinhalte zusätzlich eine praktische Aufgabe mit Stufe nach Dave; für
   Haltungsziele (z. B. Arbeitssicherheit) eine affektive Stufe nach Krathwohl
   (`references/weitere-taxonomien.md`).

**Modus C – Umformulieren**
1. Ist-Stufe bestimmen und begründen.
2. Hebel wählen (`references/taxonomie-matrix.md`, Abschnitt „Hebel"): neue Situation statt
   bekanntes Beispiel, Kriterien selbst entwickeln lassen, Alternativen vergleichen und
   entscheiden, Fehler finden statt Lösung reproduzieren, Ergebnis begründet optimieren.
3. Vorher/Nachher-Tabelle mit Begründung und angepasstem Erwartungshorizont.

## Ausgabe
Datei `45_taxonomie-analyse.md` (Modus A/C) bzw. `45_aufgabentreppe_<thema>.md` (Modus B),
Kopf nach Skill-Vertrag, dann:
- **Einordnungstabelle**: Nr. | Aufgabe (gekürzt) | Operator | Stufe | Wissensart | AFB | Begründung
- **Matrix** (Zeilen Wissensart A–D, Spalten Stufe 1–6, Zellen = Anzahl)
- **Verteilung** (Anteile Stufe 1–2 / 3 / 4–6 sowie AFB I/II/III) mit Bewertung gegen Ziel
- **Empfehlungen** mit ausformulierten Aufgaben
- Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis)

## Qualitätscheck
- [ ] Jede Einordnung begründet und nach tatsächlicher Denkleistung (nicht nur nach Verb)?
- [ ] Annahme zum Vorwissen offengelegt?
- [ ] Beide Dimensionen (Stufe + Wissensart) erfasst?
- [ ] Verteilung gegen Ziel bzw. Richtwert bewertet, Abweichungen begründet?
- [ ] Jede Empfehlung als fertige, einsetzbare Aufgabe formuliert?
- [ ] Erwartungshorizonte passen zur neuen Stufe?

## Beispielaufrufe
> „Analysiere die Aufgaben in `40_material_arbeitsblatt-pneumatik.md` nach Bloom. Die Klasse hat
> Wegeventile bereits benannt und einfache Schaltpläne gezeichnet."

> „Erstelle eine Aufgabentreppe (Stufe 1–6) zum Thema Passungen für Industriemechaniker,
> 1. Ausbildungsjahr, DQR 4."

## Referenzen – wann lesen
- `references/taxonomie-matrix.md` – Stufen, Teilprozesse, Wissensarten, Metallbeispiele je
  Stufe, Hebel zum Anheben. **Bei jeder Einordnung.**
- `references/weitere-taxonomien.md` – Original-Bloom (1956), affektiv, psychomotorisch, SOLO.
- `references/schuelermaterial.md` – was ins Material für Lernende geht: kurz, offen gestellt, anschaulich, ohne Dekoration.
- `references/operatoren-afb.md` – Operator → AFB → Stufe.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
- `scripts/bloom_check.py` – optionale Zählhilfe (Python 3, ohne Zusatzpakete); liest Word/PDF
  über `scripts/text_lesen.py`.
