#!/usr/bin/env python3
"""bloom_check – Zählhilfe: Operatoren in Aufgaben den Bloom-Stufen zuordnen.

Liest Markdown/Text sowie DOCX, ODT und PDF (über text_lesen.py im selben Ordner), erkennt
Aufgabenzeilen (Aufzählung, Nummerierung, Tabellenzeile oder Sie-Imperativ) und ordnet jeder
Zeile den ERSTEN gefundenen Operator zu. Ergebnis: Tabelle je Aufgabe + Verteilung über die
Stufen 1–6 + Hinweise.

Nicht gezählt werden Passiv- und Partizipformen („Bewertet wird …“, „… sind begründet“ –
typisch für Bewertungsraster und Hinweiskästen). Gemeldet, aber nicht eingeordnet werden
Arbeitsaufträge ohne Operator der Liste (z. B. „Notieren Sie …“, W-Fragen). Geschlossene
Formate („Kreuzen Sie … an“) werden gekennzeichnet: „Beurteilen Sie die Aussagen“ beim
Ankreuzen ist meist Wiedererkennen, nicht Bewerten.

Das ist eine Heuristik: Sie zählt Verben, nicht Denkleistung. Ob „Beurteilen Sie …"
wirklich ein Urteil verlangt, entscheidet die Lehrkraft bzw. der Skill bloom-taxonomie.

Anforderungen in Nominalform („A) Entwicklung eines Technologieschemas …“, „Ermittlung des
Wirkungsgrades“) – typisch für Lastenhefte in Projekt-Lernsituationen – werden über die
zugehörigen Verben eingeordnet und als „Nominalform“ gekennzeichnet.

Aufruf:
    python3 bloom_check.py arbeitsblatt.md [weitere.md …] [--ziele] [--alle] [--json]

    --ziele  auch Kompetenz- und Zielformulierungen zählen („bestimmen den Wirkungsgrad …“,
             „Die Schülerinnen und Schüler analysieren …“, „Sie entwickeln …“)
    --alle   jede Zeile mit Operator zählen, nicht nur erkannte Aufgabenzeilen (ohne Titel,
             Kurzzeilen und Kopffelder)
    --json   maschinenlesbare Ausgabe

Nur Python-Standardbibliothek. Exit-Code 0 immer (Werkzeug, kein Gate).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from text_lesen import lies_text          # DOCX/ODT/PDF (text_lesen.py aus _gemeinsam)
except ImportError:  # pragma: no cover – ohne Hilfsmodul nur Markdown/Text
    def lies_text(pfad: Path) -> str:
        return Path(pfad).read_text(encoding="utf-8", errors="replace")

STUFEN = {
    1: "Erinnern",
    2: "Verstehen",
    3: "Anwenden",
    4: "Analysieren",
    5: "Bewerten",
    6: "Erschaffen",
}

# AFB je Operator laut references/operatoren-afb.md (nicht aus der Stufe abgeleitet).
AFB_I = {"nennen", "angeben", "aufzählen", "auflisten", "bezeichnen", "benennen",
         "wiedergeben", "beschreiben", "darstellen", "zusammenfassen", "skizzieren"}
AFB_III = {"prüfen", "überprüfen", "beurteilen", "bewerten", "begründen", "Stellung nehmen",
           "erörtern", "diskutieren", "reflektieren", "einschätzen", "entscheiden", "abwägen",
           "kritisieren", "entwickeln", "entwerfen", "konzipieren", "gestalten", "optimieren",
           "planen", "konstruieren"}


def afb(operator: str) -> str:
    return "I" if operator in AFB_I else "III" if operator in AFB_III else "II"

# Infinitive je Stufe; trennbare Verben als "partikel+basis" (z. B. "zu+ordnen").
# Abgestimmt mit references/operatoren-afb.md.
OPERATOREN: dict[int, list[str]] = {
    1: ["nennen", "an+geben", "auf+zählen", "auf+listen", "bezeichnen", "benennen",
        "wieder+geben"],
    2: ["beschreiben", "dar+stellen", "zusammen+fassen", "skizzieren", "erklären",
        "erläutern", "zu+ordnen", "ein+ordnen", "interpretieren", "veranschaulichen"],
    3: ["an+wenden", "berechnen", "bestimmen", "ermitteln", "erstellen", "an+fertigen",
        "durch+führen", "aus+wählen", "implementieren", "programmieren", "zeichnen",
        "messen", "montieren", "ein+stellen", "aus+füllen", "dimensionieren", "simulieren",
        "um+setzen", "ein+binden",
        # berufspraktische Operatoren (references/operatoren-afb.md)
        "dokumentieren", "protokollieren", "formulieren", "verfassen", "präsentieren", "berichtigen"],
    4: ["aus+werten", "analysieren", "untersuchen", "vergleichen", "gegenüber+stellen",
        "heraus+arbeiten", "ab+leiten", "modellieren", "unterscheiden", "gliedern",
        "identifizieren"],
    5: ["prüfen", "überprüfen", "beurteilen", "bewerten", "begründen", "Stellung+nehmen",
        "erörtern", "diskutieren", "reflektieren", "ein+schätzen", "entscheiden",
        "ab+wägen", "kritisieren"],
    6: ["entwickeln", "entwerfen", "konzipieren", "gestalten", "optimieren", "planen",
        "konstruieren"],
}

UNREGELMAESSIG = {  # Basis -> zusätzliche Formen (Präsens/Imperativ)
    "geben": ["gibt", "gib"],
    "messen": ["misst", "miss"],
    "nehmen": ["nimmt", "nimm"],
    "entwerfen": ["entwirft", "entwirf"],
    "beschreiben": [],
    "entscheiden": [],
}

LISTE_RE = re.compile(r"^\s*(?:(?:\d+[.)]|[a-z][.)]|[A-H]\)|[-*+•–])\s+|\|)")  # Marker + Leerzeichen; Tabellenzeile

# Nominalformen in Anforderungen (Lastenheft) → Operator
NOMINAL = {
    "Entwicklung": "entwickeln", "Entwurf": "entwerfen", "Konzeption": "konzipieren",
    "Konstruktion": "konstruieren", "Gestaltung": "gestalten", "Optimierung": "optimieren",
    "Planung": "planen", "Bewertung": "bewerten", "Beurteilung": "beurteilen",
    "Überprüfung": "überprüfen", "Prüfung": "prüfen", "Analyse": "analysieren",
    "Untersuchung": "untersuchen", "Vergleich": "vergleichen", "Auswertung": "auswerten",
    "Ermittlung": "ermitteln", "Berechnung": "berechnen", "Bestimmung": "bestimmen",
    "Erstellung": "erstellen", "Auswahl": "auswählen", "Dimensionierung": "dimensionieren",
    "Simulation": "simulieren", "Umsetzung": "umsetzen", "Einbindung": "einbinden",
    "Durchführung": "durchführen", "Dokumentation": "dokumentieren", "Präsentation": "präsentieren",
    "Erläuterung": "erläutern", "Beschreibung": "beschreiben", "Darstellung": "darstellen",
    "Veranschaulichung": "veranschaulichen",
}
# nur direkt nach einem Aufzählungszeichen („A) Entwicklung …“, „1. Ermittlung …“) – Überschriften wie
# „Bewertung der Dokumentation“ oder Inhaltsverzeichnisse zählen nicht
NOMINAL_RE = re.compile(r"^\s*(?:[A-H]\)|\d+[.)]|[-*•–])\s*(?:\w+e[nrs]?\s+)?(" + "|".join(NOMINAL)
                        + r")\b(?!.*PAGEREF)")              # ein Adjektiv davor erlaubt („Sichere Einbindung …“)
ZIEL_RE = re.compile(r"^\s*(?:[-*•–]\s*)?(?:(?:Die\s+Schülerinnen\s+und\s+Schüler|Sie)\s+)?([a-zäöü]\w+)\b")
NICHT_BEOBACHTBAR_RE = re.compile(r"\b(?:Bereitschaft|verstehen|kennen|wissen|bewusst|Fähigkeit\w*\s+verbessern|"
                                  r"Reflexionsfähigkeit)\b", re.IGNORECASE)
KOPFFELD_RE = re.compile(r"^\s*(?:Erstellt\s+am|Autor|Version|Dateiname|Seitenzahl|Stand)\b", re.IGNORECASE)
SIE_RE = re.compile(r"\b\w*(?:en|ern|eln)\s+Sie\b", re.IGNORECASE)  # Sie-Imperativ
AUFGABE_RE = re.compile(r"^\s*\**\s*(?:Aufgabe|Auftrag|Arbeitsauftrag)\b", re.IGNORECASE)


def _formen(verb: str) -> str:
    """Regex-Alternativen der finiten Formen eines Verbs (ohne Partikel)."""
    if verb.endswith(("ern", "eln")):
        stamm = verb[:-1]
        formen = [verb, stamm + "e", stamm + "t", stamm + "st"]
    elif verb.endswith("en"):
        stamm = verb[:-2]
        formen = [verb, stamm + "e", stamm + "t", stamm + "st", stamm + "et"]
        if stamm.endswith(("d", "t")):
            formen.append(stamm + "est")
    else:
        formen = [verb]
    formen += UNREGELMAESSIG.get(verb, [])
    return "|".join(sorted(set(formen), key=len, reverse=True))


SONDERMUSTER = {  # feste Wendungen, deren Partikel nicht am Satzende steht
    "Stellung+nehmen": r"\b(?:nehmen|nimm|nimmt)\s+(?:Sie\s+)?Stellung\b|\bStellung\s+(?:zu\s+\w+\s+)?nehmen\b",
}


def _muster(eintrag: str) -> re.Pattern[str]:
    if eintrag in SONDERMUSTER:
        return re.compile(SONDERMUSTER[eintrag], re.IGNORECASE)
    if "+" in eintrag:
        partikel, basis = eintrag.split("+")
        zusammen = _formen(partikel + basis)
        getrennt = (rf"(?:{_formen(basis)})\b[^.!?\n]*?\b{partikel}\b"
                    rf"(?=\s*(?:[.!?:;,()]|$|und\b|oder\b))")   # auch „Stellen Sie … dar (Info).“
        return re.compile(rf"(?<![\wäöüß])(?:(?:{zusammen})\b|{getrennt})", re.IGNORECASE)
    return re.compile(rf"(?<![\wäöüß])(?:{_formen(eintrag)})\b", re.IGNORECASE)


MUSTER: list[tuple[int, str, re.Pattern[str]]] = [
    (stufe, eintrag.replace("Stellung+", "Stellung ").replace("+", ""), _muster(eintrag))
    for stufe, eintraege in OPERATOREN.items()
    for eintrag in eintraege
]


PASSIV_RE = re.compile(r"\b(?:wird|werden|wurde|wurden|worden|ist|sind)\b", re.IGNORECASE)
W_FRAGE_RE = re.compile(r"(?:^|[.:]\s+|\)\s*)(?:Was|Wie|Warum|Wieso|Weshalb|Welche[rsnm]?|Wo|Woran|Wann)\b[^?\n]{3,}\?")
GESCHLOSSEN_RE = re.compile(r"\bKreuzen\s+Sie\b|\bWählen\s+Sie\s+(?:eine|alle)\b|\bOrdnen\s+Sie\s+jede\b|"
                            r"„?richtig“?\s+oder\s+„?falsch", re.IGNORECASE)


def _erster_operator(zeile: str) -> list[tuple[int, int, str]]:
    """Erster Operator der Zeile; Passiv-/Partizipformen ohne Sie-Imperativ zählen nicht."""
    funde = []
    passiv = bool(PASSIV_RE.search(zeile)) and not SIE_RE.search(zeile)
    for stufe, operator, muster in MUSTER:
        for m in muster.finditer(zeile):
            if passiv and m.group(0).lower().endswith("t"):
                continue                    # „Bewertet wird …“, „… sind begründet“
            funde.append((m.start(), stufe, operator))
            break
    return funde


def ist_aufgabenzeile(zeile: str) -> bool:
    return bool(LISTE_RE.match(zeile) or SIE_RE.search(zeile) or AUFGABE_RE.match(zeile))


VERB_ZU_EINTRAG = {op: (stufe, op) for stufe, op, _ in MUSTER}


def ist_ziel(zeile: str) -> bool:
    """Kompetenzformulierung in der 3. Person Plural: beginnt mit einem Operator der Liste."""
    m = ZIEL_RE.match(zeile)
    return bool(m and len(zeile.split()) >= 3 and any(muster.match(m.group(1)) for _, _, muster in MUSTER))


def ist_rauschen(zeile: str) -> bool:
    """Titel, Kurzzeilen und Kopffelder – bei --alle nicht zählen."""
    s = zeile.strip()
    woerter = s.split()
    if len(woerter) < 3 or KOPFFELD_RE.match(s):
        return True
    # Titel: endet auf einen Infinitiv ohne Satzzeichen („ING3.1 Wasserstoffanlage … entwickeln“)
    return not re.search(r"[.!?:;]$", s) and not SIE_RE.search(s) and not LISTE_RE.match(s) \
        and not ZIEL_RE.match(s) is None and woerter[-1].lower() in {op for _, op, _ in MUSTER} \
        and not ist_ziel(s)


# Meta-Abschnitte der Bibliothek (Skill-Vertrag, Lernsituations-Vorlage): keine Aufgaben, keine Ziele.
# Exakter Vergleich der Überschrift – „Übergabe an die Schichtleitung“ (Aufgabe) bleibt gezählt.
META_ABSCHNITTE = {"rahmen", "lernsituation", "distanzunterricht", "analysebogen", "analysebogen – selbstcheck",
                   "phasencheck", "phasencheck (ergänzung der bibliothek, kein kriterium der leitlinie)",
                   "qualitätscheck", "annahmen und prüfaufträge", "übergabe", "änderungsliste",
                   "änderungsliste (modus b)", "änderungsprotokoll", "lesbarkeit"}
KOMPETENZRASTER_RE = re.compile(r"^kompetenzraster\b", re.IGNORECASE)


def ist_meta_ueberschrift(zeile: str) -> bool | None:
    """True/False für Überschriften (Meta-Abschnitt ja/nein), None für andere Zeilen."""
    m = re.match(r"^#{1,6}\s+(.*?)\s*$", zeile)
    if not m:
        return None
    titel = m.group(1).strip().strip("*").lower()
    return titel in META_ABSCHNITTE or bool(KOMPETENZRASTER_RE.match(titel))


def analysiere(text: str, quelle: str, alle: bool = False, ziele: bool = False) -> list[dict]:
    treffer: list[dict] = []
    im_code = in_yaml = im_meta = False
    for nr, zeile in enumerate(text.splitlines(), start=1):
        s = zeile.strip()
        if nr == 1 and s == "---":
            in_yaml = True
            continue
        if in_yaml:
            in_yaml = s != "---"
            continue
        if s.startswith("```"):
            im_code = not im_code
            continue
        if not im_code and (meta := ist_meta_ueberschrift(s)) is not None:
            im_meta = meta
            continue
        if im_code or im_meta or not s or s.startswith("#") or re.fullmatch(r"[|:\-\s]+", s):
            continue
        ziel = ziele and ist_ziel(zeile)
        if not alle and not ist_aufgabenzeile(zeile) and not ziel and not NOMINAL_RE.match(zeile):
            continue
        if alle and not ziel and ist_rauschen(zeile):
            continue
        if ziel and NICHT_BEOBACHTBAR_RE.search(zeile):
            treffer.append({"quelle": quelle, "zeile": nr, "operator": None, "stufe": None,
                            "nicht_beobachtbar": True, "text": re.sub(r"\s+", " ", s)[:90]})
            continue
        funde = _erster_operator(zeile)
        nominal = False
        if not funde:
            m = NOMINAL_RE.match(zeile)
            if m:
                stufe, op = VERB_ZU_EINTRAG.get(NOMINAL[m.group(1)], (None, None))
                if stufe:
                    funde, nominal = [(m.start(1), stufe, op)], True
        if not funde:
            if SIE_RE.search(zeile) or W_FRAGE_RE.search(zeile):
                treffer.append({"quelle": quelle, "zeile": nr, "operator": None, "stufe": None,
                                "text": re.sub(r"\s+", " ", s)[:90]})
            continue
        funde.sort()
        _, stufe, operator = funde[0]
        treffer.append({
            "quelle": quelle, "zeile": nr, "operator": operator, "stufe": stufe,
            "stufe_name": STUFEN[stufe], "afb": afb(operator),
            "weitere": sorted({o for _, _, o in funde[1:] if o != operator}),
            "geschlossen": bool(GESCHLOSSEN_RE.search(zeile)),
            "nominal": nominal, "ziel": ziel,
            "text": re.sub(r"\s+", " ", s)[:90],
        })
    return treffer


def auswerten(treffer: list[dict]) -> dict:
    nicht_beob = [t for t in treffer if t.get("nicht_beobachtbar")]
    ohne = [t for t in treffer if t["stufe"] is None and not t.get("nicht_beobachtbar")]
    treffer = [t for t in treffer if t["stufe"] is not None]
    n = len(treffer)
    je_stufe = {s: sum(1 for t in treffer if t["stufe"] == s) for s in STUFEN}
    niedrig = je_stufe[1] + je_stufe[2]
    hoch = je_stufe[4] + je_stufe[5] + je_stufe[6]
    hinweise: list[str] = []
    if n == 0:
        hinweise.append("Keine Aufgabenzeilen mit Operator gefunden – Datei prüfen oder --alle nutzen.")
    else:
        if niedrig / n > 1 / 3:
            hinweise.append(f"Stufe 1–2 bei {niedrig / n:.0%} (Richtwert ≤ 1/3): "
                            "Aufgaben auf Anwenden/Analysieren anheben.")
        if hoch / n < 1 / 3:
            hinweise.append(f"Stufe 4–6 nur bei {hoch / n:.0%} (Richtwert ≥ 1/3): "
                            "Analyse-, Bewertungs- oder Gestaltungsaufgaben ergänzen.")
        fehlend = [STUFEN[s] for s in (4, 5, 6) if je_stufe[s] == 0]
        if fehlend:
            hinweise.append("Keine Aufgabe in: " + ", ".join(fehlend) + ".")
        if not hinweise:
            hinweise.append("Verteilung im Richtbereich (Heuristik – Einzelprüfung trotzdem nötig).")
        geschl = [t for t in treffer if t.get("geschlossen") and t["stufe"] >= 4]
        if geschl:
            hinweise.append(f"{len(geschl)} Aufgabe(n) im geschlossenen Format mit Operator ab Stufe 4 "
                            "(z. B. „Beurteilen Sie die Aussagen … richtig oder falsch“) – beim Ankreuzen meist "
                            "Stufe 2 (Wiedererkennen), Einordnung von Hand.")
        if any(t["operator"] in ("prüfen", "überprüfen") for t in treffer):
            hinweise.append("„prüfen“ ist mehrdeutig: Prüfhandlung (inspizieren, messen) = Anwenden, "
                            "Urteil an Kriterien = Bewerten – Einzelfall prüfen.")
    nominal = [t for t in treffer if t.get("nominal")]
    if nominal:
        hinweise.append(f"{len(nominal)} Anforderung(en) in Nominalform (z. B. „Entwicklung eines …“) über das Verb "
                        "eingeordnet – im Lastenheft üblich; als Arbeitsauftrag mit Operator formulieren.")
    if nicht_beob:
        hinweise.append(f"{len(nicht_beob)} Formulierung(en) nicht beobachtbar (z. B. „Bereitschaft entwickeln“, "
                        "„Reflexionsfähigkeit verbessern“) – nicht gezählt: "
                        + "; ".join(f"Z. {t['zeile']}" for t in nicht_beob[:8]))
    if ohne:
        hinweise.append(f"{len(ohne)} Arbeitsauftrag/-aufträge ohne Operator der Liste (z. B. „Notieren Sie …“, "
                        "W-Fragen) – nicht gezählt, von Hand einordnen: "
                        + "; ".join(f"Z. {t['zeile']}" for t in ohne[:8]) + (" …" if len(ohne) > 8 else ""))
    return {
        "anzahl": n,
        "je_stufe": je_stufe,
        "anteil_stufe_1_2": round(niedrig / n, 3) if n else 0.0,
        "anteil_stufe_4_6": round(hoch / n, 3) if n else 0.0,
        "hinweise": hinweise,
        "ohne_operator": len(ohne),
    }


def als_markdown(treffer: list[dict], summe: dict) -> str:
    zeilen = ["| Quelle:Zeile | Operator | Stufe | AFB | Aufgabe (gekürzt) |",
              "|---|---|---|---|---|"]
    for t in treffer:
        if t["stufe"] is None:
            continue
        zusatz = f" (+ {', '.join(t['weitere'])})" if t["weitere"] else ""
        zusatz += " · geschlossen" if t.get("geschlossen") else ""
        zusatz += " · Nominalform" if t.get("nominal") else ""
        zusatz += " · Ziel" if t.get("ziel") else ""
        zeilen.append(f"| {t['quelle']}:{t['zeile']} | {t['operator']}{zusatz} | "
                      f"{t['stufe']} {t['stufe_name']} | {t['afb']} | {t['text']} |")
    zeilen += ["", "| Stufe | Anzahl |", "|---|---|"]
    zeilen += [f"| {s} {STUFEN[s]} | {summe['je_stufe'][s]} |" for s in STUFEN]
    zeilen += ["", f"Aufgaben gesamt: {summe['anzahl']} · Anteil Stufe 1–2: "
               f"{summe['anteil_stufe_1_2']:.0%} · Anteil Stufe 4–6: {summe['anteil_stufe_4_6']:.0%}",
               ""]
    zeilen += [f"- {h}" for h in summe["hinweise"]]
    zeilen.append("\n_Heuristik nach Operatoren – ersetzt keine Einordnung nach tatsächlicher Denkleistung._")
    return "\n".join(zeilen)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Operatoren in Aufgaben den Bloom-Stufen zuordnen.")
    p.add_argument("dateien", nargs="+", type=Path)
    p.add_argument("--alle", action="store_true", help="jede Zeile mit Operator zählen")
    p.add_argument("--ziele", action="store_true", help="auch Kompetenz- und Zielformulierungen zählen")
    p.add_argument("--json", action="store_true", help="JSON statt Markdown ausgeben")
    args = p.parse_args(argv)

    treffer: list[dict] = []
    for datei in args.dateien:
        if not datei.is_file():
            print(f"Datei nicht gefunden: {datei}", file=sys.stderr)
            continue
        treffer += analysiere(lies_text(datei), datei.name, args.alle, args.ziele)
    summe = auswerten(treffer)
    if args.json:
        print(json.dumps({"aufgaben": treffer, "auswertung": summe}, ensure_ascii=False, indent=2))
    else:
        print(als_markdown(treffer, summe))
    return 0


if __name__ == "__main__":
    sys.exit(main())
