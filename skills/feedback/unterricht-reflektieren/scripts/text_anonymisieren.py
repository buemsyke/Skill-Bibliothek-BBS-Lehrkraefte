#!/usr/bin/env python3
"""text_anonymisieren – Personenbezug aus einem Dokument entfernen (regelbasiert, lokal).

Für Unterrichtsentwürfe, Prüfungsvorschläge, Korrekturtexte oder Rückmeldungen,
BEVOR sie an eine KI gehen. Ersetzt konsistent durch Platzhalter:
[PERSON], [PERSON_2] …, [E-MAIL], [TELEFON], [DATUM], [ORT], [ADRESSE], [SCHULE].

Pässe (in dieser Reihenfolge):
1. Klassenliste (--klassenliste DATEI, ein Name pro Zeile) – höchste Priorität
2. Zusatznamen (--extra "Name1, Name2")
3. Regex-Regeln: E-Mail, Telefon, Datum, PLZ+Ort, Straße, Schulname,
   Herr/Frau + Titel + Name, Schüler-/Prüfling-Kontext + Name
4. Nachnamen-Abgleich: bekannte Nachnamen auch ohne Anrede ersetzen

Aufruf:
    python3 text_anonymisieren.py EINGABE [--ausgabe DATEI] [--klassenliste DATEI]
                                  [--extra "…"] [--zuordnung DATEI]

Ausgabe auf dem Bildschirm: NUR Anzahlen je Kategorie, nie Originale.
Die Zuordnung Original → Platzhalter wird nur mit --zuordnung geschrieben
(Rechte 600; nie an eine KI geben, nie in geteilte Ordner).

Grenzen: Regeln finden Namen nur mit Kontext (Anrede, „Schüler …", Klassenliste).
Ein Name ohne Kontext kann stehen bleiben → Ergebnis immer stichprobenartig prüfen;
Schülerdaten-Anhänge vorher entfernen.

Portiert aus „Gutachten Verfahren" (src/anonymisierung/anonymisierung.py) ohne spaCy.
Nur Python-Standardbibliothek (PDF über pdftotext, falls vorhanden).
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import zipfile
from collections import Counter
from pathlib import Path

# Buchstabenbereiche Latin + Latin-Extended (für international zusammengesetzte Klassen)
_LU = "A-Z" + chr(0xC0) + "-" + chr(0xD6) + chr(0xD8) + "-" + chr(0xDE) + chr(0x100) + "-" + chr(0x24E)
_LL = "a-z" + chr(0xDF) + "-" + chr(0xF6) + chr(0xF8) + "-" + chr(0xFE) + chr(0x101) + "-" + chr(0x24F)
_NSEG = rf"[{_LU}][{_LL}]+(?:-[{_LU}][{_LL}]+)?"

_TITEL = (r"(?:Dr\.?|Prof\.?|OStR\.?|StR\.?|StD\.?|StVD\.?|OStD\.?"
          r"|Ltd\.?\s*OStD\.?|ORR\.?|RR\.?|Dipl\.\s*\w+\.?|M\.\s*A\.?|B\.\s*A\.?)")
_ANREDE_NAME = r"(?:Herrn?|Frau)(?:[ \t]+" + _TITEL + r")?[ \t]+" + _NSEG + r"(?:[ \t]+" + _NSEG + r")?"
_SCHULTYP = (r"(?:Berufsbildende\s+Schulen?|BBS|BGS|BOS|Berufliche\s+Schule|Berufsschule|Gymnasium"
             r"|Gesamtschule|Realschule|Oberschule|Hauptschule|Grundschule|Förderschule|Berufskolleg"
             r"|Studienseminar)")
_MONATE = r"(?:Januar|Februar|März|April|Mai|Juni|Juli|August|September|Oktober|November|Dezember)"

REGELN: list[tuple[str, str]] = [
    (r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", "E-MAIL"),
    (r"(?:Tel\.?|Fax\.?|Telefon|Mobil)\.?:?\s*(?:\+49|0049|0)[\d\s/\-\.]{6,}", "TELEFON"),
    (r"(?<!\d)(?:\+49|0049)\s?\d[\d\s/\-\.]{7,}\d(?!\d)", "TELEFON"),
    (r"\b\d{1,2}\.\s*" + _MONATE + r"\s*\d{4}\b", "DATUM"),
    (r"\b\d{1,2}\.\s*\d{1,2}\.\s*\d{2,4}\b", "DATUM"),
    (r"\b\d{5}[ \t]+[A-ZÄÖÜ][a-zäöüß]+(?:[ \t\-][A-ZÄÖÜ][a-zäöüß]+)*", "ORT"),
    (_NSEG + r"(?:[ \t]+" + _NSEG + r")*(?:straße|str\.|gasse|weg|allee|ring|platz|damm|chaussee)"
     r"(?:[ \t]+\d+\s*[a-zA-Z]?)?", "ADRESSE"),
    (_SCHULTYP + r"(?:[ \t]+" + _NSEG + r"(?:[ \t]+" + _NSEG + r")*)?", "SCHULE"),
    (_ANREDE_NAME, "PERSON"),
    (r"(?<!\w)" + _TITEL + r"(?:[ \t]+" + _TITEL + r")?[ \t]+" + _NSEG + r"(?:[ \t]+" + _NSEG + r")?", "PERSON"),
    (r"(?:(?:Schüler(?:in|innen)?|Lernende[rn]?|SuS\b|Azubi[s]?|Auszubildende[rn]?"
     r"|Teilnehmer(?:in)?|Prüfling[e]?|LiV|Lehrkraft|Referendar(?:in)?)[ \t]+)"
     + _NSEG + r"(?:[ \t]+" + _NSEG + r")?", "PERSON"),
]

_TITEL_WORT = re.compile(r"^(?:Herr|Herrn|Frau|Dr\.?|Prof\.?|OStR\.?|StR\.?|StD\.?|StVD\.?|OStD\.?"
                         r"|Ltd\.?|ORR\.?|RR\.?|Dipl\.|M\.|B\.|Schüler|Schülerin|Lernende[rn]?|SuS"
                         r"|Azubis?|Auszubildende[rn]?|Teilnehmer(?:in)?|Prüflinge?|LiV|Lehrkraft"
                         r"|Referendar(?:in)?)\.?$", re.IGNORECASE)
_KEINE_NACHNAMEN = {"schule", "klasse", "gruppe", "team", "lehrkraft", "betrieb"}


def _nachname_aus(name: str) -> str:
    teile = [t for t in name.strip().split() if not _TITEL_WORT.match(t)]
    return teile[-1] if teile else name


class EntityMap:
    """Konsistente Zuordnung Original → Platzhalter (gleicher Nachname → gleicher Platzhalter)."""

    MIT_INDEX = {"PERSON", "ORT", "DATUM", "SCHULE", "ADRESSE"}

    def __init__(self) -> None:
        self.karte: dict[str, str] = {}
        self.original: dict[str, str] = {}
        self.zaehler: Counter = Counter()
        self.treffer: Counter = Counter()
        self.nachnamen: dict[str, str] = {}

    def _neu(self, kategorie: str) -> str:
        if kategorie in self.MIT_INDEX:
            self.zaehler[kategorie] += 1
            n = self.zaehler[kategorie]
            return f"[{kategorie}_{n}]" if n > 1 else f"[{kategorie}]"
        return f"[{kategorie}]"

    def platzhalter(self, original: str, kategorie: str) -> str:
        key = original.strip().lower()
        self.treffer[kategorie] += 1
        if key in self.karte:
            return self.karte[key]
        if kategorie == "PERSON":
            nn = _nachname_aus(original).lower()
            if len(nn) > 3 and nn in self.nachnamen:
                self.karte[key] = self.nachnamen[nn]
                self.original[key] = original.strip()
                return self.karte[key]
        ph = self._neu(kategorie)
        self.karte[key] = ph
        self.original[key] = original.strip()
        if kategorie == "PERSON":
            nn = _nachname_aus(original).lower()
            if len(nn) > 3 and nn not in _KEINE_NACHNAMEN:
                self.nachnamen.setdefault(nn, ph)
        return ph


def _namen_pass(text: str, emap: EntityMap, namen: list[str]) -> str:
    for name in sorted({n.strip() for n in namen if n.strip()}, key=len, reverse=True):
        if re.search(_SCHULTYP, name, re.IGNORECASE):
            kat = "SCHULE"
        else:
            kat = "PERSON"
        ph = emap.platzhalter(name, kat)
        text = re.sub(r"(?<!\w)" + re.escape(name) + r"(?!\w)", ph, text, flags=re.IGNORECASE)
        # Teile eines Personennamens (Vor-/Nachname) mit ersetzen
        if kat == "PERSON":
            for teil in name.split():
                if len(teil) > 3 and not _TITEL_WORT.match(teil):
                    text = re.sub(r"(?<!\w)" + re.escape(teil) + r"(?!\w)", ph, text)
    return text


def _regex_pass(text: str, emap: EntityMap) -> str:
    for muster, kategorie in REGELN:
        def ersetze(m: re.Match, kat: str = kategorie) -> str:
            gefunden = m.group()
            if gefunden.startswith("[") and gefunden.endswith("]"):
                return gefunden
            return emap.platzhalter(gefunden, kat)
        text = re.sub(muster, ersetze, text)
    return text


def _nachnamen_pass(text: str, emap: EntityMap) -> str:
    if not emap.nachnamen:
        return text
    muster = r"(?<!\[)\b(?:" + "|".join(re.escape(n) for n in emap.nachnamen) + r")\b"

    def ersetze(m: re.Match) -> str:
        emap.treffer["PERSON"] += 1
        return emap.nachnamen.get(m.group().lower(), m.group())
    return re.sub(muster, ersetze, text, flags=re.IGNORECASE)


def anonymisiere(text: str, klassenliste: list[str] | None = None,
                 extra: list[str] | None = None) -> tuple[str, EntityMap]:
    emap = EntityMap()
    if klassenliste:
        text = _namen_pass(text, emap, klassenliste)
    if extra:
        text = _namen_pass(text, emap, extra)
    text = _regex_pass(text, emap)
    text = _nachnamen_pass(text, emap)
    return text, emap


def lies_text(pfad: Path) -> str:
    endung = pfad.suffix.lower()
    if endung == ".pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", str(pfad), "-"], capture_output=True,
                                  text=True, check=True, timeout=120).stdout
        except (OSError, subprocess.SubprocessError) as exc:
            raise SystemExit(f"PDF nicht lesbar ({exc}).")
    if endung in {".docx", ".odt"}:
        teil = "word/document.xml" if endung == ".docx" else "content.xml"
        with zipfile.ZipFile(pfad) as z:
            xml = z.read(teil).decode("utf-8", errors="replace")
        xml = re.sub(r"</(?:w:p|text:p|text:h)>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return pfad.read_text(encoding="utf-8", errors="replace")


def _schreibe_privat(pfad: Path, inhalt: str) -> None:
    pfad.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(pfad, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(inhalt)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Personenbezug aus einem Dokument entfernen (lokal).")
    p.add_argument("eingabe", type=Path)
    p.add_argument("--ausgabe", type=Path, default=None,
                   help="Zieldatei (Default: <eingabe>__anonym.md)")
    p.add_argument("--klassenliste", type=Path, default=None, help="Datei mit einem Namen pro Zeile")
    p.add_argument("--extra", default="", help="weitere Namen/Begriffe, kommagetrennt")
    p.add_argument("--zuordnung", type=Path, default=None,
                   help="Zuordnung Original→Platzhalter privat (600) speichern – nie an eine KI")
    a = p.parse_args(argv)

    klassenliste = []
    if a.klassenliste:
        klassenliste = [z.strip() for z in a.klassenliste.read_text(encoding="utf-8").splitlines() if z.strip()]
    extra = [x.strip() for x in a.extra.split(",") if x.strip()]
    text, emap = anonymisiere(lies_text(a.eingabe), klassenliste, extra)
    ziel = a.ausgabe or a.eingabe.with_name(a.eingabe.stem + "__anonym.md")
    ziel.write_text(text, encoding="utf-8")
    if a.zuordnung:
        zeilen = ["Platzhalter;Original"] + [f"{v};{emap.original[k]}" for k, v in sorted(emap.karte.items(), key=lambda x: x[1])]
        _schreibe_privat(a.zuordnung, "\n".join(zeilen) + "\n")
    print(f"Anonymisiert → {ziel}")
    print("Ersetzungen je Kategorie: " + (", ".join(f"{k} {n}" for k, n in sorted(emap.treffer.items())) or "keine"))
    print(f"Verschiedene Platzhalter: {len(set(emap.karte.values()))}")
    print("HINWEIS: Ergebnis stichprobenartig lesen – Namen ohne Kontext können stehen bleiben.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
