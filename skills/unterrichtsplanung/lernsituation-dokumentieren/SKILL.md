---
name: lernsituation-dokumentieren
description: Entwickelt und dokumentiert Lernsituationen nach der niedersächsischen Leitlinie SchuCu-BBS 2024 – für Lernfelder der Berufsausbildung und Lerngebiete vollzeitschulischer Bildungsgänge wie des Beruflichen Gymnasiums – mit curricularen Vorgaben, Handlungskompetenz (Fachkompetenz, Personale Kompetenz), genau einer Handlungssituation, Handlungsergebnis, Inhalten, Vereinbarungen inklusive Querschnittsaufgaben, Phasenplanung der vollständigen Handlung, Lernhürden und Mustern für Diagnose-, Projekt-, Experiment- und Urteilsbildungs-Lernsituationen. Überführt ältere Lernsituationen (Handlungsprodukt, 7 Phasen, KMK-Raster) ins 2024er-Format und prüft den eigenen Entwurf mit Analysebogen und Phasencheck. Verwenden, wenn eine Lernsituation für Bildungsgangteam, Jahresplanung oder schulisches Curriculum erstellt, überarbeitet oder aktualisiert werden soll – auch aus einer Themenidee oder einem Ordnungsmittel-Auszug. Vorhandene Lernsituationen nur prüfen mit lernsituation-analysieren.
metadata:
  version: "1.14"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  ersetzt: "lernsituation-erstellen 1.x (eduwerkzeuge) – für Niedersachsen"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Lernsituation nach SchuCu-BBS 2024 dokumentieren

## Zweck
Eine Lernsituation so entwickeln und dokumentieren, dass sie im **Bildungsgangteam
abgestimmt, von anderen Lehrkräften übernommen und mit dem Analysebogen geprüft** werden
kann – im Format und in den Begriffen der Leitlinie SchuCu-BBS 2024.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).
**Betriebsmittelkennzeichen** (Steuerungstechnik) immer mit Klasse und Unterklasse – -SJ1, -MA1, -MM1,
-EA1 – gleich in Funktionsbeschreibung, Technologieschema und Zuordnungsliste (DIN EN IEC 81346-2:2020).

## Zwei Modi

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Neu entwickeln** | „Lernsituation zu Instandhaltung einer Förderanlage, Industriemechaniker, 2. Jahr" | vollständige Dokumentation nach Vorlage |
| **B Überführen bzw. überarbeiten** | „Bring meine alte LS (Anhang) ins SchuCu-2024-Format." | Dokumentation 2024 + Änderungsliste |

Eine vorhandene Lernsituation nur **prüfen** (Analysebogen, Phasencheck, Querschnitt,
Prüfbericht mit Ampel) → `lernsituation-analysieren`; überarbeitet wird danach hier in Modus B.

## Eingaben
- **Pflicht (sonst Rückfrage):** Bildungsgang/Beruf **oder** Fach; Thema **oder** Lernfeld.
- **Wichtig, sonst Annahme:** curriculare Vorgabe mit Lernfeld-/Lerngebietstitel und
  Zeitrichtwert, Ausbildungsjahr **bzw.** Schuljahrgang und Phase, Zeitrichtwert der LS,
  Lerngruppe, Lernumgebung (Fachraum, LMS), schulspezifische Entscheidungen (Blockmodell,
  Leistungsbewertung).

**Vollzeitschulische Bildungsgänge (Berufliches Gymnasium, FOS, BFS):** Lerngebiet statt
Lernfeld, Schuljahrgang statt Ausbildungsjahr, fiktiver Auftraggeber statt Betrieb,
Studienorientierung und Wissenschaftspropädeutik, Kopplung an das Fach Praxis, Notenpunkte –
`references/berufliches-gymnasium.md`. Bei optionalen Lerngebieten („eins aus drei“) kein
Vorwissen aus den anderen optionalen voraussetzen.
- **Optional:** Lernfeld-Auszug/Ordnungsmittel (hat Vorrang vor Fachwissen), vorhandene
  Lernsituation, Planungsakte, DQR-Einordnung.

Ohne Ordnungsmittel werden Kompetenzen aus fachtypischen Anforderungen abgeleitet und **jede**
Bezugnahme auf das Lernfeld mit `🔎 Prüfen: Abgleich mit RLP/RRL` markiert. Lernfeldnummern,
-titel und Zeitrichtwerte nie raten: unbekannt → Platzhalter `[LF-Nr./Titel laut RLP]`.

## Vorgehen (Modus A)

1. **Curriculare Vorgaben klären** – Ordnungsmittel, Lernfeld mit Titel, Zeitrichtwert des
   Lernfelds, DQR-Niveau (aus Akte oder Liste; sonst Annahme). **Nachschlagen, nicht
   erinnern:** Wortlaut der Zielformulierung unverändert übernehmen; was darüber hinausgeht,
   als *didaktische Konkretisierung* bzw. *Erweiterung* kennzeichnen, Nachbar-Lernfelder
   abgrenzen (`references/curriculum-abgleich.md`).
2. **Kompetenzen zuerst** („Planung vom Schluss her"): 4–7 Fachkompetenzen und 3–5
   Personale Kompetenzen, **aktiv** formuliert („Die Schülerinnen und Schüler analysieren …").
   Kommunikations-, Methoden-, Lern- und Medienkompetenz werden **eingebettet**, nicht als
   eigene Spalte. Niveau passend zum DQR (Selbständigkeit, Beurteilungsmaßstab, Transfer).
3. **Handlungssituation** – genau **eine**; alle 8 Anforderungen aus
   `references/schucu-bbs-2024.md` Abschn. 4 erfüllen: trägt die ganze LS, bedeutsam, greift
   Erfahrungen auf, **eine zentrale** Aufgaben-/Frage-/Problemstellung, exemplarisch, Rahmen
   benannt (fiktiver Betrieb, technisches System), soziale Interaktion, **offene Lösungswege**.
   Aus SuS-Perspektive formulieren (Ich-/Sie-Ansprache), konkret, 120–220 Wörter, kein
   versteckter Lösungsweg. Fiktive Namen erkennbar fiktiv, keine echten Kontaktdaten. Was die
   Lernenden davon in die Hand bekommen, ist kürzer und anschaulich – Situationsmaterial mit
   Bild (Störmeldung, Foto, Anlagenbild) statt Prosa (`references/schuelermaterial.md`).
4. **Handlungsergebnis** – mögliche Lösung der zentralen Problemstellung; materiell oder
   nicht-materiell; Hinweis, dass die finale Ausgestaltung je nach Kompetenzniveau bei den SuS
   liegt. Teilprodukte (Plakat, Prüfplan, Matrix) als Arbeitsschritte kennzeichnen, nicht als
   eigene Bewertungsgegenstände (`references/lernsituationsmuster.md` Abschn. 6).
5. **Titel** – kurz, prägnant, eine Handlung beschreibend (Verb + Gegenstand,
   z. B. „Förderband nach Störung wieder in Betrieb nehmen").
6. **Inhalte** – aus den Kompetenzen abgeleitet; Aktualität, Komplexität, Bearbeitungstiefe,
   regionale Spezifika und didaktische Reduktion begründen. Normen nur nennen, wenn sicher,
   sonst `🔎 Norm prüfen`.
7. **Lernhürden** – drei bis sieben typische Hürden (Fehlvorstellungen, Verwechslungen,
   Rechenfallen, Symptom statt Ursache) mit Gegenmaßnahme und Ort im Material
   (`references/lernsituationsmuster.md` Abschn. 5); Tabelle in der Vorlage.
8. **Distanzunterricht** – die vier Prüffragen der Leermaske beantworten (Handlungssituation
   für DU verständlich? Anpassung nötig? Ergebnis im DU erreichbar? Ergebnis angepasst?).
9. **Phasenplanung** – sechs Phasen mit Stundenanteilen, die sich mit Puffer zum
   Zeitrichtwert summieren; je Phase Fach- und Personale Kompetenz und
   Medien/Materialien/Hinweise. Der Kreis wird je Lernsituation geschlossen und darf mehrere
   Unterrichtseinheiten umfassen: Phasen auf Einheiten verteilen, Sollbruchstellen markieren.
   Fachsystematische (auch lehrkraftgeführte) Lernphasen und Übungsschleifen ausweisen, wo
   zweckdienlich, jeweils begründet und mit Rückbindungsfrage an die Handlungssituation. Jede Phase **gestalten**,
   nicht nur benennen (`references/lernsituationsmuster.md`): Entscheiden mit mindestens zwei
   Alternativen und offengelegten Kriterien, Überprüfen mit Gelegenheit zur Überarbeitung,
   Reflektieren mit Transfer- und Selbstbezugsfrage. Für Störungs-, Fehlersuch- und
   Kundendienstaufträge das Muster *Diagnose-Lernsituation* (Abschn. 1) nutzen, für Projekte mit
   Lastenheft Abschn. 9, für Versuche und Messungen Abschn. 10
   (`references/experimentsicherheit.md`), für umstrittene Technik und Technikfolgen Abschn. 11
   (`references/quellenbewertung.md`, `references/rollenspiel.md`). Kürzungsoption
   für weniger Stunden angeben (Abschn. 7).
10. **Vereinbarungen und Hinweise zur Umsetzung** – für Bildungsgangs-/Fachgruppe
    (Verknüpfungen zu anderen LS, Fächern, Parallelklassen), **Querschnittsaufgaben** (BNE,
    Demokratiebildung, Europabildung, Medienbildung, soweit das Thema sie nahelegt;
    `references/querschnittsaufgaben.md`), Leistungsfeststellung und -bewertung (Kriterien
    offengelegt, bei Gruppenarbeit Einzelanteil), Materialien und Quellen, Lernumgebung (mit
    Ersatzweg, falls Werkstatt oder Übungsanlage fehlen), didaktisch-methodische Kommentare (mit
    Lernhürden). Die Kommentare beginnen mit der **didaktischen Leitidee der Lernsituation**: ein
    bis zwei Sätze, welche übertragbare Einsicht die Lernenden am Fall gewinnen und warum sie
    bedeutsam ist (`references/didaktische-leitidee.md`). Sie ist kein neues Feld der Leitlinie;
    Auswahl, Reduktion und Phasen müssen sich auf sie beziehen lassen.
11. **Analysebogen** (16 Kriterien) und **Phasencheck** (`references/lernsituationsmuster.md`
    Abschn. 8) auf den eigenen Entwurf anwenden, Schwächen beheben. Dann formal prüfen:
    `python3 scripts/lernsituation_pruefen.py 20_lernsituation_….md` (Pflichtabschnitte, sechs
    Phasen, Phasensumme = Zeitrichtwert, 16 Zeilen mit Stufe und Beleg, Platzhalter) und
    `python3 scripts/zeichnungen_pruefen.py 20_lernsituation_….md` (Anlagenbild, Ablauf als SVG) –
    jedes ❌ beheben, dann ausgeben.

**Modus B – Überführen:** Inhalte übernehmen, Begriffe nach Tabelle „Begriffswechsel"
(`references/schucu-bbs-2024.md` Abschn. 7) umstellen, 7 Phasen auf 6 abbilden
(„Bewerten" → Überprüfen bzw. Reflektieren je nach Inhalt), fehlende Elemente ergänzen
(Distanzunterricht, Personale Kompetenz konkretisiert, Vereinbarungen, Lernhürden, Leitidee),
Änderungsliste anhängen. Hat die alte Fassung eine Leitidee oder einen Leitgedanken, wandert er
unter *didaktisch-methodische Kommentare*. Fachinhalt nicht unbemerkt verändern. Vorlagen im **KMK-Raster** (vier
Kompetenzdimensionen, Felder Leistungsbewertung, Differenzierung, Anknüpfung Moodle):
Methodenkompetenz in Fach- bzw. Personale Kompetenz einbetten, Sozial- und Selbstkompetenz
→ Personale Kompetenz, Felder 8–11 → *Vereinbarungen und Hinweise*; Angaben, die erkennbar
aus dem Gedächtnis stammen (Ausbildungsjahr, LF-Titel), als Prüfauftrag markieren statt
übernehmen. Muster: `references/beispiel-lernsituation-it.md`. Liegt ein Prüfbericht von
`lernsituation-analysieren` vor (`21_ls-analyse_….md`), seine Befunde abarbeiten – zuerst die drei
hervorgehobenen Verbesserungen – und in der Änderungsliste den Kennungen (A1–A16, P1–P10, W1–W12)
zuordnen.

**Mehrere LS eines Lernfelds bzw. Lerngebiets** (Lernfeldübersicht): Rechenbares liefert
`python3 scripts/lernsituation_pruefen.py 20_*.md [--ziel FK1,…] [--verfuegbar STD]` –
Kompetenzraster aus dem Kopffeld `kompetenz_codes` (leere Zeile oder Spalte, Kreuze in fast
allen LS), Stundenbilanz, wortgleiche Personale Kompetenzen, gleichlautende Belege.

**Viele LS aus vorhandenen Lektionen dokumentieren** (Kursprojekt mit `lessons/*/lesson.md`
nach `references/lektionsmuster.md`): Titel, Kompetenzen, Handlungssituation, Bewertungskasten,
Phasenzeiten, Stolpersteine und Didaktische Hinweise dürfen per Skript übernommen werden. Die
**Einschätzungen im Analysebogen nie aus einer Vorlage füllen** – je LS mit Beleg aus genau
dieser LS begründen; `lernsituation_pruefen.py` meldet gleichlautende Belege als ⚠.
Lektionen mit demselben Kopffeld `lernsituation` gehören zu **einer** LS und werden in einem
Dokument beschrieben (Phasen über die Lektionen verteilt, ein Handlungsergebnis).

## Ausgabe
Datei `20_lernsituation_<kurztitel>.md` nach `assets/vorlage-lernsituation.md` (Kopf nach
Skill-Vertrag, Rahmentabelle, Lernsituation, Hinweise zur Umsetzung, Phasenplanung,
Analysebogen-Selbstcheck, Pflichtabschnitte).
Die Übergabe enthält: Titel, Zeitrichtwert, Handlungssituation (Kurzfassung),
Handlungsergebnis, Leitidee, Kernkompetenzen, Phasen mit Stunden – damit `unterrichtsentwurf-erstellen`
und `unterrichtsmaterial-erstellen` ohne Rückfrage weiterarbeiten können. Mit Planungsakte die
Leitidee dort als `leitidee_ls` eintragen (liest `unterrichtsentwurf-erstellen`).

## Qualitätscheck (zusätzlich zum Analysebogen)
- [ ] Begriffe nach SchuCu-BBS 2024 (Handlungsergebnis, 6 Phasen, Personale Kompetenz)?
- [ ] Genau eine Handlungssituation, die die ganze LS trägt, mit offenen Lösungswegen?
- [ ] Kompetenzen aktiv, beobachtbar, niveaugerecht; keine „verstehen/kennen"?
- [ ] Jede Kompetenz taucht in mindestens einer Phase wieder auf; jede Phase hat eine?
- [ ] Phasenstunden summieren sich zum Zeitrichtwert?
- [ ] Leistungsbewertung mit offengelegten Kriterien, passend zu den Kompetenzen?
- [ ] Entscheiden mit mindestens zwei Alternativen, Kriterien und schriftlicher Begründung?
- [ ] Lernhürden mit Gegenmaßnahme und Ort im Material dokumentiert?
- [ ] Didaktische Leitidee unter *didaktisch-methodische Kommentare*: verdichtet, exemplarisch, bedeutsam, trägt die Phasen?
- [ ] Phasencheck ohne ❌ (Überprüfen mit Überarbeitung, Reflektieren mit Transfer; Lernzeit: Kreis in der Lernsituation geschlossen, fachsystematische Phasen begründet)?
- [ ] Lernfeld-/Lerngebiets- und Normangaben belegt oder als Prüfauftrag markiert; Stand des Ordnungsmittels aktuell?
- [ ] Querschnittsaufgaben dort eingelöst, wo das Thema sie nahelegt (Auftrag und Erwartung)?

## Beispielaufrufe
> „Erstelle eine Lernsituation nach SchuCu-BBS 2024: Anlagenmechaniker/-in SHK, 2. Jahr,
> Trinkwasserinstallation in Betrieb nehmen, 16 Stunden, Blockunterricht, Moodle."

> „Hier unsere LS aus 2019 (Anhang). Überführe sie ins 2024er-Format und prüf sie mit dem
> Analysebogen."

> „Arbeite die Befunde aus dem Prüfbericht zur LS ING4.1 ein (Anhang: LS und Prüfbericht)."

## Referenzen – wann lesen
- `assets/vorlage-lernsituation.md` – **immer** (Ausgabeformat).
- `references/schucu-bbs-2024.md` – **immer** (Anforderungen, Phasen, Analysebogen, Begriffe).
- `references/schuelermaterial.md` – was Lernende von der Lernsituation in die Hand bekommen: kurz, anschaulich, ohne Dekoration.
- `references/lernsituationsmuster.md` – beim Gestalten der Phasen (Modus A, B), für
  Diagnose-Lernsituationen und für den Phasencheck (alle Modi).
- `references/didaktische-leitidee.md` – Leitidee der Lernsituation formulieren (Schritt 10).
- `references/beispiel-lernsituation-metall.md` – als Qualitätsmaßstab für Ton, Tiefe und Umfang.
- `references/beispiel-lernsituation-it.md` – Informationstechnik; zugleich Muster für Modus B
  (Überführung aus dem KMK-Raster mit Änderungsliste).
- `references/curriculum-abgleich.md` – Ordnungsmittel nachschlagen, Konkretisierung
  kennzeichnen, Abdeckungsmatrix für mehrere LS eines Lernfelds.
- `references/operatoren-afb.md` – für Kompetenzformulierungen; im BG auch `references/operatoren-epa-technik.md`.
- `references/berufliches-gymnasium.md` – vollzeitschulische Bildungsgänge, Lerngebiete, BG; dort auch Notenpunkte (`references/notenschluessel.md`).
- `references/querschnittsaufgaben.md` – BNE, Demokratiebildung, Europabildung, Medienbildung; Querschnittscheck.
- `references/experimentsicherheit.md`, `references/quellenbewertung.md`, `references/rollenspiel.md` – zu den Mustern 9–11.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/lernsituation_pruefen.py` – Formalprüfung je LS (Schritt 11) und Lerngebiet bzw.
  Lernfeld über mehrere LS (Kompetenzraster, Stundenbilanz, Querbefunde).
- `references/lektionsmuster.md` – wenn die LS als Lektion für Lernende umgesetzt wird oder
  vorhandene Lektionen dokumentiert werden (Zuordnung Lektion ↔ sechs Phasen; eine Lernsituation
  kann mehrere Lektionen umfassen).
- `references/ki-vereinbarungen.md` – KI-Regeln der Lernsituation (Klassenebene, einmal am Anfang), KI-Phasen und Zeichen je Aufgabe.
