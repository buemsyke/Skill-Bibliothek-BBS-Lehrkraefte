# Sicherheit bei Experimenten und Schülerversuchen

Eigene Zusammenfassung für die Planung. Maßgeblich sind die **Richtlinie zur Sicherheit im
Unterricht (RiSU)** der KMK in der aktuellen Fassung, die Gefahrstoffverordnung, die
DGUV-Vorschriften und die Landesregelungen 🔎 vor jedem Einsatz prüfen. **Kein Skill gibt ein
Experiment frei.** Gefährdungsbeurteilung, Vorversuch und Freigabe verantwortet die Lehrkraft.

## Inhalt
1. Ablauf: von der Idee zum freigegebenen Versuch
2. Gefährdungsbeurteilung – Mindestinhalt
3. Typische Gefährdungen in technischen Versuchen
4. Gefahrenhinweise für die Prüfskripte
5. Plausibilität von Messwerten

---

## 1. Ablauf: von der Idee zum freigegebenen Versuch

1. **Ziel und Hypothese** festlegen: Welche Frage beantwortet der Versuch?
2. **Ersatzstoff- und Ersatzverfahrensprüfung:** Geht es mit ungefährlicheren Stoffen, kleineren
   Mengen, geringerer Spannung oder als Simulation bzw. Video?
3. **Gefährdungsbeurteilung** schriftlich (Abschn. 2); entscheiden: **Lehrerversuch** oder
   **Schülerversuch**, Gruppengröße, Aufsicht.
4. **Vorversuch** durch die Lehrkraft mit Originalmaterial; Messwerte notieren (Erwartungswerte
   für den Erwartungshorizont).
5. **Betriebsanweisung bzw. Sicherheitshinweise** in der Versuchsanleitung; **Unterweisung** der
   Lernenden vor dem Versuch, dokumentiert.
6. **Freigabe** durch die Lehrkraft (Name, Datum) – erst dann Ausgabe an Lernende.
7. **Entsorgung** und Aufräumen planen.

## 2. Gefährdungsbeurteilung – Mindestinhalt

| Feld | Inhalt |
|---|---|
| Versuch, Ziel | Bezeichnung, Lerngruppe, Lehrer- oder Schülerversuch |
| Stoffe und Geräte | Stoffe mit Menge, Konzentration, GHS-Piktogrammen, H- und P-Sätzen; Geräte mit Spannung, Leistung, bewegten Teilen |
| Gefährdungen | chemisch (Gase, Ätzwirkung, Brand, Explosion), elektrisch, mechanisch, thermisch, Strahlung, Lärm |
| Ersatzprüfung | geprüfte Alternativen und warum (nicht) gewählt |
| Maßnahmen nach **STOP** | **S**ubstitution · **T**echnisch (Abzug, Schutzscheibe, Sicherheitsbuchsen, Fehlerstrom-Schutzschalter, NOT-AUS) · **O**rganisatorisch (Mengenbegrenzung, Aufsicht, Unterweisung, Kleingruppen) · **P**ersönlich (Schutzbrille, Handschuhe, Kittel) |
| Entsorgung | Sammelbehälter, Neutralisation, Batterien/Akkus |
| Notfall | Erste Hilfe, Augendusche, Feuerlöscher, NOT-AUS, Notruf |
| Vorversuch | Datum, Ergebnis, Auffälligkeiten |
| Freigabe | Name der Lehrkraft, Datum |

Ein allgemeiner Hinweis wie „PSA tragen, Richtlinien beachten“ **ersetzt keine**
Gefährdungsbeurteilung.

## 3. Typische Gefährdungen in technischen Versuchen

- **Elektrolyse:**
  - Mit kochsalzhaltigem Elektrolyt (Salzwasser, NaCl, Salzsäure) entsteht an der Anode
    **Chlor**.
  - Für die Wasserelektrolyse ungefährlichere Elektrolyte wählen, z. B. verdünnte
    Natriumsulfatlösung 🔎 Gefährdungsbeurteilung.
  - Natron- und Kalilauge sind **ätzend**.
  - Unedle Elektroden (Zink, Aluminium) lösen sich auf; dabei entstehen Nebenprodukte.
- **Wasserstoff, Knallgas:**
  - Nur kleine Volumina (Reagenzglas) erzeugen und auffangen; keine Ansammlung in Gefäßen,
    Ballons oder Gasometern.
  - Zündquellen fernhalten, lüften.
  - Die Knallgasprobe ist ein üblicher Nachweis. Sie braucht Mengenbegrenzung, Schutzbrille und
    eine Gefährdungsbeurteilung; die Durchführung durch Schülerinnen und Schüler legt die
    Lehrkraft fest 🔎 RiSU.
- **Netzspannung (230/400 V):**
  - Schülerversuche nur mit **Schutzkleinspannung** oder an dafür gebauten Experimentier- bzw.
    Prüfständen (Sicherheitsbuchsen, Fehlerstrom-Schutz, NOT-AUS) unter Aufsicht.
  - Anschlussarbeiten an Motoren und Umrichtern nur spannungsfrei nach den **fünf
    Sicherheitsregeln**.
  - Bei Frequenzumrichtern an Restspannung im Zwischenkreis denken.
  - 🔎 Qualifikation der Lehrkraft (Elektrofachkraft, elektrotechnisch unterwiesene Person)
    nach DGUV und Landesregel.
- **Mechanik und Robotik:** rotierende Teile, Quetschstellen, Schutzzaun bzw. kollaborativer
  Betrieb nach Herstellerfreigabe, reduzierte Geschwindigkeit im Teach-Betrieb, NOT-AUS.
- **Lithium-Akkus:** Kurzschluss, mechanische Beschädigung und Überladung → Brand; nur geeignete
  Ladegeräte, Brandschutzbehälter.
- **Löten, Kleben, 3D-Druck:** Dämpfe, Absaugung, heiße Oberflächen.

## 4. Gefahrenhinweise für die Prüfskripte

`versuch_pruefen.py` (Skill `experiment-planen`) meldet ⚠️, wenn eine Versuchsanleitung eine
dieser Kombinationen enthält und die Gefährdungsbeurteilung sie nicht behandelt:

| Signal im Text | Hinweis |
|---|---|
| Elektrolyse + Kochsalz / NaCl / Salzwasser / Natriumchlorid / Salzsäure | Chlorbildung an der Anode |
| Knallgas / Knallgasprobe | Mengenbegrenzung, Schutzbrille, Lehrkraft entscheidet über Durchführung |
| Wasserstoff + sammeln / Ballon / Flasche / Gasometer | Explosionsgefahr durch größere Gasmengen |
| Natronlauge / Kalilauge / NaOH / KOH | ätzend – Schutzbrille, Handschuhe |
| 230 V / 400 V / Netzspannung / Drehstrom | Schutzkleinspannung oder Prüfstand, fünf Sicherheitsregeln |
| Lithium / Li-Ion / Akku + laden | Brandgefahr |

## 5. Plausibilität von Messwerten

Erwartungswerte im Erwartungshorizont **aus einem Vorversuch** oder aus einer Rechnung mit
physikalischer Obergrenze – nie „mögliches Ergebnis“ ohne Prüfung. Prüfskript:
`messwerte_pruefen.py`.
- **Faraday:** Gasvolumen höchstens V = I·t/(z·F)·R·T/p (H₂: z = 2; O₂: z = 4).
- **Energieerhaltung:** Wirkungsgrad höchstens 1. In Ketten wird beim Rückrechnen vom Nutzen auf
  den Aufwand **dividiert**.
- **Einheiten:** Heizwert in MJ/m³ oder kWh/kg, nie m³/MJ.
- **Messunsicherheit:** Geräteangabe bzw. Ablesegenauigkeit; bei Produkten und Quotienten
  addieren sich die relativen Unsicherheiten (Größtfehler) bzw. ihre Quadrate (Gauß).
