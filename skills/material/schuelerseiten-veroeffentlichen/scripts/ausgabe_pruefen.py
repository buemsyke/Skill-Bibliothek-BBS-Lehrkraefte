#!/usr/bin/env python3
"""ausgabe_pruefen – prüft eine Schülerausgabe, bevor sie veröffentlicht wird.

Sucht in einem Ausgabeordner (z. B. _student_site/docs oder _schuelerfassung) nach allem,
was nicht zu Lernenden gehört: Lösungen und Lösungsdiagramme, Erwartungshorizonte,
didaktische Hinweise, Bewertungskriterien, vertrauliche Dateien, Planungsakte und
Prüfberichte, offene Annahmen und Prüfaufträge der Bibliothek, Kontaktdaten – und prüft,
ob jede Seite den KI-Transparenzhinweis trägt.

Mit --projekt zusätzlich die Quelle eines Kursprojekts (lessons/NN_slug/lesson.md und
scripts/phase_config.yaml): fehlender site:-Block, solutions in copy_dirs, Überschriften,
die keiner Phase zugeordnet sind und still aus der Ausgabe fallen, Lösungsdiagramme in
lessons/*/diagrams/.

    python3 scripts/ausgabe_pruefen.py _student_site/docs --projekt .
    python3 scripts/ausgabe_pruefen.py _schuelerfassung

Exitcode 1 bei Fehlern (❌). Gibt Dateinamen und Zeilen aus, keine Inhalte von Lösungen.
Nur Python-Standardbibliothek; PyYAML für --projekt.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

# auch nummeriert („## 4. Organisation im Unterricht“) und mit den Lehrerabschnitten der
# Bibliotheks-Artefakte (Differenzierung, sprachsensible Fassung)
LEHRER_UEBERSCHRIFT = re.compile(
    r"^#{1,4}\s+(?:\d+[.)]\s*)?(Didaktische Hinweise|Lösungen?\b|Lösung und|Erwartungshorizont|Bewertungskriterien|"
    r"Musterlösung|Lehrerhandreichung|Hinweise für (die )?Lehrkr|Lehrerfassung|Qualitätscheck|"
    r"Annahmen und Prüfaufträge|Übergabe\s*$|Änderungsprotokoll|Organisation im Unterricht|"
    r"Lesbarkeit vorher)", re.I)       # Bewertungshinweis bleibt sichtbar: Kriterien werden offengelegt
LEHRER_DATEI = re.compile(
    r"(^|[_/])(solutions?|loesung(en)?|lösung(en)?|musterloesung|erwartungshorizont|begleitblatt|"
    r"planungsakte|abschlussbericht|pruefbericht|gutachten|lehrer|teacher|(lehrer)?handreichung)([_./-]|$)", re.I)
BIBLIOTHEK_DATEI = re.compile(r"^(00|70|80|90|99)_")          # Akte, Klausur, Gutachten, Prüfbericht, Bericht
LOESUNGSDIAGRAMM = re.compile(r"^\d+[a-z]?_l\d+_", re.I)        # Projektkonvention NN_lXX_*
OFFEN = re.compile(r"⚠️?\s*Annahme:|🔎\s*Prüfen|\[🔎|\bTODO\b|\[ABBILDUNG:")
MAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
MAIL_OK = re.compile(r"@(?:[\w-]+\.)*(?:example\.(?:com|org|net|de)|beispiel\.de)$", re.I)   # RFC 2606, auch Subdomains
TELEFON = re.compile(r"(\+49|\b0)\d{2,5}[ /-]?\d{3,}")
KI_MARKER = re.compile(r"KI-KENNZEICHNUNG:START|KI-gestützt erstellt|mit Unterstützung von Künstlicher Intelligenz", re.I)
TEXT_ENDUNGEN = {".md", ".html", ".txt"}


def pruefe_ausgabe(wurzel: Path, ki_pflicht: bool = True) -> list[tuple[str, str, str]]:
    befunde: list[tuple[str, str, str]] = []
    dateien = sorted(p for p in wurzel.rglob("*") if p.is_file() and "site" not in p.relative_to(wurzel).parts[:1])
    if not dateien:
        return [("❌", str(wurzel), "keine Dateien gefunden")]
    for d in dateien:
        rel = d.relative_to(wurzel).as_posix()
        if LEHRER_DATEI.search(rel) and d.name != "ki-transparenz.md":
            befunde.append(("❌", rel, "Datei/Ordner für Lehrkräfte (Lösung, Erwartungshorizont, Akte, Bericht …)"))
        elif BIBLIOTHEK_DATEI.match(d.name):
            befunde.append(("❌", rel, "Planungsakte, Klassenarbeit, Gutachten oder Bericht der Bibliothek"))
        if LOESUNGSDIAGRAMM.match(d.name):
            befunde.append(("❌", rel, "Lösungsdiagramm (NN_lXX_…) – gehört nach solutions/diagrams/"))
        if d.suffix.lower() not in TEXT_ENDUNGEN:
            continue
        text = d.read_text(encoding="utf-8", errors="replace")
        kopf = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if kopf and re.search(r"^vertraulich:\s*true", kopf.group(1), re.M):
            befunde.append(("❌", rel, "vertraulich: true im Kopf"))
        if kopf and re.search(r"^status:.*KI-Entwurf", kopf.group(1), re.M):
            befunde.append(("⚠", rel, "status „KI-Entwurf“ – ist die Lehrerfassung geprüft und freigegeben?"))
        im_code = False
        for nr, zeile in enumerate(text.splitlines(), 1):
            if zeile.lstrip().startswith("```"):
                im_code = not im_code
            if im_code:
                continue
            m = LEHRER_UEBERSCHRIFT.match(zeile)
            if m:
                befunde.append(("❌", f"{rel}:{nr}", f"Abschnitt „{m.group(1).strip()}“ für Lehrkräfte"))
            # `TODO 1` als Inline-Code ist eine Markierung im Startcode für Lernende, kein offener Platzhalter
            if OFFEN.search(re.sub(r"`[^`]*`", "", zeile)):
                befunde.append(("❌", f"{rel}:{nr}", "offene Annahme, Prüfauftrag oder Platzhalter"))
            for mm in MAIL.finditer(zeile):
                if not MAIL_OK.search(mm.group(0)):
                    befunde.append(("⚠", f"{rel}:{nr}", "E-Mail-Adresse – Personenbezug prüfen"))
            if TELEFON.search(zeile) and not re.search(r"\d{4}-\d{2}-\d{2}|\d+[.,]\d+", zeile):
                befunde.append(("⚠", f"{rel}:{nr}", "Telefonnummer? – Personenbezug prüfen"))
        if d.name == "index.md" and re.search(r"Musterlösung", text, re.I):
            befunde.append(("❌", rel, "Startseite verlinkt Musterlösungen (site.link_solutions)"))
        if ki_pflicht and d.suffix == ".md" and d.name != "ki-transparenz.md" and not KI_MARKER.search(text):
            befunde.append(("⚠", rel, "kein KI-Transparenzhinweis (Skill ki-kennzeichnung)"))
    return befunde


def pruefe_projekt(projekt: Path) -> list[tuple[str, str, str]]:
    befunde: list[tuple[str, str, str]] = []
    cfg_pfad = projekt / "scripts" / "phase_config.yaml"
    if not cfg_pfad.is_file():
        return [("⚠", "scripts/phase_config.yaml", "fehlt – edu-seiten nutzt die mitgelieferte Standard-"
                 "Konfiguration (Titel „BINFQ2 Datenbanken“, Lösungen werden mitkopiert)")]
    if yaml is None:
        return [("❌", "PyYAML", "fehlt – Projektprüfung nicht möglich (pip install pyyaml)")]
    cfg = yaml.safe_load(cfg_pfad.read_text(encoding="utf-8")) or {}
    site = cfg.get("site")
    if not site:
        befunde.append(("❌", "phase_config.yaml", "kein site:-Block – Ausgabe heißt „BINFQ2 Datenbanken“ und "
                        "solutions/ wird veröffentlicht"))
    else:
        if "solutions" in (site.get("copy_dirs") or ["h5p", "solutions", "examples"]):
            befunde.append(("❌", "phase_config.yaml", "site.copy_dirs enthält solutions – Musterlösungen würden "
                            "veröffentlicht"))
        if site.get("link_solutions", True):
            befunde.append(("⚠", "phase_config.yaml", "site.link_solutions nicht auf false"))
    if not cfg.get("ki_kennzeichnung"):
        befunde.append(("⚠", "phase_config.yaml", "kein ki_kennzeichnung:-Block – Ausgabe ohne KI-Hinweis"))
    zugeordnet = {s for ph in cfg.get("phases") or [] for s in ph.get("sections") or []}
    ausgeschlossen = set(cfg.get("excluded_sections") or [])
    ausgeschl_lekt = [str(x) for x in cfg.get("excluded_lessons") or []]
    for lesson in sorted((projekt / "lessons").glob("*/lesson.md")):
        ordner = lesson.parent.name
        if any(ordner.startswith(x) for x in ausgeschl_lekt):
            continue
        im_code = False
        for nr, zeile in enumerate(lesson.read_text(encoding="utf-8").splitlines(), 1):
            if zeile.lstrip().startswith("```"):
                im_code = not im_code
            m = re.match(r"^# (.+?)\s*$", zeile)
            if m and not im_code and m.group(1) not in zugeordnet | ausgeschlossen:
                befunde.append(("⚠", f"lessons/{ordner}/lesson.md:{nr}", f"„# {m.group(1)}“ ist keiner Phase "
                                "zugeordnet – fällt still aus der Schülerausgabe"))
        for dg in sorted((lesson.parent / "diagrams").glob("*")):
            if LOESUNGSDIAGRAMM.match(dg.name):
                befunde.append(("❌", f"lessons/{ordner}/diagrams/{dg.name}", "Lösungsdiagramm im Lektionsordner "
                                "wird mitveröffentlicht – nach solutions/diagrams/"))
    return befunde


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Schülerausgabe vor dem Veröffentlichen prüfen.")
    p.add_argument("ausgabe", type=Path, help="Ausgabeordner (z. B. _student_site/docs)")
    p.add_argument("--projekt", type=Path, default=None, help="Kursprojekt mit lessons/ und scripts/phase_config.yaml")
    p.add_argument("--ohne-ki-hinweis", action="store_true", help="KI-Hinweis nicht verlangen")
    a = p.parse_args(argv)
    if not a.ausgabe.is_dir():
        print(f"Ordner nicht gefunden: {a.ausgabe}", file=sys.stderr)
        return 2
    befunde = pruefe_ausgabe(a.ausgabe, not a.ohne_ki_hinweis)
    if a.projekt:
        befunde = pruefe_projekt(a.projekt) + befunde
    seiten = sum(1 for _ in a.ausgabe.rglob("*.md"))
    print(f"# Prüfung Schülerausgabe: {a.ausgabe}\n\nSeiten: {seiten}\n")
    for stufe in ("❌", "⚠"):
        for s, o, t in befunde:
            if s == stufe:
                print(f"- {s} {o}: {t}")
    f = sum(1 for b in befunde if b[0] == "❌")
    w = sum(1 for b in befunde if b[0] == "⚠")
    print(f"\nErgebnis: {f} Fehler, {w} Warnungen" + (" – keine Lehrerinhalte gefunden" if not f else ""))
    return 1 if f else 0


if __name__ == "__main__":
    sys.exit(main())
