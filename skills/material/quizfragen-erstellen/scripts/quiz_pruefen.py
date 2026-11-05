#!/usr/bin/env python3
"""quiz_pruefen – prüft eine Quizquelle (Markdown) vor dem Export mit edu-quiz.

Nutzt denselben Parser wie edu-quiz (mitgelieferte Kopie unter scripts/eduwerkzeuge/) und
meldet, was beim Export still verloren ginge oder im Quiz nicht funktioniert:
Übungen, deren Kopfzeile nicht erkannt wird, unbekannte Typen, Übungen ohne Frage,
Single Choice ohne oder mit nur richtigen Antworten, „[X]“ statt „[x]“, Lücken mit
Sonderzeichen, fehlende Titel und AFB, doppelte Nummern, Text nach der letzten Übung,
der an sie angehängt würde, Fragen ohne GIFT-Entsprechung, **Zeilen der Quelle, die im Export
fehlen** (z. B. Angaben vor **Frage:** oder außerhalb des Blockzitats eines Lückentexts – die
Frage wäre dann unlösbar), Formeln mit einfachem $ … $ (rendert Moodle-MathJax nicht) und
unpaarige Begrenzer \\( \\) bzw. $$. Dazu eine Übersicht je Übung, die AFB-Verteilung und die
Zahl der Formeln (ℹ).

    python3 scripts/quiz_pruefen.py 65_quiz_gurtfoerderer.md

Exitcode 1 bei Fehlern (❌). Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import contextlib
import io
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from eduwerkzeuge.h5p import core as h5p  # noqa: E402
    from eduwerkzeuge.quiz import core as quiz  # noqa: E402
except ImportError:  # pragma: no cover
    h5p = quiz = None

TYPEN_GIFT = {"H5P.MultiChoice", "H5P.TrueFalse", "H5P.Blanks", "H5P.DragText",
              "H5P.SortParagraphs", "H5P.Essay"}
TYPEN_ZUSATZ = {"H5P.DragQuestion", "H5P.QuestionSet", "H5P.SingleChoiceSet"}
HILFSANTWORT_RE = re.compile(r"\b(alle (der )?(genannten|oben)|keine der (genannten|oben)|"
                             r"alle antworten|keine antwort)\b", re.I)
EINFACHES_DOLLAR_RE = re.compile(r"(?<![$\\])\$(?![$\s])[^$\n]{1,80}(?<![$\\\s])\$(?!\$)")


def _ohne_code(text: str) -> str:
    """Text ohne Codeblöcke und Inline-Code (dort sind $ und Klammern kein TeX)."""
    text = re.sub(r"^```.*?^```", "", text, flags=re.MULTILINE | re.DOTALL)
    return re.sub(r"`[^`\n]*`", "", text)


def formelbefunde(ort: str, ue: str) -> tuple[list[tuple[str, str, str]], int]:
    """MathJax-Begrenzer einer Übung: $…$, unpaarige \\( \\) bzw. $$ → (befunde, Zahl der Formeln)."""
    t = _ohne_code(ue)
    befunde = []
    m = EINFACHES_DOLLAR_RE.search(t)
    if m:
        befunde.append(("⚠", ort, f"„{m.group(0)}“ – einfaches $ … $ rendert Moodle-MathJax nicht; \\( … \\) verwenden"))
    auf, zu, doppel = t.count("\\("), t.count("\\)"), t.count("$$")
    if auf != zu or doppel % 2:
        befunde.append(("⚠", ort, f"Formelbegrenzer unpaarig (\\( {auf}× · \\) {zu}× · $$ {doppel}×)"))
    return befunde, auf + doppel // 2 + t.count("\\[")


_LABEL_RE = re.compile(r"^\*\*[^*]{2,40}:\*\*\s*")
_OHNE_INHALT_RE = re.compile(r"^(?:##|<!--|---|\*\*(?:Titel|Operator|Typ|AFB):)")


def _sauber(text: str) -> str:
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&nbsp;", " ").replace("&#42;", "*")
    text = re.sub(r"\\\*|[*`\\]", "", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def nicht_uebernommen(ue: str, fragen: list) -> list[str]:
    """Inhaltszeilen der Übung, deren Text in keiner erzeugten Frage vorkommt."""
    import html as _html
    export = _sauber(_html.unescape(" ".join(str(f.get("params")) for f in fragen)))
    fehlend, tabellenkopf = [], True
    for zeile in ue.splitlines()[1:]:
        z = zeile.strip()
        if not z or _OHNE_INHALT_RE.match(z):
            tabellenkopf = True
            continue
        if z.startswith("|"):
            if tabellenkopf or re.fullmatch(r"[|:\-\s]+", z):   # Kopfzeile, Trennzeile
                tabellenkopf = False
                continue
            z = z.strip("|").split("|")[0]
        else:
            tabellenkopf = True
        z = re.sub(r"^(?:>\s*)+|^(?:[-*+]\s+(?:\[[ xX]\]\s*)?|\d+[.)]\s+)", "", z)
        z = _LABEL_RE.sub("", z).split("→")[0]
        kern = _sauber(z.split("*")[0] if len(z.split("*")[0].strip()) >= 8 else z)[:30].strip()
        if len(kern) >= 6 and kern not in export:
            fehlend.append(zeile.strip()[:60])
    return fehlend


def _still(funktion, *args):
    puffer = io.StringIO()
    with contextlib.redirect_stdout(puffer), contextlib.redirect_stderr(puffer):
        try:
            ergebnis = funktion(*args)
        except Exception as e:  # noqa: BLE001 – Parserfehler als Befund melden
            ergebnis = e
    return ergebnis, [z.strip() for z in puffer.getvalue().splitlines() if z.strip()]


def pruefe(text: str) -> tuple[list[tuple[str, str, str]], list[dict]]:
    """→ (befunde [(stufe, ort, text)], übersicht je Übung)."""
    befunde: list[tuple[str, str, str]] = []
    uebersicht: list[dict] = []
    if h5p is None:
        befunde.append(("❌", "Werkzeug", "mitgelieferte eduwerkzeuge fehlen (bibliothek.py sync)"))
        return befunde, uebersicht

    kopf, *_rest = re.split(r"(?=^## Übung )", text, flags=re.MULTILINE)
    if not re.search(r"^# .+?Lektion\s*\d+\s*:\s*\S", kopf, re.MULTILINE):
        befunde.append(("⚠", "Kopfzeile", "keine Zeile „# Quiz Lektion N: Titel“ – H5P-Titel wird „Quiz“"))
    for nr, zeile in enumerate(text.splitlines(), 1):
        if zeile.startswith("## ") and not zeile.startswith("## Übung "):
            befunde.append(("❌", f"Zeile {nr}", f"„{zeile[:40]}“ ist keine Übung – der Text würde an die "
                            "vorige Übung angehängt (Pflichtabschnitte gehören ins Begleitblatt)"))
        if re.match(r"^\s*-\s*\[X\]", zeile):
            befunde.append(("❌", f"Zeile {nr}", "„[X]“ wird nicht erkannt – kleines „[x]“ verwenden"))

    _, titel, uebungen = h5p.split_exercises(text)
    if not uebungen:
        befunde.append(("❌", "Datei", "keine Übung (## Übung N – … (H5P.Typ) | AFB X) gefunden"))
    nummern: Counter = Counter()
    titel_gesehen: Counter = Counter()
    formeln = 0
    for ue in uebungen:
        erste = ue.split("\n", 1)[0]
        kopfdaten = h5p.parse_exercise_header(ue)
        if not kopfdaten:
            befunde.append(("❌", erste[:50], "Kopfzeile nicht erkannt – Form: "
                            "„## Übung 3 – Beschreibung (H5P.MultiChoice) | AFB II“"))
            continue
        ort = f"Übung {kopfdaten['number']}"
        typ, afb = kopfdaten["h5p_type"], kopfdaten["afb"].strip()
        nummern[kopfdaten["number"]] += 1
        if typ not in TYPEN_GIFT | TYPEN_ZUSATZ:
            befunde.append(("❌", ort, f"unbekannter Typ {typ} – erlaubt: {', '.join(sorted(TYPEN_GIFT))}"))
            continue
        if afb not in ("I", "II", "III"):
            befunde.append(("⚠", ort, f"AFB „{afb or '–'}“ – I, II oder III angeben"))
        t = re.search(r"\*\*Titel:\*\*\s*(.+)", ue)
        if not t:
            befunde.append(("⚠", ort, "kein **Titel:** – in der Moodle-Fragensammlung heißt die Frage „Übung“"))
        else:
            titel_gesehen[t.group(1).strip()] += 1

        fragen, ausgaben = _still(h5p.parse_exercise, ue)
        if isinstance(fragen, Exception):
            befunde.append(("❌", ort, f"Parserfehler: {fragen}"))
            fragen = []
        for meldung in ausgaben:
            if "⚠" in meldung or "Error" in meldung:
                befunde.append(("⚠", ort, meldung.lstrip("⚠ ").strip()))
        if not fragen:
            befunde.append(("❌", ort, f"{typ} liefert keine Frage – Aufbau nach references/quizquelle.md prüfen"))
        _pruefe_fragen(ort, typ, ue, fragen, befunde)
        fb, n = formelbefunde(ort, ue)
        befunde += fb
        formeln += n
        if fragen:
            fehlt = nicht_uebernommen(ue, fragen)
            if fehlt:
                befunde.append(("⚠", ort, f"{len(fehlt)} Zeile(n) erscheinen nicht im Export, z. B. „{fehlt[0]}“ – "
                                "Angaben, die zum Lösen nötig sind, in **Frage:** bzw. ins Blockzitat schreiben"))
        gift = sum(1 for f in fragen if quiz.question_to_gift(f))
        if fragen and gift < len(fragen):
            befunde.append(("⚠", ort, f"{len(fragen) - gift} Frage(n) ohne GIFT-Entsprechung (nur H5P)"))
        uebersicht.append({"nr": kopfdaten["number"], "typ": typ.replace("H5P.", ""), "afb": afb or "–",
                           "fragen": len(fragen), "titel": t.group(1).strip() if t else ""})

    for n, k in sorted(nummern.items()):
        if k > 1:
            befunde.append(("⚠", f"Übung {n}", f"Nummer {k}× vergeben"))
    for tt, k in titel_gesehen.items():
        if k > 1:
            befunde.append(("⚠", "Titel", f"„{tt}“ {k}× – Titel eindeutig machen"))

    if formeln:
        befunde.append(("ℹ", "Formeln", f"{formeln} Formel(n) – MathJax-Filter im Moodle-Kurs bzw. "
                        "H5P-Bibliothek MathDisplay prüfen; GIFT mit edu-quiz ≥ 0.2.3 erzeugen"))
    afb = Counter(u["afb"] for u in uebersicht)
    gesamt = sum(afb[s] for s in ("I", "II", "III"))
    if gesamt >= 4:
        if afb["I"] / gesamt > 0.6:
            befunde.append(("⚠", "AFB", f"{afb['I']}/{gesamt} Übungen AFB I – mehr Anwenden und Beurteilen einplanen"))
        if afb["II"] + afb["III"] == 0:
            befunde.append(("⚠", "AFB", "keine Übung in AFB II oder III"))
    return befunde, uebersicht


def _pruefe_fragen(ort: str, typ: str, ue: str, fragen: list, befunde: list) -> None:
    for i, f in enumerate(fragen, 1):
        lib = (f.get("library") or "").split(" ")[0]
        p = f.get("params") or {}
        o = ort + (f" › Frage {i}" if len(fragen) > 1 else "")
        if lib == "H5P.MultiChoice":
            antworten = p.get("answers") or []
            richtig = sum(1 for a in antworten if a.get("correct"))
            if richtig == 0:
                befunde.append(("❌", o, "keine Antwort als richtig markiert (- [x])"))
            elif richtig == len(antworten):
                befunde.append(("❌", o, "alle Antworten richtig – keine Auswahlentscheidung"))
            if len(antworten) < 3 and typ == "H5P.MultiChoice":
                befunde.append(("⚠", o, f"nur {len(antworten)} Antworten – mindestens 3, besser 4"))
            for a in antworten:
                if HILFSANTWORT_RE.search(re.sub(r"<[^>]+>", "", a.get("text", ""))):
                    befunde.append(("⚠", o, "„alle/keine der genannten“ als Antwort vermeiden"))
                    break
        elif lib == "H5P.Blanks":
            luecken = sum(len(re.findall(r"\*[^*]+\*", q)) for q in p.get("questions") or [])
            if luecken == 0:
                befunde.append(("❌", o, "keine Lücke erkannt (*Antwort* bzw. **\\*Antwort\\***)"))
        elif lib == "H5P.DragText":
            if not re.search(r"\*[^*]+\*", p.get("textField", "")):
                befunde.append(("❌", o, "kein ziehbares Wort (*Wort*)"))
        elif lib == "H5P.SortParagraphs":
            if len(p.get("paragraphs") or []) < 3:
                befunde.append(("⚠", o, "weniger als 3 Schritte zum Sortieren"))
        elif lib == "H5P.Essay":
            if not (p.get("keywords") or []):
                befunde.append(("⚠", o, "keine **Schlüsselwörter:** – Rückmeldung in H5P bleibt leer"))
    if typ == "H5P.TrueFalse":
        zeilen = [z for z in ue.splitlines() if z.strip().startswith("|")]
        ohne = [z for z in zeilen[2:] if not re.search(r"\*\*(Wahr|Falsch)\*\*", z)]
        if ohne:
            befunde.append(("❌", ort, f"{len(ohne)} Tabellenzeile(n) ohne **Wahr**/**Falsch** – werden übergangen"))
        werte = Counter(m for z in zeilen for m in re.findall(r"\*\*(Wahr|Falsch)\*\*", z))
        if len(zeilen) > 4 and min(werte["Wahr"], werte["Falsch"]) == 0:
            befunde.append(("⚠", ort, "nur wahre oder nur falsche Aussagen – mischen"))


def bericht(datei: Path, befunde: list, uebersicht: list) -> str:
    zeilen = [f"# Prüfung Quizquelle: {datei.name}", "",
              "| Übung | Typ | AFB | Fragen | Titel |", "|---|---|---|---|---|"]
    zeilen += [f"| {u['nr']} | {u['typ']} | {u['afb']} | {u['fragen']} | {u['titel']} |" for u in uebersicht]
    afb = Counter(u["afb"] for u in uebersicht)
    typen = Counter(u["typ"] for u in uebersicht)
    zeilen += ["", f"Übungen: {len(uebersicht)} · Fragen: {sum(u['fragen'] for u in uebersicht)} · "
               f"AFB I/II/III: {afb['I']}/{afb['II']}/{afb['III']} · Typen: "
               + ", ".join(f"{k} {v}" for k, v in typen.most_common()), ""]
    for stufe in ("❌", "⚠", "ℹ"):
        zeilen += [f"- {s} {o}: {t}" for s, o, t in befunde if s == stufe]
    f = sum(1 for b in befunde if b[0] == "❌")
    w = sum(1 for b in befunde if b[0] == "⚠")
    zeilen += ["", f"Ergebnis: {f} Fehler, {w} Warnungen" + (" – bereit für edu-quiz" if not f else "")]
    return "\n".join(zeilen)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Quizquelle vor dem Export mit edu-quiz prüfen.")
    p.add_argument("quelle", type=Path)
    a = p.parse_args(argv)
    if not a.quelle.is_file():
        print(f"Datei nicht gefunden: {a.quelle}", file=sys.stderr)
        return 2
    befunde, uebersicht = pruefe(a.quelle.read_text(encoding="utf-8"))
    print(bericht(a.quelle, befunde, uebersicht))
    return 1 if any(b[0] == "❌" for b in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
