#!/usr/bin/env python3
"""CLI: edu-kennzeichnung – KI-Transparenzhinweise setzen, prüfen, entfernen.

    edu-kennzeichnung                 # alle Seiten aktualisieren
    edu-kennzeichnung --pruefen       # nur prüfen (Exit-Code 1 bei Lücken)
    edu-kennzeichnung --entfernen     # Hinweise wieder entfernen
    edu-kennzeichnung PROJEKTORDNER   # anderes Projekt als das aktuelle

Die Angaben (KI-System, Verantwortliche, Stand, Quellen) stehen im Block
``ki_kennzeichnung:`` der ``scripts/phase_config.yaml`` des Projekts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .core import lade_hinweis, setze_hinweise


def _finde_config(projekt: Path, explizit: Path | None) -> Path | None:
    if explizit is not None:
        return Path(explizit)
    kandidat = projekt / "scripts" / "phase_config.yaml"
    return kandidat if kandidat.is_file() else None


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="edu-kennzeichnung",
        description="Setzt den KI-Transparenzhinweis ans Ende jeder Seite.",
    )
    p.add_argument("projekt", nargs="?", type=Path, default=None,
                   help="Projektwurzel (Standard: aktuelles Verzeichnis)")
    p.add_argument("--config", type=Path, default=None,
                   help="phase_config.yaml (Standard: <Projekt>/scripts/phase_config.yaml)")
    p.add_argument("--pruefen", action="store_true",
                   help="Nur prüfen, ob alle Seiten gekennzeichnet sind")
    p.add_argument("--entfernen", action="store_true",
                   help="Kennzeichnung aus allen Seiten entfernen")
    args = p.parse_args(argv)

    projekt = (args.projekt or Path.cwd()).resolve()
    config = _finde_config(projekt, args.config)
    if config is None:
        print(f"Keine phase_config.yaml unter {projekt}/scripts/ gefunden.",
              file=sys.stderr)
        return 1

    hinweis = lade_hinweis(config)
    if hinweis is None:
        print(f"In {config} fehlt der Block 'ki_kennzeichnung:' – "
              "ohne ihn ist die Kennzeichnung abgeschaltet.", file=sys.stderr)
        return 1
    if not hinweis.verantwortlich:
        print("ki_kennzeichnung.verantwortlich ist leer – die Norm verlangt "
              "eine benannte redaktionell verantwortliche Person.", file=sys.stderr)
        return 1

    return setze_hinweise(projekt, hinweis,
                          pruefen=args.pruefen, entfernen=args.entfernen)


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
