---
name: ki-kennzeichnung
description: Kennzeichnet geprüftes, mit KI-Unterstützung erstelltes Unterrichtsmaterial transparent – Hinweis am Ende jeder Markdown-Seite mit KI-System, verantwortlicher Person und Stand, verlinkt auf eine Transparenzerklärung, gesetzt mit dem mitgelieferten Werkzeug edu-kennzeichnung (idempotent, prüfbar, wieder entfernbar) für Kursprojekte mit MkDocs-Schülerseiten und für einfache Materialordner; dazu fertige Hinweistexte für Word, PDF, Folien, Moodle, H5P, edumaps und KI-Chats im Kurs und ein Protokoll. Orientiert an den Ethischen Leitlinien der EU-Kommission für Lehrkräfte und Art. 50 der KI-Verordnung. Gekennzeichnet wird erst nach der Prüfung durch die Lehrkraft. Verwenden bei „KI-Kennzeichnung", „Transparenzhinweis", „als KI-unterstützt kennzeichnen", „KI-Transparenzerklärung", „sind alle Seiten gekennzeichnet?".
metadata:
  version: "1.4"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
  eduwerkzeuge: "kennzeichnung"
license: CC0 1.0 (Texte), MIT-0 (Skripte) – siehe LICENSE.txt
---

# KI-Kennzeichnung

## Zweck
Wer Material mit KI-Unterstützung erstellt und an Lernende gibt, macht das **sichtbar und
verantwortet es namentlich**: ein kurzer Hinweis auf jeder Seite, eine ausführliche
Erklärung an einer Stelle, gleiche Angaben in allen Medien. Den Hinweis setzt das getestete
Werkzeug `edu-kennzeichnung` – einheitlich, idempotent und prüfbar.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (im Protokoll). Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Fälle

| Fall | erkennbar an | Konfiguration | Form |
|---|---|---|---|
| **Kursprojekt** | `phase_config.yaml` im Unterordner scripts des Projekts | Block `ki_kennzeichnung:` dort | Hinweisbox in MkDocs-Seiten, Blockzitat für README |
| **Materialordner** | Markdown-Dateien ohne Projektstruktur | `ki_kennzeichnung.yaml` im Ordner | Blockzitat (Word, Moodle, Druck) |
| **andere Medien** | Word, PDF, Folien, Moodle, H5P, edumaps | – | Text aus `assets/vorlage-hinweistexte.md` |

## Eingaben
- **Pflicht (sonst Rückfrage):** verantwortliche Person (Name oder Kürzel und Schule) – wird
  veröffentlicht und nie erfunden; aus der Planungsakte übernehmen, wenn dort angegeben.
- **Wichtig, sonst Annahme:** Ordner bzw. Medien, KI-System (Standard „Claude (Anthropic)"),
  Stand (Datum der Prüfung), wofür KI genutzt wurde.
- **Optional:** Kontakt für Fehlermeldungen (Funktionsadresse), Vorgaben der Schule.

## Leitlinien (verbindlich)
1. **Erst prüfen, dann kennzeichnen.** Der Hinweis sagt „von einer Lehrkraft geprüft und
   freigegeben". Ist die Prüfung nicht bestätigt, wird nicht gekennzeichnet; Entwürfe tragen
   die Transparenzzeile der Bibliothek.
2. **Nichts behaupten, was nicht stimmt:** In der Transparenzerklärung nur zutreffende
   Aussagen (wofür KI genutzt, was nicht geschah); Platzhalter ersetzen oder streichen.
3. **Eine Quelle für die Angaben** (Block `ki_kennzeichnung:`); Datumsangaben nicht in
   Seitentexten von Hand nachziehen.
4. **Form passt zum Medium:** Hinweisbox nur in MkDocs-Seiten, sonst Blockzitat bzw. Text
   aus den Vorlagen.
5. **Nichts überschreiben:** vorhandene `phase_config.yaml` nur ergänzen; vorhandene
   Transparenzerklärung nicht ersetzen.
6. **Rechtliches vorsichtig:** Bezug auf Art. 50 KI-VO und die Ethischen Leitlinien wie in
   `references/transparenz-rahmen.md`; keine Pflicht behaupten, die nicht sicher besteht 🔎.
7. **Datenschutz:** Kürzel und Schule genügen; keine privaten Kontaktdaten.

## Vorgehen
1. **Fall bestimmen** und Prüfung bestätigen lassen (Freigabe, Prüfbericht oder Aussage der
   Lehrkraft); sonst nur vorbereiten und im Protokoll vermerken.
2. **Einrichten:**
   `python3 scripts/kennzeichnung_einrichten.py ORDNER --verantwortlich "KÜRZEL, Schule" [--stand TT.MM.JJJJ]`
   – ergänzt den Block in der Projekt-`phase_config.yaml` bzw. legt `ki_kennzeichnung.yaml`
   an und erzeugt die Transparenzerklärung aus `assets/vorlage-ki-transparenz.md`, falls sie
   fehlt. `--trockenlauf` zeigt vorher, was geschähe.
3. **Erklärung vervollständigen:** Platzhalter ersetzen, Nicht-Zutreffendes streichen
   (Leitlinie 2).
4. **Kennzeichnen:**
   - Kursprojekt: `edu-kennzeichnung ORDNER` bzw. `python3 scripts/edu.py kennzeichnung ORDNER`
   - Materialordner: zusätzlich `--config ORDNER/ki_kennzeichnung.yaml`
5. **Prüfen:** derselbe Befehl mit `--pruefen` (Exitcode 1 bei Lücken). Neue Dateien im
   Materialordner in `blockzitat` nachtragen.
6. **Andere Medien:** passende Texte aus `assets/vorlage-hinweistexte.md` mit denselben
   Angaben ausfüllen und der Lehrkraft zum Einfügen geben – für einen KI-Chat im Kurs Text 6
   (dort, wo Lernende den Chat öffnen).
7. **Protokoll** nach `assets/vorlage-protokoll.md`.

Entfernen (z. B. für eine Fassung ohne KI-Anteil): `--entfernen`.

**Ohne Skriptausführung:** Hinweis als Blockzitat nach `assets/vorlage-hinweistexte.md`
(Kurzfassung) von Hand ans Seitenende setzen; Erklärung nach Vorlage.

## Ausgabe
- Hinweisblöcke in den Dateien (zwischen `KI-KENNZEICHNUNG:START/ENDE`)
- Transparenzerklärung (`docs/ki-transparenz.md` bzw. `ki-transparenz.md`)
- Konfiguration (Block in der `phase_config.yaml` bzw. `ki_kennzeichnung.yaml`)
- `96_ki-kennzeichnung_<kurztitel>.md` – Protokoll (Artefakt nach Skill-Vertrag)

## Qualitätscheck
- [ ] Prüfung durch die Lehrkraft bestätigt, bevor gekennzeichnet wurde?
- [ ] Verantwortliche Person echt benannt, keine Platzhalter in der Erklärung?
- [ ] `--pruefen` ohne Lücken?
- [ ] Form passend zum Medium?
- [ ] Gleiche Angaben in allen Medien?

## Beispielaufrufe
> „Kennzeichne alle Materialien im Ordner LF4 als KI-unterstützt – verantwortlich ist MH,
> BBS Musterstadt, geprüft habe ich sie heute."

> „Sind in meinem Kursprojekt alle Seiten gekennzeichnet?"

> „Ich brauche einen KI-Hinweis für die Fußzeile meiner Arbeitsblätter und für den Moodle-Kurs."

## Referenzen – wann lesen
- `references/transparenz-rahmen.md` – **immer** (warum, was, wann, wie, Recht mit 🔎).
- `assets/vorlage-ki-transparenz.md` – Transparenzerklärung.
- `assets/vorlage-hinweistexte.md` – Texte für Word, PDF, Folien, Moodle, H5P, edumaps, KI-Chat im Kurs.
- `assets/vorlage-protokoll.md` – **immer** (Protokoll).
- `references/skill-vertrag.md` – Kopf, Pflichtabschnitte, Planungsakte.
- `scripts/kennzeichnung_einrichten.py` – Konfiguration und Erklärung anlegen.
- `scripts/edu.py` – startet `edu-kennzeichnung` aus der mitgelieferten Kopie
  (`scripts/eduwerkzeuge/`).
