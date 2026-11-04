#!/usr/bin/env python3
"""zitate_pruefen – stehen die zitierten Belege wirklich im geprüften Dokument?

Ein Gutachten, ein Selbstcheck oder ein Prüfbericht darf Befunde nur mit
wörtlichen Belegen stützen. Dieses Skript sucht alle Zitate in Anführungszeichen
(mind. 15 Zeichen und 2 Wörter) im BERICHT und prüft, ob sie in der QUELLE stehen:
1. exakt (nach Normalisierung von Leerraum und Silbentrennung),
2. leerraum-tolerant,
3. unscharf (bis zu 5 Abweichungen, z. B. Bindestrich- oder Apostroph-Varianten).
Markdown-Hervorhebungen (**fett**, *kursiv*, `Code`) zählen nicht. Bei Auslassungen („…“,
„[…]“) muss jedes Teilstück in der Reihenfolge der Quelle stehen.

Der YAML-Kopf des Berichts (Skill-Vertrag: titel: "…") und Blockzitate (Zeilen mit „> “ –
Vorschläge als fertige Formulierung, Transparenzhinweis) werden übersprungen. Begriffe, die
keine Belege sind, im Bericht kursiv statt in Anführungszeichen setzen.

Aufruf:
    python3 zitate_pruefen.py BERICHT.md QUELLE.(md|txt|pdf|docx|odt) [WEITERE_QUELLE …] [--json] [--mindest 1]

Mehrere Quellen (z. B. alle Dateien einer Lernsituation oder zusätzlich der Rahmenlehrplan)
gelten zusammen: Ein Zitat ist belegt, wenn es in einer von ihnen steht.

Exit-Code 1, wenn mindestens ein Zitat nicht belegt ist oder weniger als
--mindest belegte Zitate gefunden wurden. Nur Python-Standardbibliothek
(PDF über das Programm pdftotext, falls vorhanden).

Portiert aus „Gutachten Verfahren" (src/pipeline/qualitaet.py: verifiziere_zitate,
_fuzzy_substring) – ohne KI-Teile.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import zipfile
from difflib import SequenceMatcher
from pathlib import Path

_OEFFNEND = "".join(chr(c) for c in (0x201E, 0x201C, 0x201A, 0x2018, 0x22, 0xAB))
_SCHLIESSEND = "".join(chr(c) for c in (0x201D, 0x201C, 0x2019, 0x2018, 0x201B, 0x22, 0xBB))  # inkl. deutscher Schlusszeichen
_ZITAT = re.compile(
    "[" + re.escape(_OEFFNEND) + "]"
    "([^" + re.escape(_OEFFNEND + _SCHLIESSEND) + "\n]{8,}?)"
    "[" + re.escape(_SCHLIESSEND) + "]",
)


def lies_text(pfad: Path) -> str:
    """Text aus .md/.txt, .pdf (pdftotext) oder .docx/.odt (XML)."""
    endung = pfad.suffix.lower()
    if endung == ".pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", str(pfad), "-"], capture_output=True,
                                  text=True, check=True, timeout=120).stdout
        except (OSError, subprocess.SubprocessError) as exc:
            raise SystemExit(f"PDF nicht lesbar ({exc}); bitte vorher in Text umwandeln.")
    if endung in {".docx", ".odt"}:
        teil = "word/document.xml" if endung == ".docx" else "content.xml"
        with zipfile.ZipFile(pfad) as z:
            xml = z.read(teil).decode("utf-8", errors="replace")
        xml = re.sub(r"</(?:w:p|text:p|text:h)>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return pfad.read_text(encoding="utf-8", errors="replace")


def ohne_kopf(text: str) -> str:
    """YAML-Kopf (--- … ---) und Blockzitate entfernen – sie enthalten keine Belege."""
    m = re.match(r"\A---[ \t]*\n.*?\n---[ \t]*(?:\n|\Z)", text or "", re.S)
    rumpf = text[m.end():] if m else (text or "")
    return "\n".join(z for z in rumpf.splitlines() if not z.lstrip().startswith(">"))


def normiere(s: str) -> str:
    s = s.replace("\xad", "").replace("-\n", "").replace("- ", "")
    s = re.sub(r"\*\*|__|`|(?<!\w)\*(?=\S)|(?<=\S)\*(?!\w)", "", s)   # Markdown-Hervorhebung
    return re.sub(r"\s+", " ", s).strip().lower()


AUSLASSUNG = re.compile(r"\s*(?:\[…\]|\[\.\.\.\]|…|\.\.\.)\s*")


def _gefunden(zn: str, q: str, ab: int = 0) -> int:
    """Position hinter dem Fund in q (ab Position ab) oder -1."""
    i = q.find(zn, ab)
    if i >= 0:
        return i + len(zn)
    m = re.compile(r"\s*".join(re.escape(w) for w in zn.split())).search(q, ab)
    if m:
        return m.end()
    # unscharf nur für ganze Zitate bzw. lange Teilstücke – kurze Nadeln passen sonst überall
    return len(q) if ab == 0 and len(zn) >= 15 and unscharf_enthalten(zn, q) else -1


def belegt_in(z: str, q: str) -> bool:
    """Zitat mit Auslassung („…“, „[…]“): jedes Teilstück in der Reihenfolge der Quelle."""
    teile = [normiere(t) for t in AUSLASSUNG.split(z)]
    teile = [t.strip(" ,;:") for t in teile if len(t.strip(" ,;:")) >= 4]
    if len(teile) <= 1:
        return _gefunden(normiere(AUSLASSUNG.sub(" ", z)), q) >= 0
    ab = 0
    for t in teile:
        ab = _gefunden(t, q, ab)
        if ab < 0:
            return False
    return True


def extrahiere_zitate(text: str) -> list[str]:
    return [m.group(1).strip() for m in _ZITAT.finditer(text or "")]


def unscharf_enthalten(nadel: str, heuhaufen: str, max_abw: int = 5) -> bool:
    n = len(nadel)
    if n == 0 or n > len(heuhaufen) + max_abw:
        return False
    woerter = nadel.split(" ")
    # Vorfilter: mindestens die Hälfte der Wörter muss in der Quelle vorkommen
    if sum(w in heuhaufen for w in woerter) < len(woerter) / 2:
        return False
    schwelle = 1.0 - (max_abw / n)
    # Anker: die drei seltensten Wortbestandteile (≥ 3 Buchstaben/Ziffern, ohne Satzzeichen), die
    # wörtlich in der Quelle stehen – statt jede Position zu prüfen; einer davon steht fast immer
    # auch an der Fundstelle („P_erforderlich“ findet „P_(erforderlich)“ über „erforderlich“)
    kandidaten = sorted({w for w in re.findall(r"[^\W_]{3,}", nadel) if w in heuhaufen}, key=heuhaufen.count)[:3]
    if not kandidaten:                     # kein Ankerwort: vollständige Suche nur bei kleiner Quelle
        if len(heuhaufen) > 100_000:
            return False
        for pos in range(0, max(1, len(heuhaufen) - n + 1), 2):
            for breite in (n, n - max_abw, n + max_abw):
                fenster = heuhaufen[pos:pos + breite] if breite > 0 else ""
                if fenster and SequenceMatcher(a=nadel, b=fenster).ratio() >= schwelle:
                    return True
        return False
    for anker in kandidaten:
        offset, start = nadel.find(anker), 0
        while (i := heuhaufen.find(anker, start)) >= 0:
            pos = max(0, i - offset)
            for breite in (n, n - max_abw, n + max_abw):
                for q in (pos - max_abw, pos, pos + max_abw):
                    fenster = heuhaufen[max(0, q):max(0, q) + breite] if breite > 0 else ""
                    if fenster and SequenceMatcher(a=nadel, b=fenster).ratio() >= schwelle:
                        return True
            start = i + 1
    return False


def pruefe(bericht: str, quelle: str, mindest_zeichen: int = 15,
           mindest_woerter: int = 2) -> dict:
    q = normiere(quelle)
    belegt, nicht_belegt, zu_kurz = [], [], []
    for z in extrahiere_zitate(ohne_kopf(bericht)):
        zn = normiere(z)
        if len(zn) < mindest_zeichen or len(zn.split()) < mindest_woerter:
            zu_kurz.append(z)
            continue
        if belegt_in(z, q):
            belegt.append(z)
        else:
            nicht_belegt.append(z)
    return {"belegt": belegt, "nicht_belegt": nicht_belegt, "zu_kurz": zu_kurz}


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Zitate eines Berichts gegen die Quelle prüfen.")
    p.add_argument("bericht", type=Path)
    p.add_argument("quelle", type=Path, nargs="+", help="eine oder mehrere Quellen")
    p.add_argument("--mindest", type=int, default=1, help="mindestens so viele belegte Zitate")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    erg = pruefe(lies_text(a.bericht), "\n\n".join(lies_text(q) for q in a.quelle))
    ok = not erg["nicht_belegt"] and len(erg["belegt"]) >= a.mindest
    if a.json:
        print(json.dumps({**erg, "ok": ok}, ensure_ascii=False, indent=2))
    else:
        print(f"Zitate belegt: {len(erg['belegt'])} · nicht belegt: {len(erg['nicht_belegt'])} · "
              f"zu kurz (kein Beleg): {len(erg['zu_kurz'])}")
        for z in erg["nicht_belegt"]:
            print(f"  ❌ nicht in der Quelle: „{z[:120]}“")
        if len(erg["belegt"]) < a.mindest:
            print(f"  ⚠️ weniger als {a.mindest} belegte Zitate")
        print("Ergebnis: " + ("✅ alle Belege gefunden" if ok else "⚠️ Belege nachbessern oder Befund abschwächen"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
