#!/usr/bin/env python3
"""text_lesen – Text aus Unterrichtsmaterial lesen: Markdown/Text, DOCX, ODT und PDF.

Gemeinsamer Leser für die Zählhilfen der Bibliothek (bloom_check.py, lesbarkeit.py), damit
Lehrkräfte ihre Word- und PDF-Dateien direkt prüfen können. Absätze und Tabellenzellen werden
zu eigenen Zeilen; Seitenumbrüche und Formatierung entfallen.

    from text_lesen import lies_text
    text = lies_text(Path("Arbeitsblatt.docx"))

Nur Python-Standardbibliothek; PDF über das Programm pdftotext (poppler-utils), falls vorhanden.
Gescannte PDF (nur Bild) liefern keinen Text – dann vorher OCR oder Abschrift.
"""

from __future__ import annotations

import html
import re
import subprocess
import zipfile
from pathlib import Path

ENDUNGEN = (".md", ".txt", ".docx", ".odt", ".pdf")


def _listen_markieren(xml: str) -> str:
    """Absätze mit automatischer Word-Nummerierung bzw. Aufzählung (w:numPr) beginnen mit „- “ –
    so erkennen die Zählhilfen Anforderungen wie „A) …“, deren Buchstabe nur als Nummerierung
    gespeichert ist."""
    return re.sub(r"(<w:p\b[^>]*>)(.*?)(</w:p>)",
                  lambda m: m.group(1) + (re.sub(r"(<w:t(?:\s[^>]*)?>)", r"\1- ", m.group(2), count=1)
                                          if "<w:numPr>" in m.group(2) else m.group(2)) + m.group(3),
                  xml, flags=re.S)


def _xml_zu_text(xml: str, absatz: str) -> str:
    xml = re.sub(r"<w:tab/>|<text:tab/>", "\t", xml)
    xml = re.sub(r"<w:br/>|<text:line-break/>", "\n", xml)
    xml = xml.replace("<w:noBreakHyphen/>", "-")             # geschützter Bindestrich („-P1“)
    xml = re.sub(absatz, "\n", xml)
    return html.unescape(re.sub(r"<[^>]+>", "", xml)).replace("‑", "-")


def lies_text(pfad: Path) -> str:
    """Text einer Datei; unbekannte Endungen werden als UTF-8-Text gelesen."""
    pfad = Path(pfad)
    endung = pfad.suffix.lower()
    if endung == ".docx":
        with zipfile.ZipFile(pfad) as z:
            return _xml_zu_text(_listen_markieren(z.read("word/document.xml").decode("utf-8", errors="replace")),
                                r"</w:p>")
    if endung == ".odt":
        with zipfile.ZipFile(pfad) as z:
            return _xml_zu_text(z.read("content.xml").decode("utf-8", errors="replace"), r"</text:(?:p|h)>")
    if endung == ".pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", str(pfad), "-"], capture_output=True,
                                  text=True, check=True, timeout=180).stdout.replace("‑", "-")
        except (OSError, subprocess.SubprocessError) as exc:
            raise SystemExit(f"PDF nicht lesbar ({exc}); bitte als Text oder Markdown bereitstellen.")
    return pfad.read_text(encoding="utf-8", errors="replace")
