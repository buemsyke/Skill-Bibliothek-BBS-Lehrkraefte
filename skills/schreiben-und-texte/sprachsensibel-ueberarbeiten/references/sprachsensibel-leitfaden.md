# Leitfaden: Sprachliche Hürden erkennen und abbauen

Grundlagen: J. Leisen (sprachsensibler Fachunterricht, Methoden-Werkzeuge, Darstellungsformen),
P. Gibbons (Scaffolding), Makro-/Mikro-Scaffolding (Kniffka). Sprachebenen: Alltagssprache →
Bildungssprache → Fachsprache. Ziel ist der Weg zur Fachsprache, nicht ihre Vermeidung. In
Beratung, Übergabe und Einweisung von Laien kommt die Gegenrichtung als berufliche Kompetenz
hinzu: Fachsprache → Kundensprache (Abschn. 7).

## Inhalt
1. Wortebene
2. Satzebene
3. Textebene
4. Aufgabenebene
5. Darstellungsformen wechseln
6. Lesbarkeit messen und einordnen
7. Fachsprache für Laien übersetzen (Kundensprache)
8. Grenzen

---

## 1. Wortebene

| Hürde | Vorher | Nachher |
|---|---|---|
| Fachbegriff ohne Einführung | Prüfen Sie die Gurtspannung. | Prüfen Sie die **Gurtspannung** (= wie straff der Gurt gespannt ist). |
| lange Komposita | Gurtspannstationseinstellung | Einstellung an der Spannstation des Gurtes · bei Einführung gliedern: Gurt·spann·station |
| Nominalisierung | Nach erfolgter Durchführung der Schmierung … | Nachdem Sie geschmiert haben, … |
| Funktionsverbgefüge | Die Maschine ist zum Stillstand zu bringen. | Schalten Sie die Maschine aus. |
| Abkürzungen | lt. BA ggf. n. i. O. melden | laut Betriebsanleitung; wenn nötig „nicht in Ordnung" melden |
| Synonymwechsel | Gurt … Band … Förderriemen | **einen** Begriff durchhalten |
| bildliche Wendungen | Das ist das A und O. | Das ist am wichtigsten. |

Fachwörter immer **mit Artikel und Plural** einführen: *die Spannstation, die Spannstationen*.
Typische Verbindungen mitlernen: *den Gurt spannen, die Spannung prüfen, den Schmierstoff
auftragen*.

## 2. Satzebene

Die Grenze von 20 Wörtern (`lesbarkeit.py`) ist bewusst strenger als der allgemeine Richtwert für
Material für Lernende (keiner über 25 Wörter, `schuelermaterial.md`): Die sprachsensible Fassung
soll unter beiden bleiben.

| Hürde | Vorher | Nachher |
|---|---|---|
| Satzlänge > 20 Wörter, Schachtelsatz | Bevor Sie mit der Wartung, die laut Herstellerangabe alle 500 Betriebsstunden durchzuführen ist, beginnen, sichern Sie … | Die Wartung ist alle 500 Betriebsstunden fällig. Sichern Sie die Anlage, bevor Sie beginnen. |
| Partizipialattribut | die vom Hersteller vorgeschriebene, regelmäßig durchzuführende Schmierung | die Schmierung. Der Hersteller schreibt sie vor. Sie muss regelmäßig erfolgen. |
| unpersönliches Passiv | Es ist zu prüfen, ob … | Prüfen Sie, ob … |
| Negationshäufung | Nicht ohne vorherige Sicherung beginnen. | Sichern Sie zuerst die Anlage. Beginnen Sie dann. |
| Konjunktiv/Modal unklar | Man sollte ggf. … | Wenn …, dann … |

Fachtextpassiv („Die Lager werden gefettet.") gehört zur Berufssprache: im Infotext
bewusst verwenden und im Wortspeicher als Muster zeigen – in Arbeitsaufträgen aktiv formulieren.

## 3. Textebene
- Überschrift als Frage oder Handlung; Kernaussage vorweg (2 Sätze).
- Ein Absatz = ein Gedanke; Zwischenüberschriften alle 3–5 Sätze.
- Reihenfolge im Text = Reihenfolge der Handlung.
- Signalwörter für Zusammenhänge: *zuerst, danach, deshalb, weil, im Unterschied zu*.
- Wichtiges als Liste oder Tabelle; Abbildung neben der zugehörigen Stelle.

## 4. Aufgabenebene
- **Operator** an den Satzanfang und fett: „**Erstellen** Sie …".
- Eine Handlung pro Satz; Teilaufgaben nummerieren – höchstens drei. Den Auftrag dabei nicht
  in Einzelschritte zerlegen: Ziel und Ergebnis bleiben ein Auftrag, Schritte gehören in die
  gestuften Hilfen (`schuelermaterial.md` Abschn. 3).
- Ergebnisform nennen: „… in die Tabelle", „… in 3 Sätzen", „… als Skizze".
- Keine versteckten Doppelaufträge („Nennen und begründen Sie …" → zwei Teilaufgaben, wenn
  beides bewertet wird).
- Bei Erstbegegnung mit einem Operator: Operatorkarte mit Beispiel bereitstellen.

## 5. Darstellungsformen wechseln (Leisen)
Bild ↔ Text ↔ Tabelle ↔ Diagramm ↔ Symbol/Formel ↔ gegenständliche Handlung. Ein Fließtext
über Schmierstoffe wird als Vergleichstabelle oft verständlicher; ein Ablauf als nummerierte
Bildfolge. Der Wechsel zurück (Tabelle → eigener Text) ist selbst eine sprachliche Übung.

## 6. Lesbarkeit messen und einordnen
`scripts/lesbarkeit.py` liefert u. a. den **Lesbarkeitsindex LIX** (Björnsson):
LIX = durchschnittliche Satzlänge in Wörtern + Anteil langer Wörter (mehr als 6 Buchstaben)
in Prozent.

| LIX | Einordnung (Richtwerte für deutsche Texte) |
|---|---|
| unter 40 | leicht |
| 40–50 | mittel |
| 50–60 | schwer (typische Sachtexte) |
| über 60 | sehr schwer (Fachliteratur) |

Fachtexte haben wegen langer Fachwörter immer einen erhöhten LIX. Aussagekräftiger ist die
**Veränderung** vorher/nachher und die **Liste langer Sätze**. Zahlen ersetzen nicht das Lesen.

## 7. Fachsprache für Laien übersetzen (Kundensprache)

Wo Lernende Kundschaft beraten, Anlagen übergeben oder Betreiber einweisen, müssen sie ihr
Fachwissen **ohne Fachjargon** erklären – eine eigene sprachliche Leistung, die geübt werden
will. Sie ersetzt die Fachsprache nicht: Im schriftlichen Bericht und im Fachgespräch bleibt der
Fachbegriff.

| Regel | Fachsprache | Kundensprache |
|---|---|---|
| Bild oder Vergleich statt Fachbegriff | Die Tragrolle ist festgegangen. | Eine der kleinen Rollen, auf denen das Band läuft, dreht sich nicht mehr. |
| Wirkung statt Funktionsprinzip | Ungleiche Spannung führt zu Schieflauf. | Das Band ist auf einer Seite lockerer und wandert deshalb zur Seite. |
| Zahl mit Bezug und Handlung | Prüfintervall 500 Bh | Alle sechs bis sieben Wochen schauen wir wieder nach. |
| Handlungsanweisung statt Norm | gemäß Betriebsanleitung Abschn. 7.2 | Bitte schalten Sie das Band aus, bevor Sie etwas daran anfassen. |
| Einwand ernst nehmen, dann Folge zeigen | – | Ich verstehe, dass es schnell gehen soll. Wenn wir nur nachspannen, läuft das Band in ein paar Tagen wieder schief. |

- **Nicht falsch vereinfachen:** Die Erklärung darf einfacher sein, aber nicht falsch.
- **Wortspeicher mit dritter Spalte** „So sage ich es der Kundin / dem Kunden"
  (`sprachhilfen.md` Abschn. 1); Redemittel für Einwände, Kosten und Einweisung
  (`sprachhilfen.md` Abschn. 4).
- Bewertungskriterium im Gespräch: „richtig und ohne Fachjargon erklärt".

## 8. Grenzen
- Leichte Sprache ist ein eigenes Regelwerk für bestimmte Zielgruppen – nur auf Wunsch.
- Prüfungsaufgaben der Kammern werden nicht vereinfacht; stattdessen Prüfungssprache üben.
- Übersetzungen in Herkunftssprachen können als zusätzliche Brücke dienen (Glossar
  zweisprachig), ersetzen aber nicht die deutsche Fachsprache. 🔎 Übersetzungen prüfen lassen.
