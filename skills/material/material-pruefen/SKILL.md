---
name: material-pruefen
description: Prüft Unterrichtsmaterial, Arbeitsblätter, Lösungen, Erwartungshorizonte und KI-Entwürfe vor dem Einsatz mit kombinierbaren Prüfungen – Fakten (Aussagen, Normen, Vorschriften, Zitate, Quellen mit Typ und Interessenlage), Plausibilität (nachrechnen, Einheiten, physikalische Grenzen, Lösbarkeit, Widersprüche, Sicherheit bei Versuchen), Code (Python, C/C++/Arduino, G-Code), Form für Lernende (Textmenge, offene Aufträge, Darstellungen, Dekoration), Links (auch in Word, PowerPoint, PDF) und Metadaten vor der Weitergabe. Liefert einen Prüfbericht mit Befund, Sicherheit, Korrekturvorschlag, Quelle und Prüfaufträgen; lieber „nicht prüfbar" als geraten. Verwenden bei „prüfe", „Faktencheck", „stimmt das?", „Plausibilität", „Links prüfen", „Code prüfen", „Qualitätssicherung", vor der Weitergabe und nach jeder KI-Erstellung. Nicht für ganze Lernsituationen nach SchuCu-BBS (lernsituation-analysieren).
metadata:
  version: "1.5"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: pruefen
  stand: "2026-11"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Material prüfen: Fakten, Plausibilität, Form, Links

## Zweck
KI-Entwürfe und vorhandenes Material **vor dem Einsatz absichern** – mit nachvollziehbaren
Befunden statt Bauchgefühl. Die Entscheidung über Korrekturen trifft die Lehrkraft.

**Wann nicht:** Ganze Lernsituationen nach SchuCu-BBS (Analysebogen, Phasencheck) prüft `lernsituation-analysieren`.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Prüfarten (Standard: F, P, L und S bei Material für Lernende; C und M, sobald Code bzw. Weitergabe ansteht)

| Prüfart | prüft | Werkzeug |
|---|---|---|
| **F Faktencheck** | Sachaussagen, Zahlen und Grenzwerte, Normen und Vorschriften, Definitionen, Zitate, Quellenangaben – mit **Quellentyp und Interessenlage** | Websuche (falls verfügbar), gelieferte Unterlagen, Fachwissen mit Sicherheitsangabe; `references/quellenbewertung.md` |
| **P Plausibilitätscheck** | Rechnungen, Einheiten, Größenordnungen, Lösbarkeit, innere Widersprüche, Realitätsnähe, Zeitbedarf; **Experimente**: physikalische Grenzen (Faraday, η ≤ 1, Energiekette) und Sicherheit | Nachrechnen (Code), Checkliste; `python3 scripts/messwerte_pruefen.py faraday|kette|einheit|unsicherheit …`; `references/experimentsicherheit.md` |
| **C Codecheck** | Programmcode in Material und Erwartungshorizont: Syntax (Python, C/C++/Arduino mit g++), Dezimalkomma, G-Code (Vorschub, Kreisbögen, Spindel, Programmende, Verfahrbereich) | `python3 scripts/code_pruefen.py DATEI…` (liest md, docx, pdf über `scripts/text_lesen.py`) |
| **S Form für Lernende** | Teil für Lernende kurz (Fließtext gegen Richtwert, lange Sätze und Aufträge), offen statt kleinschrittig (Teilaufgaben, Schrittfolgen, Lesen als Auftrag), mit Darstellungen als Arbeitsgegenstand, ohne Dekoration (Symbole, Floskeln, Schmuckbilder), ohne Lehrerangaben, ohne Wiederholungen; Zeichnungen als SVG statt aus Zeichen (Prüfpunkt 12, auch in Lösungen) | `python3 scripts/schuelermaterial_pruefen.py DATEI.md…`; `references/schuelermaterial.md` |
| **L Linkcheck** | Erreichbarkeit, Weiterleitungen, Soft-404, Domainwechsel, http, inhaltliche Passung; auch PDF (Link-Annotationen und Text-URLs) | `python3 scripts/linkcheck.py DATEI_ODER_ORDNER` |
| **M Metadaten** | Autor, letzte Bearbeitung, Firma, Kommentare, verfolgte Änderungen, Dokumenttitel vor der Weitergabe – Werte werden nicht ausgegeben | `python3 scripts/metadaten_pruefen.py DATEI_ODER_ORDNER` |

## Eingaben
- **Pflicht:** das zu prüfende Material (eine oder mehrere Dateien, auch .docx/.pptx für L).
- **Optional:** gelieferte Referenzen (Ordnungsmittel, Herstellerunterlagen, Normauszüge),
  gewünschte Prüfart(en), Prüftiefe (Schnellcheck / gründlich), Planungsakte.

## Grundsätze
1. **Lieber nicht prüfbar als geraten.** Jeder Befund trägt eine Sicherheit (hoch/mittel/
   niedrig). „❌ falsch" nur bei hoher Sicherheit **und** benannter Quelle oder nachvollziehbarer
   Rechnung.
2. **Quellenhierarchie beachten** (`references/faktencheck-methode.md`): gelieferte
   Unterlagen → amtliche Quellen → Normen/Hersteller → Fachliteratur → Sekundärquellen.
3. **Sicherheitsrelevantes zuerst:** Arbeitsschutz, Elektrotechnik, Druck, Gefahrstoffe,
   Hygiene (z. B. Trinkwasser), Lasten; bei Versuchen Gefährdungsbeurteilung, Gase,
   Netzspannung (`references/experimentsicherheit.md`). Ein allgemeiner PSA-Hinweis ersetzt
   keine Gefährdungsbeurteilung.
4. **Nachrechnen, nicht nachlesen:** Jede Rechnung wird unabhängig neu gerechnet.
5. **Nicht still korrigieren.** Der Bericht schlägt vor; eine korrigierte Fassung entsteht
   nur auf Wunsch (oder bei eindeutigen Fehlern als separate Datei `…_korrigiert.md`).
6. **Ohne Internet ehrlich bleiben:** Ist keine Websuche verfügbar, steht das im Bericht; der
   Faktencheck stützt sich dann auf Fachwissen mit Sicherheitsangabe und Prüfaufträgen.

## Vorgehen
1. **Inventur:** Material lesen, prüfbare Einheiten nummerieren – Aussagen, Zahlen, Normen,
   Rechtsbezüge, Rechnungen, Abbildungsbezüge, Links, Personen/Firmen/Kontaktdaten,
   **Datei- und Anhangsverweise** (gegen den Ordnerinhalt). Gescannte PDF und eingebettete
   Bilder rendern und ansehen, statt sie als „nicht prüfbar“ zu übergehen.
2. **Faktencheck (F):** je Aussage Typ bestimmen, Quelle suchen (lateral lesen: was sagen
   *andere* verlässliche Quellen?), Befund und Sicherheit festlegen. Typische KI-Fehlermuster
   gezielt prüfen (`references/faktencheck-methode.md`, Abschn. 4).
3. **Plausibilitätscheck (P):** Checkliste `references/plausibilitaet.md` – Rechnungen neu
   rechnen, Einheiten/Dimension, Größenordnung, Lösbarkeit (sind alle nötigen Angaben da?),
   Konsistenz Aufgabe ↔ Lösung ↔ Abbildung ↔ Lernsituation, Realitätsnähe, Zeitbedarf.
4. **Codecheck (C)**, wenn Material Programmcode enthält: Skript ausführen; Befunde mit
   Zeilenangabe übernehmen; Bibliotheksfunktionen und Pinbelegungen bleiben 🔎 (Datenblatt).
   **Messwerte:** Beispielmessungen im Erwartungshorizont gegen die physikalische Grenze
   prüfen (`messwerte_pruefen.py`); Wirkungsgradketten rückwärts rechnen (dividieren!).
5. **Quellen bewerten:** Typ und Interessenlage jeder Quelle bestimmen
   (`references/quellenbewertung.md`). Interessenquellen ohne Gegenquelle und unbelegte Zahlen
   melden; Desinformation nur als gekennzeichneten Analysegegenstand stehen lassen.
6. **Form für Lernende (S):** Skript ausführen, Befunde mit Zeile übernehmen und gegen
   `references/schuelermaterial.md` lesen: Fehlt eine Darstellung, wo eine trüge? Ist ein
   Auftrag eine Schrittfolge, die in die Hilfen gehört? Was braucht kein Auftrag? Vorschlag je
   Befund (streichen, zusammenfassen, Darstellung ergänzen) – nicht still kürzen.
7. **Linkcheck (L):** Skript ausführen; danach für erreichbare Links stichprobenartig prüfen,
   ob der Inhalt noch zur Verwendung passt (Werbung, Tracking, Paywall, Altersangemessenheit,
   Lizenz). Ersatzlinks nur aus einer echten Suche – sonst Suchbegriffe vorschlagen.
8. **Metadaten (M)** vor jeder Weitergabe: Skript ausführen, Ergebnis ohne Werte in den
   Bericht (Feld belegt → bereinigen).
9. **Bericht schreiben**, Befunde nach Schwere sortieren, Prüfaufträge für die Lehrkraft
   formulieren (was die KI nicht prüfen konnte).

## Ausgabe
Datei `90_pruefbericht_<kurztitel>.md`, Kopf nach Skill-Vertrag:
1. **Ergebnis auf einen Blick** – Ampel (🟢 einsetzbar · 🟡 nach Korrekturen einsetzbar ·
   🔴 überarbeiten), Anzahl Befunde je Schwere, Prüfumfang (mit/ohne Websuche)
2. **Befundtabelle** – Nr. | Fundstelle | Aussage/Element | Prüfart | Befund (✅/⚠️/❌/🔎) |
   Sicherheit | Korrekturvorschlag | Quelle
3. **Nachgerechnet** – Rechnungen mit eigenem Rechenweg und Abweichung
4. **Linkliste** – Ausgabe des Skripts + inhaltliche Anmerkungen
5. **Prüfaufträge für die Lehrkraft** – z. B. „Normtext DIN … Abschn. … einsehen"
6. Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis)

## Qualitätscheck
- [ ] Alle prüfbaren Einheiten erfasst (insb. Zahlen, Normen, Sicherheitsangaben, Links, Code, Metadaten)?
- [ ] Quellen nach Typ und Interessenlage eingeordnet; Experimente gegen Grenzen und Sicherheit geprüft?
- [ ] Jeder ❌-Befund mit Quelle oder Rechnung belegt, jede Sicherheit angegeben?
- [ ] Rechnungen unabhängig nachgerechnet, Einheiten geprüft?
- [ ] Keine erfundenen Quellen oder Ersatzlinks im Bericht?
- [ ] Prüfgrenzen offen benannt (ohne Websuche, Normtext nicht verfügbar …)?
- [ ] Material für Lernende auf Form geprüft (S: Textmenge, offene Aufträge, Darstellungen, Dekoration)?
- [ ] Keine Zeichnung aus Zeichen und kein Mermaid in der Ausgabe – auch in Lösungen und Lehrerteil (`zeichnungen_pruefen.py`)?
- [ ] Ampel begründet und konsistent mit den Befunden?

## Beispielaufrufe
> „Prüf die Lernsituation `Lernsituation_Inbetriebnahme_Spuelung.md` auf Fakten und
> Plausibilität – die ist KI-generiert und noch ungeprüft."

> „Linkcheck für alle Dateien im Ordner `LF4/`, auch die Word-Dateien."

## Referenzen – wann lesen
- `references/faktencheck-methode.md` – Aussagetypen, Quellenhierarchie, laterales Lesen,
  KI-Fehlermuster, Befundskala. **Bei F.**
- `references/plausibilitaet.md` – Prüfliste und Größenordnungen für den Überschlag. **Bei P.**
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
- `scripts/linkcheck.py` – Linkprüfung (Python 3, ohne Zusatzpakete; braucht Internetzugang; PDF über poppler).
- `scripts/code_pruefen.py` (mit `scripts/text_lesen.py`) – Codecheck. **Bei C.**
- `scripts/messwerte_pruefen.py` – Faraday, Wirkungsgradkette, Einheiten, Messunsicherheit. **Bei P.**
- `scripts/metadaten_pruefen.py` – Metadaten vor der Weitergabe. **Bei M.**
- `scripts/schuelermaterial_pruefen.py` und `references/schuelermaterial.md` – Form für Lernende. **Bei S.**
- `references/quellenbewertung.md` – Quellentypen, Interessenlage, Desinformation, KI-Text. **Bei F.**
- `references/experimentsicherheit.md` – Gefährdungsbeurteilung, typische Gefahren, Messwerte. **Bei P.**
- `references/berufliches-gymnasium.md` – Realitätsnähe im BG (fiktive Auftraggeber, Lerngebiete).
