#!/usr/bin/env python3
"""kennzeichnung_einrichten – legt die Konfiguration für edu-kennzeichnung an.

Zwei Fälle:

* **Kursprojekt** (``<ordner>/scripts/phase_config.yaml`` vorhanden): Fehlt dort der Block
  ``ki_kennzeichnung:``, wird er am Dateiende angehängt (nichts anderes wird verändert).
  Ist er schon da, bleibt die Datei unberührt.
* **Einfacher Ordner** mit Markdown-Dateien: ``<ordner>/ki_kennzeichnung.yaml`` wird
  angelegt. Weil diese Dateien meist gedruckt, nach Word exportiert oder ins LMS kopiert
  werden, bekommen alle gefundenen Dateien das Blockzitat-Format (statt MkDocs-Hinweisbox).

Zusätzlich wird die Transparenzerklärung aus der Vorlage angelegt, falls sie fehlt.

    python3 scripts/kennzeichnung_einrichten.py ORDNER --verantwortlich "MH, BBS Musterstadt"
        [--stand 09.10.2026] [--ki-system "Claude (Anthropic)"] [--muster "*.md"]
        [--stil blockzitat|admonition] [--seite ki-transparenz.md] [--trockenlauf]

Danach: python3 scripts/edu.py kennzeichnung ORDNER [--config ORDNER/ki_kennzeichnung.yaml]
Nur Python-Standardbibliothek. Überschreibt keine vorhandene Datei.
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
VORLAGE = HIER.parent / "assets" / "vorlage-ki-transparenz.md"
IGNORIERT = {"_student_site", "_teacher_site", "site", "generated", ".venv", ".git", "node_modules"}


def _yaml_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _liste(werte: list[str]) -> str:
    return "[" + ", ".join(_yaml_str(w) for w in werte) + "]"


def block(verantwortlich: str, stand: str, ki_system: str, seite: str, quellen: list[str],
          blockzitat: list[str]) -> str:
    return "\n".join([
        "ki_kennzeichnung:",
        f"  verantwortlich: {_yaml_str(verantwortlich)}",
        f"  ki_system: {_yaml_str(ki_system)}",
        f"  stand: {_yaml_str(stand)}",
        f"  seite: {_yaml_str(seite)}",
        f"  quellen: {_liste(quellen)}",
        f"  ausgenommen: {_liste([seite])}",
        f"  blockzitat: {_liste(blockzitat)}",
        "",
    ])


def finde(ordner: Path, muster: str, seite: str) -> list[str]:
    treffer = []
    for p in sorted(ordner.glob(muster)):
        rel = p.relative_to(ordner).as_posix()
        if p.is_file() and rel != seite and not (set(p.relative_to(ordner).parts) & IGNORIERT):
            treffer.append(rel)
    return treffer


def erklaerung(ziel: Path, verantwortlich: str, stand: str, ki_system: str, trocken: bool) -> str:
    if ziel.exists():
        return f"vorhanden: {ziel.name} (unverändert)"
    if not VORLAGE.is_file():
        return f"⚠ Vorlage fehlt ({VORLAGE}) – {ziel.name} von Hand anlegen"
    text = (VORLAGE.read_text(encoding="utf-8")
            .replace("[Verantwortlich]", verantwortlich)
            .replace("[Stand]", stand)
            .replace("[KI-System]", ki_system))
    if not trocken:
        ziel.parent.mkdir(parents=True, exist_ok=True)
        ziel.write_text(text, encoding="utf-8")
    return f"{'(Trockenlauf) würde anlegen' if trocken else 'angelegt'}: {ziel} – Platzhalter […] ergänzen"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Konfiguration für edu-kennzeichnung anlegen.")
    p.add_argument("ordner", type=Path)
    p.add_argument("--verantwortlich", required=True,
                   help="redaktionell verantwortliche Person (Name oder Kürzel, Schule)")
    p.add_argument("--stand", default=dt.date.today().strftime("%d.%m.%Y"))
    p.add_argument("--ki-system", default="Claude (Anthropic)")
    p.add_argument("--muster", default=None, help='Dateimuster, Standard "*.md" bzw. Projektquellen')
    p.add_argument("--stil", choices=("blockzitat", "admonition"), default=None,
                   help="Standard: Ordner blockzitat, Kursprojekt admonition (MkDocs)")
    p.add_argument("--seite", default=None, help="Transparenzerklärung, projektrelativ")
    p.add_argument("--trockenlauf", action="store_true", help="nur anzeigen, nichts schreiben")
    a = p.parse_args(argv)

    ordner = a.ordner.resolve()
    if not ordner.is_dir():
        print(f"Ordner nicht gefunden: {ordner}", file=sys.stderr)
        return 2
    if not a.verantwortlich.strip() or "[" in a.verantwortlich:
        print("--verantwortlich braucht eine echte Angabe (Name oder Kürzel, Schule).", file=sys.stderr)
        return 2

    projekt_cfg = ordner / "scripts" / "phase_config.yaml"
    if projekt_cfg.is_file():
        seite = a.seite or "docs/ki-transparenz.md"
        text = projekt_cfg.read_text(encoding="utf-8")
        if any(z.startswith("ki_kennzeichnung:") for z in text.splitlines()):
            print(f"vorhanden: ki_kennzeichnung-Block in {projekt_cfg} (unverändert)")
        else:
            quellen = [a.muster] if a.muster else ["lessons/*/lesson.md", "solutions/*.md", "docs/*.md",
                                                  "README.md", "CONTRIBUTING.md"]
            neu = block(a.verantwortlich, a.stand, a.ki_system, seite, quellen,
                        ["README.md", "CONTRIBUTING.md"] if a.stil != "blockzitat" else finde(ordner, quellen[0], seite))
            zusatz = ("\n# KI-Transparenzhinweis (Skill ki-kennzeichnung) – eine Quelle für "
                      "edu-kennzeichnung und edu-seiten split\n" + neu)
            if not a.trockenlauf:
                with projekt_cfg.open("a", encoding="utf-8") as f:
                    f.write(("" if text.endswith("\n") else "\n") + zusatz)
            print(f"{'(Trockenlauf) würde ergänzen' if a.trockenlauf else 'ergänzt'}: ki_kennzeichnung-Block in {projekt_cfg}")
            print(neu)
        print(erklaerung(ordner / seite, a.verantwortlich, a.stand, a.ki_system, a.trockenlauf))
        print(f"weiter: python3 {HIER / 'edu.py'} kennzeichnung {ordner}")
        return 0

    seite = a.seite or "ki-transparenz.md"
    muster = a.muster or "*.md"
    dateien = finde(ordner, muster, seite)
    if not dateien:
        print(f"Keine Dateien zu „{muster}“ in {ordner}.", file=sys.stderr)
        return 1
    cfg = ordner / "ki_kennzeichnung.yaml"
    if cfg.exists():
        print(f"vorhanden: {cfg} (unverändert) – Dateiliste ggf. von Hand ergänzen")
    else:
        neu = ("# Konfiguration für edu-kennzeichnung (Skill ki-kennzeichnung)\n"
               + block(a.verantwortlich, a.stand, a.ki_system, seite, [muster],
                       dateien if (a.stil or "blockzitat") == "blockzitat" else []))
        if not a.trockenlauf:
            cfg.write_text(neu, encoding="utf-8")
        print(f"{'(Trockenlauf) würde anlegen' if a.trockenlauf else 'angelegt'}: {cfg} ({len(dateien)} Dateien)")
    print(erklaerung(ordner / seite, a.verantwortlich, a.stand, a.ki_system, a.trockenlauf))
    print(f"weiter: python3 {HIER / 'edu.py'} kennzeichnung {ordner} --config {cfg}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
