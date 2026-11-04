#!/usr/bin/env python3
"""vorschau_png – rendert ein SVG (Vorschau eines Diagramms oder Technologieschema) als PNG.

Zur Sichtprüfung (überlagerte Kästen, abgeschnittene Texte, Bauteile am falschen Ort) und für
Word/PowerPoint, wo eine PNG-Datei verlässlicher eingefügt wird als SVG. Nutzt, was vorhanden ist: rsvg-convert,
cairosvg (Python), inkscape oder ImageMagick.

    python3 scripts/vorschau_png.py abbildungen/42_flow_regelkreis.preview.svg [--breite 1200]
    python3 scripts/vorschau_png.py abbildungen/46_biegestation.svg

Schreibt <basis>.png neben das SVG. Exitcode 2, wenn kein Konverter verfügbar ist –
dann das SVG im Browser öffnen und dort prüfen.
"""

from __future__ import annotations

import argparse
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path


def rendere(svg: Path, png: Path, breite: int) -> str | None:
    if shutil.which("rsvg-convert"):
        subprocess.run(["rsvg-convert", "-w", str(breite), str(svg), "-o", str(png)], check=True)
        return "rsvg-convert"
    if importlib.util.find_spec("cairosvg"):
        import cairosvg  # noqa: PLC0415
        cairosvg.svg2png(url=str(svg), write_to=str(png), output_width=breite)
        return "cairosvg"
    if shutil.which("inkscape"):
        subprocess.run(["inkscape", str(svg), "--export-type=png", f"--export-filename={png}",
                        f"--export-width={breite}"], check=True, capture_output=True)
        return "inkscape"
    if shutil.which("convert"):
        subprocess.run(["convert", "-density", "150", str(svg), "-resize", f"{breite}x", str(png)], check=True)
        return "ImageMagick"
    return None


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="SVG (Diagramm-Vorschau, Technologieschema) als PNG rendern.")
    p.add_argument("svg", nargs="+", type=Path)
    p.add_argument("--breite", type=int, default=1200, help="Breite in Pixeln (Standard 1200)")
    a = p.parse_args(argv)
    for svg in a.svg:
        if not svg.is_file():
            print(f"nicht gefunden: {svg}", file=sys.stderr)
            return 1
        basis = svg.name.removesuffix(".svg").removesuffix(".preview").removesuffix(".drawio")
        png = svg.with_name(basis + ".png")
        werkzeug = rendere(svg, png, a.breite)
        if werkzeug is None:
            print("Kein SVG-Konverter gefunden (rsvg-convert, cairosvg, inkscape, ImageMagick). "
                  "Die .drawio.svg im Browser öffnen und dort prüfen.", file=sys.stderr)
            return 2
        print(f"✓ {png} ({werkzeug})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
