# Lektionsmuster – Schülerseite im Kursprojekt

Gemeinsame Referenz für `unterrichtsmaterial-erstellen`, `schuelerseiten-veroeffentlichen`,
`lernsituation-dokumentieren` und `unterricht-entwickeln`. Beschreibt, wie **Lektionen**
(`lessons/NN_slug/lesson.md`, je 90 min) die vollständige Handlung einer **Lernsituation** für
Lernende umsetzen – zum **Neuerstellen** und zum **Überarbeiten** vorhandener Lektionen.
Vorlage: `vorlage-lektion.md`, falls vorhanden; Prüfung: `scripts/lektion_pruefen.py`.

Herkunft: Kursprojekt Berufliches Gymnasium, Informatik Q3 (25 Lektionen, 2026), dort aus der
Rückmeldung der Lernenden („zu viel Text“, „zeitlich zu umfangreich“) und einer Prüfung nach
SchuCu-BBS 2024 entstanden. Stand 1.16: Der Handlungskreis wird **je Lernsituation** geschlossen,
nicht je Lektion.
⚠️ Das Muster ist als Ganzes noch nicht mit Lernenden erprobt – Rückmeldungen hier nachtragen.

## Inhalt
1. Lektion und Lernsituation
2. Aufbau (H1-Überschriften)
3. Elemente je Phase
4. Was nur in den Lehrerteil gehört
5. Kurz halten und Zeit ehrlich planen
6. Bestehende Lektionen überarbeiten
7. Prüfen

## 1. Lektion und Lernsituation

Die Lernsituation (Skill `lernsituation-dokumentieren`) ist die curriculare Planung für das
Bildungsgangteam; die Lektion ist das, was Lernende in der Hand haben. **Eine Lernsituation
umfasst eine oder mehrere Lektionen.** Der Handlungskreis wird je Lernsituation geschlossen;
eine einzelne Lektion muss nicht alle sechs Phasen enthalten. Eine Lernsituation aus nur einer
Lektion trägt alles selbst (so ist die Vorlage gebaut).

Bei mehreren Lektionen steht im Kopf `lernsituation: "<Kurzname>"` und `teil: "k/n"`. Ist
`lernsituation` gesetzt, ist `teil` Pflicht; `lernsituation: keine` gilt für Zusatzeinheiten wie
Kompaktstunden oder Klausurvorbereitung. Rollen der Lektionen:

| Rolle | Phasen (SchuCu-BBS 2024) | typische Bausteine |
|---|---|---|
| **Auftakt** (erste Lektion) | Informieren bzw. Analysieren · Planen · Entscheiden | *Vor dem Start*, Handlungssituation, Bewertungs- und KI-Kasten, Eingangsfrage mit Vorhersage, Planen, Entscheiden |
| **Erarbeitung** (mittlere Lektionen) | Durchführen (mit fachsystematischer Phase) | Input mit Lösungsbeispiel, größere Aufträge, Hilfen mit Stolpersteinen, Sicherung |
| **Abschluss** (letzte Lektion) | Überprüfen bzw. Kontrollieren · Reflektieren | Realitätstest, Rückmeldung mit Überarbeitung, Festhalten, Lernweg |

**Einmal je Lernsituation** (Auftakt bzw. Abschluss; in den übrigen Lektionen nur ein Verweis):
Handlungssituation, *Vor dem Start* und *Lernweg* (ein Selbsteinschätzungspaar), Kasten *So wird
bewertet*, Kasten *KI-Werkzeuge*, Phase Entscheiden, Realitätstest, Rückmeldung mit
Überarbeitung. **Je Lektion:** Problem bzw. Vorhersage, Fachwissen oder Input, Aufträge,
Stolpersteine, Sicherung und die Sollbruchstelle („Endet die Lektion hier, beginnt die nächste
mit …“; `lernsituationsmuster.md` Abschn. 7, falls vorhanden).

Zuordnung der Elemente zu den Phasen (Richtwerte für die Aufgaben einer Ein-Lektionen-Lernsituation):

| Phase (SchuCu-BBS 2024) | Element | Aufgaben (Richtwert) |
|---|---|---|
| Informieren bzw. Analysieren | *Vor dem Start*, Eingangsfrage mit Vorhersage, Zugang zum Fachwissen, Abgleich | – |
| Planen | Lernende planen selbst (Zerlegen, Entwerfen) | 1–2 |
| Entscheiden | Matrix mit eigenem Kriterium, Entscheidungsprotokoll – **nur bei echter Entscheidung** | 3–4 |
| Durchführen | größere Aufträge, Hilfen mit Stolperstein-Tabelle | 5–7 |
| Überprüfen bzw. Kontrollieren | Realitätstest, Rückmeldung mit Überarbeitung | 8–9 |
| Reflektieren | Festhalten (Transfer), eigener Lernweg | 10–11 |

Was in der Lernsituation als Kompetenz steht, muss in der Lektion als Auftrag vorkommen
(Rückwärtsprobe, `curriculum-abgleich.md` Abschn. 7, falls vorhanden).

## 2. Aufbau (H1-Überschriften)

Die H1-Überschriften sind fest, weil `edu-seiten split` sie über `phase_config.yaml` den
LMS-Phasen zuordnet – eine abweichende H1 fällt **still** aus der Schülerausgabe:

`Voraussetzungen und Kompetenzen` · `Fachwissen` · `Handlungssituation` · `Material` ·
`Hilfestellungen` · `Vertiefungen` · `Kompetenzcheck` · `Aufgaben zur Wiederholung und Übung` ·
`Lösungen / Handlungsergebnisse` · `Didaktische Hinweise`

Arbeitsaufträge stehen unter `Handlungssituation` als `## Arbeitsaufträge` mit
`### Phase N – Name (Sozialform, ca. X min)`.

## 3. Elemente je Phase

**Vor dem Start** (unter *Kompetenzen*, 1 min, in der Auftakt-Lektion): Lernende markieren jede
Kompetenz der Lernsituation mit ✔ / ~ / ✘. Am Ende der Lernsituation vergleichen sie damit
(Lernweg).

**Eingangsfrage mit Vorhersage** (Anfang *Fachwissen*, 3 min): ein kleiner Fall, dessen
Ergebnis die typische Fehlvorstellung der Lektion sichtbar macht. Lernende **sagen vorher**,
bevor sie lesen oder ausführen. Der Kasten **Abgleich** am Ende des Fachwissens löst auf.
Vorhersagen vor dem Ausführen gilt auch in Aufträgen: erst notieren, dann ausprobieren.

**Zugang zum Fachwissen:** Standard ist **ein** Zugang – bei neuem Verfahren oder neuer Syntax
oft ein kurzer **Lehrkraftinput mit Lösungsbeispiel** (10–15 min, im Distanzunterricht ein
Screencast; `lernsituationsmuster.md` Abschn. 12, falls vorhanden) statt langer Lektüre.
Mehrere gleichwertige Zugänge (Ausprobieren, Lesen, Fachbuch) sind nur sinnvoll, wenn
**eine** Wahl genügt und die Zeit dafür (20–30 min) in der Zeitplanung steht; ein Zugang, der
mit „danach … lesen“ endet, ist kein Zugang, sondern Mehrarbeit. Wahlmöglichkeiten (M3/M16)
entstehen besser über Hilfen, Aufgabenauswahl und Vertiefung als über Lesewege.
**Fachwissen und Hilfen enthalten nicht den Lösungscode der eigenen Aufgabe:** Das
Lösungsbeispiel zeigt einen analogen Fall. Sonst wird Durchführen zum Abschreiben, und Lesen
und Aufgabe doppeln sich.

**So wird bewertet – vor dem Start lesen** (direkt unter `## Arbeitsaufträge`, einmal je
Lernsituation): Abgabe, Kriterien mit Punkten, Summe. Gröbere Fassung des Feinrasters im
Lehrerteil mit **gleicher Summe**; die verdeckte Schwierigkeit wird hier nicht verraten.
Satz: *Bewertet wird nicht, welche Variante ihr wählt, sondern wie ihr sie begründet und
überprüft. Dein Lernweg wird nicht benotet.*

**KI-Werkzeuge in dieser Lektion** (ebenfalls vor der ersten Aufgabe): KI-Einsatz **je Phase**
mit den drei Zeichen – 🚫 Ohne KI (Vorhersagen, Entscheidung, Überprüfung, Lernweg,
Leistungsnachweise) · 💡 KI zum Verstehen · 🔧 Mit KI arbeiten (nur gekennzeichnet, nur, was
man erklären kann) – und **ein Satz Begründung** für jede Phase ohne KI. Dasselbe Zeichen steht
**am Arbeitsschritt**, vor dem Operator; wie KI genutzt werden darf, steht im Auftrag.
Weiterführende Regeln auf einer Regelseite des Kurses (fünf Regeln: erst selbst, prüfen statt
glauben, kennzeichnen, erklären können, Daten schützen); in Folgelektionen genügt ein Verweis.
Drei Ebenen, Voreinstellung je Phase, Begründungen und Prüffragen: `ki-vereinbarungen.md`, falls vorhanden.

**Planen** (Aufgaben 1–2): Lernende zerlegen und entwerfen selbst. Nicht kleinschrittig
vorgeben – ein Auftrag mit Operator und Ergebnisform statt zehn Lückenschritte. Beantwortet das
Fachwissen die Planungsaufgabe schon, ist es keine Planung, sondern Kontrolle des Gelesenen.

**Entscheiden** (Aufgaben 3–4; `lernsituationsmuster.md` Abschn. 2, falls vorhanden): **nur an
einer echten Entscheidungsstelle** der Lernsituation. Die Auftraggeberin stellt **zwei
vertretbare Varianten** A und B vor, die nicht beide gebaut werden müssen. Lernende bewerten
sie in einer Matrix (1–3 Punkte) und **ergänzen ein eigenes Kriterium**; dann halten sie die
Entscheidung fest: *Kontext · Gewählt · Verworfen, weil … · Ausschlag gab · Konsequenz*.
Lehrkraft zurückhaltend. Kleine Wahlen (Schreibweise, Parameter, Werkzeug) werden mit einem
Satz notiert – *gewählt, weil …, verworfen: …* –, nicht mit Matrix und Protokoll. Legt die
Ausstattung die Wahl fest (z. B. nur ein Werkzeug ist installierbar), setzt die Lehrkraft sie
fest, statt eine Scheinentscheidung zu inszenieren.

**Durchführen** (Aufgaben 5–7): wenige, größere Aufträge. Mindestens eine **verdeckte
Schwierigkeit** je Lernsituation – eine Stelle, an der ein naheliegender Weg scheitert, ohne
dass der Auftrag darauf hinweist. Sie steht nur in den Didaktischen Hinweisen (Ort, Symptom,
wo nachgefragt wird). Vorher ggf. eine **fachsystematische Phase** (Input mit Lösungsbeispiel).

**Stolperstein-Tabelle** (in *Hilfestellungen*; `lernsituationsmuster.md` Abschn. 5, falls vorhanden):

| Das beobachtest du | Das steckt dahinter | So gehst du vor |
|---|---|---|
| Symptom (Meldung, falsches Ergebnis) | Ursache | konkrete Abhilfe |

Gehört eine Entscheidung zur Lernsituation, kommt die Zeile dazu: *In der Matrix bekommt eine
Variante überall 3 Punkte* → *die Entscheidung stand schon fest* → *ein Kriterium suchen, bei
dem die andere gewinnt*. Daneben gestufte Hilfen (Orientierung → Werkzeug → eingeklapptes
Gerüst, entspricht Impuls → Strategie → Teilschritt in `schuelermaterial.md`); das Gerüst lässt die
Kernidee zu ergänzen übrig.

**Realitätstest** (Aufgabe 8, Abschluss): zwei konkrete Fälle, **(a)** trifft Variante A,
**(b)** trifft Variante B. Lernende gleichen mit ihrer Matrix ab – die Entscheidung wird
überprüft, nicht nur das Produkt. Ohne echte Entscheidung: das Handlungsergebnis an zwei
konkreten Fällen prüfen.

**Rückmeldung** (Aufgabe 9, Abschluss; `lernsituationsmuster.md` Abschn. 3, falls vorhanden):
mit einem Team, das **anders** entschieden hat – wo das möglich ist; sonst mit einem beliebigen
Team – **zwei Stärken und ein nächster Schritt**, danach **überarbeiten**.

**Festhalten** (Aufgabe 10): Transfer – was gilt über diesen Fall hinaus?

**Dein Lernweg** (Aufgabe 11, Abschluss, allein, 3 min, unbenotet): Vergleich mit den
Markierungen vom Anfang; wo festgesteckt, was hat geholfen; **ein nächster Schritt**.

**Vertiefungen** sind ein **Zusatz außerhalb des Kernwegs**: „Wer fertig ist, wählt eine“
(weiterführen, recherchieren, vorgreifen). Sie stehen in keiner Pflichtzeit.

## 4. Was nur in den Lehrerteil gehört

Unter `# Lösungen / Handlungsergebnisse` und `# Didaktische Hinweise` (bzw. in `solutions/`):
Feinraster mit Erwartungshorizont, verdeckte Schwierigkeit, Begründung der Varianten (welche
Zahl im Realitätstest trifft welche Variante), Rolle der Lehrkraft je Phase, Zeitplanung,
Differenzierung, typische Fehler, Querverbindungen. Für die Didaktischen Hinweise feste
Spiegelstriche verwenden – `**Rolle**`, `**Verdeckte Schwierigkeit (nicht ankündigen)**`,
`**Zeitplanung**`, `**Kernweg**`, `**Fachsystematische Phase**`, `**Differenzierung**`,
`**Querverbindung**` –, dann lassen sie sich automatisch in die Dokumentation der
Lernsituation übernehmen. Beispieldateien, die eine Aufgabe lösen, gehören nicht in die
Schülerausgabe (`copy_dirs`).

## 5. Kurz halten und Zeit ehrlich planen

Lernende empfinden lange Lektionen als Hürde, und was nicht in der Zeitplanung steht, geht
über die Zeit. Regeln:

- **Kernweg:** Das, was alle in der Lektion schaffen müssen, passt in **60–65 min je 90 min**
  (im Skill `unterrichtsentwurf-erstellen`, `methodenrepertoire.md` Abschn. 3).
  Alles darüber ist Zusatz. Die Minuten des Kernwegs stehen in den Didaktischen Hinweisen.
- **Zeitplanung vollständig:** Input, Lesen, Aufbau, Übergänge und Sicherung sind
  eingerechnet; die Summe ergibt die Dauer der Lektion. Zeiten für Zugang und Aufbau, die
  „nebenbei“ anfallen, gehören hinein. Eine Planung, die nur die Aufträge zählt, geht nicht auf.
- **Länge des Schülerteils** (alles außer Lösungen und Didaktischen Hinweisen): **höchstens
  rund 1 500 Wörter ohne Code**, Codezeilen werden getrennt gezählt (Richtwert; Vorbild ist
  eine Kompaktstunde mit Syntaxkarten und Live-Coding). Mittel: Problem zuerst, ein Beispiel
  statt drei, Darstellung statt Absatz (Skizze, Diagramm, Tabelle), Details in eingeklappte
  Kästen, Wiederholungen streichen, Boilerplate je Lernsituation nur einmal.
- **Offen, anschaulich, ohne Dekoration:** Aufträge nennen Ziel und Ergebnis statt
  Einzelschritte (Schritte in die Hilfen); Fachwissen und Aufträge arbeiten mit Darstellungen;
  keine Emojis außer den KI-Zeichen, keine Floskeln oder Ankündigungen
  (`schuelermaterial.md`, falls vorhanden).
- **Selbsteinschätzung** einmal je Lernsituation (*Vor dem Start* und *Lernweg*); nicht noch
  Ich-kann-Liste, Kompetenzraster und Arbeitsblatt-Selbstcheck in jeder Lektion.
- **Übungen** (H5P, Wiederholungsaufgaben) sind Festigung außerhalb des Kernwegs.

## 6. Bestehende Lektionen überarbeiten

Reihenfolge, die sich bewährt hat:
1. `lektion_pruefen.py` laufen lassen – Ist-Stand je Element, Wortzahl, Zeitplanung.
2. **Zuschnitt prüfen:** Gehören aufeinanderfolgende Lektionen zu *einer* Handlungssituation und
   *einem* Handlungsergebnis? Dann als eine Lernsituation führen (Kopf `lernsituation`, `teil`).
   Ein neuer Zuschnitt ändert das schulische Curriculum und braucht den **Bildungsgangbeschluss**
   (`schucu-bbs-2024.md` Abschn. 6, falls vorhanden); Kompetenzcodes und Lernsituations-
   dokumente neu prüfen.
3. **Bündeln:** Bewertungs- und KI-Kasten, *Vor dem Start*, Entscheiden, Realitätstest,
   Rückmeldung mit Überarbeitung und Lernweg je Lernsituation einmal; Aufgabennummern neu zählen
   und **alle** Verweise (Lösung, Arbeitsblatt, Beispieldateien, Didaktik) mitziehen.
4. **Entscheiden nur an echter Stelle** (Abschn. 3).
5. **Doppeltes streichen:** Fachwissen, Hilfen und Arbeitsblatt dürfen sich nicht
   wiederholen; Lösungscode aus Fachwissen und Hilfen nehmen (analoges Lösungsbeispiel).
6. **Fachsystematische Phase** einsetzen, wo Selbststudium teuer ist
   (`lernsituationsmuster.md` Abschn. 12, falls vorhanden): Begründung in den Didaktischen
   Hinweisen.
7. **Kernweg und Zeitplanung** rechnen; Vertiefungen und Übungen als Zusatz kennzeichnen.
8. Wortzahl vorher und nachher festhalten.
9. Verdeckte Schwierigkeit ergänzen und nur in den Didaktischen Hinweisen beschreiben.
10. Schülerausgabe neu erzeugen und mit `ausgabe_pruefen.py` prüfen: Es darf nichts aus dem
    Lehrerteil und keine Musterlösung (auch nicht in Beispieldateien) in der Ausgabe stehen.

## 7. Prüfen

`python3 scripts/lektion_pruefen.py lessons/*/lesson.md [--max-woerter 1500] [--json]` meldet
je Lektion, welche Elemente erkennbar sind, ob die Bewertungssumme aufgeht, ob die Phasenzeiten
und der Zugang zur Dauer passen, wie lang der Schülerteil ist (Code getrennt), ob ein Kernweg
ausgewiesen ist und ob eine Lehrkraftinput-Phase begründet und kurz genug ist
(Auftragslänge, Kleinschrittigkeit, Darstellungen und Dekoration prüft
`schuelermaterial_pruefen.py`, falls vorhanden). Tragen mehrere
Lektionen dieselbe `lernsituation`, prüft das Skript zusätzlich je Lernsituation, ob der
Handlungskreis geschlossen ist (Entscheiden, Überprüfen, Reflektieren irgendwo in der
Lernsituation). „Nicht gefunden“ heißt „von Hand nachsehen“ – das Skript sucht nach
Signalwörtern und ersetzt keine fachliche Durchsicht.
