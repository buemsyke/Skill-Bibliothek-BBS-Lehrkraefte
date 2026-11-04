#!/usr/bin/env python3
"""lesbarkeit – Lesbarkeitskennzahlen für deutschsprachiges Unterrichtsmaterial.

Misst für Markdown- oder Textdateien:
  * LIX (Björnsson): durchschnittliche Satzlänge + Anteil langer Wörter (> 6 Buchstaben) in %
  * durchschnittliche Satzlänge, Anteil Sätze über 20 Wörter (mit Fundstellen)
  * Nominalstil-Hinweis (Wörter auf -ung/-heit/-keit/-ion/-ität je 100 Wörter)
  * mögliche Passiv- und „ist zu"-Konstruktionen
  * sehr lange Wörter (Komposita ab 16 Buchstaben)

Liest Markdown/Text sowie DOCX, ODT und PDF (über text_lesen.py im selben Ordner).
Zeilen ohne Wort (leere Tabellennummern, Seitenzahlen, Trennlinien) und Zeilen ohne Satzzeichen
mit weniger als vier Wörtern (Tabellenzellen, Überschriften, Beschriftungen) zählen nicht als Satz.

Aufruf:
    python3 lesbarkeit.py material.md                 # eine Datei (auch .docx, .odt, .pdf)
    python3 lesbarkeit.py vorher.md nachher.md        # Vergleich (genau zwei Dateien)
    python3 lesbarkeit.py material.md --json
    python3 lesbarkeit.py material.md --nur-schuelerteil   # ab "# Lösungen…"/"# Didaktische Hinweise" abschneiden

Ignoriert YAML-Kopf, Codeblöcke, HTML-Kommentare, Überschriften und Tabellen.
Nur Python-Standardbibliothek. Kennzahlen sind Orientierung, kein Urteil.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from text_lesen import lies_text          # DOCX/ODT/PDF (text_lesen.py aus _gemeinsam)
except ImportError:  # pragma: no cover – ohne Hilfsmodul nur Markdown/Text
    def lies_text(pfad: Path) -> str:
        return Path(pfad).read_text(encoding="utf-8", errors="replace")

ABKUERZUNGEN = [
    "z. B.", "z.B.", "d. h.", "d.h.", "u. a.", "u.a.", "o. Ä.", "u. U.", "i. O.", "n. i. O.",
    "ggf.", "bzw.", "ca.", "Nr.", "usw.", "evtl.", "vgl.", "S.", "Abb.", "Tab.", "inkl.", "max.",
    "min.", "Std.", "lt.", "Fa.", "Hr.", "Fr.", "Dr.", "bzgl.", "etc.", "Kap.", "Bd.", "Aufl.",
    "zzgl.", "sog.", "s.", "u.", "v.", "Mio.", "Mrd.", "Jh.", "gem.", "einschl.",
]
PLATZHALTER = "․"  # „one dot leader" – ersetzt Punkte in Abkürzungen

WORT_RE = re.compile(r"[A-Za-zÄÖÜäöüß]+(?:-[A-Za-zÄÖÜäöüß]+)*|\d+(?:[.,]\d+)?")
NOMINAL_RE = re.compile(r"\b\w+(?:ung|heit|keit|ion|ität)(?:en)?\b", re.IGNORECASE)
PASSIV_RE = re.compile(
    r"\b(?:wird|werden|wurde|wurden|worden)\b[^.!?]*?\b(?:ge\w+(?:t|en)|\w+iert)\b",
    re.IGNORECASE)
ISTZU_RE = re.compile(
    r"\b(?:ist|sind|war|waren)\s+(?:\w+\s+){0,5}zu\s+\w+n\b"  # ist … zu sichern
    r"|\b\w+zu\w+n\s+(?:ist|sind|war|waren)\b",              # durchzuführen ist
    re.IGNORECASE)
LEHRERTEIL_RE = re.compile(r"^#\s+(?:Lösungen|Didaktische Hinweise)", re.MULTILINE)


def bereinige_markdown(text: str, nur_schuelerteil: bool = False) -> list[tuple[int, str]]:
    """Gibt (Zeilennummer, Fließtext) für zählbare Zeilen zurück."""
    if nur_schuelerteil:
        m = LEHRERTEIL_RE.search(text)
        if m:
            text = text[: m.start()]
    text = re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.DOTALL)
    zeilen: list[tuple[int, str]] = []
    im_code = in_yaml = False
    for nr, zeile in enumerate(text.splitlines(), start=1):
        s = zeile.strip()
        if nr == 1 and s == "---":
            in_yaml = True
            continue
        if in_yaml:
            in_yaml = s != "---"
            continue
        if s.startswith("```"):
            im_code = not im_code
            continue
        if im_code or not s or s.startswith(("#", "|", "---", "***")):
            continue
        s = re.sub(r"^\s*(?:>\s*)+", "", s)                    # Zitat
        s = re.sub(r"^\s*(?:[-*+•]|\d+[.)]|[a-z][.)])\s+", "", s)  # Listenzeichen
        s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)              # Bilder
        s = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", s)          # Links -> Text
        s = re.sub(r"[*`~]+|(?<![\w])_+|_+(?![\w])", "", s)  # Hervorhebungen, nicht Unterstriche im Wort
        s = re.sub(r"\[(?:ABBILDUNG|🔎|⚠️)[^\]]*\]", "", s)      # Platzhalter
        if s:
            zeilen.append((nr, s))
    return zeilen


def saetze(zeilen: list[tuple[int, str]]) -> list[tuple[int, str]]:
    """Zerlegt in Sätze; Listenpunkte ohne Satzzeichen gelten als eigener Satz."""
    ergebnis: list[tuple[int, str]] = []
    for nr, z in zeilen:
        for abk in ABKUERZUNGEN:
            z = z.replace(abk, abk.replace(".", PLATZHALTER))
        z = re.sub(r"(\d)\.(\d)", rf"\1{PLATZHALTER}\2", z)
        teile = re.split(r"(?<=[.!?:;])\s+(?=[A-ZÄÖÜ0-9„\"(])", z)
        for t in teile:
            t = t.replace(PLATZHALTER, ".").strip()
            if not re.search(r"[A-Za-zÄÖÜäöüß]{2,}", t):   # nur Zahlen (Tabellennummer, Seite)
                continue
            if not re.search(r"[.!?:;]\s*$", t) and len(WORT_RE.findall(t)) < 4:
                continue                                    # Zelle, Überschrift, Beschriftung
            ergebnis.append((nr, t))
    return ergebnis


def kennzahlen(text: str, nur_schuelerteil: bool = False) -> dict:
    s = saetze(bereinige_markdown(text, nur_schuelerteil))
    woerter = [w for _, satz in s for w in WORT_RE.findall(satz)]
    n_w, n_s = len(woerter), len(s)
    if n_w == 0 or n_s == 0:
        return {"saetze": n_s, "woerter": n_w, "lix": None, "hinweis": "kein Fließtext gefunden"}
    lang = [w for w in woerter if len(re.sub(r"[^A-Za-zÄÖÜäöüß]", "", w)) > 6]
    satzlaengen = [(nr, len(WORT_RE.findall(t)), t) for nr, t in s]
    lange_saetze = [(nr, n, t) for nr, n, t in satzlaengen if n > 20]
    volltext = " ".join(t for _, t in s)
    lix = n_w / n_s + 100 * len(lang) / n_w
    return {
        "saetze": n_s,
        "woerter": n_w,
        "lix": round(lix, 1),
        "lix_einordnung": einordnung(lix),
        "mittlere_satzlaenge": round(n_w / n_s, 1),
        "anteil_lange_woerter": round(100 * len(lang) / n_w, 1),
        "saetze_ueber_20_woerter": len(lange_saetze),
        "anteil_saetze_ueber_20": round(100 * len(lange_saetze) / n_s, 1),
        "nominalstil_je_100_woerter": round(100 * len(NOMINAL_RE.findall(volltext)) / n_w, 1),
        "passiv_hinweise": len(PASSIV_RE.findall(volltext)),
        "ist_zu_konstruktionen": len(ISTZU_RE.findall(volltext)),
        "sehr_lange_woerter": sorted({w for w in woerter if len(w) >= 16}, key=len, reverse=True)[:15],
        "lange_saetze": [{"zeile": nr, "woerter": n, "satz": t[:160]}
                         for nr, n, t in sorted(lange_saetze, key=lambda x: -x[1])[:10]],
    }


def einordnung(lix: float) -> str:
    if lix < 40:
        return "leicht"
    if lix < 50:
        return "mittel"
    if lix < 60:
        return "schwer"
    return "sehr schwer"


ZEILEN = [
    ("LIX", "lix"), ("Einordnung", "lix_einordnung"), ("Sätze", "saetze"), ("Wörter", "woerter"),
    ("mittlere Satzlänge (Wörter)", "mittlere_satzlaenge"),
    ("Anteil lange Wörter (%)", "anteil_lange_woerter"),
    ("Sätze > 20 Wörter", "saetze_ueber_20_woerter"),
    ("Anteil Sätze > 20 Wörter (%)", "anteil_saetze_ueber_20"),
    ("Nominalstil je 100 Wörter", "nominalstil_je_100_woerter"),
    ("mögliche Passivsätze", "passiv_hinweise"), ('„ist zu“-Konstruktionen', "ist_zu_konstruktionen"),
]


def markdown_einzeln(name: str, k: dict) -> str:
    if k.get("lix") is None:
        return f"**{name}:** {k['hinweis']}"
    out = [f"### Lesbarkeit: {name}", "", "| Kennzahl | Wert |", "|---|---|"]
    out += [f"| {label} | {k[key]} |" for label, key in ZEILEN]
    if k["lange_saetze"]:
        out += ["", "**Längste Sätze:**"]
        out += [f"- Z. {x['zeile']} ({x['woerter']} Wörter): {x['satz']}" for x in k["lange_saetze"]]
    if k["sehr_lange_woerter"]:
        out += ["", "**Sehr lange Wörter:** " + ", ".join(k["sehr_lange_woerter"])]
    out += ["", "_LIX: < 40 leicht · 40–50 mittel · 50–60 schwer · > 60 sehr schwer. "
            "Fachtexte liegen wegen langer Fachwörter höher; entscheidend ist die Veränderung. "
            "Listenpunkte ohne Satzzeichen zählen als eigene Sätze (senkt die mittlere Satzlänge)._"]
    return "\n".join(out)


def markdown_vergleich(a: str, ka: dict, b: str, kb: dict) -> str:
    out = ["### Lesbarkeit vorher/nachher", "", f"| Kennzahl | {a} | {b} |", "|---|---|---|"]
    out += [f"| {label} | {ka.get(key, '–')} | {kb.get(key, '–')} |" for label, key in ZEILEN]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Lesbarkeitskennzahlen (LIX u. a.) für Material.")
    p.add_argument("dateien", nargs="+", type=Path, help="eine Datei oder zwei zum Vergleich")
    p.add_argument("--json", action="store_true")
    p.add_argument("--nur-schuelerteil", action="store_true",
                   help="Text ab '# Lösungen…' bzw. '# Didaktische Hinweise' ignorieren")
    args = p.parse_args(argv)
    if len(args.dateien) > 2:
        p.error("höchstens zwei Dateien (vorher, nachher)")
    ergebnisse = {}
    for d in args.dateien:
        if not d.is_file():
            print(f"Datei nicht gefunden: {d}", file=sys.stderr)
            return 2
        ergebnisse[d.name] = kennzahlen(lies_text(d), args.nur_schuelerteil)
    if args.json:
        print(json.dumps(ergebnisse, ensure_ascii=False, indent=2))
    elif len(ergebnisse) == 2:
        (a, ka), (b, kb) = ergebnisse.items()
        print(markdown_vergleich(a, ka, b, kb))
        print()
        print(markdown_einzeln(b, kb))
    else:
        (a, ka), = ergebnisse.items()
        print(markdown_einzeln(a, ka))
    return 0


if __name__ == "__main__":
    sys.exit(main())
