#!/usr/bin/env python3
"""CLI für den didaktischen Qualitätscheck: ``edu-check``.

  edu-check bloom quiz.md                    # Bloom-Streuung der Verben
  edu-check phasen plan.md                   # Vorwissen, Inputlänge, Phasen
  edu-check effektiv konzeption.md           # EFFEKTIV-Kriterien (NLQ/Sims)
  edu-check alles konzeption.md --md report.md

Eingabe: Markdown (Konzeption, Verlaufsplan, Quizquelle, Klausur).
Ausgabe: Hinweise (keine Urteile); optional Markdown-Report via ``--md``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import bericht_markdown, bloom_analyse, effektiv_check, phasen_analyse


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="edu-check",
        description="Didaktischer Qualitätscheck nach den FfF-Prinzipien "
                    "(Bloom-Streuung, Phasenverschränkung, EFFEKTIV).",
    )
    p.add_argument("modus", choices=["bloom", "phasen", "effektiv", "alles"],
                   help="Prüfmodus")
    p.add_argument("datei", type=Path, help="Markdown-Datei")
    p.add_argument("--md", type=Path, default=None,
                   help="Bericht zusätzlich als Markdown-Datei speichern")

    args = p.parse_args(argv)
    if not args.datei.exists():
        print(f"Datei nicht gefunden: {args.datei}", file=sys.stderr)
        return 2
    text = args.datei.read_text(encoding="utf-8")

    bloom = bloom_analyse(text) if args.modus in ("bloom", "alles") else None
    phasen = phasen_analyse(text) if args.modus in ("phasen", "alles") else None
    effektiv = effektiv_check(text) if args.modus in ("effektiv", "alles") else None

    bericht = bericht_markdown(args.datei.name, bloom, phasen, effektiv)
    print(bericht)
    if args.md:
        args.md.write_text(bericht, encoding="utf-8")
        print(f"Bericht gespeichert: {args.md}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
