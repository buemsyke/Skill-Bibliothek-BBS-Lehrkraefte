"""seiten – Schülerausgaben aus Unterrichts-Markdown.

Beispiele:
    from eduwerkzeuge.seiten import run_split, strip_teacher_sections
    from pathlib import Path
    run_split(scripts_dir=Path("scripts"))                 # Phasen-Aufteilung
    sauber = strip_teacher_sections(markdown_text)          # Lehrerteile entfernen
"""

from .core import (
    LessonSection,
    PhaseSpec,
    SiteConfig,
    apply_ki_hinweise,
    copy_ki_transparenz,
    copy_resources,
    default_config_path,
    extract_frontmatter_field,
    fix_relative_links,
    generate_lesson_index,
    generate_phase_page,
    generate_student_site,
    load_phase_config,
    load_site_config,
    parse_frontmatter,
    run_split,
    split_into_sections,
    strip_teacher_sections,
)

__all__ = [
    "LessonSection",
    "PhaseSpec",
    "SiteConfig",
    "apply_ki_hinweise",
    "copy_ki_transparenz",
    "copy_resources",
    "default_config_path",
    "extract_frontmatter_field",
    "fix_relative_links",
    "generate_lesson_index",
    "generate_phase_page",
    "generate_student_site",
    "load_phase_config",
    "load_site_config",
    "parse_frontmatter",
    "run_split",
    "split_into_sections",
    "strip_teacher_sections",
]
