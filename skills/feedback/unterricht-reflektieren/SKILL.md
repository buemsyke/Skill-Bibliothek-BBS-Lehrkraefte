---
name: unterricht-reflektieren
description: Unterstützt Lehrkräfte an berufsbildenden Schulen, nach einer gehaltenen Stunde oder Sequenz strukturiert zu reflektieren – zur Vorbereitung der Nachbesprechung eines Unterrichtsbesuchs oder Prüfungsunterrichts, nach kollegialer Hospitation oder für die eigene Unterrichtsentwicklung nach SchuCu-BBS 2024. Vergleicht Planung und Verlauf mit Minuten je Phase, schätzt die Zielerreichung an beobachtbaren Belegen ein, betrachtet Entscheidungen, Lernbegleitung, Heterogenität und die Phasen der vollständigen Handlung, nennt Alternativen, Konsequenzen für die Folgestunde und Fragen zur Vertiefung. Höchstens drei Schwerpunkte – ohne Note, Niveaustufe oder Urteil über Personen, Lernende nur als Lerngruppe. Verwenden bei „Stunde reflektieren“, „Nachbesprechung vorbereiten“, „Reflexion nach dem UB“, „was lief anders als geplant?“. Den Entwurf vor der Stunde prüft unterrichtsentwurf-analysieren. Prüfungsunterricht nur zur eigenen Vorbereitung und gekennzeichnet.
metadata:
  version: "1.4"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: pruefen
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Unterricht reflektieren (Selbstreflexion und Nachbesprechung)

## Zweck
Nach dem Unterricht aus Plan, Verlauf und Beobachtungen eine **Reflexion mit Schwerpunkten**
machen: Was hat beim Lernen gewirkt, was lief anders als geplant und warum, was folgt für die
nächste Stunde? Die Leitlinie SchuCu-BBS 2024 nennt das „Unterricht durchführen und evaluieren“.
Ergebnis ist eine **Grundlage zur eigenen Weiterarbeit** – keine Bewertung.

## Grenzen (verbindlich)
- **Nicht** für Auswahlverfahren, dienstliche Beurteilungen oder die Benotung von
  Prüfungsunterricht (`references/leitplanken-bewertung.md`); keine Note, keine Niveaustufe, kein
  Urteil über Personen.
- **Prüfungsunterricht** (`pruefungsrelevant: true`): nur **Modus A** zur eigenen Vorbereitung,
  als **Stichpunkte** – die Reflexion in der Prüfung trägt die Lehrkraft selbst vor. Wird etwas
  Schriftliches eingereicht, die KI-Nutzung **kennzeichnen** (Abschnitt in der Vorlage). Keine
  KI-vorbereitete Nachbesprechung mit Beobachtungen Dritter.
- **Lernende nur als Lerngruppe oder in Anzahlen:** keine Namen, Initialen oder Pseudonyme, keine
  Gesundheits-, Förder- oder Herkunftsangaben zu Einzelnen, keine Einzelarbeiten oder Abgaben
  hochladen (Leitplanke „Lernstände nur für die Lerngruppe“).
- **Modus B** nur mit Zustimmung der hospitierten Lehrkraft; Beobachtungen beschreiben, nicht
  urteilen (`references/kollegiale-beratung.md`).
- Begriffe nach SchuCu-BBS 2024 (Fach- und Personale Kompetenz, sechs Phasen der vollständigen
  Handlung, Handlungssituation, Handlungsergebnis).

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` · nichts erfinden, Unsicheres als `🔎 Prüfen:` ·
Kopf und Pflichtabschnitte nach `references/skill-vertrag.md`. Jede Einschätzung mit Beleg aus den
gelieferten Unterlagen – was nicht belegt ist, wird als Frage formuliert.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Modi
| Modus | Anlass | Ergebnis |
|---|---|---|
| **A Selbstreflexion** (Standard) | eigene Stunde, vor der Nachbesprechung eines Unterrichtsbesuchs, Vorbereitung auf den Prüfungsunterricht | Schwerpunkte, Plan und Verlauf, Zielerreichung, R4–R8 als Stichpunkte, Fragen zur Vertiefung |
| **B Nachbesprechung** | kollegiale Hospitation, Teamteaching, Unterrichtsbesuch in Beratung | wie A plus Gesprächsvorlage: Lehrkraft zuerst, Beobachtungen der Hospitierenden, vereinbarte Schwerpunkte, Stellungnahme |

## Eingaben
- **Pflicht:** was geplant war (Entwurf `30_…`, Verlaufsplan oder kurze Beschreibung mit Ziel und
  Phasen) **und** was geschah (Notizen der Lehrkraft: Zeiten, Abweichungen, Ergebnisse,
  Beobachtungen).
- **Optional:** Entwurfscheck `35_…`, Stundenergebnis der Lerngruppe (ohne Namen),
  zusammengefasste Rückmeldung der Lerngruppe,
  Beobachtungen der Hospitierenden (Modus B),
  Wünsche der Lehrkraft zu Schwerpunkten, Anlass (prüfungsrelevant ja/nein).

## Vorgehen
1. **Datenschutz und Anlass.** Notizen mit Namen zuerst lokal bereinigen
   (`python3 scripts/text_anonymisieren.py NOTIZEN.md --klassenliste klasse.txt`) und
   Beobachtungen auf die Lerngruppe bzw. Anzahlen umstellen. Prüfungsunterricht? → Kopf
   `pruefungsrelevant: true`, nur Modus A.
2. **Gerüst aus dem Entwurf:** `python3 scripts/reflexion_pruefen.py --geruest 30_unterrichtsentwurf_….md`
   → Tabelle *Plan und Verlauf* mit den geplanten Minuten. Die tatsächlichen Minuten, Gründe und
   Wirkungen kommen aus den Notizen. Ohne Entwurf: Phasen aus der Beschreibung (`⚠️ Annahme:`).
3. **Schwerpunkte wählen** (höchstens drei; Wünsche der Lehrkraft zuerst, sonst nach Bedeutung für
   das Stundenziel). Gesamteindruck in ein bis zwei Sätzen.
4. **R2–R8 ausarbeiten** nach `references/reflexionsleitfaden.md`: je Schwerpunkt beschreiben →
   deuten → begründen → folgern; Stärken zuerst; Zielerreichung je Ziel mit *ja · teilweise ·
   nein · offen* und beobachtbarem Beleg, ebenso eine Zeile zur **didaktischen Leitidee** der
   Stunde (eingelöst? getragen? – `references/didaktische-leitidee.md` Abschn. 7; fehlt sie im
   Entwurf, nachträglich festhalten); Abweichungen ab fünf Minuten mit Grund; mindestens eine
   begründete Alternative; Konsequenzen konkret (Folgestunde: was, wann, wie).
5. **Fragen zur Vertiefung:** drei bis fünf aus `references/vertiefungsfragen.md`, passend zu den
   Schwerpunkten – mit Stichworten, worauf eine Antwort eingeht, ohne Musterantworten.
6. **Modus B:** Gesprächsvorlage nach `references/kollegiale-beratung.md` ergänzen.
   **Prüfungsrelevant:** Abschnitt *Kennzeichnung der KI-Nutzung* ausfüllen.
7. **Prüfen:** `python3 scripts/reflexion_pruefen.py 36_reflexion_….md` (rechnet Minuten nach,
   prüft Belege, Schwerpunkte, Datenschutz, Kennzeichnung) – jedes ❌ beheben; Belege mit
   `python3 scripts/zitate_pruefen.py 36_reflexion_….md NOTIZEN.md 30_unterrichtsentwurf_….md`
   (wörtliche Belege in „…" und in einer Zeile; eigene Vorschläge *kursiv*, nicht in
   Anführungszeichen).

## Ausgabe
`36_reflexion_<datum-oder-stunde>_<kurzthema>.md` nach `assets/vorlage-reflexion.md`.
Prüfungsunterricht: Stichpunkte statt ausformulierter Sätze.

## Qualitätscheck
- [ ] `reflexion_pruefen.py` ohne ❌; Minuten und Summen gerechnet, nicht geschätzt?
- [ ] Verlauf als Tabelle, keine Zeichnung aus Zeichen (`python3 scripts/zeichnungen_pruefen.py 36_reflexion_….md` ohne ❌)?
- [ ] Höchstens drei Schwerpunkte; Stärken mindestens so konkret wie Entwicklungsfelder?
- [ ] Jede Einschätzung mit beobachtbarem Beleg, Zitate mit `zitate_pruefen.py` geprüft?
- [ ] Didaktische Leitidee der Stunde eingeschätzt (eingelöst, getragen, Folgerung)?
- [ ] Vom Lernen der Lerngruppe her gedacht – nicht nur das eigene Handeln?
- [ ] Mindestens eine begründete Alternative und konkrete Konsequenzen für die Folgestunde?
- [ ] Keine Namen, Initialen, Pseudonyme; keine Note, keine Niveaustufe?
- [ ] Prüfungsrelevant: Modus A, Stichpunkte, Kennzeichnung ausgefüllt?

## Beispielaufrufe
> „Ich hatte heute meinen UB zur LS 4.2 (Entwurf anbei), hier meine Notizen. Bereite meine
> Reflexion für die Nachbesprechung vor – Schwerpunkt Zeit in der Erarbeitung."

> „Nächste Woche ist mein Prüfungsunterricht. Hilf mir, nach der Generalprobe die Reflexion zu
> üben – in Stichpunkten, ich kennzeichne die KI-Nutzung."

> „Mein Kollege hat bei mir hospitiert und ist einverstanden – hier seine Beobachtungen. Bereite
> die Nachbesprechung vor."

## Übergabe
Konsequenzen für die Folgestunde → `unterrichtsentwurf-erstellen`; Differenzierungsbedarf →
`differenzierung-erstellen`; Material überarbeiten → `unterrichtsmaterial-erstellen`; vor dem
nächsten Entwurf → `unterrichtsentwurf-analysieren`.

## Referenzen – wann lesen
- `references/reflexionsleitfaden.md` – **immer** (Grundsätze, R1–R8, Belege, Stolpersteine, Datenschutz, Anlässe).
- `references/vertiefungsfragen.md` – Schritt 5.
- `references/didaktische-leitidee.md` – Leitidee der Stunde einschätzen (Prüffragen nach dem Unterricht).
- `references/kollegiale-beratung.md` – Modus B.
- `references/schucu-bbs-2024.md` – Phasen, Rollen der Lehrkraft, Planungsschritt „Unterricht durchführen und evaluieren“.
- `references/leitplanken-bewertung.md`, `references/skill-vertrag.md` – Grenzen und Format.
- `scripts/reflexion_pruefen.py`, `scripts/zitate_pruefen.py`, `scripts/text_anonymisieren.py`,
  `scripts/text_lesen.py` – lokal.
