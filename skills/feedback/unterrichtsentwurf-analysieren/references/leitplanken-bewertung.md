# Leitplanken für Prüfen, Rückmelden und Bewerten

Verbindlich für Begutachtungen und Rückmeldungen (`bereich: pruefen`) und für KI-Chatbots
im Unterricht.
Ergänzt den Skill-Vertrag. Quelle: `_gemeinsam/leitplanken-bewertung.md`.

## 1. Grundsatz: Vorschlag, nie Entscheidung

- Werkzeuge und KI liefern **begründete Vorschläge**. Punkte, Noten, Rückmeldungen und
  Gutachten **verantwortet die Lehrkraft** (bzw. die zuständige Person).
- Was weitergegeben oder veröffentlicht wird, trägt bis zur Durchsicht `Freigabe: ausstehend`.
  Nach Durchsicht ersetzt die Lehrkraft die Zeile durch `Freigabe: erteilt – KÜRZEL, JJJJ-MM-TT`.
- Keine automatisierte Einzelentscheidung mit rechtlicher Wirkung (vgl. DSGVO Art. 22).

## 2. Datenschutzstufen

| Stufe | Daten | erlaubt |
|---|---|---|
| **0** | keine Personendaten (Aufgaben, Erwartungshorizont, Rubrik, Musterlösung) | Claude darf lesen und schreiben |
| **1** | pseudonymisierte Abgaben, Punkte je Pseudonym | **nur lokale Werkzeuge** lesen Antworttexte; **Claude sieht nur Zahlen, IDs, Pseudonyme und Kennzeichen** |
| **2** | Klarnamen, Zuordnungsdatei (Mapping), Rückführungsergebnisse | **nie an eine KI**; nur lokal bei der Lehrkraft |

Feste Regeln:
- Claude öffnet **keine Schülerantworten** (auch nicht pseudonymisiert) und keine Dateien
  der Stufe 2. Skripte geben nur Aggregate aus.
- **Lernstände und Lernberichte nur für die Lerngruppe** (Entscheidung der Fachberatung,
  09.10.2026): keine Einzelberichte zu Lernenden, keine Auswertung von Zugriffs- oder
  Aktivitätslogs, kein Live-Zugriff auf LMS-Kurse mit Klarnamen – Bewertungsexporte lokal
  pseudonymisieren. Einzelrückmeldungen schreibt die Lehrkraft.
- Das gilt auch für **KI-Funktionen im LMS** (KI-Chat, Seiten- oder Formularassistent,
  Zusammenfassen): Sie senden den Seiteninhalt an das Sprachmodell. Deshalb nicht auf Seiten mit
  Abgaben, Bewertungen, Teilnehmenden oder Forenbeiträgen mit Namen einsetzen; Chatbots für
  Lernende bewerten nicht, und ihre Chatverläufe werden nicht einzeln ausgewertet
  (Anwendung der Regeln oben, Stand 19.10.2026).

## 3. Ehrlichkeit und Sicherheit

- Befunde mit **Sicherheit**: hoch/mittel/niedrig bzw. Konfidenz in %.
  Ab **75 %** gilt ein Befund als Vorschlag; darunter: „unklar – Lehrkraft entscheidet".
- **„nicht prüfbar"** statt raten (fehlende Angaben, Abbildungen, Handschrift, Skizzen).
- Begutachtungen: jeder kritische Befund mit **wörtlichem Beleg**; Belege werden mit
  `scripts/zitate_pruefen.py` gegen das Dokument geprüft.

## 4. Rechtlicher Rahmen (🔎 vor Einsatz mit Schulleitung/Datenschutz abstimmen)

- KI-Verordnung (EU) 2024/1689: KI-Systeme zur **Bewertung von Lernergebnissen** und zur
  Steuerung von Lernprozessen zählen zu den **Hochrisiko-Anwendungen** (Anhang III Nr. 3);
  Systeme für **Personalentscheidungen** ebenso (Anhang III Nr. 4).
  Pflichten u. a. zu
  menschlicher Aufsicht (Art. 14), Betreiberpflichten (Art. 26) und KI-Kompetenz (Art. 4).
  🔎 Geltungsbeginn und Ausnahmen (Art. 6 Abs. 3) aktuell prüfen.
- Die Skills sind **vorbereitende Hilfen** mit menschlicher Endentscheidung; sie ersetzen
  keine Datenschutz-Folgenabschätzung und keine Freigabe durch die Schule.
- Entwurfsbegutachtungen und Unterrichtsreflexionen nur als **Selbstcheck und kollegiale
  Beratung** – nicht für Auswahlverfahren, dienstliche Beurteilungen oder die Benotung von
  Prüfungsunterricht.
- **Prüfungsrelevante Entwürfe** (Prüfungsunterricht, bewertete Unterrichtsbesuche): Der
  **Selbstcheck** durch die Autorin bzw. den Autor ist erlaubt und wird **gekennzeichnet**
  (Entscheidung der Fachberatung, 19.10.2026). Das heißt: Kopf `pruefungsrelevant: true`,
  Hinweise zur Überarbeitung statt fertiger Formulierungen, und die KI-Nutzung wird im Entwurf
  als Hilfsmittel angegeben – Form nach den Vorgaben des Studienseminars, sonst in der Erklärung
  zur selbständigen Anfertigung. Kollegiale Beratung zu solchen Entwürfen bleibt menschlich.
