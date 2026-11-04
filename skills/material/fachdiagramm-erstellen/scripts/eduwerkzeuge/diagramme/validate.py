#!/usr/bin/env python3
"""
validate — Pruefe .drawio und .drawio.svg-Dateien auf:

  1. Wohlgeformtes XML
  2. Vorhandensein der mxfile/mxGraphModel-Struktur
  3. Bei .drawio.svg: gueltiger SVG-Wrapper mit eingebettetem mxfile
  4. Notations-Plausibilitaet (Chen-ER, UML, Struktogramm, Flow), wenn
     entsprechende Marker im Dateinamen vorkommen (..._chen_*, ..._uml_*,
     ..._nsd_*, ..._flow_*).

Aufruf:
  edu-diagramm validate [PFAD ...]

Ohne Argumente werden alle lessons/**/diagrams/*.drawio* gescannt (relativ zu
repo_root, Default: aktuelles Arbeitsverzeichnis).
Beendet mit Exitcode 1, wenn mindestens ein Fehler gefunden wurde.
"""

from __future__ import annotations

import base64
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path


# Basisverzeichnis für die Standard-Suche. Wird in main() gesetzt.
REPO_ROOT = Path.cwd()


def find_targets(args: list[str]) -> list[Path]:
    if args:
        return [Path(a) for a in args]
    return sorted(
        list((REPO_ROOT / "lessons").rglob("diagrams/*.drawio*"))
        + list((REPO_ROOT / "solutions").rglob("*.drawio*"))
        + list((REPO_ROOT / "docs").rglob("diagrams/*.drawio*"))
    )


def load_mxfile_xml(path: Path) -> tuple[ET.Element, str]:
    """Extrahiert das mxfile-Root-Element aus .drawio oder .drawio.svg.
    Gibt (root, raw_xml_string) zurueck."""
    raw = path.read_text(encoding="utf-8")

    if path.name.endswith(".drawio.svg"):
        try:
            svg_root = ET.fromstring(raw)
        except ET.ParseError as e:
            raise ValueError(f"SVG ist kein wohlgeformtes XML: {e}") from e

        local = svg_root.tag.rsplit("}", 1)[-1]
        if local != "svg":
            raise ValueError(f"Wurzel-Element ist <{local}>, erwartet <svg>")

        content = svg_root.attrib.get("content")
        if not content:
            raise ValueError(
                'Im <svg>-Tag fehlt das "content"-Attribut mit dem eingebetteten mxfile.'
            )
        try:
            mx_root = ET.fromstring(content)
        except ET.ParseError as e:
            raise ValueError(f"Eingebettetes mxfile ist kein wohlgeformtes XML: {e}") from e
        return mx_root, content

    try:
        mx_root = ET.fromstring(raw)
    except ET.ParseError as e:
        raise ValueError(f".drawio ist kein wohlgeformtes XML: {e}") from e
    return mx_root, raw


def extract_mxgraphmodel(mx_root: ET.Element) -> ET.Element:
    """Findet das mxGraphModel-Element, auch wenn es base64+deflate-kodiert
    im <diagram>-Tag steckt."""
    if mx_root.tag == "mxGraphModel":
        return mx_root

    if mx_root.tag != "mxfile":
        raise ValueError(f"Wurzel ist <{mx_root.tag}>, erwartet <mxfile> oder <mxGraphModel>.")

    diagram = mx_root.find("diagram")
    if diagram is None:
        raise ValueError("<mxfile> enthaelt kein <diagram>-Element.")

    inner = diagram.find("mxGraphModel")
    if inner is not None:
        return inner

    payload = (diagram.text or "").strip()
    if not payload:
        raise ValueError("<diagram> hat weder <mxGraphModel> noch kodierten Inhalt.")

    try:
        compressed = base64.b64decode(payload)
        decompressed = zlib.decompress(compressed, -zlib.MAX_WBITS)
        url_encoded = decompressed.decode("utf-8")
        xml_str = urllib.parse.unquote(url_encoded)
        return ET.fromstring(xml_str)
    except Exception as e:
        raise ValueError(f"Konnte kodiertes <diagram> nicht dekodieren: {e}") from e


def collect_cells(graph: ET.Element) -> list[ET.Element]:
    root = graph.find("root")
    if root is None:
        raise ValueError("<mxGraphModel> enthaelt kein <root>-Element.")
    return list(root.findall("mxCell")) + list(root.findall("object"))


def style_of(cell: ET.Element) -> str:
    return (cell.attrib.get("style") or "").lower()


def is_vertex(cell: ET.Element) -> bool:
    return cell.attrib.get("vertex") == "1"


def is_edge(cell: ET.Element) -> bool:
    return cell.attrib.get("edge") == "1"


def value_of(cell: ET.Element) -> str:
    v = cell.attrib.get("value", "") or ""
    return re.sub(r"<[^>]+>", "", v).strip()


def validate_chen(cells: list[ET.Element], errors: list[str], overview: bool = False) -> None:
    """Plausibilitaetspruefungen fuer Chen-Notation.

    overview=True: Uebersichtsdiagramme (nur Entitaeten + Beziehungen, ohne
    Attribut-Ellipsen) sind zulaessig.
    """
    rectangles, ellipses, rhombi = [], [], []
    for c in cells:
        if not is_vertex(c):
            continue
        s = style_of(c)
        if "ellipse" in s:
            ellipses.append(c)
        elif "rhombus" in s:
            rhombi.append(c)
        elif "rounded=0" in s or s.startswith("shape=rectangle") or s == "" or "whitespace=wrap" in s:
            rectangles.append(c)
    if not rectangles:
        errors.append("Chen: keine Entitaetstyp-Rechtecke gefunden.")
    if not rhombi:
        errors.append("Chen: keine Beziehungs-Rauten (rhombus) gefunden.")
    if not ellipses and not overview:
        errors.append("Chen: keine Attribut-Ellipsen gefunden (bei Uebersichten Dateinamen-Suffix _uebersicht setzen).")
    for r in rhombi:
        if not value_of(r):
            errors.append("Chen: Beziehungs-Raute ohne Beschriftung.")
    for r in rectangles:
        if not value_of(r):
            errors.append("Chen: Entitaets-Rechteck ohne Beschriftung.")


def validate_uml(cells: list[ET.Element], errors: list[str]) -> None:
    """Plausibilitaetspruefungen fuer UML-Klassendiagramm.

    Einzelklassen-Diagramme (genau eine Klasse) sind zulaessig und brauchen
    keine Beziehungskante.
    """
    classes = [c for c in cells if is_vertex(c) and "swimlane" in style_of(c)]
    edges = [c for c in cells if is_edge(c)]
    if not classes:
        errors.append("UML: keine Klasse (swimlane) gefunden.")
    if len(classes) > 1 and not edges:
        errors.append("UML: mehrere Klassen, aber keine Beziehungs-Kante gefunden.")
    for cls in classes:
        if not value_of(cls):
            errors.append("UML: Klasse ohne Namen.")


def validate_nsd(cells: list[ET.Element], errors: list[str]) -> None:
    """Plausibilitaetspruefungen fuer Struktogramme (Nassi-Shneiderman)."""
    rects = [c for c in cells if is_vertex(c) and "text;" not in style_of(c)]
    texte = [c for c in cells if is_vertex(c) and "text;" in style_of(c)]
    if len(rects) < 1:
        errors.append("Struktogramm: keine Kaesten gefunden.")
    if not any(value_of(t) for t in texte):
        errors.append("Struktogramm: kein beschrifteter Kasten gefunden.")


def validate_flow(cells: list[ET.Element], errors: list[str]) -> None:
    """Plausibilitaetspruefungen fuer Block-/Ablaufdiagramme."""
    knoten = [c for c in cells if is_vertex(c) and "text;" not in style_of(c)]
    kanten = [c for c in cells if is_edge(c)]
    if len(knoten) < 2:
        errors.append(f"Flow: erwartet >=2 Knoten, gefunden {len(knoten)}.")
    if not kanten:
        errors.append("Flow: keine Kante gefunden.")
    for k in knoten:
        if not value_of(k):
            errors.append("Flow: Knoten ohne Beschriftung.")


def detect_notation(path: Path) -> str | None:
    name = path.name.lower()
    if "_chen_" in name or name.startswith("chen_"):
        return "chen"
    if "_uml_" in name or name.startswith("uml_"):
        return "uml"
    if "_nsd_" in name or name.startswith("nsd_"):
        return "nsd"
    if "_flow_" in name or name.startswith("flow_"):
        return "flow"
    return None


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        mx_root, _raw = load_mxfile_xml(path)
        graph = extract_mxgraphmodel(mx_root)
        cells = collect_cells(graph)
    except ValueError as e:
        return [str(e)]

    if not cells:
        errors.append("Keine mxCell-Elemente gefunden.")
        return errors

    notation = detect_notation(path)
    overview = "_uebersicht" in path.name.lower()
    if notation == "chen":
        validate_chen(cells, errors, overview=overview)
    elif notation == "uml":
        validate_uml(cells, errors)
    elif notation == "nsd":
        validate_nsd(cells, errors)
    elif notation == "flow":
        validate_flow(cells, errors)
    return errors


def main(argv: list[str], repo_root: Path | None = None) -> int:
    global REPO_ROOT
    REPO_ROOT = Path(repo_root) if repo_root is not None else Path.cwd()

    targets = find_targets(argv[1:])
    if not targets:
        print("Keine .drawio/.drawio.svg-Dateien gefunden.")
        return 0

    total_errors = 0
    for t in targets:
        rel = t.relative_to(REPO_ROOT) if t.is_absolute() else t
        errs = validate_file(t)
        if errs:
            total_errors += len(errs)
            print(f"FEHLER  {rel}")
            for e in errs:
                print(f"        - {e}")
        else:
            print(f"OK      {rel}")
    print()
    print(f"{len(targets)} Datei(en) geprueft, {total_errors} Fehler.")
    return 1 if total_errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
