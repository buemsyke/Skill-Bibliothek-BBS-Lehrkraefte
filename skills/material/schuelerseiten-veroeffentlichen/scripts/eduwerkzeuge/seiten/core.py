#!/usr/bin/env python3
"""
seiten – Schülerausgaben aus Unterrichts-Markdown erzeugen.

Zwei Workflows:

1. ``run_split(...)``  (aus split_lessons.py)
   Zerlegt monolithische ``lessons/XX_*/lesson.md`` anhand der H1-Überschriften
   in 5 LMS-Phasen, schreibt pro Phase eine Markdown-Datei nach
   ``_student_site/docs/`` und erzeugt eine mkdocs.yml + Startseite.

2. ``generate_student_site(...)`` / ``strip_teacher_sections(...)``
   (aus generate_student_site.py)
   Entfernt lehrkraft-eigene Abschnitte (Didaktische Hinweise, Lösungen,
   Bewertungskriterien, Erwartungshorizont) aus Lektionsdateien.

Pfade sind Parameter (Default: aktuelles Arbeitsverzeichnis bzw. mitgelieferte
phase_config.yaml). Ein Shim im Projekt übergibt sein ``scripts/``-Verzeichnis
und reproduziert damit exakt das frühere skript-relative Verhalten.
"""

from __future__ import annotations

import os
import re
import shutil
import sys
from importlib import resources
from pathlib import Path
from typing import NamedTuple

from ..kennzeichnung import KiHinweis, entferne_block, lade_hinweis, setze_block

# ---------------------------------------------------------------------------
# Optional: PyYAML – Fallback auf einfachen Parser falls nicht installiert
# ---------------------------------------------------------------------------
try:
    import yaml
except ImportError:
    yaml = None  # type: ignore


# ========================== Datenstrukturen ================================

class PhaseSpec(NamedTuple):
    phase_id: int
    slug: str
    title: str
    icon: str
    description: str
    sections: list[str]


class LessonSection(NamedTuple):
    heading: str       # H1-Überschriftstext (ohne "# ")
    body: str          # Gesamter Inhalt inkl. Überschrift


class SiteConfig(NamedTuple):
    """Projektspezifische Beschriftung und Umfang der Schülerausgabe.

    Wird aus dem optionalen ``site:``-Block der phase_config.yaml gelesen.
    Fehlt der Block, gelten die Alt-Defaults aus BINFQ2 — so erzeugen
    Projekte ohne ``site:``-Block byteweise dieselbe Ausgabe wie bisher.
    """
    name: str = "BINFQ2 Datenbanken — Schülerausgabe"
    description: str = "Unterrichtsmaterialien für Lernende – Relationale Datenbanken"
    index_title: str = "BINFQ2 Datenbanken — Schülerausgabe"
    index_heading: str = "Relationale Datenbanken — Schülerausgabe"
    # Welche Projektordner in die Schülerausgabe kopiert werden.
    copy_dirs: tuple[str, ...] = ("h5p", "solutions", "examples")
    # Ob Musterlösungen aus solutions/ verlinkt werden (Navigation, Startseite,
    # Lektionsübersicht). Ohne kopierten solutions/-Ordner wirkungslos.
    link_solutions: bool = True
    # Musterlösungs-Link auf der Lektionsübersicht nur bis zu dieser Lektion.
    solution_link_max_lesson: int = 9
    # KI-Transparenzhinweis aus dem Block ``ki_kennzeichnung:`` derselben
    # phase_config.yaml. None = abgeschaltet (Default; Projekte ohne den Block
    # erzeugen unverändert dieselbe Ausgabe wie bisher).
    ki_hinweis: KiHinweis | None = None


# ========================== Konfiguration ==================================

def default_config_path() -> Path:
    """Pfad zur mitgelieferten Standard-phase_config.yaml im Paket."""
    return Path(str(resources.files("eduwerkzeuge.seiten") / "phase_config.yaml"))


def _load_yaml(path: Path) -> dict:
    """Lade YAML-Datei (nutzt PyYAML oder simplen Fallback)."""
    text = path.read_text(encoding="utf-8")
    if yaml is not None:
        return yaml.safe_load(text)
    # Minimaler Fallback: Nur für die bekannte Struktur
    raise SystemExit(
        "PyYAML ist nicht installiert. Bitte installieren:\n"
        "  pip install pyyaml"
    )


def load_phase_config(config_path: Path) -> tuple[list[PhaseSpec], list[str], list[str]]:
    """Gibt (phases, excluded_sections, excluded_lessons) zurück."""
    data = _load_yaml(config_path)
    phases = [
        PhaseSpec(
            phase_id=p["phase_id"],
            slug=p["slug"],
            title=p["title"],
            icon=p.get("icon", ""),
            description=p.get("description", ""),
            sections=p["sections"],
        )
        for p in data["phases"]
    ]
    excluded = data.get("excluded_sections", [])
    excluded_lessons = data.get("excluded_lessons", [])
    return phases, excluded, excluded_lessons


def load_site_config(config_path: Path) -> SiteConfig:
    """Liest den optionalen ``site:``-Block der phase_config.yaml.

    Ohne ``site:``-Block gilt der Alt-Default (BINFQ2). Setzt ein Projekt nur
    ``name``, erben Seitentitel und Startseiten-Überschrift diesen Namen.

    Der KI-Transparenzhinweis wird aus dem separaten Block
    ``ki_kennzeichnung:`` derselben Datei gelesen – dieselbe Quelle, aus der
    sich auch ``edu-kennzeichnung`` bedient.
    """
    data = _load_yaml(config_path) or {}
    ki_hinweis = lade_hinweis(Path(config_path))
    block = data.get("site") or {}
    if not block:
        return SiteConfig(ki_hinweis=ki_hinweis)

    default = SiteConfig()
    name = block.get("name", default.name)
    copy_dirs = block.get("copy_dirs", list(default.copy_dirs))
    return SiteConfig(
        name=name,
        description=block.get("description", default.description),
        index_title=block.get("index_title", name),
        index_heading=block.get("index_heading", name),
        copy_dirs=tuple(copy_dirs),
        link_solutions=bool(block.get("link_solutions", default.link_solutions)),
        solution_link_max_lesson=int(
            block.get("solution_link_max_lesson", default.solution_link_max_lesson)
        ),
        ki_hinweis=ki_hinweis,
    )


# ========================== Lesson-Parsing =================================

_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)
_H1_SPLIT_RE = re.compile(r"(?=^# )", re.MULTILINE)
# Beginn/Ende eines eingezäunten Code-Blocks (``` oder ~~~, ggf. mit Sprache)
_FENCE_RE = re.compile(r"(```|~~~)")


def parse_frontmatter(text: str) -> tuple[str, str]:
    """Gibt (frontmatter_yaml_string, rest_of_document) zurück."""
    m = _FRONTMATTER_RE.match(text)
    if m:
        return m.group(1), text[m.end():]
    return "", text


def extract_frontmatter_field(fm_text: str, field: str) -> str:
    """Einfache Extraktion eines skalaren YAML-Feldes."""
    for line in fm_text.splitlines():
        if line.startswith(f"{field}:"):
            val = line.split(":", 1)[1].strip().strip('"').strip("'")
            return val
    return ""


def split_into_sections(body: str) -> list[LessonSection]:
    """Zerlegt das Dokument in Abschnitte anhand von H1-Überschriften.

    Code-Blöcke werden übersprungen: Eine Zeile wie ``# phpDocumentor`` in
    einem ```bash-Block ist ein Shell-Kommentar, keine Überschrift. Würde sie
    als H1 gewertet, zerrisse der Code-Block und der Rest des Abschnitts ginge
    beim Zuordnen zu den Phasen verloren.
    """
    parts: list[str] = []
    current: list[str] = []
    fence: str | None = None

    for line in body.splitlines(keepends=True):
        stripped = line.lstrip()
        if fence is None:
            m = _FENCE_RE.match(stripped)
            if m:
                fence = m.group(1)[:3]
            elif line.startswith("# ") and current:
                parts.append("".join(current))
                current = []
        elif stripped.startswith(fence):
            fence = None
        current.append(line)

    if current:
        parts.append("".join(current))

    sections: list[LessonSection] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Erste Zeile ist die H1-Überschrift
        first_line = part.split("\n", 1)[0]
        heading = first_line.lstrip("# ").strip()
        sections.append(LessonSection(heading=heading, body=part))
    return sections


def fix_relative_links(content: str, source_depth: int, target_depth: int) -> str:
    """Passt relative Markdown-Links an die neue Verzeichnistiefe an.

    In den Quelldateien zeigen Links wie ../../h5p/ oder ../../solutions/ auf
    Dateien relativ zur lesson.md. In der Schülerausgabe liegt die Datei ggf.
    in einer anderen Tiefe – die Prefixe müssen angepasst werden.
    """
    def replace_link(m: re.Match) -> str:
        prefix = m.group(1)  # ( oder ]( etc.
        ups = m.group(2)     # ../../ (beliebig viele)
        rest = m.group(3)    # h5p/... oder solutions/...
        return f"{prefix}../{rest}"

    # Markdown-Links:  [text](../../h5p/...)  oder  [text](../../solutions/...)
    content = re.sub(
        r'(\[.*?\]\()(\.\./)+([^)]+\))',
        replace_link,
        content,
    )
    # Auch reine Markdown-Referenzen im Fließtext: `../../h5p/...`
    content = re.sub(
        r'(`)(\.\./)+((?:h5p|solutions|examples)/[^`]+`)',
        lambda m: f"{m.group(1)}../{m.group(3)}",
        content,
    )
    return content


# ========================== Generierung ====================================

def generate_phase_page(
    lesson_title: str,
    lesson_id: str,
    phase: PhaseSpec,
    sections: list[LessonSection],
    total_phases: int,
) -> str:
    """Erzeugt den Markdown-Inhalt einer Phasen-Seite."""
    lines: list[str] = []

    # Frontmatter
    lines.append("---")
    lines.append(f'title: "{phase.title}"')
    lines.append(f'description: "Lektion {lesson_id} – {phase.description}"')
    lines.append("---")
    lines.append("")

    # Breadcrumb-Navigation
    lines.append(f"> **Lektion {lesson_id}** | "
                 f"Phase {phase.phase_id} von {total_phases}: "
                 f"*{phase.title}*")
    lines.append("")

    # Abschnitte einfügen
    for section in sections:
        lines.append(section.body)
        lines.append("")

    return "\n".join(lines)


def generate_lesson_index(
    lesson_title: str,
    lesson_id: str,
    fm_text: str,
    phases: list[PhaseSpec],
    lesson_slug: str,
    solution_filename: str | None = None,
    solution_link_max_lesson: int = 9,
) -> str:
    """Erzeugt eine Übersichtsseite (index.md) für eine Lektion.

    Hinweis: Der Musterlösungs-Link erscheint nur bis einschließlich Lektion
    ``solution_link_max_lesson``; darüber wird er später im LMS freigeschaltet.
    Steuerbar über ``site.solution_link_max_lesson`` in der phase_config.yaml.
    """
    lines: list[str] = []
    lines.append("---")
    lines.append(f'title: "Lektion {lesson_id} – {lesson_title}"')
    lines.append("---")
    lines.append("")
    lines.append("[← Zur Startseite](../index.md)")
    lines.append("")
    lines.append(f"# Lektion {lesson_id} – {lesson_title}")
    lines.append("")

    # Lernziele aus Frontmatter extrahieren
    if yaml is not None:
        fm_data = yaml.safe_load(fm_text) or {}
        goals = fm_data.get("learning_goals", [])
        duration = fm_data.get("duration", "")
        if duration:
            lines.append(f"**Dauer:** {duration}")
            lines.append("")
        if goals:
            lines.append("**Lernziele:**")
            lines.append("")
            for g in goals:
                lines.append(f"- {g}")
            lines.append("")

    lines.append("## Inhalte")
    lines.append("")
    lines.append("Die Lehrkraft schaltet die folgenden Abschnitte "
                 "schrittweise im Lernmanagementsystem frei:")
    lines.append("")
    for phase in phases:
        filename = f"{phase.phase_id:02d}_{phase.slug}.md"
        lines.append(f"| {phase.phase_id} | [{phase.title}]({filename}) "
                     f"| {phase.description} |")
    lines.insert(-len(phases), "| Phase | Abschnitt | Beschreibung |")
    lines.insert(-len(phases), "|---|---|---|")
    lines.append("")

    # Musterlösung nur bis zur konfigurierten Lektionsnummer anzeigen;
    # darüber werden die Links später im LMS freigeschaltet.
    try:
        lesson_num = int(lesson_id)
    except ValueError:
        lesson_num = 0
    if solution_filename and lesson_num <= solution_link_max_lesson:
        lines.append("## Ausführliche Musterlösung")
        lines.append("")
        lines.append(
            f"- [Vollständige Musterlösung zu Lektion {lesson_id}]"
            f"(../solutions/{solution_filename})"
        )
        lines.append("")

    return "\n".join(lines)


# ========================== Datei-Operationen ==============================

def discover_lessons(lessons_dir: Path) -> list[Path]:
    """Findet alle lesson.md-Dateien, sortiert nach Ordnername."""
    found = sorted(lessons_dir.glob("*/lesson.md"))
    return found


def copy_resources(
    project_root: Path,
    out_docs: Path,
    dirs: tuple[str, ...] = ("h5p", "solutions", "examples"),
) -> None:
    """Kopiert die angegebenen Projektordner in die Schüler-Site.

    ``dirs`` kommt aus ``site.copy_dirs`` der phase_config.yaml. Wer
    ``solutions`` weglässt, veröffentlicht keine Musterlösungen.
    """
    for dirname in dirs:
        src = project_root / dirname
        dst = out_docs / dirname
        if src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
            print(f"  ✓ {dirname}/ kopiert ({sum(1 for _ in dst.rglob('*') if _.is_file())} Dateien)")

    # Pro Lektion vorhandene diagrams/-Ordner mitkopieren.
    # Nur die fertigen Hybrid-Dateien (.drawio.svg), nicht die Build-Inputs
    # (.drawio, .preview.svg).
    def _is_publishable(name: str) -> bool:
        return name.endswith(".drawio.svg")

    lessons_dir = project_root / "lessons"
    for diagrams_src in sorted(lessons_dir.glob("*/diagrams")):
        if not diagrams_src.is_dir():
            continue
        lesson_folder = diagrams_src.parent.name
        diagrams_dst = out_docs / lesson_folder / "diagrams"
        diagrams_dst.parent.mkdir(parents=True, exist_ok=True)
        if diagrams_dst.exists():
            shutil.rmtree(diagrams_dst)
        diagrams_dst.mkdir(parents=True, exist_ok=True)
        n = 0
        for f in diagrams_src.iterdir():
            if f.is_file() and _is_publishable(f.name):
                shutil.copy2(f, diagrams_dst / f.name)
                n += 1
        print(f"  ✓ {lesson_folder}/diagrams/ kopiert ({n} Dateien)")


def copy_ki_transparenz(project_root: Path, out_docs: Path,
                        hinweis: KiHinweis) -> bool:
    """Kopiert die ausführliche KI-Transparenzerklärung in die Schüler-Site.

    Sie liegt im Projekt unter ``hinweis.seite`` (z. B. ``docs/ki-transparenz.md``)
    und landet flach neben der Startseite, weil sie von jeder Seite aus verlinkt
    wird. Ein etwaiger Kennzeichnungsblock der Quelldatei wird entfernt – die
    Seite trägt ihren Hinweis selbst im Fließtext.

    @return  True, wenn die Seite kopiert wurde
    """
    quelle = project_root / hinweis.seite
    if not quelle.is_file():
        print(f"  ⚠  {hinweis.seite} nicht gefunden – "
              "die Hinweise verlinken ins Leere.")
        return False
    ziel = out_docs / Path(hinweis.seite).name
    ziel.write_text(
        entferne_block(quelle.read_text(encoding="utf-8")), encoding="utf-8"
    )
    print(f"  ✓ {hinweis.seite} kopiert")
    return True


def apply_ki_hinweise(out_docs: Path, hinweis: KiHinweis) -> int:
    """Setzt den KI-Transparenzhinweis unter jede Seite der Schülerausgabe.

    Läuft als letzter Schritt über **alle** Markdown-Dateien der Ausgabe – die
    generierten Phasen- und Übersichtsseiten ebenso wie die aus ``copy_dirs``
    übernommenen (h5p/, examples/ …). Dadurch stimmt der relative Link zur
    Transparenzerklärung überall, unabhängig von der Verzeichnistiefe.

    Die Erklärung selbst bleibt ausgenommen: Sie soll nicht auf sich selbst
    verweisen.

    @return  Anzahl der gekennzeichneten Seiten
    """
    ziel = out_docs / Path(hinweis.seite).name
    anzahl = 0
    for pfad in sorted(out_docs.rglob("*.md")):
        if pfad == ziel:
            continue
        text = pfad.read_text(encoding="utf-8")
        link = os.path.relpath(ziel, pfad.parent).replace(os.sep, "/")
        pfad.write_text(setze_block(text, link, hinweis), encoding="utf-8")
        anzahl += 1
    return anzahl


def generate_student_mkdocs(
    out_root: Path,
    nav_entries: list[dict],
    site: SiteConfig | None = None,
) -> None:
    """Erzeugt die mkdocs.yml für die Schüler-Site.

    Keine Tab-Navigation im Seitenkopf (navigation.tabs entfernt).
    Alle Lektionen erscheinen im Sidebar-Baum, erreichbar über das
    Hamburger-Menü. Titel und Beschreibung kommen aus ``site``.
    """
    site = site or SiteConfig()
    lines: list[str] = []
    lines.append(f'site_name: "{site.name}"')
    lines.append(f'site_description: "{site.description}"')
    lines.append("theme:")
    lines.append("  name: material")
    lines.append("  palette:")
    lines.append("    - scheme: default")
    lines.append("      primary: indigo")
    lines.append("      accent: amber")
    lines.append("      toggle:")
    lines.append("        icon: material/brightness-7")
    lines.append('        name: "Dunkles Design"')
    lines.append("    - scheme: slate")
    lines.append("      primary: indigo")
    lines.append("      accent: amber")
    lines.append("      toggle:")
    lines.append("        icon: material/brightness-4")
    lines.append('        name: "Helles Design"')
    lines.append("  features:")
    lines.append("    - toc.integrate")
    lines.append("    - navigation.top")
    lines.append("    - navigation.sections")
    lines.append(f"docs_dir: docs")
    lines.append("use_directory_urls: false")
    lines.append("")
    lines.append("nav:")
    lines.append("  - Start: index.md")
    for entry in nav_entries:
        slug = entry["slug"]
        label = entry["label"]
        lines.append(f"  - '{label}':")
        lines.append(f"    - Übersicht: {slug}/index.md")
        for phase in entry["phases"]:
            p_label = phase["title"]
            p_file = phase["file"]
            lines.append(f"    - '{p_label}': {slug}/{p_file}")
        sol_file = entry.get("solution_file")
        if sol_file and site.link_solutions:
            lines.append(f"    - Musterlösung: solutions/{sol_file}")
    # Die ausführliche Transparenzerklärung schließt die Navigation ab; jede
    # Seite verlinkt sie ohnehin in ihrem Fußhinweis.
    if site.ki_hinweis is not None:
        seite = Path(site.ki_hinweis.seite).name
        lines.append(f"  - {site.ki_hinweis.nav_titel}: {seite}")
    lines.append("")
    lines.append("extra_css:")
    lines.append("  - stylesheets/extra.css")
    lines.append("")
    lines.append("markdown_extensions:")
    lines.append("  - admonition")
    lines.append("  - toc:")
    lines.append("      permalink: true")
    lines.append("  - tables")
    # Ohne sane_lists ignoriert Python-Markdown die Startnummer einer Liste
    # (Aufgabe 3 nach einem Zwischenkasten erscheint als "1.") und verschmilzt
    # eine Aufzählung mit der direkt folgenden nummerierten Liste.
    lines.append("  - sane_lists")
    # Beide Erweiterungen werden von den Unterrichtsmaterialien bereits genutzt
    # (`=== "Tab"` für differenzierte Zugänge, `??? note` für aufklappbare
    # Hilfestellungen). Ohne sie rendert diese Syntax in der Schülerausgabe als
    # roher Text – die Lehrerausgabe hat sie seit jeher aktiv.
    lines.append("  - pymdownx.tabbed:")
    lines.append("      alternate_style: true")
    lines.append("  - pymdownx.details")
    lines.append("  - pymdownx.superfences:")
    lines.append("      custom_fences:")
    lines.append("        - name: mermaid")
    lines.append("          class: mermaid")
    lines.append("          format: !!python/name:pymdownx.superfences.fence_code_format")
    lines.append("  - pymdownx.arithmatex:")
    lines.append("      generic: true")
    lines.append("")
    lines.append("extra_javascript:")
    lines.append("  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js")
    lines.append("")

    (out_root / "mkdocs.yml").write_text("\n".join(lines), encoding="utf-8")


def generate_student_index(
    out_docs: Path,
    nav_entries: list[dict],
    site: SiteConfig | None = None,
) -> None:
    """Erzeugt die Startseite der Schüler-Site.

    Da die mkdocs-Navigation auf einen einzigen Eintrag (Start) reduziert ist,
    übernimmt die Startseite die komplette Navigation: pro Lektion eine
    Auflistung aller Phasen-Seiten sowie – falls aktiviert – ein Direktlink
    zur Musterlösung.
    """
    site = site or SiteConfig()
    lines: list[str] = []
    lines.append("---")
    lines.append(f'title: "{site.index_title}"')
    lines.append("---")
    lines.append("")
    lines.append(f"# {site.index_heading}")
    lines.append("")
    lines.append("Willkommen zur Schülerausgabe der Unterrichtsmaterialien. "
                 "Die Lehrkraft schaltet die Phasen jeder Lektion über das "
                 "Lernmanagementsystem (Moodle / itslearning) schrittweise frei.")
    lines.append("")
    lines.append("## Lektionen")
    lines.append("")
    for entry in nav_entries:
        slug = entry["slug"]
        lesson_id = entry["lesson_id"]
        label = entry["label"]
        lines.append(f"### {label}")
        lines.append("")
        lines.append(f"- [Übersicht]({slug}/index.md)")
        for phase in entry["phases"]:
            p_label = phase["title"]
            p_file = phase["file"]
            lines.append(f"- [{p_label}]({slug}/{p_file})")
        # Direktlink auf die ausführliche Musterlösung (aus solutions/)
        sol_file = entry.get("solution_file")
        if sol_file and site.link_solutions:
            lines.append(f"- [Ausführliche Musterlösung](solutions/{sol_file})")
        lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*Diese Seiten werden automatisch aus den Quelldateien generiert. "
                 "Letzte Aktualisierung erfolgt bei jedem Push ins Repository.*")
    lines.append("")

    (out_docs / "index.md").write_text("\n".join(lines), encoding="utf-8")


def generate_extra_css(out_docs: Path) -> None:
    """Schreibt zusätzliches CSS für das Layout der Schülerausgabe."""
    css_dir = out_docs / "stylesheets"
    css_dir.mkdir(parents=True, exist_ok=True)
    css = (
        "/* Schülerausgabe: Inhalt auf breiten Bildschirmen zentrieren. */\n"
        "@media screen and (min-width: 76.25em) {\n"
        "  .md-main__inner { justify-content: center; }\n"
        "  .md-content { max-width: 60rem; }\n"
        "}\n"
    )
    (css_dir / "extra.css").write_text(css, encoding="utf-8")


# ========================== Workflow 2: Lehrer-Abschnitte entfernen ========

def strip_teacher_sections(content: str) -> str:
    """Remove teacher-only sections from lesson content.

    Entfernt: "# Didaktische Hinweise", "# Lösungen …", "## Bewertungskriterien"
    und "## Erwartungshorizont …" (jeweils bis zur nächsten Top-Level-Überschrift).
    """
    lines = content.split("\n")
    result = []
    skip = False

    for line in lines:
        # Stop including content when we hit "# Didaktische Hinweise"
        if re.match(r"^#\s+Didaktische Hinweise", line):
            skip = True
            continue

        # Stop including content when we hit "# Lösungen / Handlungsergebnisse"
        if re.match(r"^#\s+Lösungen", line):
            skip = True
            continue

        # Also skip "## Bewertungskriterien" subsections within other sections
        if re.match(r"^##\s+Bewertungskriterien", line):
            skip = True
            continue

        # Also skip "## Erwartungshorizont" and "## Erwartungshorizont der Vertiefungen"
        if re.match(r"^##\s+Erwartungshorizont", line):
            skip = True
            continue

        # Resume when we hit next top-level heading (if we were skipping a subsection)
        if skip and re.match(r"^#\s+[^#]", line):
            skip = False

        if not skip:
            result.append(line)

    # Remove trailing empty lines
    while result and result[-1].strip() == "":
        result.pop()

    return "\n".join(result) + "\n"


def generate_student_site(
    teacher_docs: Path,
    student_docs: Path,
    lernfelder: dict[str, list[str]],
) -> int:
    """Erzeugt Schülerdateien, indem Lehrer-Abschnitte entfernt werden.

    teacher_docs / student_docs: Wurzelverzeichnisse.
    lernfelder: {lernfeld_ordner: [dateiname, ...]}.
    Gibt die Anzahl erzeugter Dateien zurück.
    """
    teacher_docs = Path(teacher_docs)
    student_docs = Path(student_docs)
    count = 0
    for lf, lessons in lernfelder.items():
        for lesson in lessons:
            teacher_path = teacher_docs / lf / lesson
            student_path = student_docs / lf / lesson

            if not teacher_path.exists():
                print(f"WARNING: {teacher_path} not found, skipping")
                continue

            content = teacher_path.read_text(encoding="utf-8")
            student_content = strip_teacher_sections(content)

            student_path.parent.mkdir(parents=True, exist_ok=True)
            student_path.write_text(student_content, encoding="utf-8")
            count += 1
            print(f"Created: {student_path.relative_to(student_docs)}")

    print(f"\nDone: {count} student lesson files created.")
    return count


# ========================== Hauptprogramm (split) ==========================

def run_split(
    scripts_dir: Path | None = None,
    project_root: Path | None = None,
    config: Path | None = None,
    out: Path | None = None,
    no_resources: bool = False,
) -> None:
    """Erzeugt die Schülerausgabe aus den lesson.md-Dateien (split_lessons).

    Pfad-Auflösung (reproduziert das frühere skript-relative Verhalten):
      scripts_dir   – Verzeichnis eines Shim-Skripts (Default: keins → cwd)
      project_root  – Default: scripts_dir.parent, sonst cwd
      config        – Default: <scripts_dir>/phase_config.yaml,
                      sonst <project_root>/scripts/phase_config.yaml,
                      sonst mitgelieferte Standard-Config
      out           – Default: <project_root>/_student_site
    """
    scripts_dir = Path(scripts_dir).resolve() if scripts_dir else None
    if project_root is not None:
        project_root = Path(project_root)
    else:
        project_root = scripts_dir.parent if scripts_dir else Path.cwd()

    if config is not None:
        config_path = Path(config)
    else:
        kandidaten = []
        if scripts_dir:
            kandidaten.append(scripts_dir / "phase_config.yaml")
        kandidaten.append(project_root / "scripts" / "phase_config.yaml")
        config_path = next((c for c in kandidaten if c.exists()), default_config_path())

    out_root = Path(out) if out else (project_root / "_student_site")
    lessons_dir = project_root / "lessons"
    out_docs = out_root / "docs"

    print(f"Projektwurzel:  {project_root}")
    print(f"Konfiguration:  {config_path}")
    print(f"Ausgabe:        {out_root}")
    print()

    # Konfiguration laden
    phases, excluded, excluded_lessons = load_phase_config(config_path)
    site = load_site_config(config_path)

    # Musterlösungen dürfen nur verlinkt werden, wenn solutions/ auch kopiert
    # wird – sonst entstehen tote Links (und `mkdocs build --strict` bricht ab).
    if site.link_solutions and "solutions" not in site.copy_dirs:
        print("  ⚠  site.link_solutions ist aktiv, aber 'solutions' fehlt in "
              "site.copy_dirs – Musterlösungs-Links werden weggelassen.")
        site = site._replace(link_solutions=False)
    if "solutions" in site.copy_dirs:
        print("  ⚠  solutions/ wird in die Schülerausgabe kopiert – die "
              "Musterlösungen sind damit veröffentlicht.")

    section_to_phase: dict[str, PhaseSpec] = {}
    for phase in phases:
        for sec in phase.sections:
            section_to_phase[sec] = phase

    # Ausgabeverzeichnis vorbereiten
    if out_docs.exists():
        shutil.rmtree(out_docs)
    out_docs.mkdir(parents=True, exist_ok=True)

    # Lessons verarbeiten
    lesson_files = discover_lessons(lessons_dir)
    if not lesson_files:
        print("⚠  Keine lesson.md-Dateien gefunden.")
        sys.exit(1)

    print(f"Gefundene Lektionen: {len(lesson_files)}")
    print()

    nav_entries: list[dict] = []

    for lesson_path in lesson_files:
        lesson_folder = lesson_path.parent.name  # z.B. 01_einstieg_smart_office_projekt
        raw = lesson_path.read_text(encoding="utf-8")
        fm_text, body = parse_frontmatter(raw)
        # Ein Kennzeichnungsblock am Ende der lesson.md gehört zur Quelldatei,
        # nicht zum letzten Fachabschnitt – sonst landete er mitten in einer
        # Phasenseite. Die Ausgabe bekommt weiter unten einen eigenen Hinweis
        # mit passendem relativem Link.
        body = entferne_block(body)
        lesson_title = extract_frontmatter_field(fm_text, "title")
        lesson_id = extract_frontmatter_field(fm_text, "lesson_id")

        if not lesson_id:
            # Fallback: aus Ordnername
            m = re.match(r"(\d+)", lesson_folder)
            lesson_id = m.group(1) if m else "??"

        # Ausgeschlossene Lektionen überspringen
        if any(lesson_folder.startswith(f"{ex}_") or lesson_id == ex
               or lesson_folder == ex
               for ex in excluded_lessons):
            print(f"⏭  Lektion {lesson_id}: {lesson_title} (ausgeschlossen)")
            continue

        print(f"📖 Lektion {lesson_id}: {lesson_title}")

        # Abschnitte extrahieren
        all_sections = split_into_sections(body)

        # Abschnitte den Phasen zuordnen
        phase_sections: dict[int, list[LessonSection]] = {p.phase_id: [] for p in phases}
        unmatched: list[str] = []

        for section in all_sections:
            heading = section.heading
            if heading in excluded:
                continue  # Didaktische Hinweise etc. ausschließen
            if heading in section_to_phase:
                phase = section_to_phase[heading]
                phase_sections[phase.phase_id].append(section)
            else:
                unmatched.append(heading)

        if unmatched:
            print(f"  ⚠  Nicht zugeordnete Abschnitte: {unmatched}")

        # Ausgabeordner erstellen
        lesson_out = out_docs / lesson_folder
        lesson_out.mkdir(parents=True, exist_ok=True)

        # Phasen-Dateien erzeugen
        nav_phases: list[dict] = []
        for phase in phases:
            secs = phase_sections[phase.phase_id]
            if not secs:
                continue  # Phase ohne Inhalt überspringen

            filename = f"{phase.phase_id:02d}_{phase.slug}.md"
            content = generate_phase_page(
                lesson_title=lesson_title,
                lesson_id=lesson_id,
                phase=phase,
                sections=secs,
                total_phases=len(phases),
            )
            # Relative Links anpassen
            content = fix_relative_links(content, source_depth=2, target_depth=2)
            (lesson_out / filename).write_text(content, encoding="utf-8")
            nav_phases.append({"title": phase.title, "file": filename})
            print(f"  ✓ {filename}")

        # Prüfen, ob eine ausführliche Musterlösung in solutions/ existiert
        sol_candidates = list(
            (project_root / "solutions").glob(f"{lesson_folder}_loesungen.md")
        )
        solution_filename = sol_candidates[0].name if sol_candidates else None

        # Index-Seite erzeugen (nur Phasen mit Inhalt)
        active_phases = [p for p in phases if phase_sections[p.phase_id]]
        index_content = generate_lesson_index(
            lesson_title=lesson_title,
            lesson_id=lesson_id,
            fm_text=fm_text,
            phases=active_phases,
            lesson_slug=lesson_folder,
            solution_filename=solution_filename if site.link_solutions else None,
            solution_link_max_lesson=site.solution_link_max_lesson,
        )
        (lesson_out / "index.md").write_text(index_content, encoding="utf-8")

        nav_entries.append({
            "label": f"{lesson_id} – {lesson_title}",
            "lesson_id": lesson_id,
            "slug": lesson_folder,
            "phases": nav_phases,
            "solution_file": solution_filename,
        })

    print()

    # Ressourcen kopieren
    if not no_resources:
        print("Ressourcen kopieren:")
        copy_resources(project_root, out_docs, dirs=site.copy_dirs)
        if site.ki_hinweis is not None:
            copy_ki_transparenz(project_root, out_docs, site.ki_hinweis)
        print()

    # Schüler-MkDocs erzeugen
    generate_student_mkdocs(out_root, nav_entries, site=site)
    print(f"✓ mkdocs.yml erzeugt")

    # Startseite erzeugen
    generate_student_index(out_docs, nav_entries, site=site)
    print(f"✓ index.md erzeugt")

    # Zusätzliches CSS für reduziertes Layout
    generate_extra_css(out_docs)
    print("✓ stylesheets/extra.css erzeugt")

    # KI-Transparenzhinweis unter jede Seite – zuletzt, damit auch die eben
    # erzeugten Start- und Übersichtsseiten erfasst werden.
    if site.ki_hinweis is not None:
        n = apply_ki_hinweise(out_docs, site.ki_hinweis)
        print(f"✓ KI-Transparenzhinweis auf {n} Seiten gesetzt")

    print()
    print("═" * 60)
    print("  Schülerausgabe erfolgreich generiert!")
    print(f"  Ausgabeverzeichnis: {out_root}")
    print()
    print("  Vorschau starten:")
    print(f"    cd {out_root} && mkdocs serve")
    print()
    print("  Statische Site bauen:")
    print(f"    cd {out_root} && mkdocs build")
    print("═" * 60)
