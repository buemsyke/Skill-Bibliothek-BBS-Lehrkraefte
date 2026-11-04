#!/usr/bin/env python3
"""metadaten_pruefen – Dokument-Metadaten vor der Weitergabe prüfen (ohne Zusatzpakete).

Findet personenbezogene oder verräterische Angaben, die beim Weitergeben von Material
mitreisen: Autor, letzte Bearbeitung, Firma, Kommentare, Änderungsverfolgung, Dokumenttitel.

  DOCX/XLSX/PPTX  docProps/core.xml, docProps/app.xml, Kommentare, verfolgte Änderungen
  ODT/ODS/ODP     meta.xml (Autor, Ersteller)
  PDF             pdfinfo (poppler): Author, Creator, Producer, Title, Subject, Keywords

Werte werden **nicht** ausgegeben (nur „belegt“), außer mit --zeigen – damit der Bericht
selbst keine Namen weiterträgt.

Aufruf:
    python3 metadaten_pruefen.py DATEI_ODER_ORDNER… [--zeigen] [--json]

Exit-Code: 0 = nichts Personenbezogenes, 1 = mindestens ein Feld zu bereinigen, 2 = Eingabefehler.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

OOXML = {".docx", ".xlsx", ".pptx", ".dotx", ".xltx", ".potx"}
ODF = {".odt", ".ods", ".odp"}
PDF = {".pdf"}
PERSON = {"Autor", "zuletzt bearbeitet von", "Firma", "Manager", "Ersteller (ODF)", "Autor (PDF)"}


def _name(p: Path) -> str:
    return str(p).encode("utf-8", "surrogateescape").decode("utf-8", "replace")


def _xml_feld(xml: str, tag: str) -> str:
    m = re.search(rf"<{tag}[^>]*>(.*?)</{tag}>", xml, re.S)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else ""


def felder_ooxml(pfad: Path) -> dict[str, str | int]:
    erg: dict[str, str | int] = {}
    with zipfile.ZipFile(pfad) as z:
        namen = set(z.namelist())
        lies = lambda n: z.read(n).decode("utf-8", "replace") if n in namen else ""  # noqa: E731
        core, app = lies("docProps/core.xml"), lies("docProps/app.xml")
        erg["Autor"] = _xml_feld(core, "dc:creator")
        erg["zuletzt bearbeitet von"] = _xml_feld(core, "cp:lastModifiedBy")
        erg["Titel"] = _xml_feld(core, "dc:title")
        erg["Betreff"] = _xml_feld(core, "dc:subject")
        erg["Stichwörter"] = _xml_feld(core, "cp:keywords")
        erg["Firma"] = _xml_feld(app, "Company")
        erg["Manager"] = _xml_feld(app, "Manager")
        kommentare = sum(lies(n).count("<w:comment ") for n in namen if re.search(r"comments\d*\.xml$", n))
        kommentare += sum(1 for n in namen if n.startswith("xl/comments") or n.startswith("ppt/comments"))
        erg["Kommentare"] = kommentare
        haupt = lies("word/document.xml")
        erg["Änderungen (verfolgt)"] = len(re.findall(r"<w:(?:ins|del)\b", haupt))
    return erg


def felder_odf(pfad: Path) -> dict[str, str | int]:
    with zipfile.ZipFile(pfad) as z:
        meta = z.read("meta.xml").decode("utf-8", "replace") if "meta.xml" in z.namelist() else ""
    return {"Ersteller (ODF)": _xml_feld(meta, "meta:initial-creator"),
            "zuletzt bearbeitet von": _xml_feld(meta, "dc:creator"),
            "Titel": _xml_feld(meta, "dc:title")}


def felder_pdf(pfad: Path) -> dict[str, str | int]:
    if not shutil.which("pdfinfo"):
        raise RuntimeError("pdfinfo (poppler) fehlt")
    aus = subprocess.run(["pdfinfo", str(pfad)], capture_output=True, text=True, errors="replace").stdout
    roh = dict(re.findall(r"^(\w[\w ]*?):\s*(.*)$", aus, re.M))
    return {"Autor (PDF)": roh.get("Author", "").strip(), "Titel": roh.get("Title", "").strip(),
            "Betreff": roh.get("Subject", "").strip(), "Stichwörter": roh.get("Keywords", "").strip(),
            "Erzeugt mit": " / ".join(x for x in (roh.get("Creator", "").strip(), roh.get("Producer", "").strip()) if x)}


def pruefe_datei(pfad: Path) -> dict:
    endung = pfad.suffix.lower()
    if endung in OOXML:
        felder = felder_ooxml(pfad)
    elif endung in ODF:
        felder = felder_odf(pfad)
    elif endung in PDF:
        felder = felder_pdf(pfad)
    else:
        return {}
    befunde = []
    for feld, wert in felder.items():
        if not wert:
            continue
        if feld in PERSON:
            befunde.append((feld, "⚠️", "Personenangabe – vor Weitergabe entfernen"))
        elif feld in ("Kommentare", "Änderungen (verfolgt)"):
            befunde.append((feld, "⚠️", f"{wert} vorhanden – vor Weitergabe annehmen bzw. löschen"))
        elif feld == "Titel":
            befunde.append((feld, "ℹ️", "Dokumenttitel gesetzt – passt er zum Inhalt?"))
        elif feld == "Erzeugt mit":
            befunde.append((feld, "ℹ️", "Werkzeug erkennbar"))
        else:
            befunde.append((feld, "ℹ️", "belegt"))
    return {"datei": _name(pfad), "felder": felder, "befunde": befunde}


def _maskiert(wert: str | int) -> str:
    if isinstance(wert, int):
        return str(wert)
    return "belegt" if wert else "–"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Dokument-Metadaten vor der Weitergabe prüfen.")
    ap.add_argument("pfade", nargs="+", type=Path)
    ap.add_argument("--zeigen", action="store_true", help="Werte ausgeben (nur für die eigene Prüfung)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    dateien: list[Path] = []
    for p in a.pfade:
        if p.is_dir():
            dateien += sorted(f for f in p.rglob("*") if f.suffix.lower() in OOXML | ODF | PDF)
        elif p.is_file():
            dateien.append(p)
        else:
            print(f"Fehler: nicht gefunden: {_name(p)}", file=sys.stderr)
            return 2
    ergebnisse = []
    for d in dateien:
        try:
            e = pruefe_datei(d)
        except (zipfile.BadZipFile, RuntimeError, OSError) as fehler:
            e = {"datei": _name(d), "felder": {}, "befunde": [("Datei", "🔎", str(fehler))]}
        if e:
            if not a.zeigen:
                e["felder"] = {k: _maskiert(v) for k, v in e["felder"].items()}
            ergebnisse.append(e)
    if a.json:
        print(json.dumps(ergebnisse, ensure_ascii=False, indent=2))
    else:
        print("| Datei | Feld | Status | Befund |\n|---|---|---|---|")
        for e in ergebnisse:
            name = Path(e["datei"]).name
            if not e["befunde"]:
                print(f"| {name} | – | ✅ | keine Metadaten belegt |")
            for feld, status, text in e["befunde"]:
                wert = f" („{e['felder'][feld]}“)" if a.zeigen and feld in e["felder"] else ""
                print(f"| {name} | {feld}{wert} | {status} | {text} |")
        zu_bereinigen = sum(1 for e in ergebnisse if any(s == "⚠️" for _, s, _ in e["befunde"]))
        print(f"\nDateien: {len(ergebnisse)} · zu bereinigen: {zu_bereinigen}"
              + ("" if a.zeigen else " · Werte nicht ausgegeben (--zeigen für die eigene Prüfung)"))
    return 1 if any(s == "⚠️" for e in ergebnisse for _, s, _ in e["befunde"]) else 0


if __name__ == "__main__":
    sys.exit(main())
