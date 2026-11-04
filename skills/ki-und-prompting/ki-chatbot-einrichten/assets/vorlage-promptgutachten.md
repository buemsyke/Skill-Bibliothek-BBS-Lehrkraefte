---
artefakt: Promptgutachten
titel: "[Name bzw. Herkunft des Systemprompts]"
skill: ki-chatbot-einrichten
skill_version: "1.3"
stand: [JJJJ-MM-TT]
bereich: pruefen
geprueft: "[Datei bzw. Quelle, Stand]"
status: "KI-Entwurf – Einschätzung der Fachberatung bzw. Lehrkraft"
---

# Promptgutachten: [Name]

## 1. Steckbrief

| Feld | Befund |
|---|---|
| Herkunft | [Plugin, Verlag, Kollegium – Version, Stand 🔎] |
| Zweck (ein Satz) | [was die KI tun soll] |
| Zielgruppe | [Lernende · Lehrkräfte · beide] |
| Plattform und Einsatzort | [Seite, Block, Persona, Modus] |
| Länge | [n] Zeichen, [n] Abschnitte |
| Ausgabe | [Chattext · JSON mit Schema · Feldwerte] |

## 2. Datenfluss

| Daten | woher | an das Modell? | Folgerung |
|---|---|---|---|
| [Platzhalter `{{…}}`] | [Plattform setzt ein: …] | ja | [ … ] |

## 3. Stärken – übertragbar

- [Gestaltungsidee, die eigene Anweisungen übernehmen sollten – mit Stelle]

## 4. Prüfraster P1–P12

| Nr. | Kriterium | Einschätzung | Hinweis |
|---|---|---|---|
| P1 | Zweck und Zielgruppe | erfüllt · teilweise · fehlt · nicht prüfbar | |
| P2 | Aufbau | | |
| P3 | Kontextgrenze und Quellen | | |
| P4 | Didaktik | | |
| P5 | Ausgabevertrag | | |
| P6 | Darstellung | | |
| P7 | Sprache | | |
| P8 | Datenfluss und Datenschutz | | |
| P9 | Eingeschleuste Anweisungen | | |
| P10 | Leitplanken | | |
| P11 | Sicherheit | | |
| P12 | Wartbarkeit | | |

Skriptergebnis (`anweisung_pruefen.py`): [n ❌ · n ⚠ – wichtigste Zeilen]

## 5. Befunde

| Nr. | Stelle | Beleg (kurz, wörtlich) | Wirkung | Vorschlag |
|---|---|---|---|---|
| B1 | [Abschnitt] | „[…]“ | [was passiert] | [Ergänzung bzw. Formulierung] |

## 6. Einsatzempfehlung

- **geeignet für:** [ … ]
- **nicht einsetzen:** [z. B. Seiten mit Abgaben, Bewertungen oder Teilnehmerdaten]
- **vorher klären (Administration, Datenschutz):** [Anbieter, Protokolle, Sichtbarkeit je Rolle]

## Qualitätscheck

| Kriterium | Ergebnis | Hinweis |
|---|---|---|
| Herkunft und Datenfluss geklärt bzw. als 🔎 | ✅/⚠️/❌ | |
| jeder kritische Befund mit Beleg (`zitate_pruefen.py`) | | |
| Stärken und Befunde getrennt, Vorschläge umsetzbar | | |
| Prompt nicht vollständig kopiert (nur Belegzitate) | | |

## Annahmen und Prüfaufträge

- 🔎 Prüfen: [Herkunft, Version, Plattformverhalten]
- ⚠️ Annahme: [ … ]

## Übergabe

- Eigene Anweisung nach dem Muster: `ki-chatbot-einrichten` Modus A bzw. B
- [Leitplanken an Administration bzw. Datenschutz weitergeben]

> KI-gestützt erstellt (Skill ki-chatbot-einrichten v1.3). Fachliche Prüfung und Verantwortung: Lehrkraft.
