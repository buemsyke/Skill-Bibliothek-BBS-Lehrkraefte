# Lernumgebung mit Claude Code einrichten

Für Lehrkräfte, die mit Claude Code auf dem eigenen Rechner lernen. Zwei Architekturen, ein
Ordner: Die **Sicherheitsarchitektur** sagt, *was* in den Lernordner darf; die
**Wissensarchitektur** sagt, *wie* es dort geordnet ist.

## 1. Sicherheitsarchitektur – was in den Lernordner darf

- Die KI sieht alles, was im Lernordner liegt, und über sie die Cloud. Deshalb **nur
  öffentliches oder freigegebenes Material**: Herstellerhandbücher, frei zugängliche
  Fachseiten, eigene Notizen. **Nie**: interne Dokumente, Schülerarbeiten, Noten,
  Personaldaten, unveröffentlichte Prüfungsaufgaben. Wer vertraulich arbeiten muss, für den
  ist diese Umgebung nicht gebaut.
- **Isolation**, damit die KI außerhalb des Lernordners nichts erreicht:

| Lösung | Grenze | Vorteil | Nachteil |
|---|---|---|---|
| Virtuelle Maschine (z. B. VirtualBox) mit geteiltem Ordner | eigener Kernel | härteste klassische Grenze; Snapshot setzt nach Experimenten zurück | Einrichtung kostet Zeit |
| Container (z. B. Podman rootless) | gemeinsamer Kernel | schlank, startet in Sekunden | schwächere Grenze |
| Sandbox (bubblewrap; Sandbox-Modus von Claude Code unter Linux) | einzelne Prozesse | feingranular, ohne zweites System | Konfiguration je Werkzeug |

- Der Netzwerkzugang bleibt offen (die KI braucht ihre Schnittstelle und die Websuche) – der
  Schutz endet dort. Die Ordnergrenze ist **kein echter Sicherheitsmechanismus**, sondern eine
  Entscheidungshilfe: Wer eine Datei hineinlegt, entscheidet bewusst, dass die KI sie sehen darf.

## 2. Wissensarchitektur – zwei Ebenen (KISS)

```
lernen/                         ← geteilter Lernordner
├── CLAUDE.md                   ← Dauerkontext für alle Themen
├── .claude/skills/             ← wiederkehrende Abläufe (z. B. dieser Skill, Rollenspiel)
├── wissen/                     ← Ebene 1: Wissensbasis nach THEMEN (überdauert Projekte)
│   ├── waermepumpe/
│   │   ├── CLAUDE.md           ← nur was dieses Thema betrifft
│   │   ├── installationsanleitung.pdf
│   │   ├── installationsanleitung_zettel.md   ← Begleitnotiz (Fremdformat)
│   │   └── kaeltekreis.md                     ← Zettel
│   └── ki-verordnung/
└── projekte/                   ← Ebene 2: Lernprojekte, die aus der Basis schöpfen
    └── 2026-lf-waermepumpe/
        ├── 93_lernakte_waermepumpe.md
        └── 93_probepruefung_waermepumpe_P1.md
```

- **Das Thema entscheidet über die Ablage**, nicht das Projekt: Eine Notiz zum Kältekreis
  taugt in zwei Jahren für einen ganz anderen Zweck.
- Neues Lernthema = neuer Ordner unter `wissen/`, ohne Umbau.

## 3. Prompt, Projektanweisung, Skill – wer was trägt

| Baustein | trägt | Beispiel |
|---|---|---|
| **Prompt** | die aktuelle Aufgabe | „Probeprüfung zu Sprint 2, fünf Fragen" |
| **Projektanweisung** `CLAUDE.md` | dauerhaften Kontext, gilt in jeder Sitzung | KI als Coach, Wissensdatenbank und Sparringspartner; Quellenpflicht |
| **`CLAUDE.md` im Themenordner** | Regeln nur für dieses Thema | „Lies nur die drei nächsten verlinkten Zettel" |
| **Skill** | wiederverwendbare Prozedur, nur bei Bedarf geladen | Probeprüfung, Rollenspiel, dieser Skill |

Faustregel: Was über mehrere Projekte wiederkehrt → Skill. Was nur ein Thema betrifft →
`CLAUDE.md` des Themenordners. Skills nicht über die Themenordner verteilen – Claude Code
findet sie über die Beschreibung. Anweisungsdateien liefern Kontext; widersprechen sich zwei
Ebenen, ist das Ergebnis nicht garantiert – Widersprüche vermeiden.

Ablageort der Skills: projektgebunden unter `lernen/.claude/skills/` (wandert mit dem
Lernordner, vom Host aus bearbeitbar) oder persönlich unter `~/.claude/skills/` (für alle
Umgebungen; liegt dann außerhalb des geteilten Ordners). Bei gleichem Namen gilt der
projektgebundene Skill.

### Vorlage `lernen/CLAUDE.md`

```markdown
# Lernumgebung – Dauerkontext
Du arbeitest als Coach, Wissensdatenbank und Sparringspartner für meine Lernprojekte.
- Lernprojekte liegen unter projekte/, je Projekt eine Lernakte (93_lernakte_*.md). Lies sie zu
  Beginn jeder Sitzung und schreibe sie am Ende fort (Zettel, Review, offene Fragen).
- Fachaussagen nur aus wissen/ und den Quellen der Lernakte; nenne immer Datei und Seite bzw.
  Abschnitt. Steht etwas nicht in den Quellen, sag das. Erfinde nichts.
- Findest du am Ende einer Notiz Verweise (- Verweis: [..](..)), folge ihnen – aber nur bis zu
  den drei nächsten Zetteln (python3 .claude/skills/agiles-lernen-mit-ki/scripts/zettel_verknuepfen.py naechste <notiz> -n 3).
- Stelle Rückfragen und sokratische Fragen, statt sofort zu erklären, wenn ich selbst darauf
  kommen kann. Löse Übungen nicht für mich.
- Probeprüfungen wertet scripts/probepruefung_auswerten.py aus, nicht du.
- Keine personenbezogenen oder vertraulichen Daten; liegt so etwas im Ordner, sag es mir.
```

## 4. Zettelkasten

- **Zettel** = kurze Markdown-Notiz mit **einer** Kernaussage in eigenen Worten und Fundstelle
  (Vorbild: Luhmanns Zettelkasten). Welche Zettel zusammengehören, entscheidet der Mensch;
  das Skript stellt nur die Verknüpfung her.
- **Verknüpfen** (relative Pfade, damit Host und VM dieselben Verweise lesen):
  `python3 scripts/zettel_verknuepfen.py verknuepfen wissen/waermepumpe/kaeltekreis.md wissen/waermepumpe/stoerungen.md`
  → hängt an `stoerungen.md` unter `## Verweise` die Zeile `- Verweis: [kaeltekreis](kaeltekreis.md)` an.
- **Fremdformate** (PDF, XML, DOCX …) bekommen eine Begleitnotiz `<name>_zettel.md`, die den
  Verweis aufnimmt – automatisch für einen ganzen Ordner:
  `python3 scripts/zettel_verknuepfen.py begleitnotizen wissen/`
- **Nur das Nächste lesen:** `python3 scripts/zettel_verknuepfen.py naechste <notiz> -n 3`
  listet die drei nächsten verknüpften Zettel – so steuert man genau, was die KI liest, statt
  den ganzen Ordner zu laden.
- **Aufräumen:** `python3 scripts/zettel_verknuepfen.py pruefen wissen/` meldet tote Verweise,
  absolute Pfade, Fremdformate ohne Begleitnotiz und Zettel ohne jede Verbindung.

## 5. Kosten (Erfahrungswerte, ändern sich mit Preisen und Modellen)
- Ein Pro-Abo reicht laut Artikel für etwa zwei Lerneinheiten von je einer Stunde am Tag.
- Lernpfad mit dem stärksten Modell planen, Sprints mit einem schnelleren Modell und mittlerem
  Aufwand begleiten; Verbrauch gelegentlich in der Kontoübersicht prüfen.
- Gegenüber dem Browser: Die Umgebung wird einmal eingerichtet und trägt dann jedes weitere
  Lernthema; im Browser beginnt jedes Lernprojekt von vorn, und bei vielen hochgeladenen
  Dateien lädt der Chat vermutlich nur Ausschnitte nach (RAG) – das kann die Qualität mindern.
