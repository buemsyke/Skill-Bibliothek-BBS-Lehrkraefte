#!/usr/bin/env python3
"""CLI für die Edumap-Erzeugung.

    edu-edumap eingabe.{yaml,md,json} [-o ...] [--pretty] [--theme NAME|DATEI]
    edu-edumap --farben-aus MATERIAL [-o farben.yaml]       Theme-Vorschlag ausgeben
    edu-edumap eingabe.md --farben-aus MATERIAL [-o ...]    Farben direkt anwenden
"""

import argparse
import sys
from pathlib import Path

from . import core
from .core import generate, standardfarben_der_quelle
from .farben import farben_aus, theme_vorschlag, theme_yaml


def _theme_arg(wert: str | None):
    """Theme-Name bleibt, eine Datei wird absolut (relativ zum Aufrufordner)."""
    if wert and wert.lower().endswith((".yaml", ".yml")):
        return str(Path(wert).resolve())
    return wert


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="edu-edumap",
        description="Konvertiert YAML/Markdown/JSON in Edumap-JSON",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=core.__doc__,
    )
    parser.add_argument("input", nargs="?", help="Eingabedatei (.yaml, .md oder .json)")
    parser.add_argument(
        "-o", "--output",
        help="Ausgabe-JSON-Datei (Standard: <Datum> Edumaps - <Titel>.json); "
             "mit --farben-aus ohne Eingabe: YAML-Datei für das Theme",
    )
    parser.add_argument(
        "--pretty", action="store_true",
        help="JSON mit Einrueckung ausgeben",
    )
    parser.add_argument(
        "--theme",
        help="Farbgebung von aussen: Theme-Name oder YAML-Datei (geht vor das Theme der Quelle)",
    )
    parser.add_argument(
        "--farben-aus", metavar="MATERIAL",
        help="Farben aus Praesentation, Dokument, Webseite (Datei oder Adresse), CSS, SVG, "
             "Bild oder PDF lesen – ohne Eingabe als Theme-Vorschlag ausgeben, "
             "mit Eingabe direkt anwenden",
    )
    parser.add_argument(
        "--anzahl", type=int, default=6,
        help="hoechstens so viele Pfadfarben im Vorschlag (Standard 6)",
    )
    args = parser.parse_args(argv)

    if args.farben_aus and args.theme:
        parser.error("--theme und --farben-aus nicht zusammen verwenden")
    if not args.input and not args.farben_aus:
        parser.error("Eingabedatei fehlt")

    input_path = Path(args.input) if args.input else None
    if input_path is not None and not input_path.exists():
        print(f"Fehler: Datei nicht gefunden: {input_path}", file=sys.stderr)
        sys.exit(1)

    theme = _theme_arg(args.theme)
    if args.farben_aus:
        try:
            funde = farben_aus(args.farben_aus)
            if input_path is None:
                vorschlag = theme_vorschlag(funde, anzahl=args.anzahl)
            else:
                n = standardfarben_der_quelle(input_path)
                vorschlag = theme_vorschlag(funde, anzahl=max(n, 1), mindestens=n)
        except (OSError, ValueError, RuntimeError) as e:
            print(f"Fehler: {e}", file=sys.stderr)
            sys.exit(1)
        name = args.farben_aus if "://" in args.farben_aus else Path(args.farben_aus).name
        text = theme_yaml(vorschlag, name, mit_schluessel=input_path is None or not args.output)
        if input_path is None:
            if args.output:
                Path(args.output).write_text(theme_yaml(vorschlag, name, mit_schluessel=False),
                                             encoding="utf-8")
                print(f"Theme geschrieben: {args.output}")
            else:
                print(text, end="")
            return
        theme = {k: v for k, v in vorschlag.items() if k != "notizen"}
        print(text, end="")
        if len(vorschlag["pfade"]) < n:
            print(f"Hinweis: {n} Standardfarben in der Quelle, {len(vorschlag['pfade'])} Farben "
                  "im Material – Farben wiederholen sich.", file=sys.stderr)

    output_path = Path(args.output) if args.output else None
    try:
        result = generate(input_path, output_path, pretty=args.pretty, theme=theme)
    except ValueError as e:
        print(f"Fehler: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"Edumap geschrieben: {result}")


if __name__ == "__main__":
    main()
