#!/usr/bin/env python3
"""CLI: ``edu-quiz`` – eine Markdown-Quelle → GIFT und/oder H5P.

    edu-quiz QUELLE [QUELLE ...] [--to {gift,h5p,both}] [-o ORDNER] [--category CAT]

QUELLE ist eine ``.md``-Datei oder ein Ordner (dann alle ``*.md`` außer
README). Default schreibt **beide** Formate neben die Quelle.
"""

import argparse
import sys
from pathlib import Path

from .core import convert_file


def _collect_sources(quellen: list[str]) -> list[Path]:
    files: list[Path] = []
    for q in quellen:
        p = Path(q)
        if p.is_dir():
            files.extend(sorted(
                f for f in p.glob("*.md") if f.name.lower() != "readme.md"
            ))
        elif p.is_file():
            files.append(p)
        else:
            print(f"⚠ Übersprungen (nicht gefunden): {q}", file=sys.stderr)
    return files


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="edu-quiz",
        description="Erzeugt aus einer Markdown-Quizquelle GIFT- und/oder "
                    "H5P-Dateien (ein Quellformat, mehrere Ziele).",
    )
    parser.add_argument("quelle", nargs="+",
                        help=".md-Datei(en) oder Ordner mit *.md.")
    parser.add_argument("--to", choices=("gift", "h5p", "both"), default="both",
                        help="Zielformat(e). Default: both.")
    parser.add_argument("-o", "--out", default=None,
                        help="Zielordner (Default: neben der Quelle).")
    parser.add_argument("--category", default=None,
                        help="Moodle-Kategorie für die GIFT-Datei ($CATEGORY:).")
    args = parser.parse_args(argv)

    formats = ("gift", "h5p") if args.to == "both" else (args.to,)
    sources = _collect_sources(args.quelle)
    if not sources:
        print("Keine Quelldateien gefunden.", file=sys.stderr)
        sys.exit(1)

    total = 0
    for src in sources:
        written = convert_file(src, args.out, formats=formats, category=args.category)
        if written:
            for w in written:
                print(f"✓ {w}")
            total += len(written)
        else:
            print(f"⚠ Keine Fragen in {src.name} – nichts geschrieben.")

    if not total:
        sys.exit(1)
    print(f"\n✅ {total} Datei(en) erzeugt.")


if __name__ == "__main__":
    main()
