---
name: technikfolgen-abschaetzen
description: Plant und prüft Technikfolgenabschätzungen (TFA) für Unterricht an berufsbildenden Schulen und im Beruflichen Gymnasium (Lerngebiet ING5 und übergreifend) – Systemgrenze über den Lebenszyklus, prüfbare Hypothesen mit Prüfverfahren und Ergebnis (bestätigt, widerlegt, offen), Quellenmappe mit Quellentyp und Interessenlage, Perspektiven der Beteiligten mit Pro und Contra, Wertbereiche in Anlehnung an VDI 3780, Zielkonflikte, Maßnahmen gegen negative Folgen und begründetes eigenes Urteil. Achtet auf Kontroversität und Überwältigungsverbot (Beutelsbacher Konsens) und auf Bildung für nachhaltige Entwicklung. Liefert Dossier mit Erwartungshorizont, Arbeitsmaterial und Rollenkarten für Anhörung oder Bürgerdialog; prüft Dossiers und vorhandenes TFA-Material per Skript. Verwenden bei „Technikfolgenabschätzung", „TFA", „Hypothesen prüfen", „Stakeholder-Rollenspiel", „Pro und Contra Windkraft", „Folgen einer Technik bewerten", „Quellen kritisch bewerten".
metadata:
  version: "1.3"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# Technikfolgen abschätzen

## Zweck
Lernende schätzen die Folgen einer Technik für Menschen, Umwelt, Wirtschaft und Gesellschaft
ab. Sie prüfen Hypothesen an Quellen, deren Herkunft und Interesse sie kennen, und bilden ein
eigenes, begründetes Urteil. Die Rahmenrichtlinien des Beruflichen Gymnasiums verlangen das in
ING5 und als übergeordnete Kompetenz („Folgen bewerten“, „Technik als ambivalent beurteilen“).
Der Erlass Demokratiebildung verlangt, Kontroverses kontrovers darzustellen.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

**Ergebnisoffen:** Der Skill liefert Material für eine Abschätzung, keine Argumentationshilfe für
eine Seite. Bestätigte Bedenken bleiben bestätigt. Interessenquellen stehen als Positionen, nie
als einziger Beleg. Widerlegte oder unbelegte Behauptungen erscheinen nur als gekennzeichneter
Fall für Quellenkritik (`references/quellenbewertung.md`). Zahlen, Studien und Rechtsangaben nur
mit Quelle; sonst 🔎.

## Drei Modi

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Entwickeln** | „TFA-Material zu einem Windpark in Niedersachsen" | Dossier mit Erwartungshorizont, Arbeitsblatt Hypothesenprotokoll, Quellenmappe, Rollenkarten |
| **B Prüfen** | „Prüf unsere Schulungsunterlagen und das Rollenspieltranskript" | Befunde zu Hypothesen, Quellen, Kontroversität, Überwältigung; Verbesserungen |
| **C Anhörung vorbereiten** | „Rollenspiel mit Stakeholdern zur Windpark-Planung" | Rollenkarten, Ablauf, Beobachtungsbogen, Rollentausch |

## Eingaben
- **Pflicht (sonst Rückfrage):** Technik bzw. Vorhaben und Bezug (Lernsituation, Lerngebiet).
- **Wichtig, sonst Annahme:** Region, Zeitrahmen, Lerngruppe, Fächerverbindung (z. B. Politik),
  gewünschtes Handlungsergebnis (Dossier, Schulung, Anhörung, Stellungnahme).
- **Optional:** vorhandenes Material, Quellenliste, Expertenkontakte.

## Vorgehen (Modus A)
1. **Systemgrenze:** Teilsysteme und Lebenszyklus (Herstellung, Bau, Betrieb, Rückbau),
   betroffene Gruppen (`references/tfa-methode.md`) – für Lernende als **Systembild**
   (Blockschaltbild als SVG mit `fachdiagramm-erstellen`), nicht als Text und nicht als Zeichnung
   aus Zeichen.
2. **Hypothesen** prüfbar formulieren (Größe, Ort, Vergleichsmaßstab) – positive und negative
   Folgen, auch die Bedenken der Betroffenen; je Hypothese ein Prüfverfahren (Daten, Rechnung,
   Literatur, Befragung, Messung).
3. **Quellenmappe:** je Hypothese mindestens zwei Quellen verschiedenen Typs, davon mindestens
   eine ohne Interessenlage; Typ-Kürzel nach `references/quellenbewertung.md`.
4. **Prüfen und einordnen:** Ergebnis je Hypothese *bestätigt*, *widerlegt* oder *offen* –
   mit Begründung und offener Frage.
5. **Perspektiven** (mindestens drei Beteiligte) mit Position, Pro und Contra; **Wertbereiche**
   in Anlehnung an VDI 3780 (mindestens drei); **Zielkonflikt** benennen, nicht auflösen;
   **Maßnahmen** gegen negative Folgen.
6. **Urteil:** im Erwartungshorizont als Kriterien (Abwägung, Begründung, Gegenargument), nicht
   als „richtige“ Meinung.
7. **Handlungsergebnis und Material:** Hypothesenprotokoll, Quellenmappe, Rollenkarten für eine
   Anhörung mit Rollentausch (`references/rollenspiel.md`), Schulungsunterlage als ehrliche
   Folgendarstellung; Laiensprache mit `sprachsensibel-ueberarbeiten`. Material für Lernende
   nach `references/schuelermaterial.md`: Auftrag kurz und offen, Perspektiven und Wertbereiche
   als Matrix, Zahlen als Diagramm oder Tabelle mit Quelle, Rollenkarten ≤ ~60 Wörter, Quellen
   als Auszug mit Fundstelle statt abgeschrieben.
8. **Querschnitt:** BNE (Dimensionen, Zielkonflikt), Demokratiebildung (Kontroversität,
   Überwältigungsverbot), Europabildung, Medienbildung (`references/querschnittsaufgaben.md`).
9. **Prüfen:** `python3 scripts/tfa_pruefen.py 44_tfa_….md` und
   `python3 scripts/schuelermaterial_pruefen.py 44_tfa_….md 44_rollenkarten_….md` – ❌ beheben,
   ⚠ behandeln.

**Modus B:** vorhandenes Material lesen; Hypothesen, Quellen (Typ, Interessenlage,
Gegenquelle), Ergebnisoffenheit und Sachfehler prüfen (Sachfehler mit `material-pruefen`);
Signale wie „Einwandbehandlung“, „Einwände entkräften“, „Akzeptanz schaffen“ melden und eine
ergebnisoffene Rahmung als fertige Formulierung vorschlagen.

## Ausgabe
`44_tfa_<kurztitel>.md` nach `assets/vorlage-tfa-dossier.md` (Schülerfassung: Auftrag,
Hypothesenprotokoll, Quellenmappe zum Ausfüllen → `# Lösungen und Erwartungshorizont`: Dossier
→ `# Didaktische Hinweise`). Rollenkarten: `44_rollenkarten_<kurztitel>.md` nach
`assets/vorlage-rollenkarten-anhoerung.md`.

## Qualitätscheck
- [ ] Systemgrenze mit Lebenszyklus; Hypothesen prüfbar, positiv und negativ?
- [ ] Je Hypothese Prüfverfahren, Ergebnis (bestätigt/widerlegt/offen), Quellen verschiedenen Typs?
- [ ] Keine Interessenquelle als einziger Beleg; Desinformation nur als gekennzeichneter Analysefall?
- [ ] Mindestens drei Perspektiven mit Pro und Contra; drei Wertbereiche; Zielkonflikt benannt?
- [ ] Ergebnisoffene Rahmung, keine Überwältigung; Urteil über Kriterien bewertet?
- [ ] Zahlen, Studien und Recht belegt oder 🔎?
- [ ] Material für Lernende kurz, mit Systembild und Matrix, Rollenkarten knapp –
      `schuelermaterial_pruefen.py` ohne ❌?
- [ ] `tfa_pruefen.py` ohne ❌?

## Beispielaufrufe
> „Erstelle zur LS ING5.1 ein TFA-Dossier zum Windpark mit Hypothesenprotokoll, Quellenmappe und
> Rollenkarten für eine Anhörung im Gemeinderat."

> „Prüf die Schulungsunterlagen und das Transkript der LS ING5.1 auf Kontroversität und Quellen."

## Referenzen – wann lesen
- `assets/vorlage-tfa-dossier.md` – **immer** (Ausgabeformat, vom Skript gelesen).
- `references/tfa-methode.md` – Systemgrenze, Folgenarten, Hypothesen, Wertbereiche, Urteil. **Immer.**
- `references/quellenbewertung.md` – Quellentypen und Interessenlage. **Immer.**
- `references/querschnittsaufgaben.md` – BNE, Beutelsbacher Konsens, Europa, Medien.
- `references/rollenspiel.md` – Anhörung, Rollentausch, Feedback.
- `assets/vorlage-rollenkarten-anhoerung.md` – Modus C.
- `references/berufliches-gymnasium.md` – BG, Lerngebiet ING5.
- `references/operatoren-afb.md` – Aufträge (beurteilen, bewerten, Stellung nehmen).
- `references/schuelermaterial.md` – Material für Lernende: kurz, offen, anschaulich, ohne Dekoration.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte.
- `scripts/tfa_pruefen.py` (DOCX/PDF über `scripts/text_lesen.py`) – Prüfung des Dossiers bzw. Materials (lokal).
- `scripts/schuelermaterial_pruefen.py` – Form des Materials für Lernende.
