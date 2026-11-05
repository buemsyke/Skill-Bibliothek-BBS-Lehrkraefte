---
name: unterrichtsentwurf-analysieren
description: Prüft vor der Stunde einen eigenen schriftlichen Unterrichtsentwurf für Unterrichtsbesuch, Prüfungsunterricht oder Abgabe als Selbstcheck – oder bereitet eine kollegiale Beratung zum Entwurf vor – anhand der Kriterien A1–A11 (Formalien bis Verlauf nach den sechs Phasen) und einer Checkliste vor der Abgabe. Liefert Stärken und Entwicklungsfelder mit wörtlichen, geprüften Belegen, Reflexionsfragen und Überarbeitungsvorschläge – ohne Note, Niveaustufe oder Beurteilung einer Person. Prüfungsrelevante Entwürfe nur als gekennzeichneter Selbstcheck mit Hinweisen statt fertiger Formulierungen. Verwenden bei „prüf meinen Entwurf", „Feedback zum Unterrichtsentwurf", „ist mein UB-Entwurf vollständig?", „Selbstcheck vor dem Prüfungsunterricht", „Beratungsgespräch zum Entwurf vorbereiten". Nach der Stunde hilft unterricht-reflektieren. Nicht für Auswahlverfahren, dienstliche Beurteilungen oder die Benotung von Prüfungsunterricht.
metadata:
  version: "1.6"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: pruefen
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Unterrichtsentwurf analysieren (Selbstcheck und kollegiale Beratung)

## Zweck
Lehrkräften – besonders im Vorbereitungsdienst – helfen, den **eigenen** Entwurf vor der
Abgabe zu verbessern, und kollegiale Beratung strukturiert vorbereiten. Ergebnis ist eine
**Rückmeldung zur Weiterarbeit**, keine Bewertung.

## Grenzen (verbindlich)
- **Nicht** für Auswahlverfahren/Stellenbesetzung, dienstliche Beurteilungen oder die
  Benotung von Prüfungsunterricht (Hochrisiko nach KI-VO; `references/leitplanken-bewertung.md`).
  Bei solchen Anfragen freundlich ablehnen und auf menschliche Begutachtung verweisen.
- **Prüfungsrelevante Entwürfe** (Prüfungsunterricht und Entwürfe, die in eine Note oder
  Beurteilung eingehen): nur **Selbstcheck** durch die Autorin bzw. den Autor, und zwar
  **gekennzeichnet** (Entscheidung der Fachberatung, 19.10.2026):
  - Kopf `pruefungsrelevant: true`, Regelcheck mit `--pruefung`;
  - **Hinweise statt fertiger Formulierungen** – Stelle, was fehlt, warum, eine Frage; der
    Entwurf bleibt Eigenleistung;
  - Abschnitt *Kennzeichnung der KI-Nutzung* mit Text zum Einfügen in den Entwurf
    (Hilfsmittelangabe); die Regeln des Studienseminars zur KI-Nutzung haben Vorrang.
  - Im Zweifel als prüfungsrelevant behandeln (`⚠️ Annahme:`). Kein Modus Beratung.
- Kollegiale Beratung nur mit **Zustimmung** der Autorin bzw. des Autors des Entwurfs.
- **Keine Niveaustufen, keine Note, kein Ranking** – nur Stärken, Entwicklungsfelder, Fragen.
- Schülerdaten (Schülerliste, kommentierter Sitzplan) **vorher entfernen**; das Skript warnt.
- Begriffe und Kompetenzmodell nach **SchuCu-BBS 2024** (Fach- und Personale Kompetenz, sechs
  Phasen). Eine eigene Gliederung des Studienseminars darf gelten; Kriterien aus Vorgaben anderer
  Länder werden nicht übernommen.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` · nichts erfinden · Kopf und
Pflichtabschnitte nach `references/skill-vertrag.md`. Jeder Befund mit **wörtlichem Beleg**.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht:** der Entwurf (PDF, DOCX, ODT, Markdown).
- **Optional:** Modus (Selbstcheck = Standard, kollegiale Beratung), Entwurfstyp (UB, PU,
  Alltagsentwurf), prüfungsrelevant ja/nein, Vorgaben des Studienseminars/der Schule (haben
  Vorrang), Lernsituation.

## Vorgehen
1. **Datenschutz:** Enthält der Entwurf Schülerdaten? Dann zuerst Anhang entfernen lassen oder
   `python3 scripts/text_anonymisieren.py ENTWURF --klassenliste klasse.txt` (lokal) – weiter mit
   der anonymisierten Fassung. **Prüfungsrelevant?** Anlass und Entwurf lesen (Prüfungsunterricht,
   bewerteter Unterrichtsbesuch) – dann gelten die Grenzen oben.
2. **Indikatoren-Check (lokal):** `python3 scripts/entwurf_regelcheck.py ENTWURF.pdf --typ A|K|S`
   (prüfungsrelevant zusätzlich `--pruefung`: prüft die Kennzeichnung der KI-Nutzung)
   → je Kriterium erkennbare und nicht gefundene Bestandteile, fehlende Phasen der
   vollständigen Handlung, nicht beobachtbare Zielverben. „Nicht gefunden" heißt „nachsehen",
   nicht „fehlt". Bei Kurzentwurf (K) oder Sequenz (S) führt das Skript Bestandteile, die nur
   der ausführliche Entwurf verlangt (Lernausgangslage, Sachanalyse, Anlagenverzeichnis …), als
   „nicht verlangt"; eine Doppelstunde muss nicht alle sechs Phasen enthalten.
3. **Inhaltlicher Selbstcheck** je Kriterium nach `references/kriterien-entwurf.md`: Stärken
   und Entwicklungsfelder, jeweils mit wörtlichem Zitat und Seitenangabe; zu jedem
   Entwicklungsfeld 1–2 Fragen aus `references/reflexionsfragen.md`. Für A9 die didaktische
   Leitidee an den fünf Kriterien aus `references/didaktische-leitidee.md` messen; fehlt sie,
   als Entwicklungsfeld mit Reflexionsfrage aufnehmen (prüfungsrelevant: keinen Vorschlag
   formulieren).
4. **Checkliste vor der Abgabe** (`references/checkliste-vor-abgabe.md`) mit ✅/⚠️ abarbeiten.
5. **Überarbeitungsvorschläge**: höchstens fünf.
   - Sonst: als fertige Formulierungen (z. B. neues Stundenziel, ergänzte Phase im
     Verlaufsplan) – als Blockzitat (`> …`), damit die Zitatprüfung sie nicht für Belege hält.
   - **Prüfungsrelevant:** nur Hinweise – Stelle, was fehlt oder unklar ist, warum es zählt,
     eine Reflexionsfrage; keine einsetzbaren Sätze, Tabellenzeilen oder Ziele.
6. **Kennzeichnung (nur prüfungsrelevant):** Abschnitt *Kennzeichnung der KI-Nutzung* der Vorlage
   ausfüllen (KI-System, Skill und Version, Datum, Art der Nutzung) und den Checklistenpunkt
   „KI-Nutzung gekennzeichnet" prüfen.
7. **Belege prüfen:** `python3 scripts/zitate_pruefen.py 35_entwurfscheck_….md ENTWURF.pdf` –
   nicht belegte Zitate korrigieren oder streichen.
8. **Modus Beratung** (nicht bei prüfungsrelevanten Entwürfen): zusätzlich Gesprächsvorlage nach
   `references/kollegiale-beratung.md` (Stärken, max. drei Schwerpunkte, Raum für Vereinbarungen
   und Stellungnahme).

## Ausgabe
`35_entwurfscheck_<kurztitel>.md` nach `assets/vorlage-selbstcheck.md`.

## Qualitätscheck
- [ ] Keine Note, keine Niveaustufe, keine Personenbewertung im Text?
- [ ] Jeder Befund mit wörtlichem Zitat, Zitate mit Skript geprüft?
- [ ] Stärken mindestens so konkret wie Entwicklungsfelder?
- [ ] Höchstens drei Entwicklungsschwerpunkte hervorgehoben?
- [ ] Zeichnungen aus Zeichen im Entwurf (Tafelbild, Ablauf) als Hinweis genannt – `python3 scripts/zeichnungen_pruefen.py`
      auf der Markdown- bzw. Textfassung; der Selbstcheck selbst enthält keine?
- [ ] Vorschläge als einsetzbare Formulierungen – bzw. bei prüfungsrelevanten Entwürfen nur als Hinweise?
- [ ] Prüfungsrelevant: Kopf `pruefungsrelevant: true`, Regelcheck mit `--pruefung`, Kennzeichnung ausgefüllt?
- [ ] Schülerdaten nicht verarbeitet bzw. vorher entfernt?

## Beispielaufrufe
> „Selbstcheck für meinen UB-Entwurf (Anhang), Industriemechaniker 1. Jahr, 90 Minuten."

> „Das ist mein Entwurf für den Prüfungsunterricht – ist er vollständig? Ich kennzeichne die
> KI-Nutzung."

> „Bereite ein kollegiales Beratungsgespräch zu diesem Entwurf vor – die Kollegin ist
> einverstanden."

## Übergabe
Nach der gehaltenen Stunde: Reflexion bzw. Nachbesprechung mit `unterricht-reflektieren`
(vergleicht Plan und Verlauf, nutzt diesen Entwurfscheck).

## Referenzen – wann lesen
- `references/kriterien-entwurf.md` – **immer** (A1–A11, typische Entwicklungsfelder).
- `references/didaktische-leitidee.md` – A9: Kriterien, Abgrenzung, typische Fehler der Leitidee.
- `references/reflexionsfragen.md`, `references/checkliste-vor-abgabe.md` – Schritt 3–4.
- `references/kollegiale-beratung.md` – Modus Beratung.
- `references/schucu-bbs-2024.md` – Phasen, Begriffe.
- `references/operatoren-afb.md` – Zielformulierungen.
- `references/leitplanken-bewertung.md`, `references/skill-vertrag.md` – Grenzen und Format.
- `scripts/entwurf_regelcheck.py`, `scripts/zitate_pruefen.py`, `scripts/text_anonymisieren.py` – lokal.
