#!/usr/bin/env python3
"""
svg — Baut eine Hybrid-.drawio.svg-Datei aus zwei Quellen:

  1. <name>.drawio          — die mxGraphModel-Quelle (XML)
  2. <name>.preview.svg     — das fertige Anzeige-SVG mit allen Shapes

Ergebnis: <name>.drawio.svg mit dem .drawio-Inhalt als XML-escaped
content="…"-Attribut im <svg>-Wurzelelement.

Aufruf:
  edu-diagramm svg <basisname-ohne-erweiterung>
  edu-diagramm svg --all  # baut alle Paare in lessons/**/diagrams/

Die Quelldateien bleiben liegen (sie sind "Build-Inputs"). Pfade sind relativ
zu repo_root (Default: aktuelles Arbeitsverzeichnis).
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.sax.saxutils as su
from pathlib import Path


# Basisverzeichnis für relative Pfade. Wird in main() gesetzt.
REPO_ROOT = Path.cwd()


def build_one(drawio_path: Path, preview_path: Path, out_path: Path) -> None:
    drawio_src = drawio_path.read_text(encoding="utf-8")
    svg_src = preview_path.read_text(encoding="utf-8")

    m = re.search(r"<svg[^>]*>(.*)</svg>", svg_src, flags=re.DOTALL)
    if not m:
        raise SystemExit(f"In {preview_path} kein <svg>-Element gefunden.")
    inner = m.group(1)

    viewbox_m = re.search(r'viewBox="([^"]+)"', svg_src)
    viewbox = viewbox_m.group(1) if viewbox_m else "0 0 1000 600"

    content_attr = su.quoteattr(drawio_src)

    hybrid = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{viewbox}" '
        'font-family="Helvetica, Arial, sans-serif" '
        f'content={content_attr}>'
        + inner
        + "</svg>\n"
    )
    out_path.write_text(hybrid, encoding="utf-8")


def main(argv: list[str], repo_root: Path | None = None) -> int:
    global REPO_ROOT
    REPO_ROOT = Path(repo_root) if repo_root is not None else Path.cwd()

    parser = argparse.ArgumentParser(prog="edu-diagramm svg", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("base", nargs="?", help="Basispfad ohne Erweiterung")
    parser.add_argument("--all", action="store_true", help="Alle Paare unter lessons/**/diagrams/")
    args = parser.parse_args(argv[1:])

    pairs: list[tuple[Path, Path, Path]] = []

    if args.all:
        for drawio in sorted((REPO_ROOT / "lessons").rglob("diagrams/*.drawio")):
            preview = drawio.with_name(drawio.stem + ".preview.svg")
            out = drawio.with_name(drawio.stem + ".drawio.svg")
            if preview.exists():
                pairs.append((drawio, preview, out))
            else:
                print(f"SKIP    {drawio.relative_to(REPO_ROOT)} (preview fehlt)")
    elif args.base:
        base = Path(args.base)
        if not base.is_absolute():
            base = REPO_ROOT / base
        pairs.append((
            base.with_suffix(".drawio"),
            base.with_name(base.name + ".preview.svg"),
            base.with_name(base.name + ".drawio.svg"),
        ))
    else:
        parser.print_help()
        return 2

    for drawio, preview, out in pairs:
        if not drawio.exists() or not preview.exists():
            print(f"FEHLER  Quelle fehlt: {drawio} oder {preview}")
            continue
        build_one(drawio, preview, out)
        print(f"OK      {out.relative_to(REPO_ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
