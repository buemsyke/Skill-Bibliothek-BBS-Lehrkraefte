"""edumap – YAML/Markdown/JSON → Edumap-JSON.

Beispiel:
    from eduwerkzeuge.edumap import generate, parse_markdown, build_edumap
    from pathlib import Path
    generate(Path("lernlandkarte.md"))            # JSON neben der Eingabe
    daten = parse_markdown(Path("x.md").read_text())
"""

from .core import (
    DEFAULTS,
    MAPFORMATS,
    PALETTE,
    THEMES,
    build_box,
    build_edumap,
    build_mapdata,
    build_path,
    generate,
    parse_file,
    parse_markdown,
    parse_yaml,
    resolve_color,
)
from .farben import farben_aus, kontrast, lesbar, theme_vorschlag, theme_yaml

__all__ = [
    "DEFAULTS",
    "MAPFORMATS",
    "PALETTE",
    "THEMES",
    "build_box",
    "build_edumap",
    "build_mapdata",
    "build_path",
    "generate",
    "parse_file",
    "parse_markdown",
    "parse_yaml",
    "resolve_color",
    "farben_aus",
    "kontrast",
    "lesbar",
    "theme_vorschlag",
    "theme_yaml",
]
