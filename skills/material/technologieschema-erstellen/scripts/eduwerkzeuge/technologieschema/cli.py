#!/usr/bin/env python3
"""CLI für Technologieschemata: ``edu-technologieschema {svg|pruefen|legende|typen} [ARGS...]``.

  svg      Spec prüfen und schreiben: ``<out>.svg`` (Bild, Gruppe je Bauteil) und ``<out>.drawio.svg``
           (bearbeitbar in diagrams.net: Bauteile als Formen, Linien als Verbinder, Texte als Text)
  pruefen  Spec prüfen (Schema, Anker, Bildrand, überlagerte Beschriftungen, Legende)
  legende  Legende als Markdown-Tabelle ausgeben (``--out`` schreibt in eine Datei)
  textform GRAFCET als Tabelle Schritt | Aktion | Transition (Notationsblatt, gleiche Quelle wie das Bild)
  typen    alle Bauteile mit Pflicht- und optionalen Schlüsseln auflisten
  symbole  Schaltzeichen (DIN EN 60617) auflisten; ``--svg DATEI`` schreibt einen Katalogbogen

Exitcode 1 bei Fehlern (❌); Warnungen (⚠) ändern ihn nicht. Alle Pfade relativ zum Arbeitsordner.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from . import drawio
from . import grafcet as gc
from . import pruefen as pr
from . import symbole as sy
from .teile import AUFZAEHLUNGEN, GEMEIN, SCHEMA, SpecFehler


def _ausgeben(befunde) -> bool:
    fehler = False
    for b in befunde:
        print(f"  {b}")
        fehler = fehler or b.stufe == "❌"
    return fehler


def _typen() -> int:
    print("Bauteile (typ) – Pflichtschlüssel mit * markiert, übrige optional.")
    print("Gemeinsam für alle: " + ", ".join(sorted(GEMEIN - {"typ"})) + "\n")
    for typ, (pflicht, optional) in SCHEMA.items():
        schluessel = [f"{k}*" for k in sorted(pflicht)] + sorted(optional)
        print(f"  {typ:11} {', '.join(schluessel)}")
    print("\nErlaubte Werte:")
    for k, werte in AUFZAEHLUNGEN.items():
        print(f"  {k:12} {', '.join(map(str, werte))}")
    print("\nGRAFCET: typ grafcet mit kette aus schritt (art, aktivierung, aktionen, kommentar), transition (art, name, "
          "kommentar), alternativ, parallel, sprung; aktionen: \"-MA1\", \"↑ -QA1 := 1\", \"↓ -QA1 := 0\", "
          "{text, art, bedingung, kommentar}; Aktionsarten " + ", ".join(gc.AKTIONSARTEN) + ".")
    print("\nAnker: \"ID@punkt\" mit punkt = mitte, oben, unten, links, rechts, oben_links, oben_rechts, "
          "unten_links, unten_rechts (Zylinder zusätzlich hinten, spitze); Versatz \"ID@unten:0,12\".")
    return 0


def _symbole_md() -> int:
    """Alle Zeichen als Markdown-Tabellen (für die Referenz des Skills)."""
    kat = None
    for s in sy.SYMBOLE.values():
        if s.kategorie != kat:
            kat = s.kategorie
            print(f"\n### {kat}\n\n| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |\n|---|---|---|---|---|---|---|")
        herkunft = {"liste": "Liste", "zusammengesetzt": "zusammengesetzt"}.get(s.herkunft, "🔎 abgleichen")
        hinweis = (s.hinweis + (f" (Zeichen {s.norm})" if s.norm else "")).replace("|", "\\|")
        wirk = "ja" if s.wirk is not None else ""
        print(f"| `{s.name}` | {s.titel} | {s.klassen} | {', '.join(s.anschluesse)} | {wirk} | {herkunft} | {hinweis} |")
    print("\n### Betätigungsarten\n\nZusatz `betaetigung: <Name>` bei Zeichen mit Wirkverbindung (Spalte *Wirkv.*); "
          "`wirklaenge` (Standard 2) setzt die Länge der gestrichelten Linie.\n\n| Name | Betätigungsart | Quelle | Hinweis |\n|---|---|---|---|")
    for b in sy.BETAETIGUNGEN.values():
        print(f"| `{b.name}` | {b.titel} | {b.quelle} | {b.hinweis} |")
    return 0


def _symbole(svg) -> int:
    if svg:
        svg.parent.mkdir(parents=True, exist_ok=True)
        svg.write_text(sy.katalog_svg(), encoding="utf-8")
        print(f"✓ {svg}")
        return 0
    kat = None
    for s in sy.SYMBOLE.values():
        if s.kategorie != kat:
            kat = s.kategorie
            print(f"\n{kat}")
        marke = {"liste": "", "zusammengesetzt": "  (zusammengesetzt)"}.get(s.herkunft, "  🔎 abgleichen")
        print(f"  {s.name:28} {s.titel:42} Klasse {s.klassen:6} an: {', '.join(s.anschluesse)}{marke}")
    print("\nBetätigungsarten (Zusatz `betaetigung:` bei Kontakten mit Wirkverbindung)")
    for b in sy.BETAETIGUNGEN.values():
        print(f"  {b.name:20} {b.titel}")
    print("\nKlasse = zulässige Kennbuchstaben des Referenzkennzeichens. Anschlüsse: \"ID@an1\". "
          "🔎 = nach Lehrbuch-Formensprache gezeichnet, vor dem Einsatz mit Norm oder Tabellenbuch abgleichen.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="edu-technologieschema", description=__doc__.split("\n\n")[0])
    sub = p.add_subparsers(dest="befehl", required=True)
    s = sub.add_parser("svg", help="Spec prüfen und als SVG schreiben")
    s.add_argument("spec", nargs="+", type=Path)
    s.add_argument("--out", type=Path, help="Ausgabedatei (.svg) – nur mit einer Spec")
    s.add_argument("--ohne-pruefung", action="store_true", help="Warnungen nicht ausgeben")
    s.add_argument("--ohne-drawio", action="store_true", help="keine bearbeitbare .drawio.svg schreiben")
    c = sub.add_parser("pruefen", help="Spec prüfen")
    c.add_argument("spec", nargs="+", type=Path)
    lg = sub.add_parser("legende", help="Legende als Markdown-Tabelle")
    lg.add_argument("spec", type=Path)
    lg.add_argument("--out", type=Path)
    tf = sub.add_parser("textform", help="GRAFCET als Tabelle in Textform")
    tf.add_argument("spec", type=Path)
    tf.add_argument("--out", type=Path)
    sub.add_parser("typen", help="Bauteile und Schlüssel auflisten")
    sm = sub.add_parser("symbole", help="Schaltzeichen auflisten")
    sm.add_argument("--svg", type=Path, help="Katalogbogen als SVG schreiben")
    sm.add_argument("--md", action="store_true", help="Tabellen in Markdown ausgeben")
    a = p.parse_args(argv)

    if a.befehl == "typen":
        return _typen()
    if a.befehl == "symbole":
        return _symbole_md() if a.md else _symbole(a.svg)
    if a.befehl == "svg" and a.out and len(a.spec) > 1:
        print("FEHLER: --out gilt nur für eine Spec.", file=sys.stderr)
        return 2
    rc = 0
    specs = a.spec if isinstance(a.spec, list) else [a.spec]
    for pfad in specs:
        try:
            spec = pr.lade(pfad)
        except (FileNotFoundError, yaml.YAMLError, SpecFehler) as e:
            print(f"✘ {pfad}: {e}", file=sys.stderr)
            rc = 1
            continue
        befunde, szene = pr.pruefe(spec)
        if a.befehl == "textform":
            if szene is None:
                _ausgeben(befunde)
                return 1
            ketten = [e for e in spec["elemente"] if isinstance(e, dict) and e.get("typ") == "grafcet"]
            if not ketten:
                print(f"✘ {pfad}: keine 'typ: grafcet' in der Spec", file=sys.stderr)
                return 1
            tabelle = "\n".join(gc.textform(e) for e in ketten)
            if a.out:
                a.out.parent.mkdir(parents=True, exist_ok=True)
                a.out.write_text(tabelle, encoding="utf-8")
                print(f"✓ {a.out}")
            else:
                print(tabelle, end="")
            continue
        if a.befehl == "legende":
            if szene is None:
                _ausgeben(befunde)
                return 1
            tabelle = pr.legende_markdown(szene)
            if a.out:
                a.out.parent.mkdir(parents=True, exist_ok=True)
                a.out.write_text(tabelle, encoding="utf-8")
                print(f"✓ {a.out}")
            else:
                print(tabelle, end="")
            continue
        fehler = any(b.stufe == "❌" for b in befunde)
        if a.befehl == "pruefen" or not getattr(a, "ohne_pruefung", False):
            print(f"{'✘' if fehler else '✔'} {pfad}: {sum(b.stufe == '❌' for b in befunde)} Fehler, "
                  f"{sum(b.stufe == '⚠' for b in befunde)} Warnungen")
            _ausgeben(befunde)
        if fehler:
            rc = 1
            continue
        if a.befehl == "svg":
            ziel = a.out or (Path(str(spec["out"]) + ".svg") if spec.get("out") else Path(pfad).with_suffix(".svg"))
            ziel.parent.mkdir(parents=True, exist_ok=True)
            ziel.write_text(szene.svg, encoding="utf-8")
            print(f"✓ {ziel}")
            if not a.ohne_drawio:
                bearbeitbar = ziel.with_name(ziel.name.removesuffix(".svg") + ".drawio.svg")
                bearbeitbar.write_text(drawio.drawio_svg(szene, spec), encoding="utf-8")
                print(f"✓ {bearbeitbar}  (bearbeitbar in diagrams.net)")
    return rc


if __name__ == "__main__":
    sys.exit(main())
