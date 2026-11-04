#!/usr/bin/env python3
"""quiz – eine Markdown-Quelle → mehrere Quiz-Zielformate (GIFT + H5P).

Idee (Determinismus & „ein System"):
    Es gibt **eine** kanonische Quizquelle: das bereits in ``eduwerkzeuge.h5p``
    etablierte Markdown-Format (``## Übung N – Desc (H5P.Typ) | AFB X``).
    Diese Datei wird **einmal** geparst (über ``h5p.parse_exercise``) und dann
    in beliebige Zielformate exportiert:

      * ``.h5p``  – interaktiv (Reuse von ``h5p.write_h5p_file``)
      * ``.gift`` – Moodle-Fragensammlung (dieser Exporter, getestet, korrekt
        escaped)

    Der LLM-Schritt erzeugt also nur noch **Inhalt** (das Quell-Markdown); die
    fehleranfällige Formaterzeugung (GIFT-Escaping, eine 100 %-Lösung bei
    Single-Choice, Prozente bei Multiple-Response) ist deterministischer,
    getesteter Code.

Die h5p-Parser reduzieren alle Eingabetypen auf sechs Bibliotheken
(MultiChoice, TrueFalse, Blanks, DragText, SortParagraphs, Essay) – Matching,
QuestionSet etc. werden bereits dort darauf abgebildet. Entsprechend gibt es
hier genau sechs Exporter.

GIFT-Referenz: ``Toolkit/02_Skill_Quizfragen/Referenz_GIFT_Format.md``.
"""

from __future__ import annotations

import html as _html
import re
from pathlib import Path
from typing import Iterable, Optional

from eduwerkzeuge.h5p import core as _h5p


# ──────────────────────────────────────────────────────────────
# GIFT-Hilfen: Escaping & HTML→Text
# ──────────────────────────────────────────────────────────────

# Reihenfolge wichtig: Backslash zuerst, sonst werden die Escapes selbst escaped.
_GIFT_SPECIALS = ("\\", "{", "}", "=", "~", "#", ":")


def gift_escape(text: Optional[str]) -> str:
    """Escapt die GIFT-Sonderzeichen ``\\ { } = ~ # :`` mit Backslash.

    Wird auf **literalen** Text angewandt (Titel, Fragetext, Antworttext,
    Feedback) – niemals auf die GIFT-Marker (``=``/``~``/``#``/``{}``), die der
    Exporter selbst setzt.
    """
    if not text:
        return ""
    for ch in _GIFT_SPECIALS:
        text = text.replace(ch, "\\" + ch)
    return text


def _html_to_text(s: Optional[str]) -> str:
    """Wandelt das von H5P gespeicherte HTML in reinen Text.

    ``<br>`` und Block-Endtags werden zu Zeilenumbrüchen, übrige Tags entfernt,
    HTML-Entities aufgelöst. Reine Textausgabe ist für den GIFT-Import am
    robustesten (keine ``[html]``-Abhängigkeit).
    """
    if not s:
        return ""
    s = re.sub(r"(?i)<br\s*/?>", "\n", s)
    s = re.sub(r"(?i)</(p|div|pre|li|tr)\s*>", "\n", s)
    s = re.sub(r"<[^>]+>", "", s)        # restliche Tags strippen
    s = _html.unescape(s)
    s = re.sub(r"[ \t]+\n", "\n", s)     # trailing spaces je Zeile
    return s.strip()


def _gift_block_text(s: str) -> str:
    """Text für GIFT-Frageköpfe: Leerzeilen entfernen.

    In GIFT trennt eine **Leerzeile** zwei Fragen. Innerhalb einer Frage darf
    daher keine Leerzeile stehen – Mehrfach-Umbrüche werden zu einem einzigen
    Zeilenumbruch zusammengezogen (einfache Umbrüche, z. B. in Code, bleiben).
    """
    return re.sub(r"\n\s*\n+", "\n", s).strip()


def _fmt_pct(value: float) -> str:
    """Prozentwert ohne überflüssige Nachkommastellen (z. B. 50, 33.33333)."""
    return f"{value:.5f}".rstrip("0").rstrip(".")


def _title_prefix(q: dict) -> str:
    title = (q.get("metadata") or {}).get("title", "") or ""
    title = title.strip()
    return f"::{gift_escape(title)}:: " if title else ""


# ──────────────────────────────────────────────────────────────
# Cloze-Lücken (für H5P.Blanks und H5P.DragText)
# ──────────────────────────────────────────────────────────────

_BLANK_RE = re.compile(r"\*([^*\n]+)\*")


_ZAHL_RE = re.compile(r"^-?\d+(?:[.,]\d+)?$")


def _gap_to_gift(content: str) -> str:
    """``*antwort*`` / ``*antwort:tipp*`` / ``*a/b/c*`` → ``{=a =b ...}``.

    Zahlen werden numerische Antworten: ``*22,7±0,3*`` → ``{#22.7:0.3}``, ``*25*`` → ``{#25}``
    (Moodle akzeptiert dann Komma und Punkt; bei Toleranz jeden Wert im Bereich).
    """
    z = _h5p.zahl_luecke(content)
    if z:
        return "{#" + z[0].replace(",", ".") + ":" + f"{z[2]:g}" + "}"
    if _ZAHL_RE.match(content.strip()):
        return "{#" + content.strip().replace(",", ".") + "}"
    main = content
    if ":" in content:                    # H5P-Tipp nach ':' – für GIFT verworfen
        main = content.split(":", 1)[0]
    alts = [a.strip() for a in main.split("/") if a.strip()]
    if not alts:
        return "{}"
    inner = " ".join("=" + gift_escape(a) for a in alts)
    return "{" + inner + "}"


def _cloze_from_text(text: str, nur: Optional[int] = None) -> str:
    """Ersetzt ``*marker*`` durch GIFT-Lücken; escapt den Text dazwischen.

    ``nur``: nur die Lücke mit diesem Index (0-basiert) wird zum Antwortblock, die übrigen
    erscheinen als „…“ – Moodle wertet je Frage nur **einen** Antwortblock aus.
    """
    out: list[str] = []
    last = 0
    for i, m in enumerate(_BLANK_RE.finditer(text)):
        out.append(gift_escape(text[last:m.start()]))
        out.append(_gap_to_gift(m.group(1)) if nur is None or i == nur else "…")
        last = m.end()
    out.append(gift_escape(text[last:]))
    return "".join(out)


def _cloze_fragen(q: dict, teile: list[str]) -> Optional[str]:
    """Eine GIFT-Frage je Lücke (Moodle: ein Antwortblock je Frage).

    Bei mehreren Lücken bekommt jede Frage den Titel „Titel (k/n)“; die anderen Lücken
    desselben Absatzes stehen als „…“ im Text.
    """
    luecken = [(t, i) for t in teile for i, _ in enumerate(_BLANK_RE.finditer(t))]
    if not luecken:
        return None
    titel = ((q.get("metadata") or {}).get("title", "") or "").strip()
    n = len(luecken)
    bloecke = []
    for k, (teil, i) in enumerate(luecken, 1):
        t = f"{titel} ({k}/{n})" if n > 1 and titel else titel
        prefix = f"::{gift_escape(t)}:: " if t else ""
        bloecke.append(prefix + _cloze_from_text(teil, nur=i))
    return "\n\n".join(bloecke)


# ──────────────────────────────────────────────────────────────
# Exporter je H5P-Bibliothek  (params-Form siehe h5p.core.build_*)
# ──────────────────────────────────────────────────────────────

def _mc_to_gift(q: dict) -> Optional[str]:
    p = q.get("params", {})
    qtext = gift_escape(_gift_block_text(_html_to_text(p.get("question", ""))))
    answers = [a for a in p.get("answers", []) if _html_to_text(a.get("text", ""))]
    if not qtext or not answers:
        return None

    n_correct = sum(1 for a in answers if a.get("correct"))
    n_wrong = len(answers) - n_correct
    single = n_correct <= 1                # genau eine richtige → '='/'~'

    lines: list[str] = []
    warn = ""
    if n_correct == 0:
        warn = "// WARNUNG: keine als richtig markierte Antwort.\n"

    for a in answers:
        atext = gift_escape(_html_to_text(a.get("text", "")))
        fb = _html_to_text((a.get("tipsAndFeedback") or {}).get("chosenFeedback", ""))
        fb_part = "#" + gift_escape(fb) if fb else ""
        if single:
            marker = "=" if a.get("correct") else "~"
            lines.append(f"{marker}{atext}{fb_part}")
        elif a.get("correct"):
            lines.append(f"~%{_fmt_pct(100.0 / n_correct)}%{atext}{fb_part}")
        else:
            pct = _fmt_pct(100.0 / n_wrong) if n_wrong else "0"
            lines.append(f"~%-{pct}%{atext}{fb_part}")

    overall = p.get("overallFeedback") or []
    gfb = _html_to_text(overall[0].get("feedback", "")) if overall and isinstance(overall[0], dict) else ""
    body = "\n".join(lines)
    if gfb:
        body += f"\n####{gift_escape(gfb)}"

    return f"{warn}{_title_prefix(q)}{qtext} {{\n{body}\n}}"


def _tf_to_gift(q: dict) -> Optional[str]:
    p = q.get("params", {})
    qtext = gift_escape(_gift_block_text(_html_to_text(p.get("question", ""))))
    if not qtext:
        return None
    correct = str(p.get("correct", "")).lower() in ("true", "1", "yes")
    tf = "T" if correct else "F"
    wrong = _html_to_text((p.get("l10n") or {}).get("wrongAnswerMessage", ""))
    fb_part = ""
    if wrong and wrong != "Leider falsch.":
        fb_part = "#" + gift_escape(wrong)
    return f"{_title_prefix(q)}{qtext} {{{tf}{fb_part}}}"


def _blanks_to_gift(q: dict) -> Optional[str]:
    p = q.get("params", {})
    quelle = q.get("_gift_questions") or p.get("questions", [])   # mit Toleranzen, falls vorhanden
    teile = [_gift_block_text(_html_to_text(html)) for html in quelle]
    return _cloze_fragen(q, [t for t in teile if "*" in t])


def _dragtext_to_gift(q: dict) -> Optional[str]:
    p = q.get("params", {})
    text = _gift_block_text(_html_to_text(p.get("textField", "")))
    if "*" not in text:
        return None
    return _cloze_fragen(q, [text])


def _essay_to_gift(q: dict) -> Optional[str]:
    p = q.get("params", {})
    task = gift_escape(_gift_block_text(_html_to_text(p.get("taskDescription", ""))))
    if not task:
        return None
    notes = []
    kws = [k.get("keyword", "") for k in p.get("keywords", []) if k.get("keyword")]
    if kws:
        notes.append("// Erwartete Begriffe: " + ", ".join(kws))
    sample = (p.get("solution") or {}).get("sample", "")
    if sample:
        sample = _html_to_text(sample).replace("\n", " ")
        notes.append("// Musterlösung: " + sample)
    prefix = ("\n".join(notes) + "\n") if notes else ""
    return f"{prefix}{_title_prefix(q)}{task} {{}}"


def _sort_to_gift(q: dict) -> Optional[str]:
    p = q.get("params", {})
    task = _gift_block_text(_html_to_text(p.get("taskDescription", "")))
    paragraphs = [_html_to_text(x.get("text", "")) for x in p.get("paragraphs", [])]
    paragraphs = [x for x in paragraphs if x]
    if not paragraphs:
        return None
    order = " | ".join(f"{i}. {t}" for i, t in enumerate(paragraphs, 1))
    note = ("// SortParagraphs: in GIFT kein interaktiver Typ – als Freitext "
            "(manuell) exportiert.\n"
            f"// Korrekte Reihenfolge: {order}\n")
    task = gift_escape(task) if task else "Bringe die Elemente in die richtige Reihenfolge."
    return f"{note}{_title_prefix(q)}{task} {{}}"


_GIFT_EXPORTERS = {
    "H5P.MultiChoice": _mc_to_gift,
    "H5P.TrueFalse": _tf_to_gift,
    "H5P.Blanks": _blanks_to_gift,
    "H5P.DragText": _dragtext_to_gift,
    "H5P.Essay": _essay_to_gift,
    "H5P.SortParagraphs": _sort_to_gift,
}


def question_to_gift(question: dict) -> Optional[str]:
    """Ein H5P-Frage-Dict (aus ``h5p.parse_exercise``) → ein GIFT-Block.

    Gibt ``None`` zurück, wenn der Typ in GIFT nicht abbildbar/leer ist.
    """
    lib = (question.get("library", "").split() or [""])[0]
    exporter = _GIFT_EXPORTERS.get(lib)
    return exporter(question) if exporter else None


def questions_to_gift(
    questions: Iterable[dict],
    *,
    category: Optional[str] = None,
    header_comment: bool = True,
) -> str:
    """Liste von H5P-Frage-Dicts → vollständiger GIFT-Dateiinhalt (UTF-8)."""
    blocks: list[str] = []
    if header_comment:
        blocks.append("// GIFT-Datei erzeugt mit eduwerkzeuge (edu-quiz). UTF-8.")
    if category:
        blocks.append(f"$CATEGORY: {category}")
    for q in questions:
        g = question_to_gift(q)
        if g:
            blocks.append(g)
    return "\n\n".join(blocks) + "\n"


# ──────────────────────────────────────────────────────────────
# Markdown-Quelle → Fragen → Zielformate
# ──────────────────────────────────────────────────────────────

def parse_markdown(md_text: str) -> tuple[int, str, list[dict]]:
    """Quell-Markdown → (lektion_nr, titel, [H5P-Frage-Dicts]). Einmal parsen."""
    lesson_num, title, exercises = _h5p.split_exercises(md_text)
    questions: list[dict] = []
    for ex in exercises:
        questions.extend(_h5p.parse_exercise(ex))
    return lesson_num, title, questions


def markdown_to_gift(md_text: str, *, category: Optional[str] = None) -> str:
    """Bequemlichkeit: Quell-Markdown direkt → GIFT-String."""
    _, _, questions = parse_markdown(md_text)
    return questions_to_gift(questions, category=category)


_VALID_FORMATS = ("gift", "h5p")


def convert_file(
    src: Path | str,
    out_dir: Path | str | None = None,
    *,
    formats: Iterable[str] = _VALID_FORMATS,
    category: Optional[str] = None,
) -> list[Path]:
    """Eine ``.md``-Quelle → ``.gift`` und/oder ``.h5p`` im Zielordner.

    Schreibt ``<stem>.gift`` / ``<stem>.h5p``. ``out_dir`` Default = Ordner der
    Quelle. Gibt die geschriebenen Pfade zurück (leer, wenn keine Fragen).
    """
    src = Path(src)
    formats = [f for f in formats if f in _VALID_FORMATS]
    md = src.read_text(encoding="utf-8")
    _, title, questions = parse_markdown(md)
    if not questions:
        return []

    out_dir = Path(out_dir) if out_dir else src.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    if "gift" in formats:
        gp = out_dir / f"{src.stem}.gift"
        gp.write_text(questions_to_gift(questions, category=category), encoding="utf-8")
        written.append(gp)
    if "h5p" in formats:
        hp = out_dir / f"{src.stem}.h5p"
        _h5p.write_h5p_file(str(hp), title, questions)
        written.append(hp)
    return written
