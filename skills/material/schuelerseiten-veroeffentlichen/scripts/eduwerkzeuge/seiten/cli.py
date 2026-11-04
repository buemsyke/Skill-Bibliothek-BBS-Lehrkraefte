#!/usr/bin/env python3
"""CLI für die Schülerausgaben: ``edu-seiten``.

Unterbefehle:
  edu-seiten split  [--config ...] [--out ...] [--project-root ...] [--no-resources]
        Zerlegt lessons/XX_*/lesson.md in LMS-Phasen-Seiten (Default-Befehl).

  edu-seiten strip  --teacher DIR --student DIR --lf NAME=datei1.md,datei2.md ...
        Entfernt Lehrer-Abschnitte aus Lektionsdateien.
"""

import argparse
from pathlib import Path

from .core import generate_student_site, run_split


def _add_split(sub) -> None:
    p = sub.add_parser("split", help="Schülerausgabe aus lesson.md-Dateien erzeugen.")
    p.add_argument("--config", type=Path, default=None,
                   help="Pfad zur phase_config.yaml (Standard: scripts/phase_config.yaml bzw. mitgeliefert).")
    p.add_argument("--out", type=Path, default=None,
                   help="Ausgabeverzeichnis (Standard: _student_site/).")
    p.add_argument("--project-root", type=Path, default=None,
                   help="Projektwurzel (Standard: aktuelles Verzeichnis).")
    p.add_argument("--no-resources", action="store_true",
                   help="Keine Ressourcen (h5p, solutions, examples) kopieren.")


def _add_strip(sub) -> None:
    p = sub.add_parser("strip", help="Lehrer-Abschnitte aus Lektionsdateien entfernen.")
    p.add_argument("--teacher", type=Path, required=True, help="Wurzelverzeichnis der Lehrerdateien.")
    p.add_argument("--student", type=Path, required=True, help="Zielverzeichnis der Schülerdateien.")
    p.add_argument("--lf", action="append", default=[], metavar="NAME=datei1.md,datei2.md",
                   help="Lernfeld-Ordner und seine Dateien (mehrfach angebbar).")


def _parse_lf(entries: list[str]) -> dict[str, list[str]]:
    lernfelder: dict[str, list[str]] = {}
    for entry in entries:
        name, _, files = entry.partition("=")
        lernfelder[name.strip()] = [f.strip() for f in files.split(",") if f.strip()]
    return lernfelder


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="edu-seiten",
        description="Schülerausgaben aus Unterrichts-Markdown erzeugen.",
    )
    sub = parser.add_subparsers(dest="command")
    _add_split(sub)
    _add_strip(sub)
    args = parser.parse_args(argv)

    # Default-Befehl: split
    command = args.command or "split"

    if command == "strip":
        generate_student_site(args.teacher, args.student, _parse_lf(args.lf))
    else:
        run_split(
            project_root=getattr(args, "project_root", None),
            config=getattr(args, "config", None),
            out=getattr(args, "out", None),
            no_resources=getattr(args, "no_resources", False),
        )


if __name__ == "__main__":
    main()
