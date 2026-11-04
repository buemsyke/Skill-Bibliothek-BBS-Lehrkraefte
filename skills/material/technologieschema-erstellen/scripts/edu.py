#!/usr/bin/env python3
"""edu – startet einen edu-*-Befehl der eduwerkzeuge aus der mitgelieferten Kopie.

Skills, die Werkzeuge aus eduwerkzeuge brauchen, tragen die nötigen Module unter
``scripts/eduwerkzeuge/`` mit (erzeugt von ``werkzeuge/bibliothek.py sync`` aus der
Hauptkopie ``_lib/eduwerkzeuge``). So laufen sie auch dort, wo eduwerkzeuge nicht
installiert ist (Claude im Browser, Rechner von Kolleginnen und Kollegen).

    python3 scripts/edu.py edumap karte.md --pretty      # = edu-edumap karte.md --pretty
    python3 scripts/edu.py quiz quiz.md --to both        # = edu-quiz …
    python3 scripts/edu.py diagramm flow spec.yaml       # = edu-diagramm flow …
    python3 scripts/edu.py --version                     # Stand der mitgelieferten Kopie

Optionen und Ausgaben sind identisch mit den installierten ``edu-*``-Befehlen
(Referenz: KI-REFERENZ.md der eduwerkzeuge). Nur Python-Standardbibliothek; einige
Module brauchen PyYAML (``pip install pyyaml``).
"""

from __future__ import annotations

import importlib
import importlib.util
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent

# Befehlsname (edu-<name>) → Modulname, wo sie abweichen
MODULNAME = {"diagramm": "diagramme"}
BRAUCHT_YAML = {"edumap", "diagramme", "seiten", "kennzeichnung", "technologieschema"}


def verfuegbar() -> list[str]:
    paket = HIER / "eduwerkzeuge"
    module = sorted(p.name for p in paket.iterdir() if (p / "cli.py").is_file()) if paket.is_dir() else []
    umgekehrt = {v: k for k, v in MODULNAME.items()}
    return [umgekehrt.get(m, m) for m in module]


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    befehle = verfuegbar()
    if not args or args[0] in ("-h", "--help"):
        print(__doc__.strip())
        print("\nMitgeliefert in diesem Skill: " + (", ".join(befehle) or "keine Module"))
        return 0 if args else 2
    if args[0] == "--version":
        sys.path.insert(0, str(HIER))
        import eduwerkzeuge  # noqa: PLC0415
        print(f"eduwerkzeuge {eduwerkzeuge.__version__} (mitgeliefert: {', '.join(befehle)})")
        return 0

    befehl, rest = args[0], args[1:]
    modul = MODULNAME.get(befehl, befehl)
    if befehl not in befehle:
        print(f"FEHLER: '{befehl}' ist in diesem Skill nicht mitgeliefert "
              f"(vorhanden: {', '.join(befehle) or 'keine'}). Ist eduwerkzeuge installiert, "
              f"direkt 'edu-{befehl}' aufrufen.", file=sys.stderr)
        return 2
    if modul in BRAUCHT_YAML and importlib.util.find_spec("yaml") is None:
        print("FEHLER: PyYAML fehlt. Einmalig installieren: python3 -m pip install pyyaml",
              file=sys.stderr)
        return 2

    # Die mitgelieferte Kopie hat Vorrang vor einer installierten Fassung:
    # Skill und Werkzeug wurden zusammen geprüft.
    sys.path.insert(0, str(HIER))
    cli = importlib.import_module(f"eduwerkzeuge.{modul}.cli")
    sys.argv = [f"edu-{befehl}", *rest]
    try:
        rc = cli.main(rest)
    except SystemExit as e:
        rc = e.code
    if isinstance(rc, str):
        print(rc, file=sys.stderr)
        return 1
    return rc if isinstance(rc, int) else 0


if __name__ == "__main__":
    sys.exit(main())
