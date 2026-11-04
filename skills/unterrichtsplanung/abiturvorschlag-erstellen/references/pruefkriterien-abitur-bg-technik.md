# Prüfkriterien Abiturvorschlag – Berufliches Gymnasium Technik (eA)

Grundlage: Gutachtenvorlage MK Niedersachsen; EPA Technik mit dem Aufgabenbeispiel
Ingenieurwissenschaften (KMK 16.12.2021); Rahmenrichtlinien für das Fach Technik im Beruflichen
Gymnasium (Stand Mai 2008, Erweiterungen 2014, 2016, **Juni 2025**). Zusammengestellt aus der
Gutachtenpraxis der Fachberatung (Stand 2025/26). 🔎 Vor jeder Begutachtungsrunde mit der aktuellen
Gutachtenvorlage und der gültigen RRL abgleichen. Die Lerngebiete aller Schwerpunkte (BT, ET, IT,
MT, METRO, GMT, ING) stehen in `berufliches-gymnasium.md`.

**R** = regelbasiert prüfbar – beim Erstellen eines Vorschlags mit `abitur_check.py` (im Ordner `scripts/` des Skills) · **I** = inhaltliche Prüfung.

Gemeinsamer Maßstab für das Erstellen (Skill `abiturvorschlag-erstellen`) und das Begutachten
. **Fach Berufliche Informatik:** Der Katalog gilt sinngemäß
mit der Operatorenliste der EPA Berufliche Informatik (`operatoren-epa-technik.md`, Abschnitt
*Berufliche Informatik*; Profil `abitur-bg-informatik`) 🔎 mit der gültigen Fassung abgleichen.

## 1. Formales
| Nr. | Kriterium | Art |
|---|---|---|
| 1.1 | Schriftbild lesbar, Schriftart durchgängig, Formeln sauber gesetzt | I |
| 1.2 | Dokumentvorlage MK Niedersachsen verwendet (Kopf/Fuß, Deckblatt) | I |
| 1.3 | Deckblatt: „Abitur [Jahr]", „Technik", Schwerpunkt, „Vorschlag X", eA/gA, Bearbeitungszeit | I (+R Platzhalter) |

## 2. Eingereichte Unterlagen
| Nr. | Kriterium | Art |
|---|---|---|
| 2.1 | zwei Vorschläge eingereicht (nur für den vorliegenden bestätigbar) | I |
| 2.2 | Lerngebietszuordnung je Aufgabe | I |
| 2.3 | Unterrichtszusammenhang **konkret** (Inhalte, Tätigkeiten, Bezug zur Prüfung; Halbjahresthema allein reicht nicht – EPA 3.3) | I |
| 2.4 | Erwartungshorizont mit AFB-Zuordnung je Teilaufgabe | I |
| 2.5 | vollständige Musterlösung | I |
| 2.6 | Bewertungsschema mit Umrechnung in Notenpunkte | I |
| 2.7 | Hilfsmittel benannt | I |
| 2.8 | Formelsammlung beigefügt, soweit verwendet | I |

## 3. Fachliches
| Nr. | Kriterium | Art |
|---|---|---|
| 3.1 | übergeordnete Kompetenzen der RRL (Abschnitt 1.3) angesprochen | I |
| 3.2 | Lerngebiete des Schwerpunkts: die beiden verbindlichen Lerngebiete und das an der Schule gewählte optionale (z. B. IT1 + IT2 + eines aus IT3–IT5; ING1 + ING2 + eines aus ING3–ING5) | I |
| 3.3 | ganzheitliche, problembezogene Aufgabenstellung mit Situationsbeschreibung | I |
| 3.4 | Orientierung an beruflicher Handlungskompetenz | I |
| 3.5 | Fach-, Methoden-, ggf. Sozialkompetenz; alle drei AFB vertreten | I |

## 4. Transparenz und Aufgabenformulierung
| Nr. | Kriterium | Art |
|---|---|---|
| 4.1 | klare Formulierung; Lösungsweg nicht vorgezeichnet; in der Steuerungstechnik dieselben Betriebsmittelkennzeichen in Funktionsbeschreibung, Technologieschema, Zuordnungsliste, Aufgaben und Musterlösung | I (+R Hinweise aus `bmk_pruefen.py`) |
| 4.2 | Teilaufgaben unabhängig lösbar – oder Alternativwert angegeben | I |
| 4.3 | in der Bearbeitungszeit bewältigbar (Richtwert 2,5–3,0 min/BE, vertretbar 2,0–3,5; EPA-Beispiel IW: 300 min / 120 BE = 2,5) | R+I |
| 4.4 | Arbeitsauftrag mit EPA-Operator im Imperativ („Sie") | R |
| 4.5 | nur EPA-Operatoren – oder erweiterte Operatoren im LM dokumentiert; praktische Operatoren für PC-, CAD- und Simulationsarbeit (*erstellen, speichern, anpassen, vervollständigen*) als Hinweis | R |
| 4.6 | AFB-Verteilung ca. 30/40/30 % (±10 %) | R |
| 4.7 | BE bei jeder (Teil-)Aufgabe ausgewiesen | R |

## X. Zusatzkriterien (häufige Mängel)
| Nr. | Kriterium | Art |
|---|---|---|
| X.1 | erste Teilaufgabe nicht im AFB III | R |
| X.2 | erweiterte Operatoren im LM mit AFB dokumentiert | R+I |
| X.3 | „BE" statt „Punkte" | R |
| X.4 | Operatoren in SM und EWH identisch | I |
| X.5 | AFB-Zuordnungen im EWH passen zur Operatorentabelle | I (Tabelle aus dem Skript nutzen) |
| X.6 | Kopfzeile enthält den Schwerpunkt | I |
| X.7 | Verhältnis BE/Bearbeitungszeit plausibel | R |
| X.8 | EWH operatorenbezogen formuliert | I |
| X.9 | Nicht-EPA-Formulierungen markiert/ersetzt | R |
| X.10 | BE-Verteilung je Teilaufgabe nachvollziehbar, Summen stimmig | R |
| X.11 | keine Textwiederholungen/Tippfehler | I |
| X.12 | digitales Material beigelegt, sofern vorausgesetzt | I (+R Dateiliste) |
| X.13 | Gesamt-BE SM = Gesamt-BE EWH (auch je Aufgabe) | R |
| X.14 | Aufgaben verbinden Inhalte aus ≥ 2 Lerngebieten | I |

## S. Schülersicherheit (Pflicht vor Ausgabe)
| Nr. | Kriterium | Art |
|---|---|---|
| S.1 | keine offenen Platzhalter (XXX, 20__, „(unvollständig)", TODO, „Version X.Y", Pfad-Dummies) | R |
| S.2 | jede angekündigte Anlage/Vorlage/Abbildung/Schaltbild/Datenblatt ist vorhanden | R+I (Bildinhalt nur von Hand) |
| S.3 | jede referenzierte Datei liegt den Prüfungsunterlagen bei | R (Liste) + I |
| S.4 | Nummerierung lückenlos, ohne Doppelung | R |

**Validitätsregel:** Kann ein S-Kriterium aus dem Material nicht entschieden werden (Bilder
nicht eingebettet, Prüfungsunterlagen nicht einsehbar), Status ➖ mit Benennung der fehlenden
Information. Niemals raten.

## Lerngebiete und Schwerpunkt-Besonderheiten
- Lerngebiete aller Schwerpunkte mit verbindlich/optional: `berufliches-gymnasium.md`, Abschn. 3.
- **Ingenieurwissenschaften:** Aufgaben verbinden Bau-, Maschinenbau- und Elektrotechnik
  (EPA-Beispiel: drei Aufgaben je 40 BE). Hilfsmittel können PC-Software sein (CAD,
  Tabellenkalkulation, SPS-Entwicklungsumgebung). Dann ist die Abgabe der Dateien zu regeln (X.12).

## Befundregeln
- Beanstandung nennt Aufgabe/Teilaufgabe und enthält ein **wörtliches Zitat** aus SM oder LM.
- Konfidenz < 75 % → als **Hinweis** (⚠), nicht als Beanstandung (❌).
- Im Zweifel keine Beanstandung: lieber übersehen als Fehlalarm.
- Kein Operator deckt mehr als zwei aufeinanderfolgende AFB ab.
- Begründung und Status dürfen sich nie widersprechen.

## Empfehlungsstufen (genau eine wählen und begründen)
1. **Annahme ohne Auflagen**
2. **Annahme mit Überarbeitungsauflagen** (Auflagen = ❌-Befunde)
3. **Annahme nur nach Behebung der Schülersicherheits-Mängel** – Pflicht, sobald S.1–S.4 ein ❌
   tragen; in dieser Form nicht zur Bearbeitung freigegeben
4. **Ablehnung** – nur bei gravierenden strukturellen Mängeln (2.4, 2.5, 2.6, 4.6)
