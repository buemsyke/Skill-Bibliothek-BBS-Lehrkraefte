# Agiler Lernprozess mit KI

Grundlage: Röttger, N.: *Agil und strukturiert – eine Umgebung für KI-gestütztes Lernen*,
heise Developer, 10.10.2026 (Testende, die sich in fremde Fachdomänen einarbeiten). Hier
übertragen auf Lehrkräfte und Lernende an berufsbildenden Schulen.

## 1. Der Ablauf

Kickoff → Lernsprint → Review → *Ziel erreicht?* – **ja:** nächster Sprint … → Retro → Ablage;
**nein:** zurück zum Lernsprint (noch eine Runde zum selben Thema). Als Abbildung für Lernende:
Ablaufdiagramm mit `fachdiagramm-erstellen` (Bauart `flow`, Rückführung `route: unten`).

| Schritt | wer | Frage | Dauer |
|---|---|---|---|
| Kickoff | Lernende + KI, danach Fachexpertin | Was muss ich bis wann können? Wie komme ich dahin? | 30–60 min |
| Lernsprint | Lernende + KI | Stoff des Sprints erarbeiten, üben, Zettel schreiben | Lernzeit je Sprint |
| Review | Lernende + KI, bei holprigem Sprint + Fachexpertin | Ist das Sprintziel erreicht? | 10–20 min |
| Retro | Lernende (+ Fachexpertin) | Was hat getragen, was nicht? Was ändert der nächste Zyklus? | ca. 20 min |
| Ablage | Lernende (+ Ermöglicher) | Wo finden andere das Ergebnis? | – |

Bezug zur vollständigen Handlung (SchuCu-BBS): Kickoff = Informieren, Planen, Entscheiden ·
Sprint = Durchführen · Review = Überprüfen bzw. Kontrollieren · Retro = Reflektieren. Ein agiler Lernpfad ist
damit selbst eine vollständige Handlung – gut geeignet, um Selbständigkeit (Personale
Kompetenz) gezielt zu fördern.

## 2. Die sechs Kickoff-Fragen

| Nr. | Frage | gut | zu beliebig bzw. Falle |
|---|---|---|---|
| 1 | **Ziel** – Was muss ich am Ende können, woran merke ich es? | „Ich kann Störmeldungen der Anlage X den Ursachen zuordnen und die Prüfschritte begründen – nachweisbar an drei Fallkarten." | „Ich will Wärmepumpen besser verstehen." |
| 2 | **Zeithorizont** – Bis wann? | fester Termin (Prüfung, Halbjahresbeginn, Projektstart) | „irgendwann im Schuljahr" |
| 3 | **Sprint** – Wie lang, wie viel Lernzeit je Sprint? | 1 Woche (Standard), 2 Wochen bei schwer portionierbarem Stoff; z. B. 2 h je Sprint | 8 h am Stück statt 8 × 1 h |
| 4 | **Ort und Zeitpunkt** – Wo und wann lerne ich? | „Di 7:15–8:00 im Fachraum, Do im Zug"; feste Termine oder nach Bedarf | „wenn Zeit ist" |
| 5 | **Lernform** – angeleitet, selbst mit KI oder gemischt? | früh entscheiden, prägt den Zuschnitt der Sprints | Kurs und KI-Lernpfad doppelt planen |
| 6 | **Ressourcen** – Welche Quellen, welche Menschen? | Handbuch, Fachbuch, Video, Kollegin, Ausbilder | „das Internet" |

**Zeitrechnung:** Lernstunden addieren sich nicht wie auf einem Konto. Acht Wochen mit je
einer Stunde sind kein Achtstundentag – und das ist ein Vorteil: In den Pausen arbeitet der
Kopf weiter, der Stoff sitzt danach fester (verteiltes Lernen). Sprintanzahl =
Zeithorizont ÷ Sprintlänge; ein Puffersprint für Wiederholungsrunden ist sinnvoll.

## 3. Rollen

| Rolle | Aufgabe | in der Schule typischerweise |
|---|---|---|
| **Lernende** | steuert den Lernpfad, kennt den eigenen Bedarf, verantwortet, dass das Gelernte sitzt | Lehrkraft selbst; Auszubildende, Fachschülerinnen und Fachschüler |
| **KI als Lernarchitektin** | strukturiert den Stoff, erklärt Zusammenhänge, schlägt Quellen und Übungen vor | Claude, AIS.chat-Lernszenario *Kickoff* |
| **KI als Lernbegleiterin** | stellt Rückfragen, prüft das Verständnis, auch mit sokratischen Fragen | Claude, AIS.chat-Lernszenario *Lernsprint* |
| **Fachexpertin / Fachexperte** | checkt den Lernpfad zu Beginn gegen, bleibt ansprechbar, wenn etwas nicht stimmt | Kollegin mit Erfahrung, Fachberatung, Ausbilderin; für Lernende die Lehrkraft |
| **Ermöglicher** (optional) | ermöglicht Lernzeit, gleicht Ziele mit der Realität ab, schafft Anwendungsgelegenheiten | Schulleitung, Bildungsgangleitung; für Auszubildende der Ausbildungsbetrieb |

Die Fachexpertin wird gern übersprungen („wir haben ja die KI"). Beim Lernen mit KI ist sie
die wichtigste Rolle. Ohne Ermöglicher fehlt oft die Anwendungsgelegenheit, die aus Wissen
Können macht – bei Auszubildenden deshalb den Betrieb einbeziehen (Lernortkooperation).

## 4. Drei Sicherungen gegen KI-Irrtümer

| Sicherung | fängt ab | so umgesetzt |
|---|---|---|
| **Was** – gemeinsamer Lernpfad | falsche Schwerpunkte, Lücken, falsches Niveau | Lernpfad im Dialog KI–Lernende, dann Review durch die Fachexpertin (`Freigabe Lernpfad`) |
| **Woher** – gebundene Quellen | erfundene Fakten, Begriffe, Werte | KI erklärt aus den Quellen der Lernakte und nennt die Fundstelle; nur öffentliches bzw. freigegebenes Material |
| **Mensch** – grundsätzliche Skepsis | alles, was durchrutscht | Fundstelle verlangen, Seite nennen lassen, nachschlagen; Auffälliges zur Fachexpertin |

### Skepsis-Routine (für jede Sitzung)
1. Klingt eine Aussage neu oder überraschend: **Fundstelle verlangen** (Datei, Seite, Abschnitt).
2. **Nachschlagen.** Steht es dort? Wenn nein: in der Lernakte als „nicht belegt" markieren.
3. **Gegenprobe:** „Eine andere Quelle sagt etwas anderes – stimmt deine Antwort?" bringt
   Bewegung in die Antwort, ist aber **keine** Garantie.
4. Findet sich nichts Klärendes: **Fachexpertin fragen** (Abschnitt *Offene Fragen*).
5. Nur Belegtes wandert in die Zettel.

Beispiel aus dem Artikel: Die KI nennt neben Quell- und Zirruswolken flüssig auch
„Zitruswolken". Klingt plausibel – gibt es aber nicht. Wer nach der Fundstelle fragt und
nachschlägt, merkt es; wer übernimmt, wiederholt den Fehler später im Ernstfall. Am
schnellsten kommt voran, wer der KI kein Wort ungeprüft glaubt.

## 5. Lernsprint

- **Sprintziel** mit Operator, **Lernzeit**, **Quellen mit Fundstelle**, **Lernaktivitäten**,
  **Nachweis** im Review.
- Lernaktivitäten, die das Behalten fördern: Erklären in eigenen Worten · Zettel schreiben
  (eine Kernaussage, eine Fundstelle) · eigenes Beispiel aus Betrieb oder Unterricht finden ·
  Aufgabe lösen mit gestuften Hilfen · Fehler in einer vorgelegten Aussage finden ·
  Begriffe abgrenzen.
- **Sokratische Fragetypen** für die Lernbegleiterin: Klärung („Was meinst du mit …?") ·
  Begründung („Woran erkennst du das?") · Annahmen („Was setzt du dabei voraus?") · Folgen
  („Was passiert, wenn …?") · Gegenbeispiel („Gilt das auch bei …?") · Transfer („Wo begegnet
  dir das im Betrieb?").
- Kosten und Modellwahl (Claude): den Lernpfad (Modus A) mit dem stärksten verfügbaren Modell
  planen, Sprints mit einem schnelleren Modell bzw. mittlerem Aufwand begleiten; Verbrauch
  gelegentlich prüfen. In AIS.chat gilt das monatliche Kontingent des Landes 🔎.

## 6. Review

Eine Frage: **Ist das Sprintziel erreicht?** Belege: Probeprüfung (Selbstkontrolle), Erklären
in eigenen Worten, gelöste Anwendungsaufgabe.

| Befund | Entscheidung |
|---|---|
| erreicht | weiter mit dem nächsten Sprint |
| teilweise | Wiederholungsrunde zu den offenen Teilen **oder** weiter mit Begründung (Teil folgt später ohnehin) |
| nicht erreicht | Wiederholungsrunde zum selben Thema (anderer Zugang, andere Quelle); neue Themen erst im übernächsten Sprint |
| holprig, unklar, widersprüchliche Quellen | Fachexpertin dazuholen |

Richtwert Probeprüfung: ab etwa 80 % richtig *erreicht*, 60–80 % *teilweise*, darunter
*nicht erreicht* – das Skript schlägt so vor, die Entscheidung trifft die lernende Person.

## 7. Retro

Erst wenn alle Sprints durch sind, rund 20 Minuten:
1. Was hat funktioniert?
2. Was hat nicht funktioniert?
3. Welche Quelle hat getragen, welche taugte nichts?
4. Was macht der nächste Lernzyklus anders?
5. Wo liegt das Ergebnis, damit andere es finden?

Der größte Wert entsteht für andere: Wer später dasselbe lernt, findet, welcher Kurs nichts
taugte und welches Buch getragen hat. Ablage: Fachgruppen- oder Bildungsgangordner,
Moodle-Kurs der Fachgruppe, Wissensdatenbank. Bei Lerngruppen: Empfehlungen sammeln und
zusammenfassen, ohne Namen.

## 8. Typische Lernpfade in der Schule

| Anlass | Ziel (Beispiel) | Sprints | Fachexpertin | Nachweis |
|---|---|---|---|---|
| Lehrkraft übernimmt neues Lernfeld | „Ich kann die Lernsituationen des Lernfelds fachlich sicher unterrichten und typische Schülerfehler vorhersagen." | 6 × 1 Woche | Kollegin der Fachgruppe | Unterrichtsskizze, Probeerklärung |
| Lehrkraft wird Prüferin bzw. Prüfer | „Ich kann Prüfungsaufgaben nach den Vorgaben des Ausschusses beurteilen." | 4 × 1 Woche | erfahrenes Ausschussmitglied | Probebeurteilung einer Musteraufgabe |
| Auszubildende vor einer Klassenarbeit | „Ich kann Störungen der Anlage X den Ursachen zuordnen und die Beseitigung begründen." | 3–4 × 1 Woche | Lehrkraft | Probeprüfung, Fallkarte |
| Auszubildende vor der Abschlussprüfung | „Ich kann Aufgaben der Musterprüfung im Zeitrahmen lösen." | 8 × 1 Woche | Lehrkraft, Ausbilder | Musterprüfung unter Zeit |
| Fachschule Technik, Projektarbeit | „Ich kann die Auslegung begründen und gegen Alternativen abwägen." | 6 × 2 Wochen | betreuende Lehrkraft, Betrieb | Zwischenpräsentation |
| Führungs- oder Beratungsrolle | „Ich kann schwierige Gespräche strukturiert führen." | 4 × 1 Woche, mit Rollenspielen | erfahrene Person in der Rolle | Rollenspiel-Feedback |

Bewährte Phasenfolge für fachlich neue Gebiete: **Grundlagen** (wie funktioniert es, wo irrt
man typischerweise) → **Qualitätskriterien und Risiken** → **Methoden und Verfahren** →
**eigenes kleines Anwendungsprojekt**. Eine Zertifikats- oder Abschlussprüfung kann den
Lernpfad absichern – dann Musterprüfungen als Probeprüfung nutzen (Quelle angeben,
Nutzungsrechte 🔎).
