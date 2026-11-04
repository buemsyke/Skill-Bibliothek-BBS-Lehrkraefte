"""eduwerkzeuge — zentrale Bibliothek für wiederkehrende Lehr-Werkzeuge.

Die Logik aller wiederverwendbaren Skripte lebt hier an *einer* Stelle.
Projekte verlinken die Bibliothek einmalig per ``pip install -e`` in ihr venv
und greifen dann entweder per Import

    from eduwerkzeuge.h5p import write_h5p_file

oder über die 15 Konsolen-Befehle ``edu-*`` darauf zu (Übersicht: KI-REFERENZ.md).

Module:
    anonymisierung  – Moodle-ZIP-Abgaben pseudonymisieren (Mapping in ~/.config, Rückführung)
    edumap          – YAML/Markdown → Edumap-JSON
    h5p             – Markdown → H5P-Quizze (.h5p)
    seiten          – Lektionen splitten / Schülerseiten erzeugen (mkdocs)
    diagramme       – ER-/UML-/Block-/Struktogramme als draw.io / SVG
    technologieschema – Anlagenbilder für Steuerungsaufgaben (Technologieschema) als SVG
    ki              – Client für OpenAI-kompatible LLM-Server (Datenschutz)
    dokumente       – Text aus PDF/DOCX/ODT; reiche PDF→Markdown
    bewertung       – Notenschlüssel (Punkte → Notenpunkte, Schlüsseltabellen)
    moodle          – Moodle-Abgaben: Ordnernamen, ZIPs, Schüler-/CSV-Listen
    klasse          – Klassenbericht: Statistik, Notenspiegel, schwächste Kriterien
    quiz            – eine Quizquelle → Moodle-GIFT und H5P
    check           – didaktischer Qualitätscheck (Bloom, Phasen, EFFEKTIV)
    linkcheck       – externe Links in Kursmaterial prüfen
    kennzeichnung   – KI-Transparenzhinweise setzen/prüfen
"""

__version__ = "0.8.0"

__all__ = ["__version__"]
