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
