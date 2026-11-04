---
artefakt: Programmieraufgabe
titel: "[Was das Programm im Auftrag leistet]"
skill: programmieraufgabe-erstellen
skill_version: "1.5"
stand: JJJJ-MM-TT
bildungsgang: "[Bildungsgang]"
curriculare_vorgabe: "[RLP/RRL, Lernfeld/Lerngebiet]"
dqr: 4
status: "KI-Entwurf – fachlich zu prüfen"
umgebung: "[Board bzw. Steuerung, Dialekt, Entwicklungsumgebung, Sensor mit Datenblatt]"
---

# Programmieraufgabe: [Titel]

## Situation

[Bezug zur Handlungssituation in höchstens drei Sätzen: Wofür wird das Programm gebraucht?]

[ABBILDUNG: Darstellung, mit der programmiert wird – Anschlussbild bzw. Schaltplan (Pins,
Sensor, Aktor), Kennlinie des Sensors, Ablauf- oder Zustandsdiagramm, beim G-Code die
Werkstückzeichnung mit Maßen und Nullpunkt; Quelle, Alternativtext]

## Anforderungen

| Nr. | Anforderung | Prüfung |
|---|---|---|
| A1 | [Eingang: Größe, Bereich, Einheit] | Testfall 1–2 |
| A2 | [Ausgang: Format, Einheit, Takt] | Testfall 1 |
| A3 | [Fehlerverhalten] | Testfall 3 |

## Startcode

Datei `43_code/[name]_start.[ino|py|nc]` – ergänzen Sie die mit `TODO` markierten Stellen.

```[cpp|python|gcode]
[Startcode]
```

## Testfälle

| Nr. | Eingabe | erwartete Ausgabe | Toleranz |
|---|---|---|---|
| 1 | [Normalfall] | [Wert mit Einheit] | [±] |
| 2 | [Grenzfall] | | |
| 3 | [Fehlerfall] | [Meldung] | – |

## Hilfen

<details><summary>Hilfe 1 – Hinweis</summary>[…]</details>
<details><summary>Hilfe 2 – Teilschritt</summary>[…]</details>
<details><summary>Hilfe 3 – Teillösung</summary>[…]</details>

# Lösungen und Erwartungshorizont

Musterlösung: `43_code/[name]_loesung.[ino|py|nc]` – geprüft mit
`code_pruefen.py` ([Ergebnis]).

```[cpp|python|gcode]
[Musterlösung]
```

| Kriterium | erwartet | Punkte |
|---|---|---|
| Funktion | Testfälle 1–3 bestanden | |
| Messkette / Maße | [Rechnung mit Einheiten] | |
| Struktur und Kommentar | Konstanten mit Einheit, keine Tutorial-Reste | |

# Didaktische Hinweise

[Aufgabenform (PRIMM, Parsons, Lücke, Fehlersuche, offen), Vorwissen, Zeit, typische Fehler,
Regel für KI-Codeassistenten]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| | | |

## Annahmen und Prüfaufträge

- ⚠️ Annahme: …
- 🔎 Prüfen: Datenblatt, Board-Dokumentation bzw. Steuerungshandbuch

## Übergabe

- Codeordner `43_code/`, Testfälle, Prüfergebnis
- Empfohlen: `material-pruefen` (C)

> KI-gestützt erstellt (Skill programmieraufgabe-erstellen v1.5). Fachliche Prüfung und Verantwortung: Lehrkraft.
