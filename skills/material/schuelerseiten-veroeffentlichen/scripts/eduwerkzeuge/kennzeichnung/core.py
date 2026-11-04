#!/usr/bin/env python3
"""
kennzeichnung – KI-Transparenzhinweise in Unterrichtsmaterialien setzen.

Hintergrund
-----------
Unterrichtsmaterialien, die mit KI-Unterstützung entstanden sind, werden
gekennzeichnet: VO (EU) 2024/1689 (KI-Verordnung), Art. 50 Abs. 4, sowie die
*Ethischen Leitlinien für Lehrkräfte über die Nutzung von KI und Daten beim
Lehren und Lernen* (Europäische Kommission, 2022). Der Hinweis benennt das
eingesetzte System, die redaktionell verantwortliche Person und verweist auf
eine ausführliche Transparenzerklärung.

Was dieses Modul tut
--------------------
* Es setzt einen Hinweisblock ans Ende jeder Markdown-Seite eines Projekts.
* **Idempotent** – ein vorhandener Block wird ersetzt, nicht verdoppelt.
  Erkannt wird er an den HTML-Markern ``KI-KENNZEICHNUNG:START/ENDE``.
* **Pfadbewusst** – der Link zur Transparenzerklärung wird je nach
  Verzeichnistiefe der Datei relativ berechnet.
* **Formatbewusst** – Seiten innerhalb einer MkDocs-Site erhalten eine
  Admonition (``!!! info``), Dateien außerhalb (README, CONTRIBUTING) ein
  Blockzitat, das auch auf GitHub lesbar bleibt.

Die Werte (KI-System, Verantwortliche, Stand, Quellen) stehen im Block
``ki_kennzeichnung:`` der ``scripts/phase_config.yaml`` – es gibt damit **eine**
Quelle, aus der sich sowohl dieses Modul als auch ``eduwerkzeuge.seiten``
(Schülerausgabe) bedienen.

Typischer Aufruf::

    edu-kennzeichnung                # alle Seiten aktualisieren
    edu-kennzeichnung --pruefen      # nur prüfen (Exit-Code 1 bei Lücken)
    edu-kennzeichnung --entfernen    # Hinweise wieder entfernen
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import NamedTuple

try:
    import yaml
except ImportError:  # pragma: no cover - PyYAML ist harte Abhängigkeit
    yaml = None  # type: ignore


# ========================== Marker =========================================

KI_START = "<!-- KI-KENNZEICHNUNG:START – erzeugt von eduwerkzeuge.kennzeichnung -->"
KI_ENDE = "<!-- KI-KENNZEICHNUNG:ENDE -->"

# Toleranter Erkenner: findet auch Blöcke, die eine frühere Fassung (oder ein
# projekteigenes Altskript) geschrieben hat – der Kommentartext hinter :START
# darf abweichen.
_BLOCK_RE = re.compile(
    r"\n*<!--\s*KI-KENNZEICHNUNG:START.*?<!--\s*KI-KENNZEICHNUNG:ENDE\s*-->",
    re.DOTALL,
)


# ========================== Konfiguration ==================================

#: Dateien, die üblicherweise einen Hinweis tragen sollen (Glob, projektrelativ).
STANDARD_QUELLEN: tuple[str, ...] = (
    "lessons/*/lesson.md",
    "solutions/*.md",
    "docs/*.md",
    "docs/*/*.md",
    "templates/*.md",
    "README.md",
    "CONTRIBUTING.md",
)

#: Dateien, die statt einer Admonition ein Blockzitat bekommen (GitHub-lesbar).
STANDARD_BLOCKZITAT: tuple[str, ...] = ("README.md", "CONTRIBUTING.md")

#: Verzeichnisse, die nie durchsucht werden (generierte Ausgaben, Werkzeuge).
IGNORIERTE_ORDNER: frozenset[str] = frozenset({
    ".git", ".venv", "__pycache__", "site",
    "_student_site", "_teacher_site", "generated",
})


class KiHinweis(NamedTuple):
    """Inhalt eines KI-Transparenzhinweises.

    Alle Felder kommen aus dem Block ``ki_kennzeichnung:`` der
    phase_config.yaml – siehe :func:`lade_hinweis`.
    """
    #: Redaktionell verantwortliche Person/Stelle (Pflichtangabe der Norm).
    verantwortlich: str
    #: Stand der Erklärung, z. B. "20.08.2026".
    stand: str
    #: Eingesetztes KI-System.
    ki_system: str = "Claude (Anthropic)"
    #: Projektrelativer Pfad der ausführlichen Transparenzerklärung.
    seite: str = "docs/ki-transparenz.md"
    #: Beschriftung des Navigationseintrags in der Schülerausgabe.
    nav_titel: str = "KI-Transparenz"
    #: Globs der Repository-Dateien, die einen Hinweis tragen sollen.
    quellen: tuple[str, ...] = STANDARD_QUELLEN
    #: Projektrelative Pfade, die ausgenommen bleiben.
    ausgenommen: tuple[str, ...] = ()
    #: Projektrelative Pfade, die ein Blockzitat statt einer Admonition erhalten.
    blockzitat: tuple[str, ...] = STANDARD_BLOCKZITAT


def lade_hinweis(config_path: Path) -> KiHinweis | None:
    """Liest den Block ``ki_kennzeichnung:`` einer phase_config.yaml.

    @param config_path  Pfad zur phase_config.yaml
    @return             KiHinweis, oder None wenn der Block fehlt (dann bleibt
                        die Kennzeichnung im ganzen Projekt abgeschaltet)
    """
    if yaml is None:  # pragma: no cover
        raise SystemExit("PyYAML ist nicht installiert. Bitte: pip install pyyaml")
    if not Path(config_path).is_file():
        return None
    data = yaml.safe_load(Path(config_path).read_text(encoding="utf-8")) or {}
    block = data.get("ki_kennzeichnung") or {}
    if not block:
        return None

    standard = KiHinweis(verantwortlich="", stand="")
    return KiHinweis(
        verantwortlich=str(block.get("verantwortlich", "")).strip(),
        stand=str(block.get("stand", "")).strip(),
        ki_system=str(block.get("ki_system", standard.ki_system)).strip(),
        seite=str(block.get("seite", standard.seite)).strip(),
        nav_titel=str(block.get("nav_titel", standard.nav_titel)).strip(),
        quellen=tuple(block.get("quellen", standard.quellen)),
        ausgenommen=tuple(block.get("ausgenommen", standard.ausgenommen)),
        blockzitat=tuple(block.get("blockzitat", standard.blockzitat)),
    )


# ========================== Hinweistext ====================================

def text_admonition(link: str, hinweis: KiHinweis) -> str:
    """Hinweis als MkDocs-Admonition (für Seiten innerhalb einer Site)."""
    return (
        '!!! info "KI-Transparenzhinweis"\n'
        "    Diese Seite wurde **mit Unterstützung von Künstlicher Intelligenz** "
        "erstellt und\n"
        "    anschließend von einer Lehrkraft fachlich und didaktisch geprüft und "
        "freigegeben.\n"
        "\n"
        f"    Eingesetztes KI-System: **{hinweis.ki_system}** · "
        f"Verantwortlich: **{hinweis.verantwortlich}** ·\n"
        f"    Stand: {hinweis.stand} · "
        f"[Ausführliche KI-Transparenzerklärung]({link})"
    )


def text_blockzitat(link: str, hinweis: KiHinweis) -> str:
    """Hinweis als Blockzitat (für Dateien außerhalb einer Site, z. B. README)."""
    return (
        "> **KI-Transparenzhinweis** — Dieses Dokument wurde **mit Unterstützung "
        "von\n"
        "> Künstlicher Intelligenz** erstellt und anschließend von einer Lehrkraft "
        "fachlich\n"
        "> geprüft und freigegeben.\n"
        f"> Eingesetztes KI-System: **{hinweis.ki_system}** · "
        f"Verantwortlich: **{hinweis.verantwortlich}** ·\n"
        f"> Stand: {hinweis.stand} · "
        f"[Ausführliche KI-Transparenzerklärung]({link})"
    )


def block(link: str, hinweis: KiHinweis, *, stil: str = "admonition") -> str:
    """Vollständiger, an den Markern erkennbarer Hinweisblock.

    @param link     relativer Link zur Transparenzerklärung
    @param hinweis  Inhalt des Hinweises
    @param stil     "admonition" (MkDocs) oder "blockzitat" (GitHub)
    """
    rumpf = (text_blockzitat if stil == "blockzitat" else text_admonition)(link, hinweis)
    return f"{KI_START}\n\n---\n\n{rumpf}\n\n{KI_ENDE}"


# ========================== Text-Operationen ===============================

def hat_block(text: str) -> bool:
    """Trägt der Text bereits einen Kennzeichnungsblock?"""
    return _BLOCK_RE.search(text) is not None


def entferne_block(text: str) -> str:
    """Entfernt alle Kennzeichnungsblöcke aus einem Markdown-Text.

    Wird auch von ``eduwerkzeuge.seiten`` genutzt: Der Hinweis am Ende einer
    lesson.md darf nicht als Teil des letzten Abschnitts in die Schülerausgabe
    wandern – dort setzt die Generierung einen eigenen, frisch verlinkten
    Hinweis.
    """
    return _BLOCK_RE.sub("", text).rstrip() + "\n"


def setze_block(text: str, link: str, hinweis: KiHinweis, *,
                stil: str = "admonition") -> str:
    """Ersetzt bzw. ergänzt den Hinweisblock am Ende des Textes."""
    rumpf = entferne_block(text).rstrip()
    # Endet der Text bereits mit einer Trennlinie, keine zweite erzeugen.
    while rumpf.endswith("---") and not rumpf.endswith("\\---"):
        rumpf = rumpf[:-3].rstrip()
    return rumpf + "\n\n" + block(link, hinweis, stil=stil) + "\n"


# ========================== Dateien bestimmen ==============================

def link_zur_erklaerung(pfad: Path, ziel: Path) -> str:
    """Relativer Markdown-Link von ``pfad`` zur Transparenzerklärung ``ziel``.

    Rein pfadbasiert – gilt damit gleichermaßen für die Ansicht auf GitHub und
    für Ausgaben, die die Verzeichnisstruktur erhalten (Lehrerausgabe).
    """
    return os.path.relpath(ziel, pfad.parent).replace(os.sep, "/")


def sammle_dateien(wurzel: Path, hinweis: KiHinweis) -> list[Path]:
    """Alle Markdown-Dateien des Projekts, die einen Hinweis tragen sollen."""
    wurzel = Path(wurzel)
    ausgenommen = set(hinweis.ausgenommen) | {hinweis.seite}

    ergebnis: list[Path] = []
    gesehen: set[Path] = set()
    for muster in hinweis.quellen:
        for pfad in sorted(wurzel.glob(muster)):
            if not pfad.is_file():
                continue
            if any(teil in IGNORIERTE_ORDNER for teil in pfad.parts):
                continue
            if pfad.relative_to(wurzel).as_posix() in ausgenommen:
                continue
            # docs/lessons o. Ä. können Symlinks auf dieselbe Datei sein –
            # sonst würde eine Seite zweimal bearbeitet.
            echt = pfad.resolve()
            if echt in gesehen:
                continue
            gesehen.add(echt)
            ergebnis.append(pfad)
    return ergebnis


def _stil_fuer(pfad: Path, wurzel: Path, hinweis: KiHinweis) -> str:
    relativ = pfad.relative_to(wurzel).as_posix()
    return "blockzitat" if relativ in hinweis.blockzitat else "admonition"


# ========================== Hauptprogramm ==================================

def setze_hinweise(wurzel: Path, hinweis: KiHinweis, *,
                   pruefen: bool = False,
                   entfernen: bool = False,
                   leise: bool = False) -> int:
    """Setzt, prüft oder entfernt die Hinweise im ganzen Projekt.

    @return  Exit-Code: 0 = in Ordnung, 1 = Seiten ohne Kennzeichnung (--pruefen)
             bzw. keine Seiten gefunden
    """
    wurzel = Path(wurzel).resolve()
    ziel = wurzel / hinweis.seite
    dateien = sammle_dateien(wurzel, hinweis)

    def sag(*args) -> None:
        if not leise:
            print(*args)

    if not dateien:
        sag("Keine Markdown-Seiten gefunden.")
        return 1

    sag(f"Projektwurzel:   {wurzel}")
    sag(f"Verantwortlich:  {hinweis.verantwortlich} | "
        f"KI-System: {hinweis.ki_system} | Stand: {hinweis.stand}")
    sag(f"Seiten gefunden: {len(dateien)}")
    sag("")

    if pruefen:
        fehlend = [p for p in dateien
                   if not hat_block(p.read_text(encoding="utf-8"))]
        for pfad in fehlend:
            sag(f"  FEHLT     {pfad.relative_to(wurzel)}")
        if not ziel.is_file():
            sag(f"  FEHLT     {hinweis.seite} (Transparenzerklärung)")
            return 1
        if fehlend:
            sag(f"\n{len(fehlend)} Seite(n) ohne KI-Kennzeichnung.")
            return 1
        sag("Alle Seiten sind gekennzeichnet.")
        return 0

    if entfernen:
        anzahl = 0
        for pfad in dateien:
            text = pfad.read_text(encoding="utf-8")
            if hat_block(text):
                pfad.write_text(entferne_block(text), encoding="utf-8")
                sag(f"  entfernt  {pfad.relative_to(wurzel)}")
                anzahl += 1
        sag(f"\n{anzahl} Kennzeichnung(en) entfernt.")
        return 0

    if not ziel.is_file():
        sag(f"  ⚠  {hinweis.seite} fehlt – die Hinweise verlinken ins Leere.")

    geaendert = 0
    for pfad in dateien:
        text = pfad.read_text(encoding="utf-8")
        neu = setze_block(
            text,
            link_zur_erklaerung(pfad, ziel),
            hinweis,
            stil=_stil_fuer(pfad, wurzel, hinweis),
        )
        if neu != text:
            pfad.write_text(neu, encoding="utf-8")
            sag(f"  gesetzt   {pfad.relative_to(wurzel)}")
            geaendert += 1
        else:
            sag(f"  aktuell   {pfad.relative_to(wurzel)}")
    sag(f"\n{geaendert} von {len(dateien)} Seite(n) aktualisiert.")
    return 0
