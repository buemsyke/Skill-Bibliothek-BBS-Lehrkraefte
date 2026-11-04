#!/usr/bin/env python3
"""CLI für Diagramme: ``edu-diagramm {box|chen|flow|struktogramm|svg|validate} [ARGS...]``.

  box           UML-/Relationenschema-Diagramme aus YAML-Spec
  chen          Chen-ER-Diagramme aus YAML-Spec
  flow          Block-/Ablaufdiagramme aus YAML-Spec
  struktogramm  Nassi-Shneiderman-Diagramme aus YAML-Spec
  svg           Hybrid-.drawio.svg aus .drawio + .preview.svg bauen
  validate      .drawio/.drawio.svg-Dateien prüfen

Alle Pfade sind relativ zum aktuellen Arbeitsverzeichnis.
"""

import sys

import yaml

from . import box, chen, flow, struktogramm, svg, validate

_COMMANDS = {
    "box": box.main,
    "chen": chen.main,
    "flow": flow.main,
    "struktogramm": struktogramm.main,
    "svg": svg.main,
    "validate": validate.main,
}

_HILFE = [
    ("box", "UML-/Relationenschema-Diagramm aus YAML-Spec"),
    ("chen", "Chen-ER-Diagramm aus YAML-Spec"),
    ("flow", "Block-/Ablaufdiagramm aus YAML-Spec"),
    ("struktogramm", "Nassi-Shneiderman-Diagramm aus YAML-Spec"),
    ("svg", "Hybrid-.drawio.svg bauen"),
    ("validate", ".drawio/.drawio.svg prüfen"),
]


def _usage() -> None:
    namen = "|".join(name for name, _ in _HILFE)
    print(f"Verwendung: edu-diagramm {{{namen}}} [ARGS...]", file=sys.stderr)
    for name, beschreibung in _HILFE:
        print(f"  {name:<13} {beschreibung}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("-h", "--help"):
        _usage()
        return 0 if args[:1] in (["-h"], ["--help"]) else 2

    command = args[0]
    runner = _COMMANDS.get(command)
    if runner is None:
        print(f"Unbekannter Befehl: {command}", file=sys.stderr)
        _usage()
        return 2

    # Die Untermodule erwarten argv im sys.argv-Stil (argv[1:] = echte Argumente).
    try:
        return runner([command] + args[1:])
    except FileNotFoundError as e:
        print(f"FEHLER: Datei nicht gefunden: {e.filename or e}", file=sys.stderr)
        return 1
    except yaml.YAMLError as e:
        print(f"FEHLER: Die Spec ist kein gültiges YAML:\n  {e}", file=sys.stderr)
        return 1
    except (ValueError, KeyError) as e:
        msg = e.args[0] if e.args else e
        print(f"FEHLER: {msg}", file=sys.stderr)
        print("Hinweis: Aufbau einer Spec siehe KI-REFERENZ.md (Abschnitt edu-diagramm).", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
