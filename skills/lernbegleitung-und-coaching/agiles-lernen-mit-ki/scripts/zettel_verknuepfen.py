#!/usr/bin/env python3
"""zettel_verknuepfen – Zettelkasten für eine Lernumgebung (Markdown-Zettel mit Verweisen).

Nach dem Vorbild von append_path.sh (Röttger, heise Developer 2026), mit drei Änderungen:
relative statt absoluter Pfade (Host und VM sehen dieselben Verweise), Begleitnotizen für
Fremdformate werden automatisch angelegt, und es gibt eine Prüfung und eine Nachbarschaftsliste.

Befehle:
    verknuepfen VON NACH      hängt an NACH unter „## Verweise" die Zeile
                              „- Verweis: [VON-Name](relativer/Pfad)" an. Ist NACH kein Text
                              (PDF, XML, DOCX …), nimmt dessen Begleitnotiz NACH_zettel.md den
                              Verweis auf (wird bei Bedarf angelegt). --beidseitig: auch zurück.
    begleitnotizen ORDNER     legt für jede Fremdformat-Datei ohne Begleitnotiz eine an.
    naechste NOTIZ [-n 3]     listet die n nächsten über Verweise erreichbaren Zettel
                              (Breitensuche) – damit die KI nur diese liest.
    pruefen ORDNER            tote Verweise (❌), absolute Pfade, Fremdformate ohne Begleitnotiz,
                              Zettel ohne Verbindung (⚠).

Welche Zettel zusammengehören, entscheidet der Mensch; das Skript stellt nur die technische
Verknüpfung her. Exit 0 = ok, 1 = ❌ gefunden, 2 = Eingabefehler. Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from collections import deque
from pathlib import Path

TEXT = {".md", ".txt", ".markdown"}
IGNORIEREN = {".git", "__pycache__", ".claude", "node_modules"}
VERWEIS = re.compile(r"^\s*[-*]\s*Verweis:\s*\[[^\]]*\]\(([^)]+)\)", re.MULTILINE)
UEBERSCHRIFT = "## Verweise"


class Eingabefehler(Exception):
    pass


def ist_text(p: Path) -> bool:
    return p.suffix.lower() in TEXT


def begleitnotiz(p: Path) -> Path:
    return p.with_name(f"{p.stem}_zettel.md")


def ist_begleitnotiz(p: Path) -> bool:
    return p.name.endswith("_zettel.md")


def lege_begleitnotiz_an(datei: Path) -> tuple[Path, bool]:
    notiz = begleitnotiz(datei)
    if notiz.exists():
        return notiz, False
    notiz.write_text(f"# Zettel zu {datei.name}\n\n"
                     f"Datei: [{datei.name}]({datei.name})\n\n"
                     "Kernaussagen in eigenen Worten (mit Seite):\n- \n\n"
                     f"{UEBERSCHRIFT}\n", encoding="utf-8")
    return notiz, True


def verweise(notiz: Path) -> list[str]:
    try:
        return VERWEIS.findall(notiz.read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return []


def ziel_von(notiz: Path, verweis: str) -> Path:
    return Path(verweis) if os.path.isabs(verweis) else (notiz.parent / verweis)


def verknuepfen(von: Path, nach: Path) -> tuple[Path, str]:
    """Hängt an NACH (bzw. dessen Begleitnotiz) einen Verweis auf VON an. → (Datei, Meldung)."""
    for p in (von, nach):
        if not p.exists():
            raise Eingabefehler(f"Datei nicht gefunden: {p}")
    if von.resolve() == nach.resolve():
        raise Eingabefehler("VON und NACH sind dieselbe Datei")
    notiz = nach
    hinweis = ""
    if not ist_text(nach):
        notiz, neu = lege_begleitnotiz_an(nach)
        hinweis = f" (Begleitnotiz {'angelegt' if neu else 'genutzt'})"
    rel = os.path.relpath(von.resolve(), notiz.resolve().parent).replace(os.sep, "/")
    text = notiz.read_text(encoding="utf-8")
    if any(ziel_von(notiz, v).resolve() == von.resolve() for v in verweise(notiz)):
        return notiz, f"schon verknüpft: {notiz} → {rel}"
    if UEBERSCHRIFT not in text:
        text = text.rstrip("\n") + f"\n\n{UEBERSCHRIFT}\n"
    text = text.rstrip("\n") + f"\n- Verweis: [{von.stem}]({rel})\n"
    notiz.write_text(text, encoding="utf-8")
    return notiz, f"verknüpft: {notiz} → {rel}{hinweis}"


def dateien(ordner: Path) -> list[Path]:
    return sorted(p for p in ordner.rglob("*")
                  if p.is_file() and not any(t in IGNORIEREN or t.startswith(".") for t in p.relative_to(ordner).parts))


def begleitnotizen(ordner: Path) -> list[Path]:
    neu = []
    for p in dateien(ordner):
        if not ist_text(p):
            notiz, angelegt = lege_begleitnotiz_an(p)
            if angelegt:
                neu.append(notiz)
    return neu


def naechste(start: Path, n: int = 3) -> list[Path]:
    if not start.exists():
        raise Eingabefehler(f"Datei nicht gefunden: {start}")
    if not ist_text(start):
        start = begleitnotiz(start)
    gesehen = {start.resolve()}
    ergebnis: list[Path] = []
    schlange = deque([start])
    while schlange and len(ergebnis) < n:
        aktuell = schlange.popleft()
        for v in verweise(aktuell):
            ziel = ziel_von(aktuell, v)
            if not ist_text(ziel) and begleitnotiz(ziel).exists():
                ziel = begleitnotiz(ziel)
            if not ziel.exists() or ziel.resolve() in gesehen:
                continue
            gesehen.add(ziel.resolve())
            ergebnis.append(ziel)
            schlange.append(ziel)
            if len(ergebnis) >= n:
                break
    return ergebnis


def pruefen(ordner: Path) -> list[tuple[str, str]]:
    befunde: list[tuple[str, str]] = []
    alle = dateien(ordner)
    notizen = [p for p in alle if ist_text(p)]
    eingehend: dict[Path, int] = {p.resolve(): 0 for p in notizen}
    for notiz in notizen:
        rel_notiz = notiz.relative_to(ordner)
        for v in verweise(notiz):
            if os.path.isabs(v):
                befunde.append(("⚠", f"{rel_notiz}: absoluter Pfad „{v}“ – relativ verknüpfen, sonst bricht er zwischen Host und VM"))
            ziel = ziel_von(notiz, v)
            if not ziel.exists():
                befunde.append(("❌", f"{rel_notiz}: Verweis ins Leere „{v}“"))
                continue
            if ziel.resolve() in eingehend:
                eingehend[ziel.resolve()] += 1
    for p in alle:
        if not ist_text(p) and not begleitnotiz(p).exists():
            befunde.append(("⚠", f"{p.relative_to(ordner)}: Fremdformat ohne Begleitnotiz ({begleitnotiz(p).name})"))
    for notiz in notizen:
        if ist_begleitnotiz(notiz) or notiz.name.upper() in ("CLAUDE.MD", "README.MD") or notiz.name.startswith("93_"):
            continue
        if not verweise(notiz) and eingehend[notiz.resolve()] == 0:
            befunde.append(("⚠", f"{notiz.relative_to(ordner)}: Zettel ohne Verbindung – mit einem passenden Zettel verknüpfen"))
    return befunde


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Zettel einer Lernumgebung verknüpfen und prüfen.")
    sub = p.add_subparsers(dest="befehl", required=True)
    v = sub.add_parser("verknuepfen", help="Verweis auf VON an NACH anhängen")
    v.add_argument("von", type=Path)
    v.add_argument("nach", type=Path)
    v.add_argument("--beidseitig", action="store_true", help="auch NACH in VON verknüpfen")
    b = sub.add_parser("begleitnotizen", help="Begleitnotizen für Fremdformate anlegen")
    b.add_argument("ordner", type=Path)
    n = sub.add_parser("naechste", help="die n nächsten verknüpften Zettel")
    n.add_argument("notiz", type=Path)
    n.add_argument("-n", type=int, default=3)
    q = sub.add_parser("pruefen", help="Verweise und Begleitnotizen prüfen")
    q.add_argument("ordner", type=Path)
    a = p.parse_args(argv)
    try:
        if a.befehl == "verknuepfen":
            _, meldung = verknuepfen(a.von, a.nach)
            print(meldung)
            if a.beidseitig:
                _, meldung = verknuepfen(a.nach, a.von)
                print(meldung)
            return 0
        if a.befehl in ("begleitnotizen", "pruefen") and not a.ordner.is_dir():
            raise Eingabefehler(f"Ordner nicht gefunden: {a.ordner}")
        if a.befehl == "begleitnotizen":
            neu = begleitnotizen(a.ordner)
            for notiz in neu:
                print(f"angelegt: {notiz}")
            print(f"{len(neu)} Begleitnotiz(en) angelegt")
            return 0
        if a.befehl == "naechste":
            for z in naechste(a.notiz, a.n):
                print(z)
            return 0
        befunde = pruefen(a.ordner)
        for stufe, meldung in befunde:
            print(f"{stufe} {meldung}")
        fehler = sum(s == "❌" for s, _ in befunde)
        print(f"pruefen: {fehler} ❌ · {len(befunde) - fehler} ⚠")
        return 1 if fehler else 0
    except (Eingabefehler, OSError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
