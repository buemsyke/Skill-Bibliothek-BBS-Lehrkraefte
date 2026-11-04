<!-- Assistenten-Fassung des Skills 'technikfolgen-abschaetzen'. Abschnitt ANWEISUNG als Systemanweisung einfügen; ANHÄNGE als Wissensbasis hochladen oder anhängen. -->
# ANWEISUNG
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

# ANHÄNGE

## Anhang: assets/vorlage-rollenkarten-anhoerung.md

---
artefakt: Rollenkarten
titel: "Anhörung: [Vorhaben]"
skill: technikfolgen-abschaetzen
skill_version: "1.3"
stand: JJJJ-MM-TT
bildungsgang: "[Bildungsgang]"
curriculare_vorgabe: "[RRL/RLP, Lerngebiet/Lernfeld]"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
---

# Anhörung: [Vorhaben]

**Rahmen:** [Gemeinderat, Bürgerversammlung, Podiumsdiskussion] · **Dauer:** [30–45 min] ·
**Leitung:** [Moderation durch eine Lernende oder einen Lernenden]

**Regeln:** Jede Rolle vertritt ihre Position mit Belegen aus der Quellenmappe. Gegenargumente
werden wiedergegeben, bevor man antwortet. Keine Rolle „gewinnt“. Nach der ersten Runde werden
die Rollen getauscht.

## Rollenkarte: [Beteiligte Gruppe] (fiktiv)

- **Anliegen:** […]
- **Verdeckte Information** (erst auf gute Nachfrage): […]
- **Belege:** [Q-Nummern der Quellenmappe]
- **Wozu Sie bereit sind:** [Kompromiss, Bedingung]

<!-- je beteiligter Gruppe eine Karte (≤ ~60 Wörter): Anwohnende, Landwirtschaft, Naturschutz,
     Gemeinde, Netzbetreiber, Unternehmen … Belege als Q-Nummern, nicht abgeschrieben. -->

## Beobachtungsbogen

| Kriterium | gelungen | teilweise | noch nicht | Beobachtung |
|---|---|---|---|---|
| Position der Rolle glaubwürdig vertreten | | | | |
| Belege statt Behauptungen | | | | |
| Gegenargument wiedergegeben und beantwortet | | | | |
| Zielkonflikt oder Kompromiss benannt | | | | |

## Auswertung

1. Welche Hypothesen wurden in der Anhörung bestätigt, welche blieben offen?
2. Was hat sich an Ihrer eigenen Einschätzung durch den Rollentausch geändert?

# Didaktische Hinweise

- Rollen zulosen oder nach Interesse wählen lassen; verdeckte Informationen nur auf der Karte der Rolle.
- Ergebnisoffen moderieren (Beutelsbacher Konsens): Die Lehrkraft bewertet Begründungen, nicht Positionen.

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Jede Rolle mit Belegen aus der Quellenmappe (Q-Nummern), keine erfundenen Zahlen | ✅/⚠️/❌ | |
| Positionen ausgewogen, keine Rolle als „richtig“ angelegt | | |
| Rollenkarten je ≤ ~60 Wörter, Gruppen als fiktiv gekennzeichnet | | |
| Beobachtungsbogen beobachtbar formuliert, ohne Noten | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Ergebnisse der Anhörung gehen ins Urteil des Dossiers (`44_tfa_…`).
- Empfohlene nächste Skills: `material-pruefen`, `sprachsensibel-ueberarbeiten`

> KI-gestützt erstellt (Skill technikfolgen-abschaetzen v1.3). Fachliche Prüfung und Verantwortung: Lehrkraft.

## Anhang: assets/vorlage-tfa-dossier.md

---
artefakt: Technikfolgenabschätzung
titel: "[Technik bzw. Vorhaben]"
skill: technikfolgen-abschaetzen
skill_version: "1.3"
stand: JJJJ-MM-TT
bildungsgang: "[Bildungsgang]"
curriculare_vorgabe: "[RRL/RLP, Lerngebiet/Lernfeld]"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
---

# Technikfolgenabschätzung: [Titel]

<!-- Tabellenköpfe so lassen – tfa_pruefen.py liest sie. Ergebnis je Hypothese: bestätigt,
     widerlegt oder offen. Typ-Kürzel der Quellen nach quellenbewertung.md. -->

## Auftrag

[Ergebnisoffene Rahmung: Wer will die Abschätzung, wozu, und warum ehrlich?]

## Systemgrenze

- Teilsysteme: […]
- Lebenszyklus: Herstellung · Bau · Betrieb · Rückbau
- Betroffene: […]

[ABBILDUNG: Systembild – Teilsysteme, Stoff- und Energieflüsse, Lebenszyklus, Betroffene
(Blockschaltbild als SVG mit fachdiagramm-erstellen); Alternativtext]

## Hypothesen

| Nr. | Hypothese (prüfbar) | Prüfverfahren | Quellen | Ergebnis | Begründung und offene Frage |
|---|---|---|---|---|---|
| H1 | […] | [Daten / Rechnung / Literatur / Befragung / Messung] | Q1, Q2 | [bestätigt / widerlegt / offen] | […] |

## Quellenmappe

| Nr. | Quelle (Titel, Herausgeber, Jahr, Fundstelle) | Typ | Interessenlage | Kernaussage | gestützt durch |
|---|---|---|---|---|---|
| Q1 | […] | [amtlich / wissenschaft / norm / verband / unternehmen / initiative / presse / sekundaer / einzelmeinung / ki] | [gering / Branche / Anliegen …] | […] | [Q-Nr.] |

## Perspektiven

| Beteiligte | Position | Pro | Contra |
|---|---|---|---|
| [Gruppe] | […] | […] | […] |

## Wertbereiche

| Wertbereich (in Anlehnung an VDI 3780) | Folgen | Einschätzung |
|---|---|---|
| [Sicherheit / Gesundheit / Umweltqualität / Wirtschaftlichkeit / Wohlstand / Funktionsfähigkeit / Persönlichkeitsentfaltung / Gesellschaftsqualität] | […] | […] |

## Zielkonflikt

[Welche Wertbereiche stehen gegeneinander? Was bleibt offen?]

## Maßnahmen gegen negative Folgen

- […]

## Urteil

[Begründetes Urteil mit Kriterien, Belegen, Gegenargument und Bedingung]

# Lösungen und Erwartungshorizont

[Erwartungen je Hypothese; Kriterien für das Urteil (Abwägung, Begründung, Gegenargument,
Zielkonflikt) – keine „richtige“ Meinung]

# Didaktische Hinweise

[Rahmung, Fächerverbindung, Querschnittsaufgaben, Zeit, Lernhürden (Hypothese ≠ Meinung,
Interessenquelle als Beleg, Korrelation ≠ Kausalität)]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: …

## Übergabe

- Hypothesen mit Ergebnis, Quellenmappe, Perspektiven
- Empfohlen: `sprachsensibel-ueberarbeiten` (Laiensprache),
  `material-pruefen` (Sachfehler)

> KI-gestützt erstellt (Skill technikfolgen-abschaetzen v1.3). Fachliche Prüfung und Verantwortung: Lehrkraft.

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
  Vorschläge erstellen: `abiturvorschlag-erstellen`.
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

## Anhang: references/rollenspiel.md

# Rollenspiel-Framework

Gespräche – Kundenberatung, Reklamation, Mitarbeiter- oder Elterngespräch, Anhörung mit
mehreren Beteiligten – lassen sich schlecht aus einem Buch lernen. Ein Rollenspiel mit der KI
übt sie gefahrlos und beliebig oft; im Unterricht trägt dasselbe Framework Rollenspiele
zwischen Lernenden (Rollenkarten, Beobachtungsbogen).
Trennung wie im Artikel: **Das Framework** (dieses Dokument, wiederverwendbar) legt fest, *wie*
gespielt wird; **das Szenario** steht im Auftrag bzw. im Steckbrief.

## 1. Spielregeln für die KI

1. **Rollen kenntlich machen.** Jeder Beitrag beginnt mit der Kennung:
   `[Rolle: Frau Beispiel (fiktiv), Kundin]` bzw. `[Coach]`. Mehrere Figuren nacheinander
   bekommen je eine eigene Kennung.
2. **In der Rolle bleiben**, bis die lernende Person einen Befehl gibt oder das Gespräch
   natürlich endet. Ton passend zum Szenario: Team-Chat, Telefonat, Gespräch an der Anlage.
3. **Improvisieren erlaubt.** Die Figur darf ausweichen, ungeduldig oder skeptisch sein,
   überraschen und unbequem werden – genau das macht die Übung wirksam. Sie bleibt dabei
   realistisch und respektvoll: keine Beleidigungen, keine Diskriminierung, keine Drohungen.
4. **Verdeckte Information.** Jede Figur hat etwas, das sie erst auf **gute Nachfragen**
   preisgibt (wahrer Grund, eigentlicher Bedarf, Vorgeschichte). Schlechte oder suggestive
   Fragen bringen sie nicht heraus.
5. **Kurze Beiträge** (ein bis vier Sätze), damit die lernende Person führen muss.
6. **Fachlich korrekt.** Nennt die Figur Fachliches, stimmt es mit den Quellen überein; die
   Figur darf Laienbegriffe benutzen und Fachchinesisch zurückfragen.
7. **Keine echten Personen, Firmen oder Daten.** Namen sind erkennbar fiktiv.

## 2. Steuerbefehle der lernenden Person

| Befehl | Wirkung |
|---|---|
| `STOPP` | Szene anhalten; `[Coach]` fragt, was los ist, und gibt einen Hinweis |
| `WEITER` | Szene an derselben Stelle fortsetzen |
| `NEUSTART` | Szene mit derselben Figur von vorn |
| `NÄCHSTE` | nächste Figur der Serie |
| `FEEDBACK` | Szene beenden, Feedback nach Kriterien |

## 3. Serie

Drei Durchgänge mit unterschiedlichen Figuren, vom echten Notfall bis zum bloßen Wunsch –
so lernt die lernende Person zu unterscheiden, statt ein Schema abzuspulen. Am Ende jeder Szene
eine **Entscheidung**, die die lernende Person trifft und begründet (z. B. Auftrag annehmen
oder nicht, Urlaub genehmigen oder nicht, Termin sofort oder später).

## 4. Feedback

Nach `FEEDBACK` oder dem Gesprächsende, klar abgesetzt (`--- Feedback ---`):
- je Kriterium (drei bis vier, aus dem Steckbrief): **was gut lief** – mit kurzem Zitat aus dem
  Gespräch – und **ein konkreter Tipp** für das nächste Mal;
- die Entscheidung: nachvollziehbar begründet? andere vertretbare Entscheidung?
- **keine Note, keine Punkte**; Ton wertschätzend und konkret.

Kriteriensätze (Beispiele):

| Gesprächsart | Kriterien |
|---|---|
| Führung, Mitarbeitergespräch | Kommunikation · Empathie · Fairness · Führung |
| Kundenberatung | Bedarfsermittlung · Fachlichkeit · Verständlichkeit · Umgang mit Einwänden |
| Reklamation | Zuhören · Sachklärung · Lösungsangebot · Verbindlichkeit |
| Übergabe an Kundschaft | Vollständigkeit · Verständlichkeit · Sicherheitshinweise · Dokumentation |
| Elterngespräch, Ausbildergespräch | Gesprächsrahmen · Sachlichkeit · Perspektivwechsel · Vereinbarung |
| Anhörung, Bürgerdialog, Podiumsdiskussion (mehrere Beteiligte) | Perspektivübernahme · Belege statt Behauptungen · Umgang mit Kritik · Abwägung und Zielkonflikt |

**Anhörung statt Verkaufsgespräch.** Bei gesellschaftlich umstrittenen Themen (z. B.
Technikfolgenabschätzung) ist das Rollenspiel ein **Perspektivwechsel**, kein Training im
Widerlegen von Einwänden. Keine Rolle „gewinnt“. Bedenken, die die Prüfung bestätigt, werden
anerkannt. Nach einer Runde werden die Rollen getauscht. Abschluss ist ein eigenes begründetes
Urteil der Lernenden (Beutelsbacher Konsens, `querschnittsaufgaben.md`, falls vorhanden).

## 5. Szenario-Steckbrief (Vorlage)

```markdown
## Rollenspiel: <Titel>
- **Lernende Person:** <Rolle, z. B. Anlagenmechanikerin SHK im 2. Ausbildungsjahr>
- **Situation:** <Ort, Anlass, Vorgeschichte – zwei bis drei Sätze>
- **Ton:** <Telefonat | Gespräch vor Ort | Team-Chat>
- **Figuren (Serie):**
  1. <Figur, fiktiv> – Anliegen: … – verdeckt: … – Haltung: …
  2. <Figur, fiktiv> – Anliegen: … – verdeckt: … – Haltung: …
  3. <Figur, fiktiv> – Anliegen: … – verdeckt: … – Haltung: …
- **Entscheidung am Ende:** <was die lernende Person entscheiden muss>
- **Kriterien für das Feedback:** <drei bis vier>
- **Quellen für Fachliches:** <Q-Nummern der Lernakte>
```

## 6. Beispiele für berufsbildende Schulen

| Bildungsgang | Szenario | verdeckte Information |
|---|---|---|
| Anlagenmechaniker/-in SHK | Kundin meldet Gluckern und oben kalte Heizkörper | hat selbst Wasser nachgefüllt, weiß nicht wie viel |
| Kfz-Mechatroniker/-in | Kunde holt Fahrzeug ab, Rechnung höher als erwartet | hatte Zusatzarbeiten telefonisch freigegeben, erinnert sich nicht |
| Industriemechaniker/-in | Schichtleiter will Anlage trotz Störung weiterlaufen lassen | Liefertermin für einen Großkunden am Abend |
| Fachinformatiker/-in | Anwenderin meldet „das Internet ist kaputt" | hat ein neues Gerät mitgebracht und angeschlossen |
| Lehrkraft (Fortbildung) | Auszubildender kommt wiederholt zu spät | pflegt nachmittags einen Angehörigen (Figur fiktiv, sensibel spielen) |
| Berufliches Gymnasium Technik (ING5) | Anhörung zum Windpark: Anwohnerin, Landwirt, Naturschutzverband, Netzbetreiber, Projektierer | Anwohnerin fürchtet vor allem Wertverlust des Hauses; Landwirt rechnet mit Pacht |

## 7. Umsetzung je Plattform

- **Claude:** Framework (dieses Dokument) + Steckbrief im Auftrag; Rollenspiel als eigener
  Skill nur, wenn es über viele Lernprojekte wiederkehrt.
- **AIS.chat:** als **Dialogpartner** anlegen – Spielregeln, Steuerbefehle und
  Feedbackregeln in das Verhaltensfeld, je Figur ein eigener Dialogpartner oder die Serie in
  einem (Vorlage im Skill `agiles-lernen-mit-ki`: AIS-Paket, Abschnitt D).
- **Unterricht ohne KI:** Rollenkarten je Figur (Anliegen, verdeckte Information, Haltung,
  Belege), Beobachtungsbogen mit den Kriterien aus Abschn. 4, Auswertung im Plenum.

## Anhang: references/schuelermaterial.md

# Material für Lernende – knapp, offen, anschaulich

Gemeinsame Regel für alles, was Lernende in die Hand bekommen: Arbeitsblatt, Infoblatt,
Situationsmaterial, Vorlagen, Hilfekarten, Versuchsanleitung, Programmieraufgabe, Rollenkarten,
Lektion, Lernlandkarte, Quiz und Schülerseiten. Ausgenommen ist der Lehrerteil
(`# Lösungen und Erwartungshorizont`, `# Didaktische Hinweise`). Vorgabe der Fachberatung
(31.10.2026). Prüfung: `scripts/schuelermaterial_pruefen.py`, falls vorhanden.
Klausur- und Abiturformat haben eigene Richtwerte (`klausur-erstellen`, `abiturvorschlag-erstellen`);
die vier Regeln gelten dort sinngemäß.

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
| Aufbau einer Anlage, eines Bauteils, eines Versuchs | beschriftete Skizze, Foto mit Positionsnummern, Anlagenbild | eigenes Foto oder Herstellerunterlage (Platzhalter mit Quelle); Blockschaltbild mit `fachdiagramm-erstellen`; Technologieschema mit `technologieschema-erstellen` |
| Ablauf, Vorgehen, Programm | Ablaufdiagramm, Struktogramm, Zustandsdiagramm | `fachdiagramm-erstellen`; GRAFCET und Funktionsplan mit `technologieschema-erstellen` |
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
Ausgenommen von den Richtwerten sind Klausur- und Abiturformat mit eigenen Regeln
(`klausur-erstellen`, `abiturvorschlag-erstellen`: Operator-Aufträge bis rund 40 bzw. 45 Wörter,
Antwortraum je Operator); kurz, eindeutig und ohne Dekoration bleiben auch sie.

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
| Anlagenbild (Technologieschema), Schaltplanauszug mit Schaltzeichen, GRAFCET, Funktionsplan (FUP), Netzplan | `technologieschema-erstellen` |
| Simulationsschaltung | `circuitjs-schaltung-erstellen` |

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
| 46 | Technologieschema (Schemablatt mit Legende, Specs unter `schema/`, SVG unter `abbildungen/`) | technologieschema-erstellen |
| 47 | Simulationsschaltung (circuit.js: Schaltungstext, Messgeräte mit Erwartungswerten, Begleitblatt) | circuitjs-schaltung-erstellen |
| 48 | Mikrocontroller-Simulation (Wokwi: Spec, Projektordner mit Sketch, Schaltung und Szenarien, Zeitablauf, Begleitblatt) | wokwi-simulation-erstellen |
| 50 | Sprachsensible Fassung | sprachsensibel-ueberarbeiten |
| 60 | Differenzierung | differenzierung-erstellen |
| 65 | Quiz (Quelle, GIFT, H5P, Begleitblatt) | quizfragen-erstellen |
| 70 | Klassenarbeit / Lernzielkontrolle mit Erwartungshorizont | klausur-erstellen |
| 75 | Abiturvorschlag (dezentral): Schüler- und Lehrermaterial je Vorschlag, Bewertungsbogen, Begleitblatt | abiturvorschlag-erstellen |
| 90 | Prüfbericht | material-pruefen |
| 92 | Lernlandkarte (edumaps: Quelle, Import-JSON, Begleitblatt) | lernlandkarte-erstellen |
| 93 | Lernakte, Probeprüfung, AIS-Paket (agiles Lernen mit KI) | agiles-lernen-mit-ki |
| 94 | Veröffentlichungsprotokoll Schülerausgabe | schuelerseiten-veroeffentlichen |
| 95 | KI-Chatbot (Paket mit Systemanweisung und Probelauf), Promptgutachten | ki-chatbot-einrichten |
| 96 | KI-Kennzeichnung (Protokoll) | ki-kennzeichnung |
| 99 | Abschlussbericht (Paketübersicht, Qualitätscheck, konsolidierte Prüfaufträge) | unterricht-entwickeln |

`abiturvorschlag-erstellen` (Nr. 75) hält Schüler- und Lehrermaterial einreichungsfertig: Kopf und
Pflichtabschnitte stehen im **Begleitblatt** (`75_abitur_<kurztitel>_begleitblatt.md`), nicht in den
Einreichungsunterlagen.

**Werkzeug-Skills** (Nr. 42, 46, 47, 48, 65, 92) erzeugen außer dem Artefakt Dateien mit Werkzeugen
(`edu-diagramm`, `edu-technologieschema`, `schaltung.py`, `wokwi.py`, `edu-quiz`, `edu-edumap`). Die Quelle (YAML bzw. Markdown) ist dann kein
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

## Anhang: references/tfa-methode.md

# Technikfolgenabschätzung im Unterricht – Methode

Eigene Zusammenfassung für den Unterricht. Grundlage sind die Verfahren der
Technikfolgenabschätzung und -bewertung, wie sie u. a. die VDI-Richtlinie 3780 *Technikbewertung –
Begriffe und Grundlagen* (2000) und Institute wie das ITAS am KIT beschreiben 🔎 Originaltext.

## 1. Wozu TFA?

Technik wirkt über ihren Zweck hinaus – erwünscht und unerwünscht, sofort und später, nah und
fern. Eine TFA macht diese Folgen sichtbar, **bevor** entschieden wird, und benennt, was offen
ist. Sie ist keine Werbung und keine Ablehnung, sondern eine Entscheidungshilfe.

## 2. Systemgrenze und Lebenszyklus

- **Was wird betrachtet?** Ganze Anlage oder ein Teilsystem (z. B. Rotorblatt, Fundament,
  Netzanschluss), ein Standort oder viele.
- **Lebenszyklus:** Rohstoffe und Herstellung → Transport und Bau → Betrieb → Rückbau,
  Wiederverwendung, Recycling.
- **Wer ist betroffen?** Anwohnende, Landwirtschaft, Natur, Gemeinde, Netzbetreiber,
  Beschäftigte, künftige Generationen.

## 3. Folgenarten

| Unterscheidung | Beispiel |
|---|---|
| beabsichtigt – unbeabsichtigt | Strom aus Wind – Schattenwurf |
| direkt – indirekt | Flächenverbrauch – veränderte Pachtpreise |
| kurz – langfristig | Baulärm – Rückbau nach Jahrzehnten |
| lokal – global | Landschaftsbild – Treibhausgasbilanz |
| sicher – unsicher | gemessene Schallpegel – künftige Recyclingverfahren |

## 4. Hypothesen

- **Prüfbar:** nennt eine Größe, einen Ort oder Vergleichsmaßstab und eine Richtung.
  „Am nächsten Wohnhaus wird der nächtliche Richtwert für Lärm überschritten.“ statt
  „Windräder machen krank.“
- **Beide Richtungen:** Hypothesen zu Nutzen und zu Schaden, auch die Bedenken der Betroffenen.
- **Prüfverfahren:** Daten (z. B. Netz- und Wetterdaten), Rechnung (Energiebilanz), Literatur
  (amtliche und wissenschaftliche Quellen), Befragung von Fachleuten, Messung.
- **Ergebnis:** *bestätigt*, *widerlegt* oder *offen* – mit Begründung und der Information, die
  für ein sicheres Urteil fehlt.

## 5. Wertbereiche (in Anlehnung an VDI 3780)

Die Richtlinie ordnet die Ziele technischen Handelns in Wertbereiche: **Funktionsfähigkeit,
Wirtschaftlichkeit, Wohlstand, Sicherheit, Gesundheit, Umweltqualität, Persönlichkeitsentfaltung
und Gesellschaftsqualität**. Die Werte können sich gegenseitig fördern oder in Konkurrenz stehen.
Für den Unterricht reicht: je Folge den betroffenen Wertbereich benennen und Konflikte zwischen
Wertbereichen sichtbar machen.

## 6. Sachurteil und Werturteil

- **Sachurteil:** Was ist (wahrscheinlich) der Fall? → Hypothesenprüfung.
- **Werturteil:** Wie ist das zu bewerten, gemessen an welchen Werten? → Wertbereiche,
  Abwägung.
- **Zielkonflikt** benennen, nicht wegdefinieren (z. B. Klimaschutz und Versorgungssicherheit ↔
  Landschaftsbild, Artenschutz, Lärm).
- **Maßnahmen** zeigen, wie negative Folgen kleiner werden (Abschaltalgorithmen, Abstand,
  Design for Recycling, Beteiligung der Gemeinde).

## 7. Kontroversität und Rolle der Lernenden

- Was in Wissenschaft und Gesellschaft umstritten ist, erscheint kontrovers – mit Positionen und
  Begründungen (Beutelsbacher Konsens, `querschnittsaufgaben.md`, falls vorhanden).
- **Rahmung prüfen:** Ein Auftrag „Einwände des Vertriebs entkräften“ macht aus der TFA
  Marketing. Gute Alternative: Ein Unternehmen will Vertrauen gewinnen und lässt deshalb ehrlich
  abschätzen – auch, was gegen das Vorhaben spricht.
- **Rollenspiel als Perspektivwechsel:** Anhörung oder Bürgerdialog mit Rollentausch, kein
  Verkaufsgespräch, keine Gewinner (`rollenspiel.md`, falls vorhanden).
- **Eigene Rolle reflektieren:** Was ändert sich am Urteil, wenn ich im Auftrag des
  Unternehmens, der Gemeinde oder einer Initiative spreche?

## 8. Erwartungshorizont für Urteile

Bewertet wird die **Qualität der Begründung**, nicht die Meinung:
- Urteil benennt Kriterien bzw. Wertbereiche.
- Belege aus geprüften Hypothesen.
- Mindestens ein Gegenargument wird wiedergegeben und gewichtet.
- Zielkonflikt und offene Fragen werden benannt.
- Folgerung (Empfehlung, Bedingung, Maßnahme) passt zur Begründung.
