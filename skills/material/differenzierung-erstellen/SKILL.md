---
name: differenzierung-erstellen
description: Erstellt Differenzierungsangebote zu vorhandenem Unterrichtsmaterial, einer Aufgabe, einer Stunde oder einer Lernsituation für heterogene Lerngruppen an berufsbildenden Schulen – gestufte Lernhilfen (Hilfekarten), Grund- und Erweiterungsaufgaben (Fundamentum/Additum), Sprinter- und Wahlaufgaben, Lösungsbeispiele mit Ausblenden, Helfer- und Expertensysteme, Selbstkontrolle und sprachliche Unterstützung – bei gleichem Lernziel und gleichem Handlungsergebnis, mit Hinweisen zu Organisation und Bewertungsgerechtigkeit. Nutzt vorhandene Leistungsdaten (z. B. Klassenbericht), arbeitet aber auch ohne. Verwenden bei „differenziere", „Hilfekarten", „für Schwächere/Stärkere", „Zusatzaufgaben", „Scaffolding", „Binnendifferenzierung", „heterogene Klasse", „Lernende ohne/mit Abitur in einer Klasse". Nicht für die sprachliche Überarbeitung des Materials selbst (sprachsensibel-ueberarbeiten).
metadata:
  version: "2.7"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  ersetzt: "differenzierung-erstellen 1.x (eduwerkzeuge)"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# Differenzierung erstellen

## Zweck
Allen Lernenden ermöglichen, **dasselbe Ziel auf unterschiedlichen Wegen** zu erreichen –
und Leistungsstarke nicht mit „mehr vom Gleichen", sondern mit höherer Denkleistung zu fordern.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Eingaben
- **Pflicht (sonst Rückfrage):** Ausgangsmaterial (Datei/Text) **oder** Aufgabe/Thema mit Ziel.
- **Wichtig, sonst Annahme:** Anlass der Differenzierung (Vorwissen, Tempo, Sprache,
  Motivation, Leistungsdaten), Lerngruppe, Zeit, Sozialform, Medien (Papier/LMS).
- **Optional:** Ergebnisdaten
  (schwächste Aufgaben/Kriterien bzw. Themen mit Förderbedarf aus dem Lernstandsbericht, ohne
  Einzelergebnisse). Mit installiertem `eduwerkzeuge`: `edu-klasse bericht ergebnisse.csv` →
  schwächste Kriterien als Ansatzpunkt. Personenbezogene Daten vorher pseudonymisieren; im
  Artefakt nur Kürzel.

Ohne Angaben gilt die typische BBS-Heterogenität als Annahme: Vorbildung von „ohne Abschluss"
bis Hochschulreife, unterschiedliche Betriebserfahrung, einzelne SuS mit Deutsch als
Zweitsprache. **Berufliches Gymnasium:** Eingang mit erweitertem Sekundarabschluss I,
keine Betriebserfahrung, Streuung vor allem im mathematisch-physikalischen Vorwissen und im
selbständigen Arbeiten in Projekten; Additum wissenschaftspropädeutisch (Herleitung,
Modellgrenzen, Quellenarbeit), Fundamentum sichert die Anforderungen der Klausur
(`references/berufliches-gymnasium.md`).

## Leitlinien (verbindlich)
1. **Gleiches Ziel, gleiches Handlungsergebnis.** Differenziert werden Zugang, Hilfen,
   Komplexität, Tempo, Darstellungsform – nicht der Kompetenzanspruch.
2. **Hilfen gestuft, nie lösend.** Impuls → Strategie → Teilschritt → Kontrolle. Keine Stufe
   verrät das komplette Ergebnis. Hier – nicht in der Aufgabe – stehen die Schritte; je Stufe
   kurz (≤ ~40 Wörter), gern als Teilbild, Skizze oder Lückenbild (als SVG mit
   `fachdiagramm-erstellen`, nie als Zeichnung aus Zeichen).
3. **Erweiterung = Vertiefung.** Additum hebt die Taxonomiestufe (übertragen, beurteilen,
   optimieren), nicht die Menge.
4. **Selbstwahl vor Zuweisung.** Lernende wählen Hilfen und Niveaus selbst; Zuweisung nur mit
   klarem Anlass und ohne Etikettierung.
5. **Übungsdichte für Grundlagen.** Wer Routinen aufbaut, braucht genügend gleichartige
   Übungen mit Lösung zur Selbstkontrolle – Differenzierung „nach unten" heißt oft: mehr
   gestufte Übung, nicht weniger Anspruch.
6. **Bewertungsgerechtigkeit.** Offenlegen, welche Kriterien mit welcher Hilfe erreichbar
   sind; Hilfennutzung dient der Rückmeldung, nicht der Abwertung.
7. **Differenzierung ≠ Nachteilsausgleich.** Formale Nachteilsausgleiche folgen eigenen
   Regeln der Schule; der Skill weist nur darauf hin.
8. **Kurz, offen, anschaulich, ohne Dekoration** (`references/schuelermaterial.md`):
   Differenzierung macht die Aufgabe weder kleinschrittiger noch länger. Sie ergänzt Hilfen, die
   man bei Bedarf zieht, und andere Darstellungsformen (Bild statt Text, Modell, Tabelle).
   Stufen heißen mit Wort und Nummer – keine Farbpunkte oder Symbole als Kennung.

## Formen – nach Anlass wählen (Details: `references/differenzierungsformen.md`)

| Anlass | Form(en) | Vorlage |
|---|---|---|
| unterschiedliches Vorwissen/Tempo | gestufte Hilfekarten, Lösungsbeispiel mit Ausblenden | `assets/vorlage-gestufte-hilfen.md` |
| Leistungsspreizung | Fundamentum/Additum, Sprinteraufgaben | `assets/vorlage-fundamentum-additum.md` |
| schwache Kriterien aus Daten | gezielte Übungsvariante zum Kriterium | `assets/vorlage-fundamentum-additum.md` |
| Motivation/Interessen | Wahlaufgaben, Kontextwahl (Betrieb, Branche) | – |
| Kooperation | Helfer-/Expertensystem, Tandem mit Rollen | – |
| Sprache | Wortspeicher, Satzbausteine, Operatorkarte (vertieft: `sprachsensibel-ueberarbeiten`) | – |
| Selbststeuerung | Checklisten, Lösungen zur Selbstkontrolle, Lernwegeliste | – |

## Vorgehen
1. Ausgangsmaterial lesen; **Ziel, Handlungsergebnis und kritische Stellen** (wo bleiben
   Lernende erfahrungsgemäß hängen?) bestimmen.
2. Anlass klären (Daten oder Annahme) und 2–3 passende Formen wählen – nicht alle.
3. Material erstellen: je kritischer Teilaufgabe Hilfekarten (3–4 Stufen); ein Fundamentum
   (sichert das Ziel) und 1–2 Addita (höhere Stufe); bei Bedarf Übungsserie mit Lösungen.
4. **Organisation** beschreiben: Wo liegen Hilfen (Tisch, Umschlag, LMS-Aufklappelement)? Wie
   wählen Lernende? Was tun Schnelle? Wie wird gesichert, dass alle das Ziel erreichen?
5. Bewertungsbezug festlegen; Lehrerhinweise (Beobachtungsschwerpunkte, typische Fehler).
6. Prüfen mit `python3 scripts/schuelermaterial_pruefen.py 60_differenzierung_<kurztitel>.md`
   (Hilfen je Stufe, Darstellungen, Dekoration), Qualitätscheck, dann ausgeben.

## Ausgabe
Datei `60_differenzierung_<kurztitel>.md`, Kopf nach Skill-Vertrag. **Aufbau so, dass
`schuelerseiten-veroeffentlichen` (`edu-seiten strip`) die Schülerfassung ohne Nacharbeit
erzeugt** – alles für Lehrkräfte steht unter einer der beiden Lehrer-Überschriften:
1. `# <Titel>` – Teil für Lernende: **Hilfekarten** je Teilaufgabe, **Fundamentum und Additum**
   (ggf. Sprinteraufgaben, Übungsserie), **Bewertungshinweis** in Schülersprache (Leitlinie 6:
   Kriterien offenlegen)
2. `# Lösungen und Erwartungshorizont` – Lösungen der Zusatzaufgaben und Übungen
3. `# Didaktische Hinweise` – **Überblick** (Ziel/Handlungsergebnis unverändert, Anlass, gewählte
   Formen mit Begründung, Befunde zum Ausgangsmaterial), **Organisation im Unterricht**
   (Bereitstellung, Wahlmodus, Zeit), danach die Pflichtabschnitte
   (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis)
Keine `⚠️ Annahme:` im Teil für Lernende.
Weiterverarbeitung (optional): Hilfekarten als gestufte Spoiler in einer Lernlandkarte
(`lernlandkarte-erstellen`) oder als H5P-Übung (`quizfragen-erstellen`), Schülerfassung ohne
Lehrerteil bzw. Schülerseiten je Phase (`schuelerseiten-veroeffentlichen`).

## Qualitätscheck
- [ ] Ziel und Handlungsergebnis in allen Varianten identisch?
- [ ] Hilfen gestuft (Impuls → Strategie → Teilschritt → Kontrolle), letzte Stufe nicht lösend?
- [ ] Additum auf höherer Taxonomiestufe statt Mehrmenge?
- [ ] Selbstwahl möglich, keine Etikettierung?
- [ ] Organisation im Raum/LMS konkret beschrieben?
- [ ] Bewertungsbezug offengelegt?
- [ ] Sprache der Hilfen einfacher als die der Aufgabe?
- [ ] Hilfen kurz und anschaulich, Aufgabe nicht kleinschrittiger als das Original, keine
      Deko-Symbole – `schuelermaterial_pruefen.py` ohne ❌?

## Beispielaufrufe
> „Differenziere das Arbeitsblatt `40_material_arbeitsblatt-1_arbeitsplan.md`: Hilfekarten zur
> Auswertung der Betriebsanleitung, eine Erweiterung für Schnelle."

> „Der Klassenbericht zeigt Schwächen bei ‚Passungen berechnen'. Erstelle eine gestufte
> Übungsserie mit Lösungen und zwei Transferaufgaben."

## Referenzen – wann lesen
- `assets/vorlage-gestufte-hilfen.md`, `assets/vorlage-fundamentum-additum.md` – Ausgabebausteine.
- `references/differenzierungsformen.md` – alle Formen mit Beispielen und Organisationstipps.
- `references/operatoren-afb.md` – Operatoren und Stufen für das Additum.
- `references/schuelermaterial.md` – Material für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `scripts/schuelermaterial_pruefen.py` – Prüfung des Teils für Lernende.
- `references/skill-vertrag.md` – Ausgabeformat und Planungsakte.
