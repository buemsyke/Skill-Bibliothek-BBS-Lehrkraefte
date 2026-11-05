<!-- Assistenten-Fassung des Skills 'lernsituation-analysieren'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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

# ANHÄNGE

## Anhang: assets/vorlage-ls-analyse.md

---
artefakt: LS-Analyse
titel: "[Titel der geprüften Lernsituation]"
skill: lernsituation-analysieren
skill_version: "1.4"
stand: JJJJ-MM-TT
bildungsgang: "[Beruf / Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld bzw. Lerngebiet mit Nr. und Titel]"
dqr: 0
geprueft: "[Datei(en) der Lernsituation]"
format: "[Leermaske 2024 | älteres Format | KMK-Raster | Schulvorlage | Bibliotheksformat]"
anlass: "[Selbstcheck | Abstimmung im Bildungsgangteam | Übernahme | Fortbildung]"
status: "KI-Entwurf – Rückmeldung zur Lernsituation, fachlich zu prüfen"
---

# Analyse der Lernsituation „[Titel]“

## Ergebnis auf einen Blick

**Ampel:** [🟢 einsetzbar | 🟡 nach Überarbeitung einsetzbar | 🔴 grundlegend überarbeiten] –
[ein Satz zur Begründung]

| Teil | Ergebnis |
|---|---|
| A Analysebogen (Leitlinie, verbindlich) | [n× trifft zu · n× trifft eher zu · n× trifft eher nicht zu · n× trifft nicht zu] |
| B Phasencheck (Bibliothek) | [n× ✅ · n× ⚠️ · n× ❌] |
| C Didaktische Leitidee (Bibliothek) | [vorhanden, Kriterien erfüllt / vorhanden, schärfen / fehlt – Vorschlag unten] |
| D Querschnittsaufgaben (Erlasse) | [eingelöst: … · naheliegend, aber offen: …] |
| E Weitere Aspekte | [wichtigste Befunde in Stichworten] |

## Stärken

- [Stärke mit Beleg: „…“]
- …

## Die drei wirksamsten Verbesserungen

1. **[Aspekt] ([Kennung])** – [Befund in einem Satz].
   > [fertige Formulierung bzw. bei prüfungsrelevanten Lernsituationen nur der Hinweis, was zu ändern ist]
2. …
3. …

## A – Analysebogen (Leitlinie SchuCu-BBS 2024)

| Nr. | Kriterium | Einschätzung | Begründung | Beleg |
|---|---|---|---|---|
| 1 | Kompetenzen leiten sich aus den curricularen Vorgaben ab | [trifft zu …] | … | „…“ |
| 2 | Personale Kompetenz ist konkretisiert | | | |
| 3 | Fachkompetenz ist konkretisiert | | | |
| 4 | Inhalte leiten sich aus den curricularen Vorgaben ab | | | |
| 5 | Inhalte sind analysiert (Aktualität, Komplexität, Bearbeitungstiefe, regionale Spezifika) | | | |
| 6 | Handlungssituation initiiert einen Lernprozess | | | |
| 7 | … trägt den Lernprozess über die gesamte Lernsituation | | | |
| 8 | … ist für Berufsausübung und/oder Lebenswelt bedeutsam (Lernbereich: [berufsbezogen/berufsübergreifend]) | | | |
| 9 | … greift berufliche, persönliche und/oder gesellschaftliche Erfahrungen auf | | | |
| 10 | … wirft eine zentrale Aufgaben-, Frage- bzw. Problemstellung auf | | | |
| 11 | … ist exemplarisch | | | |
| 12 | … benennt den Rahmen | | | |
| 13 | … berücksichtigt soziale Interaktion | | | |
| 14 | … ermöglicht verschiedene, möglichst offene Lösungswege | | | |
| 15 | Handlungsergebnis ist Lösung der zentralen Problemstellung | | | |
| 16 | Vereinbarungen und Hinweise zur Umsetzung sind vollständig dokumentiert | | | |

## B – Phasencheck (Ergänzung der Bibliothek, kein Kriterium der Leitlinie)

| Nr. | Bereich | Ergebnis | Befund und Beleg | Vorschlag |
|---|---|---|---|---|
| P1 | Informieren | | | |
| P2 | Planen | | | |
| P3 | Entscheiden | | | |
| P4 | Durchführen | | | |
| P5 | Überprüfen | | | |
| P6 | Reflektieren | | | |
| P7 | Lernhürden | | | |
| P8 | Leistungsbewertung | | | |
| P9 | Leitidee | | | |
| P10 | Lernzeit | | | |

## C – Didaktische Leitidee

[Vorhanden: „…“ – Kriterien L1 verdichtet · L2 exemplarisch · L3 bedeutsam · L4 stimmig ·
L5 tragend: …]
[Fehlt – Vorschlag als Hinweis:]
> [Leitidee nach dem Muster]

## D – Querschnittsaufgaben (Erlasse)

| Nr. | Ergebnis | Befund und Beleg |
|---|---|---|
| Q1 | [✅/⚠️/❌/➖] | |
| Q2 | | |
| Q3 | | |
| Q4 | | |
| Q5 | | |
| Q6 | | |
| Q7 | | |

## E – Weitere Aspekte

| Kennung | Aspekt | Ergebnis | Befund und Beleg | vertiefen mit |
|---|---|---|---|---|
| W1 | Bestandteile, Format 2024 | | | |
| W2 | Kompetenzen beobachtbar formuliert | | | |
| W3 | Niveau passt zum DQR | | | |
| W4 | Anspruch der Aufträge | | | |
| W5 | Sprache der Handlungssituation | | | |
| W6 | Differenzierung | | | |
| W7 | Sicherheit bei Versuchen | [nur bei Versuchen] | | |
| W8 | Quellen | | | |
| W9 | Fachliche Angaben (Normen, Rechnungen, Links) | | | |
| W10 | Fiktive Akteure, Datenschutz, Platzhalter | | | |
| W11 | Berufliches Gymnasium | [nur BG] | | |
| W12 | Mehrere Lernsituationen | [nur bei mehreren LS] | | |

## Vorbefund des Skripts

[Aufruf und Kurzfassung von `ls_analyse.py`; wo die Einschätzung oben vom Vorbefund abweicht,
kurz begründen (z. B. Bestandteil anders benannt).]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Vorbefund eingearbeitet, Abweichungen begründet | | |
| Analysebogen vollständig, jede Einschätzung mit Beleg aus dieser Lernsituation | | |
| Belege mit `zitate_pruefen.py` gefunden | | |
| Verbindlichkeit getrennt (Leitlinie · Erlass/Ordnungsmittel · Bibliothek) | | |
| Stärken zuerst, höchstens drei Verbesserungen hervorgehoben | | |
| Keine Aussage über Personen, keine Namen | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Geprüfte Datei(en), Ampel, drei Verbesserungen
- Empfohlene nächste Skills: `lernsituation-dokumentieren` Modus B (überarbeiten bzw. ins Format
  2024 überführen), weitere je Befund laut Spalte „vertiefen mit“

> KI-gestützt erstellt (Skill lernsituation-analysieren v1.4). Fachliche Prüfung und Verantwortung: Lehrkraft bzw. Bildungsgangteam.

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

## Anhang: references/curriculum-abgleich.md

# Curriculare Vorgaben abgleichen – nachschlagen, zerlegen, Abdeckung nachweisen

Gemeinsame Referenz für Lernsituationen, Lernfeldplanung und Leistungsüberprüfungen. Quelle:
`_gemeinsam/curriculum-abgleich.md` (übernommen und verdichtet aus der *lernfeld-werkstatt*,
Abschnitt Curriculum-Recherche).

## Inhalt
1. Grundsatz: nachschlagen, nicht erinnern
2. Ebenen der Vorgaben
3. Wo nachschlagen
4. Was aus dem Ordnungsmittel übernommen wird
5. Teilkompetenzen (K-Codes)
6. Vier Töpfe: Kern, Konkretisierung, Erweiterung, Ausschluss
7. Abdeckungsmatrix – der Vollständigkeitsnachweis
8. Häufige Fehler

---

## 1. Grundsatz: nachschlagen, nicht erinnern

- Lernfeld- bzw. Lerngebietsnummer, amtlicher Titel, Ausbildungsjahr bzw. Schuljahrgang,
  Zeitrichtwert und **Zielformulierung** stehen im Ordnungsmittel. Sie werden **wörtlich** übernommen – nicht geglättet, gekürzt
  oder aus dem Gedächtnis rekonstruiert.
- Liegt das Dokument nicht vor und ist es nicht beschaffbar: **nicht raten.** Platzhalter
  setzen (`[LF-Nr./Titel laut RLP]`, `[Zeitrichtwert laut RLP]`), `🔎 Prüfen: Abgleich mit
  RLP/RRL` vermerken und an allem weiterarbeiten, was nicht davon abhängt.
- Ohne Ordnungsmittel entsteht nur ein **begründeter Entwurf** – das wird im Artefakt gesagt.

## 2. Ebenen der Vorgaben

| Ebene | regelt | Verbindlichkeit |
|---|---|---|
| **KMK-Rahmenlehrplan** des Ausbildungsberufs | Lernfelder mit Nummer, Titel, Zeitrichtwert, Ausbildungsjahr, Zielformulierung | verbindlich für den berufsbezogenen Unterricht |
| **Ausbildungsordnung / Ausbildungsrahmenplan** | betriebliche Ausbildung | für den Unterricht Kontext und Abgleich (Lernortkooperation) |
| **Landesvorgaben** (Niedersachsen: Rahmenrichtlinien, curriculare Vorgaben, Leitlinie SchuCu-BBS) | Umsetzung im Land, schulische Bildungsgänge, berufsübergreifender Lernbereich | landesverbindlich |
| **Rahmenrichtlinien vollzeitschulischer Bildungsgänge** (Berufliches Gymnasium, Fachoberschule, Berufsfachschule) | **Lerngebiete** mit Titel, Zeitrichtwert, Zielformulierung, Inhalten bzw. Anwendungsbezügen, Unterrichtshinweisen; im BG Einführungs- und Qualifikationsphase, verbindliche und optionale Lerngebiete | landesverbindlich; ersetzt dort den KMK-Rahmenlehrplan (`berufliches-gymnasium.md`, falls vorhanden) |
| **Erlasse zu Querschnittsaufgaben** (BNE, Demokratiebildung) und KMK-Empfehlungen (Europabildung, Bildung in der digitalen Welt) | Aufgaben aller Bildungsgänge, umgesetzt in Lernsituationen | verbindlich bzw. empfohlen; Geltungsdauer prüfen (`querschnittsaufgaben.md`, falls vorhanden) |
| **Handreichungen** anderer Länder, Verlage, Kammern | Umsetzungsideen, Lernsituationsvorschläge | **nicht bindend** – Anregung |
| **Schulisches Curriculum** (Bildungsgangteam) | Verteilung, Lernsituationen, Leistungsbewertung | schulverbindlich |

Reihenfolge beim Nachschlagen (duale Ausbildung): Rahmenlehrplan → Ausbildungsrahmenplan
(Abgleich) → Landesvorgaben → Handreichungen. Vollzeitschulisch: Rahmenrichtlinien → ggf.
EPA/Prüfungsvorgaben → Handreichungen (z. B. NLQ-Musterlernsituationen). Bei Widerspruch gilt
die höhere Ebene; Musterlernsituationen sind Anregung, keine Vorgabe.

## 3. Wo nachschlagen

- **KMK-Rahmenlehrpläne:** Website der KMK (Bereich Berufliche Bildung, Rahmenlehrpläne) 🔎 aktuelle Fassung und Beschlussdatum prüfen.
- **Ausbildungsordnungen:** BIBB; Verordnungstext über das Bundesgesetzblatt bzw. gesetze-im-internet.
- **Niedersachsen:** curriculare Vorgaben und Rahmenrichtlinien (BG, FOS, BFS) über den
  Niedersächsischen Bildungsserver (NiBiS, Bereich BBS) 🔎; Stand im Kopf der RRL
  (z. B. „Stand Mai 2008, Erweiterungen … Juni 2025“) ins Artefakt übernehmen.
- Mit Websuche: Rahmenlehrplan als PDF suchen, Seite des Lernfelds notieren (kommt in die
  Quellenangabe). Ohne Websuche: Lehrkraft um das PDF oder den Wortlaut bitten.

## 4. Was aus dem Ordnungsmittel übernommen wird

1. **Eckdaten:** Lernfeld- bzw. Lerngebietskürzel, amtlicher Titel (wörtlich), Ausbildungsjahr
   bzw. Schuljahrgang/Phase, Zeitrichtwert, Stand des Ordnungsmittels.
2. **Zielformulierung im Wortlaut** (der ganze Block „Die Schülerinnen und Schüler …").
3. **Vorbemerkungen**, soweit sie das Lernfeld betreffen (z. B. Bezug zu Teil 1 der gestreckten
   Abschlussprüfung, Fachrichtungen, gemeinsame Kernqualifikationen).
4. **Nachbar-Lernfelder bzw. -Lerngebiete** – Titel und Ziele mitlesen, **um abzugrenzen**:
   Was dort steht, gehört nicht in diese Lernsituation. Bei **optionalen** Lerngebieten
   („eins aus drei“) darf eine LS kein Vorwissen aus einem der anderen optionalen voraussetzen.
5. **Lerngebiete ohne Inhaltsliste** (z. B. BG Ingenieurwissenschaften: nur Zielformulierung
   und Anwendungsbezüge): Alle Inhalte der LS sind Konkretisierung (Abschn. 6) und werden so
   gekennzeichnet; die Anwendungsbezüge sind Beispiele, keine Pflicht.

## 5. Teilkompetenzen (K-Codes)

Die Zielformulierung wird in nummerierte Teilkompetenzen zerlegt – **sinngleich, mit den
Wörtern des Originals**, in dessen Reihenfolge:

- **K0** = Leitkompetenz (erster Satz, „verfügen über die Kompetenz, …"); worauf das Lernfeld zuläuft.
- **K1 … Kn** = weitere Sätze bzw. Halbsätze; ein Halbsatz mit eigener Handlung wird ein eigener K-Code.
- Jeder K-Code erhält ein Schlagwort und den Originalwortlaut.

```markdown
- **(K2) Wartungsplan:** … die Wartungsarbeiten **nach Herstellerangaben planen** … [Wortlaut laut RLP]
```

Lieber ein K-Code zu viel als eine Kompetenz, die in einem Sammelcode verschwindet.

## 6. Vier Töpfe: Kern, Konkretisierung, Erweiterung, Ausschluss

Verhindert den häufigsten Fehler: **didaktische Konkretisierung als amtliche Vorgabe ausgeben.**

| Topf | Inhalt | Kennzeichnung im Artefakt |
|---|---|---|
| **Kern** | nur, was die Zielformulierung bzw. die Inhalte des Ordnungsmittels ausdrücklich nennen | darf als Vorgabe zitiert werden |
| **Konkretisierung** | übliche Fachsystematik, Verfahren, Normen, Werkzeuge, die das Ordnungsmittel nicht nennt | „didaktische Ausgestaltung", nie „laut RLP gefordert" |
| **Erweiterung** | bewusst zusätzliche Inhalte über den Zeitrichtwert hinaus | ausdrücklich als Erweiterung mit Stundenzahl |
| **Ausschluss** | gehört in ein anderes Lernfeld oder Fach | als bewusste Entscheidung begründet |

## 7. Abdeckungsmatrix – der Vollständigkeitsnachweis

Im BG heißt diese Matrix in NLQ-Mustern **„Kompetenzraster zur Lerngebietsanalyse“** (dort oft
noch „Lernfeldanalyse“): Zeilen = Sätze der Zielformulierung, Spalten = Lernsituationen des
Lerngebiets, Kreuze = federführend eingelöst. Die Prüfregeln unten gelten unverändert; die
**Rückwärtsprobe** prüft in beide Richtungen: Hat jedes Kreuz einen Auftrag? Ist jeder
eingelöste Satz angekreuzt?

Für die Planung mehrerer Lernsituationen eines Lernfelds (Bildungsgangteam, didaktische
Jahresplanung) und für Leistungsüberprüfungen:

| K-Code | Schlagwort | LS 1 | LS 2 | LS 3 | … | geprüft in |
|---|---|---|---|---|---|---|
| K0 | Leitkompetenz | (vorb.) | | ✅ | | KA Aufg. 6 |
| K1 | … | ✅ | (Wdh.) | | | LZK 1 F. 3 |

**Prüfregeln**
1. Keine leere Zeile – jeder K-Code ist mindestens einer Lernsituation federführend (✅) zugeordnet.
2. Keine leere Spalte – jede Lernsituation löst mindestens einen K-Code ein.
3. Jeder Pflichtinhalt genau einmal federführend; Wiederholungen als „(Wdh.)", Vorbereitung als „(vorb.)".
4. **Rückwärtsprobe:** Zu jedem ✅ lässt sich ein konkreter Auftrag bzw. eine Phase benennen.
5. **Stundenbilanz:** Summe der Lernsituationen = Zeitrichtwert des Lernfelds (+ ausgewiesene Erweiterung).
6. **„geprüft in":** Jeder Kern-K-Code kommt in mindestens einer Leistungsüberprüfung vor –
   und keine Leistungsüberprüfung fragt Stoff ab, der erst **nach** ihr unterrichtet wird.

## 8. Häufige Fehler

- Kompetenzen erfinden, die gut klingen, aber nicht im Ordnungsmittel stehen.
- „Lernfeld“ statt „Lerngebiet“ in vollzeitschulischen Bildungsgängen; veralteter Stand des
  Ordnungsmittels im Kopf der LS.
- **Wortlaut-Regel:** Artefakte (Lernsituation, Analysebogen) zitieren die Zielformulierung mit
  Quelle; die Dateien der Skill-Bibliothek selbst geben keine Ordnungsmittel im Wortlaut wieder.
- Wortlaut glätten, weil er sperrig ist.
- Handreichungen anderer Länder wie Vorgaben behandeln.
- Inhalte des Nachbar-Lernfelds hineinziehen.
- Zeitrichtwert ignorieren – mehr Material ist kein besseres Material, sondern nicht unterrichtbar.
- Die Leitkompetenz K0 nirgends einlösen.
- Leistungsüberprüfungen ohne Bezug zur Matrix schreiben.

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

## Anhang: references/experimentsicherheit.md

# Sicherheit bei Experimenten und Schülerversuchen

Eigene Zusammenfassung für die Planung. Maßgeblich sind die **Richtlinie zur Sicherheit im
Unterricht (RiSU)** der KMK in der aktuellen Fassung, die Gefahrstoffverordnung, die
DGUV-Vorschriften und die Landesregelungen 🔎 vor jedem Einsatz prüfen. **Kein Skill gibt ein
Experiment frei.** Gefährdungsbeurteilung, Vorversuch und Freigabe verantwortet die Lehrkraft.

## Inhalt
1. Ablauf: von der Idee zum freigegebenen Versuch
2. Gefährdungsbeurteilung – Mindestinhalt
3. Typische Gefährdungen in technischen Versuchen
4. Gefahrenhinweise für die Prüfskripte
5. Plausibilität von Messwerten

---

## 1. Ablauf: von der Idee zum freigegebenen Versuch

1. **Ziel und Hypothese** festlegen: Welche Frage beantwortet der Versuch?
2. **Ersatzstoff- und Ersatzverfahrensprüfung:** Geht es mit ungefährlicheren Stoffen, kleineren
   Mengen, geringerer Spannung oder als Simulation bzw. Video?
3. **Gefährdungsbeurteilung** schriftlich (Abschn. 2); entscheiden: **Lehrerversuch** oder
   **Schülerversuch**, Gruppengröße, Aufsicht.
4. **Vorversuch** durch die Lehrkraft mit Originalmaterial; Messwerte notieren (Erwartungswerte
   für den Erwartungshorizont).
5. **Betriebsanweisung bzw. Sicherheitshinweise** in der Versuchsanleitung; **Unterweisung** der
   Lernenden vor dem Versuch, dokumentiert.
6. **Freigabe** durch die Lehrkraft (Name, Datum) – erst dann Ausgabe an Lernende.
7. **Entsorgung** und Aufräumen planen.

## 2. Gefährdungsbeurteilung – Mindestinhalt

| Feld | Inhalt |
|---|---|
| Versuch, Ziel | Bezeichnung, Lerngruppe, Lehrer- oder Schülerversuch |
| Stoffe und Geräte | Stoffe mit Menge, Konzentration, GHS-Piktogrammen, H- und P-Sätzen; Geräte mit Spannung, Leistung, bewegten Teilen |
| Gefährdungen | chemisch (Gase, Ätzwirkung, Brand, Explosion), elektrisch, mechanisch, thermisch, Strahlung, Lärm |
| Ersatzprüfung | geprüfte Alternativen und warum (nicht) gewählt |
| Maßnahmen nach **STOP** | **S**ubstitution · **T**echnisch (Abzug, Schutzscheibe, Sicherheitsbuchsen, Fehlerstrom-Schutzschalter, NOT-AUS) · **O**rganisatorisch (Mengenbegrenzung, Aufsicht, Unterweisung, Kleingruppen) · **P**ersönlich (Schutzbrille, Handschuhe, Kittel) |
| Entsorgung | Sammelbehälter, Neutralisation, Batterien/Akkus |
| Notfall | Erste Hilfe, Augendusche, Feuerlöscher, NOT-AUS, Notruf |
| Vorversuch | Datum, Ergebnis, Auffälligkeiten |
| Freigabe | Name der Lehrkraft, Datum |

Ein allgemeiner Hinweis wie „PSA tragen, Richtlinien beachten“ **ersetzt keine**
Gefährdungsbeurteilung.

## 3. Typische Gefährdungen in technischen Versuchen

- **Elektrolyse:**
  - Mit kochsalzhaltigem Elektrolyt (Salzwasser, NaCl, Salzsäure) entsteht an der Anode
    **Chlor**.
  - Für die Wasserelektrolyse ungefährlichere Elektrolyte wählen, z. B. verdünnte
    Natriumsulfatlösung 🔎 Gefährdungsbeurteilung.
  - Natron- und Kalilauge sind **ätzend**.
  - Unedle Elektroden (Zink, Aluminium) lösen sich auf; dabei entstehen Nebenprodukte.
- **Wasserstoff, Knallgas:**
  - Nur kleine Volumina (Reagenzglas) erzeugen und auffangen; keine Ansammlung in Gefäßen,
    Ballons oder Gasometern.
  - Zündquellen fernhalten, lüften.
  - Die Knallgasprobe ist ein üblicher Nachweis. Sie braucht Mengenbegrenzung, Schutzbrille und
    eine Gefährdungsbeurteilung; die Durchführung durch Schülerinnen und Schüler legt die
    Lehrkraft fest 🔎 RiSU.
- **Netzspannung (230/400 V):**
  - Schülerversuche nur mit **Schutzkleinspannung** oder an dafür gebauten Experimentier- bzw.
    Prüfständen (Sicherheitsbuchsen, Fehlerstrom-Schutz, NOT-AUS) unter Aufsicht.
  - Anschlussarbeiten an Motoren und Umrichtern nur spannungsfrei nach den **fünf
    Sicherheitsregeln**.
  - Bei Frequenzumrichtern an Restspannung im Zwischenkreis denken.
  - 🔎 Qualifikation der Lehrkraft (Elektrofachkraft, elektrotechnisch unterwiesene Person)
    nach DGUV und Landesregel.
- **Mechanik und Robotik:** rotierende Teile, Quetschstellen, Schutzzaun bzw. kollaborativer
  Betrieb nach Herstellerfreigabe, reduzierte Geschwindigkeit im Teach-Betrieb, NOT-AUS.
- **Lithium-Akkus:** Kurzschluss, mechanische Beschädigung und Überladung → Brand; nur geeignete
  Ladegeräte, Brandschutzbehälter.
- **Löten, Kleben, 3D-Druck:** Dämpfe, Absaugung, heiße Oberflächen.

## 4. Gefahrenhinweise für die Prüfskripte

`versuch_pruefen.py` (Skill `experiment-planen`) meldet ⚠️, wenn eine Versuchsanleitung eine
dieser Kombinationen enthält und die Gefährdungsbeurteilung sie nicht behandelt:

| Signal im Text | Hinweis |
|---|---|
| Elektrolyse + Kochsalz / NaCl / Salzwasser / Natriumchlorid / Salzsäure | Chlorbildung an der Anode |
| Knallgas / Knallgasprobe | Mengenbegrenzung, Schutzbrille, Lehrkraft entscheidet über Durchführung |
| Wasserstoff + sammeln / Ballon / Flasche / Gasometer | Explosionsgefahr durch größere Gasmengen |
| Natronlauge / Kalilauge / NaOH / KOH | ätzend – Schutzbrille, Handschuhe |
| 230 V / 400 V / Netzspannung / Drehstrom | Schutzkleinspannung oder Prüfstand, fünf Sicherheitsregeln |
| Lithium / Li-Ion / Akku + laden | Brandgefahr |

## 5. Plausibilität von Messwerten

Erwartungswerte im Erwartungshorizont **aus einem Vorversuch** oder aus einer Rechnung mit
physikalischer Obergrenze – nie „mögliches Ergebnis“ ohne Prüfung. Prüfskript:
`messwerte_pruefen.py`.
- **Faraday:** Gasvolumen höchstens V = I·t/(z·F)·R·T/p (H₂: z = 2; O₂: z = 4).
- **Energieerhaltung:** Wirkungsgrad höchstens 1. In Ketten wird beim Rückrechnen vom Nutzen auf
  den Aufwand **dividiert**.
- **Einheiten:** Heizwert in MJ/m³ oder kWh/kg, nie m³/MJ.
- **Messunsicherheit:** Geräteangabe bzw. Ablesegenauigkeit; bei Produkten und Quotienten
  addieren sich die relativen Unsicherheiten (Größtfehler) bzw. ihre Quadrate (Gauß).

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

## Anhang: references/kollegiale-beratung.md

# Kollegiale Beratung zu Entwurf oder Unterricht

Leitlinien für ein Beratungsgespräch auf Augenhöhe, sinngemäß angelehnt an gängige
Beratungsstandards in der Lehrkräfteausbildung. Gilt vor dem Unterricht (Entwurf,
`unterrichtsentwurf-analysieren`) und danach (Nachbesprechung, Hospitation,
`unterricht-reflektieren`). Der Skill bereitet das Gespräch vor – er ersetzt es nicht und
bewertet keine Person.

## Voraussetzungen
- Die Lehrkraft, deren Entwurf bzw. Unterricht besprochen wird, hat **zugestimmt** und behält
  die Hoheit über das Ergebnis.
- Keine Verwendung für Auswahlverfahren, dienstliche Beurteilungen oder die Benotung von
  Prüfungsunterricht. Bei prüfungsrelevanten Entwürfen nur der Selbstcheck der Autorin bzw. des
  Autors (Leitplanke, gekennzeichnet) – keine KI-vorbereitete Beratung durch Dritte.
- Beobachtungen der Hospitierenden **beschreiben**, was geschah (Zeit, Handlung, Wirkung), und
  urteilen nicht über die Person; Lernende nur als Lerngruppe oder in Anzahlen.

## Neun Leitlinien
1. **Anlass klären:** Worum geht es in diesem Gespräch, was wünscht sich die Lehrkraft?
2. **Ablauf transparent machen:** Zeit, Schritte, Ergebnisform vorab vereinbaren.
3. **Zuerst die Lehrkraft:** kurze eigene Einschätzung, bevor Rückmeldungen kommen.
4. **Stärken konkret benennen** – mit Beleg aus Entwurf oder Beobachtung; realistisches Bild, Unterstützung anbieten.
5. **Dialog statt Urteil:** Impulse und Fragen, die Selbsterkenntnis fördern (Reflexionsfragen).
6. **Höchstens drei Schwerpunkte** gemeinsam festlegen – Stärken ausbauen, Entwicklungsfelder bearbeiten.
7. **Zielorientiert:** konkrete nächste Schritte für die nächste Planung vereinbaren.
8. **Schriftlich festhalten:** knappe Zusammenfassung, möglichst von der Lehrkraft selbst formuliert.
9. **Stellungnahme ermöglichen:** Die Lehrkraft kann ergänzen oder widersprechen.

## Gesprächsvorlage (Ergebnis des Skills im Modus Beratung)
- Stärken (3, mit Beleg)
- vorgeschlagene Schwerpunkte (max. 3) mit je 1–2 Reflexionsfragen
- vereinbarte nächste Schritte (von der Lehrkraft auszufüllen)
- Raum für die Stellungnahme der Lehrkraft

## Anhang: references/leitplanken-bewertung.md

# Leitplanken für Prüfen, Rückmelden und Bewerten

Verbindlich für Begutachtungen und Rückmeldungen (`bereich: pruefen`) und für KI-Chatbots
im Unterricht.
Ergänzt den Skill-Vertrag. Quelle: `_gemeinsam/leitplanken-bewertung.md`.

## 1. Grundsatz: Vorschlag, nie Entscheidung

- Werkzeuge und KI liefern **begründete Vorschläge**. Punkte, Noten, Rückmeldungen und
  Gutachten **verantwortet die Lehrkraft** (bzw. die zuständige Person).
- Was weitergegeben oder veröffentlicht wird, trägt bis zur Durchsicht `Freigabe: ausstehend`.
  Nach Durchsicht ersetzt die Lehrkraft die Zeile durch `Freigabe: erteilt – KÜRZEL, JJJJ-MM-TT`.
- Keine automatisierte Einzelentscheidung mit rechtlicher Wirkung (vgl. DSGVO Art. 22).

## 2. Datenschutzstufen

| Stufe | Daten | erlaubt |
|---|---|---|
| **0** | keine Personendaten (Aufgaben, Erwartungshorizont, Rubrik, Musterlösung) | Claude darf lesen und schreiben |
| **1** | pseudonymisierte Abgaben, Punkte je Pseudonym | **nur lokale Werkzeuge** lesen Antworttexte; **Claude sieht nur Zahlen, IDs, Pseudonyme und Kennzeichen** |
| **2** | Klarnamen, Zuordnungsdatei (Mapping), Rückführungsergebnisse | **nie an eine KI**; nur lokal bei der Lehrkraft |

Feste Regeln:
- Claude öffnet **keine Schülerantworten** (auch nicht pseudonymisiert) und keine Dateien
  der Stufe 2. Skripte geben nur Aggregate aus.
- **Lernstände und Lernberichte nur für die Lerngruppe** (Entscheidung der Fachberatung,
  09.10.2026): keine Einzelberichte zu Lernenden, keine Auswertung von Zugriffs- oder
  Aktivitätslogs, kein Live-Zugriff auf LMS-Kurse mit Klarnamen – Bewertungsexporte lokal
  pseudonymisieren. Einzelrückmeldungen schreibt die Lehrkraft.
- Das gilt auch für **KI-Funktionen im LMS** (KI-Chat, Seiten- oder Formularassistent,
  Zusammenfassen): Sie senden den Seiteninhalt an das Sprachmodell. Deshalb nicht auf Seiten mit
  Abgaben, Bewertungen, Teilnehmenden oder Forenbeiträgen mit Namen einsetzen; Chatbots für
  Lernende bewerten nicht, und ihre Chatverläufe werden nicht einzeln ausgewertet
  (Anwendung der Regeln oben, Stand 19.10.2026).

## 3. Ehrlichkeit und Sicherheit

- Befunde mit **Sicherheit**: hoch/mittel/niedrig bzw. Konfidenz in %.
  Ab **75 %** gilt ein Befund als Vorschlag; darunter: „unklar – Lehrkraft entscheidet".
- **„nicht prüfbar"** statt raten (fehlende Angaben, Abbildungen, Handschrift, Skizzen).
- Begutachtungen: jeder kritische Befund mit **wörtlichem Beleg**; Belege werden mit
  `scripts/zitate_pruefen.py` gegen das Dokument geprüft.

## 4. Rechtlicher Rahmen (🔎 vor Einsatz mit Schulleitung/Datenschutz abstimmen)

- KI-Verordnung (EU) 2024/1689: KI-Systeme zur **Bewertung von Lernergebnissen** und zur
  Steuerung von Lernprozessen zählen zu den **Hochrisiko-Anwendungen** (Anhang III Nr. 3);
  Systeme für **Personalentscheidungen** ebenso (Anhang III Nr. 4).
  Pflichten u. a. zu
  menschlicher Aufsicht (Art. 14), Betreiberpflichten (Art. 26) und KI-Kompetenz (Art. 4).
  🔎 Geltungsbeginn und Ausnahmen (Art. 6 Abs. 3) aktuell prüfen.
- Die Skills sind **vorbereitende Hilfen** mit menschlicher Endentscheidung; sie ersetzen
  keine Datenschutz-Folgenabschätzung und keine Freigabe durch die Schule.
- Entwurfsbegutachtungen und Unterrichtsreflexionen nur als **Selbstcheck und kollegiale
  Beratung** – nicht für Auswahlverfahren, dienstliche Beurteilungen oder die Benotung von
  Prüfungsunterricht.
- **Prüfungsrelevante Entwürfe** (Prüfungsunterricht, bewertete Unterrichtsbesuche): Der
  **Selbstcheck** durch die Autorin bzw. den Autor ist erlaubt und wird **gekennzeichnet**
  (Entscheidung der Fachberatung, 19.10.2026). Das heißt: Kopf `pruefungsrelevant: true`,
  Hinweise zur Überarbeitung statt fertiger Formulierungen, und die KI-Nutzung wird im Entwurf
  als Hilfsmittel angegeben – Form nach den Vorgaben des Studienseminars, sonst in der Erklärung
  zur selbständigen Anfertigung. Kollegiale Beratung zu solchen Entwürfen bleibt menschlich.

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

## Anhang: references/pruefkatalog-lernsituation.md

# Prüfkatalog Lernsituation

Alle Aspekte, nach denen die Bibliothek eine Lernsituation beurteilt – an einer Stelle, mit
Kennung, Verbindlichkeit, Prüfweg und Quelle. Die Kriterien selbst stehen in den Referenzen
(eine Quelle je Regel); der Katalog sagt, **was** geprüft wird, **wo** es steht und **wer**
es prüft. Die Kennungen benutzt auch der Vorbefund von `scripts/ls_analyse.py`.

**Verbindlichkeit:** **L** Leitlinie SchuCu-BBS 2024 (verbindlich) · **E** Erlass bzw.
Ordnungsmittel (RLP, RRL) · **B** Bibliothek (Hinweis, kein Verstoß gegen die Leitlinie).
**Prüfweg:** **S** Skript (Vorbefund) · **K** Claude mit wörtlichem Beleg aus der LS ·
**S+K** Skript findet, Claude urteilt.

## Teil A – Analysebogen der Leitlinie (L)

Kriterien und Skala nach `schucu-bbs-2024.md` Abschn. 5 (trifft zu · trifft eher zu · trifft
eher nicht zu · trifft nicht zu), Anforderungen an die Handlungssituation nach Abschn. 4. Je
Kriterium: Stufe, Begründung, Beleg. Geurteilt wird nach dem Text, nicht nach der Vorlage – ein
ausgefülltes Feld erfüllt das Kriterium noch nicht.

| Kennung | Kriterium (Kurzform) | Prüfweg | worauf achten |
|---|---|---|---|
| A1 | Kompetenzen leiten sich aus den curricularen Vorgaben ab | K | Zielformulierung im Wortlaut nachschlagen (`curriculum-abgleich.md`), Nachbar-Lernfelder bzw. -Lerngebiete mitlesen; ohne Auszug nur Prüfauftrag |
| A2 | Personale Kompetenz konkretisiert | K | Sozialkompetenz und Selbständigkeit am Fall, nicht allgemein („arbeiten im Team“); wortgleich in mehreren LS → W12 |
| A3 | Fachkompetenz konkretisiert | S+K | Operatoren und Beobachtbarkeit (W2), Aktualität, Komplexität, Bearbeitungstiefe |
| A4 | Inhalte leiten sich aus den curricularen Vorgaben ab | K | wie A1; Konkretisierung und Erweiterung gekennzeichnet? |
| A5 | Inhalte analysiert | K | Reduktion begründet, regionale Spezifika |
| A6 | Handlungssituation initiiert einen Lernprozess | K | Anlass, der Fragen der Lernenden auslöst |
| A7 | … trägt den Lernprozess über die gesamte LS | K | Lassen sich alle Phasen auf sie zurückführen? |
| A8 | … ist bedeutsam (Lernbereich angeben) | K | berufsbezogen bzw. berufsübergreifend; BG: Studienorientierung (W11) |
| A9 | … greift Erfahrungen der Lernenden auf | K | |
| A10 | … wirft **eine** zentrale Aufgaben-, Frage- bzw. Problemstellung auf | S+K | Skript zählt Fragen und Aufträge; viele Einzelaufträge statt einer Problemstellung? |
| A11 | … ist exemplarisch | K | Übertrag auf andere Fälle möglich (vgl. Leitidee) |
| A12 | … benennt den Rahmen | K | Betrieb, Einrichtung, System; Akteure fiktiv (W10) |
| A13 | … berücksichtigt soziale Interaktion | K | Kunde, Team, Auftraggeber |
| A14 | … ermöglicht verschiedene, möglichst offene Lösungswege | K | kein versteckter Lösungsweg, keine Schrittanleitung in der Situation |
| A15 | Handlungsergebnis löst die zentrale Problemstellung | K | materiell oder nicht-materiell; Teilprodukte sind Arbeitsschritte |
| A16 | Vereinbarungen und Hinweise vollständig dokumentiert | S+K | didaktisch-methodische Kommentare, Distanzunterricht, Leistungsfeststellung und -bewertung, Materialien, Quellen, Lernumgebung (W1) |

## Teil B – Phasencheck (B)

Prüffragen P1–P10 nach `lernsituationsmuster.md` Abschn. 8 (Skala ✅ erkennbar · ⚠️ angelegt,
aber dünn · ❌ fehlt), Lernzeit nach Abschn. 12. Getrennt vom Analysebogen ausweisen; ❌ ist ein
Hinweis, kein Verstoß. Das Skript meldet, ob die sechs Phasen genannt sind (P1–P6), Stichworte zu
Entscheiden (P3), Überprüfen (P5) und Reflektieren (P6), Lernhürden (P7), Leitidee (P9) und die
Zeitsumme (P10); ob die Phasen **gestaltet** sind, prüft Claude.

## Teil C – Didaktische Leitidee (B)

Kriterien L1–L5 nach `didaktische-leitidee.md` Abschn. 4: verdichtet · exemplarisch · bedeutsam ·
stimmig · tragend. Fehlt sie, einen Vorschlag nach dem Muster machen – als Hinweis; die Leitidee
ist kein Feld der Leitlinie.

## Teil D – Querschnittsaufgaben (E)

Q1–Q7 nach `querschnittsaufgaben.md` Abschn. 5 (✅ · ⚠️ · ❌ · ➖ nicht naheliegend). Bewertet
wird nur, was das Thema nahelegt. Das Skript nennt lediglich, welche Bereiche im Text vorkommen.

## Teil E – Weitere Aspekte

| Kennung | Aspekt | Verb. | Prüfweg | Quelle | vertiefen mit |
|---|---|---|---|---|---|
| W1 | Bestandteile der Leitlinie vorhanden; Format 2024 statt älterer Begriffe (Handlungsprodukt, Selbstkompetenz, sieben Phasen) | L | S+K | `schucu-bbs-2024.md` Abschn. 3 und 7 | `lernsituation-dokumentieren` Modus B (überführen) |
| W2 | Kompetenzen beobachtbar formuliert (Operator, keine „verstehen, kennen, wissen“) | B | S+K | `operatoren-afb.md` | `lernsituation-dokumentieren` |
| W3 | Niveau passt zum DQR (Selbständigkeit, Offenheit, Transfer) | B | K | DQR-Angabe der LS bzw. des Bildungsgangs | `dqr-zuordnen` Modus B |
| W4 | Anspruch der Aufträge (Bloom-Stufen, AFB) | B | S+K | `operatoren-afb.md` | `bloom-taxonomie` |
| W5 | Sprache der Handlungssituation zugänglich, Fachbegriffe bleiben | B | S+K | Lesbarkeit (LIX ≤ 60 als Richtwert) | `sprachsensibel-ueberarbeiten` |
| W6 | Differenzierung angelegt (gleiches Ziel, gestufte Hilfen) | B | S+K | – | `differenzierung-erstellen` |
| W7 | Sicherheit bei Versuchen (Gefährdungsbeurteilung, Ersatzweg) | E/B | S+K | `experimentsicherheit.md` | `experiment-planen` |
| W8 | Quellen nach Typ und Interessenlage, keine Interessenquelle als einziger Beleg | B | K | `quellenbewertung.md` | `material-pruefen` |
| W9 | Fachliche Richtigkeit: Normen, Paragrafen, Rechnungen, Links | B | S+K | Skript listet Normen und Links | `material-pruefen` F+P+L |
| W10 | Fiktive Akteure erkennbar fiktiv, keine echten Kontaktdaten, keine Namen, keine Platzhalter | B | S+K | `skill-vertrag.md` Abschn. 4 und 5 | – |
| W11 | Berufliches Gymnasium: Lerngebiet, Schuljahrgang und Phase, Studienorientierung, Fach Praxis | E | K | `berufliches-gymnasium.md` | – (nur BG) |
| W12 | Mehrere LS: Kompetenzraster mit Rückwärtsprobe, Stundenbilanz, Doppelungen, wortgleiche Personale Kompetenzen | E | S+K | `curriculum-abgleich.md` Abschn. 4 und 7 | `lernsituation-dokumentieren` (Lernfeldübersicht) |

## Teil F – Gesamtbild

**Ampel** (angelehnt an Gate G1 des Orchestrators):
- 🟢 **einsetzbar** – Analysebogen ohne „trifft nicht zu“, höchstens zweimal „trifft eher nicht
  zu“; kein ❌ in W1, W7, W10.
- 🟡 **nach Überarbeitung einsetzbar** – bis zu zwei Kriterien „trifft nicht zu“ außerhalb von
  A7, A10 und A14, oder mehr als zwei „trifft eher nicht zu“, oder ❌ in W7 bzw. W10.
- 🔴 **grundlegend überarbeiten** – die Handlungssituation trägt nicht (A7), es gibt keine
  zentrale Problemstellung (A10) oder keine offenen Lösungswege (A14), oder Phasen fehlen ganz.

**Reihenfolge der Verbesserungen:** zuerst Verbindliches (L vor E vor B), dann, was die meisten
Kriterien zugleich verbessert (meist die Handlungssituation), dann Aufwand. Höchstens drei
hervorheben; alles Weitere steht knapp in den Tabellen.

## Anhang: references/quellenbewertung.md

# Quellen bewerten – Typ, Interessenlage, Belegkraft

Für Lehrkräfte (Material prüfen) und für Lernende (Quellenmappe, Technikfolgenabschätzung,
Recherche). Ergänzt die Quellenhierarchie im Faktencheck (`faktencheck-methode.md`, nur in
`material-pruefen`): Diese fragt *wie verlässlich*, die Quellenbewertung fragt zusätzlich
*wer spricht mit welchem Interesse*.

## 1. Quellentypen (Kürzel verbindlich für Quellenmappen und `tfa_pruefen.py`)

| Kürzel | Typ | Beispiele | Interessenlage | Belegkraft für Sachaussagen |
|---|---|---|---|---|
| `amtlich` | Gesetz, Verordnung, Behörde, amtliche Statistik | Gesetze im Internet, Umweltbundesamt, Bundesamt für Strahlenschutz, BSI, Destatis | gering (staatlicher Auftrag) | hoch |
| `wissenschaft` | begutachtete Studie, Forschungsinstitut, Hochschule | Fachzeitschrift mit Peer-Review, Fraunhofer, KIT-ITAS | gering bis mittel (Auftraggeber prüfen) | hoch |
| `norm` | Norm, technische Regel, Richtlinie | DIN/EN/ISO, VDI-Richtlinie, DGUV-Regel | gering | hoch (Inhalt nur im Normtext) |
| `verband` | Branchen- oder Fachverband, Kammer | Bundesverband WindEnergie, Bundesverband Ziegel, VDZ | **ja** (Branche) | mittel – Zahlen oft korrekt, Auswahl und Deutung interessengeleitet |
| `unternehmen` | Hersteller, Betreiber, Dienstleister | Herstellerdatenblatt, Unternehmensbroschüre | **ja** (Verkauf) | mittel – für eigene Produktdaten hoch, für Vergleiche niedrig |
| `initiative` | NGO, Bürgerinitiative, Lobbyorganisation | Umweltverband, Bürgerinitiative gegen …, Verbraucherorganisation | **ja** (Anliegen) | mittel bis niedrig – Positionen, keine neutrale Datenbasis |
| `presse` | Qualitätsjournalismus, Fachpresse | Tageszeitung, öffentlich-rechtlicher Rundfunk, Fachmagazin | gering bis mittel | mittel – als Hinweis, Primärquelle suchen |
| `sekundaer` | Lexikon, Lehrbuch, Fachportal, Tutorial | Wikipedia, Tabellenbuch, Fachportal | gering | mittel – Einstieg, kein Beleg für Grenzwerte |
| `einzelmeinung` | Blog, Streitschrift, Video einer Einzelperson, Social Media | privater Blog, Reader „… schwere Schäden!“ | **ja** oder unbekannt | niedrig |
| `ki` | KI-generierter Text | Chatbot-Auskunft, KI-erstelltes Transkript | unbekannt | **kein Beleg** – nur Material zum Prüfen |

**Regeln:**
- **Interessengeleitete Quellen** (`verband`, `unternehmen`, `initiative`, `einzelmeinung`)
  sind erlaubt und für Kontroversen sogar nötig. Sie werden als Position gekennzeichnet und
  **nie als einziger Beleg** einer Sachaussage verwendet; daneben steht mindestens eine Quelle
  vom Typ `amtlich`, `wissenschaft` oder `norm`.
- **Desinformation** oder wissenschaftlich widerlegte Aussagen nur als ausdrücklich
  gekennzeichneter **Analysegegenstand** („Prüfen Sie diese Behauptung“), nie als Information.
- **KI-Text** ist nie Beleg. Ein KI-erstelltes Muster (z. B. Rollenspieltranskript) wird wie
  ein Erwartungshorizont fachlich geprüft und gekennzeichnet.
- Für sicherheitsrelevante Werte nur `amtlich`, `norm` oder Herstellerangabe zum konkreten
  Produkt.

## 2. Prüffragen je Quelle (für Lernende)

1. **Wer** steht dahinter (Impressum, Herausgeber, Finanzierung)?
2. **Welches Interesse** könnte die Darstellung prägen?
3. **Wann** erschienen, noch aktuell?
4. **Worauf** stützt sich die Aussage (Daten, Studie, Meinung)? Ist die Originalquelle
   auffindbar?
5. **Was sagen andere** verlässliche Quellen? (lateral lesen)

## 3. Quellenmappe – Format

| Nr. | Quelle (Titel, Herausgeber, Jahr, URL bzw. Fundstelle) | Typ | Interessenlage | Kernaussage | gestützt durch |
|---|---|---|---|---|---|
| Q1 | UBA (2021): Ökobilanzen Windenergie und Photovoltaik, Kap. 7 | amtlich | gering | energetische Amortisation unter einem Jahr | – |
| Q2 | Branchenverband (Jahr): Hintergrundpapier Ökobilanz | verband | Branche Windenergie | 30- bis 40-fache Energierückgewinnung | Q1 |

Die Spalte *Typ* enthält genau ein Kürzel aus Abschn. 1.

## 4. Typische Fehler in Material und Schülerprodukten

- Branchen- oder Aktivistenpapier als neutraler Beleg zitiert.
- Linktext widerspricht dem Inhalt (Titel „Gefahr …“, Seite „Entwarnung …“).
- Lange wörtliche Übernahmen ohne Belegfunktion (Zitatrecht: nur so viel wie nötig, mit Quelle).
- Zahl ohne Quelle und ohne Definition („Netzzugänge stiegen von … auf …“).
- KI-Text mit erfundenen Studien („Laut einer Studie des Instituts X … bis zu 15 %“).

## Anhang: references/querschnittsaufgaben.md

# Querschnittsaufgaben in Lernsituationen – BNE, Demokratiebildung, Europabildung, Medienbildung

Diese Aufgaben gelten für **alle** Bildungsgänge der berufsbildenden Schulen in Niedersachsen,
den berufsbezogenen und den berufsübergreifenden Lernbereich. Sie werden **in**
Lernsituationen umgesetzt, nicht als eigenes Fach. Eigene Zusammenfassung; maßgeblich sind die
Originaltexte.

| Bereich | Grundlage | Geltung |
|---|---|---|
| Bildung für nachhaltige Entwicklung (BNE) | RdErl. d. MK „Bildung für nachhaltige Entwicklung (BNE) an öffentlichen allgemein bildenden und berufsbildenden Schulen …“ v. 1.3.2021 | in Kraft seit 1.6.2021, **außer Kraft mit Ablauf des 31.12.2026** 🔎 Nachfolgeregelung prüfen |
| Demokratiebildung | RdErl. d. MK „Stärkung der Demokratiebildung an öffentlichen allgemein bildenden und berufsbildenden Schulen …“ v. 11.5.2021 | in Kraft seit 1.6.2021, **außer Kraft mit Ablauf des 31.12.2026** 🔎 Nachfolgeregelung prüfen |
| Europabildung | KMK-Beschluss „Europabildung in der Schule“ v. 8.6.1978 i. d. F. v. 15.10.2020 | Empfehlung der KMK |
| Medienbildung | KMK-Strategie „Bildung in der digitalen Welt“ und Landeskonzepte 🔎 | Empfehlung, Landesvorgaben prüfen |

## Inhalt
1. BNE
2. Demokratiebildung und Beutelsbacher Konsens
3. Europabildung
4. Medienbildung (Quellen, KI)
5. Querschnittscheck für eine Lernsituation
6. Formulierungshilfen

---

## 1. Bildung für nachhaltige Entwicklung (BNE)

**Kern:** Lernende sollen die Folgen ihres Handelns für die Welt erkennen, kritisch hinterfragen
und verantwortlich entscheiden können. Ökologische, ökonomische, soziale, politische, kulturelle
und ethische Dimensionen werden **miteinander** betrachtet, nicht nacheinander.

- Zwei Kompetenzmodelle stehen im Erlass:
  - die **Gestaltungskompetenz** (zwölf Teilkompetenzen, z. B. vorausschauend denken,
    interdisziplinär arbeiten, Zielkonflikte abwägen, Perspektiven übernehmen);
  - der **Orientierungsrahmen Globale Entwicklung** mit **Erkennen – Bewerten – Handeln**.
- An berufsbildenden Schulen wird BNE **immanent in handlungsorientierten Lernsituationen**
  aufgebaut und in den schulischen Curricula nach SchuCu-BBS verankert.
- Gelingensbedingungen: relevante Fragen der Lernenden aufgreifen, Dimensionen verbinden,
  partizipativ und selbstwirksam lernen, mit außerschulischen Partnern arbeiten.

**Warnzeichen in einer LS:** „Nachhaltigkeit“ nur als Wort im Titel oder einer Kompetenz,
ohne Auftrag und ohne Erwartungshorizont; nur die ökologische Dimension; kein Zielkonflikt
(z. B. Kosten ↔ CO₂ ↔ Versorgungssicherheit).

## 2. Demokratiebildung und Beutelsbacher Konsens

**Kern:** Schule ist ein demokratischer Erfahrungsraum. Gesellschaftliche Konflikte und
Zukunftsfragen werden regelmäßig **kritisch-kontrovers** im Unterricht behandelt – nach dem
**Beutelsbacher Konsens**. Demokratiebildung ist Querschnittsaufgabe aller Fächer und
Lernbereiche; besonders wichtig sind kooperatives Lernen, dialogische Kommunikation und
konstruktiver Umgang mit Konflikten.

**Beutelsbacher Konsens (drei Grundsätze, eigene Worte):**
1. **Überwältigungsverbot:** Lehrkräfte und Material drängen den Lernenden keine Meinung auf;
   sie sollen sich ein eigenes Urteil bilden können.
2. **Kontroversitätsgebot:** Was in Wissenschaft und Politik umstritten ist, erscheint auch im
   Unterricht umstritten – mit den Positionen und ihren Begründungen.
3. **Interessenorientierung (Schülerorientierung):** Lernende sollen ihre eigene Interessenlage
   erkennen und Wege finden, sie zu vertreten.

Grenze: Positionen, die mit der freiheitlich-demokratischen Grundordnung und den Menschenrechten
unvereinbar sind, werden nicht als gleichwertig behandelt und nicht unkommentiert gelassen.

**Warnzeichen in einer LS:**
- Der Auftrag gibt das Urteil vor („Einwände entkräften“, „überzeugen“, „Akzeptanz schaffen“),
  und das Musterprodukt widerlegt jede Gegenposition.
- Eine Seite kommt nur als Karikatur vor.
- Rollenspiele lassen eine Seite „gewinnen“.
- Interessenquellen erscheinen als neutraler Beleg.

**Gute Lösungen:** Perspektivwechsel (Rollenkarten für mehrere Beteiligte), Anhörung oder
Bürgerdialog statt Verkaufsgespräch, ausgewiesene Zielkonflikte, eigenes begründetes Urteil mit
Gegenargument, Rollenspiel mit Rollentausch.

## 3. Europabildung

**Kern:** Lokale, regionale und nationale Fragen im europäischen Zusammenhang sehen; die EU als
Werte- und Rechtsgemeinschaft; Zusammenarbeit über Grenzen; Mobilität und Sprachen.

**Anknüpfungspunkte in technischen Lernsituationen:** europäische Normen (EN) und
Normungsorganisationen; europäisches Verbundnetz und Strommarkt; EU-Recht (Maschinenrichtlinie
bzw. -verordnung, KI-Verordnung, Ökodesign, Abfall- und Batterierecht); europaweite
Ausschreibungen; Fachkräftemobilität.

**Warnzeichen:** europäische Bezüge stehen im Material (z. B. „europaweite Ausschreibung“,
„EN 619“), werden aber nie zum Gegenstand.

## 4. Medienbildung (Quellen, KI)

- Informationen beschaffen, **Quellen nach Typ und Interessenlage bewerten**
  (`quellenbewertung.md`, falls vorhanden), Desinformation erkennen.
- KI-Werkzeuge reflektiert nutzen: KI-Auskünfte prüfen, KI-Unterstützung kennzeichnen, keine
  personenbezogenen Daten eingeben.
- Der KI-Einsatz im Unterricht ist **geregelt und begründet**: Klassenregeln, KI-Phasen je
  Unterrichtseinheit und Zeichen am Arbeitsschritt (🚫 Ohne KI · 💡 KI zum Verstehen ·
  🔧 Mit KI arbeiten) – `ki-vereinbarungen.md`, falls vorhanden.
- Urheberrecht und Zitieren (Belegfunktion, Umfang), Lizenzen.

## 5. Querschnittscheck für eine Lernsituation

Für `lernsituation-analysieren` und für Prüfberichte. Skala ✅ erkennbar
(Auftrag + Erwartung) · ⚠️ angelegt (nur genannt) · ❌ fehlt, obwohl naheliegend · ➖ nicht
naheliegend. Nicht jede LS muss alles leisten. Bewertet wird, was das **Thema nahelegt**; die
Abdeckung über alle LS eines Bildungsgangs gehört in die Jahresplanung.

| Nr. | Bereich | Prüffrage |
|---|---|---|
| Q1 | BNE | Werden mindestens zwei Dimensionen der Nachhaltigkeit mit einem Zielkonflikt bearbeitet (Auftrag **und** Erwartungshorizont)? |
| Q2 | BNE | Treffen die Lernenden eine begründete Entscheidung mit Folgen für andere (Erkennen – Bewerten – Handeln)? |
| Q3 | Demokratie | Ist ein gesellschaftlich umstrittenes Thema auch im Material kontrovers dargestellt (Positionen mit Begründung)? |
| Q4 | Demokratie | Bleibt das Urteil offen – kein vorgegebenes Ergebnis, keine Überwältigung durch Auftrag oder Musterlösung? |
| Q5 | Demokratie | Gibt es kooperative, dialogische Formen (Perspektivwechsel, Anhörung, Aushandlung) und Selbstwirksamkeit? |
| Q6 | Europa | Werden naheliegende europäische Bezüge (Normen, Recht, Netze, Märkte) zum Gegenstand? |
| Q7 | Medien | Bewerten die Lernenden Quellen nach Typ und Interessenlage? Werden KI-Auskünfte geprüft und KI-Hilfe gekennzeichnet? Ist festgelegt und begründet, wo KI genutzt wird und wo nicht (Phase, Arbeitsschritt; Prüffragen K1–A2 in `ki-vereinbarungen.md`, falls vorhanden)? |

## 6. Formulierungshilfen

- *Fachkompetenz (BNE):* „… beurteilen die Lösung unter ökologischen, ökonomischen und sozialen
  Gesichtspunkten und benennen Zielkonflikte.“
- *Personale Kompetenz (Demokratie):* „… vertreten in der Anhörung eine zugewiesene Position
  sachlich, auch gegen die eigene Meinung, und wägen Gegenargumente ab.“
- *Handlungsergebnis:* „Empfehlung an den Gemeinderat mit Abwägung der Positionen und eigenem
  begründetem Urteil“ statt „Argumentationsleitfaden zur Einwandbehandlung“.
- *Vereinbarungen:* „Querschnittsaufgaben: BNE (Zielkonflikt Kosten/Klimabilanz in Phase
  Entscheiden), Demokratiebildung (Anhörung mit Rollentausch), Europabildung (EN-Normen,
  Verbundnetz).“

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
