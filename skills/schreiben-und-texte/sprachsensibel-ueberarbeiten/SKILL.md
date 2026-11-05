---
name: sprachsensibel-ueberarbeiten
description: Überarbeitet vorhandenes Unterrichtsmaterial sprachsensibel (Leisen, sprachliches Scaffolding) – macht Aufgaben, Infotexte und Arbeitsblätter sprachlich zugänglich, ohne Fachinhalt oder Fachsprache wegzunehmen, und ergänzt Sprachhilfen wie Wortspeicher mit Artikel und Plural, Satzbausteine je Operator, Operatorkarten, Lesehilfen und Redemittel für berufliche Gespräche, auch Kundensprache für Beratung und Einweisung. Liefert ein Änderungsprotokoll und Lesbarkeitswerte vorher/nachher; authentische Dokumente (Normen, Betriebsanleitungen) bleiben im Original und erhalten Lesehilfen. Verwenden bei „sprachsensibel", „vereinfache den Text", „für DaZ-Schülerinnen und -Schüler", „Sprachförderung im Fach", „Wortspeicher", „Satzbausteine", „zu schwer formuliert", „Kundensprache" oder für Sprachlernklassen. Nicht für fachliche Hilfekarten und Niveaustufen (differenzierung-erstellen) und nicht für neues Material (unterrichtsmaterial-erstellen).
metadata:
  version: "1.6"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Material sprachsensibel überarbeiten

## Zweck
Sprache darf nicht zur Hürde für Fachlernen werden – und Fachsprache bleibt Lernziel.
Der Skill macht Material **zugänglich** und baut gleichzeitig **sprachliche Handlungsfähigkeit
im Beruf** auf.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Drei Modi

| Modus | Wann | Ergebnis |
|---|---|---|
| **A Überarbeiten** (Standard) | selbst erstelltes Material (Arbeitsblatt, Infotext, Aufgabe) | sprachsensible Fassung + Sprachhilfen + Änderungsprotokoll |
| **B Hilfen ergänzen** | authentische Dokumente (Betriebsanleitung, Norm, Datenblatt, Prüfungsaufgabe) oder Original soll bleiben | Original unverändert + Lesehilfen, Wortspeicher, Leseauftrag |
| **C Analysieren** | „Wo sind die sprachlichen Hürden?" | Hürdenbericht mit Lesbarkeitswerten und Prioritäten |

## Eingaben
- **Pflicht:** das Material (Datei/Text).
- **Wichtig, sonst Annahme:** Zielgruppe (Standard: heterogene Berufsschulklasse mit
  einzelnen SuS mit Deutsch als Zweitsprache, Orientierung etwa GER B1), Fachbegriffe, die
  verbindlich gelernt werden sollen, Einsatzform (Papier, LMS, mündlich).
- **Optional:** Sprachstandsinformationen (zusammengefasst, ohne Namen), Vorgaben der Schule.

## Leitlinien (verbindlich)
1. **Fachinhalt bleibt identisch.** Keine fachliche Aussage geht verloren oder wird ungenau.
2. **Fachsprache bleibt – wird aber eingeführt.** Fachbegriffe nicht durch Alltagswörter
   ersetzen, sondern beim ersten Auftreten erklären und im Wortspeicher sichern.
3. **Einfache Sprache, nicht Leichte Sprache.** Leichte Sprache (eigenes Regelwerk) nur auf
   ausdrücklichen Wunsch.
4. **Authentisches bleibt authentisch** (Modus B). Im Beruf zählt das Original.
5. **Operatoren bleiben** (prüfungsrelevant) und werden über Operatorkarten erschlossen.
6. **Unterstützen statt ersetzen (Scaffolding):** Hilfen so bauen, dass sie später wegfallen
   können (Makro-Scaffolding: Aufgabenfolge, Mikro-Scaffolding: Impulse, Satzmuster).
7. **Darstellungsformen wechseln:** Text ↔ Tabelle ↔ Bild ↔ Schema – ein Wechsel ist oft die
   beste Vereinfachung (Leisen).
8. **Für Laien übersetzen, wo der Beruf es verlangt.** Enthält das Material Beratung, Übergabe
   oder Einweisung, kommt die Gegenrichtung hinzu: Fachsprache → Kundensprache, richtig und ohne
   Fachjargon (Leitfaden Abschn. 7). Im schriftlichen Bericht bleibt der Fachbegriff. Dasselbe
   gilt für **Laienpublikum** in Schulungsunterlagen, Bürgerdialog, Anhörung oder Präsentation
   vor Auftraggebern (z. B. Technikfolgenabschätzung im Beruflichen Gymnasium): verständlich,
   belegt, Unsicherheiten offen benannt.
9. **Kürzen vor Ergänzen** (`references/schuelermaterial.md`): Die sprachsensible Fassung ist
   nicht länger und nicht kleinschrittiger als das Original. Eine Darstellung ersetzt Absätze;
   Sprachhilfen sind kompakt (Wortspeicher als Tabelle, gern mit Bild; je Operator ein
   Satzmuster) und erklären nicht in Prosa; keine Dekoration.

## Vorgehen (Modus A)
1. **Analysieren:** Hürden auf Wort-, Satz-, Text- und Aufgabenebene markieren
   (`references/sprachsensibel-leitfaden.md`). Optional Lesbarkeit messen:
   `python3 scripts/lesbarkeit.py DATEI.md` (auch .docx, .odt, .pdf; LIX, Satzlängen, lange Sätze, Nominalstil,
   Passiv-Hinweise).
2. **Fachbegriffe festlegen:** Welche müssen gelernt werden (bleiben + Wortspeicher), welche
   sind nur Ballast (ersetzen)?
3. **Überarbeiten** nach Leitfaden: kurze Sätze, ein Gedanke pro Satz, Aktiv, Verben statt
   Nominalketten, Partizipialattribute auflösen, Komposita bei Einführung gliedern, klare
   Gliederung, Operator hervorheben, eine Handlung pro Auftragssatz – ohne den Auftrag in
   Einzelschritte zu zerlegen (Schritte gehören in Hilfen); Überflüssiges streichen.
4. **Sprachhilfen ergänzen** (`references/sprachhilfen.md`): Wortspeicher (Artikel, Plural,
   typische Verbverbindungen), Satzbausteine zu den verwendeten Operatoren, ggf. Leseauftrag,
   Redemittel für Gespräche (Kundengespräch, Übergabe, Präsentation). Bei Beratung oder
   Einweisung: Wortspeicher mit Spalte Kundensprache und Redemittel für Einwände, Kosten und
   Einweisung; bei Anhörung und Bürgerdialog Redemittel, die **Bedenken ernst nehmen** statt sie
   „zu behandeln“ (Abwägen, Unsicherheit benennen, Gegenposition wiedergeben).
5. **Abgleichen:** Fachinhalt vorher/nachher vergleichen; Lesbarkeit erneut messen; Wortzahl
   und Form vorher/nachher mit `python3 scripts/schuelermaterial_pruefen.py ORIGINAL.md
   50_…_sprachsensibel.md` (Fließtext, Aufträge, Darstellungen).
6. **Protokoll** der wesentlichen Änderungen schreiben.

## Ausgabe
Datei `50_<originalname>_sprachsensibel.md` (Original nie überschreiben), Kopf nach
Skill-Vertrag. **Aufbau so, dass `schuelerseiten-veroeffentlichen` (`edu-seiten strip`) die
Schülerfassung ohne Nacharbeit erzeugt:**
1. `# <Titel>` – **Überarbeitete Fassung** (gleiche Struktur wie das Original) und
   **Sprachhilfen** (Wortspeicher, Satzbausteine, ggf. Leseauftrag, Redemittel) – Teil für Lernende,
   ohne `⚠️ Annahme:`
2. `# Lösungen und Erwartungshorizont` – Lehrerteil des Originals (überarbeitet oder Verweis)
3. `# Didaktische Hinweise` – **Änderungsprotokoll** (Stelle | vorher | nachher | Begründung),
   **Lesbarkeit** vorher/nachher mit Einordnung, **Hinweise für die Lehrkraft** (sprachliches
   Lernziel, Fachbegriffe zum Üben, mündliche Unterstützung), Annahmen zur Zielgruppe, danach
   die Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis)

## Qualitätscheck
- [ ] Fachliche Aussagen vollständig und unverändert korrekt?
- [ ] Verbindliche Fachbegriffe erhalten, eingeführt und im Wortspeicher?
- [ ] Sätze überwiegend kurz; keine Nominalketten und Schachtelsätze im Schülerteil?
- [ ] Jede Aufgabe: Operator hervorgehoben, eine Handlung pro Satz, Ergebnisform klar?
- [ ] Satzbausteine passen zu den verwendeten Operatoren?
- [ ] Authentische Dokumente im Original belassen (Modus B)?
- [ ] Bei Beratung/Einweisung: Kundensprache und Redemittel für Einwände vorhanden, fachlich
      nicht falsch vereinfacht?
- [ ] Keine Verniedlichung, kein Kindersprachton – erwachsenengerecht?
- [ ] Fassung nicht länger als das Original (Fließtext), Aufträge nicht kleinschrittiger,
      Sprachhilfen kompakt, keine Dekoration – `schuelermaterial_pruefen.py` ohne ❌?

## Beispielaufrufe
> „Überarbeite `40_material_arbeitsblatt-1_arbeitsplan.md` sprachsensibel. In der Klasse sind
> vier SuS mit Deutsch als Zweitsprache (ca. B1). Fachbegriffe Wartung, Inspektion,
> Instandsetzung müssen bleiben."

> „Hier ein Auszug aus der Betriebsanleitung. Nicht ändern – aber Lesehilfen und Wortspeicher
> dazu."

## Referenzen – wann lesen
- `references/sprachsensibel-leitfaden.md` – Hürden und Regeln auf Wort-, Satz-, Text-,
  Aufgabenebene mit Vorher/Nachher-Beispielen; Kundensprache (Abschn. 7). **Immer.**
- `references/sprachhilfen.md` – Wortspeicher (auch mit Kundensprache), Satzbausteine je
  Operator, Leseaufträge, Redemittel (auch Einwände, Kosten, Einweisung), Methodenwerkzeuge.
- `references/operatoren-afb.md` – Operatoren und Erwartungen.
- `references/schuelermaterial.md` – Material für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `scripts/schuelermaterial_pruefen.py` – Wortzahl und Form vorher/nachher.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
- `scripts/lesbarkeit.py` – optionale Messung (Python 3, ohne Zusatzpakete); liest Word/PDF über
  `scripts/text_lesen.py`.
