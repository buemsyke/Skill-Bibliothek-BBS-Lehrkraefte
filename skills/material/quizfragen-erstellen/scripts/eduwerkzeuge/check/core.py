"""Kernlogik des didaktischen Qualitätschecks (deterministisch, ohne LLM).

Alle Prüfungen arbeiten mit Wortlisten/Mustern auf Markdown-Text. Sie liefern
Hinweise („gefunden" / „nicht gefunden – manuell prüfen"), keine Urteile.
Didaktische Grundlage: skills/Referenz_Lernwirksamkeit.md (FfF/NLQ).
"""

from __future__ import annotations

import re
from typing import Any

# ---------------------------------------------------------------------------
# Bloom-Taxonomie (Anderson/Krathwohl): Verben je Stufe
# ---------------------------------------------------------------------------

BLOOM_STUFEN: dict[int, tuple[str, list[str]]] = {
    1: ("Erinnern", [
        "nennen", "aufzählen", "auflisten", "bezeichnen", "angeben",
        "wiedergeben", "aufschreiben", "zeigen", "benennen",
    ]),
    2: ("Verstehen", [
        "beschreiben", "erläutern", "erklären", "zusammenfassen",
        "interpretieren", "übersetzen", "verdeutlichen", "einordnen",
        "zuordnen", "unterscheiden sie kurz",
    ]),
    3: ("Anwenden", [
        "anwenden", "durchführen", "einsetzen", "berechnen", "implementieren",
        "ausführen", "übertragen", "demonstrieren", "lösen", "ergänzen",
    ]),
    4: ("Analysieren", [
        "analysieren", "untersuchen", "vergleichen", "unterscheiden",
        "gegenüberstellen", "gliedern", "ableiten", "prüfen", "testen",
        "identifizieren",
    ]),
    5: ("Evaluieren", [
        "beurteilen", "bewerten", "begründen", "einschätzen", "diskutieren",
        "kritisieren", "stellung nehmen", "entscheiden", "abwägen",
    ]),
    6: ("Kreieren", [
        "entwickeln", "entwerfen", "konstruieren", "konzipieren", "erstellen",
        "gestalten", "planen", "optimieren", "modellieren", "formulieren",
    ]),
}

# ---------------------------------------------------------------------------
# Phasen-Analyse: Vorwissensaktivierung, Inputlänge, Verschränkung
# ---------------------------------------------------------------------------

_VORWISSEN = [
    "vorwissen", "impuls", "hypothese", "vermutung", "brainstorming",
    "kartenabfrage", "vorkenntnisse", "erwartungsabfrage", "schätzfrage",
    "vorerfahrung", "einstiegsfrage", "aktivierung",
]
_INPUT = ["input", "vortrag", "präsentation", "lehrervortrag", "instruktion",
          "erklärvideo", "demonstration", "video"]
_ERPROBUNG = ["erprobung", "erarbeitung", "anwendung", "übung", "arbeitsphase",
              "ausführen", "erproben", "anwenden", "üben", "praxisphase",
              "arbeitsauftrag", "microteaching"]
_REFLEXION = ["reflexion", "reflektieren", "abgleich", "auswertung",
              "feedback", "besprechung", "sicherung", "metaebene"]
_TRANSFER = ["transfer", "praxisaufgabe", "praxisauftrag", "hausaufgabe",
             "umsetzung im unterricht", "rückkopplung", "ausblick"]

_MIN_RE = re.compile(r"(\d+)\s*(?:min|minuten|')", re.IGNORECASE)
_MAX_INPUT_MIN = 20

# ---------------------------------------------------------------------------
# EFFEKTIV-Kriterien (NLQ, nach Sims et al. 2023)
# ---------------------------------------------------------------------------

EFFEKTIV_KRITERIEN: dict[str, tuple[str, list[str]]] = {
    "E1": ("Evaluation vorgesehen", [
        "evaluation", "evaluieren", "befragung", "fragebogen", "erhebung",
        "wirksamkeit prüfen", "follow-up", "feedbackbogen",
    ]),
    "F1": ("Forschung als Grundlage", [
        "quelle", "studie", "forschung", "evidenz", "literatur", "lipowsky",
        "sims", "hattie", "vanier", "wissenschaft",
    ]),
    "F2": ("Formate lernwirksam", [
        "fortbildungstyp", "vanier-typ", "format", "blended", "workshop",
        "verschränkung", "erprobung",
    ]),
    "E2": ("Erfahrung nutzbar", [
        "erfahrung", "eigene praxis", "praxisbeispiel", "fall", "vorwissen",
        "mitgebracht", "austausch",
    ]),
    "K": ("Konzeptionslinien mitgedacht", [
        "schulkontext", "schulentwicklung", "curriculum", "leitbild",
        "einbettung", "schulleitung", "gesamtkonzept", "konzeptionslinie",
    ]),
    "T": ("Trainingselemente eingeplant", [
        "training", "erprobung", "übung", "simulation", "microteaching",
        "rollenspiel", "feedbackphase", "coaching",
    ]),
    "I": ("Innovationen eingebaut", [
        "innovation", "neu", "aktuell", "digital", "ki", "methode",
    ]),
    "V": ("Vielfalt gestaltet", [
        "heterogen", "differenzierung", "wahlmöglichkeit", "vielfalt",
        "unterschiedliche", "adaptiv", "niveau",
    ]),
}


def _vorkommen(text_niedrig: str, woerter: list[str]) -> list[str]:
    """Liefert die Wörter aus ``woerter``, die im Text vorkommen."""
    treffer = []
    for w in woerter:
        if re.search(r"(?<![a-zäöüß])" + re.escape(w), text_niedrig):
            treffer.append(w)
    return treffer


# ---------------------------------------------------------------------------
# Öffentliche Analysen
# ---------------------------------------------------------------------------

def bloom_analyse(text: str) -> dict[str, Any]:
    """Zählt Bloom-Verben je Stufe und bewertet die Streuung.

    Rückgabe: ``{"stufen": {1: {"name", "treffer", "anzahl"}, …},
    "gesamt", "anteil_niedrig" (Stufe 1–2), "anteil_hoch" (Stufe 4–6),
    "hinweise": [str, …]}``.
    Richtwert (Referenz_Lernwirksamkeit.md, Abschn. 3):
    höchstens 1/3 Stufe 1–2, mindestens 1/3 Stufe 4–6.
    """
    t = text.lower()
    stufen: dict[int, dict[str, Any]] = {}
    gesamt = 0
    for stufe, (name, verben) in BLOOM_STUFEN.items():
        anzahl = 0
        treffer: dict[str, int] = {}
        for verb in verben:
            n = len(re.findall(r"(?<![a-zäöüß])" + re.escape(verb), t))
            if n:
                treffer[verb] = n
                anzahl += n
        stufen[stufe] = {"name": name, "treffer": treffer, "anzahl": anzahl}
        gesamt += anzahl

    hinweise: list[str] = []
    anteil_niedrig = anteil_hoch = 0.0
    if gesamt == 0:
        hinweise.append(
            "Keine Bloom-Verben gefunden – Operatoren ergänzen oder Dokument "
            "manuell prüfen.")
    else:
        niedrig = stufen[1]["anzahl"] + stufen[2]["anzahl"]
        hoch = stufen[4]["anzahl"] + stufen[5]["anzahl"] + stufen[6]["anzahl"]
        anteil_niedrig = niedrig / gesamt
        anteil_hoch = hoch / gesamt
        if anteil_niedrig > 1 / 3:
            hinweise.append(
                f"Anteil Stufe 1–2 (Erinnern/Verstehen) ist {anteil_niedrig:.0%} "
                "(> 1/3): mehr Analyse-/Bewertungs-/Gestaltungsaufgaben einplanen.")
        if anteil_hoch < 1 / 3:
            hinweise.append(
                f"Anteil Stufe 4–6 (Analysieren/Evaluieren/Kreieren) ist nur "
                f"{anteil_hoch:.0%} (< 1/3): kognitiv aktivierende Fragen ergänzen.")
        if not hinweise:
            hinweise.append("Bloom-Streuung im Richtbereich.")
    return {
        "stufen": stufen,
        "gesamt": gesamt,
        "anteil_niedrig": round(anteil_niedrig, 3),
        "anteil_hoch": round(anteil_hoch, 3),
        "hinweise": hinweise,
    }


def phasen_analyse(text: str) -> dict[str, Any]:
    """Prüft Vorwissensaktivierung, Inputlängen und Phasen-Verschränkung.

    Rückgabe: ``{"vorwissen": {"gefunden", "treffer"},
    "phasen": {"input", "erprobung", "reflexion", "transfer"},
    "lange_inputs": [{"zeile", "minuten"}, …], "hinweise": […]}``.
    """
    t = text.lower()

    vorwissen_treffer = _vorkommen(t, _VORWISSEN)
    phasen = {
        "input": bool(_vorkommen(t, _INPUT)),
        "erprobung": bool(_vorkommen(t, _ERPROBUNG)),
        "reflexion": bool(_vorkommen(t, _REFLEXION)),
        "transfer": bool(_vorkommen(t, _TRANSFER)),
    }

    # Inputblöcke > 20 min: Zeilen mit Input-Stichwort und Minutenangabe
    lange_inputs: list[dict[str, Any]] = []
    for zeile in text.splitlines():
        z = zeile.lower()
        if any(re.search(r"(?<![a-zäöüß])" + re.escape(w), z) for w in _INPUT):
            for m in _MIN_RE.finditer(z):
                minuten = int(m.group(1))
                if minuten > _MAX_INPUT_MIN:
                    lange_inputs.append(
                        {"zeile": zeile.strip(), "minuten": minuten})

    hinweise: list[str] = []
    if vorwissen_treffer:
        hinweise.append(
            "Vorwissensaktivierung erkennbar ("
            + ", ".join(vorwissen_treffer[:4]) + ").")
    else:
        hinweise.append(
            "Keine Vorwissensaktivierung gefunden (P2) – Einstieg mit "
            "Impulsfrage/Hypothesenbildung ergänzen.")
    fehlend = [k for k, v in phasen.items() if not v]
    if fehlend:
        hinweise.append(
            "Nicht erkennbare Phase(n): " + ", ".join(fehlend)
            + " – Verschränkung Input → Erprobung → Reflexion (→ Transfer) "
              "prüfen (P3).")
    else:
        hinweise.append("Alle Phasen (Input/Erprobung/Reflexion/Transfer) erkennbar.")
    for li in lange_inputs:
        hinweise.append(
            f"Inputblock mit {li['minuten']} min (> {_MAX_INPUT_MIN} min): "
            "aufteilen und mit Erprobung verschränken (P3).")
    return {
        "vorwissen": {"gefunden": bool(vorwissen_treffer),
                      "treffer": vorwissen_treffer},
        "phasen": phasen,
        "lange_inputs": lange_inputs,
        "hinweise": hinweise,
    }


def effektiv_check(text: str) -> dict[str, Any]:
    """Prüft die acht EFFEKTIV-Kriterien (NLQ, nach Sims et al. 2023).

    Rückgabe: ``{"kriterien": {kuerzel: {"name", "gefunden", "treffer"}, …},
    "erfuellt", "gesamt", "hinweise": […]}``. „Nicht gefunden" bedeutet:
    manuell prüfen bzw. ergänzen – nicht automatisch „nicht erfüllt".
    """
    t = text.lower()
    kriterien: dict[str, dict[str, Any]] = {}
    erfuellt = 0
    for kuerzel, (name, woerter) in EFFEKTIV_KRITERIEN.items():
        treffer = _vorkommen(t, woerter)
        kriterien[kuerzel] = {
            "name": name, "gefunden": bool(treffer), "treffer": treffer}
        if treffer:
            erfuellt += 1
    hinweise = [
        f"{erfuellt}/{len(EFFEKTIV_KRITERIEN)} Kriterien im Text erkennbar."]
    for kuerzel, k in kriterien.items():
        if not k["gefunden"]:
            hinweise.append(
                f"'{k['name']}' ({kuerzel}) nicht gefunden – manuell prüfen "
                "bzw. in der Konzeption ergänzen.")
    return {
        "kriterien": kriterien,
        "erfuellt": erfuellt,
        "gesamt": len(EFFEKTIV_KRITERIEN),
        "hinweise": hinweise,
    }


# ---------------------------------------------------------------------------
# Markdown-Bericht
# ---------------------------------------------------------------------------

def bericht_markdown(titel: str,
                     bloom: dict[str, Any] | None = None,
                     phasen: dict[str, Any] | None = None,
                     effektiv: dict[str, Any] | None = None) -> str:
    """Fasst die Analysen als Markdown-Bericht zusammen."""
    teile = [f"# Didaktischer Qualitätscheck: {titel}",
             "",
             "> Deterministische Hinweise (edu-check), keine Urteile. "
             "Grundlage: skills/Referenz_Lernwirksamkeit.md."]
    if bloom is not None:
        teile += ["", "## Bloom-Streuung", "",
                  "| Stufe | Name | Treffer |", "|---|---|---|"]
        for stufe, s in bloom["stufen"].items():
            verben = ", ".join(f"{v} ({n})" for v, n in s["treffer"].items()) or "–"
            teile.append(f"| {stufe} | {s['name']} | {verben} |")
        teile += ["", *(f"- {h}" for h in bloom["hinweise"])]
    if phasen is not None:
        teile += ["", "## Phasen (Vorwissen · Input · Erprobung · Reflexion)", "",
                  *(f"- {h}" for h in phasen["hinweise"])]
    if effektiv is not None:
        teile += ["", "## EFFEKTIV-Check", "",
                  "| Kriterium | Erkennbar | Fundwörter |", "|---|---|---|"]
        for kuerzel, k in effektiv["kriterien"].items():
            ok = "ja" if k["gefunden"] else "**nein – manuell prüfen**"
            teile.append(
                f"| {k['name']} ({kuerzel}) | {ok} | "
                f"{', '.join(k['treffer']) or '–'} |")
        teile += ["", f"- {effektiv['hinweise'][0]}"]
    teile.append("")
    return "\n".join(teile)
