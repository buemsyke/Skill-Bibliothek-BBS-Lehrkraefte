"""check – didaktischer Qualitätscheck (FfF-Prinzipien, deterministisch).

Prüft Markdown-Dokumente (Fortbildungskonzeptionen, Verlaufspläne,
Quizquellen, Klausuren) auf Hinweise zu lernwirksamen Merkmalen:

- ``bloom_analyse``    – Streuung der Operatoren/Verben über die Bloom-Stufen
- ``phasen_analyse``   – Vorwissensaktivierung, Inputlänge, Verschränkung
                         Input → Erprobung → Reflexion
- ``effektiv_check``   – acht EFFEKTIV-Kriterien (NLQ, nach Sims et al. 2023)

Die Ergebnisse sind **Hinweise, keine Urteile**: „nicht gefunden" heißt
„manuell prüfen". Grundlage: ``skills/Referenz_Lernwirksamkeit.md``.

Beispiel:
    from eduwerkzeuge.check import bloom_analyse, phasen_analyse, effektiv_check
"""

from .core import (
    BLOOM_STUFEN,
    EFFEKTIV_KRITERIEN,
    bericht_markdown,
    bloom_analyse,
    effektiv_check,
    phasen_analyse,
)

__all__ = [
    "BLOOM_STUFEN",
    "EFFEKTIV_KRITERIEN",
    "bericht_markdown",
    "bloom_analyse",
    "effektiv_check",
    "phasen_analyse",
]
