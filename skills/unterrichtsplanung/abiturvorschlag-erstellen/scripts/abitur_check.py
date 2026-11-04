#!/usr/bin/env python3
"""abitur_check – Selbstprüfung eines dezentralen Abiturvorschlags (lokal, deterministisch).

Liest Schülermaterial (SM) und Lehrermaterial (LM) im Markdown-Format des Skills
abiturvorschlag-erstellen und prüft alles, was sich rechnen oder regelbasiert prüfen lässt:

  Katalog (R-Teil):  1.3 Kopf · 2.2/2.3 Kursfolge und Bezug je Aufgabe · 3.2/X.14 Lerngebiete ·
                     2.4 AFB je Zeile · 2.5 Lösungsvorschlag je Teilaufgabe · 2.6 Bewertungsmaßstab ·
                     2.7 Hilfsmittel · 3.3 Handlungssituation · X.10 Summen · X.13 SM = LM ·
                     4.3 Gesamt-BE · X.7 Zeit je BE · 4.6 AFB gesamt und je Aufgabe · X.1 Einstieg ·
                     X.5 AFB im Operatorbereich · 4.4/4.5/X.2 Operatoren · X.9 Formulierungen ·
                     X.4 Operatoren SM = LM · X.3 „BE“ · S.1 Platzhalter · S.2 Anlagen · S.3 Dateien ·
                     S.4 Nummerierung
  K – Korrigierbarkeit: K.1 Merkmaltabelle je Teilaufgabe · K.2 Summen der Merkmale · K.3 Größe
                     und Wertwörter · K.4 Toleranz/Rundung · K.5 Alternativen bei offenen Aufgaben ·
                     K.6 Folgefehler bei Ersatzwerten · K.7 Auftragssätze · K.8 Anteil „Urteil“ ·
                     K.9 Bezeichner
  T – Betriebsmittelkennzeichen über bmk_pruefen.py im selben Ordner (nur wenn BMK vorkommen)
  Z – Zeichnungen als SVG über zeichnungen_pruefen.py: Z.1 Schülermaterial, Z.2 Lehrermaterial
      (❌ Zeichnung aus Zeichen; eingebundene SVG: ❌ fehlt, Text über Text oder Linie, Text aus
      dem Kasten, außerhalb des Bildes; ⚠ Mermaid, SVG ohne Spec – von Hand? –, schräge Leitungen)

Aufruf:
    python3 abitur_check.py SM.md LM.md [--fach technik|informatik] [--zeit 300] [--be 120]
        [--vergleich SM_B.md LM_B.md] [--bewertungsbogen DATEI.md] [--operatoren PFAD] [--json]

Operatoren und AFB-Bereiche stehen in references/operatoren-epa-technik.md (Kopie aus _gemeinsam).
--bewertungsbogen schreibt einen leeren Bewertungsbogen aus den Merkmaltabellen (überschreibt nie).
Exit-Code 1 bei ❌. Nur Python-Standardbibliothek; läuft vollständig lokal.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
try:
    from bmk_pruefen import pruefe_bmk          # bmk_pruefen.py aus _gemeinsam
except ImportError:  # pragma: no cover – ohne Hilfsmodul entfällt der BMK-Abgleich
    pruefe_bmk = None
try:
    from zeichnungen_pruefen import pruefe_zeichnungen   # zeichnungen_pruefen.py aus _gemeinsam
except ImportError:  # pragma: no cover – ohne Hilfsmodul entfällt Z
    pruefe_zeichnungen = None

AFB = ("I", "II", "III")
NOTEN = [(95, "15"), (90, "14"), (85, "13"), (80, "12"), (75, "11"), (70, "10"), (65, "09"), (60, "08"),
         (55, "07"), (50, "06"), (45, "05"), (40, "04"), (33, "03"), (27, "02"), (20, "01"), (0, "00")]
AFB_ZIEL = {"I": 30.0, "II": 40.0, "III": 30.0}
TAKT_GUT, TAKT_VERTRETBAR = (2.5, 3.0), (2.0, 3.5)
URTEIL_GRENZE = 30.0          # Prozent der BE (Richtwert, wie Freitextanteil in klausur-erstellen)
MERKMAL_MAX = 3.0

PARTIKEL = ("zusammen", "gegenüber", "heraus", "wieder", "durch", "dar", "aus", "ein", "auf", "an", "ab",
            "zu", "vor", "fest", "her", "nach", "weg")
# Imperative, die keine Arbeitsaufträge sind (Bearbeitungshinweise, Formatanweisungen)
HINWEIS = {"verwenden", "benutzen", "nutzen", "berücksichtigen", "beachten", "gehen", "annehmen", "zugrundelegen",
           "achten", "rechnen", "weiterrechnen", "vernachlässigen", "voraussetzen", "betrachten", "runden",
           "beziehen", "beginnen", "ankreuzen", "legen", "nehmen"}
FORMAT_INFORMATIK = {"eintragen", "ausfüllen", "markieren"}      # nach einem Operator zulässig (EPA Informatik)
KEIN_VERB = {"wenn", "falls", "sollten", "sollen", "können", "könnten", "haben", "hätten", "dass", "ob", "wie",
             "damit", "bevor", "nachdem", "sofern", "indem", "sodass", "als", "weil", "da", "sind", "waren",
             "werden", "würden", "müssen", "dürfen", "brauchen", "wollen", "möchten", "bitte", "was", "wo",
             "womit", "wobei", "worauf", "wofür", "welche", "welches", "welchen", "welcher", "die", "das",
             "der", "den", "dem", "des", "ein", "eine", "einen", "und", "oder", "aber", "auch", "nun", "dann",
             "erhalten", "bekommen", "finden", "sehen", "kennen"}
X9 = {"angeben": "„Geben Sie … an“ – durch „Nennen Sie“ oder „Bestimmen Sie“ ersetzen",
      "schreiben": "„Schreiben Sie …“ – kein Operator",
      "auswählen": "„Wählen Sie … aus“ – z. B. „Bestimmen Sie … nach der Regel …“",
      "eintragen": "„Tragen Sie … ein“ – nur als Formatanweisung nach einem Operator",
      "ausfüllen": "„Füllen Sie … aus“ – nur als Formatanweisung nach einem Operator"}
UNG = {"berechnung": "berechnen", "bestimmung": "bestimmen", "darstellung": "darstellen", "erläuterung": "erläutern",
       "erklärung": "erklären", "zeichnung": "zeichnen", "ableitung": "ableiten", "abschätzung": "abschätzen",
       "auswertung": "auswerten", "begründung": "begründen", "durchführung": "durchführen", "ermittlung": "ermitteln",
       "konstruktion": "konstruieren", "optimierung": "optimieren", "skizze": "skizzieren",
       "strukturierung": "strukturieren", "analyse": "analysieren", "untersuchung": "untersuchen",
       "beurteilung": "beurteilen", "bewertung": "bewerten", "stellungnahme": "stellung nehmen",
       "dimensionierung": "dimensionieren", "entwicklung": "entwickeln", "entwurf": "entwerfen",
       "überprüfung": "überprüfen", "nachweis": "nachweisen", "übertragung": "übertragen",
       "dokumentation": "dokumentieren", "beschreibung": "beschreiben", "nennung": "nennen", "vergleich": "vergleichen",
       "implementierung": "implementieren", "erstellung": "erstellen", "erweiterung": "erweitern",
       "modellierung": "modellieren", "bezeichnung": "bezeichnen", "kennzeichnung": "kennzeichnen",
       "anwendung": "anwenden", "definition": "definieren", "diskussion": "diskutieren", "einordnung": "einordnen",
       "kommentierung": "kommentieren", "vervollständigung": "vervollständigen", "benennung": "benennen"}
OFFEN = {"technik": {"entwickeln", "entwerfen", "konstruieren", "optimieren", "beurteilen", "bewerten",
                     "stellung nehmen", "analysieren", "untersuchen", "übertragen"},
         "informatik": {"entwickeln", "entwerfen", "modellieren", "implementieren", "erweitern", "testen",
                        "diskutieren", "beurteilen", "stellung nehmen", "übertragen"}}
RECHNEN = {"berechnen", "bestimmen", "ermitteln", "dimensionieren", "nachweisen", "abschätzen", "auswerten"}
VAGE = re.compile(r"\bggf\.|\bgegebenenfalls\b|\bevtl\.|\beventuell\b|\bmöglichst\b|\bkurz\b|\busw\.|\betc\.|"
                  r"\bo\.\s?Ä\.|\bu\.\s?a\.|\bmindestens\b|\bunter anderem\b", re.I)
KRITERIENLOS = re.compile(r"\b(?:geeignet|sinnvoll|angemessen|passend)\w*", re.I)
KRITERIUM_DA = re.compile(r"\bhinsichtlich\b|\bbezüglich\b|\banhand\b|\bKriteri|\bim Hinblick\b|\bin Bezug auf\b|"
                          r"\bgemäß\b|\bnach (?:der|den|dem) (?:Regel|Vorgabe|Tabelle|Anlage)|\bAnlage\s+\d", re.I)
PLURAL = re.compile(r"\b(?:Vorteile|Nachteile|Gründe|Maßnahmen|Möglichkeiten|Sensoren|Sensortypen|Sensorarten|"
                    r"Kriterien|Aspekte|Beispiele|Ursachen|Fehler|Unterschiede|Eigenschaften|Komponenten|"
                    r"Teilsysteme|Bauteile|Funktionen|Anforderungen|Risiken|Merkmale|Schritte|Argumente|Varianten|"
                    r"Alternativen|Testfälle|Gefahren|Probleme|Einflussgrößen|Ziele)\b")
ZAHLWORT = re.compile(r"\b(?:zwei|drei|vier|fünf|sechs|sieben|acht|neun|zehn|elf|zwölf|beide[nr]?|alle[nr]?|"
                      r"sämtliche[nr]?|jeweils|je|jede[nmrs]?)\b|(?<![\w-])\d+\b", re.I)
# „Kriterien Förderstrom und Bewässerungsdauer“: Mehrzahl mit benannter Aufzählung gilt als Umfang
AUFZAEHLUNG = re.compile(r"\s+[„\"]?[A-ZÄÖÜ][\w-]*[“\"]?(?:\s*,\s*[„\"]?[A-ZÄÖÜ][\w-]*[“\"]?)*\s+(?:und|sowie)\s+[„\"]?[A-ZÄÖÜ]")
WERTWORT = re.compile(r"\b(?:sinnvoll\w*|angemessen\w*|im Wesentlichen|weitgehend\w*|überzeugend\w*|schlüssig\w*|"
                      r"nachvollziehbar\w*|ansprechend\w*|gut|gute[nmrs]?)\b", re.I)
ERSATZWERT = re.compile(r"Ersatzwert|Rechnen Sie (?:im Folgenden |ab hier )?mit .{0,60}? weiter|"
                        r"falls Sie .{0,80}? nicht (?:lösen|bestimmen|berechnen|ermitteln)", re.I)
PLATZHALTER = [(r"\bXXX+\b", "„XXX“"), (r"\b20\s*_\s*_", "Jahresangabe „20__“"), (r"\b20XX\b", "„20XX“"),
               (r"\bJJJJ\b", "„JJJJ“"), (r"\bTT\.MM\.", "„TT.MM.“"), (r"\bVersion\s+X\.[XY]\b", "„Version X.Y“"),
               (r"\(\s*unvollständig\s*\)", "„(unvollständig)“"), (r"\bTODO\b", "„TODO“"), (r"\bFIXME\b", "„FIXME“"),
               (r"\bBBS\s*…", "„BBS …“"), (r"\[ABBILDUNG", "„[ABBILDUNG …]“")]
EINHEITEN = {"mm", "cm", "dm", "m", "km", "n", "kn", "n/mm", "n/mm²", "kg", "g", "t", "s", "ms", "min", "h", "v", "mv",
             "kv", "a", "ma", "w", "kw", "mw", "hz", "khz", "mhz", "ω", "kω", "°c", "k", "%", "bar", "pa", "kpa",
             "mpa", "l", "m³", "m²", "db", "bit", "byte", "kb", "mb", "gb", "bit/s", "mbit/s", "nm", "m/s", "1/min",
             "w/(m²·k)", "kwh", "be"}
DATEI = re.compile(r"\b[\w\-]+\.(?:pdf|lsc|java|py|php|html?|css|csv|xlsx?|docx?|sql|ino|zip|txt|json|xml|png|"
                   r"jpe?g|gif|svg|drawio|ap\d+|zap\d+|s7p|pkt|dxf|step|stp|ipt|iam)\b", re.I)
# „Anlage 2“ ist ein Verweis, „die Anlage 15 min“ (technische Anlage, Zahl mit Einheit) nicht
ANLAGE_VERWEIS = re.compile(r"\bAnlage\s+(\d+[a-z]?)\b(?![.,]\d)(?!\s*(?:min|s|h|ms|bar|mbar|Pa|kPa|kW|W|l|m|mm|cm|"
                            r"°C|K|%|V|mV|A|mA|Hz|m³/h|l/min)(?![\w/]))")
ABK = ("z. B.", "z.B.", "u. a.", "d. h.", "bzw.", "ca.", "Nr.", "Abb.", "vgl.", "ggf.", "evtl.", "inkl.", "max.",
       "min.", "Pos.", "Kap.", "usw.", "etc.", "o. Ä.", "s. o.", "s. u.", "lt.", "zzgl.", "Std.", "Tab.")


@dataclass
class Befund:
    kriterium: str
    name: str
    status: str            # ✅ ❌ ⚠ ➖
    befund: str


@dataclass
class Teil:
    nummer: str
    titel: str
    be: float | None
    text: str = ""
    operatoren: list[str] = field(default_factory=list)


@dataclass
class Aufgabe:
    nummer: int
    titel: str
    be: float | None
    teile: list[Teil] = field(default_factory=list)


@dataclass
class EwhZeile:
    teil: str
    text: str
    afb: dict
    summe: float | None
    operator: str | None
    substantiv: bool = True


@dataclass
class Merkmal:
    nr: str
    text: str
    art: str
    afb: str
    be: float


# ───────────────────────────── Markdown lesen ─────────────────────────────

def bereinigt(text: str) -> str:
    """YAML-Kopf und HTML-Kommentare entfernen (Vorlagenhinweise sind kein Prüfungstext)."""
    text = re.sub(r"\A﻿?---\n.*?\n---\n", "", text, flags=re.S)
    return re.sub(r"<!--.*?-->", "", text, flags=re.S)


def zellen(zeile: str) -> list[str]:
    return [re.sub(r"[*`]", "", z).strip() for z in zeile.strip().strip("|").split("|")]


def tabellen(text: str) -> list[list[list[str]]]:
    erg, akt = [], []
    for zeile in text.splitlines():
        s = zeile.strip()
        if s.startswith("|") and s.count("|") >= 2:
            if not re.fullmatch(r"\|?[\s:|\-]+\|?", s):
                akt.append(zellen(s))
        elif akt:
            erg.append(akt)
            akt = []
    if akt:
        erg.append(akt)
    return erg


def abschnitte(text: str) -> list[dict]:
    """Überschriften mit Ebene, Titel, eigenem Inhalt und Inhalt samt Unterabschnitten."""
    zeilen = text.splitlines()
    koepfe = [(i, len(m.group(1)), re.sub(r"[*_`]", "", m.group(2)).strip())
              for i, z in enumerate(zeilen) if (m := re.match(r"^\s{0,3}(#{1,6})\s+(.*?)\s*#*\s*$", z))]
    erg = []
    for k, (i, ebene, titel) in enumerate(koepfe):
        naechster = koepfe[k + 1][0] if k + 1 < len(koepfe) else len(zeilen)
        ende = next((j for j, e, _ in koepfe[k + 1:] if e <= ebene), len(zeilen))
        erg.append({"ebene": ebene, "titel": titel, "zeile": i, "inhalt": "\n".join(zeilen[i + 1:naechster]),
                    "gesamt": "\n".join(zeilen[i + 1:ende])})
    return erg


def finde(abschn: list[dict], muster: str) -> dict | None:
    return next((a for a in abschn if re.search(muster, a["titel"], re.I)), None)


def zahl(s: str | None) -> float | None:
    m = re.search(r"-?\d+(?:[.,]\d+)?", s or "")
    return float(m.group(0).replace(",", ".")) if m else None


def fmt(x: float | None) -> str:
    if x is None:
        return "–"
    return (f"{x:.1f}".rstrip("0").rstrip(".") if x % 1 else f"{x:.0f}").replace(".", ",")


# ───────────────────────────── Operatoren ─────────────────────────────

BEREICH = {"AFB I": ["I"], "AFB I/II": ["I", "II"], "AFB II": ["II"], "AFB II/III": ["II", "III"], "AFB III": ["III"]}


def lade_operatoren(pfad: Path) -> dict:
    """{"technik": {"ops": {op: [AFB…]}, "nicht": {…}}, "informatik": {…}} aus operatoren-epa-technik.md."""
    text = re.sub(r"<!--.*?-->", "", pfad.read_text(encoding="utf-8"), flags=re.S)

    def tabelle(abschnitt: str) -> dict:
        zeilen = [z for z in abschnitt.splitlines() if z.strip().startswith("|")]
        for i, z in enumerate(zeilen):
            kopf = zellen(z)
            if kopf and kopf[0] == "AFB I" and "AFB III" in kopf and i + 2 < len(zeilen):
                daten = zellen(zeilen[i + 2])
                return {op.strip().lower(): BEREICH[k] for k, zelle in zip(kopf, daten) if k in BEREICH
                        for op in zelle.split(",") if op.strip()}
        return {}

    def kursiv(abschnitt: str, nach: str = "") -> set[str]:
        i = abschnitt.find(nach) if nach else 0
        if i < 0:
            return set()
        m = re.search(r"\*([^*\s][^*]*)\*", abschnitt[i + len(nach):])
        return {w.strip().lower() for w in m.group(1).replace("\n", " ").split(",") if w.strip()} if m else set()

    teile = re.split(r"^## ", text, flags=re.M)
    einleitung = teile[0]
    keine = next((t for t in teile if t.startswith("Keine EPA-Operatoren")), "")
    info = next((t for t in teile if t.startswith("Berufliche Informatik")), "")
    return {"technik": {"ops": tabelle(einleitung), "nicht": kursiv(keine)},
            "informatik": {"ops": tabelle(info), "nicht": kursiv(info, "Nicht in der Liste:")}}


def operatorenpfad(angabe: str | None) -> Path:
    kandidaten = [Path(angabe)] if angabe else [HIER.parent / "references" / "operatoren-epa-technik.md",
                                                HIER.parents[1] / "_gemeinsam" / "operatoren-epa-technik.md"]
    for p in kandidaten:
        if p.is_file():
            return p
    raise SystemExit("operatoren-epa-technik.md nicht gefunden (references/ des Skills; ggf. bibliothek.py sync)")


def _schuetzen(s: str) -> str:
    for a in ABK:
        s = s.replace(a, a.replace(".", "∯"))
    return s


def saetze(text: str) -> list[str]:
    ohne_tabellen = "\n".join(z for z in text.splitlines() if not z.strip().startswith("|"))
    teile = re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ„\"(\[*])|\n\s*\n|\n(?=\s*(?:[-*+]|\d+\.)\s)", _schuetzen(ohne_tabellen))
    erg = []
    for s in teile:
        s = re.sub(r"\*\*|__|(?<![\w*])\*(?=\w)|(?<=\w)\*(?![\w*])", "", s)          # Hervorhebung
        s = re.sub(r"^\s*(?:[-*+]|\(?[a-z0-9]{1,2}[.)])\s+", "", s)                       # Listenzeichen
        s = " ".join(s.replace("∯", ".").split())
        if s:
            erg.append(s)
    return erg


IMPERATIV = re.compile(r"\b([A-Za-zÄÖÜäöüß]+)\s+Sie\b")


def infinitiv(verb: str, rest: str, ops: dict) -> str:
    v = verb.lower()
    woerter = re.findall(r"[A-Za-zÄÖÜäöüß]+", rest)
    teil = woerter[-1].lower() if woerter else ""
    if v == "nehmen" and re.search(r"\bStellung\b", rest):
        return "stellung nehmen"
    if teil in PARTIKEL and teil + v in ops:
        return teil + v
    if v in ops:
        return v
    if teil in PARTIKEL:
        return teil + v
    if v == "legen" and re.search(r"\bzugrunde\b", rest):
        return "zugrundelegen"
    return v


def auftraege(satz: str, ops: dict) -> list[tuple[int, str, bool]]:
    """(Position, Infinitiv, Imperativ-Stelle) der Sie-Verben eines Satzes. Imperativ-Stelle =
    Satzanfang, nach Komma oder nach „und/oder/sowie“; sonst eine Inversion („Dazu erhalten Sie …“)."""
    funde = []
    treffer = [m for m in IMPERATIV.finditer(satz) if m.group(1).lower() not in KEIN_VERB]
    for n, m in enumerate(treffer):
        ende = treffer[n + 1].start() if n + 1 < len(treffer) else len(satz)
        rest = re.split(r"[.;:!?]", satz[m.end():ende])[0]
        rest = re.sub(r"\s*(?:,|\bund\b|\boder\b|\bsowie\b)\s*$", "", rest.strip())
        vor = satz[:m.start()].rstrip()
        stelle = not vor or vor.endswith(",") or bool(re.search(r"\b(?:und|oder|sowie)$", vor))
        funde.append((m.start(), infinitiv(m.group(1), rest, ops), stelle))
    k = re.match(r"^\s*([A-ZÄÖÜ][a-zäöüß]+)\s+(?:und|sowie)\s+[a-zäöüß]+\s+Sie\b", satz)
    if k and k.group(1).lower() in ops:
        funde.insert(0, (0, k.group(1).lower(), True))
    return funde


def ewh_operator(text: str, ops: dict) -> tuple[str | None, bool]:
    woerter = re.findall(r"[A-Za-zÄÖÜäöüß]+", text)
    if not woerter:
        return None, True
    w = woerter[0].lower()
    if w == "stellung" and len(woerter) > 1 and woerter[1].lower() == "nehmen":
        return "stellung nehmen", True
    if w in ops:
        return w, True
    if w in UNG:
        return UNG[w], False
    return None, True


# ───────────────────────────── Schülermaterial ─────────────────────────────

AUFGABE_KOPF = re.compile(r"^\s{0,3}(?:#{1,4}\s*)?(\d+)\.\s*Aufgabe\b\s*[–\-:]?\s*(.*)$")
TEIL_KOPF = re.compile(r"^\s{0,3}(?:#{1,5}\s*)?(\d+)\.(\d+)\s+(\S.*)$")
BE_ANGABE = re.compile(r"[\[(]\s*(?:insgesamt\s+)?(\d+(?:[.,]\d+)?)\s*BE\s*[\])]|insgesamt\s+(\d+(?:[.,]\d+)?)\s*BE", re.I)
BLOCK_ENDE = re.compile(r"^\s{0,3}#\s|^\s{0,3}#{1,4}\s*(?:Anlage|Material|Hilfsmittel|B\.\s|C\.\s)", re.I)


def lies_sm(text: str, ops: dict) -> dict:
    t = bereinigt(text)
    zeilen = t.splitlines()
    aufgaben: list[Aufgabe] = []
    teil: Teil | None = None
    for z in zeilen:
        if BLOCK_ENDE.match(z) and not AUFGABE_KOPF.match(z):
            teil = None
            continue
        ma = AUFGABE_KOPF.match(z)
        if ma and (z.lstrip().startswith("#") or BE_ANGABE.search(z)):
            be = BE_ANGABE.search(ma.group(2))
            titel = BE_ANGABE.sub("", ma.group(2)).strip(" –-:")
            aufgaben.append(Aufgabe(int(ma.group(1)), titel, zahl(be.group(1) or be.group(2)) if be else None))
            teil = None
            continue
        mt = TEIL_KOPF.match(z)
        if mt and aufgaben and int(mt.group(1)) == aufgaben[-1].nummer and (z.lstrip().startswith("#") or BE_ANGABE.search(z)):
            be = BE_ANGABE.search(mt.group(3))
            teil = Teil(f"{mt.group(1)}.{mt.group(2)}", BE_ANGABE.sub("", mt.group(3)).strip(" –-:"),
                        zahl(be.group(1) or be.group(2)) if be else None)
            aufgaben[-1].teile.append(teil)
            continue
        if teil is not None:
            teil.text += z + "\n"
    for a in aufgaben:
        for tl in a.teile:
            tl.operatoren = [inf for s in saetze(tl.text) for _, inf, _ in auftraege(s, ops) if inf in ops]
    abschn = abschnitte(t)
    erste = next((i for i, z in enumerate(zeilen) if AUFGABE_KOPF.match(z) and z.lstrip().startswith("#")), None)
    vor_aufgaben = "\n".join(zeilen[:erste]) if erste is not None else t[:4000]
    thema = re.search(r"\*\*Thema:\*\*\s*(.+)|^Thema:\s*(.+)", t, re.M)
    hilfsmittel = finde(abschn, r"Hilfsmittel")
    return {"text": t, "aufgaben": aufgaben, "abschnitte": abschn, "kopf": vor_aufgaben,
            "thema": (thema.group(1) or thema.group(2)).strip() if thema else "",
            "anlagen": {m.group(1).lower() for a in abschn if (m := re.match(r"Anlage\s+(\d+[a-z]?)\b", a["titel"], re.I))},
            "hilfsmittel": bool(hilfsmittel and hilfsmittel["gesamt"].strip()),
            "situation": bool(finde(abschn, r"Handlungssituation|Ausgangssituation|Situationsbeschreibung"))}


# ───────────────────────────── Lehrermaterial ─────────────────────────────

def lies_lm(text: str, ops: dict) -> dict:
    t = bereinigt(text)
    abschn = abschnitte(t)
    lm: dict = {"text": t, "abschnitte": abschn, "kursfolge": [], "bezug": {}, "abweichend": "", "erweitert": {},
                "dateien": set(), "ewh": [], "summen": {}, "gesamt": None, "prozent": None, "massstab": None,
                "loesungen": {}, "ewh_probleme": []}
    for tab in tabellen(t):
        kopf = [z.lower() for z in tab[0]]
        if any("halbjahr" in k for k in kopf) and any("lerngebiet" in k for k in kopf):
            ih, il = next(i for i, k in enumerate(kopf) if "halbjahr" in k), next(i for i, k in enumerate(kopf) if "lerngebiet" in k)
            ist = next((i for i, k in enumerate(kopf) if "status" in k), None)
            for r in tab[1:]:
                if il < len(r) and r[il]:
                    lm["kursfolge"].append({"halbjahr": r[ih] if ih < len(r) else "", "lerngebiet": r[il],
                                            "status": (r[ist] if ist is not None and ist < len(r) else "").lower()})
    bez = finde(abschn, r"Bezug der Aufgaben")
    if bez:
        for a in abschn:
            m = re.match(r"(\d+)\.\s*Aufgabe", a["titel"])
            if m and a["zeile"] > bez["zeile"] and a["ebene"] > bez["ebene"] and a["zeile"] < bez["zeile"] + bez["gesamt"].count("\n") + 2:
                lm["bezug"][int(m.group(1))] = a["titel"] + "\n" + a["gesamt"]
    abw = finde(abschn, r"Abweichende AFB")
    lm["abweichend"] = abw["gesamt"] if abw else ""
    erw = finde(abschn, r"Erweiterte Operatoren")
    erw_text = erw["gesamt"] if erw else (t if re.search(r"Operatorenliste\s+wurde[^\n]*erweitert", t, re.I) else "")
    for tab in tabellen(erw_text):
        kopf = [z.lower() for z in tab[0]]
        if kopf and "operator" in kopf[0]:
            ia = next((i for i, k in enumerate(kopf) if "afb" in k or "anforderung" in k), len(kopf) - 1)
            for r in tab[1:]:
                bereiche = [x for x in re.findall(r"\bI{1,3}\b", r[ia] if ia < len(r) else "")]
                for op in re.split(r"[/,]", r[0]):
                    if op.strip():
                        lm["erweitert"][op.strip().lower()] = sorted(set(bereiche), key=AFB.index) or list(AFB)
    dig = finde(abschn, r"Digitales Material")
    if dig:
        lm["dateien"] = {m.group(0).lower() for m in DATEI.finditer(dig["gesamt"])}
    # Erwartungshorizont
    ewh = finde(abschn, r"^Erwartungshorizont")
    for tab in tabellen(ewh["gesamt"] if ewh else ""):
        kopf = [z.strip() for z in tab[0]]
        if not ("I" in kopf and "II" in kopf and "III" in kopf):
            continue
        i1, i2, i3 = kopf.index("I"), kopf.index("II"), kopf.index("III")
        isum = next((i for i, k in enumerate(kopf) if k in ("Σ", "∑", "Summe", "BE")), None)
        itext = next((i for i, k in enumerate(kopf) if re.search(r"erwartet|leistung", k, re.I)), 1)
        akt = None
        for r in tab[1:]:
            r = r + [""] * (len(kopf) - len(r))
            label = r[0] or r[itext]
            werte = {"I": zahl(r[i1]) or 0.0, "II": zahl(r[i2]) or 0.0, "III": zahl(r[i3]) or 0.0}
            s = zahl(r[isum]) if isum is not None else None
            voll = all(zahl(r[i]) is not None for i in (i1, i2, i3, isum) if i is not None) and isum is not None
            m = re.match(r"Summen?\s+(?:(\d+)\.\s*Aufgabe|Aufgabe\s+(\d+))", label, re.I)
            if m:
                lm["summen"][int(m.group(1) or m.group(2))] = {**werte, "S": s, "voll": voll}
            elif re.match(r"Gesamtsummen?", label, re.I) and ("prozent" in label.lower() or "%" in " ".join(r[1:])):
                lm["prozent"] = {**werte, "S": s}
            elif re.match(r"Gesamtsummen?", label, re.I):
                lm["gesamt"] = {**werte, "S": s, "voll": voll}
            elif re.fullmatch(r"\d+\.\d+", r[0]):
                akt = r[0]
                op, subst = ewh_operator(r[itext], ops)
                lm["ewh"].append(EwhZeile(akt, r[itext], werte, s, op, subst))
            elif not r[0] and akt and r[itext]:
                op, subst = ewh_operator(r[itext], ops)
                lm["ewh"].append(EwhZeile(akt, r[itext], werte, s, op, subst))
            elif any(r):
                lm["ewh_probleme"].append(label or " | ".join(r))
        break
    # Bewertungsmaßstab
    mass = finde(abschn, r"Bewertungsma(ß|ss)stab|Umrechnung")
    for tab in tabellen(mass["gesamt"] if mass else ""):
        prozent = next((r for r in tab if re.search(r"prozent", r[0], re.I)), None)
        be = next((r for r in tab if re.search(r"\bBE\b", r[0])), None)
        if prozent:
            lm["massstab"] = {"prozent": [zahl(x) for x in prozent[1:] if x.strip()],
                              "be": [zahl(x) for x in be[1:] if x.strip()] if be else None}
            break
    # Musterlösung: Lösungsvorschläge mit Merkmaltabelle
    for a in abschn:
        m = re.search(r"Lösungsvorschlag\s+zur\s+Teilaufgabe\s+(\d+\.\d+)", a["titel"], re.I)
        if not m:
            continue
        merkmale = []
        for tab in tabellen(a["gesamt"]):
            kopf = [z.lower() for z in tab[0]]
            if any("merkmal" in k for k in kopf) and "be" in kopf:
                ib, im = kopf.index("be"), next(i for i, k in enumerate(kopf) if "merkmal" in k)
                ia = next((i for i, k in enumerate(kopf) if k == "art"), None)
                iafb = next((i for i, k in enumerate(kopf) if k == "afb"), None)
                for r in tab[1:]:
                    r = r + [""] * (len(kopf) - len(r))
                    if re.match(r"^(?:Σ|∑|Summe)", r[0] or r[im], re.I) or zahl(r[ib]) is None:
                        continue
                    merkmale.append(Merkmal(r[0], r[im], (r[ia] if ia is not None else "").strip().lower(),
                                            (r[iafb] if iafb is not None else "").strip().upper(), zahl(r[ib])))
        lm["loesungen"][m.group(1)] = {"text": a["gesamt"], "merkmale": merkmale}
    return lm


# ───────────────────────────── Hilfsrechnungen ─────────────────────────────

def grenzen(gesamt: float) -> list[tuple[str, int, float]]:
    """(Notenpunkte, ab Prozent, ab BE) – auf halbe BE aufgerundet (wie notenschluessel.md)."""
    return [(p, proz, math.ceil(round(proz / 100 * gesamt * 2, 6)) / 2) for proz, p in NOTEN]


def lerngebiete_in(text: str, codes: list[str]) -> set[str]:
    norm = lambda s: re.sub(r"\s+", "", s).upper()
    gefunden = {norm(c) for c in codes if c and re.search(rf"(?<![\w]){re.escape(c)}(?![\w])", text)}
    gefunden |= {norm(m) for m in re.findall(r"\b(?:BT|ET|IT|MT|METRO|GMT|ING)\s?[1-6]\b", text)}
    return gefunden


def platzhalter(text: str) -> list[str]:
    funde = [name for muster, name in PLATZHALTER if re.search(muster, text)]
    klammern = []
    for m in re.finditer(r"\[([^\]\n]{1,80})\](?!\()", text):
        inhalt = m.group(1).strip()
        if (not inhalt or inhalt.lower() in ("x", " ") or re.fullmatch(r"[\d\s.,;:–\-…]+", inhalt)
                or re.fullmatch(r"\d+(?:[.,]\d+)?\s*BE", inhalt) or inhalt.lower() in EINHEITEN
                or re.search(r"[<>≤≥≠]|(?<![:!<>])=", inhalt)):     # Vergleich im GRAFCET: [-BT1 > −16 °C]
            continue
        klammern.append(f"[{inhalt[:30]}]")
    if klammern:
        funde.append("Vorlagenklammern " + ", ".join(sorted(set(klammern))[:6]) + (" …" if len(set(klammern)) > 6 else ""))
    return funde


# ───────────────────────────── Prüfung ─────────────────────────────

def pruefe(sm_text: str, lm_text: str, opdaten: dict, fach: str | None = None, zeit: float | None = None,
           be_soll: float | None = None, basis_sm: Path | None = None,
           basis_lm: Path | None = None) -> tuple[list[Befund], dict, dict, dict]:
    """basis_sm/basis_lm: Ordner der Dateien – dann werden eingebundene SVG mitgeprüft (Z)."""
    if fach is None:
        fach = "informatik" if re.search(r"Berufliche\s+Informatik|\|\s*Informatik\b", bereinigt(sm_text)[:800]) else "technik"
    ops = opdaten[fach]["ops"]
    nicht = opdaten[fach]["nicht"]
    sm, lm = lies_sm(sm_text, ops), lies_lm(lm_text, ops)
    befunde: list[Befund] = []
    B = lambda k, n, s, t: befunde.append(Befund(k, n, s, t))
    teile = [tl for a in sm["aufgaben"] for tl in a.teile]
    info: dict = {"fach": fach, "aufgaben": len(sm["aufgaben"]), "teilaufgaben": len(teile)}

    # 1.3 Kopf
    kopf = sm["kopf"]
    fehlt = []
    if not re.search(r"Abitur\s+(?:20\d\d)\b", kopf):
        fehlt.append("Abitur mit Jahr")
    if not re.search(r"Technik\s*[–-]\s*[A-ZÄÖÜ]|Berufliche Informatik|Informatik", kopf):
        fehlt.append("Fach mit Schwerpunkt")
    if not re.search(r"Schülermaterial|Material für Prüflinge", kopf):
        fehlt.append("„Schülermaterial“")
    vorschlag = re.search(r"Vorschlag\s+([A-Z])\b", kopf)
    if not vorschlag:
        fehlt.append("Vorschlag A/B")
    if not re.search(r"\b[eg]A\b", kopf):
        fehlt.append("eA/gA")
    mz = re.search(r"Bearbeitungszeit:?\s*(\d+)\s*(?:min|Min)", kopf)
    if not mz:
        fehlt.append("Bearbeitungszeit")
    lm_kopf = lm["text"][:1500]
    lm_fehlt = [w for w, rx in (("„Lehrermaterial“", r"Lehrermaterial|Erwartungshorizont"),
                                ("Vorschlag", r"Vorschlag\s+[A-Z]\b"), ("Abitur mit Jahr", r"Abitur\s+20\d\d\b")) if not re.search(rx, lm_kopf)]
    if vorschlag and re.search(r"Vorschlag\s+([A-Z])\b", lm_kopf) and re.search(r"Vorschlag\s+([A-Z])\b", lm_kopf).group(1) != vorschlag.group(1):
        lm_fehlt.append("Vorschlag im LM weicht ab")
    B("1.3", "Kopf vollständig (Jahr, Fach/Schwerpunkt, Vorschlag, eA, Zeit)", "❌" if fehlt else ("⚠" if lm_fehlt else "✅"),
      ("Schülermaterial ohne " + ", ".join(fehlt) if fehlt else "") + (("; " if fehlt else "") + "Lehrermaterial ohne " + ", ".join(lm_fehlt) if lm_fehlt else "")
      or "vollständig")
    info["vorschlag"] = vorschlag.group(1) if vorschlag else None

    # 3.3 Handlungssituation, 2.7 Hilfsmittel
    B("3.3", "Handlungssituation", "✅" if sm["situation"] else "⚠",
      "Abschnitt vorhanden" if sm["situation"] else "kein Abschnitt „Handlungssituation“ – ganzheitliche Situation beschreiben")
    B("2.7", "Hilfsmittel benannt", "✅" if sm["hilfsmittel"] else "❌",
      "Abschnitt vorhanden" if sm["hilfsmittel"] else "kein Abschnitt „Hilfsmittel“ mit Inhalt im Schülermaterial")

    # 2.2/2.3 Kursfolge und Bezug
    codes = [k["lerngebiet"] for k in lm["kursfolge"]]
    probleme, kurz = [], []
    if not lm["kursfolge"]:
        probleme.append("keine Kursfolge-Tabelle (Halbjahr | Lerngebiet | Titel | Status)")
    lg_je_aufgabe: dict[int, set[str]] = {}
    for a in sm["aufgaben"]:
        txt = lm["bezug"].get(a.nummer)
        if not txt:
            probleme.append(f"kein Bezug zum Unterricht für die {a.nummer}. Aufgabe")
            continue
        woerter = len(re.findall(r"\w+", txt))
        lg_je_aufgabe[a.nummer] = lerngebiete_in(txt, codes)
        if woerter < 40:
            kurz.append(f"{a.nummer}. Aufgabe ({woerter} Wörter)")
        if not lg_je_aufgabe[a.nummer]:
            kurz.append(f"{a.nummer}. Aufgabe ohne Lerngebiet")
    B("2.3", "Unterrichtszusammenhang konkret (Kursfolge, Bezug je Aufgabe)", "❌" if probleme else ("⚠" if kurz else "✅"),
      "; ".join(probleme + (["knapp: " + ", ".join(kurz)] if kurz else [])) or
      f"Kursfolge mit {len(lm['kursfolge'])} Halbjahren, Bezug für alle Aufgaben")
    if lm["kursfolge"]:
        soll = {re.sub(r"\s+", "", k["lerngebiet"]).upper() for k in lm["kursfolge"]
                if re.search(r"verbindlich|optional", k["status"])}
        abgedeckt = set().union(*lg_je_aufgabe.values()) if lg_je_aufgabe else set()
        fehlen = sorted(soll - abgedeckt)
        B("3.2", "verbindliche und gewähltes optionales Lerngebiet geprüft", "⚠" if fehlen else "✅",
          ("nicht im Bezug einer Aufgabe genannt: " + ", ".join(fehlen)) if fehlen else "alle abgedeckt: " + ", ".join(sorted(soll)))
        einzeln = [f"{n}. Aufgabe ({', '.join(sorted(v)) or '–'})" for n, v in sorted(lg_je_aufgabe.items()) if len(v) < 2]
        B("X.14", "jede Aufgabe verbindet ≥ 2 Lerngebiete", "⚠" if einzeln else "✅",
          ("nur ein Lerngebiet: " + ", ".join(einzeln)) if einzeln else "erfüllt")

    # X.10 Summen im Schülermaterial
    abw = []
    for a in sm["aufgaben"]:
        s = sum(tl.be or 0 for tl in a.teile)
        if a.be is None:
            abw.append(f"{a.nummer}. Aufgabe ohne BE-Angabe")
        elif any(tl.be is None for tl in a.teile):
            abw.append(f"{a.nummer}. Aufgabe: Teilaufgabe ohne BE (" + ", ".join(tl.nummer for tl in a.teile if tl.be is None) + ")")
        elif abs(s - a.be) > 1e-6:
            abw.append(f"{a.nummer}. Aufgabe: Teilaufgaben {fmt(s)} ≠ angegeben {fmt(a.be)}")
    gesamt_sm = sum(a.be or 0 for a in sm["aufgaben"])
    info["gesamt_sm"] = gesamt_sm

    # Erwartungshorizont rechnen
    ewh = lm["ewh"]
    je_teil: dict[str, dict] = {}
    for z in ewh:
        d = je_teil.setdefault(z.teil, {"I": 0.0, "II": 0.0, "III": 0.0, "S": None, "ops": [], "zeilen": 0})
        for k in AFB:
            d[k] += z.afb[k]
        if z.summe is not None and d["S"] is None:
            d["S"] = z.summe
        d["zeilen"] += 1
        if z.operator:
            d["ops"].append(z.operator)
    rechnung = []
    for nr, d in je_teil.items():
        zeilen_summe = d["I"] + d["II"] + d["III"]
        if d["S"] is None:
            rechnung.append(f"{nr}: Σ fehlt")
        elif abs(zeilen_summe - d["S"]) > 1e-6:
            rechnung.append(f"{nr}: Zeilen {fmt(zeilen_summe)} ≠ Σ {fmt(d['S'])}")
    afb_aufgabe: dict[int, dict] = {}
    for nr, d in je_teil.items():
        a = afb_aufgabe.setdefault(int(nr.split(".")[0]), {"I": 0.0, "II": 0.0, "III": 0.0})
        for k in AFB:
            a[k] += d[k]
    for n, s in lm["summen"].items():
        ist = afb_aufgabe.get(n, {"I": 0.0, "II": 0.0, "III": 0.0})
        diff = [f"{k}: {fmt(s[k])} ≠ {fmt(ist[k])}" for k in AFB if abs(s[k] - ist[k]) > 1e-6]
        if not s["voll"]:
            diff.append("Summenzeile ohne alle vier Zahlen (auch 0 eintragen)")
        elif abs(s["S"] - sum(ist.values())) > 1e-6:
            diff.append(f"Σ {fmt(s['S'])} ≠ {fmt(sum(ist.values()))}")
        if diff:
            rechnung.append(f"Summen {n}. Aufgabe: " + ", ".join(diff))
    fehlende_summen = [a.nummer for a in sm["aufgaben"] if a.nummer not in lm["summen"]]
    if fehlende_summen:
        rechnung.append("Summenzeile fehlt für " + ", ".join(f"{n}. Aufgabe" for n in fehlende_summen))
    tot = {k: sum(d[k] for d in je_teil.values()) for k in AFB}
    gesamt_lm = sum(tot.values())
    info["gesamt_lm"] = gesamt_lm
    if lm["gesamt"] is None:
        rechnung.append("Zeile „Gesamtsummen (absolut)“ fehlt")
    else:
        g = lm["gesamt"]
        diff = [f"{k}: {fmt(g[k])} ≠ {fmt(tot[k])}" for k in AFB if abs(g[k] - tot[k]) > 1e-6]
        if not g["voll"]:
            diff.append("nicht alle vier Zahlen eingetragen")
        if g["S"] is None or abs(g["S"] - gesamt_lm) > 1e-6:
            diff.append(f"Σ {fmt(g['S'])} ≠ {fmt(gesamt_lm)}")
        if diff:
            rechnung.append("Gesamtsummen: " + ", ".join(diff))
    if lm["prozent"] and gesamt_lm:
        diff = [f"{k}: {fmt(lm['prozent'][k])} % ≠ {100 * tot[k] / gesamt_lm:.1f} %".replace(".", ",") for k in AFB
                if abs(lm["prozent"][k] - 100 * tot[k] / gesamt_lm) > 1.0]
        if diff:
            rechnung.append("Gesamtsummen (prozentual): " + ", ".join(diff))
    if lm["ewh_probleme"]:
        rechnung.append("nicht zuordenbare Zeilen: " + "; ".join(lm["ewh_probleme"][:3]))
    B("X.10", "Summen stimmig (Schülermaterial, Erwartungshorizont)", "❌" if abw or rechnung else "✅",
      "; ".join(abw + rechnung) or "Teilaufgaben → Aufgaben → Gesamtsummen → Prozent stimmen")

    # X.13 SM = LM
    abw = []
    for tl in teile:
        d = je_teil.get(tl.nummer)
        if d is None:
            abw.append(f"{tl.nummer} fehlt im Erwartungshorizont")
        elif tl.be is not None and abs((d["S"] if d["S"] is not None else d["I"] + d["II"] + d["III"]) - tl.be) > 1e-6:
            abw.append(f"{tl.nummer}: SM {fmt(tl.be)} ≠ LM {fmt(d['S'] if d['S'] is not None else d['I'] + d['II'] + d['III'])}")
    zusatz = sorted(set(je_teil) - {tl.nummer for tl in teile})
    if zusatz:
        abw.append("nur im Erwartungshorizont: " + ", ".join(zusatz))
    if abs(gesamt_sm - gesamt_lm) > 1e-6:
        abw.append(f"gesamt: SM {fmt(gesamt_sm)} ≠ LM {fmt(gesamt_lm)}")
    B("X.13", "BE Schülermaterial = Erwartungshorizont", "❌" if abw else "✅", "; ".join(abw) or f"je Teilaufgabe stimmig, gesamt {fmt(gesamt_sm)} BE")

    # 4.3 Gesamt-BE, X.7 Takt
    soll = be_soll if be_soll is not None else 120.0
    B("4.3", "Gesamtumfang wie vorgegeben", "✅" if abs(gesamt_sm - soll) < 1e-6 else "❌",
      f"{fmt(gesamt_sm)} BE (Vorgabe {fmt(soll)} BE)")
    zeit_ist = zeit or (float(mz.group(1)) if mz else None)
    info["zeit"] = zeit_ist
    if zeit_ist and gesamt_sm:
        takt = zeit_ist / gesamt_sm
        info["takt"] = round(takt, 2)
        status = "✅" if TAKT_GUT[0] <= takt <= TAKT_GUT[1] else ("⚠" if TAKT_VERTRETBAR[0] <= takt <= TAKT_VERTRETBAR[1] else "❌")
        B("X.7", "Bearbeitungszeit je BE", status,
          f"{fmt(zeit_ist)} min / {fmt(gesamt_sm)} BE = {takt:.2f} min je BE (Richtbereich 2,5–3,0, vertretbar 2,0–3,5)".replace(".", ","))
    else:
        B("X.7", "Bearbeitungszeit je BE", "➖", "Bearbeitungszeit oder BE nicht erkannt")
    gross = [f"{tl.nummer} ({fmt(tl.be)} BE)" for tl in teile if tl.be is not None and not 2 <= tl.be <= 20]
    if not 2 <= len(sm["aufgaben"]) <= 4 or gross:
        B("4.3", "Gliederung (2–4 Aufgaben, Teilaufgaben 2–20 BE)", "⚠",
          "; ".join(([f"{len(sm['aufgaben'])} Aufgaben"] if not 2 <= len(sm["aufgaben"]) <= 4 else []) +
                    (["Teilaufgaben außerhalb 2–20 BE: " + ", ".join(gross)] if gross else [])))

    # 2.4, 4.6, je Aufgabe, X.1, X.5
    leer = [f"{z.teil} „{z.text[:30]}“" for z in ewh if not any(z.afb[k] for k in AFB)]
    B("2.4", "Erwartungshorizont mit AFB je Zeile", "❌" if leer or not ewh else "✅",
      ("Zeilen ohne BE: " + "; ".join(leer[:5])) if leer else ("kein Erwartungshorizont (Tabelle mit Spalten I, II, III) gefunden" if not ewh else f"{len(ewh)} Zeilen mit AFB"))
    if gesamt_lm:
        proz = {k: 100 * tot[k] / gesamt_lm for k in AFB}
        info["afb"] = {k: round(v, 1) for k, v in proz.items()}
        aus10 = [k for k in AFB if abs(proz[k] - AFB_ZIEL[k]) > 10]
        aus5 = [k for k in AFB if abs(proz[k] - AFB_ZIEL[k]) > 5]
        B("4.6", "AFB-Verteilung gesamt (Ziel 30/40/30)", "❌" if aus10 else ("⚠" if aus5 else "✅"),
          " · ".join(f"AFB {k} {fmt(tot[k])} ({proz[k]:.0f} %)" for k in AFB) +
          (f" – außerhalb ±10: {', '.join(aus10)}" if aus10 else (f" – außerhalb ±5: {', '.join(aus5)}" if aus5 else "")))
        luecken = [f"{n}. Aufgabe ohne AFB {k}" for n, d in sorted(afb_aufgabe.items()) for k in AFB if d[k] == 0]
        B("4.6", "je Aufgabe alle drei AFB", "❌" if luecken else "✅", "; ".join(luecken) or "in jeder Aufgabe I, II und III")
    if teile:
        erste = [z for z in ewh if z.teil == teile[0].nummer]
        if erste:
            nur3 = all(z.afb["I"] == 0 and z.afb["II"] == 0 for z in erste)
            ohne1 = sum(z.afb["I"] for z in erste) == 0
            B("X.1", "erste Teilaufgabe nicht AFB III", "❌" if nur3 else ("⚠" if ohne1 else "✅"),
              f"{teile[0].nummer}: " + ("nur AFB III" if nur3 else ("ohne AFB I – Einstieg mit AFB I empfohlen" if ohne1 else "Einstieg mit AFB I")))
    abweichend_ops = {op for op in list(ops) + list(lm["erweitert"]) if re.search(rf"\b{re.escape(op)}", lm["abweichend"], re.I)}
    fehlzu, begruendet, nachbar, ohne_op, nominal = [], [], [], [], []
    for z in ewh:
        belegt = [k for k in AFB if z.afb[k]]
        if belegt in (["I", "III"], ["I", "II", "III"]):
            nachbar.append(f"{z.teil} „{z.text[:25]}“ ({'/'.join(belegt)})")
        if not z.operator:
            ohne_op.append(f"{z.teil} „{z.text[:25]}“")
            continue
        if not z.substantiv:
            nominal.append(f"{z.teil} „{z.text.split()[0]}“")
        bereich = ops.get(z.operator) or lm["erweitert"].get(z.operator)
        if bereich and any(k not in bereich for k in belegt):
            eintrag = f"{z.teil} {z.operator} (AFB {'/'.join(belegt)}, Liste {'/'.join(bereich)})"
            (begruendet if z.operator in abweichend_ops else fehlzu).append(eintrag)
    text = []
    if fehlzu:
        text.append("AFB außerhalb des Operatorbereichs: " + "; ".join(fehlzu))
    if nachbar:
        text.append("mehr als zwei bzw. nicht benachbarte AFB in einer Zeile: " + "; ".join(nachbar))
    if begruendet:
        text.append("abweichend, im Lehrermaterial begründet: " + "; ".join(begruendet))
    B("X.5", "AFB je Zeile im Bereich des Operators", "❌" if fehlzu or nachbar else ("⚠" if begruendet else "✅"),
      "; ".join(text) or "alle Zeilen im Operatorbereich")
    text = []
    if ohne_op:
        text.append("Zeile beginnt nicht mit einem Operator: " + "; ".join(ohne_op[:6]))
    if nominal:
        text.append("Nominalform statt substantiviertem Infinitiv („Berechnen der …“): " + ", ".join(nominal[:6]))
    unterschied = []
    for tl in teile:
        d = je_teil.get(tl.nummer)
        if d and set(tl.operatoren) != set(d["ops"]):
            unterschied.append(f"{tl.nummer}: SM {', '.join(sorted(set(tl.operatoren))) or '–'} / EWH {', '.join(sorted(set(d['ops']))) or '–'}")
    if unterschied:
        text.append("Operatoren verschieden: " + "; ".join(unterschied[:6]))
    B("X.4", "Operatoren in Schülermaterial und Erwartungshorizont gleich", "⚠" if text else "✅",
      "; ".join(text) or "gleich, substantiviert")

    # 4.4/4.5/X.2/X.9/K.7 Aufträge
    ohne, fremd, x9, k7 = [], [], [], []
    for tl in teile:
        if not tl.operatoren:
            ohne.append(tl.nummer)
        for s in saetze(tl.text):
            funde = auftraege(s, ops)
            op_funde = [(p, inf, st) for p, inf, st in funde if inf in ops]
            for _, inf, stelle in funde:
                if inf in ops or inf in HINWEIS or (fach == "informatik" and inf in FORMAT_INFORMATIK) or not stelle:
                    continue
                if inf in X9:
                    x9.append(f"{tl.nummer}: {X9[inf]}")
                else:
                    fremd.append((tl.nummer, inf))
            if len({inf for _, inf, _ in op_funde}) >= 2:
                k7.append(f"{tl.nummer}: zwei Operatoren in einem Satz ({', '.join(dict.fromkeys(i for _, i, _ in op_funde))})")
            if op_funde and not op_funde[0][2]:
                k7.append(f"{tl.nummer}: Operator nicht am Satzanfang („{s[:40]}…“)")
            if op_funde and VAGE.search(s):
                k7.append(f"{tl.nummer}: „{VAGE.search(s).group(0)}“")
            if op_funde and KRITERIENLOS.search(s) and not KRITERIUM_DA.search(s):
                k7.append(f"{tl.nummer}: „{KRITERIENLOS.search(s).group(0)}“ ohne Kriterium")
            mehrzahl = PLURAL.search(s)
            if op_funde and mehrzahl and not ZAHLWORT.search(s) and not AUFZAEHLUNG.match(s[mehrzahl.end():]):
                k7.append(f"{tl.nummer}: Umfang offen („{mehrzahl.group(0)}“ ohne Zahlwort)")
            if s.rstrip().endswith("?"):
                k7.append(f"{tl.nummer}: Frage statt Arbeitsauftrag")
            if op_funde and len(s.split()) > 45:
                k7.append(f"{tl.nummer}: Auftragssatz mit {len(s.split())} Wörtern")
    B("4.4", "Arbeitsauftrag mit Listenoperator im Imperativ „Sie“", "❌" if ohne else "✅",
      ("kein Operator der Liste in: " + ", ".join(ohne)) if ohne else "jede Teilaufgabe hat einen Operator")
    dok = [f"{n}: {v}" for n, v in fremd if v in lm["erweitert"]]
    undok = [f"{n}: {v}" + (" (keine EPA-Operator)" if v in nicht else "") for n, v in fremd if v not in lm["erweitert"]]
    B("4.5", "nur Operatoren der Liste (sonst als erweitert dokumentiert)", "❌" if undok else ("⚠" if dok else "✅"),
      "; ".join((["nicht in der Liste, nicht dokumentiert: " + ", ".join(undok)] if undok else []) +
                (["erweiterte Operatoren (im LM dokumentiert, X.2): " + ", ".join(dok)] if dok else [])) or "nur Listenoperatoren")
    B("X.9", "keine Nicht-Operator-Formulierungen", "⚠" if x9 else "✅", "; ".join(dict.fromkeys(x9)) or "keine gefunden")

    # X.3 Punkte, S.1–S.4
    n_punkte = len(re.findall(r"\b\d+\s*(?:Punkte?|Pkt\.?)(?![\w])", sm["text"]))
    B("X.3", "„BE“ statt „Punkte“", "❌" if n_punkte else "✅", f"{n_punkte}× „Punkte“ im Schülermaterial" if n_punkte else "durchgängig BE")
    ph = [f"SM {x}" for x in platzhalter(sm["text"])] + [f"LM {x}" for x in platzhalter(lm["text"])]
    B("S.1", "keine offenen Platzhalter", "❌" if ph else "✅", "; ".join(ph) or "keine")
    verweise = {m.group(1).lower() for m in ANLAGE_VERWEIS.finditer(sm["text"])}
    fehlend = sorted(v for v in verweise if v not in sm["anlagen"])
    B("S.2", "angekündigte Anlagen vorhanden", "❌" if fehlend else "✅",
      ("ohne eigenen Abschnitt: " + ", ".join(f"Anlage {v}" for v in fehlend)) if fehlend else
      (f"{len(sm['anlagen'])} Anlagen vorhanden – Bildinhalte von Hand prüfen" if sm["anlagen"] else "keine Anlagen angekündigt"))
    dateien = {m.group(0).lower() for m in DATEI.finditer(sm["text"])}
    ungelistet = sorted(dateien - lm["dateien"])
    B("S.3", "referenzierte Dateien im Lehrermaterial gelistet", "⚠" if ungelistet else "✅",
      ("nicht unter „Digitales Material“: " + ", ".join(ungelistet[:8])) if ungelistet else
      ("alle gelistet – den Prüfungsunterlagen beilegen" if dateien else "keine Dateien referenziert"))
    nb = []
    if [a.nummer for a in sm["aufgaben"]] != list(range(1, len(sm["aufgaben"]) + 1)):
        nb.append("Aufgaben nicht fortlaufend: " + ", ".join(str(a.nummer) for a in sm["aufgaben"]))
    for a in sm["aufgaben"]:
        subs = [int(tl.nummer.split(".")[1]) for tl in a.teile]
        if subs != list(range(1, len(subs) + 1)):
            nb.append(f"{a.nummer}. Aufgabe: " + ", ".join(tl.nummer for tl in a.teile))
    if not sm["aufgaben"]:
        nb.append("keine Aufgaben erkannt (Format „## N. Aufgabe – Titel (insgesamt n BE)“)")
    B("S.4", "Nummerierung lückenlos", "❌" if nb else "✅", "; ".join(nb) or "lückenlos")

    # 2.5 Lösungsvorschläge, K.1–K.6, K.8
    ohne_loesung = [tl.nummer for tl in teile if tl.nummer not in lm["loesungen"]]
    B("2.5", "Lösungsvorschlag je Teilaufgabe", "❌" if ohne_loesung else "✅",
      ("fehlt für: " + ", ".join(ohne_loesung)) if ohne_loesung else "vollständig")
    k1, k2, k3, k4, k5, k6, arten_fehlen = [], [], [], [], [], [], []
    anteile = {"fest": 0.0, "kriterium": 0.0, "urteil": 0.0}
    for tl in teile:
        loes = lm["loesungen"].get(tl.nummer)
        if not loes:
            continue
        mm = loes["merkmale"]
        if not mm:
            k1.append(tl.nummer)
            continue
        summe = sum(m.be for m in mm)
        soll_be = tl.be if tl.be is not None else (je_teil.get(tl.nummer) or {}).get("S")
        if soll_be is not None and abs(summe - soll_be) > 1e-6:
            k2.append(f"{tl.nummer}: Merkmale {fmt(summe)} ≠ {fmt(soll_be)} BE")
        d = je_teil.get(tl.nummer)
        if d:
            je_afb = {k: sum(m.be for m in mm if m.afb == k) for k in AFB}
            if any(m.afb not in AFB for m in mm):
                k2.append(f"{tl.nummer}: Merkmal ohne AFB (I, II oder III)")
            elif any(abs(je_afb[k] - d[k]) > 1e-6 for k in AFB):
                k2.append(f"{tl.nummer}: AFB der Merkmale {'/'.join(fmt(je_afb[k]) for k in AFB)} ≠ EWH {'/'.join(fmt(d[k]) for k in AFB)}")
        for m in mm:
            if m.be > MERKMAL_MAX:
                k3.append(f"{tl.nummer} Nr. {m.nr}: {fmt(m.be)} BE")
            if WERTWORT.search(m.text):
                k3.append(f"{tl.nummer} Nr. {m.nr}: „{WERTWORT.search(m.text).group(0)}“")
            if m.art in anteile:
                anteile[m.art] += m.be
            else:
                arten_fehlen.append(f"{tl.nummer} Nr. {m.nr}")
        text_l = loes["text"]
        if set(tl.operatoren) & RECHNEN and not re.search(r"Toleranz|Rundung|gerundet|runden", text_l, re.I):
            k4.append(tl.nummer)
        if set(tl.operatoren) & OFFEN[fach] and (not re.search(r"Gleichwertig", text_l, re.I)
                                                 or not any(m.art in ("kriterium", "urteil") for m in mm)):
            k5.append(tl.nummer)
        if ERSATZWERT.search(tl.text) and not re.search(r"Folgefehler", text_l, re.I):
            k6.append(tl.nummer)
    B("K.1", "Merkmaltabelle je Teilaufgabe", "❌" if k1 else ("➖" if not lm["loesungen"] else "✅"),
      ("ohne Merkmaltabelle: " + ", ".join(k1)) if k1 else "jede BE an einem Merkmal")
    B("K.2", "Merkmale = BE der Teilaufgabe und AFB des Erwartungshorizonts", "❌" if k2 else "✅", "; ".join(k2) or "stimmig")
    B("K.3", "Merkmale ≤ 3 BE, beobachtbar formuliert", "⚠" if k3 else "✅", "; ".join(k3[:8]) or "erfüllt")
    B("K.4", "Rechnung und Auswahl mit Toleranz bzw. Rundung", "⚠" if k4 else "✅",
      ("ohne Toleranz/Rundung: " + ", ".join(k4)) if k4 else "angegeben")
    B("K.5", "offene Aufgaben mit Alternativen und funktionalen Merkmalen", "⚠" if k5 else "✅",
      ("ohne „Gleichwertig“ oder ohne Merkmal der Art Kriterium/Urteil: " + ", ".join(k5)) if k5 else "angegeben")
    B("K.6", "Ersatzwert mit Folgefehlerregel", "⚠" if k6 else "✅",
      ("Ersatzwert ohne Folgefehlerregel: " + ", ".join(k6)) if k6 else "stimmig")
    B("K.7", "eindeutige Aufträge (ein Operator je Satz, Zahlwort, keine vagen Wörter)", "⚠" if k7 else "✅",
      "; ".join(list(dict.fromkeys(k7))[:10]) + (f" (+{len(set(k7)) - 10})" if len(set(k7)) > 10 else "") if k7 else "keine Befunde")
    summe_art = sum(anteile.values())
    if summe_art:
        urteil = 100 * anteile["urteil"] / summe_art
        info["arten"] = {k: round(100 * v / summe_art, 1) for k, v in anteile.items()}
        B("K.8", "Anteil „Urteil“ (Richtwert ≤ 30 %)", "⚠" if urteil > URTEIL_GRENZE or arten_fehlen else "✅",
          " · ".join(f"{k} {100 * v / summe_art:.0f} %" for k, v in anteile.items()) +
          (f"; Art fehlt bzw. unbekannt: {', '.join(arten_fehlen[:6])}" if arten_fehlen else ""))
    sm_bez = set(re.findall(r"`([^`\n]{1,40})`", sm["text"]))
    lm_bez = set(re.findall(r"`([^`\n]{1,40})`", lm["text"]))
    abw = sorted({f"{b} ≠ {s}" for b in lm_bez for s in sm_bez if b != s and b.lower() == s.lower()})
    B("K.9", "Bezeichner in SM und LM gleich geschrieben", "⚠" if abw else "✅", "; ".join(abw[:6]) or "gleich")

    # 2.6 Bewertungsmaßstab
    if not lm["massstab"]:
        B("2.6", "Bewertungsmaßstab (Notenpunkte)", "❌", "keine Tabelle mit Zeile „ab Prozent“ unter „Bewertungsmaßstab“")
    else:
        soll_p = [float(p) for p, _ in NOTEN]
        abw_p = lm["massstab"]["prozent"] != soll_p
        be_ist = lm["massstab"]["be"]
        be_soll_liste = [g for _, _, g in grenzen(gesamt_lm or gesamt_sm)]
        abw_be = bool(be_ist) and [round(x or 0, 1) for x in be_ist] != [round(x, 1) for x in be_soll_liste]
        B("2.6", "Bewertungsmaßstab (Notenpunkte)", "❌" if abw_be else ("⚠" if abw_p else "✅"),
          ("BE-Grenzen weichen von der Rechnung ab (siehe Tabelle unten)" if abw_be else "") +
          ("; " if abw_be and abw_p else "") + ("Prozentgrenzen weichen vom Maßstab 95 … 33/27/20 % ab" if abw_p else "") or
          ("Prozent und BE-Grenzen stimmen" if be_ist else "Prozentgrenzen stimmen; Zeile „ab BE“ ergänzen"))

    # T – Betriebsmittelkennzeichen
    bmk_info = {}
    if pruefe_bmk is not None:
        tb, bmk_info = pruefe_bmk(sm_text, lm_text)
        if not (len(tb) == 1 and tb[0].status == "➖"):
            befunde += [Befund(b.kriterium, b.name, b.status, b.befund) for b in tb]
    else:
        B("T", "Betriebsmittelkennzeichen", "➖", "bmk_pruefen.py fehlt im Ordner scripts/ (bibliothek.py sync)")

    # Z – Zeichnungen als SVG (Skill-Vertrag Abschn. 3)
    if pruefe_zeichnungen is not None:
        for nr, name, text, basis in (("Z.1", "Schülermaterial", sm_text, basis_sm),
                                      ("Z.2", "Lehrermaterial", lm_text, basis_lm)):
            stufe, hinweis, _ = pruefe_zeichnungen(text, basis=basis)
            B(nr, f"Zeichnungen als SVG ({name})", stufe, hinweis)
    else:
        B("Z", "Zeichnungen als SVG", "➖", "zeichnungen_pruefen.py fehlt im Ordner scripts/ (bibliothek.py sync)")

    info["afb_summen"] = tot
    modell = {"sm": sm, "lm": lm, "je_teil": je_teil, "tot": tot, "bmk": bmk_info}
    return befunde, info, modell, {"lg": set().union(*lg_je_aufgabe.values()) if lg_je_aufgabe else set()}


# ───────────────────────────── Vergleich A/B ─────────────────────────────

def vergleiche(info_a: dict, mod_a: dict, zus_a: dict, info_b: dict, mod_b: dict, zus_b: dict) -> list[Befund]:
    befunde = []
    schwer = []
    if abs(info_a["gesamt_sm"] - info_b["gesamt_sm"]) > 1e-6:
        schwer.append(f"BE {fmt(info_a['gesamt_sm'])} ≠ {fmt(info_b['gesamt_sm'])}")
    if info_a.get("zeit") != info_b.get("zeit"):
        schwer.append(f"Zeit {fmt(info_a.get('zeit'))} ≠ {fmt(info_b.get('zeit'))} min")
    hinweis = []
    if info_a.get("afb") and info_b.get("afb"):
        diff = {k: abs(info_a["afb"][k] - info_b["afb"][k]) for k in AFB}
        if max(diff.values()) > 10:
            hinweis.append("AFB-Abstand > 10 Punkte: " + ", ".join(f"{k} {diff[k]:.0f}" for k in AFB))
        elif max(diff.values()) > 5:
            hinweis.append("AFB-Abstand > 5 Punkte: " + ", ".join(f"{k} {diff[k]:.0f}" for k in AFB))
    ta, tb = mod_a["sm"]["thema"], mod_b["sm"]["thema"]
    if ta and ta.strip().lower() == tb.strip().lower():
        hinweis.append(f"gleiches Thema „{ta}“")
    if zus_a["lg"] != zus_b["lg"]:
        hinweis.append(f"Lerngebiete verschieden: A {', '.join(sorted(zus_a['lg']))} / B {', '.join(sorted(zus_b['lg']))}")
    titel_a = {tl.titel.lower() for a in mod_a["sm"]["aufgaben"] for tl in a.teile}
    titel_b = {tl.titel.lower() for a in mod_b["sm"]["aufgaben"] for tl in a.teile}
    gleich = sorted(titel_a & titel_b)
    if gleich:
        hinweis.append("gleiche Teilaufgaben-Titel: " + ", ".join(gleich[:4]))
    befunde.append(Befund("2.1", "Vorschläge A und B gleichwertig, nicht austauschbar", "❌" if schwer else ("⚠" if hinweis else "✅"),
                          "; ".join(schwer + hinweis) or
                          "gleiche BE und Zeit; AFB A " + "/".join(fmt(info_a.get("afb", {}).get(k)) for k in AFB) +
                          " %, B " + "/".join(fmt(info_b.get("afb", {}).get(k)) for k in AFB) + " %; verschiedene Themen"))
    return befunde


# ───────────────────────────── Ausgabe ─────────────────────────────

def bericht(befunde: list[Befund], info: dict, modell: dict) -> str:
    sm, je_teil = modell["sm"], modell["je_teil"]
    z = [f"### Selbstprüfung Abiturvorschlag {info.get('vorschlag') or ''} ({info['fach']})".replace("  ", " "), "",
         f"Aufgaben: {info['aufgaben']} · Teilaufgaben: {info['teilaufgaben']} · BE SM: {fmt(info['gesamt_sm'])} · "
         f"BE EWH: {fmt(info['gesamt_lm'])} · Zeit: {fmt(info.get('zeit'))} min" +
         (f" · {info['takt']:.2f} min/BE".replace(".", ",") if info.get("takt") else ""), "",
         "| Krit. | Kriterium | Status | Befund |", "|---|---|---|---|"]
    z += [f"| {b.kriterium} | {b.name} | {b.status} | {b.befund} |" for b in befunde]
    z += ["", "| Teilaufgabe | BE SM | BE EWH | I | II | III | Operatoren SM | Operatoren EWH | Merkmale |",
          "|---|---:|---:|---:|---:|---:|---|---|---:|"]
    for a in sm["aufgaben"]:
        for tl in a.teile:
            d = je_teil.get(tl.nummer, {"I": 0, "II": 0, "III": 0, "S": None, "ops": []})
            mm = modell["lm"]["loesungen"].get(tl.nummer, {}).get("merkmale", [])
            z.append(f"| {tl.nummer} | {fmt(tl.be)} | {fmt(d['S'])} | {fmt(d['I'])} | {fmt(d['II'])} | {fmt(d['III'])} | "
                     f"{', '.join(dict.fromkeys(tl.operatoren)) or '–'} | {', '.join(dict.fromkeys(d['ops'])) or '–'} | {len(mm)} |")
    tot = modell["tot"]
    z += ["", "    Gesamtsummen (AFB I, AFB II, AFB III, gesamt) " +
          " ".join(fmt(tot[k]) for k in AFB) + f" {fmt(sum(tot.values()))}", ""]
    gesamt = info["gesamt_lm"] or info["gesamt_sm"]
    if gesamt:
        g = grenzen(gesamt)
        z += [f"Bewertungsmaßstab für {fmt(gesamt)} BE (Grenzen auf halbe BE aufgerundet):", "",
              "| Notenpunkte | " + " | ".join(p for p, _, _ in g) + " |", "|---|" + "---|" * len(g),
              "| ab Prozent | " + " | ".join(str(pr) for _, pr, _ in g) + " |",
              "| ab BE | " + " | ".join(fmt(b) for _, _, b in g) + " |", ""]
    z.append("_Regelbasierte Selbstprüfung. Lösbarkeit, fachliche Richtigkeit und Bildinhalte prüft die "
             "Lehrkraft (Lösbarkeitsprobe, Korrekturprobe)._")
    return "\n".join(z)


def bewertungsbogen(info: dict, modell: dict) -> str:
    sm, lm = modell["sm"], modell["lm"]
    kopf = re.search(r"Abitur\s+(20\d\d)", sm["kopf"])
    fach = re.search(r"(Technik\s*[–-]\s*[^|\n]+?–|Berufliche Informatik)", sm["kopf"])
    z = [f"# Bewertungsbogen – Abitur {kopf.group(1) if kopf else ''}, {fach.group(1).strip() if fach else ''}, "
         f"Vorschlag {info.get('vorschlag') or ''}".replace("  ", " "), "",
         "| Prüflingsnummer | Erstkorrektur (Kürzel, Datum) | Zweitkorrektur (Kürzel, Datum) |", "|---|---|---|",
         "| | | |", "",
         "Erzeugt aus den Merkmaltabellen des Lehrermaterials (`abitur_check.py`). Keine Namen eintragen.", ""]
    gesamt = 0.0
    for a in sm["aufgaben"]:
        z += [f"## {a.nummer}. Aufgabe – {a.titel} ({fmt(a.be)} BE)", "",
              "| Teilaufgabe | Nr. | Bewertungsmerkmal | AFB | erreichbar | erreicht |", "|---|---|---|---|---:|---:|"]
        summe = 0.0
        for tl in a.teile:
            for m in lm["loesungen"].get(tl.nummer, {}).get("merkmale", []):
                z.append(f"| {tl.nummer} | {m.nr} | {m.text} | {m.afb} | {fmt(m.be)} | |")
                summe += m.be
        z += [f"| **Summe {a.nummer}. Aufgabe** | | | | **{fmt(summe)}** | |", ""]
        gesamt += summe
    g = grenzen(gesamt) if gesamt else []
    z += ["## Ergebnis", "", "| | erreichbar | erreicht |", "|---|---:|---:|", f"| **Gesamt** | **{fmt(gesamt)}** | |",
          "| Notenpunkte | | |", "", f"Umrechnung ({fmt(gesamt)} BE):", "",
          "| Notenpunkte | " + " | ".join(p for p, _, _ in g) + " |", "|---|" + "---|" * len(g),
          "| ab BE | " + " | ".join(fmt(b) for _, _, b in g) + " |", ""]
    return "\n".join(z)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Selbstprüfung eines dezentralen Abiturvorschlags (lokal).")
    p.add_argument("schuelermaterial", type=Path)
    p.add_argument("lehrermaterial", type=Path)
    p.add_argument("--fach", choices=("technik", "informatik"), default=None,
                   help="Operatorenliste (Standard: aus dem Kopf erkannt, sonst technik)")
    p.add_argument("--zeit", type=float, default=None, help="Bearbeitungszeit in Minuten (sonst aus dem Kopf)")
    p.add_argument("--be", type=float, default=None, help="vorgegebene Gesamt-BE (Standard 120)")
    p.add_argument("--vergleich", type=Path, nargs=2, metavar=("SM_B", "LM_B"), help="zweiten Vorschlag vergleichen")
    p.add_argument("--bewertungsbogen", type=Path, default=None, help="leeren Bewertungsbogen schreiben (überschreibt nie)")
    p.add_argument("--operatoren", default=None, help="Pfad zu operatoren-epa-technik.md")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    opdaten = lade_operatoren(operatorenpfad(a.operatoren))
    sm, lm = a.schuelermaterial.read_text(encoding="utf-8"), a.lehrermaterial.read_text(encoding="utf-8")
    befunde, info, modell, zus = pruefe(sm, lm, opdaten, a.fach, a.zeit, a.be,
                                        a.schuelermaterial.parent, a.lehrermaterial.parent)
    if a.vergleich:
        bef_b, info_b, mod_b, zus_b = pruefe(a.vergleich[0].read_text(encoding="utf-8"),
                                             a.vergleich[1].read_text(encoding="utf-8"), opdaten, a.fach, a.zeit, a.be,
                                             a.vergleich[0].parent, a.vergleich[1].parent)
        befunde += vergleiche(info, modell, zus, info_b, mod_b, zus_b)
        befunde += [Befund(f"B:{b.kriterium}", b.name, b.status, b.befund) for b in bef_b if b.status in ("❌", "⚠")]
    if a.bewertungsbogen:
        if a.bewertungsbogen.exists():
            print(f"{a.bewertungsbogen} existiert bereits – nicht überschrieben (anderen Namen wählen).", file=sys.stderr)
            return 2
        a.bewertungsbogen.write_text(bewertungsbogen(info, modell), encoding="utf-8")
    if a.json:
        print(json.dumps({"info": {k: (sorted(v) if isinstance(v, set) else v) for k, v in info.items()},
                          "befunde": [asdict(b) for b in befunde]}, ensure_ascii=False, indent=2))
    else:
        print(bericht(befunde, info, modell))
        if a.bewertungsbogen:
            print(f"\nBewertungsbogen geschrieben: {a.bewertungsbogen}")
    return 1 if any(b.status == "❌" for b in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
