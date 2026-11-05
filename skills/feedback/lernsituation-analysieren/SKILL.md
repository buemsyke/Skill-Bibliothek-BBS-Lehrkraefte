---
name: lernsituation-analysieren
description: Prüft vorhandene Lernsituationen – als Word, PDF oder Markdown, auch ältere Vorlagen, einzeln oder alle eines Lernfelds – nach der Leitlinie SchuCu-BBS 2024 und den Mustern der Bibliothek. Ein Skript liest jedes Format und liefert einen Vorbefund; darauf folgen Analysebogen mit 16 Kriterien, Phasencheck, Leitidee, Querschnittsaufgaben, DQR-Niveau und Quellen, bei mehreren Lernsituationen Kompetenzraster und Stundenbilanz – jede Einschätzung mit geprüftem Beleg. Ergebnis ist ein Prüfbericht mit Ampel, Stärken und den drei wirksamsten Verbesserungen. Verwenden bei „Prüf diese Lernsituation", „Analysebogen ausfüllen", „Ist unsere LS SchuCu-konform?", „Rückmeldung zur Lernsituation", „wir wollen die LS übernehmen", „alle LS des Lernfelds prüfen". Nicht zum Neuschreiben oder Überführen (lernsituation-dokumentieren), nicht für einzelnes Material ohne Lernsituation (material-pruefen), nie zur Beurteilung von Personen.
metadata:
  version: "1.4"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: pruefen
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Lernsituation analysieren (Prüfbericht nach SchuCu-BBS 2024)

## Zweck
Eine vorhandene Lernsituation in einem Durchgang nach allem prüfen, was Leitlinie und Bibliothek
verlangen – damit Lehrkraft bzw. Bildungsgangteam sehen, was trägt, was fehlt und was zuerst zu
tun ist. Der Skill prüft und schlägt vor; er schreibt die Lernsituation nicht um (dafür
`lernsituation-dokumentieren`, Modus B).

## Wann dieser Skill – und wann nicht
- **Ja:** vorhandene Lernsituation(en) in beliebigem Format prüfen, Analysebogen ausfüllen,
  Rückmeldung für das Bildungsgangteam vorbereiten, eigene LS vor der Abstimmung prüfen, alle LS
  eines Lernfelds bzw. Lerngebiets nebeneinander prüfen.
- **Nein:** LS neu entwickeln oder überführen → `lernsituation-dokumentieren` (prüft den eigenen
  Entwurf dort selbst); Unterrichtsentwurf → `unterrichtsentwurf-analysieren`; nur Fakten und Links
  eines Materials → `material-pruefen`.
- **Grenzen:** Rückmeldung zur Lernsituation, nie ein Urteil über Personen; nicht für
  Auswahlverfahren oder dienstliche Beurteilungen. Ist die LS Teil einer Prüfungsleistung (etwa
  Anlage zu einem Entwurf für den Prüfungsunterricht): nur gekennzeichneter Selbstcheck, Hinweise
  statt fertiger Formulierungen (`references/leitplanken-bewertung.md`). Zum Ton der Rückmeldung an
  Kolleginnen und Kollegen: `references/kollegiale-beratung.md`.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen · einheitlicher Kopf und Pflichtabschnitte.
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht:** die Lernsituation (Datei oder eingefügter Text).
- **Wichtig, sonst Annahme:** Bildungsgang bzw. Beruf, Lernfeld bzw. Lerngebiet mit Auszug aus
  RLP bzw. RRL (für A1 und A4 – ohne Auszug nur Prüfauftrag), DQR-Niveau, Anlass (Selbstcheck,
  Abstimmung, Übernahme).
- **Optional:** weitere LS desselben Lernfelds, Kompetenzcodes der Zielformulierung, verfügbare
  Stunden, Material zur LS.
- Namen von Lehrkräften und Lernenden vorher entfernen; das Skript meldet Autorenzeilen und
  Kontaktdaten.

## Ablauf

1. **Vorbefund per Skript** – mit Dateizugriff immer zuerst:
   `python3 scripts/ls_analyse.py LS.docx [weitere LS …] --text vorbefund/`
   Liest Word, ODT, PDF und Markdown (`scripts/text_lesen.py`) und gibt je Aspekt die Kennung aus
   dem Prüfkatalog aus; nutzt `scripts/bloom_check.py` (Operatoren) und `scripts/lesbarkeit.py`
   (LIX). Liegt die LS im Format der Bibliothek vor, läuft zusätzlich die Formalprüfung
   `scripts/lernsituation_pruefen.py`. Gescannte PDF ohne Text: Abschrift oder OCR erbitten.
   **Ohne Skriptausführung** (z. B. AIS.chat): Vorbefund selbst nach Teil E des Katalogs erheben
   und das im Bericht vermerken.
2. **Kontext klären** – Format erkennen (Leermaske 2024, älteres Format, KMK-Raster,
   Schulvorlage). Bildungsgang, Lernfeld bzw. Lerngebiet und DQR aus der LS übernehmen, sonst
   Annahme. Curriculare Vorgabe nachschlagen, nicht erinnern (`references/curriculum-abgleich.md`).
3. **Teil A – Analysebogen** (`references/schucu-bbs-2024.md` Abschn. 4 und 5): je Kriterium
   Stufe, Begründung und wörtlicher Beleg. Nach dem Text urteilen, nicht nach der Vorlage.
4. **Teil B – Phasencheck** (`references/lernsituationsmuster.md` Abschn. 8, Lernzeit Abschn. 12):
   getrennt vom Analysebogen; ❌ ist ein Hinweis, kein Verstoß gegen die Leitlinie.
5. **Teil C – Leitidee** (`references/didaktische-leitidee.md` Abschn. 4): vorhanden → Kriterien
   L1–L5; fehlt → ein Vorschlag nach dem Muster.
6. **Teil D – Querschnitt** Q1–Q7 (`references/querschnittsaufgaben.md` Abschn. 5): nur, was das
   Thema nahelegt.
7. **Teil E – weitere Aspekte** W1–W12 (`references/pruefkatalog-lernsituation.md`): Vorbefund
   übernehmen und bewerten; Niveau gegen DQR (W3), Kompetenzformulierungen
   (`references/operatoren-afb.md`), Quellen (`references/quellenbewertung.md`), Versuche
   (`references/experimentsicherheit.md`), Berufliches Gymnasium
   (`references/berufliches-gymnasium.md`); bei mehreren LS Kompetenzraster mit Rückwärtsprobe,
   Doppelungen und wortgleiche Personale Kompetenzen (W12).
8. **Belege prüfen:** `python3 scripts/zitate_pruefen.py 21_ls-analyse_<kurztitel>.md LS.docx [RLP.pdf]`
   – nicht gefundene Belege korrigieren oder streichen.
9. **Gesamtbild** nach Katalog Teil F: Ampel, Stärken zuerst, die drei wirksamsten Verbesserungen
   als fertige Formulierung (prüfungsrelevant: nur als Hinweis); alles Weitere knapp in den Tabellen.

**Mehrere LS** in einem Auftrag: je LS ein Bericht (Teile A–E), die Querbefunde (W12) in der
Übergabe bzw. einem Sammelbericht. Jede Einschätzung mit Beleg aus genau dieser LS – nie aus einer
anderen übernehmen.

## Ausgabe
`21_ls-analyse_<kurztitel>.md` nach `assets/vorlage-ls-analyse.md`; der Vorbefund steht als
Kurzfassung im Bericht, der gelesene Text unter `vorbefund/`. Die Übergabe nennt Ampel, die drei
Verbesserungen, offene Prüfaufträge und je Befund den Skill zum Vertiefen (Katalog, Spalte
„vertiefen mit“).

## Qualitätscheck
- [ ] Vorbefund des Skripts eingearbeitet, Abweichungen begründet?
- [ ] Analysebogen vollständig (16 Zeilen), Stufen der Leitlinie, jede mit Beleg aus dieser LS?
- [ ] Verbindlichkeit getrennt: Leitlinie (A) · Erlass bzw. Ordnungsmittel (D, W11, W12) · Bibliothek (B, C, W)?
- [ ] Belege mit `zitate_pruefen.py` gefunden?
- [ ] Zeichnungen aus Zeichen in der LS als Verbesserung genannt (`python3 scripts/zeichnungen_pruefen.py`
      auf der Textfassung aus `vorbefund/`); der Prüfbericht selbst enthält keine?
- [ ] Stärken zuerst, höchstens drei Verbesserungen hervorgehoben, konkret und umsetzbar?
- [ ] Ohne Auszug aus RLP bzw. RRL: A1 und A4 als Prüfauftrag, nicht als Urteil?
- [ ] Keine Aussage über Personen, keine Namen?

## Beispielaufrufe
> „Prüf diese Lernsituation (Anhang) – wir wollen sie im Bildungsgangteam übernehmen."

> „Hier sind die vier LS zu Lernfeld 7 als Word-Dateien. Prüf sie nach SchuCu-BBS 2024 und sag
> uns, wo das Lernfeld Lücken hat."

> „Ist meine LS von 2019 noch SchuCu-konform? Nur prüfen, noch nicht überarbeiten."

## Referenzen – wann lesen
- `references/pruefkatalog-lernsituation.md` – **immer** (Kennungen, Prüfweg, Verbindlichkeit, Ampel).
- `assets/vorlage-ls-analyse.md` – **immer** (Ausgabe).
- `references/schucu-bbs-2024.md` – Teil A und W1 (Bestandteile, Begriffswechsel).
- `references/lernsituationsmuster.md` – Teil B.
- `references/didaktische-leitidee.md` – Teil C.
- `references/querschnittsaufgaben.md` – Teil D.
- `references/ki-vereinbarungen.md` – Q7 (KI-Regeln, KI-Phasen, Zeichen): Prüffragen K1–A2.
- `references/curriculum-abgleich.md` – A1, A4 und W12.
- `references/operatoren-afb.md`, `references/berufliches-gymnasium.md`,
  `references/experimentsicherheit.md`, `references/quellenbewertung.md` – Teil E.
- `references/kollegiale-beratung.md`, `references/leitplanken-bewertung.md` – Ton und Grenzen.
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/ls_analyse.py` – Vorbefund; nutzt `scripts/text_lesen.py`, `scripts/bloom_check.py`,
  `scripts/lesbarkeit.py`, `scripts/lernsituation_pruefen.py`.
- `scripts/zitate_pruefen.py` – Belege gegen die geprüften Dateien.
