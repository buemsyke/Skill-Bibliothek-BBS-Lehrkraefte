# Plattformen: wo die Anweisung steht, was sie zeigt, wohin die Daten gehen

Stand der Angaben: Oktober 2026. Welche KI-Funktionen eine Moodle-Instanz hat, hängt von
Version, installierten Plugins und Freischaltung durch die Administration ab – **alles mit 🔎
an der eigenen Instanz prüfen**, bevor es ins Paket kommt.

## 1. Überblick

| Plattform | Anweisung steht … | für Lernende | Hintergrundwissen | prüfen 🔎 |
|---|---|---|---|---|
| **Moodle mit KI-Chat-Plugin** (z. B. KI-Chat-Block mit KI-Manager, OpenAI-Chat-Block) | je Block, Kurs oder als „Persona“ – je nach Plugin; teils nur durch die Administration | wenn der Block für die Rolle sichtbar ist | je nach Plugin: Text im Feld, Dateien, „Quelle der Wahrheit“ | Felder, Zeichenlimit, wer die Anweisung ändern darf, Anbieter, Protokolle |
| **Moodle mit Seiten- oder Formularassistent** (Agenten- bzw. Formularmodus eines Plugins) | im Plugin, nicht änderbar | meist nur Lehrkräfte | die aktuelle Seite: Felder, Werte, Hilfetexte | ob der Modus auf Bewertungs- und Abgabeseiten aktiv ist |
| **Moodle-Kern ab 4.5** (KI-Subsystem: Anbieter und Platzierungen) | Systemanweisung je Aktion in der Website-Administration | Kursassistenz (Zusammenfassen, ab 5.0 Erklären), Editor (Text, Bild erzeugen) | der Text der Seite bzw. die Eingabe | Version, Anbieter, Nutzungsrichtlinie, Bericht über KI-Nutzung |
| **AIS.chat** | Assistent (Lehrkräfte), Lernszenario und Dialogpartner (Lernende über Link, ohne Konto) | ja, zeitlich begrenzt | Dateien je Element | Zeichenlimit, Freigabedauer, Upload durch Lernende – Details im Skill `agiles-lernen-mit-ki` |
| **andere Assistenten** (fobizz u. a.) | Anweisungsfeld des Assistenten | je nach Dienst | Dateien | Vertrag mit dem Schulträger, Altersgrenzen, Serverstandort |

Lehrkräfte richten Chatbots für Lernende nur auf Plattformen ein, die Schule bzw. Land
freigegeben haben 🔎 (Medienkonzept, Datenschutzbeauftragte bzw. Datenschutzbeauftragter).

## 2. Darstellung in Moodle

- **Formeln:** Der Filter *MathJax* muss für Kurs bzw. Website aktiv sein 🔎. Er rendert
  `\( … \)` im Text, `\[ … \]` und `$$ … $$` abgesetzt – **nicht** `$ … $`. Der Filter
  *TeX-Notation* setzt `$$ … $$` als Bild. In der Anweisung deshalb immer: „Formeln mit
  \( … \) im Satz und $$ … $$ abgesetzt.“ Test T8.
- **Chatfenster:** Ob ein KI-Chat-Plugin Markdown, Tabellen und Formeln rendert, ist Sache des
  Plugins 🔎 – Probelauf T8/T9 entscheidet. Rendert es kein Markdown, in FORM „ohne Markdown,
  Listen mit Bindestrich“ schreiben.
- **Code:** im Chat als Codeblock mit Sprache (```` ```python ````); in HTML-Feldern (Editor)
  als `<pre><code class="language-python">…</code></pre>`. Farbige Hervorhebung nur mit
  passendem Filter bzw. Plugin 🔎.
- **Werte für Felder:** Was eine KI für ein Formularfeld vorschlägt, wird unverändert
  übernommen – also ohne Codezaun, im Format des Felds (HTML im Editor, sonst reiner Text).
- **Quizfragen** mit Formeln: Quelle mit `\( … \)` schreiben, Export mit `edu-quiz` (≥ 0.2.3
  maskiert Formeln und Code für GIFT) – Skill `quizfragen-erstellen`.

## 3. Datenfluss – was geht an das Sprachmodell?

| Funktion | wird gesendet | Folgerung |
|---|---|---|
| Chat mit Anweisung | Anweisung, Hintergrundwissen (ganz oder in Ausschnitten), Chatverlauf | keine Personendaten in Anweisung und Dateien; Lernende geben keine ein |
| Seiten- oder Formularassistent | zusätzlich Inhalt der aktuellen Seite: Feldbezeichnungen, **aktuelle Werte**, Hilfetexte | **nie auf Seiten mit Schülerdaten** (Bewertung, Abgaben, Teilnehmende, Foren mit Namen) |
| Zusammenfassen, Erklären | Text der Aktivität bzw. Auswahl | nur Material ohne Personendaten |
| Text- oder Bilderzeugung im Editor | Eingabe der Lehrkraft | Ergebnis prüfen und kennzeichnen (`ki-kennzeichnung`) |

Dazu klären 🔎: **Anbieter** (Cloud-Dienst oder lokales Modell, z. B. über Ollama), Vertrag
zur Auftragsverarbeitung, Serverstandort, **Protokolle** (wer kann Anfragen und Chatverläufe
einsehen?). Protokolle und Chatverläufe von Lernenden werden **nicht** für Einzelauswertungen
genutzt (Leitplanke: Lernstände nur für die Lerngruppe).

## 4. Einrichten – Checkliste

- [ ] Plattform von Schule bzw. Land freigegeben; Anbieter und Protokolle bekannt 🔎
- [ ] Sichtbarkeit: nur für die Lerngruppe, nur im geplanten Zeitraum; in Prüfungssituationen
      (Klassenarbeit als Moodle-Test) ausgeblendet
- [ ] Anweisung eingefügt, Zeichenlimit eingehalten (`anweisung_pruefen.py --max-zeichen N`)
- [ ] Hintergrundwissen: nur eigene, öffentliche oder freigegebene Dateien; **keine
      Musterlösungen** bewerteter Aufgaben, keine Schülerarbeiten
- [ ] Nutzungsrichtlinie bzw. Einwilligung geklärt; bei Minderjährigen Vorgaben der Schule und
      Altersgrenzen des Anbieters 🔎
- [ ] Lernende informiert: Hinweistext „KI-Chat im Kurs“ (`ki-kennzeichnung`), Einführung im
      Unterricht
- [ ] Probelauf in der Schüleransicht bzw. mit Zweitgerät, Pflichttests ✓
- [ ] Freigabezeile durch die Lehrkraft; Termin für die Überprüfung nach dem Einsatz

## 5. Nach dem Einsatz

- Rückmeldung der Lerngruppe **zusammengefasst** einholen (was half, wo antwortete der Chatbot
  falsch?) – keine Einzelauswertung von Chatverläufen.
- Falsche Antworten, die Lernende melden, als neuen fachlichen Test in den Probelauf aufnehmen
  und die Anweisung bzw. das Hintergrundwissen nachschärfen.
- Chatbot nach dem Zeitraum ausblenden bzw. Freigabe beenden.
