"""kennzeichnung – KI-Transparenzhinweise in Unterrichtsmaterialien.

Setzt einen idempotenten Hinweisblock ans Ende jeder Markdown-Seite und
liefert die Bausteine, mit denen ``eduwerkzeuge.seiten`` dieselben Angaben in
die generierte Schülerausgabe schreibt.

Beispiel:
    from eduwerkzeuge.kennzeichnung import lade_hinweis, setze_hinweise
    hinweis = lade_hinweis(Path("scripts/phase_config.yaml"))
    setze_hinweise(Path("."), hinweis)
"""

from .core import (
    IGNORIERTE_ORDNER,
    KI_ENDE,
    KI_START,
    STANDARD_BLOCKZITAT,
    STANDARD_QUELLEN,
    KiHinweis,
    block,
    entferne_block,
    hat_block,
    lade_hinweis,
    link_zur_erklaerung,
    sammle_dateien,
    setze_block,
    setze_hinweise,
    text_admonition,
    text_blockzitat,
)

__all__ = [
    "IGNORIERTE_ORDNER",
    "KI_ENDE",
    "KI_START",
    "STANDARD_BLOCKZITAT",
    "STANDARD_QUELLEN",
    "KiHinweis",
    "block",
    "entferne_block",
    "hat_block",
    "lade_hinweis",
    "link_zur_erklaerung",
    "sammle_dateien",
    "setze_block",
    "setze_hinweise",
    "text_admonition",
    "text_blockzitat",
]
