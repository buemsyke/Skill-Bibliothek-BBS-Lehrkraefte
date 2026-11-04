#!/usr/bin/env python3
"""CLI für die H5P-Erzeugung: ``edu-h5p [PROJEKTVERZEICHNIS]``.

Erwartet im Projektverzeichnis einen Ordner ``h5p/`` mit ``*.md``-Dateien
und schreibt die erzeugten ``.h5p``-Dateien nach ``h5p/generated/``.
"""

import argparse
from pathlib import Path

from .core import main as _run


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="edu-h5p",
        description="Erzeugt H5P-Quizze (.h5p) aus Markdown in <Projekt>/h5p/.",
    )
    parser.add_argument(
        "projekt",
        nargs="?",
        default=None,
        help="Projektverzeichnis mit Unterordner h5p/ (Default: aktuelles Verzeichnis).",
    )
    args = parser.parse_args(argv)
    project_dir = Path(args.projekt) if args.projekt else None
    _run(project_dir)


if __name__ == "__main__":
    main()
