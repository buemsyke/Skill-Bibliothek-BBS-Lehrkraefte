#!/usr/bin/env python3
"""freigabe_pruefen – Gate: Hat die Lehrkraft die Korrekturvorschläge freigegeben?

KI- oder werkzeuggestützte Korrekturen sind Vorschläge. Erst nach Durchsicht trägt die
Lehrkraft in jede Datei eine Freigabezeile ein:

    Freigabe: erteilt – MH, 2026-10-09

(Kürzel und Datum; Bindestrich oder Gedankenstrich; Datum TT.MM.JJJJ oder JJJJ-MM-TT.)
Solange „Freigabe: ausstehend" oder keine Zeile drinsteht, gilt die Datei als nicht
freigegeben. Folge-Schritte (Auswertung, Weitergabe, Veröffentlichung) laufen nur auf
freigegebenen Dateien.

Aufruf:
    python3 freigabe_pruefen.py PFAD [PFAD …] [--muster "korrektur_*.md"] [--json]

Exit-Code 0 = alles freigegeben, 1 = mindestens eine Datei offen. Gibt nur Dateinamen,
Kürzel und Datum aus – keine Inhalte. Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

FREIGABE = re.compile(
    r"^\s*(?:[>*\-]\s*)?\**Freigabe\**\s*:\s*\**erteilt\**\s*[-–—]\s*"
    r"(?P<kuerzel>[A-Za-zÄÖÜäöüß]{1,6})\s*,\s*"
    r"(?P<datum>\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{2,4})\s*$",
    re.MULTILINE,
)
AUSSTEHEND = re.compile(r"^\s*(?:[>*\-]\s*)?\**Freigabe\**\s*:\s*\**ausstehend", re.MULTILINE | re.IGNORECASE)


def pruefe_datei(pfad: Path) -> dict:
    text = pfad.read_text(encoding="utf-8", errors="replace")
    m = FREIGABE.search(text)
    if m:
        return {"datei": pfad.name, "freigegeben": True, "kuerzel": m["kuerzel"], "datum": m["datum"]}
    status = "ausstehend" if AUSSTEHEND.search(text) else "keine Freigabezeile"
    return {"datei": pfad.name, "freigegeben": False, "status": status}


def sammle(pfade: list[Path], muster: str) -> list[Path]:
    dateien: list[Path] = []
    for p in pfade:
        if p.is_dir():
            dateien += sorted(p.glob(muster))
        elif p.is_file():
            dateien.append(p)
    return dateien


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Freigabezeilen in Korrekturdateien prüfen.")
    ap.add_argument("pfade", nargs="+", type=Path)
    ap.add_argument("--muster", default="korrektur_*.md", help="Dateimuster in Ordnern")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    dateien = sammle(a.pfade, a.muster)
    if not dateien:
        print("Keine Dateien gefunden.", file=sys.stderr)
        return 1
    erg = [pruefe_datei(d) for d in dateien]
    offen = [e for e in erg if not e["freigegeben"]]
    if a.json:
        print(json.dumps({"dateien": erg, "alle_freigegeben": not offen}, ensure_ascii=False, indent=2))
    else:
        print(f"Freigegeben: {len(erg) - len(offen)} von {len(erg)}")
        for e in offen:
            print(f"  ⏳ {e['datei']}: {e['status']}")
        print("Ergebnis: " + ("✅ alle freigegeben" if not offen else "⛔ Folge-Schritte erst nach Freigabe"))
    return 0 if not offen else 1


if __name__ == "__main__":
    sys.exit(main())
