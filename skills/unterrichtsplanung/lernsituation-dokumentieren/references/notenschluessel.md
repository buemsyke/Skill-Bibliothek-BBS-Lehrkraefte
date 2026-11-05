# Notenschlüssel

Gemeinsame Referenz für Leistungsüberprüfungen.
Quelle: `_gemeinsam/notenschluessel.md`.
Die Tabellen sind identisch mit `eduwerkzeuge.bewertung` (`edu-bewertung schluessel --max N`).

## 15-Punkte-System (Standard: `--system 15`)
| ab % | 95 | 90 | 85 | 80 | 75 | 70 | 65 | 60 | 55 | 50 | 45 | 40 | 33 | 27 | 20 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Punkte | 15 | 14 | 13 | 12 | 11 | 10 | 09 | 08 | 07 | 06 | 05 | 04 | 03 | 02 | 01 | 00 |
| Note | 1+ | 1 | 1- | 2+ | 2 | 2- | 3+ | 3 | 3- | 4+ | 4 | 4- | 5+ | 5 | 5- | 6 |

„Unter ausreichend“ = weniger als 04 Punkte (5+ und schlechter).

## Berufliches Gymnasium (Notenpunkte)
Im BG werden Leistungen in **Notenpunkten 15–00** angegeben; die Prozentgrenzen oben sind die
übliche Umrechnung (05 Punkte ab 45 %) 🔎 mit Fachkonferenzbeschluss und EPA-Hinweisen
abgleichen. Der **Bewertungsmaßstab der Abiturprüfung** (Umrechnung der BE in Notenpunkte)
folgt derselben Prozenttabelle (95 … 45/40/33/27/20 %); ältere Vorlagen nennen 34/28 % für 03/02
Punkte 🔎 mit der geltenden Vorgabe abgleichen.
Unter 05 Punkten gilt ein Kurs als unterpunktet (Unterkurs) – Folgen für die
Gesamtqualifikation nach der geltenden Verordnung 🔎. Die Gewichtung von Klausuren und
sonstigen Leistungen (Projekt, Dokumentation, Präsentation, Mitarbeit) legt die Fachkonferenz
fest 🔎.

## Kammer-Schlüssel (`--system ihk`) 🔎
92 / 81 / 67 / 50 / 30 / 0 % → Note 1 … 6. Vor Verwendung mit der zuständigen Kammer bzw. der
Prüfungsordnung abgleichen.

## Eigene Grenzen
`--grenzen "90:1,80:2,65:3,50:4,25:5,0:6"` (Prozent:Note, Stufe ab 0 % Pflicht) – z. B. nach
Fachkonferenzbeschluss. 🔎 Beschluss der Fachkonferenz bzw. Schulregelung ist maßgeblich.

## Beim Erstellen einer Klassenarbeit
- Punktegrenzen **aus der Gesamtpunktzahl rechnen**, nie aus einer anderen Arbeit abschreiben:
  `edu-bewertung schluessel --max N [--system ihk]`.
  Grenzen werden auf **halbe Punkte aufgerundet**, damit jede Grenze
  erreichbar ist (bei Single Choice auf ganze Punkte).
- Nach jeder Änderung der Gesamtpunktzahl neu rechnen.
- Welcher Schlüssel gilt, entscheidet die Schule (Fachkonferenz, Bildungsgang). Prüfungsnahe
  Arbeiten in dualen Berufen nutzen oft den Kammer-Schlüssel – 🔎 mit der Schulregel abgleichen.

## Rechtlicher Rahmen 🔎
- Notenbildung, Gewichtung schriftlich/mündlich und Genehmigungspflichten (z. B. wenn mehr
  als ein Drittel der Arbeiten unter „ausreichend“ liegt) regeln Erlasse und Schulbeschlüsse.
  
- Die Note setzt die Lehrkraft. Der Notenspiegel ist ein Hilfsmittel auf Grundlage
  freigegebener Punkte (DSGVO Art. 22: keine ausschließlich automatisierte Entscheidung).
