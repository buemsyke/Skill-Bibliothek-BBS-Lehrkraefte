<!-- Assistenten-Fassung des Skills 'unterrichtsentwurf-erstellen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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

# ANHÄNGE

## Anhang: assets/vorlage-unterrichtsentwurf.md

---
artefakt: Unterrichtsentwurf
titel: "[Thema der Stunde]"
skill: unterrichtsentwurf-erstellen
skill_version: "1.12"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld mit Titel]"
dqr: 0
entwurfstyp: "K | S | A"
status: "KI-Entwurf – fachlich zu prüfen"
---

# Unterrichtsentwurf: [Thema der Stunde]

<!-- Typ K (Kurzentwurf/Stundenverlaufsplan): nur die mit (K) markierten Abschnitte ausfüllen.
     Typ S (Sequenz): zuerst „Sequenzübersicht (S)", dann je Stunde die (K)-Abschnitte. -->

## Rahmen (K)

| Feld | Eintrag |
|---|---|
| Entwurfstyp | [Alltagsentwurf / kurzer UB / ausführlicher UB / Prüfungsunterricht] |
| Klasse | [Kurzbezeichnung] · [Anzahl] SuS |
| Bildungsgang / Schulform | |
| Fach / Lernfeld bzw. Lerngebiet | [Nr. und Titel laut Ordnungsmittel; BG: Lerngebiet, Schuljahrgang/Phase] |
| Lernsituation | [Nr. und Titel, Stunde x von y] |
| DQR-Niveau | |
| Datum, Zeit, Raum | [von der Lehrkraft] |
| Dauer | [45 / 90] Minuten |
| Phase(n) der vollständigen Handlung | [z. B. Planen, Entscheiden]; vorher: …; danach: … |
| Weitere Erwachsene im Unterricht | [falls beteiligt: Doppelbesetzung, Schulbegleitung, Sozialpädagogik – Rolle je Phase; sonst entfällt] |

## Sequenzübersicht (S)

**Leitidee der Sequenz bzw. Lernsituation:** [1–2 Sätze – `didaktische-leitidee.md`]

| Stunde | Thema | Stundenziel (Kurzform) | Phase der vollst. Handlung | Einstieg | Erarbeitung | Sicherung | Sozialformen | Ergebnis |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |

*Varianz:* kein Einstiegstyp zweimal hintereinander · ≥ 3 Erarbeitungsmethoden · ≥ 1 kooperative Großform.

## 1 Planung der Lernsituation (A)

### 1.1 Analyse der Rahmenbedingungen

#### 1.1.1 Curriculare und (fach-)didaktische Einordnung
[Ordnungsmittel und Kompetenzerwartungen, schulisches Curriculum, DQR-Anforderungen,
Bedeutsamkeit (Gegenwart im Betrieb bzw. in der Lebenswelt, Zukunft), Exemplarität und
Zugänglichkeit, fachdidaktische Prinzipien, Bedeutung für Folgelernen]

#### 1.1.2 Analyse der Lernausgangslage
[zusammenfassend: Lernatmosphäre, Vorkenntnisse bezogen auf das Stundenziel, bekannte
Methoden, Heterogenität und sprachliche Voraussetzungen, Barrieren und wie die Planung sie
abbaut, Kooperation – ohne Einzeldaten; Folgerungen für die Planung]

### 1.2 Darstellung der Lernsituation
[Kurzfassung von Handlungssituation und Handlungsergebnis; Stundenübersicht]

**Leitidee der Lernsituation:** [1–2 Sätze, aus den didaktisch-methodischen Kommentaren der LS]

| Stunde | Stundenthema | Ziel der Stunde | Phase der vollst. Handlung | Inhalte | Methodische Hinweise | Medien |
|---|---|---|---|---|---|---|
| | | | | | | |
| **→ diese Stunde** | | | | | | |

Vollständige Darstellung: Anhang I.

## 2 Planung der Unterrichtsstunde

### 2.1 Sachanalyse und Auswahl-/Reduktionsentscheidung (A)
[Mindmap als eingerückte Liste oder Strukturbild als SVG (fachdiagramm-erstellen); ✔ = ausgewählt, ✂ = bewusst reduziert;
ausführlich ggf. im Anhang II]

### 2.2 Darstellung der Unterrichtsstunde

#### 2.2.1 Leitidee und Stundenziel (K)

- **Leitidee der Stunde:** [1–2 Sätze: welche übertragbare Einsicht die Lernenden an diesem Schritt gewinnen und warum sie bedeutsam ist – ergänzt das Stundenziel, ersetzt es nicht]
- **FK:** Die SuS **[Operator]** …, indem sie …
- **PK:** Die SuS **[Operator]** …, indem sie …
- **Stundenergebnis:** [was am Ende sichtbar vorliegt]

#### 2.2.2 Didaktisch-methodische Entscheidungen (A)
[Begründungen zu Einstieg, Erarbeitung, Sicherung, Reflexion; Differenzierung; Medien;
Rolle der Lehrkraft; erwogene Alternativen]

#### Verlaufsplan (K)

| Zeit | Unterrichtsphase und -geschehen (L / SuS) | Phase der vollst. Handlung | Aktions- und Sozialform | Medien/Material | Didaktisch-methodische Begründung |
|---|---|---|---|---|---|
| 00–08 | **Einstieg** – L: „[Impuls wörtlich]" · SuS: [erwartete Antworten] | Informieren bzw. Analysieren | PL | | Vorwissen aktivieren, Problem öffnen |
| | **Erarbeitung** – Arbeitsauftrag: „[wörtlich]" | | EA/PA/GA | AB … | |
| | **Sicherung** – | | | | |
| | **Reflexion / Transfer** – [Frage, die die Leitidee aufgreift] | | | | |
| Σ | [Summe = Dauer − ca. 10 % Puffer] | | | | |

#### Sollbruchstelle und Reserve (K)
- **Sollbruchstelle:** [was entfällt bei Zeitnot]
- **Didaktische Reserve:** [Vertiefung für schnelle Gruppen]
- **Hausaufgabe / Ausblick:** [optional]

#### Lehrerhinweise (K)
- **Kernweg:** [__ min] – [welche Phasen/Aufgaben alle schaffen müssen]; darüber hinaus
  gekennzeichnet als *Zusatz* · *wenn Zeit bleibt* · *Praxischeck*
- **Stolpersteine und Moderation:** [typische Fehlvorstellungen, Gelenkstellen, Impulse bei Stocken]
- **Differenzierung:** [Hilfen, Zusatz, sprachliche Unterstützung – wer bekommt was, wie wählen SuS]
- **KI-Einsatz in der Stunde (optional):** [je Phase 🚫 Ohne KI · 💡 KI zum Verstehen · 🔧 Mit KI arbeiten – mit einem Satz Begründung, der das Stundenziel nennt, z. B. „Übung ohne KI, weil ich sehen will, was die SuS schon selbst können"; Ansage zu Beginn der Phase]
- **Anschluss:** [woran die Vorstunde endete · was die Folgestunde braucht]
- **Werkzeuge (optional):** [Quiz `quizfragen-erstellen`, Lernlandkarte `lernlandkarte-erstellen`, Schülerseiten `schuelerseiten-veroeffentlichen`]

## 3 Anhang

| Nr. | Inhalt |
|---|---|
| I | Tabellarische Darstellung der Lernsituation (bzw. Verweis auf `20_lernsituation_*.md`) |
| II | Sachanalyse (Mindmap, eine Seite) |
| III | Schülerdaten – **von der Lehrkraft einzutragen**, nur Vornamen/Kürzel |
| IV | Didaktisches Material **mit Erwartungshorizont** (K) |
| V | Verwendete Literatur und Quellen (nur tatsächlich genutzte, vollständig) |
| – | Erklärung zur selbständigen Anfertigung nach Vorgabe des Studienseminars; KI-Nutzung offenlegen |

### Anhang IV – Material und Erwartungshorizont (K)
[Arbeitsauftrag(e) mit Operator, Hilfekarten, Tafelbild-Entwurf, Erwartungshorizont]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Leitidee der Stunde: …
- Stundenziel FK/PK: …
- benötigtes Material: … → `unterrichtsmaterial-erstellen`
- Differenzierungsbedarf: … → `differenzierung-erstellen`
- Empfohlene nächste Skills: … (vor der Abgabe `unterrichtsentwurf-analysieren`, nach der Stunde `unterricht-reflektieren`)

> KI-gestützt erstellt (Skill unterrichtsentwurf-erstellen v1.12). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: references/berufliches-gymnasium.md

# Berufliches Gymnasium (BG) – was für Planung, Prüfung und Bewertung anders ist

Die Bibliothek ist ursprünglich für die duale Berufsausbildung (Lernfelder, Ausbildungsjahr,
Betrieb, Kammerprüfung) gebaut. Diese Datei sagt, was im **Beruflichen Gymnasium**
(Niedersachsen, vollzeitschulisch, Abschluss Allgemeine Hochschulreife, DQR 4) anders gilt.
Beispiel ist das BG **Technik**. Für die Fachrichtungen Wirtschaft, Gesundheit und Soziales
gilt die Struktur sinngemäß; Lerngebiete und Fächer aus der jeweiligen RRL einsetzen.

Bezug: Rahmenrichtlinien für das Fach Technik im Beruflichen Gymnasium – Technik –
(Stand Mai 2008, Erweiterungen August 2014, 2016 und Juni 2025); Rahmenrichtlinien für das
Fach Praxis (Stand August 2009); EPA Technik (KMK) mit Aufgabenbeispiel Ingenieurwissenschaften
(Beschluss 16.12.2021). 🔎 Stand vor jeder Planung prüfen (NiBiS, KMK).

## Inhalt
1. Begriffe: was im BG anders heißt
2. Aufbau der Rahmenrichtlinien
3. Lerngebiete im BG Technik (Übersicht)
4. Fach Praxis und Projektarbeit
5. Leistungsbewertung und Abitur
6. Lernsituationen im BG – Hinweise
7. Kopffelder und Planungsakte

---

## 1. Begriffe: was im BG anders heißt

| duale Ausbildung | Berufliches Gymnasium |
|---|---|
| Rahmenlehrplan (KMK), Lernfeld (LF) | Rahmenrichtlinien (RRL, Land), **Lerngebiet** (z. B. ING3) |
| Ausbildungsjahr 1–3(½) | **Schuljahrgang 11–13**; Jg. 11 = **Einführungsphase**, Jg. 12–13 = **Qualifikationsphase** (Halbjahre 12.1 … 13.2) |
| Beruf, Ausbildungsbetrieb, Lernortkooperation | **Fachrichtung** und **Schwerpunkt** (z. B. Technik/Ingenieurwissenschaften); Profilfach Technik, Fach Praxis; Kooperation mit Hochschulen, Unternehmen, außerschulischen Lernorten |
| Kammerprüfung, Notenskala 1–6 | **Abiturprüfung** (EPA), **Notenpunkte 15–0** |
| Auszubildende | Schülerinnen und Schüler (meist ohne Berufserfahrung; oft angesprochen als „angehende Ingenieurinnen und Ingenieure“) |
| Kunde, Betrieb als Rahmen | **fiktiver Auftraggeber** (Ingenieurbüro, Unternehmen, Kommune), Lastenheft |
| Ziel: berufliche Handlungskompetenz | zusätzlich **Studierfähigkeit** und **wissenschaftspropädeutisches Arbeiten** |

Die Leitlinie SchuCu-BBS 2024 gilt auch für das BG: Lernsituationen, Handlungssituation,
Handlungsergebnis, sechs Phasen, Analysebogen. Sie nennt ausdrücklich *Lerngebiete* und die
*Studienorientierung* als Bedeutsamkeit der Handlungssituation.

## 2. Aufbau der Rahmenrichtlinien

Jedes Lerngebiet hat
- **Titel** – charakterisiert Ziele und Inhalte;
- **Zeitrichtwert** – eingeplante Unterrichtsstunden, als Anregung verbindlich gemeint;
- **Zielformulierung** – das, was am **Ende des Bildungsgangs** erreicht sein soll. Sie
  definiert das Lerngebiet; mehrere Lernsituationen teilen sich die Ziele;
- **Inhalte** – Mindestanforderungen (bei den neuen Lerngebieten Ingenieurwissenschaften
  stattdessen nur **Anwendungsbezüge** als Beispiele);
- **Unterrichtshinweise** – Anregungen für die didaktischen Teams.

Daneben nennt die RRL **übergeordnete Kompetenzen** des Fachs (Abschn. 1.3), die alle
Lerngebiete konkretisieren, u. a.: Probleme analysieren und Lösungen beurteilen, Folgen
technischer Lösungen unter humanen, ökonomischen und ökologischen Aspekten bewerten,
Lösungsvarianten vergleichen und den Kompromiss darstellen, Modelle bilden und ihren
Geltungsbereich beachten, **Experimente** durchführen, **Hypothesen formulieren und prüfen**,
Fachsprache in Umgangssprache übertragen, Technik als ambivalent beurteilen.

**Konsequenz für die Planung:**
- Kompetenzen der LS aus der Zielformulierung ableiten; deren Wortlaut im Artefakt mit Quelle
  zitieren, nie glätten (`curriculum-abgleich.md`, falls vorhanden).
- Bei Lerngebieten ohne Inhaltsliste sind alle Inhalte **Konkretisierung** der Schule und so
  zu kennzeichnen.
- Die übergeordneten Kompetenzen sind ein Prüfmaßstab für die ganze Lerngebietsfolge
  (z. B. „Wo wird experimentiert? Wo werden Hypothesen geprüft?“).

## 3. Lerngebiete im BG Technik (Übersicht, Stand RRL 06/2025)

**Einführungsphase (Jg. 11), alle Schwerpunkte:** T1 Technische Informationen nutzen und
erstellen (40 h) · T2 Technische Systeme hinsichtlich Aufbau und Funktion analysieren (60 h) ·
T3 Technische Produkte entwerfen und deren Herstellung planen (60 h).

**Qualifikationsphase (Jg. 12–13):** je Schwerpunkt zwei verbindliche Lerngebiete, ein
optionales (**eins aus drei**, Wahl der Schule) und ein schulisch bestimmtes Lerngebiet in 13.2;
je 80 h. Die Reihenfolge legt die Schule fest.

| Schwerpunkt | verbindlich | optional (eins aus drei) | 13.2 schulisch |
|---|---|---|---|
| Bautechnik | BT1 Fertigung einfacher Baukörper planen · BT2 Einfache Tragwerke konstruieren und berechnen | BT3 Gebäude unter bauphysikalischen Aspekten planen · BT4 Ebene Stabwerke planen · BT5 Wohngebäude planen | BT6 |
| Elektrotechnik | ET1 Gleich- und Wechselspannungsnetzwerke analysieren · ET2 Technische Prozesse steuern | ET3 Elektrische Antriebe auswählen und deren Leistungselektronik dimensionieren · ET4 Technische Prozesse regeln · ET5 Schaltungen der Kommunikationstechnik analysieren und erstellen | ET6 |
| Informationstechnik | IT1 Technische Prozesse steuern · IT2 Netzwerke analysieren, planen und konfigurieren | IT3 Software zur Prozessdatenverarbeitung entwickeln · IT4 Messwerte erfassen und verarbeiten · IT5 Software zur grafischen Darstellung technischer Prozesse entwickeln | IT6 |
| Metalltechnik | MT1 Technische Produkte gestalten und dimensionieren · MT2 Herstellung und Prüfung technischer Produkte planen | MT3 Technische Prozesse automatisieren · MT4 Bauelemente mit CNC-Maschinen in Serie fertigen · MT5 Bauelemente optimieren | MT6 |
| Mechatronik | METRO 1 Mechatronische Systeme analysieren und erweitern · METRO 2 Technische Prozesse steuern | METRO 3 Messwerte erfassen und verarbeiten · METRO 4 Handhabungssysteme programmieren und optimieren · METRO 5 Antriebslösungen für mechatronische Systeme entwickeln | METRO 6 |
| Gestaltungs- und Medientechnik | GMT1 Druckprodukte erstellen · GMT2 Audiovisuelle Produkte erstellen | GMT3 Designprodukte entwickeln · GMT4 Komplexe mehrseitige Druckprodukte herstellen · GMT5 Komplexe audiovisuelle Produktionen erstellen | GMT6 |
| **Ingenieurwissenschaften** | **ING1** Technische Systeme erweitern · **ING2** Technische Systeme konstruieren | **ING3** Technische Systeme zukunftsorientiert entwickeln · **ING4** Optimierungsvorschläge für technische Systeme bewerten und realisieren · **ING5** Technikfolgenabschätzungen durchführen | **ING6** |

**Ingenieurwissenschaften – Besonderheiten (eigene Zusammenfassung):**
- Für ING1–ING6 gilt ein gemeinsamer Hinweis: Themen ganzheitlich und **interdisziplinär**
  (Bau-, Maschinenbau-, Elektro- und Informationstechnik) in praxis- oder lebensnahen
  **Projekten** bearbeiten.
- ING2 soll parallel zum Fach Praxis (Lerngebiet „Projekte durchführen“) laufen und das
  **Projektmanagement** einbeziehen.
- ING5 orientiert sich an Verfahren der Technikfolgenabschätzung (z. B. VDI 3780) und kann den
  ganzen Produktlebenszyklus betrachten.
- Weil ING3–ING5 *eins aus drei* sind, darf eine LS **kein Vorwissen aus einem anderen
  optionalen Lerngebiet** voraussetzen; aufbauen darf sie auf ING1/ING2 und der
  Einführungsphase.

## 4. Fach Praxis und Projektarbeit

- Das Fach Praxis (RRL 2009) hat eigene Lerngebiete über Jg. 11–13, u. a. *Projekte durchführen*
  (Jg. 12) und in Jg. 13 ein Lerngebiet, das sich am gleichzeitig unterrichteten Lerngebiet des
  Profilfachs Technik ausrichtet.
- In einem Halbjahr von Jg. 12 entsteht eine **Projektarbeit mit beruflichem Bezug**
  (wissenschaftspropädeutisch, Einzel- oder Gruppenarbeit), betreut im Fach Praxis.
- **Konsequenz:** Fertigung, Inbetriebnahme und Versuche einer Profilfach-LS gehören oft in den
  Praxisunterricht. Die LS weist die Verzahnung aus (Vereinbarungen → Verknüpfungen zu anderen
  Fächern/Lerngebieten).

## 5. Leistungsbewertung und Abitur

- **Notenpunkte 15–0**; Umrechnung prozentualer Leistung: `notenschluessel.md` (falls vorhanden). Unter 05 Punkten
  gilt ein Kurs als **unterpunktet** (Unterkurs) – Folgen für die Gesamtqualifikation 🔎 nach der
  geltenden Verordnung (BbS-VO, Ergänzende Bestimmungen) prüfen.
- **Klausuren** in der Qualifikationsphase: Aufgaben mit **EPA-Operatoren**, Bewertungseinheiten
  (**BE**), Anforderungsbereiche **30/40/30** (±10), Erwartungshorizont je Teilaufgabe mit AFB
  (`operatoren-epa-technik.md`, falls vorhanden).
- **Abiturprüfung Technik:** eA-Fach; das KMK-Aufgabenbeispiel Ingenieurwissenschaften rechnet
  mit 300 min für 120 BE (2,5 min/BE) und mit PC-Software (CAD, Tabellenkalkulation,
  SPS-Entwicklungsumgebung) als Hilfsmittel.
- **Dezentrale Abiturprüfung:** Für Schwerpunkte ohne zentrale Aufgaben reicht die Schule
  Abiturvorschläge (in der Regel zwei, A und B) zur Genehmigung ein – je Schülermaterial und
  Lehrermaterial mit unterrichtlichen Voraussetzungen (Kursfolge, Bezug jeder Aufgabe zum
  Unterricht), Erwartungshorizont mit Anforderungsbereichen je Teilaufgabe, Bewertungsmaßstab
  und vollständiger Musterlösung 🔎 Verfahren und Fristen der Schulbehörde. Mechatronik wird
  seit 2021 zentral geprüft (allgemeiner Teil zu METRO 1 und 2, dazu ein schuleigener Teil)
  🔎 aktuellen Stand prüfen.
- **Sonstige Leistungen / Mitarbeit:** Projekte, Dokumentationen, Präsentationen, Kolloquien,
  Versuchsprotokolle. Gewichtung gegenüber Klausuren legt die Fachkonferenz fest 🔎. Kriterien
  offenlegen, Einzelanteil bei Gruppenarbeit ausweisen.
- Keine Kammer, kein Ausbildungsbetrieb: Rückmeldungen gehen an Schülerinnen und Schüler und –
  bei Minderjährigen – an Erziehungsberechtigte, nicht an Betriebe.

## 6. Lernsituationen im BG – Hinweise

- **Handlungssituation:** Rolle (z. B. internes Ingenieurteam, Ingenieurbüro), fiktiver
  Auftraggeber, Lastenheft. Bedeutsam heißt hier auch **studien- und gesellschaftsbezogen**
  (Energiewende, Automatisierung, Technikfolgen).
- **Soziale Interaktion:** Projektgruppe, Auftraggeber, Expertinnen und Experten,
  Stakeholder-Rollenspiel, Fachgespräch – nicht „andere Auszubildende“.
- **Offenheit:** Lastenheft nennt Ziele und Randbedingungen, nicht die Technik; Alternativen
  werden nach technischen, ökologischen und ökonomischen Kriterien abgewogen.
- **Wissenschaftspropädeutik:** Hypothesen, Modelle und ihr Geltungsbereich, Quellenkritik,
  Zitieren, Experiment mit Fehlerbetrachtung, Dokumentation.
- **Projekt-LS:** Muster in `lernsituationsmuster.md`, falls vorhanden (Projekt mit Lastenheft, Experiment,
  Urteilsbildung/TFA).
- **Querschnittsaufgaben** (BNE, Demokratiebildung, Europabildung, Medienbildung):
  `querschnittsaufgaben.md`, falls vorhanden.
- **Kompetenzraster zur Lerngebietsanalyse** (in NLQ-Mustern oft noch „Lernfeldanalyse“
  genannt): Zielformulierung des Lerngebiets × Lernsituationen, mit Rückwärtsprobe
  (`curriculum-abgleich.md` Abschn. 7, falls vorhanden).

## 7. Kopffelder und Planungsakte

Statt `ausbildungsjahr` im BG:

```yaml
schulform: "Berufliches Gymnasium Technik"
schwerpunkt: "Ingenieurwissenschaften"
schuljahrgang: 13            # 11 | 12 | 13
phase: "Qualifikationsphase" # Einführungsphase | Qualifikationsphase
lerngebiet: "ING3 Technische Systeme zukunftsorientiert entwickeln"
zeitrichtwert_lerngebiet: 80
curriculare_vorgabe: "RRL Technik im Beruflichen Gymnasium – Technik – (Erweiterung 06/2025)"
dqr: 4
```

Typische Fehler: „Lernfeld“ statt „Lerngebiet“; veralteter RRL-Stand im Kopf; Ausbildungsjahr
statt Schuljahrgang; reale Kontaktdaten des fiktiven Auftraggebers.

## Anhang: references/didaktische-leitidee.md

# Didaktische Leitidee einer Stunde bzw. Lernsituation

Planungshilfe der Bibliothek (Entscheidung der Fachberatung, 19.10.2026), in eigenen Worten.
Die Leitlinie SchuCu-BBS 2024 kennt den Begriff nicht; die Leitidee **ergänzt** ihre Begriffe –
Handlungssituation, Handlungsergebnis, Fach- und Personale Kompetenz, sechs Phasen – und
**ersetzt keinen** davon. Sie ist kein zusätzliches Feld der Lernsituation, kein Kriterium des
Analysebogens und kein zweites Ziel.

## Inhalt
1. Was die Leitidee ist
2. Abgrenzung zu den Begriffen der Leitlinie
3. Zwei Ebenen und wo sie steht
4. Formulieren – Muster und Kriterien
5. Beispiele
6. Typische Fehler
7. Prüffragen vor und nach dem Unterricht

## 1. Was die Leitidee ist

Die didaktische Leitidee sagt in **ein bis zwei Sätzen**, worum es im Kern geht: welche
**übertragbare Einsicht**, Fertigkeit oder Haltung die Lernenden **am exemplarischen Fall**
gewinnen sollen und **warum** das für sie in Beruf bzw. Lebenswelt bedeutsam ist. Sie bündelt
die Analyse (Sachstruktur, Lernausgangslage, Bedeutsamkeit, Exemplarität) zu einer Richtung,
an der sich Auswahl und Reduktion, Phasierung, Arbeitsaufträge und Sicherung ausrichten.

## 2. Abgrenzung zu den Begriffen der Leitlinie

| Begriff | Frage | Beispiel LS 4.2 *Gurtförderer warten* |
|---|---|---|
| Thema | Worum geht es inhaltlich? | Wartung eines Gurtförderers |
| **Handlungssituation** (Leitlinie) | Vor welchem Problem stehen die Lernenden? | Wartung seit drei Monaten überfällig, höchstens zwei Stunden Stillstand, Plan muss freigegeben werden |
| **Didaktische Leitidee** (Bibliothek) | Was sollen die Lernenden an diesem Fall exemplarisch erfassen – und warum ist das bedeutsam? | Eine Anlage läuft nur sicher und zuverlässig weiter, wenn nach dem Plan des Herstellers gewartet wird statt nach Gefühl – Planung ist Teil der Arbeitssicherheit, nicht Papierkram. |
| **Fach- und Personale Kompetenz** (Leitlinie) bzw. Stundenziel | Was können die Lernenden am Ende nachweisbar? | erstellen einen Arbeitsplan …, indem …; stimmen Arbeitsteilung im Tandem ab, indem … |
| **Handlungsergebnis** (Leitlinie) | Was liegt am Ende vor? | Arbeitsplan, gewartete Anlage, Wartungsprotokoll, Übergabe mit Empfehlung |

Die Leitidee beschreibt die **Richtung**, die Kompetenzen bzw. das Stundenziel machen sie
**überprüfbar**, das Handlungsergebnis macht sie **sichtbar**.

## 3. Zwei Ebenen und wo sie steht

| Ebene | Reichweite | Ort in der Dokumentation |
|---|---|---|
| **Leitidee der Lernsituation** | trägt alle Phasen der vollständigen Handlung | Lernsituation: unter *Vereinbarungen und Hinweise zur Umsetzung → didaktisch-methodische Kommentare* (kein neues Feld); Entwurf Typ A: *Darstellung der Lernsituation*; Sequenz (Typ S): über der Sequenzübersicht; Lehrerhandreichung: Abschnitt 2 |
| **Leitidee der Stunde** | konkretisiert die Leitidee der Lernsituation für den Schritt dieser Stunde | Entwurf: unmittelbar vor dem Stundenziel; Reflexion: Zeile in der Zielerreichung |

Die Leitidee der Stunde widerspricht der der Lernsituation nicht; sie zeigt, welchen Teil davon
diese Stunde einlöst.

## 4. Formulieren – Muster und Kriterien

**Muster:**
> Am [Fall aus der Handlungssituation] erfassen die Lernenden, dass bzw. wie [übertragbare
> Einsicht] – bedeutsam, weil [Gegenwart bzw. Zukunft in Beruf oder Lebenswelt].

Ebenso möglich: ein bis zwei Sätze ohne Muster oder eine **Leitfrage** aus Sicht der Lernenden
(„Woran erkenne ich, ob die Anlage ohne Bedenken weiterlaufen kann?"), sofern Einsicht und
Bedeutsamkeit erkennbar bleiben.

**Fünf Kriterien:**
1. **verdichtet** – ein bis zwei Sätze, eine Idee;
2. **exemplarisch** – reicht über den Fall hinaus (auf andere Anlagen, Aufträge, Situationen);
3. **bedeutsam** – mit Bezug zu Beruf bzw. Lebenswelt jetzt oder später (knüpft an die
   Anforderungen 2, 3 und 5 der Leitlinie an die Handlungssituation an);
4. **stimmig** – passt zur Handlungssituation und wird durch Kompetenzen bzw. Stundenziel
   operationalisiert, ohne sie zu wiederholen;
5. **tragend** – Auswahl und Reduktion, Phasierung und Arbeitsaufträge lassen sich auf sie
   zurückführen; Sicherung oder Reflexion greift sie auf.

## 5. Beispiele

| Lernsituation bzw. Stunde | Leitidee |
|---|---|
| IM 1, LS 4.2, Stunde Planen *Arbeitsplan erstellen* | Ein Arbeitsplan ist die Voraussetzung für sicheres Arbeiten: Wer die Herstellerangaben in eine begründete Reihenfolge bringt und das Wiedereinschalten ausschließt, kann eine Anlage in knapper Zeit zuverlässig warten. |
| AM SHK 2, LS 7.1 *Luft aus einer Heizungsanlage beseitigen* | Luft in der Anlage ist ein Symptom: Wer Befunde systematisch vergleicht, findet die Ursache, statt nur zu entlüften – und kann der Kundin erklären, warum das Problem nicht wiederkommt. |
| BG Technik, ING3, Kickoff *Lastenheft analysieren* | Ein Lastenheft beschreibt, was der Auftraggeber braucht, nicht wie es gebaut wird – wer zuerst die richtigen Fragen stellt, vermeidet teure Fehlentwicklungen. |
| FI, LS 5.2 *Ticket-Tool entwickeln* | Software wird für Menschen gebaut: Erst wenn die Anforderungen des Supports als Testfälle feststehen, lässt sich zeigen, dass das Werkzeug zuverlässig hilft. |

## 6. Typische Fehler

| Fehler | Beispiel | Besser |
|---|---|---|
| Thema statt Leitidee | „Wartung von Gurtförderern" | Einsicht und Bedeutsamkeit benennen (Abschn. 5) |
| Ziel statt Leitidee | „Die SuS erstellen einen Arbeitsplan." | das ist das Stundenziel – die Leitidee sagt, *wofür* |
| zu allgemein | „Die SuS sollen selbstständig arbeiten." | an den Fall binden: was genau, warum gerade hier |
| zu viele Ideen | drei Sätze mit drei Schwerpunkten | eine Idee; Weiteres in die didaktischen Entscheidungen |
| steht nur im Entwurf | Leitidee formuliert, Sicherung greift sie nicht auf | in Sicherung oder Reflexion eine Frage dazu stellen |
| fremdes Kompetenzmodell | Leitidee als Kopf eines Rasters mit vier Kompetenzdimensionen | Kompetenzen bleiben Fach- und Personale Kompetenz (Leitlinie) |

## 7. Prüffragen vor und nach dem Unterricht

**Vor dem Unterricht** (Entwurf, Selbstcheck):
- Ist die Leitidee formuliert – und erfüllt sie die fünf Kriterien?
- Lässt sich jede Phase auf sie beziehen? Was im Verlauf trägt nichts zu ihr bei?
- Wo im Verlauf (Sicherung, Reflexion) wird sie für die Lernenden sichtbar?

**Nach dem Unterricht** (Reflexion):
- Woran ließ sich erkennen, dass die Lernenden die Leitidee erfasst haben – Äußerungen,
  Stundenergebnis, Transfer (Anzahlen, ohne Namen)?
- Hat die Leitidee die Stunde getragen, oder war sie zu groß bzw. zu klein für die Zeit?
- Was folgt für die Leitidee der nächsten Stunde?

## Anhang: references/ki-vereinbarungen.md

# KI-Vereinbarungen auf drei Ebenen – Klasse, Unterricht, Aufgabe

Gemeinsame Referenz für `unterricht-entwickeln`, `unterrichtsentwurf-erstellen`,
`unterrichtsmaterial-erstellen`, `lernsituation-dokumentieren`, `schuelerseiten-veroeffentlichen`,
`lernsituation-analysieren` und `ki-chatbot-einrichten`. Sie beantwortet: **Wo legt die Lehrkraft
fest, ob und wie Lernende KI nutzen – und wie sagt sie es so, dass die Lernenden es verstehen?**

Herkunft: Praxisbericht einer BBS-Lehrkraft zu KI-Regeln auf drei Ebenen; die Ebenen greift ein
angekündigter Artikel in der Zeitschrift PÄDAGOGIK auf, Grundlage der Klassenregeln ist dort ein
KI-Leitfaden für Lehrende und Lernende (Angaben 🔎 ergänzen). In eigenen Worten gefasst und um
Voreinstellungen, Prüffragen und Planungsorte der Bibliothek ergänzt. Stand 1.33. Keine Vorgabe
der Leitlinie SchuCu-BBS 2024, sondern ergänzende Planungshilfe; Vorgaben der Schule und des
Landes zur KI-Nutzung gehen vor 🔎.

## Inhalt
1. Warum Klassenregeln allein nicht reichen
2. Drei Ebenen
3. Die drei Zeichen am Arbeitsschritt
4. Voreinstellung je Phase
5. Begründen und ansagen
6. Lockern: Lernende entscheiden mehr
7. Wo das in der Planung steht
8. Prüffragen
9. Formulierungshilfen
10. Ältere Fassung: die KI-Ampel

---

## 1. Warum Klassenregeln allein nicht reichen

Ein Beispiel aus dem Praxisbericht: Die Klassenregel lautet „KI darf das Lernen unterstützen“.
Eine Übungsphase ist bewusst ohne KI angelegt, weil die Lehrkraft sehen will, was die Lernenden
schon selbst können. Ein Schüler beruft sich auf die Regel – „Üben ist doch auch Lernen“ – und hat
aus seiner Sicht recht. Die Lehrkraft widerspricht scheinbar der eigenen Vereinbarung.

- **Ob KI hilft oder im Weg steht, hängt vom Ziel der Phase ab.** Dieses Ziel kennt zuerst nur die
  Lehrkraft.
- Ein Zusatz wie „außer die Lehrkraft sagt etwas anderes“ zeigt, *dass* es Ausnahmen gibt, nicht
  *warum* diese Phase eine ist.
- Also braucht es neben der Klassenregel Vereinbarungen und Hinweise, die zeigen, **wann und wie**
  KI konkret genutzt werden kann und soll – und das **Ziel** dahinter sichtbar machen.

## 2. Drei Ebenen

Klarheit entsteht, wenn alle drei Ebenen festgelegt sind und ineinandergreifen.

| Ebene | Was wird festgelegt | Wann und wo | Beispiel |
|---|---|---|---|
| **Klasse** | verbindlicher Rahmen: freigegebene KI-Werkzeuge, Datenschutz, Angabe der KI-Nutzung bei Abgaben, Grundsatz zur Lernunterstützung, Vorrang von Ansage und Zeichen | zu Beginn des Schuljahres bzw. der Lernsituation, mit der Klasse vereinbart; Regelseite oder Aushang | „Freigegeben sind … Personenbezogene Daten gehören nicht in KI-Werkzeuge. Bei Abgaben geben wir an, wofür wir KI genutzt haben.“ |
| **Unterricht** | KI-Einsatz **phasenweise**: welche Phase mit, welche bewusst ohne KI – mit kurzer Begründung | bei der Planung (Verlauf, Lektion); zu Beginn der Phase angesagt | Einstieg ohne KI · Erarbeitung mit KI für Recherche und Feedback · Übung ohne KI |
| **Aufgabe** | **Zeichen am Arbeitsschritt**, dazu im Auftrag, wie KI konkret genutzt werden darf | Arbeitsblatt, Lektion, Aufgabenkarte | siehe Abschn. 3 |

Bewährt für die Klassenebene sind **fünf Regeln** (Lektionsmuster): erst selbst versuchen ·
prüfen statt glauben · KI-Nutzung kennzeichnen · erklären können, was man übernimmt · Daten
schützen. Die Klassenregel sollte außerdem sagen, dass es ausgewiesene Phasen und Aufgaben ohne
KI gibt und dass **Ansage und Zeichen der Grundregel vorgehen** – sonst entsteht der Widerspruch
aus Abschn. 1.

## 3. Die drei Zeichen am Arbeitsschritt

Die Lernenden sehen auf einen Blick, ob und in welchem Umfang KI erlaubt ist. **Zeichen und Wort
gehören zusammen** (lesbar im Schwarzweißdruck, für Screenreader, unabhängig von der Farbe):
die Legende mit Wort steht auf derselben Seite (Blattkopf, Infokasten der Lektion), am
Arbeitsschritt genügt dann das Zeichen; wo die Aufgabe ohne Legende gelesen wird (Aufgabenkarte,
Einzelblatt), steht das Wort dabei.

| Zeichen | Wort | Bedeutung | typische Aufträge |
|---|---|---|---|
| 🚫 | **Ohne KI** | Der Arbeitsschritt wird ohne KI-Werkzeug bearbeitet. | Vorwissen und Vorhersage, Üben als Standortbestimmung, eigener Entwurf, Entscheidung und Begründung, Reflexion, Leistungsnachweis |
| 💡 | **KI zum Verstehen** | KI ist als Lernunterstützung erlaubt: Begriffe und Zusammenhänge erklären lassen, Verständnisfragen stellen. Das Ergebnis des Arbeitsschritts entsteht bei den Lernenden. | Erarbeiten neuer Begriffe, Nachfragen zu einem Fachtext, Beispiel erklären lassen |
| 🔧 | **Mit KI arbeiten** | Die Lernenden setzen KI im Auftrag für einen Teil der Arbeit ein – als Werkzeug beim Schreiben, für Recherche oder Feedback. Sie prüfen das Ergebnis, kennzeichnen es nach der Klassenregel und können erklären, was sie übernehmen. | Rohfassung einer Dokumentation überarbeiten lassen, Feedback zum eigenen Entwurf einholen, Quellen sammeln |

Regeln für den Gebrauch:
- **Wie** KI genutzt werden darf, steht zusätzlich im Arbeitsauftrag (Werkzeug, Umfang, was
  nicht). Das Zeichen sagt „ob und wie weit“, der Auftrag sagt „wie genau“.
- **Ein Zeichen je Arbeitsschritt**, wo sich die Schritte unterscheiden; ein Zeichen für das
  ganze Blatt nur, wenn es für alle Schritte gilt.
- **Wo Zeichen verwendet werden, trägt jeder Arbeitsschritt eines.** Ein fehlendes Zeichen lädt
  zur Rückfrage aus Abschn. 1 ein.
- Das Zeichen steht **vor dem Operator**: `**3.** 🚫 *Ohne KI* – Skizzieren Sie …`

Beispiel (Arbeitsblatt):

> **1.** 🚫 *Ohne KI* – Skizzieren Sie, welche Ursachen Sie für die Störung vermuten (5 min).
> **2.** 💡 *KI zum Verstehen* – Lassen Sie sich die Begriffe aus Ihrer Skizze erklären, die Sie
> nicht sicher kennen; notieren Sie je Begriff einen Satz in eigenen Worten.
> **3.** 🔧 *Mit KI arbeiten* – Lassen Sie sich Rückmeldung zu Ihrem Prüfplan geben (nur den
> Plan eingeben, keine Namen); entscheiden Sie, welche Hinweise Sie übernehmen, und halten Sie
> fest, welche nicht.

## 4. Voreinstellung je Phase

Voreinstellung für die **Unterrichtsebene**, keine Vorschrift: Wer abweicht, begründet es in
einem Satz (Abschn. 5). Sie folgt der Leitplanke der Bibliothek, dass **Entscheiden, Überprüfen und
Reflektieren Leistung der Lernenden bleiben**.

| Phase bzw. Element | Voreinstellung | Begründung (Ziel) |
|---|---|---|
| Einstieg, Vorwissen, Vorhersage | 🚫 | sichtbar machen, was schon da ist; eine Vorhersage wirkt nur, wenn sie vorher eigen war |
| Informieren, Erarbeiten | 💡; für Recherche 🔧 | Begriffe klären, Quellen finden – Quellen und Auskünfte danach prüfen |
| Planen | erster eigener Entwurf 🚫; danach 💡 oder 🔧 | der eigene Weg entsteht bei den Lernenden; KI prüft oder fragt nach, entwirft nicht vor |
| Entscheiden | 🚫 | Urteil und Begründung sind die Leistung dieser Phase |
| Durchführen, Üben | nach Ziel: Standortbestimmung 🚫 · Verstehen 💡 · Dokumentation, Text 🔧 | das Ziel der Übung bestimmt das Zeichen |
| Überprüfen (mit Überarbeitung) | 🚫; KI-Rückmeldung nur als zusätzliche Quelle (🔧), die die Lernenden selbst bewerten | die Überprüfung ist Leistung der Lernenden |
| Reflektieren | 🚫 | der eigene Lernweg lässt sich nicht auslagern |
| Leistungsnachweis | 🚫, sofern die Aufgabe nicht ausdrücklich etwas anderes vorsieht; Vorgaben der Schule gehen vor 🔎 | Nachweis der eigenen Leistung |

## 5. Begründen und ansagen

- **Eine kurze Begründung gehört zu jeder Phase ohne KI** – und zu jeder Abweichung von der
  Voreinstellung. Muster: *„Heute ohne KI, weil …“*. Mündlich zu Beginn der Phase, schriftlich
  am Blatt bzw. im Infokasten der Lektion.
- Die Begründung nennt das **Ziel**, nicht das Verbot:

| Ziel | Formulierung |
|---|---|
| Standortbestimmung | „Ich möchte sehen, was ihr schon selbst könnt – dann wissen wir, was ihr noch braucht.“ |
| eigenes Urteil | „Hier entsteht euer Urteil. Das kann euch kein Werkzeug abnehmen.“ |
| Automatisieren, Üben | „Was ihr selbst durchgeführt habt, steht euch in der Arbeit zur Verfügung.“ |
| Prüfungsnähe | „In der Klassenarbeit gibt es dieses Werkzeug auch nicht.“ |
| Zeit gewinnen | „Mit KI ist die Recherche in zehn Minuten erledigt – die Zeit brauchen wir für die Auswertung.“ |

- **Sinn der Regeln immer wieder thematisieren:** warum es sie gibt und warum eine Aufgabe mal
  ohne KI, mal mit KI zum Verstehen, mal mit KI als Werkzeug gedacht ist – zu Beginn, in der
  Reflexion (*Wo hat dir das Zeichen geholfen, wo hat es gestört?*) und bei der Rückfrage eines
  Lernenden. Regeln ohne verstandenen Sinn tragen nicht.
- In den Unterrichtsentwurf gehört die Begründung in die didaktisch-methodischen Entscheidungen
  und in die Lehrerhinweise (*KI-Einsatz in der Stunde*), nicht in den Schülertext.

## 6. Lockern: Lernende entscheiden mehr

Die Zeichen helfen besonders in Klassen, in denen sich Abläufe erst einspielen und selbstständiges
Lernen im Aufbau ist. Mit der Zeit kann die Steuerung lockerer werden. Vorschlag der Bibliothek:

1. **Lehrkraft setzt** das Zeichen je Arbeitsschritt (Beginn).
2. Zeichen **je Phase**, die Arbeitsschritte erben es; Ausnahmen werden ausgewiesen.
3. Die Lehrkraft gibt einen **Rahmen** vor („hier sind 💡 und 🔧 möglich“), die Lernenden **wählen
   und begründen** („ich nutze hier 💡, weil …“) und kennzeichnen ihre Nutzung.

Diagnose-Übungen und Leistungsnachweise (🚫) bleiben in jeder Stufe Entscheidung der Lehrkraft.
Ob eine Klasse die nächste Stufe erreicht hat, zeigen die Rückmeldungen der Lernenden und die
Kennzeichnung in den Abgaben – nicht der Kalender.

## 7. Wo das in der Planung steht

| Artefakt | Ebene | Stelle |
|---|---|---|
| Lernsituation | Klasse | KI-Regeln **einmal am Anfang** (zusammen mit Bewertungskriterien), Verweis auf die Regelseite; nicht in jeder Einheit wiederholen |
| Unterrichtsentwurf, Verlaufsplan | Unterricht | je Phase Zeichen und Begründung (Lehrerhinweise *KI-Einsatz in der Stunde*; Begründung in den didaktisch-methodischen Entscheidungen) |
| Lektion (Schülerseite) | Unterricht, Aufgabe | Infokasten *KI-Werkzeuge in dieser Lektion* vor der ersten Aufgabe; Zeichen am Arbeitsschritt |
| Arbeitsblatt, Aufgabenkarte | Aufgabe | Zeichen vor dem Operator; Hinweis zum Wie im Auftrag |
| KI-Chat im Kurs | Aufgabe | nur dort anbieten oder nennen, wo 💡 oder 🔧 gilt; in 🚫-Phasen bleibt er geschlossen bzw. wird nicht empfohlen (Einsatzort in der Beschreibung des Chats) |

## 8. Prüffragen

Für Planung und Prüfberichte. Skala ✅ · ⚠️ · ❌ · ➖ nicht naheliegend (wie bei den Querschnittsaufgaben).

| Nr. | Ebene | Prüffrage |
|---|---|---|
| K1 | Klasse | Gibt es verbindliche Regeln (Werkzeuge, Daten, Kennzeichnung) – und verweisen Lernsituation bzw. Lektion darauf, statt sie zu wiederholen? |
| K2 | Klasse | Sagt die Grundregel, dass Ansage und Zeichen vorgehen, sodass Ausnahmen kein Widerspruch sind? |
| U1 | Unterricht | Ist je Phase festgelegt, ob KI genutzt wird – mit einer Begründung, die das Ziel der Phase nennt? |
| U2 | Unterricht | Bleiben Entscheiden, Überprüfen und Reflektieren Leistung der Lernenden? |
| A1 | Aufgabe | Trägt jeder Arbeitsschritt ein Zeichen mit Wort, und steht im Auftrag, wie KI genutzt werden darf? |
| A2 | Aufgabe | Passen Zeichen und Phase zusammen (keine 🔧-Aufgabe in einer Phase ohne KI)? |

## 9. Formulierungshilfen

- *Klassenregel:* „KI darf euer Lernen unterstützen. Wann und wie, zeigen die Ansage und das
  Zeichen am Arbeitsschritt – sie gehen dieser Grundregel vor.“
- *Ansage:* „Die nächste Übung läuft ohne KI. Ich möchte sehen, was ihr schon selbst könnt.“
- *Auf die Rückfrage „Üben ist doch auch Lernen“:* „Ja – und heute übt ihr, ohne dass euch
  jemand etwas abnimmt, damit ihr seht, wo ihr steht. Deshalb steht auf dem Blatt 🚫.“
- *Infokasten (Lektion):* „🚫 **Phase 2 und 4:** ohne KI – Entscheidung, Überprüfung und Lernweg
  sind eure eigenen. 💡 **Phase 1 und 3:** KI zum Verstehen. 🔧 **Aufgabe 6:** mit KI arbeiten,
  Nutzung kennzeichnen. Warum? [ein Satz]“

## 10. Ältere Fassung: die KI-Ampel

Frühere Fassungen der Bibliothek (Lektionsmuster, Stand 1.15) kannten eine **KI-Ampel je
Phase**: 🟢 Erklärhilfe · 🟡 übernehmen nur gekennzeichnet und nur, was man erklären kann ·
🔴 ohne KI. Sie ist durch die drei Zeichen ersetzt:

| früher | jetzt |
|---|---|
| 🟢 Erklärhilfe | 💡 KI zum Verstehen |
| 🟡 übernehmen nur gekennzeichnet, nur Erklärbares | 🔧 Mit KI arbeiten (Kennzeichnen und Erklären-können sind Klassenregeln) |
| 🔴 ohne KI | 🚫 Ohne KI |

Gründe: Die Zeichen unterscheiden sich in Form und Wort, nicht nur in der Farbe; sie gelten am
**Arbeitsschritt**, nicht nur je Phase; und die Ampelfarben bleiben den Prüfberichten
(einsetzbar · nach Überarbeitung · überarbeiten) vorbehalten. Bereits erstellte Lektionen mit der
Ampel bleiben gültig und können beim nächsten Überarbeiten umgestellt werden.

## Anhang: references/leitfragen-planung.md

# Leitfragen und Wirksamkeitsprinzipien für die Stundenplanung

Grundlage: Handlungsleitfaden zur kompetenzorientierten Unterrichtsplanung (Studienseminar,
Stand 03/2021), Leitlinie SchuCu-BBS 2024, Prinzipien lernwirksamer Planung (Lipowsky,
Anderson/Krathwohl, Deci & Ryan, Wahl). Leitfragen sind Reflexionshilfen – nicht alle müssen
im Entwurf beantwortet werden.

## Inhalt
1. Curriculare und (fach-)didaktische Einordnung
2. Lernausgangslage
3. Sachanalyse
4. Leitidee und Stundenziel
5. Didaktisch-methodische Entscheidungen
6. Wirksamkeitsprinzipien (verbindlich)
7. Gelenkstellen und Sollbruchstelle
8. Abkürzungen

## 1. Curriculare und (fach-)didaktische Einordnung
- Auf welche Ordnungsmittel beziehe ich mich, welche Kompetenzerwartungen formulieren sie?
- Welche Vorgaben macht das schulische Curriculum (Lernsituation übernehmen, anpassen, neu)?
- Welche Anforderungen stellt das DQR-Niveau?
- Welche Relevanz hat das Thema (exemplarisch, gegenwärtig, zukünftig, beruflich, privat)?
  Ausführlich begründen (Entwurfstyp A) – die Fragen knüpfen an die Anforderungen der Leitlinie
  an die Handlungssituation an (bedeutsam, greift Erfahrungen auf, exemplarisch):
  - **Gegenwart:** Wo begegnet den Lernenden der Gegenstand schon heute – im Betrieb, in der
    Lebenswelt? Welche Erfahrungen bringen sie mit?
  - **Zukunft:** Wofür brauchen sie ihn später – in der Abschlussprüfung, als Fachkraft, im
    weiteren Bildungsgang?
  - **Exemplarisch:** Wofür steht der Fall über sich hinaus? Auf welche anderen Anlagen,
    Aufträge oder Situationen lässt sich das Gelernte übertragen?
  - **Zugänglich:** Was macht den Gegenstand für diese Lerngruppe anschaulich und greifbar –
    und wo liegen Hürden (Sprache, Abstraktion, Vorwissen)?
  - **Struktur:** Welche Teilschritte bauen aufeinander auf, wo liegen die Gelenkstellen?
  Die Antworten begründen Auswahl und Reduktion (Abschn. 3) und das Stundenziel (Abschn. 4) – sie
  ersetzen sie nicht.
- Welche fachdidaktischen Prinzipien gelten (Handlungs-, Problem-, Arbeitsprozessorientierung,
  Sicherheit vor Tempo, Systemdenken)?
- Welche Bedeutung hat die Stunde für nachfolgende Lernprozesse und andere Fächer?

## 2. Lernausgangslage (zusammenfassend, ohne sensible Einzeldaten)
- Lernatmosphäre, Größe, Zusammensetzung, Ausbildungsbetriebe/Branchen
- fachliche Vorkenntnisse bezogen auf das Stundenziel; was muss zuerst gelegt werden?
- bekannte und neue Methoden; eingeführte Rituale und Regeln
- Heterogenität: Leistung, Tempo, Sprache (Deutsch als Zweitsprache), Motivation
- Kooperationsfähigkeit, Selbständigkeit
- Zugänglichkeit: Welche Barrieren gibt es (Material, Raum, Sprache, Tempo), und wie baut die
  Planung sie ab? Unterstützungsbedarf nur zusammenfassend, nie einer Person zugeordnet.
- Weitere Erwachsene im Unterricht (Doppelbesetzung, Schulbegleitung, Sozialpädagogik): Welche
  Rolle und Aufgabe hat wer in welcher Phase – was ist abgesprochen?
- Woher stammen die Einschätzungen (Beobachtung, Lernstandserhebung, Gespräch)?

## 3. Sachanalyse und Auswahl-/Reduktionsentscheidung
- Welches sind die zentralen Aspekte des Gegenstands und wie hängen sie zusammen?
- Expertenwissen über die Stunde hinaus zeigen; Auswahl markieren (✔), Reduktion (✂) begründen.
- Form: Mindmap/Concept-Map (i. d. R. eine Seite) oder knapper Fließtext.

## 4. Leitidee und Stundenziel
- Welche übertragbare Einsicht sollen die Lernenden an diesem Schritt gewinnen – und warum ist
  sie für sie bedeutsam? (Leitidee in ein bis zwei Sätzen; aus der Leitidee der Lernsituation
  abgeleitet; `didaktische-leitidee.md`)
- Lassen sich Auswahl, Reduktion und Phasen auf die Leitidee zurückführen? Wo greift die
  Sicherung oder Reflexion sie auf?
- Benenne ich den angestrebten Zuwachs an Wissen, Fertigkeiten, Haltungen?
- Ist das Ergebnis präzise, überprüfbar, mit angemessenem Operator formuliert?
- Welchen Beitrag leistet jede Phase? Woran erkenne ich am Ende, dass das Ziel erreicht ist?

## 5. Didaktisch-methodische Entscheidungen
- Wie stelle ich Transparenz her (Ziel, Ablauf, Advance Organizer)?
- In welcher Phase liegt der fachdidaktische Schwerpunkt?
- Wodurch entsteht kognitive Auseinandersetzung? Woran knüpfe ich an?
- Wie fördere und fordere ich schwächere und stärkere SuS konkret?
- Treffen Medien, Materialien und Aufgaben das Niveau? Sind sie sprachlich zugänglich?
- Welche Rolle übernehme ich je Phase (informierend, moderierend, impulsgebend, beratend,
  bewertend)? Welches SuS-Verhalten erwarte ich?
- Wie wird der Lernzuwachs sichtbar (Reflexion, gelöste Aufgaben, Handlungsergebnis)?
- Was ist beim Phasenübergang zu beachten?

## 6. Wirksamkeitsprinzipien (verbindlich für jeden Entwurf)

| Prinzip | Umsetzung im Verlauf | Warnsignal |
|---|---|---|
| Vorwissen aktivieren | Einstieg mit Impulsfrage, Schätzung, Hypothese, Bild/Störung; nach der Erarbeitung Abgleich mit den Hypothesen | Stoff „von vorn" ohne Anknüpfung |
| Input, Erprobung, Reflexion verschränken | Input ≤ 15–20 min am Stück (auch als begründete fachsystematische Phase), danach sofort Anwendung; Reflexion nicht nur am Ende | langer Vortrag, Praxis erst am Schluss |
| Kognitiv aktivieren | Fragen über Taxonomiestufen streuen, mind. eine Analyse-/Bewertungs-/Gestaltungsfrage; Wartezeit ≥ 3 s | nur Erinnerungsfragen, Kettenfragen |
| Lernende aktiv | Erarbeitung = größter Block, in der Regel geringer Redeanteil der Lehrkraft (Ausnahme: begründete fachsystematische Phase), begründeter Sozialformwechsel | Unterrichtsgespräch als Hauptphase |
| Autonomie und Kompetenzerleben | echte Wahlmöglichkeit (Weg, Hilfe, Sozialform), erreichbare Herausforderung, lernförderliche Rückmeldung | alles vorgegeben, Fehler werden sanktioniert |
| Sicherung | Ergebnis fixiert und für alle verfügbar; Bezug zum Stundenziel | Sicherung entfällt aus Zeitnot |

## 7. Gelenkstellen und Sollbruchstelle
- **Gelenkstellen** (Übergänge, zentrale Impulse, Arbeitsauftrag) wörtlich formulieren –
  dort scheitern Stunden am häufigsten.
- **Sollbruchstelle:** welcher Teil entfällt oder wird gekürzt, wenn die Zeit knapp wird
  (z. B. zweite Präsentation, Transferaufgabe → Hausaufgabe). Nie die Sicherung.
- **Didaktische Reserve:** Zusatzaufgabe für schnelle Gruppen, die das Stundenziel vertieft.
- **Puffer:** ca. 10 % der Stundenzeit nicht verplanen.

## 8. Abkürzungen
SuS Schülerinnen und Schüler · L Lehrkraft · PL Plenum · EA/PA/GA Einzel-/Partner-/Gruppenarbeit
(ag arbeitsgleich, at arbeitsteilig) · UG Unterrichtsgespräch · AB Arbeitsblatt ·
IB Informationsblatt · TA Tafelanschrieb · WB Whiteboard/Beamer · LMS Lernmanagementsystem ·
LS Lernsituation · FK Fachkompetenz · PK Personale Kompetenz · AFB Anforderungsbereich ·
UB Unterrichtsbesuch · PU Prüfungsunterricht

## Anhang: references/lernsituationsmuster.md

# Lernsituationsmuster – Diagnose, Entscheiden, Überprüfen, Reflektieren, Projekt, Experiment, Urteilsbildung

Bauformen, mit denen eine Handlungssituation **alle sechs Phasen** trägt. Gewonnen aus dem
Abgleich mit Lernsituationen aus der Fortbildung (u. a. SHK, LF 7) und mit NLQ-Mustern des
Beruflichen Gymnasiums Technik (ING3–ING5), verallgemeinert und in eigenen Worten. Die Muster ergänzen die Leitlinie (`schucu-bbs-2024.md`, falls vorhanden); sie sind **kein
Bestandteil der Leitlinie**. Beispiele: Gurtförderer GF-2 (fiktiv).

## Inhalt
1. Diagnose-Lernsituation
2. Entscheiden gestalten
3. Überprüfen gestalten
4. Reflektieren gestalten
5. Lernhürden planen
6. Roter Faden durch die Lernsituation
7. Zeitvarianten und Ersatzwege
8. Phasencheck (Ergänzung zum Analysebogen)
9. Projekt-Lernsituation mit Lastenheft
10. Hypothesen- und Experiment-Lernsituation
11. Urteilsbildung und Technikfolgenabschätzung
12. Lernzeit effizient nutzen – fachsystematische und lehrkraftgeführte Lernphasen

---

## 1. Diagnose-Lernsituation

Für Kundendienst-, Instandhaltungs- und Fehlersuchaufträge: Störmeldung, Reklamation,
Fehlerbild an Anlage, Netzwerk oder Software. Kern: **Die Lernenden finden die Ursache selbst.**

| Phase | Baustein | Material |
|---|---|---|
| Informieren | Vermutungen sammeln (mind. drei, die wahrscheinlichste markieren), auf einem Plakat festhalten, das hängen bleibt; System erfassen (Schema, Checkliste); Fachwissen in fachsystematischen Phasen, jeweils mit Rückbindungsfrage (Abschn. 6) | Situationsmaterial, Checkliste, Infotexte |
| Planen | Prüfplan: Prüfschritt, geprüfte Vermutung, erwartetes Ergebnis; Befunde auf Anforderung; Ursachen begründet ausschließen; Nachweis durch Rechnung, Messung oder Norm | Prüfplan und Befundkarten, Übung mit Kontrollwert |
| Entscheiden | Maßnahmen gegen die Ursache, nicht gegen das Symptom | Entscheidungsmatrix (Abschn. 2) |
| Durchführen | Handlungsergebnis, z. B. Störungsbericht mit Empfehlung; Umsetzung an Übungsanlage oder Ersatzweg | Berichtsvorlage, Arbeitsbericht |
| Überprüfen | Peer-Check; Abgleich mit den Anfangsvermutungen | Peer-Feedback-Bogen |
| Reflektieren | Transfer auf ein verändertes Fehlerbild | Reflexionsauftrag (Abschn. 4) |

Regeln:
- **Nichts verraten.** Kein Auftrag, keine Überschrift und keine Hilfe nennt die Ursache
  („Sie vermuten, dass das Lager …" nimmt die Diagnose vorweg). In einer Expertenphase ist die
  Ursache ein Thema unter mehreren.
- **Information gegen Planung.** Befunde gibt es nur zu Prüfschritten, die im eigenen Prüfplan
  stehen. Die Lehrkraft gibt sie in einer Rolle aus (Meisterin, Schichtleitung). Wer gründlich
  plant, erfährt mehr – das differenziert von selbst.
- **Stimmiges Befundbild.** Die Befunde ergeben eine Ursachenkette (oder bewusst zwei
  unabhängige Fehler). Einige schließen Vermutungen aus. Mindestens ein Befund ist auffällig,
  aber nicht die Ursache (falsche Fährte). Alle Werte passen zur Handlungssituation.
- **Ursache statt Symptom** als Maßstab: Im Bewertungsraster erreicht eine reine
  Symptombehandlung höchstens die unterste Stufe; in der Entscheidungsmatrix hat „Wirksamkeit
  gegen die Ursache" das höchste Gewicht.
- **Prüfreihenfolge im Erwartungshorizont:** vom Einfachen und Zerstörungsfreien zum
  Aufwendigen (befragen → ablesen → ansehen → messen → zerlegen). Andere begründete
  Reihenfolgen gelten.
- Die **Wirkungskette** (Ursache → Folgen → Symptom) steht im Erwartungshorizont und im Raster;
  als Bild mit `fachdiagramm-erstellen` (Ablauf).

## 2. Entscheiden gestalten

Die Leitlinie verlangt, dass die Lernenden sich für einen Lösungsweg entscheiden. Damit das eine
Leistung ist und kein Abnicken:
- **Mindestens zwei vertretbare Alternativen** vorgeben, Platz für eigene; in der
  Diagnose-Lernsituation **drei**, darunter die naheliegende, billige Teil- oder
  Symptomlösung. Eine Entscheidung gehört nur dorthin, wo es echte Alternativen gibt: Müssen
  beide Varianten ohnehin gebaut werden oder legt die Ausstattung die Wahl fest, ist es eine
  Scheinentscheidung und kostet Zeit ohne Lernzuwachs.
- **Kriterien mit Gewichtung** offenlegen (z. B. Wirksamkeit gegen die Ursache ×3,
  Sicherheit bzw. Norm- und Herstellervorgabe ×2, Kosten ×1, Aufwand oder Stillstand ×1).
  Die Gewichtung dürfen die Lernenden **begründet ändern** – die Begründung zählt mit.
- **Zielkonflikt** aus der Handlungssituation: Budget, Stillstandszeit oder Termin gegen
  fachliche Notwendigkeit.
- **Nachweis**, dass die naheliegende Lösung nicht reicht (Befund, Messung oder Rechnung). So
  wird die Analyse zur Entscheidungsgrundlage.
- Die Entscheidung wird **schriftlich begründet** und geht als Abschnitt in das
  Handlungsergebnis ein.
- Die Lehrkraft gibt Rückmeldung zu Kriterien und Begründung, nicht zur „richtigen" Maßnahme.

Kleinere Form: Pro-Contra-Tabelle zweier Lösungen oder Planbesprechung mit der Lehrkraft in
einer Rolle.

## 3. Überprüfen gestalten

- **Kriterien = offengelegtes Bewertungsraster** des Handlungsergebnisses, dazu Kontrollwerte.
- **Peer-Check:** Ergebnis mit einer Partnergruppe tauschen, mit dem Raster prüfen,
  Rückmeldung „zwei Stärken, ein nächster Schritt", **danach das eigene Ergebnis
  überarbeiten**. Ohne eingeplante Überarbeitungszeit bleibt Feedback folgenlos.
- **Feedbackregeln** vorab: Beobachtetes beschreiben, nicht die Person; der nächste Schritt ist
  konkret und machbar; wer Feedback bekommt, hört zu und fragt höchstens nach.
- **Abgleich mit den Anfangsvermutungen:** Was hat sich bestätigt, woran war es zu erkennen?
- **Gesprächsleistungen** (Beratung, Übergabe, Einweisung) in einer Simulation mit
  Rollenkarten und Beobachtungsbogen prüfen; wer die Kundenrolle spielt, beobachtet mit.

## 4. Reflektieren gestalten

Reflexionsfragen nach vier Typen; je Lernsituation mindestens eine **Transfer-** und eine
**Selbstbezugsfrage**:

| Typ | fragt nach | Beispiel (GF-2) |
|---|---|---|
| Ergebnis | Was ist erreicht, was hat sich bestätigt? | Welche Vermutung hat sich bestätigt – an welchem Befund haben Sie es erkannt? |
| Vorgehen | Wie bin ich vorgegangen, wo hakte es? | An welcher Stelle kamen Sie nicht weiter, und was hat geholfen? |
| Transfer | Was tue ich in einer veränderten Lage? | Wie gehen Sie vor, wenn der Gurt nach dem Rollentausch weiter schief läuft? |
| Selbstbezug | Was ist mein nächster Schritt? | Was prüfen Sie beim nächsten Störungsauftrag als Erstes? |

- **Selbsteinschätzung am Anfang und am Ende** (Kompetenzraster oder Kannliste) vergleichen:
  „Wo haben Sie sich verbessert, wo noch nicht?" Die Bögen bleiben bei den Lernenden – keine
  Auswertung je Person (Leitplanke: Lernstände nur für die Lerngruppe).
- Transfer in den Ausbildungsbetrieb über einen Erkundungsauftrag (Methodenrepertoire,
  „Mein Betrieb").
- Abschluss im Plenum, z. B. Blitzlicht.

## 5. Lernhürden planen

Vor dem Material drei bis sieben Hürden benennen: Fehlvorstellungen, Verwechslung ähnlicher
Begriffe, Rechenfallen (Vorzeichen, Einheit, Bezugsgröße, Über- und Absolutwert), Symptom statt
Ursache, Vermischung benachbarter Themen. Je Hürde Gegenmaßnahme und **Ort im Material**:

| Lernhürde | Gegenmaßnahme | Ort im Material |
|---|---|---|
| „Mehr Fett schmiert besser" | Herstellerangabe zur Füllmenge auswerten; Folgen der Überfettung im Infotext | Infoblatt Schmierung, Aufgabe 2 |
| Wartungsintervall in Tagen statt Betriebsstunden gerechnet | Stolperstein-Kasten, Kontrollwert | Arbeitsblatt 3 |

- **Gegenmaßnahmen:** Stolperstein-Kasten für Lernende auf dem Arbeitsblatt, Hilfekarte,
  Kontrollwert mit Diagnosehinweis („Wenn nicht: Einheit prüfen"), Befundkarte, Diagramm oder
  Versuch, Kriterium in Matrix oder Raster.
- **Fehlvorstellungen aufgreifen, nicht nur benennen:** Vorhersage notieren → mit Diagramm,
  Messung oder Versuch konfrontieren → Erklärung selbst formulieren → in der Sicherung
  ausdrücklich klären.
- Dokumentieren in den *didaktisch-methodischen Kommentaren* der Lernsituation und unter
  *Stolpersteine* in der Lehrerhandreichung.

## 6. Roter Faden durch die Lernsituation

- **Rückbindungsfrage:** Jede fachsystematische Phase (Expertengruppe, Infotext, Lehrgang)
  endet mit „Was bedeutet das für [Anlage, Kundin, Auftrag der Handlungssituation]?". In der
  Sicherung bekommt die Frage eine eigene Spalte, im Erwartungshorizont je Thema eine Antwort.
- **Ein Handlungsergebnis bündelt.** Teilprodukte (Plakat, Steckbrief, Prüfplan, Matrix) sind
  Arbeitsschritte und Informationsquellen, **keine eigenen Bewertungsgegenstände**. Das hält
  die Bewertung schlank. Wird das Ergebnis in einem Gespräch vertreten, bekommt das Gespräch
  eine Rückmeldung nach Kriterien.
  **Ausnahme:** Nennen die curriculare Vorgabe, die Leistungsbewertung der LS oder ein
  Beschluss des Bildungsgangs **Teilleistungen** ausdrücklich (z. B. Dokumentation,
  Präsentation, Projektprozess, Umsetzung in Projekten des BG), werden sie getrennt bewertet:
  mit offengelegten Kriterien und Gewichten, **ohne Doppelbewertung** desselben Kriteriums und
  mit ausgewiesenem Einzelanteil bei Gruppenarbeit.
- **Wiederkehrende Elemente:** Was der Einstieg aufwirft (Vermutungen, Behauptung der Kundin),
  wird beim Überprüfen wieder aufgegriffen und kann im Gespräch als Einwand zurückkommen.
- **KI-Auskunft als Situationsmaterial:** Die Kundin bringt den Rat eines KI-Chatbots mit.
  Die Lernenden prüfen ihn: Was stimmt, was fehlt, was wäre die Folge, wenn sie danach handelt?
  Lernziel (Medienbildung): Allgemeine Auskünfte ohne Anlagendaten ersetzen keine Diagnose;
  geprüft wird an Befunden, Herstellerangaben und Normen. Die Auskunft selbst formulieren
  (fiktiv, teils richtig, teils unvollständig), keine echte Chatbot-Ausgabe übernehmen.
- **Wahl** von Thema und Produktform (Plakat, Steckbrief, Erklärvideo) – Ziel und
  Handlungsergebnis bleiben für alle gleich.

## 7. Zeitvarianten und Ersatzwege

- **Puffer** in der Phasenplanung ausweisen; Phasenzeiten plus Puffer = Zeitrichtwert.
- **Kürzungsoption:** Für den Fall weniger Stunden festlegen, was gekürzt wird, mit Minuten je
  Baustein (z. B. Steckbrief statt Plakat −20 min, eine Gesprächsrunde statt zwei −10 min).
  Nie gekürzt werden **Entscheiden, Überprüfen (mit Überarbeitung) und Reflektieren der
  Lernsituation** sowie die Sicherung des Handlungsergebnisses – je Lernsituation, nicht je
  Unterrichtseinheit.
- **Handlungskreis über mehrere Einheiten**: Der
  Kreis wird je Lernsituation geschlossen, nicht je 90 Minuten. Die Phasen werden auf die
  Einheiten verteilt (z. B. Einheit 1: Informieren, Planen, Entscheiden · Einheit 2:
  Durchführen · Einheit 3: Überprüfen, Reflektieren). Jede Einheit endet an einer
  Sollbruchstelle mit einem gesicherten Zwischenergebnis und sagt, womit die nächste beginnt.
  Die letzte Einheit überprüft und reflektiert das Handlungsergebnis der **ganzen**
  Lernsituation; Bewertungskriterien, KI-Regeln und Selbsteinschätzung stehen einmal am
  Anfang der Lernsituation. Die KI-Regeln legen den Rahmen (Klassenebene); je Einheit und
  Aufgabe sagen Zeichen und kurze Begründung, wo KI genutzt wird und wo nicht
  (`ki-vereinbarungen.md`, falls vorhanden).
- **Sollbruchstelle zwischen Phasen** auch im Schülermaterial markieren („Endet der Block hier,
  beginnt die nächste Stunde mit …").
- **Ersatzweg bei fehlender Ausstattung:** Ist keine Übungsanlage frei, läuft der praktische Teil
  als Planspiel oder Simulation mit derselben Dokumentation (z. B. Arbeitsbericht). So bleibt
  das Handlungsergebnis erreichbar – das hilft auch bei den Prüffragen zum Distanzunterricht.

## 8. Phasencheck (Ergänzung zum Analysebogen)

Die 16 Kriterien des Analysebogens prüfen die Phasen nicht einzeln. Der Phasencheck ergänzt
sie. Er ist **kein Kriterium der Leitlinie** und wird getrennt vom Analysebogen ausgewiesen.
Skala: ✅ erkennbar · ⚠️ angelegt, aber dünn · ❌ fehlt.

| Nr. | Bereich | Prüffrage | bei ⚠️/❌ |
|---|---|---|---|
| 1 | Informieren | Werden Vorwissen oder Vermutungen aktiviert und wird Fachwissen an die Handlungssituation zurückgebunden? | Abschn. 6 |
| 2 | Planen | Planen die Lernenden selbst (Vorgehen, Prüfplan, Kriterien), und verrät kein Auftrag die Lösung? | Abschn. 1 |
| 3 | Entscheiden | Werden mindestens zwei Alternativen nach offengelegten Kriterien abgewogen und wird die Entscheidung schriftlich begründet? | Abschn. 2 |
| 4 | Durchführen | Entsteht das Handlungsergebnis – mit praktischem Anteil oder Ersatzweg, wo der Beruf es verlangt? | Abschn. 7 |
| 5 | Überprüfen | Prüfen die Lernenden nach Kriterien (Raster, Kontrollwerte), mit Zeit zum Überarbeiten? | Abschn. 3 |
| 6 | Reflektieren | Gibt es mindestens eine Transfer- und eine Selbstbezugsfrage und einen Anlass, den eigenen Lernfortschritt zu sehen? | Abschn. 4 |
| 7 | Lernhürden | Sind Lernhürden mit Gegenmaßnahme und Ort im Material dokumentiert? | Abschn. 5 |
| 8 | Leistungsbewertung | Sind Bewertungsgegenstände, Kriterien, Gewichte und – bei Gruppenarbeit – der Einzelanteil offengelegt, bevor die Lernenden arbeiten? | Abschn. 6 |
| 9 | Leitidee | Ist eine didaktische Leitidee der Lernsituation formuliert (unter *didaktisch-methodische Kommentare*), exemplarisch und bedeutsam, und lassen sich die Phasen auf sie beziehen? | `didaktische-leitidee.md`, falls vorhanden |
| 10 | Lernzeit | Ist der Kreis innerhalb der Lernsituation geschlossen (auch über mehrere Einheiten)? Ist die Zeitplanung vollständig (Input, Lesen, Aufbau, Übergänge), der Kernweg ausgewiesen, und jede fachsystematische Phase begründet und zurückgebunden? | Abschn. 7 und 12 |

## 9. Projekt-Lernsituation mit Lastenheft

Für längere Lernsituationen (20–60 h), typisch im Beruflichen Gymnasium und in Fachschulen:
Ein fiktiver Auftraggeber übergibt ein **Lastenheft** (was und wofür, Randbedingungen), die
Lernenden antworten mit einem **Pflichtenheft** (wie) und liefern ein Handlungsergebnis
(Dokumentation, Prototyp, Simulation, Präsentation).

| Phase | Baustein | Material |
|---|---|---|
| Informieren | Lastenheft analysieren: Anforderungen, Randbedingungen (Budget, Normen, Termine), offene Fragen an den Auftraggeber | Lastenheft, Fragenliste |
| Planen | Pflichtenheft mit Lösungsideen; Projektstrukturplan, Arbeitspakete mit Verantwortlichen, Meilensteine; Kriterien für das Ergebnis | Vorlage Pflichtenheft, Projektplan |
| Entscheiden | Lösungsvarianten nach technischen, ökologischen und ökonomischen Kriterien (Abschn. 2); Freigabe des Pflichtenhefts in einem Meilensteingespräch | Entscheidungsmatrix |
| Durchführen | Arbeitspakete umsetzen (Rechnung, Konstruktion, Programm, Experiment, Simulation); Projektjournal | Infomaterial, Hilfekarten, Projektjournal |
| Überprüfen | Soll-Ist-Abgleich mit Lastenheft und Pflichtenheft; Test, Peer-Review, Zwischenpräsentation | Prüfliste aus dem Lastenheft |
| Reflektieren | Projekt-Retrospektive: Vorgehen, Zusammenarbeit, Annahmen, die das Ergebnis bestimmt haben | Reflexionsauftrag |

Regeln:
- **Das Lastenheft nennt Ziele, nicht die Lösung.** „Ganzjährige Versorgung aus eigener
  PV-Erzeugung“ lässt Alternativen zu; „mittels Wasserstoffs“ legt die Technik fest. Soll die
  Technik vorgegeben sein, wenigstens Varianten innerhalb der Technik offenlassen.
- **Jede Anforderung führt zu einem Teil des Handlungsergebnisses** und zu einem Erwartungsteil
  im Erwartungshorizont. Fachkompetenzen ohne Lastenheftpunkt (z. B. „Nachhaltigkeit
  beurteilen“) laufen ins Leere.
- **Ein roter Faden statt sechs Inseln:** heterogene Anforderungen (Baustelle, CNC-Teil, App)
  über eine Systemfrage verbinden; künstlich angehängte Teilaufgaben als solche begründen.
- **Projektmanagement lernen, nicht nur verlangen:** Meilensteine, Rollen, Journal einführen
  (im BG mit ING2 und Fach Praxis abstimmen).
- **Fiktiver Auftraggeber:** erkennbar fiktiv, keine echten Telefonnummern, E-Mail mit
  `example.org`. Platzhalter für die Lehrkraft vor der Ausgabe entfernen.
- **Der Erwartungshorizont zeigt mehrere vertretbare Lösungen** oder die Kriterien, an denen
  jede Lösung gemessen wird – nicht nur „eine mögliche Lösung“.
- **Bewertung:** Teilleistungen (Dokumentation, Präsentation, Prozess) nach Abschn. 6;
  Fachgespräch je Arbeitspaket für den Einzelanteil.

## 10. Hypothesen- und Experiment-Lernsituation

Die Lernenden stellen eine prüfbare Vermutung auf, planen einen Versuch oder eine Messung,
werten aus und vergleichen mit der Vermutung. Geeignet für Wirkungsgrade, Kennlinien,
Werkstoffeigenschaften, Sensorik.

- **Vorhersage vor dem Versuch** schriftlich (Hypothese mit Begründung), danach Abgleich:
  bestätigt, widerlegt, offen – mit Erklärung.
- **Variablen** benennen (unabhängig, abhängig, konstant gehalten); mindestens eine Variable
  wählen die Lernenden selbst.
- **Erwartungswerte aus Vorversuch oder Rechnung mit physikalischer Grenze**
  (`experimentsicherheit.md` Abschn. 5, falls vorhanden): Ein „mögliches Ergebnis“, das gegen Energieerhaltung
  oder Faraday verstößt, lehrt das Falsche.
- **Fehlerbetrachtung** mit Messunsicherheit und Vergleich Labor ↔ Technik („Warum liegt der
  Wirkungsgrad im Versuch bei 30 %, in der Anlage bei 70 %?“) – das ist die Rückbindungsfrage.
- **Sicherheit vor Ausgabe:** Gefährdungsbeurteilung, Vorversuch, Freigabezeile der Lehrkraft
  (`experiment-planen`).

## 11. Urteilsbildung und Technikfolgenabschätzung

Für gesellschaftlich umstrittene Technik (Energieanlagen, Mobilität, KI, Automatisierung):
Die Lernenden schätzen Folgen ab, prüfen Hypothesen an Quellen und bilden ein eigenes Urteil.

| Phase | Baustein |
|---|---|
| Informieren | Technik und Systemgrenze (Lebenszyklus: Herstellung, Betrieb, Rückbau); Beteiligte und Betroffene sammeln |
| Planen | Hypothesen zu Folgen formulieren (positiv und negativ), Prüfverfahren je Hypothese festlegen (Daten, Rechnung, Literatur, Befragung) |
| Entscheiden | Hypothesen auswählen, Bewertungsmethode und Wertbereiche festlegen (in Anlehnung an VDI 3780) |
| Durchführen | Hypothesen prüfen mit Quellenmappe (Typ und Interessenlage, `quellenbewertung.md`, falls vorhanden); Ergebnis je Hypothese: bestätigt, widerlegt, offen |
| Überprüfen | Anhörung bzw. Bürgerdialog als Rollenspiel mit mehreren Perspektiven (`rollenspiel.md`, falls vorhanden); Abgleich der Ergebnisse mit den Hypothesen |
| Reflektieren | eigenes Urteil und eigene Rolle (z. B. Ingenieurteam im Auftrag eines Unternehmens) reflektieren |

Regeln:
- **Ergebnisoffen rahmen** (Beutelsbacher Konsens, `querschnittsaufgaben.md`, falls vorhanden). Ein Auftrag
  „Einwände entkräften“ oder „Akzeptanz schaffen“ gibt das Urteil vor. Besser: Auftraggeber
  wünscht eine **ehrliche** Folgenabschätzung, weil er Vertrauen braucht.
- **Hypothese ≠ Meinung:** prüfbar formulieren („Der Schallpegel überschreitet am nächsten
  Wohnhaus nachts den Richtwert“ statt „Windräder machen krank“).
- **Bestätigte Bedenken bleiben bestätigt** und führen zu Maßnahmen, die negative Folgen
  verringern; Zielkonflikte werden benannt, nicht aufgelöst.
- **Musterlösungen** (Schulungsunterlagen, Transkripte) sind selbst ausgewogen und fachlich
  geprüft; KI-erzeugte Muster werden gekennzeichnet und wie ein Erwartungshorizont geprüft.
- Werkzeug: `technikfolgen-abschaetzen` (Dossier, Quellenmappe, Rollenkarten, Prüfskript).

## 12. Lernzeit effizient nutzen – fachsystematische und lehrkraftgeführte Lernphasen

Wo es zweckdienlich und gut begründet ist, darf
fachsystematisch und lehrkraftgeführt (auch frontal) unterrichtet werden. Die Leitlinie sieht
das ausdrücklich vor (Lernsituation „kann fachsystematische Lernphasen enthalten“, Lehrkraft
in informierender Rolle, „Unterrichtszeit effizient nutzen“;
`schucu-bbs-2024.md` Abschn. 2, falls vorhanden). Eigenständiges Entdecken ersetzt Anleitung nicht überall: Bei geringem
Vorwissen belastet vollständig offenes Erarbeiten das Arbeitsgedächtnis, ausgearbeitete
Beispiele wirken dann besser; mit wachsender Erfahrung kehrt sich das um (Fading,
`gestaltungsprinzipien.md` im Skill `unterrichtsmaterial-erstellen`).

**Zweckdienlich, wenn …**

| Anlass | Beispiel |
|---|---|
| neues Verfahren oder neue Syntax bei wenig Vorwissen | Lösungsbeispiel mit lautem Denken („Vormachen“), erste Zeilen Code live |
| Werkzeug- oder Sicherheitsunterweisung | Aufbau einer Messschaltung, Einrichtung des Testwerkzeugs |
| gemeinsame Notation oder Fachsprache nötig | Schreibweise einer Tabelle, Bezeichner, Norm |
| Fehlvorstellung nach einer Vorhersage klären | die Lösung der Eingangsfrage am Fall zeigen |
| deutlicher Zeitgewinn gegenüber Selbststudium | zehn Minuten Demonstration statt 25 Minuten Lesen |

**Form**
- **Höchstens 15–20 Minuten am Stück**, danach sofort Anwendung durch die Lernenden an einem
  **anderen** Fall als dem vorgemachten (vormachen → gemeinsam → selbst).
- Eine **Rückbindungsfrage** (Abschn. 6) an die Handlungssituation und ein **gesichertes
  Ergebnis** (Merkkarte, Tafelbild, Beispieldatei) – nicht nur Zuhören.
- Im Distanzunterricht als kurzer Screencast oder Live-Impuls; die Lernenden können anhalten
  und nachfragen.
- Das Lösungsbeispiel zeigt einen **analogen** Fall, nicht die Lösung der eigenen Aufgabe.

**Nicht zulässig**
- Die **Entscheidung**, die **Überprüfung** oder die **Reflexion** der Lernenden ersetzen:
  Sie bleiben deren Leistung (Abschn. 2–4).
- Ein Unterrichtsgespräch oder einen Vortrag zur Hauptphase machen.
- Die Begründung weglassen: „weil es schneller geht“ genügt nicht, wenn die Lernenden den
  Weg selbst finden könnten und dies das Lernziel ist.

**Dokumentieren**
- In den *didaktisch-methodischen Kommentaren* der Lernsituation bzw. den Didaktischen
  Hinweisen der Lektion eine Zeile: `**Fachsystematische Phase**: … (Dauer), weil …`.
- Im Phasencheck Zeile 10 prüfen. Für Entwürfe zum Unterrichtsbesuch und Prüfungsunterricht
  gelten die Kriterien des Entwurfsbogens weiter (u. a. überwiegend aktive Lernzeit); die
  fachsystematische Phase wird dort wie gewohnt begründet (Skill `unterrichtsentwurf-erstellen`).

## Anhang: references/methodenrepertoire.md

# Methodenrepertoire und Varianzregeln

Übernommen und verdichtet aus der Referenz *Didaktik-Methodik* der `lernfeld-werkstatt`;
ergänzt um die Begriffe der Leitlinie SchuCu-BBS 2024. Nicht alles in jeder
Stunde – aber über eine Sequenz bzw. Lernsituation hinweg **alle Familien** mindestens einmal.

## Inhalt
1. Methodenfamilien je Phase
2. Varianzregeln für Sequenzen
3. Stundenrhythmus und Kernweg
4. Einstiegsauftrag (AFB I) in wechselnder Form
5. Transfer in den Ausbildungsbetrieb („Mein Betrieb")
6. Gesprächssimulation im Kugellager

Muster für ganze Lernsituationen (Diagnose, Entscheiden, Überprüfen, Reflektieren):
`lernsituationsmuster.md`.

---

## 1. Methodenfamilien je Phase

| Phase | Methoden (Auswahl) |
|---|---|
| **Einstieg** (induktiv: vom Fall zur Regel) | Bildimpuls · Zitat einer Person aus dem Betrieb · Widerspruch/Streitgespräch · Falschaussage („Stimmt das?") · Behauptung oder KI-Auskunft der Kundschaft („Reicht das?") · Vermutungen sammeln (Plakat bleibt hängen) · Zahl des Tages · Artefakt auf dem Tisch (Auftrag, Rechnung, Messprotokoll, defektes Bauteil) · Blitzumfrage · Mini-Rollenspiel · Fehlerbeleg |
| **Erarbeitung** | Textarbeit mit Leitfragen · Gruppenpuzzle · Stationenlernen · Placemat · Lernen durch Lehren · Expertenrunde · Fallanalyse · Prüfplan mit Befundkarten auf Anforderung · Entscheidungsmatrix · Dokumentenprüfung gegen ein Regelwerk (Checkliste, Norm, Herstellerangabe) · Strukturlegetechnik · Messung/Versuch · Rollenspiel · Pro-Contra-Debatte · Expertenbefragung (Interview mit Fachleuten, vorbereitete Fragen) · Experiment mit Hypothese · Simulation (Software) |
| **Sicherung** | Galerierundgang mit Rückbindungsfrage („Was bedeutet das für …?") · Think–Pair–Share · Merksatz selbst formulieren · Lückenraster · Ein-Satz-Zusammenfassung · Begriffsnetz · Fehlersuche im Musterprodukt · Abgleich mit den Anfangsvermutungen · Quiz (Papier oder H5P) |
| **Vertiefung / Transfer** | Anwendung auf den Betrieb bzw. Auftraggeber der Handlungssituation · Vergleich mit einem zweiten Betrieb · „Mein Betrieb" (Abschn. 5) · Beratungsgespräch simulieren (Kugellager, Abschn. 6) · KI-Auskunft fachlich prüfen · Produkt bauen (Arbeitsplan, Prüfprotokoll, Steckbrief, Kundeninformation) · Kriterienraster anwenden · Peer-Check mit anschließender Überarbeitung |
| **Abschluss** | Selbstcheck-Tabelle („kann ich · unsicher · muss ich üben") · Selbsteinschätzung vom Anfang vergleichen · Reflexionsfrage (Transfer oder Selbstbezug) · Blitzlicht · Zielscheibe · Exit-Ticket · Ausblick auf das Handlungsergebnis |

Sozialformen: Einzel · Partner · Gruppe (3–4) · Plenum · Stationen · Markt · Kugellager.

**Grenze der Induktion:** Wo Induktion künstlich würde (Aufbau einer Norm, Gliederung eines
Formulars), ist eine kurze deduktive Passage erlaubt – nie am Anfang einer Lernsituation (in
Folgestunden zulässig, wenn das Problem steht), und der Anwendungsfall danach ist Pflicht. Eine
begründete fachsystematische Phase (Lösungsbeispiel, Demonstration, höchstens 15–20 min am
Stück) ist zulässig, wo sie Lernzeit spart (`lernsituationsmuster.md` Abschn. 12, falls vorhanden).

## 2. Varianzregeln für Sequenzen (Typ S)

Eine Übersicht wird **beim Planen geführt**, nicht nachträglich rekonstruiert:

| Stunde | Einstieg | Erarbeitung | Sicherung | Vertiefung | Sozialformen |
|---|---|---|---|---|---|
| 1 | Artefakt | Textarbeit + Raster | Think–Pair–Share | Anwendung im Betrieb | EA · PA · PL |
| 2 | Falschaussage | Gruppenpuzzle | Galerierundgang | Kriterienraster | GA · PL |

1. Kein Einstiegstyp zweimal hintereinander.
2. Je Lernsituation (bzw. Sequenz ab vier Stunden) mindestens **drei verschiedene
   Erarbeitungsmethoden** und mindestens **eine kooperative Großform** (Gruppenpuzzle,
   Stationen, Markt, Rollenspiel, Kugellager).
3. Mindestens drei begründete Sozialformwechsel je Doppelstunde.
4. Handlungsergebnisse variieren – nicht fünfmal „Plakat".
5. Die Form des Einstiegsauftrags rotiert (Abschn. 4).

## 3. Stundenrhythmus und Kernweg

Richtzeiten (Erfahrungswerte einer Lernfeldreihe; an Lerngruppe und Ziel anpassen):

| Phase | 90 min | 45 min | Funktion |
|---|---|---|---|
| Einstieg | 10' | 5' | Problem aufwerfen, Vorwissen aktivieren |
| Erarbeitung | 25' | 12' | Material erschließen, Fachwissen erarbeiten |
| Sicherung | 15' | 10' | Ergebnisse zusammentragen, Merksatz, Abgleich |
| Vertiefung | 25' | 8' | Anwendung auf den Fall, Transfer |
| Abschluss | 15' | 10' | Selbstcheck, Ausblick |

Stunden, in denen das Handlungsergebnis entsteht, verschieben Gewicht nach hinten
(z. B. 10' / 25' / 10' / 25' / 20').

**Kernweg:** Was auf dem Blatt steht und was in der Stunde bearbeitet wird, sind zwei Dinge. Der
Kernweg (60–65 min je Doppelstunde) trägt die Stunde; alles darüber ist gekennzeichnet als
*Zusatz*, *wenn Zeit bleibt* oder *Praxischeck*. Die Minutensumme des Kernwegs steht als erster
Lehrerhinweis. *Erfahrungswert:* Ohne diese Trennung lagen in einer Reihe 14 von 21
Arbeitsblättern über dem Zeitbudget.

## 4. Einstiegsauftrag (AFB I) in wechselnder Form

Damit die Sicherung des Grundverständnisses über viele Stunden nicht zur Routine wird:

| Form | taugt für |
|---|---|
| Lückentext mit Wortspeicher (mit überzähligen Wörtern) | Fachbegriffe an der richtigen Stelle |
| Richtig/Falsch **mit Berichtigung** | hebt sich vom Raten ab |
| Zuordnung mit Buchstabenangebot | Begriff ↔ Bedeutung, Fall ↔ Kategorie |
| Begriffe in eigenen Worten | Gegentest zum Abschreiben |
| W-Fragen als Kurzantwortkacheln | schnelle Verständnissicherung |

Der Auftrag wird als **Betriebsauftrag erzählt** („Die Meisterin bittet Sie, … zu prüfen"),
nie als „Zusammenfassung" überschrieben. Ab dem 2. Ausbildungsjahr (im BG ab der Qualifikationsphase) darf die
Reproduktionsebene auch der Informationsteil tragen (Begriffstabelle, Wortspeicher), wenn der
erste Auftrag eine gestufte Hilfe bietet.

## 5. Transfer in den Ausbildungsbetrieb („Mein Betrieb")

Ein Erkundungsauftrag in den eigenen Ausbildungsbetrieb verbindet die Lernorte und
differenziert von selbst. Regeln:

- Der Auftrag muss **im Betrieb beantwortbar** sein (jemanden fragen, ein Dokument ansehen).
- Nur dort einsetzen, wo **alle** Betriebe etwas beitragen können; sonst seltener (z. B. jede
  dritte Stunde).
- **Drei Zugänge**, damit niemand Auskunft über den eigenen Betrieb geben *muss*:

| Situation | Bezugsgröße |
|---|---|
| Betrieb passt zum Thema | eigener Betrieb |
| Betrieb ist anders aufgestellt | Vergleichsbetrieb aus der Handlungssituation |
| Betrieb gibt nichts her oder soll nicht Thema sein | Materialkasten auf dem Blatt mit Angaben des Vergleichsbetriebs |

Der dritte Zugang ist Schutz, keine Bequemlichkeit: Wer im eigenen Betrieb Missstände sieht oder
aus einem Kleinstbetrieb kommt, soll nicht vor der Klasse dazu Stellung nehmen müssen.

## 6. Gesprächssimulation im Kugellager

Übt Beratung, Übergabe oder Einweisung mehrmals hintereinander mit wechselnden Partnern.

- **Aufbau:** Innen- und Außenkreis, Paare sitzen sich gegenüber. Innen spielt die Fachkraft,
  außen die Kundin oder der Kunde mit einer **Rollenkarte** (Typ: sparsam, vorinformiert,
  besorgt, planend, eilig – Material im Skill `unterrichtsmaterial-erstellen`).
- **Ablauf je Runde (8–12 min):** Gespräch 4–6 min → die Kundenrolle füllt den
  Beobachtungsbogen Gespräch und gibt Rückmeldung (zwei Stärken, ein nächster Schritt) → der
  Außenkreis rückt einen Platz weiter, neue Karte. Nach der Hälfte die Rollen tauschen.
- **Variante Trio** (Fachkraft, Kundin, Beobachtung), wenn die Rückmeldung genauer sein soll
  oder der Raum keinen Kreis zulässt.
- **Vorbereitung:** Redemittel und Wortspeicher mit Kundensprache (`sprachsensibel-ueberarbeiten`);
  Üben zu Hause mit einem KI-Dialogpartner (`agiles-lernen-mit-ki`, Rollenspiel).
- **Sicherung:** zwei bis drei gelungene Formulierungen im Plenum sammeln.
- **Zeit:** zwei Runden mit Rollentausch ≈ 25 min; Kürzung: eine Runde.

## 7. Methoden für Projekt-Lernsituationen

| Methode | Zweck | Hinweise |
|---|---|---|
| **Kickoff** | Lastenheft verstehen, Fragen an den Auftraggeber sammeln | Lehrkraft in der Rolle des Auftraggebers beantwortet Fragen; Ergebnis: Fragenliste und erstes Pflichtenheft |
| **Stand-up** (5–10 min) | Stand, Hindernisse, nächster Schritt je Gruppe | zu Beginn jeder Arbeitsphase; Hindernisse notieren, nicht sofort lösen |
| **Meilenstein-Gespräch** | Entscheidungen freigeben, Rückkopplung | 10 min je Gruppe; Kriterien vorher bekannt; Ergebnis ins Projektjournal |
| **Fachgespräch je Arbeitspaket** | Einzelanteil sichtbar machen | 5–8 min je Person zur eigenen Teilaufgabe (Kolloquium); Fragen aus dem Bewertungsplan |
| **Zwischenpräsentation / Peer-Review** | Ergebnis nach Kriterien prüfen und überarbeiten | Gruppen prüfen sich gegenseitig mit dem Raster; Überarbeitungszeit einplanen |
| **Pro-Contra-Debatte, Anhörung** | Positionen und Zielkonflikte vertreten | Rollen zuweisen, Rollentausch; kein „Gewinner“ (`rollenspiel.md` im Skill `agiles-lernen-mit-ki`) |
| **Retrospektive** | Vorgehen und Zusammenarbeit auswerten | „Was behalten wir bei? Was ändern wir? Welche Annahme hat das Ergebnis am stärksten bestimmt?“ |

**Transfer ohne Ausbildungsbetrieb** (vollzeitschulisch): Übertragung auf ein zweites System,
auf die eigene Lebenswelt (Haushalt, Schule, Kommune) oder auf eine Hochschul- bzw.
Berufsperspektive statt „Mein Betrieb“.

## Anhang: references/operatoren-afb.md

# Operatoren, Anforderungsbereiche (AFB) und Taxonomiestufen

Arbeitsliste für berufsbildende Schulen. Die Zuordnung ist ein **Regelfall, kein Automatismus**:
Welche Stufe eine Aufgabe tatsächlich fordert, hängt vom Unterricht davor ab (Ist das
Verfahren geübt → Anwenden; ist es neu → Analysieren/Erschaffen). Ordnet ein Lehrplan,
eine Prüfungsordnung oder die Fachgruppe Operatoren anders zu, gilt deren Liste.

**Abweichende Liste im Beruflichen Gymnasium (Abitur, Klausuren der Qualifikationsphase):** Dort
gelten die Operatoren der EPA Technik mit eigener AFB-Zuordnung (`operatoren-epa-technik.md`, falls vorhanden).
Wichtigste Unterschiede: *begründen* nur AFB II, *dokumentieren* AFB III, *beschreiben* und
*nennen* nur AFB I; *erstellen*, *programmieren*, *implementieren*, *testen* sind keine
EPA-Operatoren (dort *entwickeln*, *entwerfen*, *überprüfen* verwenden oder als erweiterte
Operatoren im Lehrermaterial ausweisen).
**Im Fach Berufliche Informatik** gilt die EPA Berufliche Informatik mit eigener Liste (dort sind
*erstellen*, *implementieren*, *testen*, *erweitern*, *vervollständigen* Operatoren; Abschnitt
*Berufliche Informatik* in `operatoren-epa-technik.md`, falls vorhanden).

Spalten: **AFB** = Anforderungsbereich I (Reproduktion), II (Reorganisation und Transfer),
III (Reflexion und Problemlösung). **Bloom** = Stufe der revidierten Taxonomie nach
Anderson/Krathwohl (1 Erinnern · 2 Verstehen · 3 Anwenden · 4 Analysieren · 5 Bewerten ·
6 Erschaffen).

## AFB I – Reproduktion

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| nennen, angeben, aufzählen | Begriffe, Daten, Fakten ohne Erläuterung wiedergeben | 1 |
| bezeichnen, benennen | Bauteile, Größen, Symbole korrekt mit Fachbegriff versehen | 1 |
| wiedergeben | Inhalte sachlich zutreffend in eigenen Worten formulieren | 1–2 |
| beschreiben | Sachverhalt, Ablauf oder Aufbau strukturiert und fachsprachlich wiedergeben | 2 |
| darstellen | Zusammenhänge geordnet wiedergeben, auch grafisch (Skizze, Tabelle, Schema) | 2 |
| zusammenfassen | Kernaussagen komprimiert und strukturiert wiedergeben | 2 |
| skizzieren | Wesentliches vereinfacht grafisch oder in Stichpunkten darstellen | 2 |

## AFB II – Reorganisation und Transfer

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| erklären | Ursache–Wirkung bzw. Funktionsweise nachvollziehbar machen | 2 |
| erläutern | Sachverhalt beschreiben **und** durch Zusatzinformationen/Beispiele verständlich machen | 2–3 |
| zuordnen, einordnen | Sachverhalte begründet in einen Zusammenhang oder eine Systematik stellen | 2–3 |
| anwenden | Bekanntes Verfahren auf einen neuen, ähnlichen Fall übertragen | 3 |
| berechnen, bestimmen, ermitteln | Ergebnis mit nachvollziehbarem Lösungsweg und Einheiten gewinnen | 3 |
| auswählen | aus Alternativen kriteriengeleitet das Passende festlegen (Tabellenbuch, Katalog, Datenblatt) | 3–4 |
| erstellen, anfertigen | Produkt nach Vorgaben anfertigen (Schaltplan, Arbeitsplan, Prüfprotokoll, Stückliste) | 3 |
| durchführen | Verfahren, Messung, Prüfung fachgerecht ausführen und dokumentieren | 3 |
| auswerten | Daten, Messwerte, Diagramme interpretieren und Schlüsse ziehen | 4 |
| analysieren, untersuchen | Bestandteile, Strukturen, Fehlerursachen systematisch herausarbeiten | 4 |
| vergleichen, gegenüberstellen | Gemeinsamkeiten und Unterschiede kriteriengeleitet herausarbeiten | 4 |
| herausarbeiten | aus Material bestimmte Sachverhalte erkennen und darstellen | 4 |
| ableiten | aus Gegebenem begründet eine Folgerung oder Größe gewinnen | 4 |
| modellieren | Sachverhalt in ein Modell überführen (Ablaufplan, GRAFCET, Struktogramm, Ersatzschaltbild) | 4–6 |
| implementieren, programmieren | Modell/Konzept in einer konkreten Umgebung lauffähig umsetzen | 3–6 |

## AFB III – Reflexion und Problemlösung

| Operator | Erwartete Leistung | Bloom |
|---|---|---|
| prüfen, überprüfen | Aussagen, Ergebnisse oder Lösungen an Kriterien/Normen messen und Abweichungen begründen | 5 |
| beurteilen | zu einem Sachverhalt ein begründetes **Sachurteil** nach Kriterien fällen | 5 |
| bewerten | wie beurteilen, zusätzlich mit begründetem eigenem Standpunkt bzw. Wertmaßstab | 5 |
| begründen | Aussage oder Entscheidung durch Argumente und Fachwissen stützen | 4–5 |
| Stellung nehmen, erörtern, diskutieren | Argumente abwägen und zu einem begründeten Ergebnis kommen | 5 |
| reflektieren | eigenes Vorgehen/Ergebnis kriteriengeleitet kritisch prüfen, Konsequenzen ableiten | 5 |
| entwickeln, entwerfen, konzipieren | für ein neues Problem eine eigenständige Lösung erarbeiten | 6 |
| gestalten | eigenständig und kreativ eine Lösung oder ein Produkt ausformen | 6 |
| optimieren | bestehende Lösung begründet verbessern (Kosten, Sicherheit, Energie, Qualität) | 5–6 |
| planen (offen) | Vorgehen für eine offene Problemstellung eigenständig festlegen | 6 |

## Berufspraktische Operatoren in schriftlichen Aufträgen

Für Aufträge, die eine berufliche Handlung vorbereiten, dokumentieren oder kommunizieren. Der
AFB hängt davon ab, ob Form und Verfahren vorgegeben sind (I–II) oder selbst gewählt und
begründet werden müssen (II–III).

| Operator | Erwartete Leistung | AFB | Bloom |
|---|---|---|---|
| berichtigen | falsche Aussage erkennen und fachlich richtigstellen | I–II | 2–3 |
| dokumentieren, protokollieren | Vorgehen, Messwerte und Ergebnisse vollständig und nachvollziehbar festhalten | I–II | 2–3 |
| messen | Größe mit geeignetem Messmittel bestimmen, Messwert mit Einheit angeben | I–II | 3 |
| formulieren, verfassen | adressatengerechten Text verfassen (Kundeninformation, E-Mail, Übergabenotiz) | II | 3 |
| präsentieren | Ergebnis adressatengerecht, strukturiert und fachsprachlich vorstellen | II | 3–4 |
| simulieren | Verhalten eines Systems mit Software oder Modell nachbilden und die Ergebnisse deuten | II | 3–4 |
| experimentieren, einen Versuch durchführen | nach Plan messen, beobachten, dokumentieren und Sicherheitsregeln einhalten | II | 3 |
| eine Hypothese aufstellen, formulieren | eine prüfbare Vermutung mit Begründung formulieren | III | 6 |
| nachweisen | rechnerisch oder experimentell zeigen, dass eine Anforderung erfüllt ist | II–III | 4–5 |

## Wissensarten und Anforderungsbereiche

| Wissensart | Leitfrage | typischer AFB |
|---|---|---|
| Sachwissen | Was muss man kennen? | I – nennen, beschreiben, zuordnen |
| Prozesswissen | Wie geht man vor? | II – anwenden, durchführen, erstellen, analysieren |
| Reflexionswissen | Warum so, mit welcher Wirkung? | III – beurteilen, bewerten, begründen, entwickeln |

Material und Prüfungen sollten über Sachwissen hinausgehen: kein Arbeitsblatt nur mit AFB I,
kein erster Auftrag auf AFB III. Verteilungen werden **ausgezählt**, nicht geschätzt.

## Praktische Operatoren (Werkstatt, Labor) – psychomotorische Stufen nach Dave

| Operator (Beispiele) | Stufe nach Dave (1970) |
|---|---|
| nachmachen, unter Anleitung ausführen | 1 Imitation |
| nach Anleitung montieren, einstellen, messen | 2 Manipulation |
| genau, sicher und ohne Hilfe fertigen, prüfen, justieren | 3 Präzision |
| mehrere Arbeitsschritte koordiniert ausführen, Abläufe kombinieren, in Betrieb nehmen | 4 Handlungsgliederung |
| routiniert, situationsangepasst und effizient arbeiten, instand setzen unter Zeitdruck | 5 Naturalisierung |

## Verben für Personale Kompetenz (SchuCu-BBS)

Sozialkompetenz: *stimmen sich ab, wirken mit, beraten, präsentieren adressatengerecht,
geben und nehmen Rückmeldung, übernehmen Verantwortung im Team, vertreten Ergebnisse,
lösen Konflikte sachlich*.
Selbständigkeit: *planen ihr Vorgehen eigenständig, schätzen ein, reflektieren, handeln in
Verantwortung, setzen sich selbstkritisch auseinander, identifizieren Verbesserungspotenziale,
wählen Lernhilfen aus, beachten Arbeitssicherheit eigenverantwortlich*.

## Nicht verwenden (nicht beobachtbar)

*verstehen, kennen, wissen, lernen, begreifen, sich bewusst sein, vertraut sein mit,
Einblick gewinnen, die Bereitschaft entwickeln, die Fähigkeit verbessern*. Ersatz: Was tun die SuS sichtbar, **woran** erkennt man es?

## Faustregeln für Aufgaben

- **Operator + Inhalt + Bedingung:** „Berechnen Sie die erforderliche Kolbenkraft **für
  den Ausschiebezylinder** unter Berücksichtigung eines Wirkungsgrads von 0,85."
- Keine W-Fragen („Was ist …?") in Aufgaben – immer einen Operator.
- Pro Teilaufgabe **ein** Operator; Mehrfachoperatoren („nennen und erläutern") nur, wenn
  beide Leistungen bewertet werden.
- Der Operator legt die Bewertung mit fest: nennen ≈ 1 Punkt je Aspekt, erläutern ≈ 2 Punkte
  je Aspekt, beurteilen = Kriterium + Urteil + Begründung.

## Anhang: references/schucu-bbs-2024.md

# SchuCu-BBS 2024 – Kompaktreferenz

Quelle: Niedersächsisches Kultusministerium, *Leitlinie Schulisches Curriculum berufsbildende
Schulen (SchuCu-BBS) 2024*, Stand Juli 2024; ergänzend die unverbindliche „Leermaske für
Lernsituationen" (NLQ, Stand 08/2023) und der Analysebogen für Lernsituationen.
Wortlaute in Anführungszeichen sind der Leitlinie entnommen.

## Inhalt
1. Handlungskompetenz
2. Vollständige Handlung (6 Phasen) und Rolle der Lehrkraft
3. Bestandteile einer Lernsituation
4. Anforderungen an die Handlungssituation
5. Analysebogen (16 Kriterien)
6. Schulisches Curriculum: Planungsablauf
7. Begriffswechsel gegenüber älteren Vorlagen

---

## 1. Handlungskompetenz

- „Ziel des handlungsorientierten Unterrichts ist die Entwicklung von Handlungskompetenz" –
  im berufsbezogenen **und** berufsübergreifenden Lernbereich.
- Handlungskompetenz entfaltet sich laut DQR in den Dimensionen
  - **Fachkompetenz** = Wissen und Fertigkeiten
  - **Personale Kompetenz** = Sozialkompetenz und Selbständigkeit
- „In Handlungskompetenz sind Kommunikations-, Methoden-, Lern- und Medienkompetenz
  immanent." → Sie werden **nicht als eigene Spalte** ausgewiesen, sondern in Fach- bzw.
  Personaler Kompetenz mitformuliert.
- Kompetenzen werden **aktiv** beschrieben: „Die Schülerinnen und Schüler … erfassen …,
  planen …, analysieren und beheben …". Für Personale Kompetenz eignen sich Verben wie
  *begründen, wirken mit, gestalten, schätzen ein, handeln in Verantwortung, reflektieren,
  setzen sich (selbst)kritisch auseinander, identifizieren Verbesserungspotenziale*.

## 2. Vollständige Handlung und Rolle der Lehrkraft

Die Phasen „können je nach Kompetenz der Schülerinnen und Schüler unterschiedlich ausgedehnt
und gewichtet sein", sind nicht immer trennscharf; Üben und Wiederholen ist in jeder Phase
möglich. Fachgruppen dürfen fachdidaktische Vorgehensweisen ausweisen.

| Phase | Leitfrage | Was die SuS tun | Typische Aufgaben der Lehrkraft |
|---|---|---|---|
| **Informieren bzw. Analysieren** | Was soll getan werden? | erfassen und analysieren die zentrale Aufgaben-, Frage- bzw. Problemstellung der Handlungssituation | SuS in die Situation versetzen, selbstgesteuerte Lernprozesse initiieren, Materialien bereitstellen (impulsgebende Rolle) |
| **Planen** | Wie kann die Umsetzung erfolgen? | planen Vorgehen und Dokumentation, beschaffen Informationen, erstellen Arbeits- und Zeitplan, schlagen Handlungsergebnisse vor, legen Kontrollkriterien fest | kooperative Lernprozesse fördern, Vorwissen aktivieren, ggf. weiteres Material bereitstellen |
| **Entscheiden** | Welcher Lösungsweg wird gewählt? | entscheiden sich für Lösungsweg(e), legen Handlungsergebnis, Vorgehen, Rückkopplungsschleifen, Zeitrahmen, Verantwortlichkeiten und Einschätzungskriterien fest | Rückmeldung geben, Fragen beantworten, Entscheidungsprozesse moderieren |
| **Durchführen** | Der gewählte Lösungsweg wird umgesetzt. | bearbeiten die Problemstellung gemäß Entscheidung, berücksichtigen sich ändernde Rahmenbedingungen | Hilfestellungen geben, Materialien/Medien bereitstellen, Unterrichtszeit effizient nutzen, Handlungsergebnis sichern |
| **Überprüfen bzw. Kontrollieren** | Ist das Handlungsergebnis sach- und fachgerecht? | überprüfen das Ergebnis gemäß festgelegten Kriterien, schätzen seine Eignung als Lösung ein | Gesprächsanlässe schaffen, Rückmeldung nach Beurteilungskriterien, Hinweise zur Gewichtung in der Leistungsbewertung |
| **Reflektieren** | Was kann zukünftig verbessert werden? | reflektieren die Bearbeitung, identifizieren Stärken und Verbesserungspotenziale von Lernprozess und Ergebnis | individuelle Reflexion anleiten, mehrperspektivische Unterrichtsbeobachtung nutzen (UB-BBS im Portal PIE-BBS) |

Die Lehrkraft wechselt zwischen **informierender, moderierender, impulsgebender, beratender
und bewertender** Rolle. Lernumgebung: kognitives (Kopf), affektives (Herz) und
psychomotorisches (Hand) Lernen; Ausstattung muss Wechsel von Methoden, Medien und
Sozialformen zulassen. Leistungsbewertung nach „verbindlichen und offengelegten Kriterien".

*Hinweis der Bibliothek (keine Aussage der Leitlinie; Entscheidung der Fachberatung, 23.10.2026):*
Die Leitlinie lässt zu, dass der Handlungskreis mehrere Unterrichtseinheiten umfasst: Die
Phasen „können je nach Kompetenz der Schülerinnen und Schüler unterschiedlich ausgedehnt und
gewichtet sein“, der Zeitrichtwert einer Lernsituation ist die **Summe** der eingeplanten
Stunden, und eine Lernsituation „kann fachsystematische Lernphasen enthalten“. Die Lehrkraft
wechselt auch in die informierende Rolle und soll „Unterrichtszeit effizient nutzen“. Daraus
folgt für die Bibliothek: Der Kreis wird **je Lernsituation** geschlossen, nicht je 90-Minuten-
Einheit; fachsystematische, lehrkraftgeführte Phasen sind zulässig, wenn sie zweckdienlich und
begründet sind und an die Handlungssituation zurückgebunden werden
(`lernsituationsmuster.md` Abschn. 12, falls vorhanden).

## 3. Bestandteile einer Lernsituation

| Element | Anforderung laut Leitlinie |
|---|---|
| **Curriculare Vorgaben** | ausweisen: RRL, RLP (Lernfeld/Lerngebiet/Modul/Qualifizierungsbaustein **mit Titel**), KC |
| **Titel** | „kurz, prägnant und beschreibt die Handlung" (Leermaske: kompetenzorientiert, z. B. „Beton herstellen", „Going green") |
| **Zeitrichtwert** | Summe der eingeplanten Unterrichtsstunden; Bezugspunkt ist der Zeitrichtwert der curricularen Vorgabe |
| **Handlungskompetenz** | Fachkompetenz und Personale Kompetenz konkretisiert (Aktualität, Komplexität, Bearbeitungstiefe, regionale Spezifika); **Inhalte** erschließen sich aus den Kompetenzen und können gesondert ausgewiesen werden |
| **Handlungssituation** | **genau eine pro Lernsituation**; Kern der Lernsituation (Anforderungen s. Abschn. 4) |
| **Handlungsergebnis** | mögliche Lösung der zentralen Aufgaben-, Frage- bzw. Problemstellung; materiell oder nicht-materiell (digitales Produkt, Werkstück, Handlungskonzept, Stellungnahme, Pro-und-Kontra-Diskussion, Beratungsgespräch …); finale Festlegung je nach Kompetenzniveau durch SuS, ggf. Lehrkraft |
| **Vereinbarungen und Hinweise zur Umsetzung** | dokumentieren: didaktisch-methodische Kommentare, Distanzunterricht, Leistungsfeststellung und -bewertung, Materialien, ergänzende Quellen, Lernumgebung |

Eine Lernsituation „kann fachsystematische Lernphasen enthalten", um den Lernprozess zu
unterstützen. Die Handlungssituation darf für die SuS „inhaltlich-sprachlich" angepasst
werden.

## 4. Anforderungen an die Handlungssituation

Die Handlungssituation …
1. initiiert und trägt einen Lernprozess über die **gesamte** Lernsituation,
2. ist bedeutsam – berufsbezogen für die Berufsausübung und/oder Lebenswelt, berufsübergreifend
   für die Lebenswelt und/oder Berufsausübung (ggf. inkl. Studienorientierung),
3. greift mögliche berufliche, persönliche oder gesellschaftliche Erfahrungen der SuS auf,
4. wirft **eine zentrale** Aufgaben-, Frage- bzw. Problemstellung auf,
5. ist exemplarisch,
6. benennt den Rahmen (Modellunternehmen, Einrichtung, Praxis, technisches System, Fall,
   Szenario, reale Situation),
7. berücksichtigt in der Regel soziale Interaktion (Beratungsgespräch, Zusammenarbeit mit
   anderen Auszubildenden …),
8. ermöglicht verschiedene, nach Möglichkeit **offene** Bearbeitungs- bzw. Lösungswege.

*Hinweis der Bibliothek (keine Aussage der Leitlinie):* In vollzeitschulischen Bildungsgängen,
besonders im **Beruflichen Gymnasium**, liest sich Anforderung 2 auch als Studienorientierung
und wissenschaftspropädeutischer Anspruch; Anforderung 7 meint dort Zusammenarbeit in der
Projektgruppe, mit fiktiven Auftraggebern, Expertinnen und Experten oder Stakeholdern
(`berufliches-gymnasium.md`, falls vorhanden).

## 5. Analysebogen für Lernsituationen (16 Kriterien)

Skala: trifft zu · trifft eher zu · trifft eher nicht zu · trifft nicht zu.

**Handlungskompetenz**
1. Die Kompetenzen leiten sich aus den curricularen Vorgaben ab.
2. Die Personale Kompetenz ist konkretisiert (Aktualität, Komplexität, Bearbeitungstiefe,
   regionale Spezifika).
3. Die Fachkompetenz ist konkretisiert (ebenso).
4. Die Inhalte leiten sich aus den curricularen Vorgaben ab.
5. Die Inhalte sind analysiert (Aktualität, Komplexität, Bearbeitungstiefe, regionale
   Spezifika).

**Handlungssituation**
6. initiiert einen Lernprozess.
7. trägt einen Lernprozess über die gesamte Lernsituation.
8. ist für die Berufsausübung und/oder die Lebenswelt der SuS bedeutsam (Lernbereich angeben:
   berufsbezogen/berufsübergreifend). *(BG: Profilfach = berufsbezogener Lernbereich; Studienorientierung mitbewerten.)*
9. greift mögliche berufliche, persönliche und/oder gesellschaftliche Erfahrungen auf.
10. wirft eine zentrale Aufgaben-, Frage- bzw. Problemstellung auf.
11. ist exemplarisch.
12. benennt den Rahmen.
13. berücksichtigt soziale Interaktion.
14. ermöglicht verschiedene und nach Möglichkeit offene Bearbeitungs- bzw. Lösungswege.

**Handlungsergebnis**
15. Das mögliche Handlungsergebnis stellt eine Lösung einer zentralen Aufgaben-, Frage- bzw.
    Problemstellung dar.

**Vereinbarungen und Hinweise zur Umsetzung**
16. Vereinbarungen und Hinweise zur Umsetzung der Lernsituation sind vollständig dokumentiert.

## 6. Schulisches Curriculum: Planungsablauf

Schulisches Curriculum = **didaktisch-methodische Planung** + **Jahresplanung**; Aufgabe
aller im Bildungsgang tätigen Lehrkräfte.

1. Schulspezifische Entscheidungen und Vorgaben berücksichtigen (z. B. Blockmodell,
   Lernumgebung, Präsenz/Distanz, Grundsätze der Leistungsbewertung, Lernortkooperation).
2. Curriculare Vorgaben analysieren (Lerngebiete, Lernfelder, Module, Qualifizierungsbausteine).
3. Inhaltliche Abstimmung über alle Lernsituationen: Titel skizzieren, Personale Kompetenzen,
   Fachkompetenzen und Inhalte zuordnen, Handlungssituationen skizzieren, Zeitrichtwerte
   schätzen, Überschneidungen erfassen, Reihenfolge und Parallelität festlegen, Einführung
   und Vertiefung von Lern- und Arbeitstechniken abstimmen.
4. Lernsituationen planen und dokumentieren (ggf. didaktische Reduktion, Exemplarität);
   **Bildungsgangbeschluss** dokumentieren, bevor Materialien ausgestaltet werden.
5. Materialien und Medien gemeinsam entwickeln bzw. beschaffen, regelmäßig evaluieren.
6. Jahresplanung: zeitliche Reihenfolge, organisatorische Vereinbarungen (Prüfungstermine,
   Praktika …), jährlich anpassen und kommunizieren.
7. Unterricht durchführen und evaluieren (z. B. Instrumente aus PIE-BBS); Curriculum
   regelmäßig überprüfen.

Einordnung in das Qualitätsmanagement: Kernaufgabenmodell KAM-BBS, Qualitätsbereich B
„Bildungsangebote gestalten".

## 7. Begriffswechsel gegenüber älteren Vorlagen

| Ältere Vorlagen / andere Länder | SchuCu-BBS 2024 |
|---|---|
| Handlungsprodukt, Lernergebnis | **Handlungsergebnis** (materiell oder nicht-materiell) |
| Einstiegsszenario, Lernsituationsbeschreibung | **Handlungssituation** (eine pro LS) |
| Selbstkompetenz, Humankompetenz | **Selbständigkeit** (Teil der Personalen Kompetenz) |
| Methoden-/Lernkompetenz als eigene Spalte | immanent in Fach- und Personaler Kompetenz |
| vier Dimensionen Fach-, Methoden-, Sozial-, Selbstkompetenz (KMK-Raster) | **Fachkompetenz** (Wissen, Fertigkeiten) und **Personale Kompetenz** (Sozialkompetenz, Selbständigkeit); Methodenkompetenz wird eingebettet |
| Phasen „Ausführen" und „Bewerten/Reflektieren" | **Durchführen** bzw. **Reflektieren** (Bewertungsanteile ggf. unter Überprüfen bzw. Kontrollieren) |
| Felder „Leistungsbewertung", „Differenzierung", „Anknüpfung LMS/Moodle", „Material & Medien" | unter **Vereinbarungen und Hinweise** (Leistungsfeststellung und -bewertung · didaktisch-methodische Kommentare · Lernumgebung · Materialien und Quellen) |
| 7 Phasen: (Problem-)Analyse, Information, Planung, Entscheidung, Ausführung, Kontrolle/Bewertung, Reflexion/Transfer | **6 Phasen**: Informieren bzw. Analysieren, Planen, Entscheiden, Durchführen, Überprüfen bzw. Kontrollieren, Reflektieren |
| Lern- und Arbeitstechniken, Unterrichtsmaterialien/Fundstelle, organisatorische Hinweise (je eigenes Feld) | gebündelt unter **Vereinbarungen und Hinweise zur Umsetzung der Lernsituation** |
| nur Präsenzunterricht | **Präsenz- und Distanzunterricht** mitdenken |

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.

## Inhalt
1. Vier Regeln
2. Darstellungen statt Text
3. Aufträge offen statt kleinschrittig
4. Was entfällt
5. Richtwerte
6. Rückwärtsprobe vor der Ausgabe

## 1. Vier Regeln

1. **Kurz.** Lernende lesen nur, was sie für den Auftrag brauchen. Kein Satz ohne Aufgabe,
   keine Wiederholung, kein Exkurs.
2. **Offen gestellt.** Ein Auftrag nennt Ziel (Operator), Gegenstand, Ergebnisform und woran
   man merkt, dass man fertig ist. Den Weg finden die Lernenden; Schritte und Gerüste stehen in
   gestuften Hilfen, die man bei Bedarf zieht.
3. **Anschaulich.** Aufgaben arbeiten mit Zeichnungen, Darstellungen und Grafiken: ablesen,
   auswerten, ergänzen, Fehler finden, selbst zeichnen. Was eine Darstellung zeigt, wird nicht
   zusätzlich beschrieben.
4. **Ohne Dekoration.** Nur, was dem Ziel dient (Abschn. 4).

Gekürzt wird Überflüssiges, nicht Fachinhalt: Fachbegriffe, Sicherheitshinweise und
Erfolgskriterien bleiben vollständig.

## 2. Darstellungen statt Text

| Inhalt | Darstellung | so entsteht sie |
|---|---|---|
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen` |
| System, Energie- und Datenfluss, Regelkreis | Blockschaltbild | `fachdiagramm-erstellen` |
| Zusammenhang zweier Größen | Diagramm, Kennlinie mit beschrifteten Achsen | aus gerechneten Werten oder dem Datenblatt als SVG erzeugen (Code), nie geschätzt |
| Vergleich, Kriterien, Kenndaten | Tabelle, Matrix | Markdown-Tabelle |
| Begriffe und ihre Beziehungen | Strukturbild | `fachdiagramm-erstellen` (Bauart `flow`), Tabelle |
| Daten und Software | ER-, Klassen-, Sequenzdiagramm | `fachdiagramm-erstellen` |
| Schaltung, Werkstück | Schaltplan, technische Zeichnung nach Norm | Herstellerunterlage, Tabellenbuch, eigene Zeichnung (Platzhalter mit Quelle) |

Jede Zeichnung entsteht als **SVG aus einer Spec** – nie als Zeichnung aus Zeichen (ASCII-Art) und
nie als Mermaid in der Ausgabe (Skill-Vertrag Abschn. 3).

**Die Darstellung ist Arbeitsgegenstand, nicht Beigabe.** Aufträge, die mit ihr arbeiten
(Beispiele am Gurtförderer GF-2, fiktiv):

| Auftrag | Beispiel |
|---|---|
| ablesen, auswerten | „Ermitteln Sie aus der Kennlinie die Drehzahl bei 80 % Last.“ |
| ergänzen | „Benennen Sie im Anlagenbild die Bauteile ① bis ④.“ |
| Fehler finden | „Der Arbeitsplan in Abb. 2 enthält zwei Fehler. Berichtigen Sie sie.“ |
| selbst zeichnen | „Skizzieren Sie, wie die Spannstation verstellt werden muss.“ |
| vergleichen | „Vergleichen Sie die Gurtlaufbilder A und B.“ |

Regeln:
- **Am Auftrag:** Abbildung direkt bei dem Auftrag, der sie braucht; Beschriftung in die
  Abbildung, Positionsnummern statt Legendentext, wo möglich.
- **Fachlich richtig und normgerecht:** Schaltzeichen, Kennzeichen und Formelzeichen nach
  Norm; Werte hinter Diagrammen sind gerechnet.
- **Schwarzweiß lesbar:** Farbe nur mit Bedeutung und nie allein (zusätzlich Linienart oder
  Beschriftung).
- **Nie erfinden:** keine KI-Bilder, die Fotos, echte Anlagen oder Messkurven vortäuschen. Was
  nicht selbst gezeichnet werden kann (Foto, Herstellerzeichnung, Normauszug), steht als
  Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle/Lizenz]` und ist ein Prüfauftrag.
- **Barrierearm:** Alternativtext (ein Satz) je Abbildung.
- **Platz für Zeichnungen der Lernenden:** in der Druckfassung Kasten oder Raster statt Linien.

Nicht jede Aufgabe braucht ein Bild (Begründung, Gespräch, Reflexion). Ein Arbeitsblatt oder
Infoblatt ganz ohne Darstellung ist aber zu begründen.

## 3. Aufträge offen statt kleinschrittig

**Kleinschrittig – so nicht:**

> 1. Lesen Sie den Wartungsplan (M1).
> 2. Unterstreichen Sie alle Arbeiten, die nach 500 Betriebsstunden fällig sind.
> 3. Übertragen Sie die Arbeiten in die erste Spalte der Tabelle.
> 4. Ergänzen Sie in der zweiten Spalte das Werkzeug.
> 5. Ergänzen Sie in der dritten Spalte die Sicherheitsmaßnahme.
> 6. Addieren Sie die Zeiten.

**Offen – so:**

> **1 Erstellen Sie** den Arbeitsplan für die 500-h-Wartung des GF-2 (Wartungsplan M1,
> Vorlage M3). Fertig, wenn jeder Schritt Werkzeug und Sicherheitsmaßnahme hat und die
> Gesamtzeit unter 2 h liegt.

Die Schritte stehen – kürzer – in den gestuften Hilfen (Impuls → Strategie → Teilschritt →
Kontrolle; Skill `differenzierung-erstellen`). Wer sie braucht, zieht sie. Formate mit weniger
Stufen ordnen zu: Lernlandkarte – Kontrolle ist der Selbstcheck des Lernpostens; Lektion –
Orientierung, Werkzeug, Gerüst entsprechen Impuls, Strategie, Teilschritt, die Kontrolle leisten
Realitätstest und Rückmeldung.

Signale für Kleinschrittigkeit:
- mehr als drei Teilaufgaben a), b), c) an einem Auftrag;
- eine Schrittfolge im Auftrag, die den Lösungsweg vorgibt („zunächst …, dann …,
  anschließend …“) oder eine Reihe kurzer Einzelaufträge, die zusammen einen Auftrag ergeben;
- Lesen, Unterstreichen, Abschreiben oder Übertragen als eigener Auftrag – das sind Mittel,
  kein Ziel;
- Lücken, die sich durch Abschreiben aus dem Text füllen lassen;
- Teilaufgaben, deren Ergebnis die nächste schon verrät.

**Zulässig und nicht kleinschrittig:**
- **Sicherheitsrelevante Schritte** (Freischalten, Stoffe, Mengen, Reihenfolge an der
  Maschine) stehen vollständig und in Reihenfolge – auch in einer offenen Anleitung.
- **Bedienschritte**, die nicht Lernziel sind (Messgerät einstellen, Software starten): kurz,
  am besten als Bildfolge oder Hinweis, nicht als Auftrag.
- **Übungsfolgen** zum Einschleifen einer Routine: gleichartige, je für sich vollständige
  Aufgaben (gelöstes Beispiel → steigend → eingekleidet).
- **Lösungsbeispiel mit Ausblenden:** steht als Beispiel, nicht als Auftrag.
- **Einführende Bildungsgänge** (Berufseinstieg, BVJ): enger geführt über Lösungsbeispiele,
  Hilfen und hohen Anschauungsgrad – nicht über zerlegte Aufträge.

## 4. Was entfällt

| entfällt | stattdessen |
|---|---|
| Schmuckbilder, Cliparts, Symbol- und Stockfotos, Illustrationen ohne Fachinhalt | Abbildung mit Fachinhalt – oder keine |
| Emojis und Symbole ohne Funktion (auch farbige Punkte als Stufenkennung) | Wort; zulässig sind die KI-Zeichen 🚫 💡 🔧 (`ki-vereinbarungen.md`, falls vorhanden), Warn- und Gefahrenzeichen, Ankreuzkästchen ☐ und ✔ ~ ✘ zur Selbsteinschätzung |
| Begrüßung, Motivationssätze („Viel Spaß!“, „Los geht’s!“), Ankündigungen („In diesem Arbeitsblatt lernen Sie …“) | gleich mit Situation oder Auftrag beginnen |
| Einleitung, die den Auftrag vorwegnimmt; Zusammenfassung dessen, was eben dastand | Kernaussage einmal, vorn |
| Exkurse, Anekdoten, Technikgeschichte, „Wussten Sie schon?“-Kästen | als Vertiefung, wenn sie zum Ziel beitragen – sonst streichen |
| dasselbe in Fachwissen, Hilfe und Auftrag | einmal, dort, wo es gebraucht wird |
| Zierrahmen, Farbflächen, Schmuckschriften | klare Überschriften; Kästen nur mit Funktion (Hilfe, Stolperstein, Sicherheit) |
| Angaben für die Lehrkraft (AFB, Kompetenzcodes, Annahmen, Prüfvermerke) | im Lehrerteil |
| Information, die kein Auftrag braucht | streichen |

Keine Dekoration, also bleibend: Kopfzeile (Lernsituation, Zeit, Sozialform), Name und Datum
auf Druckblättern, Erfolgskriterien, Bewertungskasten, KI-Zeichen, Quellen- und
Lizenzangaben, KI-Transparenzhinweis.

## 5. Richtwerte

Orientierung, kein Urteil. ⚠️ Noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

| Element | Richtwert |
|---|---|
| Ausgangslage, Bezug zur Situation | höchstens drei Sätze; besser Situationsmaterial (Störmeldung, Foto, Anlagenbild) |
| Arbeitsauftrag | ein bis zwei Sätze, ≤ ~25 Wörter, Operator zuerst; der Kontext steht einmal in der Ausgangslage |
| Teilaufgaben je Auftrag | höchstens drei |
| Satz | meist unter 15 Wörtern, keiner über 25; die sprachsensible Fassung ist bewusst strenger (über 20 Wörter teilen, `lesbarkeit.py`) |
| Infoblatt | eine Seite, ≤ ~300 Wörter Fließtext, mindestens eine tragende Darstellung |
| Arbeitsblatt (Teil für Lernende) | ≤ ~350 Wörter Fließtext (ohne Tabellen, Code, Abbildungen), mindestens eine Darstellung |
| Situationsmaterial | ≤ ~150 Wörter |
| Hilfekarte | je Stufe ≤ ~40 Wörter, gern als Teilbild oder Skizze |
| Rollenkarte | ≤ ~60 Wörter |
| Lektion (90 min) | ≤ ~1 500 Wörter ohne Code (`lektionsmuster.md`, falls vorhanden) |
| Lernlandkarte (eine Unterrichtseinheit) | ≤ ~1 500 Wörter wie eine Lektion; je Karte nur Auftrag, Material, Hilfen, Selbstcheck |
| sonstiges Material | ≤ ~400 Wörter Fließtext je Datei |

Authentische Dokumente (Betriebsanleitung, Datenblatt, Norm, Quelle der Quellenmappe) bleiben
im Original und zählen nicht mit – sie liegen als Auszug mit Fundstelle bei, nicht
abgeschrieben.

## 6. Rückwärtsprobe vor der Ausgabe

1. **Jeder Absatz, jede Abbildung:** Welcher Auftrag braucht das? Keiner → streichen.
2. **Jeder Auftrag:** Operator, Ergebnisform, Erfolgskriterium – und kein vorgegebener
   Lösungsweg? Schritte → in die Hilfen.
3. **Jede Aufgabe:** Mit welcher Darstellung wird gearbeitet? Keine → ergänzen, wo eine trägt.
4. **Dekoration** (Abschn. 4) gestrichen?
5. **Skript:** `python3 scripts/schuelermaterial_pruefen.py DATEI.md` – Fließtext, lange Sätze
   und Aufträge, Teilaufgaben und Schrittfolgen, Darstellungen je Auftrag, Dekoration,
   Lehrerangaben, doppelte Sätze. Wortzahl und Befunde im Qualitätscheck festhalten.

## Anhang: references/skill-vertrag.md

# Skill-Vertrag der Bibliothek „Unterrichtsentwicklung BBS"

Gemeinsamer Standard für alle Skills dieser Bibliothek. Er sorgt dafür, dass jeder Skill
**allein** funktioniert und trotzdem **mit jedem anderen kombinierbar** ist. Die Quelle liegt
in `_gemeinsam/skill-vertrag.md`; jeder Skill trägt eine Kopie unter `references/`.

---

## 1. Eigenständig arbeiten – Entwurf vor Rückfrage

1. Der Skill braucht nur den Auftrag der Lehrkraft. Fehlende Angaben werden durch
   **begründete, fachtypische Annahmen** ersetzt und sichtbar markiert:
   `⚠️ Annahme: 2. Ausbildungsjahr, 24 SuS, heterogen.` bzw. im Beruflichen Gymnasium
   `⚠️ Annahme: Jg. 13 (Qualifikationsphase), 22 SuS, Lerngebiet ING3.`
2. **Rückfragen nur, wenn ohne Antwort der ganze Entwurf unbrauchbar wäre** (z. B. Beruf
   bzw. Fach völlig unbekannt). Dann höchstens drei gebündelte Fragen, jeweils mit Vorschlag
   als Standardantwort.
3. Ziel ist ein **vollständiger erster Entwurf** (alle Abschnitte gefüllt), nicht ein
   perfekter Teil. Die Lehrkraft schärft nach.
4. Ein Skill ruft **keinen anderen Skill selbst auf**. Er empfiehlt am Ende sinnvolle
   Folge-Skills. Das Verketten übernimmt der Orchestrator `unterricht-entwickeln`.

## 2. Kontext übernehmen – die Planungsakte

Liegt eine **Planungsakte** vor (Datei `00_planungsakte.md` im Arbeitsordner oder ein
Planungsakte-Block im Gespräch), übernimmt der Skill daraus alle passenden Angaben und fragt
nichts erneut ab. Nach getaner Arbeit trägt er sein Artefakt in die Akte ein und ergänzt
leere Felder, die er festgelegt hat. Widersprüche zur Akte werden gemeldet, nicht still
überschrieben.

```markdown
---
projekt: "LS 4 – Förderband nach Störung wieder in Betrieb nehmen"
bundesland: Niedersachsen
schulform: Berufsschule (Teilzeit)
bildungsgang: Industriemechaniker/-in
ausbildungsjahr: 2          # vollzeitschulisch (z. B. BG) stattdessen: schuljahrgang, phase, schwerpunkt, lerngebiet
curriculare_vorgabe: "Rahmenlehrplan Industriemechaniker/-in, LF 6"
dqr: 4
zeitrichtwert_ls: 16
lerngruppe: "22 SuS, heterogen, 3 SuS mit Deutsch als Zweitsprache (ca. B1)"
rahmen: "Fachraum Steuerungstechnik, Moodle, 90-Minuten-Blöcke"
handlungssituation: "…"
handlungsergebnis: "…"
leitidee_ls: "…"            # didaktische Leitidee der Lernsituation (1–2 Sätze)
---

## Artefakte
| Nr. | Artefakt | Skill | Status | Datei |
|---|---|---|---|---|
| 10 | DQR-Einordnung | dqr-zuordnen | Entwurf | 10_dqr-einordnung.md |

## Entscheidungen
- …

## Annahmen und Prüfaufträge (gesammelt)
- …
```

## 3. Ausgabe – einheitlich und weiterverwendbar

**Format:** Markdown. Mit Dateizugriff wird als Datei gespeichert, sonst im Chat ausgegeben.
Ein bestehendes Dokument wird **nie überschrieben**; Überarbeitungen erhalten ein Suffix
(`…_sprachsensibel.md`, `…_v2.md`).

**Text zum Einfügen** (Systemanweisung, Moodle-Textfeld, Hinweistext, Importquelle) steht als
eigener Block im Format des Ziels – ohne Erläuterungen darin; Erläuterungen stehen davor oder
danach. **Vorschläge zu Vorhandenem** (Begutachtung, Überarbeitung, Einstellungen) nennen je
Vorschlag Stelle, neuen Wert und Begründung; was schon passt, wird zusammengefasst bestätigt
statt wiederholt.

**Material für Lernende** (alles, was Lernende in die Hand bekommen; Vorgabe der Fachberatung,
31.10.2026): **kurz** – kein Satz ohne Aufgabe; **offen gestellt** – Ziel, Ergebnis und
Erfolgskriterium statt Lösungsweg, Schritte in gestufte Hilfen; **anschaulich** – Aufgaben
arbeiten mit Zeichnungen, Darstellungen und Grafiken; **ohne Dekoration** – keine Schmuckbilder,
Emojis ohne Funktion, Floskeln oder Inhalte, die kein Auftrag braucht. Richtwerte und Beispiele:
`schuelermaterial.md`, falls vorhanden. Die Pflichtabschnitte (unten) stehen im Teil für die
Lehrkraft (nach `# Lösungen und Erwartungshorizont` bzw. `# Didaktische Hinweise`), nie im Teil für
Lernende.

**Zeichnungen** (Vorgabe der Fachberatung, 01.11.2026): Jede Zeichnung in einem Artefakt – Material
für Lernende, Lösung, Erwartungshorizont, Tafelbild, Entwurf, Begleitblatt – entsteht als **SVG aus
einer Spec** mit dem passenden Zeichen-Skill, dazu eine in diagrams.net bearbeitbare `.drawio.svg`,
eingebunden mit `![Alternativtext](abbildungen/….svg)` und kursiver Bildunterschrift. **Nie** als
Zeichnung aus Zeichen (ASCII-Art: Kästen aus ┌─┐ oder +---+, Pfeilketten, Struktogramm oder GRAFCET
im Codeblock), nie als Mermaid in der Ausgabe, nie als von Hand geschriebenes SVG.

| Zeichnung | Skill bzw. Weg |
|---|---|
| Blockschaltbild, Anlagen- und Systemübersicht, Ablauf, Regelkreis, Struktogramm, ER-Modell, UML, Relationenschema | `fachdiagramm-erstellen` |
| Kennlinie, Messwertdiagramm | aus den Werten per Code als SVG (z. B. matplotlib), Wertetabelle daneben |
| Foto, Werkstückzeichnung, fremde Abbildung | Datei mit Quelle und Lizenz, sonst Platzhalter `[ABBILDUNG: Inhalt, Zweck, Quelle]` |
| GRAFCET, Funktionsplan, Schaltplan | Fachsoftware; im Text zusätzlich als Tabelle (Schritt, Aktion, Transition) |

Erlaubt bleiben Text-Tabellen derselben Inhalte (GRAFCET in Textform, Zuordnungsliste) für die
Zweitkorrektur und die Barrierefreiheit; Verzeichnisbäume und Programmcode sind keine Zeichnungen.
Lösungsbilder tragen `_loesung` im Namen und stehen nur im Teil für die Lehrkraft. **Ohne
Skriptausführung** (Assistent ohne Code) liefert der Skill die Spec und an der Stelle des Bildes den
Platzhalter `[ABBILDUNG: Inhalt – Spec <datei>.yaml]`; die Lehrkraft erzeugt das SVG lokal.
Vorhandenes Material mit Zeichnungen aus Zeichen wird beim Überarbeiten umgestellt. Prüfung:
`zeichnungen_pruefen.py`, falls vorhanden (❌ Zeichnung aus Zeichen, ⚠ Mermaid). Es öffnet auch jede
eingebundene SVG: ❌ Text über Text, Form oder Linie über Text, Text ragt aus seinem Kasten oder aus
dem Bild; ⚠ SVG ohne Spec und Werkzeugkennung (von Hand?), schräge Leitungen, Datei fehlt. Ein Skill,
der Zeichnungen braucht, ruft dafür das Zeichen-Skill auf oder bringt dessen Werkzeug mit
(`metadata.eduwerkzeuge`) – `pruefen` meldet einen `edu-*`-Befehl ohne beides.

**Dateinamen** (Nummer = Platz in der Planungskette):

| Nr. | Artefakt | Skill |
|---|---|---|
| 00 | Planungsakte | unterricht-entwickeln |
| 10 | DQR-Einordnung | dqr-zuordnen |
| 20 | Lernsituation | lernsituation-dokumentieren |
| 21 | LS-Analyse (Prüfbericht: Analysebogen, Phasencheck, Querschnitt, weitere Aspekte) | lernsituation-analysieren |
| 30 | Unterrichtsentwurf | unterrichtsentwurf-erstellen |
| 35 | Entwurfscheck (Selbstcheck/Beratung) | unterrichtsentwurf-analysieren |
| 36 | Unterrichtsreflexion (nach der Stunde: Selbstreflexion, Nachbesprechung) | unterricht-reflektieren |
| 40 | Unterrichtsmaterial | unterrichtsmaterial-erstellen |
| 41 | Experiment (Versuchsanleitung, Lehrerfassung, Gefährdungsbeurteilung) | experiment-planen |
| 42 | Fachdiagramm (Diagrammblatt, Specs unter `diagramme/`, SVG unter `abbildungen/`) | fachdiagramm-erstellen |
| 43 | Programmieraufgabe (Aufgabe, Codeordner `43_code/`, Erwartungshorizont) | programmieraufgabe-erstellen |
| 44 | Technikfolgenabschätzung (Dossier, Quellenmappe, Rollenkarten) | technikfolgen-abschaetzen |
| 45 | Taxonomie-Analyse | bloom-taxonomie |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

**Werkzeug-Skills** (Nr. 42, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
Artefakt mit Pflichtabschnitten – diese hätten in der Quelle Folgen für die Ausgabe –, sondern
Kopf und Pflichtabschnitte stehen in einem **Begleitblatt** (`…_begleitblatt.md`,
Diagrammblatt). Nummern 92–96 (Ausspielen) folgen auf den Prüfbericht: veröffentlicht wird
geprüftes Material. Nr. 93 (agiles Lernen) kann auch für sich stehen, wenn eine Lehrkraft
selbst lernt; die Lernakte gehört dann der lernenden Person.

**Kopf jedes Artefakts:**

```yaml
---
artefakt: Lernsituation
titel: "Förderband nach Störung wieder in Betrieb nehmen"
skill: lernsituation-dokumentieren
skill_version: "1.0"
stand: 2026-10-08
bildungsgang: "Industriemechaniker/-in"
curriculare_vorgabe: "RLP Industriemechaniker/-in, LF 6"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
# optional:
bereich: planung            # planung | pruefen
vertraulich: false          # true bei unveröffentlichten Prüfungsvorschlägen o. Ä.
---
```

**Pflichtabschnitte am Ende jedes Artefakts:**

1. `## Qualitätscheck` – Tabelle *Kriterium | Ergebnis (✅/⚠️/❌) | Hinweis*. Ein ❌ wird vor
   der Ausgabe behoben; was sich nicht beheben lässt, wird zu ⚠️ mit Begründung.
2. `## Annahmen und Prüfaufträge` – alle `⚠️ Annahme:` und alle `🔎 Prüfen:` (Normen,
   Grenzwerte, Rechtsvorgaben, Herstellerangaben, regionale Besonderheiten).
3. `## Übergabe` – kurze Stichpunkte für Folge-Skills (z. B. Handlungsergebnis, zentrale
   Kompetenzen, Dateinamen) und **empfohlene nächste Skills**.
4. Transparenzhinweis als letzte Zeile:
   `> KI-gestützt erstellt (Skill <name> v<version>). Fachliche Prüfung und Verantwortung: Lehrkraft.`
   Die verantwortliche Rolle darf passend zum Artefakt abweichen (z. B. Lehrkraft bzw.
   Bildungsgangteam, Lernende und Fachexpertin); die Zeile beginnt immer mit `> KI-gestützt`, nennt
   Skill und aktuelle Version und steht in **einer** Zeile.

Ausnahmen: **Teilartefakte** tragen Kopf und Pflichtabschnitte im zugehörigen Begleitblatt bzw.
Erwartungshorizont;
**Akten** (Planungsakte) führen einen Verlauf;
**Lektionen** im Kursprojekt folgen `vorlage-lektion.md`, falls vorhanden (Kopf für die Seitenausgabe).

## 4. Fachliche Redlichkeit

- **Nichts erfinden:** keine ausgedachten Normnummern, Paragrafen, Zitate, Studien,
  Grenzwerte, URLs oder Quellen. Unsicheres wird markiert: `[🔎 Norm prüfen]`,
  `[🔎 Wert prüfen]`. „Weiß ich nicht sicher" ist ein gültiges Ergebnis.
- **Rechnen statt schätzen:** Zahlenwerte in Aufgaben und Lösungen werden nachgerechnet,
  Einheiten mitgeführt. Ist ein Code-Werkzeug verfügbar, wird es dafür benutzt.
- **Quellenlage offenlegen:** Unterscheiden zwischen *aus gelieferten Unterlagen* und *aus
  allgemeinem Fachwissen*. Gelieferte Ordnungsmittel haben Vorrang.
- **Fiktive Akteure klar fiktiv:** Firmen, Personen und Adressen in Handlungssituationen
  sind erkennbar ausgedacht („(fiktiv)“ beim ersten Auftreten); keine echten Telefonnummern,
  keine realen Personen; E-Mail-Adressen nur mit Beispiel-Domains (`example.org`, RFC 2606).

## 5. Datenschutz

- Für Begutachtungen, Rückmeldungen und KI-Chatbots gelten zusätzlich die **Leitplanken**
  (`references/leitplanken-bewertung.md`, falls vorhanden): Datenschutzstufen 0–2, keine
  Bewertung einzelner Lernender durch KI, Freigabe durch die Lehrkraft.
- Für Planung und Material werden **keine personenbezogenen Daten** gebraucht.
- Gibt die Lehrkraft Namen oder Leistungsdaten von Lernenden an, werden sie im Artefakt
  pseudonymisiert (S01, S02 …) und es folgt ein kurzer Hinweis.
- Keine Gesundheits-, Förder- oder Herkunftsangaben zu einzelnen Lernenden in Artefakten;
  Lerngruppen werden nur zusammenfassend beschrieben.

## 6. Begriffe und Bezugsrahmen

- Standard ist das **berufsbildende Schulwesen in Niedersachsen**. Für vollzeitschulische
  Bildungsgänge, besonders das **Berufliche Gymnasium** (Lerngebiete, Schuljahrgang,
  Notenpunkte, EPA), gilt zusätzlich `berufliches-gymnasium.md`, falls vorhanden. Verbindliche
  Begriffe nach **Leitlinie SchuCu-BBS 2024**: Handlungssituation, Handlungsergebnis,
  Handlungskompetenz mit **Fachkompetenz** (Wissen, Fertigkeiten) und **Personaler
  Kompetenz** (Sozialkompetenz, Selbständigkeit); vollständige Handlung in sechs Phasen
  (Informieren bzw. Analysieren · Planen · Entscheiden · Durchführen · Überprüfen bzw.
  Kontrollieren · Reflektieren).
- **SchuCu-BBS 2024 ist verbindlich** (Entscheidung der Fachberatung, 19.10.2026): kein
  anderes Kompetenzmodell (etwa vier Dimensionen), keine anderen Phasen oder Begriffe. Eine
  Gliederung des Studienseminars oder der Schule darf gelten; ihre Abschnitte werden mit den
  Begriffen der Leitlinie gefüllt. Vorgaben anderer Länder übernehmen die Skills nicht.
- **Vollständige Handlung und Lernzeit**: Der
  Handlungskreis wird je Lernsituation geschlossen, aber nicht zwingend in 90 Minuten – er
  darf mehrere Unterrichtseinheiten umfassen (Entscheiden, Überprüfen mit Überarbeitung und
  Reflektieren der Lernsituation bleiben immer). Fachsystematische, lehrkraftgeführte
  Lernphasen sind zulässig, wo zweckdienlich und begründet; die Begründung wird dokumentiert
  (`lernsituationsmuster.md` Abschn. 12, falls vorhanden).
- **Didaktische Leitidee** (Planungshilfe der Bibliothek):
  `didaktische-leitidee.md`, falls vorhanden. Ein bis zwei Sätze, welche übertragbare Einsicht
  die Lernenden am exemplarischen Fall gewinnen und warum sie bedeutsam ist – für die
  Lernsituation (unter *didaktisch-methodische Kommentare*) und für die Stunde (vor dem
  Stundenziel). Sie ergänzt die Begriffe der Leitlinie und ersetzt keinen.
- Sprache: sachlich, geschlechtergerecht („Schülerinnen und Schüler", Abkürzung „SuS").
- Kompetenzen und Ziele werden mit **beobachtbaren Operatoren** formuliert
  (`references/operatoren-afb.md`, falls vorhanden). Nicht verwenden: *verstehen, kennen,
  wissen, lernen, sich bewusst sein*.

## 7. Selbstprüfung

Vor der Ausgabe prüft der Skill sein Ergebnis gegen die eigene Checkliste **und** gegen
diesen Vertrag (Annahmen markiert? Nichts erfunden? Pflichtabschnitte vorhanden? Material für
Lernende kurz, offen gestellt, anschaulich, ohne Dekoration? Jede Zeichnung als SVG aus einer
Spec, keine Zeichnung aus Zeichen – `zeichnungen_pruefen.py`, falls vorhanden?), behebt Mängel und
gibt erst dann aus.

## 8. Plattformen

- **Claude (Skills aktiviert):** Ordner als Skill installieren; Claude lädt ihn bei Bedarf.
- **Assistenten ohne Skill-Funktion (z. B. AIS-Chat.schule, fobizz):** Inhalt von
  `SKILL.md` als Anweisung des Assistenten einfügen, Dateien aus `references/` und
  `assets/` als Wissensbasis hochladen. Die Planungsakte wird dann von Hand zwischen den
  Assistenten weitergegeben.
- **Chatbots für Lernende** (Moodle-KI-Chat, AIS.chat-Lernszenario) bekommen keine
  Skill-Fassung, sondern eine eigene kurze Systemanweisung mit Probelauf (`ki-chatbot-einrichten`,
  im AIS-Paket `agiles-lernen-mit-ki`).

## Anhang: references/stundenziele.md

# Stundenziele kompetenzorientiert formulieren

## Muster

**Fachkompetenz (FK):**
> Die SuS **[Operator]** [fachlicher Inhalt], indem sie [beobachtbare fachliche Handlung].

**Personale Kompetenz (PK):**
> Die SuS **[Operator]** [Aspekt der Sozialkompetenz oder Selbständigkeit], indem sie
> [beobachtbare Handlung].

Weitere Dimensionen (z. B. Methoden-, Lern-, Medienkompetenz) nur, wenn sie das Verständnis der
Planung verbessern; nach SchuCu-BBS 2024 sind sie in FK und PK enthalten.

## Leitidee und Stundenziel

Die **didaktische Leitidee** sagt, *wofür* die Stunde steht (übertragbare Einsicht, Bedeutsamkeit),
das **Stundenziel** macht sie überprüfbar. Beispiel LS 4.2, Stunde Planen:
- *Leitidee:* Ein Arbeitsplan ist die Voraussetzung für sicheres Arbeiten – wer die
  Herstellerangaben begründet ordnet und das Wiedereinschalten ausschließt, kann eine Anlage in
  knapper Zeit zuverlässig warten.
- *FK:* Die SuS **erstellen** einen Arbeitsplan für die Wartung des Gurtförderers, indem sie …

Die Leitidee ist kein zweites Ziel und keine Themenangabe (`didaktische-leitidee.md`, falls vorhanden).

## Fünf Kriterien (Handlungsleitfaden Studienseminar)
1. präzise und überprüfbar formuliert
2. angemessener Operator (AFB I–III bzw. Taxonomiestufe passend zum Niveau)
3. intendiertes Ergebnis klar benannt
4. sinnvoller Lernschritt innerhalb der Lernsituation
5. am Ende der Stunde beobachtbar

## Gute Beispiele (Metalltechnik)

| Dimension | Formulierung |
|---|---|
| FK | Die SuS **erstellen** einen Arbeitsplan für die Wartung des Gurtförderers, indem sie die Angaben der Betriebsanleitung auswerten und Arbeitsschritte, Hilfsmittel und Sicherheitsmaßnahmen in eine sinnvolle Reihenfolge bringen. |
| FK | Die SuS **bestimmen** die Passungsart einer Welle-Nabe-Verbindung, indem sie Grenzmaße aus dem Tabellenbuch ermitteln und Höchst- und Mindestspiel berechnen. |
| FK | Die SuS **ermitteln** die Ursache für den ausbleibenden Rückhub des Zylinders, indem sie Schaltplan und Weg-Schritt-Diagramm systematisch vergleichen. |
| PK | Die SuS **vertreten** ihre Planung gegenüber der Instandhaltungsleiterin, indem sie ihre Entscheidungen fachlich begründen und Rückfragen beantworten. |
| PK | Die SuS **schätzen** ihr Vorgehen bei der Fehlersuche **ein**, indem sie im Tandem mithilfe des Reflexionsbogens Stärken und einen Verbesserungsschritt benennen. |

## Typische Fehler → Korrektur

| Fehler | Beispiel | Besser |
|---|---|---|
| nicht beobachtbares Verb | Die SuS verstehen das Prinzip der Kraftübersetzung. | Die SuS **erklären** die Kraftübersetzung am Hebel der Blechschere, indem sie Kräfte und Hebelarme in eine Skizze eintragen. |
| Tätigkeit statt Ziel | Die SuS bearbeiten das Arbeitsblatt. | Ergebnis benennen, das am Arbeitsblatt sichtbar wird. |
| zu groß für eine Stunde | Die SuS planen und realisieren eine SPS-Steuerung. | auf den Schritt der Stunde begrenzen (z. B. Zuordnungsliste erstellen). |
| mehrere Hauptziele | … berechnen …, außerdem … präsentieren …, außerdem … | ein Hauptziel; der Rest sind Teilziele der Phasen. |
| „indem" wiederholt den Operator | Die SuS berechnen die Kraft, indem sie die Kraft berechnen. | Handlung beschreiben, die das Ergebnis erzeugt. |
| PK als Floskel | Die SuS arbeiten gut im Team zusammen. | konkret und beobachtbar: Wer tut was, woran sieht man es? |
