#!/usr/bin/env python3
"""bmk_pruefen – Betriebsmittelkennzeichen (BMK) einer Steuerungsaufgabe abgleichen (lokal).

Prüft Schülermaterial (SM) und optional Lehrermaterial (LM, Erwartungshorizont/Musterlösung)
einer Aufgabe aus der Steuerungstechnik: Stehen dieselben Kennzeichen in Funktionsbeschreibung,
Legende des Technologieschemas, Zuordnungsliste, Aufgaben, Anlagen und Musterlösung?

  T.1 BMK aus Lehrermaterial und Musterlösung kommen im Schülermaterial vor (sonst „nur im LM“)
  T.2 BMK aus Legende und vorgegebener Zuordnungsliste stehen in der Funktionsbeschreibung
  T.3 Technologieschema als Bild hat eine Text-Legende (sonst Bildinhalt von Hand prüfen)
  T.4 Kontaktart (NO/NC bzw. Schließer/Öffner) oder Signalbedeutung je Geber (S…, B…) genannt
      und widerspruchsfrei in Text, vorgegebener Zuordnungsliste und Musterlösung
  T.5 Operanden je Zuordnungsliste eindeutig, Schreibweise je Spalte einheitlich, vorgegebene
      Zeilen = Musterlösung; Musterlösung vollständig (Geber, Melder, Schaltgeräte, Magnetspulen)
  T.6 BMK-Schreibweise einheitlich („-S1“, nicht daneben „S1“, „- S1“ oder „Taster S1“)
  T.7 Grundstellung, Start und Stopp/Not-Halt beschrieben oder ausdrücklich ausgeklammert
  T.8 Kennbuchstaben nach DIN EN IEC 81346-2:2020: Klasse und Unterklasse vorhanden, keine
      Kennbuchstaben der Ausgabe 2009 (-SF Taster, -RZ, Klasse A, SPS als -KF). So kurz wie
      möglich (didaktische Reduktion): Unterklasse nur, wenn die Klasse verschiedenartige
      Betriebsmittel enthält (-BL1 neben -BT1), sonst nur die Klasse (-S1, -S2 statt -SJ1, -SJ2);
      je Klasse eine Tiefe. Nennt der Text die Ausgabe 2009 („81346-2:2009“), gilt sie ohne
      Tabellenabgleich.
  T.9 GRAFCET in Textform nach dem Notationsblatt der Bibliothek (Tabellen „Schritt | Aktion |
      Transition“): UND „·“, ODER „+“, NICHT „¬“, Zeit „5s/X3“, Vergleiche in [ ], Folgeschritt nach
      „→“, speichernde Aktionen „↑ -Q1 := 1“; keine Schreibweisen aus Programmiersprachen.

Plattformen: Zuordnungslisten dürfen je eine Spalte für SPS, Kleinsteuerung und Mikrocontroller
haben (Operanden wie %I0.0, %IW64, %IX4.0, I1, AI1, IA5, D2, A0, GPIO16, GP26, PB12); T.5 prüft
jede Spalte für sich. Eine Anlage, deren
Überschrift „Notation“ enthält (Notationsblatt), wird übersprungen – ihre Beispiel-Kennzeichen
gehören nicht zur Aufgabe.

Kennzeichen wie „-S1“, „-BG12“, „-Q1“ (Kennbuchstaben nach DIN EN IEC 81346-2, Bindestrich
vorn; Tabelle in normen-technik.md). Eine andere Hauskonvention gibt --bmk-muster als regulären
Ausdruck an, z. B. "[SBKQYHMP][0-9]{1,2}" für „S1, B2, K1“ (dann entfällt T.8).

Aufruf:
    python3 bmk_pruefen.py SM.(md|docx|odt|pdf|txt) [LM.…] [--bmk-muster REGEX] [--json]

Bilder kann das Skript nicht lesen: Kennzeichen, die nur im Bild stehen, fehlen im Abgleich –
dafür gibt es die Text-Legende (T.3). Liest DOCX, ODT und PDF über text_lesen.py im selben
Ordner. Exit-Code 1 bei ❌. Läuft vollständig lokal; nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from text_lesen import lies_text          # DOCX/ODT/PDF (text_lesen.py aus _gemeinsam)
except ImportError:  # pragma: no cover – ohne Hilfsmodul nur Markdown/Text
    def lies_text(pfad: Path) -> str:
        return Path(pfad).read_text(encoding="utf-8", errors="replace")

STANDARD = r"-[A-Z]{1,3}[0-9]{1,3}"
# Varianten derselben Kennung: Gedankenstrich statt Bindestrich, Leerzeichen dazwischen
VARIANTE = re.compile(r"(?<![\w\-–])([-–])(\s?)([A-Z]{1,3})(\s?)([0-9]{1,3})(?![\w])")
# Alte Kennzeichnung mit Gerätewort davor („Taster S1“, „Schütz K1“) – nur als Hinweis
ALT = re.compile(r"\b(?:Taster|Schalter|Sensor|Geber|Endschalter|Schütz|Relais|Ventil|Magnetventil|"
                 r"Leuchte|Leuchtmelder|Melder|Motor|Zylinder)\s+([SBKQYHMP][0-9]{1,2})\b")
KONTAKT = {"no": "NO", "nc": "NC", "schließer": "NO", "öffner": "NC"}
KONTAKT_NACH = re.compile(r"^\s*\(?\s*(NO|NC|Schließer|Öffner)\b", re.IGNORECASE)
KONTAKT_IN_KLAMMER = re.compile(r"\((?:[^()]{0,20}?)\b(NO|NC|Schließer|Öffner)\b[^()]{0,30}\)", re.IGNORECASE)
KONTAKT_VOR = re.compile(r"\b(NO|NC|Schließer|Öffner)\s*$", re.IGNORECASE)
SIGNAL = re.compile(r"(?:\b[01][-‑]Signal\b|\bSignal\s*[01]\b|\bmeldet\s+[01]\b|\bliefert\s+[01]\b|=\s*[01]\b|"
                    r"\b\d+\s*(?:…|\.\.\.|bis)\s*\d+\s*(?:mA|V)\b|\banalog)", re.IGNORECASE)
OPERAND = re.compile(r"^%?(?:[IQEAM][XBWD]?|DB\d+\.DBX)\d+(?:\.\d+)?$"      # SPS, Kleinsteuerung
                     r"|^(?:D|GPIO|GP|IO|AI|AQ|IA|QA|PIN|P[A-K])\d{1,2}$", re.IGNORECASE)  # Pins D2, GPIO16, GP2, PB12; LOGO! AI1; easyE4 IA1
# Operand als Wort im Spaltentext (PDF/DOCX): SPS „I0.0“, „%Q0.1“, „E1.2“, LOGO „I1“, „Q4“
OPERAND_WORT = re.compile(r"(?<![\w.%-])(%?(?:[IQEA]X?\d+\.\d+|[IQ]\d{1,2})|GPIO\d{1,2})(?![\w.])")
GRUND = re.compile(r"Grundstellung|Ausgangsstellung|Ausgangslage|Ausgangsposition|Grundposition|Grundzustand|"
                   r"Ausgangszustand|Anfangszustand|Initialschritt|Ruhezustand|Ruhelage|zu Beginn|"
                   r"bei (?:der )?Inbetriebnahme|beim Einschalten", re.IGNORECASE)
START = re.compile(r"\bStart|gestartet|einschalt|Einschalt", re.IGNORECASE)
STOPP = re.compile(r"Stopp|\bStop\b|\bHalt|Not-?Halt|NOT-?HALT|Not-?Aus|NOT-?AUS|angehalten", re.IGNORECASE)
LISTENMARKE = re.compile(r"^\s*(?:[-*+]|\d+\.)\s+")
EA_RELEVANT = re.compile(r"^-?(?:S|B|P|Q|MB)")

# Kennbuchstaben nach DIN EN IEC 81346-2:2020 (IEC 81346-2:2019, Tabelle 2): Unterklassen je Klasse.
# A, I und O sind keine Klassen, D, J, L, V, Y und Z reserviert. Bedeutungen: normen-technik.md
UNTERKLASSEN_2020 = {
    "B": "ABCDEFGHJKLMPQRSTUWXYZ", "C": "ABCFLMNPQ", "E": "ABCEGMPQTUV", "F": "ABCELMNQRS",
    "G": "ABCFLMPQR", "H": "JKLMPQRSUVWX", "K": "EFGHJZ", "M": "ABCDLMST", "N": "ABCDE",
    "P": "FGHJKLZ", "Q": "ABCMNPQRSZ", "R": "ABFLMNQU", "S": "FGHJKZ", "T": "ABCFLMPR",
    "U": "ABCLMNPQTU", "W": "BDEGHJLMPQRVZ", "X": "BDEGHKMNPSTZ",
}
# Kennbuchstaben der Ausgabe 2009, die in Prüfungsaufgaben 2020 anders heißen
AUS_2009 = {"SF": "Taster und Schalter heißen -SJ, SF ist Gesichtserkennung",
            "RZ": "Drosselrückschlagventil heißt -RN"}
AUSGABE_81346 = re.compile(r"81346-2\s*(?::|\(|,?\s*Ausgabe)\s*(20\d\d)")
SPS_ALS_KF = re.compile(r"(?:\bSPS\b|Steuerung|Kleinsteuerung|Mikrocontroller|Controller)\s*(?:\([^)\n]{0,20}\)\s*)?"
                        r"[-–](KF\d+)|\|\s*[-–](KF\d+)\s*\|\s*(?:SPS|Steuerung|Kleinsteuerung|Mikrocontroller|Controller)")

# Anlage mit dem Notationsblatt: Überschrift mit „Notation“ (Beispiel-Kennzeichen gehören nicht zur Aufgabe)
NOTATION_KOPF = re.compile(r"^(#{1,6})\s+.*\bNotation", re.IGNORECASE)
# T.9 GRAFCET in Textform (Notationsblatt der Bibliothek)
FREMD_LOGIK = re.compile(r"\b(?:AND|OR|NOT|XOR|UND|ODER|NICHT)\b|&&|\|\||(?<![<>=!])!(?!=)|[∧∨]|(?:^|[\s(·+])/-?[A-Z]")
ZEIT = re.compile(r"(\d+(?:,\d+)?)(\s*)(ms|s|min|h)\s*/\s*X\s*\w+")
ZEIT_OHNE_SCHRITT = re.compile(r"\b\d+(?:,\d+)?\s?(?:ms|s|min|h)\b(?!\s*/)")
VERGLEICH = re.compile(r"[<>≤≥≠]|(?<![:<>!=])=(?![=>])")
QUALIFIER = re.compile(r"(?:^|[,;]\s*)(?:N|S|R|D|L|P|SD|DS|SL)\s+(?:-|%|`)")

ABSCHNITT_ART = [                       # Reihenfolge zählt: Teilaufgaben-Überschriften zuerst
    ("aufgabe", re.compile(r"\d+\.\s*aufgabe\b|^aufgabe\s+\d+|^\d+\.\d+\b", re.I)),
    ("funktion", re.compile(r"funktionsbeschreibung|ablaufbeschreibung|anlagenbeschreibung|prozessbeschreibung", re.I)),
    ("legende", re.compile(r"legende|technologieschema|anlagenschema|lageplan", re.I)),
    ("zuordnung", re.compile(r"zuordnungs(?:liste|tabelle)|belegungs(?:liste|plan)|e/a-liste|symboltabelle", re.I)),
    ("anlage", re.compile(r"^(?:anlage|material|vorlage)\b|^b\.\s*material", re.I)),
]
STICHWORT_ZEILE = re.compile(r"^\s*(?:\*\*)?(Funktionsbeschreibung|Technologieschema|Legende|Zuordnungsliste|"
                             r"Zuordnungstabelle|Handlungssituation|Hilfsmittel|Handlungsergebnisse|Material|"
                             r"Anlage\s+\d+\w?|\d+\.\s*Aufgabe|Aufgabe\s+\d+|\d+\.\d+\s+\S.*)(?:\*\*)?\s*:?\s*$", re.I)


@dataclass
class Befund:
    kriterium: str
    name: str
    status: str            # ✅ ❌ ⚠ ➖
    befund: str


# ───────────────────────────── Text zerlegen ─────────────────────────────

def _ohne_kopf(text: str, notation: bool = False) -> str:
    """YAML-Kopf und HTML-Kommentare entfernen (Vorlagenhinweise sind kein Aufgabentext); ohne
    notation=True auch die Anlage „Notation …“ bis zur nächsten Überschrift gleicher Ebene."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    if notation:
        return text
    aus, ebene = [], None
    for zeile in text.splitlines(keepends=True):
        m = re.match(r"^(#{1,6})\s", zeile)
        if ebene is not None and not (m and len(m.group(1)) <= ebene):
            continue
        ebene = None
        k = NOTATION_KOPF.match(zeile)
        if k:
            ebene = len(k.group(1))
            continue
        aus.append(zeile)
    return "".join(aus)


def abschnitte(text: str) -> list[tuple[str, str, str]]:
    """(Art, Überschrift, Inhalt) – Markdown-Überschriften oder Stichwortzeilen (PDF-Text)."""
    teile: list[tuple[str, str, list[str]]] = [("einleitung", "", [])]
    for zeile in _ohne_kopf(text).splitlines():
        m = re.match(r"^\s{0,3}#{1,6}\s+(.*?)\s*#*\s*$", zeile)
        kopf = m.group(1) if m else None
        if kopf is None and len(zeile.split()) <= 8:
            s = STICHWORT_ZEILE.match(zeile)
            kopf = s.group(1) if s else None
        if kopf is not None:
            name = re.sub(r"[*_`]", "", kopf).strip()
            art = next((a for a, muster in ABSCHNITT_ART if muster.search(name)), "sonstiges")
            teile.append((art, name, [zeile] if not m else []))
            continue
        teile[-1][2].append(zeile)
    return [(a, n, "\n".join(z)) for a, n, z in teile]


def tabellen(text: str) -> list[list[list[str]]]:
    """Markdown-Tabellen als Zeilenlisten (ohne Trennzeile), Zellen ohne Formatierung."""
    erg, akt = [], []
    for zeile in text.splitlines():
        s = zeile.strip()
        if s.startswith("|") and s.count("|") >= 2:
            if re.fullmatch(r"\|?[\s:|\-]+\|?", s):
                continue
            akt.append([re.sub(r"[*`]", "", z).strip() for z in s.strip("|").split("|")])
        elif akt:
            erg.append(akt)
            akt = []
    if akt:
        erg.append(akt)
    return erg


# ───────────────────────────── BMK finden ─────────────────────────────

def _finder(muster: str | None) -> re.Pattern:
    kern = muster or STANDARD
    return re.compile(rf"(?<![\w\-–])({kern})(?![\w])")


def kennung(roh: str) -> str:
    """Normalform: Gedankenstrich → Bindestrich, Leerzeichen raus („– S 1“ → „-S1“)."""
    return re.sub(r"\s+", "", roh.replace("–", "-"))


def bmk_im_text(text: str, finder: re.Pattern, standard: bool) -> list[tuple[str, str, int]]:
    """(Kennung, Schreibweise, Position) aller Funde; bei Standardmuster auch Varianten."""
    funde = []
    zeilen = [LISTENMARKE.sub("", z) for z in text.splitlines()]
    flach = "\n".join(zeilen)
    if standard:
        for m in VARIANTE.finditer(flach):
            funde.append((kennung(m.group(0)), m.group(0), m.start()))
    else:
        funde += [(m.group(1), m.group(1), m.start()) for m in finder.finditer(flach)]
    return funde


def kontaktarten(text: str, finder: re.Pattern, standard: bool) -> tuple[dict[str, set[str]], set[str]]:
    """Kontaktart je Kennung aus dem Fließtext und Kennungen mit beschriebener Signalbedeutung."""
    arten: dict[str, set[str]] = {}
    signal: set[str] = set()
    flach = "\n".join(LISTENMARKE.sub("", z) for z in text.splitlines())
    funde = bmk_im_text(flach, finder, standard)
    for i, (k, roh, pos) in enumerate(funde):
        ende = pos + len(roh)
        naechster = funde[i + 1][2] if i + 1 < len(funde) else len(flach)
        voriger = funde[i - 1][2] + len(funde[i - 1][1]) if i > 0 else 0
        nach = flach[ende:min(naechster, ende + 40)].split("\n", 1)[0]       # nur in derselben Zeile
        satz_nach = re.split(r"[.;!?]", nach, maxsplit=1)[0]
        vor = flach[max(voriger, pos - 20):pos].rsplit("\n", 1)[-1]
        m = KONTAKT_NACH.match(nach) or KONTAKT_IN_KLAMMER.match(nach.lstrip()) or KONTAKT_VOR.search(vor)
        if m:
            arten.setdefault(k, set()).add(KONTAKT[m.group(1).lower()])
        if SIGNAL.search(satz_nach) or m:
            signal.add(k)
    for zeile in flach.splitlines():
        z = " ".join(zeile.replace("|", " ").split())
        ks = {k for k, _, _ in bmk_im_text(z, finder, standard)}
        mk = re.search(r"(?<![\w-])(NO|NC|Schließer|Öffner)(?![\w-])", z)
        if len(ks) == 1 and mk:
            k = ks.pop()
            arten.setdefault(k, set()).add(KONTAKT[mk.group(1).lower()])
            signal.add(k)
    return arten, signal


def zuordnungslisten(text: str, finder: re.Pattern, standard: bool) -> list[dict]:
    """Tabellen mit BMK-Spalte und mindestens einer Operandenspalte: [{bmk: {spalte: operand}}, kontakt]."""
    listen = []
    for tab in tabellen(text):
        if len(tab) < 2:
            continue
        kopf = [z.lower() for z in tab[0]]
        bmk_spalte = next((i for i, z in enumerate(kopf) if re.search(r"bmk|betriebsmittel|kennzeichen|symbol", z)), None)
        if bmk_spalte is None:
            # Spalte, in der die meisten Zellen eine Kennung sind
            treffer = [sum(1 for r in tab[1:] if i < len(r) and finder.fullmatch(kennung(r[i]) if standard else r[i]))
                       for i in range(len(kopf))]
            if not treffer or max(treffer) < 2:
                continue
            bmk_spalte = treffer.index(max(treffer))
        op_spalten = [i for i, z in enumerate(kopf)
                      if re.search(r"operand|adresse|e/a|eingang|ausgang|sps|logo|kleinsteuerung|pin|gpio|mikrocontroller|µc", z)]
        if not op_spalten:
            op_spalten = [i for i in range(len(kopf)) if i != bmk_spalte and
                          sum(1 for r in tab[1:] if i < len(r) and OPERAND.match(r[i].replace(" ", ""))) >= 2]
        kontakt_spalte = next((i for i, z in enumerate(kopf) if re.search(r"funktion|kontakt|no/nc|öffner|schließer", z)), None)
        zeilen: dict[str, dict] = {}
        for r in tab[1:]:
            if bmk_spalte >= len(r):
                continue
            zelle = r[bmk_spalte]
            k = kennung(zelle) if standard else zelle.strip()
            if not finder.fullmatch(k):
                continue
            ops = {kopf[i]: r[i].replace(" ", "") for i in op_spalten if i < len(r) and r[i].strip()}
            kontakt = None
            if kontakt_spalte is not None and kontakt_spalte < len(r):
                mk = re.search(r"\b(NO|NC|Schließer|Öffner)\b", r[kontakt_spalte], re.I)
                kontakt = KONTAKT[mk.group(1).lower()] if mk else None
            zeilen[k] = {"operanden": ops, "kontakt": kontakt, "zelle": zelle}
        if zeilen and op_spalten:
            listen.append({"spalten": [kopf[i] for i in op_spalten], "zeilen": zeilen})
    return listen + _spaltentext_listen(text, finder, standard)


def _spaltentext_listen(text: str, finder: re.Pattern, standard: bool) -> list[dict]:
    """Zuordnungslisten aus Spaltentext (PDF/DOCX): Zeilen mit genau einer Kennung und Operanden;
    benachbarte Zeilen (höchstens sechs andere Zeilen dazwischen, z. B. Seitenumbruch) bilden eine Liste."""
    listen, akt, abstand = [], {}, 0
    for zeile in text.splitlines():
        if zeile.strip().startswith("|"):
            continue
        z = " ".join(zeile.split())
        ks = list(dict.fromkeys(k for k, _, _ in bmk_im_text(z, finder, standard)))
        ops = OPERAND_WORT.findall(z)
        if len(ks) == 1 and ops:
            mk = re.search(r"(?<![\w-])(NO|NC|Schließer|Öffner)(?![\w-])", z)
            akt[ks[0]] = {"operanden": {f"Operand {i + 1}": o.upper() for i, o in enumerate(ops)},
                          "kontakt": KONTAKT[mk.group(1).lower()] if mk else None, "zelle": ks[0]}
            abstand = 0
        elif akt:
            abstand += 1
            if abstand > 6:
                listen.append(akt)
                akt, abstand = {}, 0
    if akt:
        listen.append(akt)
    return [{"spalten": sorted({s for z in liste.values() for s in z["operanden"]}), "zeilen": liste}
            for liste in listen if len(liste) >= 2]


# ───────────────────────────── Prüfung ─────────────────────────────

def ausgabe_81346(*texte: str) -> str | None:
    """Im Text genannte Ausgabe der DIN EN IEC 81346-2: „2009“ (auch DIN EN 81346-2:2010) oder „2020“."""
    for text in texte:
        for m in AUSGABE_81346.finditer(text or ""):
            if m.group(1) in ("2009", "2010"):
                return "2009"
            if m.group(1) in ("2019", "2020"):
                return "2020"
    return None


def pruefe_kennbuchstaben(kennungen: list[str], sm: str, lm: str) -> tuple[Befund, str]:
    """T.8 – Kennbuchstaben gegen DIN EN IEC 81346-2:2020; zweiter Wert: geltende Ausgabe."""
    name = "Kennbuchstaben nach DIN EN IEC 81346-2"
    genannt = ausgabe_81346(sm, lm)
    buchstaben = {k: re.match(r"-([A-Z]+)", k).group(1) for k in kennungen}
    text = []
    klassen: dict[str, list[str]] = {}
    for k, b in buchstaben.items():
        klassen.setdefault(b[0], []).append(k)
    gemischt, kuerzer = [], []
    for ks in klassen.values():
        tiefe = {len(buchstaben[k]) for k in ks}
        if len(tiefe) > 1:                                   # -B1 neben -BG2
            ks = sorted(ks, key=lambda k: len(buchstaben[k]))
            gemischt.append(f"{ks[0]} neben {ks[-1]}")
            continue
        # kleinste Tiefe, die alle Arten der Klasse noch unterscheidet (-SJ1, -SJ2 → -S1, -S2)
        arten = {buchstaben[k] for k in ks}
        d = next(d for d in range(1, max(tiefe) + 1) if len({a[:d] for a in arten}) == len(arten))
        if d < max(tiefe):
            kuerzer.append(", ".join(ks) + " → " + ", ".join(f"-{buchstaben[k][:d]}{k[len(buchstaben[k]) + 1:]}"
                                                               for k in ks))
    if gemischt:
        text.append("Tiefe innerhalb einer Klasse gemischt: " + "; ".join(gemischt))
    if kuerzer:
        text.append("kürzer möglich – Unterklasse ohne Unterscheidung in der Klasse: " + "; ".join(kuerzer))
    if genannt == "2009":
        return Befund("T.8", name, "⚠" if text else "✅",
                      "; ".join(text + ["Ausgabe 2009 im Text genannt (aktuell: DIN EN IEC 81346-2:2020) – "
                                        "Unterklassen nicht gegen die Tabelle geprüft"])), "2009"
    alt: dict[str, list[str]] = {}          # Grund → Kennungen
    fremd = []
    for k, b in buchstaben.items():
        if b[0] == "A":
            alt.setdefault("Klasse A gibt es nicht mehr", []).append(k)
        elif b[0] in "IO":
            fremd.append(f"{k} ({b[0]} ist keine Klasse)")
        elif b[0] not in UNTERKLASSEN_2020:
            fremd.append(f"{k} (Klasse {b[0]} reserviert)")
        elif b[:2] in AUS_2009:
            alt.setdefault(AUS_2009[b[:2]], []).append(k)
        elif len(b) > 1 and b[1] not in UNTERKLASSEN_2020[b[0]]:
            fremd.append(k)
    sps = sorted({"-" + (m.group(1) or m.group(2)) for m in SPS_ALS_KF.finditer(sm + "\n" + lm)})
    if sps:
        alt["Steuerung (SPS) heißt -KE, -KF ist Relais und Zeitrelais"] = sps
    if fremd:
        text.append("nicht in Tabelle 2 der Ausgabe 2020: " + ", ".join(fremd))
    if alt:
        text.append("Kennbuchstaben der Ausgabe 2009: "
                    + "; ".join(f"{', '.join(ks)} ({grund})" for grund, ks in alt.items())
                    + (" – Ausgaben gemischt" if genannt == "2020" else
                       " – auf die Ausgabe 2020 umstellen oder die Ausgabe 2009 im Schülermaterial nennen"))
    if text:
        return Befund("T.8", name, "⚠", "; ".join(text)), "2020"
    return Befund("T.8", name, "✅", f"{len(kennungen)} Kennzeichen passen zur Ausgabe 2020"
                  + ("" if genannt else " (Ausgabe im Schülermaterial nicht genannt)")), "2020"


def pruefe_grafcet(*texte: str) -> Befund:
    """T.9 – GRAFCET-Tabellen (Schritt | Aktion | Transition) in der Schreibweise des Notationsblatts."""
    name = "GRAFCET-Notation (Notationsblatt)"
    funde: dict[str, list[str]] = {}            # Befund → Schritte
    n_tab = 0
    for text in texte:
        for tab in tabellen(text or ""):
            kopf = [z.lower() for z in tab[0]]
            s_sp = next((i for i, z in enumerate(kopf) if "schritt" in z and "folge" not in z), None)
            t_sp = next((i for i, z in enumerate(kopf) if re.search(r"transition|weiterschalt|übergang", z)), None)
            if s_sp is None or t_sp is None:
                continue
            n_tab += 1
            a_sp = next((i for i, z in enumerate(kopf) if "aktion" in z), None)
            for nr, r in enumerate(tab[1:]):
                schritt = r[s_sp].split()[0] if s_sp < len(r) and r[s_sp].split() else "?"
                if nr == 0 and s_sp < len(r) and not re.search(r"initial", r[s_sp], re.I):
                    funde.setdefault("Initialschritt nicht gekennzeichnet", []).append(schritt)
                tr = r[t_sp].replace("->", "→") if t_sp < len(r) else ""
                if tr.strip() and tr.strip() not in ("–", "-"):
                    ohne_klammer = re.sub(r"\[[^\]]*\]", "", tr)
                    ohne_zeit = ZEIT.sub("", ohne_klammer)
                    if FREMD_LOGIK.search(tr):
                        funde.setdefault(f"Verknüpfung als „·“, „+“, „¬“ ({FREMD_LOGIK.search(tr).group(0).strip()})", []).append(schritt)
                    if re.search(r"(?<=\S)\s*\*\s*(?=\S)", ohne_zeit):
                        funde.setdefault("UND als „·“ statt „*“", []).append(schritt)
                    if any(m.group(2) for m in ZEIT.finditer(tr)):
                        funde.setdefault("Zeitbedingung ohne Leerzeichen („5s/X3“)", []).append(schritt)
                    if ZEIT_OHNE_SCHRITT.search(ohne_zeit):
                        funde.setdefault("Zeit ohne Schrittbezug – als „t/Xn“ schreiben", []).append(schritt)
                    if VERGLEICH.search(ohne_klammer):
                        funde.setdefault("Vergleich in eckige Klammern [ … ] setzen", []).append(schritt)
                    if "→" not in tr:
                        funde.setdefault("Folgeschritt nach „→“ angeben", []).append(schritt)
                akt = r[a_sp] if a_sp is not None and a_sp < len(r) else ""
                if QUALIFIER.search(akt):
                    funde.setdefault("Bestimmungszeichen der Ablaufsprache (S, R, N …) – GRAFCET: „↑ -Q1 := 1“", []).append(schritt)
                if ":=" in akt and not re.search(r"[↑↓]", akt):
                    funde.setdefault("speichernde Aktion ohne Auslöser (↑ bei Aktivierung, ↓ bei Deaktivierung)", []).append(schritt)
                if any(re.match(r"\s*[↑↓]", teil) and ":=" not in teil for teil in re.split(r"[;,]", akt)):
                    funde.setdefault("speichernde Aktion ohne Zuweisung („↑ -Q1 := 1“ statt „↑ -Q1“)", []).append(schritt)
                if re.search(r"(?<!:)=\s*[01]\b", akt):
                    funde.setdefault("kontinuierliche Aktion nur mit dem Kennzeichen, ohne „= 1“", []).append(schritt)
    if not n_tab:
        return Befund("T.9", name, "➖", "kein GRAFCET in Textform (Tabelle Schritt | Aktion | Transition) – Zeichnung von Hand prüfen")
    if funde:
        return Befund("T.9", name, "⚠", "; ".join(f"{text} (Schritt {', '.join(dict.fromkeys(s))})"
                                                for text, s in funde.items()))
    return Befund("T.9", name, "✅", f"{n_tab} GRAFCET-Tabelle(n) in der Schreibweise des Notationsblatts")

def pruefe_bmk(sm: str, lm: str | None = None, muster: str | None = None) -> tuple[list[Befund], dict]:
    """Befunde T.1–T.9 und Inventar {Kennung: {Fundorte, Kontaktart}}."""
    standard = muster is None
    finder = _finder(muster)
    teile = abschnitte(sm)
    orte: dict[str, set[str]] = {}
    schreibweisen: dict[str, set[str]] = {}
    for art, _, inhalt in teile:
        ort = {"funktion": "F", "legende": "L", "zuordnung": "Z", "anlage": "M", "aufgabe": "A"}.get(art, "E")
        for k, roh, _ in bmk_im_text(inhalt, finder, standard):
            orte.setdefault(k, set()).add(ort)
            schreibweisen.setdefault(k, set()).add(roh.strip())
    sm_listen = zuordnungslisten(_ohne_kopf(sm), finder, standard)
    for liste in sm_listen:
        for k in liste["zeilen"]:
            orte.setdefault(k, set()).add("Z")
    lm_text = _ohne_kopf(lm) if lm else ""
    lm_listen = zuordnungslisten(lm_text, finder, standard) if lm else []
    lm_bmk = {k for k, _, _ in bmk_im_text(lm_text, finder, standard)} if lm else set()
    for k in lm_bmk:
        orte.setdefault(k, set()).add("LM")
    if lm:
        for k, roh, _ in bmk_im_text(lm_text, finder, standard):
            schreibweisen.setdefault(k, set()).add(roh.strip())

    info = {"bmk": {}, "funktionsbeschreibung": any(a == "funktion" for a, _, _ in teile)}
    if not orte:
        return [Befund("T", "Betriebsmittelkennzeichen", "➖",
                       "keine Kennzeichen gefunden – Abgleich entfällt (keine Steuerungsaufgabe?)")], info

    sm_flach = _ohne_kopf(sm)
    arten, signal = kontaktarten(sm_flach, finder, standard)
    for liste in sm_listen:
        for k, z in liste["zeilen"].items():
            if z["kontakt"]:
                arten.setdefault(k, set()).add(z["kontakt"])
                signal.add(k)
    lm_arten, _ = kontaktarten(lm_text, finder, standard) if lm else ({}, set())
    for liste in lm_listen:
        for k, z in liste["zeilen"].items():
            if z["kontakt"]:
                lm_arten.setdefault(k, set()).add(z["kontakt"])
    befunde: list[Befund] = []
    sm_bmk = {k for k, o in orte.items() if o - {"LM"}}

    # T.1 nur im Lehrermaterial
    nur_lm = sorted(lm_bmk - sm_bmk)
    if lm is None:
        befunde.append(Befund("T.1", "BMK der Musterlösung im Schülermaterial", "➖", "kein Lehrermaterial übergeben"))
    else:
        befunde.append(Befund("T.1", "BMK der Musterlösung im Schülermaterial", "❌" if nur_lm else "✅",
                              ("nur im Lehrermaterial (im Schülertext nicht eingeführt – höchstens im Bild): "
                               + ", ".join(nur_lm)) if nur_lm else "alle Kennzeichen des Lehrermaterials sind im Schülermaterial eingeführt"))

    # T.2 Legende/Zuordnungsliste ⊆ Funktionsbeschreibung
    hat_fb = info["funktionsbeschreibung"]
    in_fb = {k for k, o in orte.items() if "F" in o}
    soll = {k for k, o in orte.items() if o & {"L", "Z"}}
    if not hat_fb:
        befunde.append(Befund("T.2", "BMK in der Funktionsbeschreibung", "⚠",
                              "kein Abschnitt „Funktionsbeschreibung“ gefunden – alle Kennzeichen dort mit Bedeutung einführen"))
    else:
        fehlt = sorted(soll - in_fb)
        legende = {k for k, o in orte.items() if "L" in o}
        nicht_in_legende = sorted(in_fb - legende) if legende else []
        text = []
        if fehlt:
            text.append("in Legende/Zuordnungsliste, aber nicht in der Funktionsbeschreibung: " + ", ".join(fehlt))
        if nicht_in_legende:
            text.append("in der Funktionsbeschreibung, aber nicht in der Legende des Technologieschemas: " + ", ".join(nicht_in_legende))
        befunde.append(Befund("T.2", "BMK in der Funktionsbeschreibung", "❌" if fehlt else ("⚠" if nicht_in_legende else "✅"),
                              "; ".join(text) or "alle Kennzeichen der Legende und Zuordnungsliste stehen in der Funktionsbeschreibung"))

    # T.3 Bild ohne Legende
    schema = [(n, i) for a, n, i in teile if a == "legende"]
    bild = any(re.search(r"!\[|\[ABBILDUNG|\.(?:png|jpe?g|svg|gif)\b", i, re.I) for _, i in schema) or \
        bool(re.search(r"Technologieschema[^\n]{0,40}(?:Abbildung|Bild)|(?:Abbildung|Bild)\s*\d*\s*:?\s*Technologieschema", sm_flach))
    legende = {k for k, o in orte.items() if "L" in o}
    bild = bild or any(re.search(r"technologieschema|anlagenschema", n, re.I) for n, _ in schema)
    if bild and not legende:
        befunde.append(Befund("T.3", "Technologieschema mit Text-Legende", "⚠",
                              "Technologieschema als Bild ohne Legende im Text – Kennzeichen im Bild von Hand mit der Funktionsbeschreibung abgleichen"))
    else:
        befunde.append(Befund("T.3", "Technologieschema mit Text-Legende", "✅" if legende else "➖",
                              "Legende mit Kennzeichen vorhanden" if legende else "kein Technologieschema erkannt"))

    # T.4 Kontaktart
    widerspruch = []
    for k in sorted(set(arten) | set(lm_arten)):
        alle = arten.get(k, set()) | lm_arten.get(k, set())
        if len(alle) > 1:
            quelle = "Schülermaterial" if len(arten.get(k, set())) > 1 else "Schüler- und Lehrermaterial"
            widerspruch.append(f"{k} ({'/'.join(sorted(alle))}, {quelle})")
    geber = sorted(k for k in sm_bmk if re.match(r"^-?[SB]", k))
    ohne = [k for k in geber if k not in signal]
    text = []
    if widerspruch:
        text.append("widersprüchliche Kontaktart: " + ", ".join(widerspruch))
    if ohne:
        text.append("Kontaktart (NO/NC) bzw. Signalbedeutung im Schülermaterial nicht genannt: " + ", ".join(ohne))
    if not geber and not widerspruch:
        befunde.append(Befund("T.4", "Kontaktart und Signalbedeutung der Geber", "➖",
                              "keine Geber (S…, B…) im Schülermaterial"))
    else:
        befunde.append(Befund("T.4", "Kontaktart und Signalbedeutung der Geber", "❌" if widerspruch else ("⚠" if ohne else "✅"),
                              "; ".join(text) or f"für alle {len(geber)} Geber genannt und widerspruchsfrei"))

    # T.5 Zuordnungslisten
    text, schwer = [], False
    for herkunft, listen in (("Schülermaterial", sm_listen), ("Lehrermaterial", lm_listen)):
        for liste in listen:
            for spalte in liste["spalten"]:
                belegt: dict[str, list[str]] = {}
                formen = set()
                for k, z in liste["zeilen"].items():
                    op = z["operanden"].get(spalte)
                    if op:
                        belegt.setdefault(op.upper(), []).append(k)
                        formen.add("%" if op.startswith("%") else re.sub(r"[0-9.]", "", op.upper())[:1] + ("." if "." in op else ""))
                doppelt = [f"{op} ({', '.join(ks)})" for op, ks in belegt.items() if len(ks) > 1]
                if doppelt:
                    schwer = True
                    text.append(f"{herkunft}, Spalte „{spalte}“: Operand doppelt belegt: " + "; ".join(doppelt))
                if any(f == "%" for f in formen) and any(f != "%" for f in formen):
                    text.append(f"{herkunft}, Spalte „{spalte}“: Schreibweise gemischt (mit und ohne %)")
    if sm_listen and lm_listen:
        vorgabe = {k: z for liste in sm_listen for k, z in liste["zeilen"].items()}
        loesung = {k: z for liste in lm_listen for k, z in liste["zeilen"].items()}
        for k, z in vorgabe.items():
            if k in loesung:
                abw = [f"{s}: {v} ≠ {loesung[k]['operanden'].get(s)}" for s, v in z["operanden"].items()
                       if s in loesung[k]["operanden"] and loesung[k]["operanden"][s].upper() != v.upper()]
                if abw:
                    schwer = True
                    text.append(f"{k}: vorgegebene Zeile weicht von der Musterlösung ab ({'; '.join(abw)})")
    if lm_listen:
        loesung_bmk = {k for liste in lm_listen for k in liste["zeilen"]}
        # nur Kennzeichen mit eigenem Operanden: Geber (S, B), Melder (P), Schaltgeräte (Q), Magnetspulen (MB);
        # Motoren, Zylinder und die Steuerung selbst hängen nicht direkt an einem Operanden
        geber_aktoren = {k for k in sm_bmk if ("F" in orte[k] or "L" in orte[k]) and EA_RELEVANT.match(k)}
        fehlt = sorted(geber_aktoren - loesung_bmk)
        if fehlt:
            text.append("in der Zuordnungsliste der Musterlösung nicht enthalten (Absicht? sonst ergänzen): " + ", ".join(fehlt))
    if not sm_listen and not lm_listen:
        befunde.append(Befund("T.5", "Zuordnungslisten eindeutig und stimmig", "➖", "keine Zuordnungsliste erkannt"))
    else:
        befunde.append(Befund("T.5", "Zuordnungslisten eindeutig und stimmig", "❌" if schwer else ("⚠" if text else "✅"),
                              "; ".join(text) or "Operanden eindeutig, Vorgabe und Musterlösung stimmig"))

    # T.6 Schreibweise
    gemischt = [f"{k}: " + " / ".join(sorted(v)) for k, v in sorted(schreibweisen.items()) if len(v) > 1]
    if standard:
        roh = sm_flach + "\n" + lm_text
        # „Q1“ als Ausgang der Kleinsteuerung neben dem Schütz -Q1 ist kein Kennzeichen ohne Bindestrich
        operanden = {op.upper() for liste in sm_listen + lm_listen for z in liste["zeilen"].values()
                     for op in z["operanden"].values()}
        for k in sorted(orte):
            if k[1:].upper() in operanden:
                continue
            ohne_strich = re.findall(rf"(?<![\w\-–]){re.escape(k[1:])}(?![\w])", roh)
            if ohne_strich:
                gemischt.append(f"{k} auch ohne Bindestrich ({len(ohne_strich)}×)")
        alt = sorted(set(ALT.findall(roh)))
        if alt:
            gemischt.append("alte Kennzeichnung daneben: " + ", ".join(alt))
    befunde.append(Befund("T.6", "BMK-Schreibweise einheitlich", "⚠" if gemischt else "✅",
                          "; ".join(gemischt) or "einheitlich"))

    # T.7 Grundstellung, Start, Stopp
    if hat_fb or sm_listen:
        fehlt = [w for w, rx in (("Grundstellung", GRUND), ("Start", START), ("Stopp/Not-Halt", STOPP)) if not rx.search(sm_flach)]
        befunde.append(Befund("T.7", "Grundstellung, Start, Stopp/Not-Halt beschrieben", "⚠" if fehlt else "✅",
                              ("nicht beschrieben: " + ", ".join(fehlt) + " – beschreiben oder ausdrücklich ausklammern")
                              if fehlt else "beschrieben"))

    # T.8 Kennbuchstaben nach DIN EN IEC 81346-2
    if standard:
        t8, info["ausgabe_81346"] = pruefe_kennbuchstaben(sorted(orte), _ohne_kopf(sm, notation=True),
                                                          _ohne_kopf(lm, notation=True) if lm else "")
        befunde.append(t8)
    else:
        befunde.append(Befund("T.8", "Kennbuchstaben nach DIN EN IEC 81346-2", "➖",
                              "eigenes Kennzeichenmuster – Kennbuchstaben nicht geprüft"))

    # T.9 GRAFCET in Textform
    befunde.append(pruefe_grafcet(sm_flach, lm_text))

    for k in sorted(orte, key=lambda x: (re.sub(r"\d", "", x), int(re.sub(r"\D", "", x) or 0))):
        kontakt = "/".join(sorted(arten.get(k, set()) | lm_arten.get(k, set()))) or ("Signal" if k in signal else "–")
        info["bmk"][k] = {"orte": sorted(orte[k]), "kontakt": kontakt}
    return befunde, info


# ───────────────────────────── Ausgabe ─────────────────────────────

ORTE = [("F", "Funktionsbeschreibung"), ("L", "Legende/Schema"), ("Z", "Zuordnungsliste SM"),
        ("A", "Aufgaben"), ("M", "Anlagen"), ("E", "übriger SM-Text"), ("LM", "Lehrermaterial")]


def markdown(befunde: list[Befund], info: dict) -> str:
    z = ["### BMK-Abgleich (Steuerungstechnik)", "",
         "| Krit. | Kriterium | Status | Befund |", "|---|---|---|---|"]
    z += [f"| {b.kriterium} | {b.name} | {b.status} | {b.befund} |" for b in befunde]
    if info.get("bmk"):
        z += ["", "| BMK | " + " | ".join(n for _, n in ORTE) + " | Kontaktart |",
              "|---|" + "---|" * (len(ORTE) + 1)]
        for k, d in info["bmk"].items():
            z.append(f"| {k} | " + " | ".join("✓" if o in d["orte"] else "" for o, _ in ORTE) + f" | {d['kontakt']} |")
    z += ["", "_Regelbasierter Abgleich der Textfassung. Kennzeichen in Bildern prüft die Lehrkraft "
          "gegen die Legende._"]
    return "\n".join(z)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Betriebsmittelkennzeichen in Schüler- und Lehrermaterial abgleichen (lokal).")
    p.add_argument("schuelermaterial", type=Path)
    p.add_argument("lehrermaterial", type=Path, nargs="?")
    p.add_argument("--bmk-muster", default=None,
                   help="regulärer Ausdruck für ein Kennzeichen (Standard: -[A-Z]{1,3}[0-9]{1,3}, z. B. -SJ1)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    sm = lies_text(a.schuelermaterial)
    lm = lies_text(a.lehrermaterial) if a.lehrermaterial else None
    befunde, info = pruefe_bmk(sm, lm, a.bmk_muster)
    if a.json:
        print(json.dumps({"befunde": [asdict(b) for b in befunde], "info": info}, ensure_ascii=False, indent=2))
    else:
        print(markdown(befunde, info))
    return 1 if any(b.status == "❌" for b in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
