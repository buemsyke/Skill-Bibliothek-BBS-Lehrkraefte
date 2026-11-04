#!/usr/bin/env python3
"""
_common — gemeinsame Bausteine der Diagramm-Generatoren.

Jeder Generator (``box``, ``chen``, ``flow``, ``struktogramm``) erzeugt drei
Dateien zum selben Basisnamen:

  ``<out>.drawio``       reine draw.io-XML (bearbeitbar in app.diagrams.net)
  ``<out>.preview.svg``  gerenderte Vorschau ohne eingebettetes XML
  ``<out>.drawio.svg``   Hybrid: SVG-Darstellung + eingebettetes draw.io-XML

Nur die Hybrid-Datei wird in die Schülerausgabe kopiert (siehe
``seiten.copy_resources``): Sie zeigt sich im Browser als Bild und lässt sich
per Drag & Drop in draw.io weiterbearbeiten.

Dieses Modul enthält bewusst keine Diagrammlogik, sondern nur Text-, Farb- und
Datei-Hilfen, die alle Generatoren teilen.
"""

from __future__ import annotations

import re
import xml.sax.saxutils as su
from pathlib import Path

FONT_FAMILY = "Helvetica, Arial, sans-serif"

#: Farbpaare (Füllung, Rand) — die Standardpalette von draw.io.
PALETTE: dict[str, tuple[str, str]] = {
    "blau": ("#dae8fc", "#6c8ebf"),
    "gruen": ("#d5e8d4", "#82b366"),
    "gelb": ("#fff2cc", "#d6b656"),
    "rot": ("#f8cecc", "#b85450"),
    "lila": ("#e1d5e7", "#9673a6"),
    "orange": ("#ffe6cc", "#d79b00"),
    "grau": ("#f5f5f5", "#666666"),
    "weiss": ("#ffffff", "#333333"),
}

DEFAULT_FARBE = "blau"


def farben(name: str | None) -> tuple[str, str]:
    """Farbname → (Füllfarbe, Randfarbe).

    Unbekannte Namen und ``None`` liefern die Standardfarbe. Direkte Hex-Werte
    (``"#rrggbb"``) werden als Füllfarbe mit dunklem Rand übernommen.
    """
    if not name:
        return PALETTE[DEFAULT_FARBE]
    if name.startswith("#"):
        return (name, "#333333")
    return PALETTE.get(name.lower(), PALETTE[DEFAULT_FARBE])


def slug(s: str) -> str:
    """Beliebigen Text in eine XML-taugliche ID verwandeln."""
    return re.sub(r"[^A-Za-z0-9]+", "_", s).strip("_").lower() or "x"


def xml_escape(s: str) -> str:
    """Text für XML-Attribute und -Inhalte maskieren."""
    return su.escape(str(s), {'"': "&quot;", "'": "&apos;"})


def text_breite(text: str, font_size: float, *, fett: bool = False) -> float:
    """Schätzt die Pixelbreite einer Textzeile.

    Ausreichend genau, um Kästen automatisch zu dimensionieren — die Generatoren
    zeichnen nicht mit echten Font-Metriken.
    """
    faktor = 0.60 if fett else 0.545
    return len(text) * font_size * faktor


def zeilen(wert: str | list[str] | None) -> list[str]:
    """Normalisiert ``None`` / String (mit ``\\n``) / Liste zu einer Zeilenliste."""
    if wert is None:
        return []
    if isinstance(wert, str):
        return [z for z in wert.split("\n")]
    return [str(z) for z in wert]


def br_join(lines: list[str]) -> str:
    """Zeilenliste → draw.io-Label (HTML mit ``<br/>``), bereits maskiert."""
    return "&lt;br/&gt;".join(xml_escape(z) for z in lines)


def mk_mxfile(cells: list[str], page_w: int, page_h: int, title: str, diagram_id: str) -> str:
    """Baut aus fertigen ``<mxCell>``-Strings eine vollständige .drawio-Datei."""
    inner = "\n        ".join(['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>'] + cells)
    return (
        '<mxfile host="app.diagrams.net" type="device">\n'
        f'  <diagram id="{xml_escape(diagram_id)}" name="{xml_escape(title)}">\n'
        f'    <mxGraphModel dx="{page_w}" dy="{page_h}" grid="1" gridSize="10" guides="1" '
        f'tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
        f'pageWidth="{page_w}" pageHeight="{page_h}" math="0" shadow="0">\n'
        f"      <root>\n        {inner}\n      </root>\n"
        "    </mxGraphModel>\n  </diagram>\n</mxfile>\n"
    )


def mk_svg(parts: list[str], page_w: int, page_h: int, title: str, style: str) -> str:
    """Baut aus SVG-Fragmenten eine vollständige preview.svg."""
    kopf = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {page_w} {page_h}" '
        f'font-family="{FONT_FAMILY}">',
        f"  <title>{xml_escape(title)}</title>",
        f"  <style>{style}</style>",
        f'  <rect x="0" y="0" width="{page_w}" height="{page_h}" fill="#ffffff"/>',
    ]
    return "\n".join(kopf + parts + ["</svg>"]) + "\n"


def mk_hybrid(drawio_xml: str, preview_svg: str) -> str:
    """Verschmilzt .drawio und preview.svg zur bearbeitbaren ``.drawio.svg``."""
    m = re.search(r"<svg[^>]*>(.*)</svg>", preview_svg, flags=re.DOTALL)
    if m is None:
        raise ValueError("preview.svg enthält kein <svg>-Element.")
    inner = m.group(1)
    viewbox_m = re.search(r'viewBox="([^"]+)"', preview_svg)
    viewbox = viewbox_m.group(1) if viewbox_m else "0 0 1000 600"
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<svg xmlns="http://www.w3.org/2000/svg" '
        f'viewBox="{viewbox}" '
        f'font-family="{FONT_FAMILY}" '
        f"content={su.quoteattr(drawio_xml)}>" + inner + "</svg>\n"
    )


def schreibe_ausgaben(repo_root: Path, out: str, drawio_xml: str, preview_svg: str) -> Path:
    """Schreibt .drawio, .preview.svg und .drawio.svg; gibt den Hybrid-Pfad zurück."""
    out_drawio = repo_root / f"{out}.drawio"
    out_preview = repo_root / f"{out}.preview.svg"
    out_hybrid = repo_root / f"{out}.drawio.svg"
    out_drawio.parent.mkdir(parents=True, exist_ok=True)
    out_drawio.write_text(drawio_xml, encoding="utf-8")
    out_preview.write_text(preview_svg, encoding="utf-8")
    out_hybrid.write_text(mk_hybrid(drawio_xml, preview_svg), encoding="utf-8")
    return out_hybrid
