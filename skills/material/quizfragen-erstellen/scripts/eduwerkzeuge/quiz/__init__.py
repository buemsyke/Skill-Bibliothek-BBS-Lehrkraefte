"""quiz – eine Markdown-Quelle → mehrere Quiz-Zielformate (GIFT + H5P).

Die kanonische Quelle ist das h5p-Markdown-Format; ``quiz`` parst es einmal
(über ``eduwerkzeuge.h5p``) und exportiert deterministisch nach GIFT und/oder
H5P.

Beispiel:
    from eduwerkzeuge.quiz import markdown_to_gift, convert_file
    gift = markdown_to_gift(md_text, category="LF5/Grundlagen")
    convert_file("quiz.md", formats=("gift", "h5p"))   # → quiz.gift + quiz.h5p
"""

from .core import (
    convert_file,
    gift_escape,
    markdown_to_gift,
    parse_markdown,
    question_to_gift,
    questions_to_gift,
)

__all__ = [
    "convert_file",
    "gift_escape",
    "markdown_to_gift",
    "parse_markdown",
    "question_to_gift",
    "questions_to_gift",
]
