---
name: dqr-zuordnen
description: Ordnet einen Bildungsgang, Ausbildungsberuf oder Abschluss dem Deutschen Qualifikationsrahmen (DQR, Niveau 1–8) zu, begründet die Zuordnung an den amtlichen Deskriptoren (Wissen, Fertigkeiten, Sozialkompetenz, Selbständigkeit) und leitet daraus Folgen für den Unterricht ab – Anforderungsniveau, Grad der Selbständigkeit, Offenheit von Handlungssituationen, AFB-Verteilung. Prüft außerdem, ob Lernsituationen, Kompetenzformulierungen oder Aufgaben zum Zielniveau passen, und formuliert Kompetenzen niveaugerecht. Verwenden bei Fragen wie „Welches DQR-Niveau hat …?", „Passt meine Lernsituation zu DQR 4?", „Formuliere die Kompetenzen auf Niveau 3", für die Niveauangabe in Unterrichtsentwürfen oder bei der Planung eines Bildungsgangs.
metadata:
  version: "1.2"
  bibliothek: unterrichtsentwicklung-bbs
  bereich: planung
  stand: "2026-11"
license: CC BY-SA 4.0 (Texte), MIT (Skripte) – siehe LICENSE.txt
---

# DQR-Zuordnung

## Zweck
Das Kompetenzniveau eines Bildungsgangs belastbar bestimmen und in **konkrete
Planungsentscheidungen** übersetzen – damit Lernsituationen, Aufgaben und Bewertung weder
über- noch unterfordern.

## Arbeitsweise (Skill-Vertrag, Kurzform)
Entwurf vor Rückfrage · Annahmen als `⚠️ Annahme:` markieren · nichts erfinden, Unsicheres als
`🔎 Prüfen:` · vorhandene Planungsakte nutzen und fortschreiben · einheitlicher Kopf und
Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzhinweis).
Details: `references/skill-vertrag.md`.
**Zeichnungen** nur als SVG aus den Zeichen-Skills, nie als ASCII-Art oder Mermaid (Skill-Vertrag
Abschn. 3, Prüfung `scripts/zeichnungen_pruefen.py`).

## Drei Modi – aus dem Auftrag ableiten

| Modus | Auftrag (Beispiel) | Ergebnis |
|---|---|---|
| **A Zuordnen** | „Welches DQR-Niveau hat die Ausbildung zur Fachkraft für Metalltechnik?" | DQR-Steckbrief mit Begründung und Planungsfolgen |
| **B Abgleichen** | „Passt diese Lernsituation zu DQR 4?" (Datei/Text) | Niveauprofil des Materials, Abweichungen, Änderungsvorschläge |
| **C Formulieren** | „Formuliere Kompetenzen zu ‚Spannungsmessung' auf Niveau 3." | niveaugerechte Fach- und Personale Kompetenzen |

Mehrere Modi dürfen kombiniert werden (häufig A + C).

## Eingaben
- **Pflicht:** Bildungsgang/Beruf/Abschluss (Modus A) bzw. das zu prüfende Material (Modus B)
  bzw. Thema + Zielniveau (Modus C).
- **Optional:** Ausbildungsjahr bzw. Schuljahrgang, Lernfeld bzw. Lerngebiet, Ordnungsmittel-Auszug, Bundesland.
- Ohne Angabe gilt: Niedersachsen, Berufsschule, Niveau laut amtlicher Liste.

## Vorgehen

1. **Qualifikation bestimmen.** In `references/dqr-zuordnungen.md` den Qualifikationstyp
   suchen. Ergebnis immer mit Quelle und Stand angeben („DQR-Liste, Stand 01.08.2025").
   Nicht gelistet → „nicht zugeordnet" sagen; eine eigene Einschätzung ist dann als
   **didaktische Einschätzung** zu kennzeichnen, nie als amtliche Zuordnung.
2. **Deskriptoren abgleichen.** Für das Zielniveau und die Nachbarniveaus die vier Säulen aus
   `references/dqr-niveaus.md` mit dem Bildungsgang bzw. Material vergleichen. Belege aus dem
   gelieferten Ordnungsmittel zitieren; fehlt eins, typische Anforderungen des Berufs nennen
   und als Annahme markieren.
3. **Anforderungsstruktur prüfen** (DQR-Glossar): Komplexität, Dynamik, erforderliche
   Selbständigkeit, Innovationsfähigkeit. Unterscheiden: **Aufgabe** (Zielzustand und Methode
   vorgegeben) vs. **Problem** (Ausgangszustand selbst spezifizieren, Methode selbst wählen).
4. **Progression beachten.** Das Niveau gilt dem **Abschluss**. Für frühe Ausbildungsjahre
   eine begründete Progression vorschlagen (z. B. LF 1–4 überwiegend Merkmale von Niveau 3,
   ab dem 3. Jahr durchgängig Niveau 4) – als Planungsentscheidung gekennzeichnet. Im
   **Beruflichen Gymnasium** (AHR, DQR 4) über die Schuljahrgänge: Jg. 11 (Einführungsphase)
   Merkmale von Niveau 3 zulässig, Jg. 12 angeleitete Projekte, Jg. 13 durchgängig Niveau 4
   (`references/berufliches-gymnasium.md`).
5. **Planungsfolgen ableiten** (Tabelle unten) und mit Beispielen aus dem Fach füllen.
6. **Modus B:** Jede Kompetenzformulierung bzw. Aufgabe einem Niveau zuordnen
   (Indikatoren: Anleitungsgrad, Offenheit, Beurteilungsmaßstab, Transfer). Abweichungen
   ≥ 1 Niveau benennen und eine umformulierte Fassung anbieten.
7. **Modus C:** Kompetenzen aktiv formulieren („Die Schülerinnen und Schüler …"), Fach- und
   Personale Kompetenz getrennt, Operatoren aus `references/operatoren-afb.md`; die
   niveautypischen Signalwörter aus den Deskriptoren aufnehmen (z. B. Niveau 4: *selbständig
   planen, Handlungsalternativen beurteilen, Abläufe begründen*).
8. Qualitätscheck, dann ausgeben.

## Planungsfolgen – Tabelle, die immer ausgefüllt wird

| Planungsmerkmal | Niveau n − 1 (zur Abgrenzung) | **Zielniveau n** | Konkreter Hinweis für dieses Fach |
|---|---|---|---|
| Handlungssituation (Struktur, Offenheit) | | | |
| Anleitung vs. Selbständigkeit | | | |
| Beurteilungsmaßstab für Ergebnisse | | | |
| Transfer | | | |
| Zusammenarbeit/Kommunikation | | | |
| Lernberatung / Lernhilfen | | | |
| Schwerpunkt AFB / Taxonomiestufen | | | |

Für die AFB-Verteilung gelten nur **Faustwerte, keine amtliche Vorgabe**: Niveau 2 eher
I > II > III; Niveau 3 Schwerpunkt II mit einfachen III-Anteilen; Niveau 4 Schwerpunkt II mit
deutlichem III-Anteil (Beurteilen unter Handlungsalternativen); Niveau 6 Schwerpunkt II–III
mit offenen Problemstellungen.

## Ausgabe

Datei `10_dqr-einordnung.md` (bzw. im Chat) mit Kopf nach Skill-Vertrag – bei mehreren
Lernsituationen desselben Bildungsgangs **eine** Datei mit gemeinsamem Steckbrief und je LS
einem Niveauprofil –, dann:
1. **DQR-Steckbrief** – Qualifikation, amtliches Niveau, Quelle/Stand, Niveauindikator im Wortlaut
2. **Begründung** – Vier-Säulen-Abgleich (Tabelle: Säule | Deskriptor Zielniveau | Beleg im
   Bildungsgang | Abgrenzung zum Nachbarniveau)
3. **Planungsfolgen** – Tabelle oben, ggf. Progression über die Ausbildungsjahre bzw. Schuljahrgänge
4. Modus B: **Niveauprofil des Materials** (Element | festgestelltes Niveau | Begründung |
   Vorschlag) · Modus C: **Kompetenzformulierungen**
5. Pflichtabschnitte (Qualitätscheck, Annahmen und Prüfaufträge, Übergabe mit `dqr: n` und
   Kernaussagen für Folge-Skills, Transparenzhinweis)

## Qualitätscheck
- [ ] Amtliches Niveau mit Quelle und Stand – oder ausdrücklich „nicht zugeordnet"?
- [ ] Amtliche Zuordnung und didaktische Einschätzung sauber getrennt?
- [ ] Alle vier Säulen abgeglichen, Nachbarniveau zur Abgrenzung genutzt?
- [ ] Planungsfolgen konkret für das Fach (keine Deskriptor-Paraphrasen)?
- [ ] Kompetenzen aktiv, beobachtbar, ohne „verstehen/kennen/wissen"?
- [ ] AFB-Hinweise als Faustwerte gekennzeichnet?

## Beispielaufrufe
> „Ordne die Ausbildung Kraftfahrzeugmechatroniker/-in in den DQR ein und sag mir, was das für
> Lernsituationen im 1. Ausbildungsjahr bedeutet."

> „Hier sind die Kompetenzen meiner Lernsituation (Anhang). Entsprechen sie DQR 4? Mach
> Verbesserungsvorschläge."

## Referenzen – wann lesen
- `references/dqr-zuordnungen.md` – **immer** in Schritt 1 (amtliche Liste, Schulformbrücke).
- `references/dqr-niveaus.md` – Schritt 2–7 (Deskriptoren im Wortlaut, Glossar, Kurzübersicht).
- `references/operatoren-afb.md` – Modus C und Vorschläge in Modus B.
- `references/berufliches-gymnasium.md` – BG: Phasen, Lerngebiete, Progression Jg. 11–13.
- `references/skill-vertrag.md` – Ausgabeformat, Planungsakte, Redlichkeitsregeln.
