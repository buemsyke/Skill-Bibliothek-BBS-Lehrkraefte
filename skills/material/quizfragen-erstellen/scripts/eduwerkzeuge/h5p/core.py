#!/usr/bin/env python3
"""Erzeugt H5P-Dateien (.h5p) aus Markdown-Quiz-Definitionen.

Liest alle ``*.md`` (außer README.md) aus dem ``h5p/``-Verzeichnis eines
Projekts und erzeugt die zugehörigen ``.h5p``-Dateien in ``h5p/generated/``.

``project_dir`` (Default: aktuelles Arbeitsverzeichnis) ist das Projekt-
Wurzelverzeichnis; ein Shim unter ``scripts/`` übergibt
``Path(__file__).parent.parent`` und reproduziert damit exakt das frühere
``Path(__file__).parent.parent``.
"""

import html as html_mod
import json
import os
import sys
import re
import uuid
import zipfile
from pathlib import Path


# ──────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────

def new_uuid():
    """Generate new UUID for H5P sub-content."""
    return str(uuid.uuid4())


def html_escape(text):
    """Escape HTML special characters."""
    return html_mod.escape(text, quote=True)


# ──────────────────────────────────────────────────────────────
# Markdown Parsing – Generic
# ──────────────────────────────────────────────────────────────

def split_exercises(md_content):
    """Split markdown into lesson metadata and individual exercise texts."""
    parts = re.split(r'(?=^## Übung )', md_content, flags=re.MULTILINE)
    header_part = parts[0]
    exercises = [p.strip() for p in parts[1:] if p.strip()]

    title_match = re.search(r'^# .+?Lektion\s*(\d+)\s*:\s*(.+)', header_part, re.MULTILINE)
    if title_match:
        lesson_num = int(title_match.group(1))
        title = title_match.group(2).strip()
    else:
        lesson_num = 0
        title = "Quiz"

    return lesson_num, title, exercises


def parse_exercise_header(text):
    """Extract metadata from ## Übung N – Desc (H5P.Type) | AFB X."""
    first_line = text.split('\n')[0]
    m = re.match(
        r'## Übung\s+(\d+)\s*[–\-]\s*(.+?)\s*\((H5P\.\w+)\)\s*\|\s*AFB\s*(.+)',
        first_line,
    )
    if m:
        return {
            'number': int(m.group(1)),
            'description': m.group(2).strip(),
            'h5p_type': m.group(3).strip(),
            'afb': m.group(4).strip(),
        }
    # Fallback without AFB
    m = re.match(
        r'## Übung\s+(\d+)\s*[–\-]\s*(.+?)\s*\((H5P\.\w+)\)',
        first_line,
    )
    if m:
        return {
            'number': int(m.group(1)),
            'description': m.group(2).strip(),
            'h5p_type': m.group(3).strip(),
            'afb': '',
        }
    return None


def extract_title(text):
    """Extract **Titel:** value.

    Fehlt die Zeile, gilt die Beschreibung aus der Kopfzeile
    (``## Übung N – Beschreibung (H5P.Typ)``) – sonst hießen alle Fragen
    gleich „Übung“ und wären in der Moodle-Fragensammlung nicht unterscheidbar.
    """
    m = re.search(r'\*\*Titel:\*\*\s*(.+)', text)
    if m:
        return m.group(1).strip()
    header = parse_exercise_header(text)
    return header['description'] if header else "Übung"


def extract_blockquote(text):
    """Extract blockquote text (lines starting with >)."""
    lines = []
    in_quote = False
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('>'):
            in_quote = True
            content = re.sub(r'^>\s?', '', stripped)
            lines.append(content)
        elif in_quote and stripped == '':
            lines.append('')
        elif in_quote:
            in_quote = False
    return '\n'.join(lines).strip()


def convert_blank_markers(text):
    r"""Convert **\*answer\*** → *answer* for H5P."""
    return re.sub(r'\*\*\\\*(.+?)\\\*\*\*', r'*\1*', text)


# Eine bereits umgewandelte Lücke: einzelnes Sternchenpaar innerhalb einer Zeile.
HAS_BLANK_RE = re.compile(r'(?<!\*)\*[^*\n]+\*(?!\*)')

# Zahlenlücke mit Toleranz: ``*22,7±0,3*`` (auch ``+/-``). Moodle (GIFT) wertet mit
# Toleranz, H5P.Blanks kennt keine Toleranz und erhält Alternativen.
ZAHL_LUECKE_RE = re.compile(
    r'^\s*(-?\d+(?:[.,]\d+)?)\s*(?:±|\+/-|\+-)\s*(\d+(?:[.,]\d+)?)\s*$')


def zahl_luecke(inhalt):
    """``'22,7±0,3'`` → ``('22,7', 22.7, 0.3)``; sonst ``None``."""
    m = ZAHL_LUECKE_RE.match(inhalt or '')
    if not m:
        return None
    return m.group(1), float(m.group(1).replace(',', '.')), float(m.group(2).replace(',', '.'))


def h5p_zahl_alternativen(inhalt):
    """Zahlenlücke → H5P-Alternativen: Wert mit Komma und Punkt, gerundete ganze Zahl,
    wenn sie in der Toleranz liegt. Andere Lücken bleiben unverändert."""
    z = zahl_luecke(inhalt)
    if not z:
        return inhalt
    text, wert, tol = z
    alt = [text.replace('.', ','), text.replace(',', '.')]
    ganz = round(wert)
    if abs(ganz - wert) <= tol + 1e-9:
        alt.append(str(ganz))
    return '/'.join(dict.fromkeys(alt))


def _zahl_luecken_fuer_h5p(html):
    return HAS_BLANK_RE.sub(lambda m: '*' + h5p_zahl_alternativen(m.group(0)[1:-1]) + '*', html)


def extract_code_block(text):
    """Extract first fenced code block content."""
    m = re.search(r'```\w*\n(.*?)```', text, re.DOTALL)
    return m.group(1).strip() if m else ""


# Spaltentrenner einer Markdown-Tabelle: nur ein unmaskiertes ``|``.
_TABLE_PIPE_RE = re.compile(r'(?<!\\)\|')


def _split_table_row(line):
    r"""Zerlegt eine Markdown-Tabellenzeile in Zellen.

    Getrennt wird nur an unmaskierten ``|``. Wie in GFM steht ``\|`` für einen
    senkrechten Strich in der Zelle, auch in Code (``$a \|\| $b`` → ``$a || $b``).
    """
    cells = _TABLE_PIPE_RE.split(line.strip())
    # Leere Elemente vor dem ersten und nach dem letzten Trenner entfernen
    if cells and cells[0].strip() == '':
        cells = cells[1:]
    if cells and cells[-1].strip() == '':
        cells = cells[:-1]
    return [c.strip().replace('\\|', '|') for c in cells]


def extract_table_rows(text):
    """Return list of table rows as lists of cell strings (excluding separator)."""
    rows = []
    for line in text.split('\n'):
        if line.strip().startswith('|'):
            cells = _split_table_row(line)
            # Skip separator rows
            if cells and all(re.match(r'^[\-:]+$', c) for c in cells):
                continue
            rows.append(cells)
    return rows


# ──────────────────────────────────────────────────────────────
# H5P Content Builders
# ──────────────────────────────────────────────────────────────

# Ein "<", das kein Tag beginnt (`$t < 55`, `<=`, `<?php`). Absichtliche Tags
# wie <u>…</u> (Primärschlüssel in BINFQ2) bleiben erhalten.
_LOSES_KLEINER_RE = re.compile(r'<(?![A-Za-z/!])')


def _md_inline_to_html(s):
    """Convert simple inline Markdown (bold/italic/code) to HTML."""
    if not s:
        return s
    # Loses "<" maskieren – sonst hielte es der GIFT-Export für einen Tag und
    # schluckte den Text bis zum nächsten ">".
    s = _LOSES_KLEINER_RE.sub('&lt;', s)
    # Code spans first so emphasis inside backticks is preserved
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'__(.+?)__', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'<em>\1</em>', s)
    s = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'<em>\1</em>', s)
    return s


def build_multichoice(question_html, answers, feedback="", title=""):
    """Build H5P.MultiChoice question dict.

    answers: list of {'correct': bool, 'text': str, 'feedback': str (optional)}
    Per-answer feedback is stored under tipsAndFeedback.chosenFeedback so it
    only appears after the learner selects that answer.
    """
    ans_list = []
    for a in answers:
        ans_text = _md_inline_to_html(a['text'])
        chosen_fb = _md_inline_to_html(a.get('feedback', '').strip())
        ans_list.append({
            'correct': a['correct'],
            'text': f"<div>{ans_text}</div>",
            'tipsAndFeedback': {
                'tip': '',
                'chosenFeedback': chosen_fb,
                'notChosenFeedback': '',
            },
        })

    correct_count = sum(1 for a in answers if a['correct'])
    return {
        'library': 'H5P.MultiChoice 1.16',
        'params': {
            'question': f"<p>{question_html}</p>",
            'answers': ans_list,
            'overallFeedback': [
                {'from': 0, 'to': 100, 'feedback': feedback}
            ] if feedback else [{'from': 0, 'to': 100}],
            'behaviour': {
                'enableRetry': True,
                'enableSolutionsButton': True,
                'enableCheckButton': True,
                'type': 'auto',
                'singlePoint': correct_count <= 1,
                'randomAnswers': True,
                'showSolutionsRequiresInput': True,
                'confirmCheckDialog': False,
                'confirmRetryDialog': False,
                'autoCheck': False,
                'passPercentage': 100,
            },
            'media': {'disableImageZooming': False},
            'UI': {
                'checkAnswerButton': 'Überprüfen',
                'submitAnswerButton': 'Absenden',
                'showSolutionButton': 'Lösung anzeigen',
                'tryAgainButton': 'Wiederholen',
                'tipsLabel': 'Tipp anzeigen',
                'scoreBarLabel': 'Du hast :num von :total Punkten.',
                'tipAvailable': 'Tipp verfügbar',
                'feedbackAvailable': 'Feedback verfügbar',
                'readFeedback': 'Feedback vorlesen',
                'wrongAnswer': 'Falsche Antwort',
                'correctAnswer': 'Richtige Antwort',
                'shouldCheck': 'Hätte ausgewählt werden sollen',
                'shouldNotCheck': 'Hätte nicht ausgewählt werden sollen',
                'noInput': 'Bitte antworte, bevor du die Lösung anschaust',
            },
        },
        'subContentId': new_uuid(),
        'metadata': {
            'contentType': 'Multiple Choice',
            'license': 'U',
            'title': title or 'Multiple Choice',
        },
    }


def build_blanks(questions_html, title=""):
    """Build H5P.Blanks content.

    questions_html: list of HTML strings, each with *blank* markers.
    """
    return {
        'library': 'H5P.Blanks 1.14',
        'params': {
            'questions': questions_html,
            'overallFeedback': [{'from': 0, 'to': 100}],
            'showSolutions': 'Lösung anzeigen',
            'tryAgain': 'Wiederholen',
            'checkAnswer': 'Überprüfen',
            'submitAnswer': 'Absenden',
            'notFilledOut': 'Bitte fülle alle Lücken aus.',
            'answerIsCorrect': "':ans' ist korrekt",
            'answerIsWrong': "':ans' ist falsch",
            'answeredCorrectly': 'Richtig beantwortet',
            'answeredIncorrectly': 'Falsch beantwortet',
            'solutionLabel': 'Richtige Antwort:',
            'inputLabel': 'Lücke @num von @total',
            'inputHasTipLabel': 'Tipp verfügbar',
            'tipLabel': 'Tipp',
            'behaviour': {
                'enableRetry': True,
                'enableSolutionsButton': True,
                'enableCheckButton': True,
                'caseSensitive': False,
                'showSolutionsRequiresInput': True,
                'autoCheck': False,
                'acceptSpellingErrors': True,
            },
            'media': {'disableImageZooming': False},
        },
        'subContentId': new_uuid(),
        'metadata': {
            'contentType': 'Fill in the Blanks',
            'license': 'U',
            'title': title or 'Lückentext',
        },
    }


def build_truefalse(statement, correct, feedback_correct="", feedback_wrong=""):
    """Build H5P.TrueFalse content for a single statement."""
    return {
        'library': 'H5P.TrueFalse 1.8',
        'params': {
            'question': f"<p>{statement}</p>",
            'correct': 'true' if correct else 'false',
            'behaviour': {
                'enableRetry': True,
                'enableSolutionsButton': True,
                'confirmCheckDialog': False,
                'confirmRetryDialog': False,
            },
            'l10n': {
                'trueText': 'Wahr',
                'falseText': 'Falsch',
                'score': 'Du hast @score von @total Punkten.',
                'checkAnswer': 'Überprüfen',
                'submitAnswer': 'Absenden',
                'showSolutionButton': 'Lösung anzeigen',
                'tryAgain': 'Wiederholen',
                'wrongAnswerMessage': feedback_wrong or 'Leider falsch.',
                'correctAnswerMessage': feedback_correct or 'Richtig!',
            },
            'media': {'disableImageZooming': False},
        },
        'subContentId': new_uuid(),
        'metadata': {
            'contentType': 'True/False Question',
            'license': 'U',
            'title': statement[:80],
        },
    }


def build_dragtext(text_field, title=""):
    """Build H5P.DragText content.

    text_field: text with *draggable* markers, newline-separated lines.
    """
    return {
        'library': 'H5P.DragText 1.10',
        'params': {
            'textField': text_field,
            'overallFeedback': [{'from': 0, 'to': 100}],
            'behaviour': {
                'enableRetry': True,
                'enableSolutionsButton': True,
                'enableCheckButton': True,
                'instantFeedback': False,
            },
            'checkAnswer': 'Überprüfen',
            'submitAnswer': 'Absenden',
            'tryAgain': 'Wiederholen',
            'showSolution': 'Lösung anzeigen',
            'dropZoneIndex': 'Ablagezone @index.',
            'empty': 'Ablagezone @index ist leer.',
            'contains': 'Ablagezone @index enthält @draggable.',
            'ariaDraggableIndex': '@index von @count.',
            'tipLabel': 'Tipp anzeigen',
            'correctText': 'Richtig!',
            'incorrectText': 'Falsch!',
            'resetDropTitle': 'Zurücksetzen',
            'resetDropDescription': 'Möchtest du diese Ablagezone zurücksetzen?',
            'grabbed': 'Element gegriffen.',
            'cancelledDragging': 'Ziehen abgebrochen.',
            'correctAnswer': 'Richtige Antwort:',
            'feedbackHeader': 'Feedback',
            'scoreBarLabel': 'Du hast :num von :total Punkten.',
        },
        'subContentId': new_uuid(),
        'metadata': {
            'contentType': 'Drag the Words',
            'license': 'U',
            'title': title or 'Drag the Words',
        },
    }


def build_sortparagraphs(task_description, paragraphs, title=""):
    """Build H5P.SortParagraphs content."""
    para_list = [{'text': p} for p in paragraphs]
    return {
        'library': 'H5P.SortParagraphs 0.11',
        'params': {
            'taskDescription': f'<p>{task_description}</p>',
            'paragraphs': para_list,
            'behaviour': {
                'scoring': 'all',
                'applyPenalties': True,
                'enableRetry': True,
                'enableSolutionsButton': True,
                'addButtonsForMovement': True,
                'duplicatesInterchangeable': True,
            },
            'l10n': {
                'checkAnswer': 'Überprüfen',
                'submitAnswer': 'Absenden',
                'showSolution': 'Lösung anzeigen',
                'tryAgain': 'Wiederholen',
                'up': 'Nach oben',
                'down': 'Nach unten',
                'disabled': 'Deaktiviert',
                'correctAnswer': 'Richtige Position',
                'wrongAnswer': 'Falsche Position',
                'header': 'Feedback',
            },
        },
        'subContentId': new_uuid(),
        'metadata': {
            'contentType': 'Sort the Paragraphs',
            'license': 'U',
            'title': title or 'Sortieraufgabe',
        },
    }


def build_essay(task_description, keywords, sample_solution="", title=""):
    """Build H5P.Essay content."""
    kw_list = [
        {'keyword': kw, 'alternatives': [], 'points': 1, 'forgiving': True}
        for kw in keywords
    ]

    params = {
        'taskDescription': f'<p>{task_description}</p>',
        'overallFeedback': [{'from': 0, 'to': 100}],
        'behaviour': {
            'minimumLength': 10,
            'maximumLength': 10000,
            'inputFieldSize': 10,
            'enableRetry': True,
            'ignoreScoring': False,
            'pointsHost': 1,
        },
        'checkAnswer': 'Überprüfen',
        'submitAnswer': 'Absenden',
        'tryAgain': 'Wiederholen',
        'showSolution': 'Lösung anzeigen',
    }
    if kw_list:
        params['keywords'] = kw_list
    if sample_solution:
        params['solution'] = {
            'introduction': 'Musterlösung:',
            'sample': sample_solution,
        }

    return {
        'library': 'H5P.Essay 1.5',
        'params': params,
        'subContentId': new_uuid(),
        'metadata': {
            'contentType': 'Essay',
            'license': 'U',
            'title': title or 'Freitext',
        },
    }


# ──────────────────────────────────────────────────────────────
# Exercise Parsers
# ──────────────────────────────────────────────────────────────

_ANSWER_LINE_RE = re.compile(r'^([ \t]*)-\s*\[([\sx])\]\s*(.+)$', re.MULTILINE)
_SUB_FEEDBACK_RE = re.compile(
    r'^[ \t]+-\s*\*+\s*(?:Feedback\s*:?\s*)?(.+?)\*+\s*$',
    re.IGNORECASE,
)
# Rückmeldung je Antwort: "→ Feedback: …" (auch "->") oder kursiv am Zeilenende
# "→ *…*". Die kursive Form nur mit "→" – "->" ist in PHP der Objektoperator.
_INLINE_FEEDBACK_RE = re.compile(
    r'\s*[–\-]?\s*(?:(?:→|->)\s*Feedback\s*:?\s*(.+)|→\s*\*(?!\*)(.+?)\*)\s*$',
    re.IGNORECASE,
)


def _clean_markdown_inline(s):
    """Strip lightweight markdown markers used in answer feedback."""
    s = s.strip()
    # Strip surrounding bold/italic markers
    s = re.sub(r'^\*+\s*', '', s)
    s = re.sub(r'\s*\*+$', '', s)
    return s.strip()


def _extract_mc_answers(text):
    """Extract answer options from - [x] / - [ ] lines.

    Splits per-answer feedback (inline "→ Feedback: …" or "→ *…*", or as a
    sub-bullet "  - *Feedback: …*") so it can be rendered as chosenFeedback
    and only becomes visible after the learner selects the answer.
    """
    answers = []
    matches = list(_ANSWER_LINE_RE.finditer(text))
    if not matches:
        return answers

    for i, m in enumerate(matches):
        correct = m.group(2).strip() == 'x'
        raw_text = m.group(3).strip()

        # 1) Inline feedback after "→ Feedback:" or as "→ *…*"
        inline_fb = _INLINE_FEEDBACK_RE.search(raw_text)
        feedback = ''
        if inline_fb:
            feedback = (inline_fb.group(1) or inline_fb.group(2)).strip()
            raw_text = raw_text[:inline_fb.start()].rstrip(' .–-:')

        # 2) Sub-bullet feedback in the lines following this answer (until
        #    the next answer line or blank line)
        if not feedback:
            start = m.end()
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            block = text[start:end]
            for line in block.splitlines():
                if not line.strip():
                    # Allow first blank only as separator – stop on second blank
                    continue
                sub = _SUB_FEEDBACK_RE.match(line)
                if sub:
                    feedback = _clean_markdown_inline(sub.group(1))
                    break
                # Other indented lines are part of the answer continuation
                if line.startswith((' ', '\t')) and line.lstrip().startswith('-'):
                    # Plain sub-bullet without feedback marker – stop scanning
                    break

        answers.append({
            'correct': correct,
            'text': raw_text,
            'feedback': feedback,
        })
    return answers


def parse_multichoice_exercise(text):
    """Parse H5P.MultiChoice exercise → list of question dicts."""
    title = extract_title(text)
    code_block = extract_code_block(text)
    code_html = ""
    if code_block:
        code_html = f"<pre><code>{html_escape(code_block)}</code></pre>"

    questions = []

    # Split by **Frage N:** or **Frage:**
    frage_splits = re.split(r'\*\*Frage(?:\s+\d+)?:\*\*\s*', text)

    if len(frage_splits) > 1:
        for i, section in enumerate(frage_splits[1:], 1):
            # Question text = lines before first - [ ]
            lines = section.strip().split('\n')
            q_lines = []
            for line in lines:
                if re.match(r'\s*-\s*\[', line.strip()):
                    break
                q_lines.append(line.strip())
            q_text = ' '.join(q_lines).strip()

            answers = _extract_mc_answers(section)
            feedback = ""
            fb = re.search(r'\*\*Feedback:?\*\*\s*(.+?)(?:\n\n|\n\*\*|\Z)', section, re.DOTALL)
            if fb:
                feedback = fb.group(1).strip()

            if answers:
                full_q = q_text
                if code_html:
                    full_q = f"{q_text}<br><br>{code_html}"
                q_title = f"{title} ({i})" if len(frage_splits) > 2 else title
                questions.append(build_multichoice(full_q, answers, feedback, title=q_title))
    else:
        # No explicit Frage header – try to find answers directly
        answers = _extract_mc_answers(text)
        if answers:
            # Try to find question text from **Aufgabenstellung:**
            q_text = title
            aufg = re.search(r'\*\*Aufgabenstellung:\*\*\s*(.+?)(?=\n\s*-\s*\[)', text, re.DOTALL)
            if aufg:
                q_text = aufg.group(1).strip()
            full_q = q_text
            if code_html:
                full_q = f"{q_text}<br><br>{code_html}"
            questions.append(build_multichoice(full_q, answers, title=title))

    return questions


# ──────────────────────────────────────────────────────────────
# Markdown Parsing – H5P.Blanks (Aufgabenkörper → HTML)
# ──────────────────────────────────────────────────────────────

# Ab diesen Zeilen endet der Aufgabenkörper (Auswertungs-/Hinweisblöcke).
_BLANKS_STOP_RE = re.compile(
    r'^\s*(?:\*\*(?:Feedback|Tipp|Tipps|Bewertung|Hinweis|Musterlösung|'
    r'Musterloesung|Erwartete)|---\s*$)'
)
# Metazeilen des Übungskopfes – gehören nicht zum Aufgabentext.
_BLANKS_META_RE = re.compile(r'^\s*\*\*(?:Operator|Typ|AFB):?\*\*')
# Marker, hinter denen der Aufgabentext (neu) beginnt.
_BLANKS_START_RE = re.compile(
    r'^\s*\*\*(?:Text mit Lücken|Aufgabentext|Titel):\*\*'
)
_TABLE_SEP_RE = re.compile(r'^:?-{2,}:?$')
_INLINE_CODE_RE = re.compile(r'`([^`]+)`')
_INLINE_BOLD_RE = re.compile(r'\*\*([^*]+)\*\*')


def extract_blanks_body(text):
    r"""Aufgabenkörper einer Blanks-Übung.

    Alles zwischen der ``## Übung``-Kopfzeile und dem ersten Feedback- oder
    Hinweisblock, ohne die Metazeilen (``**Operator:** …``). Steht ein
    Startmarker im Text (``**Titel:**``, ``**Aufgabentext:**``,
    ``**Text mit Lücken:**``), beginnt der Körper dahinter.

    Eingezäunte Code-Blöcke bleiben unangetastet: Ein ``---`` darin beendet den
    Körper nicht.
    """
    body = []
    code = None
    for i, line in enumerate(text.split('\n')):
        if line.lstrip().startswith('```'):
            code = line if code is None else None
            body.append(line)
            continue
        if code is not None:
            body.append(line)
            continue
        if i == 0 and line.lstrip().startswith('#'):
            continue
        if _BLANKS_STOP_RE.match(line):
            break
        if _BLANKS_START_RE.match(line):
            body = []                    # alles davor war Vorspann
            continue
        if _BLANKS_META_RE.match(line):
            continue
        body.append(line)
    return '\n'.join(body).strip()


# Platzhalter für geschützte Lücken. Steuerzeichen, die in Quiz-Markdown nicht
# vorkommen – dadurch bleibt jedes verbleibende ``*`` eindeutig ein Literal.
_BLANK_OPEN, _BLANK_CLOSE = '\x00', '\x01'
_BLANK_MARKER_RE = re.compile(r'\*\*\\\*(.+?)\\\*\*\*')


def protect_blank_markers(text):
    r"""``**\*antwort\***`` → interne Platzhalter.

    Erst dadurch lassen sich alle übrigen Sternchen als das behandeln, was sie
    sind: Literale. In Quelltext steht ``*`` für Multiplikation oder einen
    Kommentarrahmen, im Fließtext für Kursivsatz – H5P.Blanks würde daraus sonst
    Lücken machen. Aus ``rohwert * 5.0 / `` **\*1024.0\*** entstünde die Lücke
    ``5.0 / `` statt ``1024.0``.
    """
    return _BLANK_MARKER_RE.sub(
        lambda m: f'{_BLANK_OPEN}{m.group(1)}{_BLANK_CLOSE}', text)


def restore_blank_markers(text):
    """Platzhalter → H5P-Lückenform ``*antwort*``."""
    return text.replace(_BLANK_OPEN, '*').replace(_BLANK_CLOSE, '*')


def escape_blanks_text(text):
    """HTML-Escaping für Fließtext einer Blanks-Übung – **ohne** Anführungszeichen.

    In Elementinhalt müssen nur ``&``, ``<`` und ``>`` maskiert werden. Würde man
    auch ``"`` maskieren, landete die Entity in der Antwort: Aus der Lücke
    ``**\\*"temperatur"\\***`` würde die erwartete Eingabe ``&quot;temperatur&quot;``,
    die niemand tippen kann.
    """
    return html_mod.escape(text, quote=False)


def neutralize_asterisks(text):
    """Literale Sternchen als ``&#42;`` maskieren.

    Wird im Browser als ``*`` angezeigt, von der Lückensuche in H5P.Blanks aber
    nicht als Begrenzer erkannt. Geschützte Lücken (siehe
    :func:`protect_blank_markers`) sind zu diesem Zeitpunkt Platzhalter und
    bleiben unberührt.
    """
    return text.replace('*', '&#42;')


def blanks_inline_html(text):
    r"""Inline-Markdown einer Blanks-Zeile nach HTML.

    Wandelt ``code`` und ``**fett**`` um; alle danach noch verbliebenen
    Sternchen sind Literale und werden maskiert. Setzt voraus, dass die Lücken
    mit :func:`protect_blank_markers` geschützt wurden.
    """
    text = escape_blanks_text(text)
    text = _INLINE_CODE_RE.sub(
        lambda m: f'<code>{neutralize_asterisks(m.group(1))}</code>', text)
    text = _INLINE_BOLD_RE.sub(lambda m: f'<strong>{m.group(1)}</strong>', text)
    return neutralize_asterisks(text)


def _is_table_block(lines):
    return len(lines) >= 2 and all(l.lstrip().startswith('|') for l in lines)


def blanks_table_html(lines):
    """Markdown-Tabelle → HTML-Tabelle; Lücken in den Zellen bleiben erhalten."""
    rows = [_split_table_row(l) for l in lines]
    head, body = [], rows
    if len(rows) >= 2 and rows[1] and all(_TABLE_SEP_RE.match(c) for c in rows[1] if c):
        head, body = rows[0], rows[2:]

    parts = ['<table>']
    if head:
        parts.append('<thead><tr>')
        parts += [f'<th>{blanks_inline_html(c)}</th>' for c in head]
        parts.append('</tr></thead>')
    parts.append('<tbody>')
    for row in body:
        parts.append('<tr>')
        parts += [f'<td>{blanks_inline_html(c)}</td>' for c in row]
        parts.append('</tr>')
    parts.append('</tbody></table>')
    return ''.join(parts)


def blanks_body_to_html(body):
    r"""Aufgabenkörper einer Blanks-Übung als HTML.

    Absätze werden zu ``<p>`` (Zeilenumbrüche als ``<br>``), Markdown-Tabellen
    zu ``<table>``, eingezäunte Code-Blöcke zu ``<pre><code>``. Die Lückenmarker
    müssen bereits in der H5P-Form ``*antwort*`` vorliegen.
    """
    out, block, code = [], [], None

    def flush():
        lines = [l for l in block if l.strip()]
        block.clear()
        if not lines:
            return
        if _is_table_block(lines):
            out.append(blanks_table_html(lines))
        else:
            out.append('<p>' + '<br>'.join(blanks_inline_html(l) for l in lines) + '</p>')

    for line in body.split('\n'):
        if line.lstrip().startswith('```'):
            if code is None:
                flush()
                code = []
            else:
                out.append('<pre><code>'
                           + neutralize_asterisks(escape_blanks_text('\n'.join(code)))
                           + '</code></pre>')
                code = None
            continue
        if code is not None:
            code.append(line)
        elif line.strip():
            block.append(line)
        else:
            flush()
    if code is not None:
        out.append('<pre><code>'
                   + neutralize_asterisks(escape_blanks_text('\n'.join(code)))
                   + '</code></pre>')
    flush()
    return restore_blank_markers(''.join(out))


# HTML-Entities, die in einer Antwort stehen bleiben müssten, weil das Zeichen in
# HTML maskiert gehört – die Lernenden können sie nicht eingeben.
_ENTITY_IN_BLANK_RE = re.compile(r'&(?:amp|lt|gt|quot|#x27|#39|#42);')


def warn_reserved_blank_chars(questions_html, leise=False):
    """Vor Lücken warnen, deren Antwort so nicht eingebbar ist.

    Zwei Fälle, beide nur im Quiz-Markdown zu beheben:

    1. **H5P-Sonderzeichen.** ``/`` trennt Alternativantworten, ``:`` leitet
       einen Tipp ein. ``*//*`` wird dadurch zu zwei leeren Alternativen,
       ``*self::*`` zur Antwort ``self`` mit leerem Tipp. Gewollte
       Alternativen wie ``*kleiner gleich/kleiner oder gleich*`` sind kein
       Fehler – gewarnt wird bei ``/`` nur, wenn eine Alternative leer bliebe.
    2. **Zeichen, die HTML maskieren muss** (``<``, ``>``, ``&``). Sie stehen in
       der Antwort als Entity (``&lt;?php``); eingetippt wird aber ``<?php``.

    Beides ergäbe eine unlösbare Lücke. Deshalb ein Hinweis beim Erzeugen statt
    einer stillen Fehlausgabe – genau daran krankte der Lückentext-Parser zuvor.

    Gibt die beanstandeten Antworten als ``(antwort, grund)`` zurück
    (leere Liste = alles in Ordnung).
    """
    treffer = []
    for html in questions_html:
        for blank in HAS_BLANK_RE.findall(html):
            antwort = blank.strip('*')
            leere_alternative = '/' in antwort and not all(
                a.strip() for a in antwort.split('/'))
            if leere_alternative or ':' in antwort:
                treffer.append((antwort, "'/' bzw. ':' – H5P deutet das als "
                                         "Alternative bzw. Tipp"))
            elif _ENTITY_IN_BLANK_RE.search(antwort):
                treffer.append((antwort, "ein Zeichen, das HTML maskieren muss "
                                         "(<, > oder &) – so nicht eingebbar"))
    if not leise:
        for antwort, grund in treffer:
            print(f"    ⚠ Lücke {antwort!r} enthält {grund}. "
                  f"Antwort im Markdown umformulieren.")
    return treffer


def parse_blanks_exercise(text):
    """Parse H5P.Blanks exercise → list of question dicts."""
    title = extract_title(text)

    # Check for numbered Aufgabe sections
    aufgabe_sections = re.split(r'\*\*Aufgabe\s+\d+(?:\s*\([^)]*\))?:\*\*\s*', text)

    questions_html = []
    if len(aufgabe_sections) > 1:
        # Multiple Aufgabe sub-sections
        for section in aufgabe_sections[1:]:
            bq = extract_blockquote(section)
            if bq:
                bq = convert_blank_markers(bq)
                if '*' in bq:
                    html_text = bq.replace('\n', '<br>')
                    questions_html.append(f"<p>{html_text}</p>")
            else:
                # Fallback: find text with blank markers in plain paragraphs
                section_converted = convert_blank_markers(section)
                paragraphs = re.split(r'\n\s*\n', section_converted)
                for para in paragraphs:
                    para = para.strip()
                    if para and '*' in para and not para.startswith('**'):
                        html_text = para.replace('\n', '<br>')
                        questions_html.append(f"<p>{html_text}</p>")
    else:
        # Try blockquote first
        bq = extract_blockquote(text)
        if bq:
            bq = convert_blank_markers(bq)
            paragraphs = re.split(r'\n\s*\n', bq)
            for para in paragraphs:
                para = para.strip()
                if para and '*' in para:
                    html_text = para.replace('\n', '<br>')
                    questions_html.append(f"<p>{html_text}</p>")
            if not questions_html and '*' in bq:
                html_text = bq.replace('\n', '<br>')
                questions_html.append(f"<p>{html_text}</p>")

        # Fallback: den gesamten Aufgabenkörper der Übung rendern.
        #
        # Früher wurde hier ein ``**Titel:**``- bzw. ``**Aufgabentext:**``-Marker
        # vorausgesetzt; Übungen ohne einen solchen Marker lieferten still gar
        # keine Frage. Jetzt wird der Körper anhand von Kopfzeile, Metazeilen und
        # Feedback-Block abgegrenzt und als ein zusammenhängender HTML-Block
        # ausgegeben – so bleibt der Kontext (Code-Block, Tabellenkopf,
        # einleitender Satz) bei den Lücken, zu denen er gehört.
        if not questions_html:
            body = protect_blank_markers(extract_blanks_body(text))
            if _BLANK_OPEN in body:
                rendered = blanks_body_to_html(body)
                if rendered:
                    questions_html.append(rendered)

    if questions_html:
        warn_reserved_blank_chars(questions_html)
        h5p_html = [_zahl_luecken_fuer_h5p(h) for h in questions_html]
        frage = build_blanks(h5p_html, title=title)
        if h5p_html != questions_html:
            frage['_gift_questions'] = questions_html   # Toleranzen für den GIFT-Export
        return [frage]
    return []


def parse_truefalse_exercise(text):
    """Parse H5P.TrueFalse exercise → list of question dicts (one per row)."""
    title = extract_title(text)
    questions = []

    rows = extract_table_rows(text)
    # Skip header row (first row with words)
    data_rows = rows[1:] if rows else []

    for cells in data_rows:
        if len(cells) < 2:
            continue

        # Dynamically find the column containing **Wahr**/**Falsch**
        answer_idx = -1
        for i, cell in enumerate(cells):
            if re.match(r'\*\*(Wahr|Falsch)\*\*', cell.strip()):
                answer_idx = i
                break

        if answer_idx < 0:
            continue

        # Statement is the column immediately before the answer
        statement_idx = max(answer_idx - 1, 0)
        statement = cells[statement_idx].strip()
        if not statement or statement.startswith('---'):
            continue

        answer_cell = cells[answer_idx].strip()

        # Grab feedback from the next column if present
        extra_feedback = ""
        if answer_idx + 1 < len(cells):
            extra_feedback = cells[answer_idx + 1].strip()

        # Parse **Wahr** / **Falsch** and optional inline explanation
        m = re.match(r'\*\*(Wahr|Falsch)\*\*(?:\s*[–\-]\s*(.+))?', answer_cell)
        if m:
            correct = m.group(1) == 'Wahr'
            explanation = m.group(2).strip() if m.group(2) else extra_feedback
            questions.append(build_truefalse(
                statement, correct,
                feedback_correct="Richtig!",
                feedback_wrong=explanation or "Leider falsch.",
            ))

    return questions


def parse_dragtext_exercise(text):
    """Parse H5P.DragText exercise → list of question dicts."""
    title = extract_title(text)
    bq = extract_blockquote(text)
    if not bq:
        return []

    bq = convert_blank_markers(bq)
    bq = _sanitize_dragtext_body(bq)

    if '*' in bq:
        return [build_dragtext(bq, title=title)]
    return []


def _sanitize_dragtext_body(text):
    """Remove markdown emphasis around draggable markers and clean ':'.

    Keeps ``*draggable*`` markers intact, but strips ``**bold**`` runs that
    are not used as a drag marker. Stray asterisks not paired as drag
    markers are also removed.
    """
    # Strip ``**bold**`` → bold (but never touch the single * drag markers)
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    # Strip ``__bold__``
    text = re.sub(r'__(.+?)__', r'\1', text)
    return text


def parse_dragquestion_exercise(text):
    """Parse H5P.DragQuestion exercise (matching/comparison) → list of question dicts."""
    title = extract_title(text)
    rows = extract_table_rows(text)

    if len(rows) < 2:
        return []

    header = rows[0]
    data_rows = rows[1:]

    # Detect comparison table (3+ columns with ✓)
    has_checkmarks = any('✓' in ''.join(cells) for cells in data_rows)

    if len(header) > 2 and has_checkmarks:
        return _parse_comparison_table(title, header, data_rows)
    elif len(header) >= 2:
        return _parse_matching_table(title, header, data_rows)
    return []


def _strip_dragtext_markdown(s):
    """Sanitize a cell value for use in H5P DragText.

    H5P.DragText uses ``*`` to delimit draggable words and ``:`` inside a
    drag marker (``*word:tip*``) to introduce a tip. Outside drag markers
    these characters are harmless, but markdown emphasis around answer
    options would otherwise leak ``*`` into the rendered prompt.
    """
    s = s.strip()
    # Code-Spans: `int` → int. Sonst zeigte das Ziehwort die Backticks, und
    # GIFT verlangte sie als Eingabe.
    s = re.sub(r'`([^`]+)`', r'\1', s)
    # Remove markdown bold/italic markers (** … **, * … *, _ … _, __ … __)
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'__(.+?)__', r'\1', s)
    s = re.sub(r'(?<!\w)\*(.+?)\*(?!\w)', r'\1', s)
    s = re.sub(r'(?<!\w)_(.+?)_(?!\w)', r'\1', s)
    # Strip any remaining stray asterisks – they would create spurious
    # drag zones in H5P.DragText output.
    s = s.replace('*', '')
    return s.strip()


def _parse_matching_table(title, header, data_rows):
    """Convert simple 2-column matching to DragText."""
    lines = []
    # Pre-compute averages once (over original rows) so the cleaned strings
    # don't skew the side-length decision.
    avg_left = sum(len(r[0]) for r in data_rows if len(r) >= 2) / max(len(data_rows), 1)
    avg_right = sum(len(r[1]) for r in data_rows if len(r) >= 2) / max(len(data_rows), 1)

    for cells in data_rows:
        if len(cells) < 2:
            continue
        left = _strip_dragtext_markdown(cells[0])
        right = _strip_dragtext_markdown(cells[1])
        if not left or not right:
            continue

        if avg_right <= avg_left:
            # Right is shorter → make right draggable
            draggable = right.replace(':', ' –')
            lines.append(f"{left}: *{draggable}*")
        else:
            # Left is shorter → make left draggable
            draggable = left.replace(':', ' –')
            lines.append(f"{right}: *{draggable}*")

    if lines:
        return [build_dragtext('\n'.join(lines), title=title)]
    return []


def _parse_comparison_table(title, header, data_rows):
    """Convert comparison table (with ✓) to MultiChoice questions."""
    # header[0] is the property column name, header[1:] are categories
    categories = header[1:]
    questions = []

    for cells in data_rows:
        if len(cells) < 2:
            continue
        prop = cells[0].strip()
        if not prop:
            continue

        # Build MC answers from categories
        answers = []
        for i, cat in enumerate(categories):
            cell_val = cells[i + 1].strip() if i + 1 < len(cells) else ''
            correct = '✓' in cell_val
            answers.append({'correct': correct, 'text': cat.strip()})

        correct_cats = [a['text'] for a in answers if a['correct']]
        if correct_cats and answers:
            q_text = f"Welche Kategorie(n) haben die Eigenschaft: <strong>{prop}</strong>?"
            questions.append(build_multichoice(
                q_text, answers, title=f"{title} – {prop}"
            ))

    return questions


def parse_sortparagraphs_exercise(text):
    """Parse H5P.SortParagraphs exercise → list of question dicts."""
    title = extract_title(text)

    # Extract task description
    aufgabe = ""
    m = re.search(r'\*\*Aufgabenstellung:\*\*\s*(.+?)(?=\n\s*\n|\n\d+\.)', text, re.DOTALL)
    if m:
        aufgabe = m.group(1).strip()

    # Extract numbered list
    items = re.findall(r'^\d+\.\s+(.+)$', text, re.MULTILINE)

    if items:
        return [build_sortparagraphs(aufgabe, items, title=title)]
    return []


def parse_essay_exercise(text):
    """Parse H5P.Essay exercise → list of question dicts."""
    title = extract_title(text)

    # Extract task description – try multiple formats
    task_desc = ""

    # 1. Try **Aufgabentext:** or **Aufgabenstellung:** headers
    task_match = re.search(
        r'\*\*(?:Aufgabentext|Aufgabenstellung|Aufgabe):\*\*\s*\n'
        r'(.+?)(?=\n\*\*Schlüsselwörter|\n\*\*Musterlösung|\n\*\*Bewertung|\n---\s*$|\Z)',
        text, re.DOTALL
    )
    if task_match:
        task_desc = task_match.group(1).strip()

    # 2. Fallback: try blockquote
    if not task_desc:
        bq = extract_blockquote(text)
        if bq:
            task_desc = bq

    # 3. Fallback: grab body text after title, before keywords/solution
    if not task_desc:
        body_match = re.search(
            r'\*\*Titel:\*\*[^\n]*\n\s*\n(.+?)(?=\n\*\*Schlüsselwörter|\n\*\*Musterlösung|\n\*\*Bewertung|\Z)',
            text, re.DOTALL
        )
        if body_match:
            task_desc = body_match.group(1).strip()

    # Extract keywords – handle both bullet list and inline comma-separated
    keywords = []
    kw_match = re.search(
        r'\*\*Schlüsselwörter[^:]*:\*\*\s*\n((?:\s*[-*]\s+.+\n?)+)',
        text,
    )
    if kw_match:
        keywords = [kw.strip() for kw in re.findall(r'[-*]\s+(.+)', kw_match.group(1))]
    else:
        # Try inline comma-separated format
        kw_inline = re.search(r'\*\*Schlüsselwörter[^:]*:\*\*\s*(.+)', text)
        if kw_inline:
            keywords = [kw.strip() for kw in kw_inline.group(1).split(',')]

    # Extract sample solution
    sample = ""
    sol_match = re.search(r'\*\*Musterlösung[^:]*:\*\*\s*\n(.+?)(?:\n\n---|\n\n##|\n\n\*\*Bewertung|\Z)', text, re.DOTALL)
    if sol_match:
        sample = sol_match.group(1).strip()

    if task_desc:
        return [build_essay(task_desc, keywords, sample, title=title)]
    return []


def parse_questionset_exercise(text):
    """Parse H5P.QuestionSet exercise with mixed ### Frage N sub-questions."""
    title = extract_title(text)
    questions = []

    # Split by ### Frage N headers
    frage_parts = re.split(r'(?=^### Frage\s+\d+)', text, flags=re.MULTILINE)

    for part in frage_parts[1:]:  # skip preamble
        # Determine sub-question type from **Typ:** field
        typ_match = re.search(r'\*\*Typ:\*\*\s*(.+)', part)
        typ = typ_match.group(1).strip().lower() if typ_match else ""

        if 'multiple choice' in typ or 'multiple-choice' in typ:
            qs = parse_multichoice_exercise(part)
            if not qs:
                # Fallback: parse MC answers directly from this section
                answers = _extract_mc_answers(part)
                if answers:
                    # Get question text (lines before answers, after Typ line)
                    lines = part.strip().split('\n')
                    q_lines = []
                    past_typ = False
                    for line in lines:
                        if '**Typ:**' in line:
                            past_typ = True
                            continue
                        if past_typ and not re.match(r'\s*-\s*\[', line.strip()) and line.strip():
                            q_lines.append(line.strip())
                        elif re.match(r'\s*-\s*\[', line.strip()):
                            break
                    q_text = ' '.join(q_lines).strip()
                    qs = [build_multichoice(q_text, answers, title=q_text[:60])]
            questions.extend(qs)

        elif 'lückentext' in typ or 'blanks' in typ:
            bq = extract_blockquote(part)
            if bq:
                bq = convert_blank_markers(bq)
                if '*' in bq:
                    html_text = bq.replace('\n', '<br>')
                    questions.append(build_blanks(
                        [f"<p>{html_text}</p>"],
                        title=title,
                    ))

        elif 'wahr' in typ or 'falsch' in typ:
            # Extract statement and answer from text like:
            # Statement text
            # → **Falsch** – explanation
            lines = part.strip().split('\n')
            statement = ""
            correct = True
            explanation = ""
            past_typ = False
            for line in lines:
                if '**Typ:**' in line:
                    past_typ = True
                    continue
                stripped = line.strip()
                if past_typ and stripped and not stripped.startswith('→') and not stripped.startswith('**'):
                    statement = stripped
                if stripped.startswith('→'):
                    m = re.match(r'→\s*\*\*(Wahr|Falsch)\*\*(?:\s*[–\-]\s*(.+))?', stripped)
                    if m:
                        correct = m.group(1) == 'Wahr'
                        explanation = m.group(2).strip() if m.group(2) else ''
            if statement:
                questions.append(build_truefalse(
                    statement, correct,
                    feedback_wrong=explanation or 'Leider falsch.',
                ))

    return questions


def parse_singlechoiceset_exercise(text):
    """Parse H5P.SingleChoiceSet self-assessment – skip non-quiz content."""
    # Self-assessment tables (Anfänger/Sicher/Experte) cannot be meaningfully
    # converted to quiz questions. Return empty list.
    return []


# ──────────────────────────────────────────────────────────────
# Exercise Router
# ──────────────────────────────────────────────────────────────

PARSERS = {
    'H5P.MultiChoice': parse_multichoice_exercise,
    'H5P.Blanks': parse_blanks_exercise,
    'H5P.TrueFalse': parse_truefalse_exercise,
    'H5P.DragText': parse_dragtext_exercise,
    'H5P.DragQuestion': parse_dragquestion_exercise,
    'H5P.SortParagraphs': parse_sortparagraphs_exercise,
    'H5P.Essay': parse_essay_exercise,
    'H5P.QuestionSet': parse_questionset_exercise,
    'H5P.SingleChoiceSet': parse_singlechoiceset_exercise,
}


def parse_exercise(exercise_text):
    """Route exercise to appropriate parser based on H5P type."""
    header = parse_exercise_header(exercise_text)
    if not header:
        return []

    parser = PARSERS.get(header['h5p_type'])
    if parser:
        try:
            return parser(exercise_text)
        except Exception as e:
            print(f"    ⚠ Error in Übung {header['number']} ({header['h5p_type']}): {e}")
            import traceback
            traceback.print_exc()
            return []
    else:
        print(f"    ⚠ Unknown H5P type: {header['h5p_type']}")
        return []


# ──────────────────────────────────────────────────────────────
# H5P File Generation
# ──────────────────────────────────────────────────────────────

# Standard library versions used in generated H5P files
LIB_VERSIONS = {
    'H5P.MultiChoice': (1, 16),
    'H5P.Blanks': (1, 14),
    'H5P.TrueFalse': (1, 8),
    'H5P.DragText': (1, 10),
    'H5P.DragQuestion': (1, 14),
    'H5P.SortParagraphs': (0, 11),
    'H5P.Essay': (1, 5),
}


def create_h5p_json(title, questions):
    """Create h5p.json metadata."""
    used_libs = {q['library'].split(' ')[0] for q in questions}

    deps = [
        {'machineName': 'H5P.QuestionSet', 'majorVersion': 1, 'minorVersion': 20},
        {'machineName': 'FontAwesome', 'majorVersion': 4, 'minorVersion': 5},
        {'machineName': 'H5P.JoubelUI', 'majorVersion': 1, 'minorVersion': 3},
        {'machineName': 'H5P.Transition', 'majorVersion': 1, 'minorVersion': 0},
        {'machineName': 'H5P.FontIcons', 'majorVersion': 1, 'minorVersion': 0},
        {'machineName': 'H5P.Question', 'majorVersion': 1, 'minorVersion': 5},
    ]

    for lib in used_libs:
        if lib in LIB_VERSIONS:
            major, minor = LIB_VERSIONS[lib]
            deps.append({'machineName': lib, 'majorVersion': major, 'minorVersion': minor})

    return {
        'title': title,
        'language': 'de',
        'mainLibrary': 'H5P.QuestionSet',
        'embedTypes': ['div'],
        'license': 'U',
        'preloadedDependencies': deps,
    }


def create_content_json(title, questions):
    """Create content.json for a QuestionSet."""
    return {
        'introPage': {
            'showIntroPage': True,
            'startButtonText': 'Quiz starten',
            'title': title,
            'introduction': f'<p>Teste dein Wissen zum Thema: {title}</p>',
        },
        'progressType': 'dots',
        'passPercentage': 50,
        'disableBackwardsNavigation': False,
        'randomQuestions': False,
        'endGame': {
            'showResultPage': True,
            'showSolutionButton': True,
            'showRetryButton': True,
            'noResultMessage': 'Quiz beendet',
            'message': 'Dein Ergebnis:',
            'overallFeedback': [
                {'from': 0, 'to': 49, 'feedback': 'Übe weiter! Du schaffst das.'},
                {'from': 50, 'to': 79, 'feedback': 'Gut gemacht! Fast alles richtig.'},
                {'from': 80, 'to': 100, 'feedback': 'Ausgezeichnet! Sehr gut verstanden.'},
            ],
            'solutionButtonText': 'Lösung anzeigen',
            'retryButtonText': 'Wiederholen',
            'finishButtonText': 'Beenden',
            'submitButtonText': 'Absenden',
            'showAnimations': False,
            'skippable': False,
            'skipButtonText': 'Video überspringen',
        },
        'override': {
            'checkButton': True,
            'showSolutionButton': 'on',
            'retryButton': 'on',
        },
        'texts': {
            'prevButton': 'Zurück',
            'nextButton': 'Weiter',
            'finishButton': 'Beenden',
            'submitButton': 'Absenden',
            'textualProgress': 'Frage @current von @total',
            'jumpToQuestion': 'Frage %d von %total',
            'questionLabel': 'Frage',
            'readSpeakerProgress': 'Frage @current von @total',
            'unansweredText': 'Nicht beantwortet',
            'answeredText': 'Beantwortet',
            'currentQuestionText': 'Aktuelle Frage',
            'navigationLabel': 'Fragen',
        },
        # interne Schlüssel (``_…``, z. B. ``_gift_questions``) gehören nicht ins Paket
        'questions': [{k: v for k, v in q.items() if not k.startswith('_')} for q in questions],
    }


def write_h5p_file(output_path, title, questions):
    """Write the .h5p ZIP file."""
    h5p_meta = create_h5p_json(title, questions)
    content = create_content_json(title, questions)

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr(
            'h5p.json',
            json.dumps(h5p_meta, ensure_ascii=False, indent=2),
        )
        zf.writestr(
            'content/content.json',
            json.dumps(content, ensure_ascii=False, indent=2),
        )

    return output_path


# ──────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────

def process_file(md_path, output_dir, stats=None):
    """Process one markdown file → one .h5p file.

    ``stats`` ist ein optionales Dict, in dem die Zahl der erzeugten Fragen unter
    ``"questions"`` aufsummiert wird. Ohne dieses Argument müsste der Aufrufer
    die Datei ein zweites Mal parsen, nur um zu zählen – das verdoppelt die
    Arbeit und auch jede Warnung.
    """
    print(f"\n{'─'*60}")
    print(f"📄 {md_path.name}")

    content = md_path.read_text(encoding='utf-8')
    lesson_num, title, exercises = split_exercises(content)

    print(f"  Lektion {lesson_num:02d}: {title}")
    print(f"  {len(exercises)} Übungen gefunden")

    all_questions = []
    for ex_text in exercises:
        header = parse_exercise_header(ex_text)
        qs = parse_exercise(ex_text)
        all_questions.extend(qs)
        if header:
            print(f"    Übung {header['number']:2d}: {header['h5p_type']:<25s} → {len(qs)} Frage(n)")

    if not all_questions:
        print(f"  ⚠ Keine Fragen generiert!")
        return None

    print(f"  Gesamt: {len(all_questions)} Fragen")

    if stats is not None:
        stats['questions'] = stats.get('questions', 0) + len(all_questions)

    output_path = output_dir / f"{md_path.stem}.h5p"
    write_h5p_file(str(output_path), title, all_questions)
    print(f"  ✅ → {output_path.name}")

    return output_path


def main(project_dir=None):
    """Erzeugt aus ``<project_dir>/h5p/*.md`` die ``.h5p``-Dateien in
    ``<project_dir>/h5p/generated/``. Default project_dir = cwd."""
    project_dir = Path(project_dir) if project_dir is not None else Path.cwd()
    h5p_dir = project_dir / 'h5p'
    output_dir = h5p_dir / 'generated'

    output_dir.mkdir(exist_ok=True)

    md_files = sorted([
        f for f in h5p_dir.glob('*.md')
        if f.name.lower() != 'readme.md'
    ])

    if not md_files:
        print("Keine Markdown-Dateien in h5p/ gefunden.")
        sys.exit(1)

    print(f"═══ H5P-Generator ═══")
    print(f"{len(md_files)} Quiz-Dateien gefunden.\n")

    generated = []
    stats = {}
    for md_file in md_files:
        result = process_file(md_file, output_dir, stats=stats)
        if result:
            generated.append(result)
    total_questions = stats.get('questions', 0)

    print(f"\n{'═'*60}")
    print(f"✅ {len(generated)}/{len(md_files)} H5P-Dateien generiert in h5p/generated/")
    for f in generated:
        # Get file size
        size_kb = os.path.getsize(f) / 1024
        print(f"  ✓ {f.name} ({size_kb:.1f} KB)")
