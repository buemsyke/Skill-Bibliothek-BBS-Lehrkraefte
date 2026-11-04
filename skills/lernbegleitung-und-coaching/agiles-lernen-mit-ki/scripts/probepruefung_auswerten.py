#!/usr/bin/env python3
"""probepruefung_auswerten – zählt eine Probeprüfung zur Selbstkontrolle deterministisch aus.

Sprachmodelle verzählen sich beim Auswerten („3 von 5 … nein warte … 2 von 5"). Dieses Skript
liest die Auswertungstabelle einer Probeprüfung – eine Markdown-Tabelle mit mindestens den
Spalten „Lösung" und „Antwort", optional „Nr.", „Kapitel" (bzw. „Thema") und „Fundstelle" –
und rechnet:

  Ergebnis     richtig / gesamt, beantwortet, offen; Quote in Prozent
  Kapitel      richtig / gesamt je Kapitel, Kapitel unter der Schwelle → wiederholen
  Vorschlag    Review erreicht (≥ 80 %) · teilweise (≥ 60 %) · nicht erreicht – entscheiden
               muss die lernende Person
  Hinweise     Lösung ohne Fundstelle (Lösung an der Quelle prüfen), doppelte Nummern

Antworten: Buchstaben („c"), Mehrfachauswahl („a,c" oder „a c" – Reihenfolge egal), wahr/falsch
(„w"/„f", „wahr"/„falsch"), Zahlen („2,5" = „2.5"). Leere Antwort oder „–" = nicht beantwortet.

Aufruf:
    python3 probepruefung_auswerten.py DATEI.md [--pruefung P1] [--erreicht 80] [--teilweise 60]
        [--json]

--pruefung wählt die Tabelle unter einer Überschrift, die den Text enthält (bei mehreren
Probeprüfungen in einer Datei). Ausgabe: Markdown zum Einfügen in Probeprüfung und Lernakte.

Exit 0 = ausgewertet, 1 = Zeilen ohne Lösung (nicht auswertbar), 2 = keine Auswertungstabelle.
Selbstkontrolle, keine Note. Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

WAHR = {"w", "wahr", "richtig", "true", "ja", "j"}
FALSCH = {"f", "falsch", "false", "nein", "n"}
LEER = {"", "-", "–", "—", "?", "offen"}
SPALTEN = {
    "nr": ("nr", "nr.", "nummer", "#", "frage"),
    "kapitel": ("kapitel", "kap", "kap.", "thema", "modul", "lernziel"),
    "loesung": ("lösung", "loesung", "schlüssel", "richtig", "korrekt"),
    "antwort": ("antwort", "deine antwort", "eingabe", "gewählt"),
    "fundstelle": ("fundstelle", "quelle", "beleg", "seite"),
}


class Eingabefehler(Exception):
    pass


def _zellen(zeile: str) -> list[str]:
    inhalt = zeile.strip()
    if inhalt.startswith("|"):
        inhalt = inhalt[1:]
    if inhalt.endswith("|"):
        inhalt = inhalt[:-1]
    return [z.strip() for z in inhalt.split("|")]


def _spaltenname(kopf: str) -> str | None:
    k = re.sub(r"[*_`]", "", kopf).strip().lower()
    for name, varianten in SPALTEN.items():
        if k in varianten:
            return name
    return None


def tabellen(text: str) -> list[dict]:
    """Alle Markdown-Tabellen mit Überschriften-Kontext: {ueberschriften, kopf, zeilen}."""
    ergebnis: list[dict] = []
    stapel: list[tuple[int, str]] = []
    zeilen = text.splitlines()
    i = 0
    while i < len(zeilen):
        z = zeilen[i]
        m = re.match(r"^(#{1,6})\s+(.*)$", z)
        if m:
            ebene = len(m.group(1))
            stapel = [(e, t) for e, t in stapel if e < ebene] + [(ebene, m.group(2).strip())]
        if z.lstrip().startswith("|") and i + 1 < len(zeilen) and re.match(r"^\s*\|?\s*:?-{2,}", zeilen[i + 1]):
            kopf = _zellen(z)
            koerper = []
            i += 2
            while i < len(zeilen) and zeilen[i].lstrip().startswith("|"):
                koerper.append(_zellen(zeilen[i]))
                i += 1
            ergebnis.append({"ueberschriften": [t for _, t in stapel], "kopf": kopf, "zeilen": koerper})
            continue
        i += 1
    return ergebnis


def auswertungstabelle(text: str, pruefung: str | None = None) -> tuple[dict, dict[str, int]]:
    for t in tabellen(text):
        index = {}
        for nr, k in enumerate(t["kopf"]):
            name = _spaltenname(k)
            if name and name not in index:
                index[name] = nr
        if "loesung" not in index or "antwort" not in index:
            continue
        if pruefung and not any(pruefung.lower() in u.lower() for u in t["ueberschriften"]):
            continue
        return t, index
    hinweis = f" unter einer Überschrift mit „{pruefung}“" if pruefung else ""
    raise Eingabefehler(f"keine Tabelle mit den Spalten „Lösung“ und „Antwort“{hinweis} gefunden")


def _ist_wahr_falsch(werte: frozenset | None) -> bool:
    return bool(werte) and len(werte) == 1 and next(iter(werte)) in WAHR | FALSCH


def normalisiere(wert: str, wahr_falsch: bool = False) -> frozenset | None:
    s = re.sub(r"[*_`]", "", wert or "").strip().lower()
    if s in LEER:
        return None
    if re.search(r"\d", s):
        zahl = re.sub(r"\s+", "", s).replace(",", ".")
        return frozenset({zahl})
    teile = [t.strip(").:") for t in re.split(r"[,;/+\s]+|\bund\b", s) if t.strip(").:")]
    if wahr_falsch:
        teile = ["wahr" if t in WAHR else "falsch" if t in FALSCH else t for t in teile]
    return frozenset(teile) if teile else None


def _zelle(zeile: list[str], index: dict[str, int], name: str) -> str:
    nr = index.get(name)
    return zeile[nr].strip() if nr is not None and nr < len(zeile) else ""


def auswerten(text: str, pruefung: str | None = None, erreicht: float = 80.0,
              teilweise: float = 60.0) -> dict:
    tabelle, index = auswertungstabelle(text, pruefung)
    fragen, hinweise, fehler = [], [], []
    gesehen: set[str] = set()
    for lfd, zeile in enumerate(tabelle["zeilen"], start=1):
        if not any(zeile):
            continue
        nr = _zelle(zeile, index, "nr") or str(lfd)
        if re.match(r"^\s*(?:σ|∑|summe|gesamt)", nr, re.I):
            continue
        if nr in gesehen:
            hinweise.append(f"Frage {nr}: Nummer doppelt")
        gesehen.add(nr)
        loesung_roh = _zelle(zeile, index, "loesung")
        antwort_roh = _zelle(zeile, index, "antwort")
        kapitel = _zelle(zeile, index, "kapitel") or "–"
        fundstelle = _zelle(zeile, index, "fundstelle")
        roh_loesung = normalisiere(loesung_roh)
        wf = _ist_wahr_falsch(roh_loesung)
        loesung = normalisiere(loesung_roh, wf)
        antwort = normalisiere(antwort_roh, wf)
        if loesung is None:
            fehler.append(f"Frage {nr}: keine Lösung eingetragen – nicht auswertbar")
            status = "ohne Lösung"
        elif antwort is None:
            status = "offen"
        else:
            status = "richtig" if antwort == loesung else "falsch"
        if loesung is not None and not fundstelle:
            hinweise.append(f"Frage {nr}: Lösung ohne Fundstelle – an der Quelle prüfen")
        fragen.append({"nr": nr, "kapitel": kapitel, "loesung": loesung_roh, "antwort": antwort_roh,
                       "status": status, "fundstelle": fundstelle})
    if not fragen:
        raise Eingabefehler("Auswertungstabelle ohne Zeilen")
    wertbar = [f for f in fragen if f["status"] != "ohne Lösung"]
    gesamt = len(wertbar)
    richtig = sum(f["status"] == "richtig" for f in wertbar)
    offen = sum(f["status"] == "offen" for f in wertbar)
    quote = round(100 * richtig / gesamt, 1) if gesamt else 0.0
    kapitel: dict[str, dict] = {}
    for f in wertbar:
        k = kapitel.setdefault(f["kapitel"], {"richtig": 0, "gesamt": 0, "fundstellen": []})
        k["gesamt"] += 1
        k["richtig"] += f["status"] == "richtig"
        if f["status"] != "richtig" and f["fundstelle"] and f["fundstelle"] not in k["fundstellen"]:
            k["fundstellen"].append(f["fundstelle"])
    for k in kapitel.values():
        k["quote"] = round(100 * k["richtig"] / k["gesamt"], 1)
    wiederholen = [name for name, k in kapitel.items() if k["quote"] < erreicht]
    if quote >= erreicht:
        vorschlag = "erreicht"
    elif quote >= teilweise:
        vorschlag = "teilweise"
    else:
        vorschlag = "nicht erreicht"
    titel = pruefung or next((u for u in reversed(tabelle["ueberschriften"]) if re.search(r"\bP\d+\b", u)), "")
    kennung = (re.search(r"\bP\d+\b", titel) or re.search(r"\bP\d+\b", text))
    return {"kennung": kennung.group(0) if kennung else "P", "fragen": fragen, "gesamt": gesamt,
            "richtig": richtig, "beantwortet": gesamt - offen, "offen": offen, "quote": quote,
            "kapitel": kapitel, "wiederholen": wiederholen, "vorschlag": vorschlag,
            "schwellen": {"erreicht": erreicht, "teilweise": teilweise},
            "hinweise": hinweise, "fehler": fehler}


def _prozent(wert: float) -> str:
    return f"{wert:.0f} %" if float(wert).is_integer() else f"{wert:.1f} %".replace(".", ",")


def ausgabe(erg: dict) -> str:
    zeichen = {"richtig": "✓", "falsch": "✗", "offen": "–", "ohne Lösung": "?"}
    z = [f"## Ergebnis {erg['kennung']} (ausgewertet mit probepruefung_auswerten.py)", "",
         "| Nr. | Kapitel | Lösung | Antwort | Ergebnis | Fundstelle |", "|---|---|---|---|---|---|"]
    for f in erg["fragen"]:
        z.append(f"| {f['nr']} | {f['kapitel']} | {f['loesung']} | {f['antwort'] or '–'} | "
                 f"{zeichen[f['status']]} | {f['fundstelle'] or '–'} |")
    z += ["", f"**{erg['richtig']} von {erg['gesamt']} richtig ({_prozent(erg['quote'])})** · "
              f"beantwortet {erg['beantwortet']} · offen {erg['offen']}", ""]
    if len(erg["kapitel"]) > 1 or "–" not in erg["kapitel"]:
        z += ["| Kapitel | richtig | Quote |", "|---|---|---|"]
        for name, k in erg["kapitel"].items():
            z.append(f"| {name} | {k['richtig']}/{k['gesamt']} | {_prozent(k['quote'])} |")
        z.append("")
    s = erg["schwellen"]
    z.append(f"Vorschlag Review: **{erg['vorschlag']}** (erreicht ab {_prozent(s['erreicht'])}, "
             f"teilweise ab {_prozent(s['teilweise'])}) – die Entscheidung trifft die lernende Person.")
    if erg["wiederholen"]:
        teile = []
        for name in erg["wiederholen"]:
            fund = erg["kapitel"][name]["fundstellen"]
            teile.append(name + (f" ({', '.join(fund)})" if fund else ""))
        z.append("Wiederholen: " + "; ".join(teile))
    for h in erg["hinweise"]:
        z.append(f"⚠ {h}")
    for e in erg["fehler"]:
        z.append(f"❌ {e}")
    wdh = ", ".join(erg["wiederholen"]) if erg["wiederholen"] else "–"
    z += ["", "Für die Lernakte:",
          f"- **Beleg:** {erg['kennung']} {erg['richtig']}/{erg['gesamt']} richtig "
          f"({_prozent(erg['quote'])}) · wiederholen: {wdh}",
          "", "Selbstkontrolle, keine Note."]
    return "\n".join(z) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Probeprüfung deterministisch auszählen (Selbstkontrolle).")
    p.add_argument("datei", type=Path, help="Probeprüfung bzw. Lernakte (Markdown) mit Auswertungstabelle")
    p.add_argument("--pruefung", default=None, help="Tabelle unter einer Überschrift mit diesem Text, z. B. P2")
    p.add_argument("--erreicht", type=float, default=80.0, help="Quote für „erreicht“ (Standard 80)")
    p.add_argument("--teilweise", type=float, default=60.0, help="Quote für „teilweise“ (Standard 60)")
    p.add_argument("--json", action="store_true", help="Ergebnis als JSON")
    a = p.parse_args(argv)
    try:
        erg = auswerten(a.datei.read_text(encoding="utf-8"), a.pruefung, a.erreicht, a.teilweise)
    except (Eingabefehler, OSError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(erg, ensure_ascii=False, indent=2))
    else:
        print(ausgabe(erg), end="")
    return 1 if erg["fehler"] else 0


if __name__ == "__main__":
    sys.exit(main())
