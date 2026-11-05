---
name: unterrichtsentwurf-erstellen
description: Erstellt schriftliche Unterrichtsentwürfe für berufsbildende Schulen – vom kompakten Alltagsentwurf bis zum ausführlichen Entwurf für Unterrichtsbesuch oder Prüfungsunterricht (Studienseminar) – mit curricularer und didaktischer Einordnung, Lernausgangslage, Sachanalyse mit Reduktionsentscheidungen, didaktischer Leitidee und kompetenzorientiertem Stundenziel (Fach- und Personale Kompetenz), didaktisch-methodischen Begründungen, Verlaufsplan entlang der vollständigen Handlung, Sollbruchstelle, Lehrerhinweisen und Anhang mit Material und Erwartungshorizont – auch als reiner Stundenverlaufsplan oder als Sequenz mehrerer Stunden mit Methodenvarianz. Verwenden, wenn eine konkrete Unterrichtsstunde, Doppelstunde (45/90 Minuten) oder Unterrichtssequenz aus einer Lernsituation oder einem Thema geplant und begründet werden soll, bei „Stundenverlaufsplan", „Verlaufsplanung", „Stunde planen", für Unterrichtsbesuche, Lehrproben, Hospitationen oder als Vorlage für Kolleginnen und Kollegen.
metadata:
  version: "1.12"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  ersetzt: "verlaufsplanung-erstellen 1.x (eduwerkzeuge)"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Unterrichtsentwurf erstellen

## Zweck
Eine einzelne Stunde (oder Doppelstunde) so planen und **begründen**, dass andere den Plan
nachvollziehen, durchführen und beurteilen können – eingebettet in die Lernsituation und die
vollständige Handlung.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Entwurfstypen – Umfang wählen

| Typ | Anlass | Umfang |
|---|---|---|
| **K Kurzentwurf / Stundenverlaufsplan** (Standard) | Alltagsplanung, Vertretung, Weitergabe an Kollegium | Rahmen, Leitidee und Stundenziel, Verlaufsplan mit Begründungsspalte, Sollbruchstelle, Lehrerhinweise, Material/Erwartungshorizont |
| **S Sequenz** | mehrere Stunden einer Lernsituation (z. B. eine Phase der vollständigen Handlung) | Sequenzübersicht mit Methodenvarianz + je Stunde ein Verlaufsplan Typ K (kompakt) |
| **A Ausführlicher Entwurf** | Unterrichtsbesuch, Prüfungsunterricht, Hospitation | vollständige Gliederung nach `assets/vorlage-unterrichtsentwurf.md` (Abschn. 1–3 + Anhang) |

Hat das Studienseminar oder die Schule eine eigene Gliederung, **gilt diese** (Datei hochladen
lassen); die Inhalte dieses Skills werden dann darauf abgebildet. Begriffe und Kompetenzmodell
bleiben die der SchuCu-BBS 2024 (Fach- und Personale Kompetenz, sechs Phasen).

> **Prüfungsrelevante Entwürfe:** Für Lehrkräfte im Vorbereitungsdienst sind Entwürfe
> bewertete Eigenleistungen. Der Skill weist darauf hin, die Regeln des Studienseminars zur
> KI-Nutzung und zur Selbständigkeitserklärung zu beachten, und liefert den Entwurf als
> **Arbeitsgrundlage**, die eigenständig zu überarbeiten ist. Den fertigen eigenen Entwurf
> darf die Lehrkraft mit `unterrichtsentwurf-analysieren` prüfen – als gekennzeichneter
> Selbstcheck (Leitplanke); die KI-Nutzung gibt sie im Entwurf als Hilfsmittel an.

## Eingaben
- **Pflicht (sonst Rückfrage):** Thema **oder** Lernsituation; Bildungsgang/Beruf.
- **Wichtig, sonst Annahme:** Dauer (45/90 min), Position der Stunde in der LS und Phase(n)
  der vollständigen Handlung, Lerngruppe (Größe, Vorwissen, Heterogenität, Sprache),
  Raum/Medien, Entwurfstyp.
- **Optional:** Lernsituation (z. B. `20_lernsituation_*.md`), Ordnungsmittel-Auszug,
  vorhandenes Material, Planungsakte, Vorgaben des Studienseminars.

## Vorgehen

1. **Einbettung klären.** Welche Phase(n) der vollständigen Handlung deckt die Stunde ab?
   Welche liegen davor/danach? (Der Handlungskreis muss nicht in einer Stunde geschlossen
   werden – aber der Bezug muss sichtbar sein.)
2. **Leitidee und Stundenziel zuerst** („vom Ende her"):
   - **Didaktische Leitidee der Stunde:** ein bis zwei Sätze, welche übertragbare Einsicht die
     Lernenden an diesem Schritt der Handlungssituation gewinnen und warum sie bedeutsam ist –
     abgeleitet aus der Leitidee der Lernsituation (Planungsakte `leitidee_ls`, LS unter
     *didaktisch-methodische Kommentare*; fehlt sie, mitformulieren). Muster, Kriterien,
     Beispiele: `references/didaktische-leitidee.md`. Sie ergänzt das Stundenziel, ersetzt es nicht.
   - **Stundenziel:** genau **ein** überprüfbares Hauptziel, das die Leitidee operationalisiert,
     formuliert nach Muster `Die SuS [Operator] [Inhalt], indem sie [beobachtbare Handlung].` – je
     eine Formulierung für Fachkompetenz (FK) und Personale Kompetenz (PK); weitere nur bei
     Bedarf. Muster und Beispiele: `references/stundenziele.md`. Woran wird das Erreichen am
     Stundenende sichtbar? → Stundenergebnis festlegen; Sicherung oder Reflexion greift die
     Leitidee auf.
3. **Sachanalyse und Reduktion.** Sachstruktur als Mindmap (eingerückte Liste oder
   Strukturbild als SVG mit `fachdiagramm-erstellen`), Auswahl ✔ und bewusste Reduktion ✂ markieren und begründen. Fachlich
   exakt; Werte und Normen prüfen oder markieren.
4. **Verlauf planen** – Grundrhythmus Einstieg → Erarbeitung → Sicherung → (Reflexion/Transfer),
   verankert in der vollständigen Handlung. Verbindlich (`references/leitfragen-planung.md`):
   - Einstieg aktiviert **Vorwissen** und öffnet das Problem (≤ 10 % der Zeit); zentrale
     Impulse **wörtlich** notieren, erwartete SuS-Antworten skizzieren.
   - **Kein Lehrkraftinput länger als 15–20 min am Stück**; auf Input folgt Erprobung. Das gilt
     auch für begründete fachsystematische Phasen (Entscheidung der Fachberatung 23.10.2026:
     Lernzeit effizient nutzen, `references/lernsituationsmuster.md` Abschn. 12): lieber
     mehrere kurze Inputs mit Anwendung dazwischen als ein langer.
   - Erarbeitung ist der **größte Block**; Arbeitsauftrag mit Operator, Sozialform, Zeit,
     Ergebnisform; Differenzierung (Hilfen, Erweiterung) benannt.
   - **Sicherung nie kürzen**; Ergebnis sichtbar (Tafelbild, Plakat, Protokoll, LMS).
   - Mindestens ein kognitiv aktivierender Impuls auf Stufe Analysieren/Bewerten/Erschaffen.
   - ca. **10 % Puffer**; **Sollbruchstelle** markieren (was entfällt bei Zeitnot – nie die
     Sicherung); didaktische Reserve für schnelle Gruppen.
   - **Kernweg ausweisen:** Minutensumme dessen, was alle in der Stunde schaffen müssen
     (Richtwert 60–65 min je Doppelstunde). Alles darüber trägt eine Kennzeichnung – *Zusatz*
     (Differenzierung nach oben), *wenn Zeit bleibt* (Reserve, ggf. Hausaufgabe), *Praxischeck*
     (Transfer in den Ausbildungsbetrieb).
   - Lehrkraftvortrag insgesamt in der Regel ≤ 25 % der Zeit; mehr nur als begründete
     fachsystematische Phase (Alltagsentwurf, Sequenz) – **nicht im Typ A** für Unterrichtsbesuch
     und Prüfungsunterricht, dort gelten die Kriterien der Fachberatung (z. B. überwiegend
     aktive Lernzeit). Mindestens drei Sozialformwechsel je Doppelstunde, jeder begründet.
     Einstieg einer Lernsituation induktiv (Fall, Bild, Widerspruch, Zahl) – nie eine Definition;
     Folgestunden dürfen mit einem kurzen Input beginnen, wenn er an das offene Problem anknüpft.
     Methodenauswahl: `references/methodenrepertoire.md`.
5. **Begründen.** Für jede Phase: Warum diese Methode/Sozialform/dieses Medium für dieses
   Ziel und diese Lerngruppe? Alternativen kurz abwägen (bes. Entwurfstyp A). Bei Typ A auch
   die Bedeutsamkeit (Gegenwart, Zukunft), Exemplarität und Zugänglichkeit des Gegenstands
   begründen (`references/leitfragen-planung.md` Abschn. 1); sind weitere Erwachsene im
   Unterricht, ihre Rollen je Phase festhalten.
   **Lehrerhinweise** ergänzen: Kernweg in Minuten, Stolpersteine und Moderation (typische
   Fehlvorstellungen, Gelenkstellen), Differenzierung, Anschluss an Vorstunde und Folgestunde.
   **KI-Einsatz in der Stunde**, wo Lernende KI nutzen könnten: je Phase 🚫 Ohne KI · 💡 KI zum
   Verstehen · 🔧 Mit KI arbeiten mit einem Satz Begründung, der das Stundenziel nennt – auch
   die Phasen *ohne* KI (`references/ki-vereinbarungen.md`).
6. **Material und Erwartungshorizont** (Anhang): Arbeitsauftrag mit Operatoren, Hilfekarten,
   Tafelbild, Lösung/Erwartung. Was Lernende bekommen, ist kurz, offen gestellt, anschaulich und
   ohne Dekoration (`references/schuelermaterial.md`): Arbeitsauftrag in ein bis zwei Sätzen
   mit Ergebnis statt Schrittfolge, Tafelbild als Struktur- oder Ablaufbild (SVG mit
   `fachdiagramm-erstellen`, nie als Zeichnung aus Zeichen). Wenn ein eigenes
   Materialpaket nötig ist, Übergabe an `unterrichtsmaterial-erstellen` empfehlen und im Anhang
   den Platz vorsehen.
7. **Prüfen**: Zeitsumme, Zielbezug jeder Phase, Checkliste unten; Anhang für Lernende mit
   `python3 scripts/schuelermaterial_pruefen.py 30_unterrichtsentwurf_….md`, Zeichnungen im ganzen Entwurf
   (auch Tafelbild, Lösung) mit `python3 scripts/zeichnungen_pruefen.py 30_unterrichtsentwurf_….md`; Mängel beheben.

**Typ S – Sequenz:** zuerst die Leitidee der Sequenz bzw. Lernsituation, dann die
Sequenzübersicht (Stunde · Thema · Stundenziel · Phase der
vollständigen Handlung · Einstieg · Erarbeitungsmethode · Sicherung · Sozialformen ·
Ergebnis). Varianzregeln aus `references/methodenrepertoire.md` Abschn. 2 einhalten (kein
Einstiegstyp zweimal hintereinander, mindestens drei Erarbeitungsmethoden, eine kooperative
Großform). Dann je Stunde Schritte 2–7 in Kurzform.
**Projekt-Lernsituationen (20–60 h, z. B. Berufliches Gymnasium mit Lastenheft):** Die Sequenz
folgt den Meilensteinen statt Einzelstunden – Kickoff (Lastenheft analysieren, Fragen an den
Auftraggeber), Planung mit Pflichtenheft und Projektplan, Meilenstein-Gespräche (Entscheidungen
freigeben), Arbeitsphasen mit kurzen Stand-ups, Zwischenpräsentation bzw. Peer-Review,
Fachgespräch je Arbeitspaket, Präsentation des Handlungsergebnisses, Retrospektive. Voll
ausgeplant (Typ K) werden nur Kickoff, Meilensteine und Präsentation; Arbeitsphasen erhalten
Ziel, Ergebnis und Hilfen. Muster: `references/lernsituationsmuster.md` Abschn. 9–11; BG-Rahmen
(Lerngebiet, Schuljahrgang, 45-/90-Minuten-Blöcke, Fach Praxis):
`references/berufliches-gymnasium.md`.

**Werkzeuge an passenden Phasen (optional, Skills mit mitgelieferten `eduwerkzeuge`):**
Sicherungsquiz (`quizfragen-erstellen`), Diagramme (`fachdiagramm-erstellen`), Stundenablauf
als Zeitstrahl oder Lernlandkarte in edumaps (`lernlandkarte-erstellen`), Schülerseiten je
Phase (`schuelerseiten-veroeffentlichen`);
nach Leistungsdaten differenzieren (Notenspiegel/Klassenbericht → `differenzierung-erstellen`).
**Nach der Stunde:** Plan und Verlauf vergleichen, Nachbesprechung vorbereiten →
`unterricht-reflektieren`; dessen Konsequenzen fließen in die Folgestunde.

## Ausgabe
Datei `30_unterrichtsentwurf_<datum-oder-stunde>_<kurzthema>.md`, Kopf nach Skill-Vertrag.
- **Typ K:** Abschnitte *Rahmen · Leitidee und Stundenziel · Verlaufsplan · Sollbruchstelle und Reserve ·
  Material und Erwartungshorizont* aus der Vorlage.
- **Typ S:** Sequenzübersicht + je Stunde Typ K in einer Datei
  `30_sequenz_<phase-oder-thema>.md`.
- **Typ A:** vollständige Vorlage `assets/vorlage-unterrichtsentwurf.md`.
Verlaufstabelle immer mit den Spalten *Zeit | Unterrichtsphase und -geschehen (L/SuS) |
Phase der vollständigen Handlung | Aktions- und Sozialform | Medien/Material |
Didaktisch-methodische Begründung*.
Schülerdaten **nie** von der KI ausfüllen lassen – Platzhalter für die Lehrkraft.

## Qualitätscheck
- [ ] Leitidee der Stunde in ein bis zwei Sätzen (exemplarisch, bedeutsam, passend zur Leitidee der LS) – kein Thema, kein zweites Ziel?
- [ ] Genau ein Hauptziel, überprüfbar, mit Operator, operationalisiert die Leitidee; FK und PK; kein „verstehen"?
- [ ] Stundenergebnis benannt und in der Sicherung sichtbar; Sicherung oder Reflexion greift die Leitidee auf?
- [ ] Bezug zur Phase der vollständigen Handlung und zur LS ausgewiesen?
- [ ] Einstieg aktiviert Vorwissen; Impulse wörtlich; erwartete Antworten?
- [ ] Kein Input > 20 min; Erarbeitung größter Block; Sicherung vollständig?
- [ ] Mind. ein Impuls auf Taxonomiestufe 4–6?
- [ ] Differenzierung konkret (nicht nur „Hilfekarten bei Bedarf")?
- [ ] Zeitsumme = Dauer − Puffer; Sollbruchstelle markiert; Kernweg ausgewiesen?
- [ ] Lehrerhinweise (Stolpersteine, Anschluss) vorhanden?
- [ ] KI-Einsatz je Phase festgelegt und begründet (auch Phasen ohne KI), Entscheiden/Überprüfen/Reflektieren bei den Lernenden?
- [ ] Typ S: Einstiege und Erarbeitungsmethoden variieren, kooperative Großform vorhanden?
- [ ] Projekt-Sequenz: Kickoff, Meilensteine mit Entscheidung, Fachgespräch je Arbeitspaket, Präsentation und Retrospektive eingeplant?
- [ ] Jede Methoden-/Medienentscheidung begründet?
- [ ] Typ A: Bedeutsamkeit und Exemplarität begründet; Rollen weiterer Erwachsener benannt (falls beteiligt)?
- [ ] Fachlich geprüft oder als Prüfauftrag markiert; Quellen echt?
- [ ] Material für Lernende im Anhang kurz, offen gestellt, mit Darstellung (`schuelermaterial_pruefen.py` ohne ❌)?
- [ ] Tafelbild und Lösungsbilder als SVG aus Spec, keine Zeichnung aus Zeichen (`zeichnungen_pruefen.py` ohne ❌)?

## Beispielaufrufe
> „Ausführlicher Unterrichtsentwurf (UB) für 90 min aus `20_lernsituation_gurtfoerderer.md`,
> Phase Planen: Arbeitsplan für die Wartung erstellen. Klasse IM1b, 21 SuS, zwei SuS mit
> Deutsch als Zweitsprache."

> „Kurzentwurf 45 min: Einführung Toleranzen und Passungen, Zerspanungsmechaniker 1. Jahr."

> „Plane die Phase Planen der LS als Sequenz von drei Doppelstunden – mit wechselnden
> Einstiegen und einem Gruppenpuzzle."

## Referenzen – wann lesen
- `assets/vorlage-unterrichtsentwurf.md` – Ausgabeformat (Typ A vollständig, Typ K Auszug).
- `references/leitfragen-planung.md` – Leitfragen je Abschnitt (Bedeutsamkeit, Exemplarität, Zugänglichkeit, Team) und Wirksamkeitsprinzipien.
- `references/didaktische-leitidee.md` – Leitidee der Stunde und der Lernsituation: Abgrenzung zu den Begriffen der Leitlinie, Muster, Kriterien, Beispiele, typische Fehler.
- `references/schuelermaterial.md` – was ins Material für Lernende geht: kurz, offen gestellt, anschaulich, ohne Dekoration.
- `references/stundenziele.md` – Zielmuster, gute und schlechte Beispiele.
- `references/ki-vereinbarungen.md` – KI-Phasen und Zeichen je Phase, Begründungsmuster („Heute ohne KI, weil …").
- `references/methodenrepertoire.md` – Methodenfamilien je Phase, Varianzregeln, Transferauftrag in den Betrieb bzw. in die Lebenswelt, Kugellager, Projektmethoden.
- `references/berufliches-gymnasium.md` – Berufliches Gymnasium: Lerngebiet, Schuljahrgang, Projekte, Fach Praxis.
- `references/lernsituationsmuster.md` – Stunden in einer Diagnose-Lernsituation und in den
  Phasen Entscheiden, Überprüfen und Reflektieren; Lernhürden für die Lehrerhinweise.
- `references/schucu-bbs-2024.md` – Phasen der vollständigen Handlung, Lehrkraftrolle.
- `references/operatoren-afb.md` – Operatoren für Ziele und Aufträge.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
