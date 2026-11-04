"""h5p – Markdown-Quiz-Definitionen → H5P-Dateien (.h5p).

Beispiel:
    from eduwerkzeuge.h5p import write_h5p_file, parse_exercise, split_exercises
    from eduwerkzeuge.h5p import main
    from pathlib import Path
    main(Path("/pfad/zum/projekt"))   # erzeugt <projekt>/h5p/generated/*.h5p
"""

from .core import (
    PARSERS,
    blanks_body_to_html,
    build_blanks,
    build_dragtext,
    build_essay,
    build_multichoice,
    build_sortparagraphs,
    build_truefalse,
    create_content_json,
    create_h5p_json,
    extract_blanks_body,
    main,
    parse_exercise,
    parse_exercise_header,
    process_file,
    protect_blank_markers,
    split_exercises,
    warn_reserved_blank_chars,
    write_h5p_file,
)

__all__ = [
    "PARSERS",
    "blanks_body_to_html",
    "build_blanks",
    "build_dragtext",
    "build_essay",
    "build_multichoice",
    "build_sortparagraphs",
    "build_truefalse",
    "create_content_json",
    "create_h5p_json",
    "extract_blanks_body",
    "main",
    "parse_exercise",
    "parse_exercise_header",
    "process_file",
    "protect_blank_markers",
    "split_exercises",
    "warn_reserved_blank_chars",
    "write_h5p_file",
]
