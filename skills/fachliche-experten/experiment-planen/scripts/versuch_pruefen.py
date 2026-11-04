#!/usr/bin/env python3
"""versuch_pruefen – Versuchsanleitung mit Gefährdungsbeurteilung prüfen (lokal, deterministisch).

Prüft eine Versuchsanleitung nach assets/vorlage-versuchsanleitung.md (Markdown, auch DOCX/ODT/PDF
über text_lesen.py, falls vorhanden):

  Abschnitte     Fragestellung/Hypothese, Variablen, Material, Aufbau, Durchführung, Messwerte,
                 Auswertung, Fehlerbetrachtung, Gefährdungsbeurteilung, Entsorgung, Notfall, Vorversuch
  Messwerte      Tabelle mit Einheiten im Kopf („U in V“, „I [mA]“)
  Gefahren       typische Kombinationen (references/experimentsicherheit.md Abschn. 4) – ⚠, wenn die
                 Gefährdungsbeurteilung die Gefahr nicht behandelt
  Ersatzstoffe   Ersatzstoff- bzw. Ersatzverfahrensprüfung erwähnt
  Freigabe       Zeile „Freigabe: ausstehend“ bzw. „Freigabe: erteilt – KÜRZEL, JJJJ-MM-TT“
  Platzhalter    offene [Platzhalter]

Kein Skript und keine KI gibt einen Versuch frei – das Ergebnis ist eine Vorprüfung für die Lehrkraft.

Aufruf:
    python3 versuch_pruefen.py 41_experiment_….md [--json]

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from text_lesen import lies_text  # type: ignore
except Exception:  # noqa: BLE001
    def lies_text(pfad: Path) -> str:  # type: ignore[misc]
        return Path(pfad).read_text(encoding="utf-8", errors="replace")

ABSCHNITTE = [
    ("Fragestellung bzw. Hypothese", r"fragestellung|hypothese|vorhersage"),
    ("Variablen", r"variable"),
    ("Material und Geräte", r"material|geräte"),
    ("Aufbau", r"aufbau"),
    ("Durchführung", r"durchführung"),
    ("Messwerte", r"messwert|messung|messtabelle"),
    ("Auswertung", r"auswertung"),
    ("Fehlerbetrachtung", r"fehlerbetrachtung|messunsicherheit|fehlerdiskussion"),
    ("Gefährdungsbeurteilung", r"gefährdungsbeurteilung"),
]
GB_FELDER = [
    ("Entsorgung", r"entsorgung"),
    ("Notfall", r"notfall|erste hilfe"),
    ("Vorversuch", r"vorversuch"),
]
# Signal im Text → Begriffe, die die Gefährdungsbeurteilung dann enthalten soll, Hinweis
GEFAHREN = [
    (r"elektroly", r"kochsalz|\bnacl\b|salzwasser|natriumchlorid|salzsäure",
     r"chlor", "Elektrolyse mit kochsalzhaltigem Elektrolyt: Chlorbildung an der Anode – Ersatzelektrolyt oder Abzug"),
    (r"knallgas", None, r"menge|reagenzglas|schutzbrille",
     "Knallgas: Mengenbegrenzung (Reagenzglas), Schutzbrille, Lehrkraft entscheidet über Durchführung"),
    (r"wasserstoff", r"sammeln|ballon|flasche|gasometer|speicher",
     r"explosi|zündquelle", "Wasserstoff in größeren Mengen: Explosionsgefahr, Zündquellen fernhalten"),
    (r"natronlauge|kalilauge|\bnaoh\b|\bkoh\b", None, r"ätzend|schutzbrille|handschuh",
     "Lauge: ätzend – Schutzbrille und Handschuhe"),
    (r"230\s*v|400\s*v|netzspannung|drehstrom", None,
     r"schutzkleinspannung|prüfstand|sicherheitsbuchse|fünf sicherheitsregeln|5 sicherheitsregeln",
     "Netzspannung: nur Schutzkleinspannung oder Prüfstand mit Sicherheitsbuchsen; fünf Sicherheitsregeln"),
    (r"lithium|li-ion|li-po|akku", r"lad", r"brand",
     "Lithium-Akku laden: Brandgefahr – geeignetes Ladegerät, Brandschutzbehälter"),
]
KATEGORIE = re.compile(r"^(?:elektrode\w*|material|probe|variante|stufe|gruppe|art|bemerkung\w*|beobachtung\w*|"
                       r"einstellung|nr\.?|durchgang)$", re.IGNORECASE)   # Spalten ohne Einheit
EINHEIT_KOPF = re.compile(r"\bin\s+[A-Za-zµΩ°%/·³²]+|\[[^\]]+\]|\(\s*[A-Za-zµΩ°%/·³²]+\s*\)")


def _ohne_markdown_ueberschriften(text: str) -> str:
    """DOCX/PDF ohne „#“: kurze Zeilen ohne Satzzeichen am Ende als Überschrift markieren."""
    if re.search(r"^#+\s", text, re.M):
        return text
    aus = []
    for z in text.splitlines():
        s = z.strip()
        kurz = 0 < len(s.split()) <= 6 and not re.search(r"[.,;!?]$", s) and not s.startswith("|")
        aus.append(f"## {s}" if kurz and re.match(r"[A-ZÄÖÜ]", s) else z)
    return "\n".join(aus)


def abschnitt(text: str, muster: str) -> str:
    """Text des ersten Abschnitts, dessen Überschrift auf das Muster passt (bis zur nächsten gleichen Ebene)."""
    zeilen = text.splitlines()
    for i, z in enumerate(zeilen):
        m = re.match(r"^(#+)\s+(.*)", z)
        if m and re.search(muster, m.group(2), re.IGNORECASE):
            ebene = len(m.group(1))
            rest = []
            for w in zeilen[i + 1:]:
                n = re.match(r"^(#+)\s", w)
                if n and len(n.group(1)) <= ebene:
                    break
                rest.append(w)
            return "\n".join(rest)
    return ""


def pruefe(text: str) -> list[tuple[str, str, str]]:
    befunde: list[tuple[str, str, str]] = []
    text = _ohne_markdown_ueberschriften(text)
    ueberschriften = " | ".join(re.findall(r"^#+\s+(.*)$", text, re.M))
    fehlend = [name for name, m in ABSCHNITTE if not re.search(m, ueberschriften, re.IGNORECASE)]
    befunde.append(("Abschnitte", "✅" if not fehlend else "❌",
                    "vollständig" if not fehlend else "fehlt: " + ", ".join(fehlend)))

    gb = abschnitt(text, r"gefährdungsbeurteilung")
    if gb:
        gb_fehlend = [name for name, m in GB_FELDER if not re.search(m, gb, re.IGNORECASE)]
        befunde.append(("Gefährdungsbeurteilung: Felder", "✅" if not gb_fehlend else "❌",
                        "Entsorgung, Notfall, Vorversuch vorhanden" if not gb_fehlend else "fehlt: " + ", ".join(gb_fehlend)))
        stop = re.search(r"\bSTOP\b|substitution|technisch.*organisatorisch", gb, re.IGNORECASE | re.S)
        befunde.append(("Maßnahmen nach STOP", "✅" if stop else "⚠️",
                        "angegeben" if stop else "Maßnahmen nicht nach STOP geordnet"))
        ersatz = re.search(r"ersatz", gb, re.IGNORECASE)
        befunde.append(("Ersatzstoffprüfung", "✅" if ersatz else "⚠️",
                        "dokumentiert" if ersatz else "Ersatzstoff- bzw. Ersatzverfahrensprüfung fehlt"))

    for signal, zusatz, erwartet, hinweis in GEFAHREN:
        if re.search(signal, text, re.IGNORECASE) and (zusatz is None or re.search(zusatz, text, re.IGNORECASE)):
            behandelt = bool(gb) and re.search(erwartet, gb, re.IGNORECASE)
            befunde.append(("Gefahrenhinweis", "✅" if behandelt else "⚠️",
                            hinweis + (" – in der Gefährdungsbeurteilung behandelt" if behandelt else
                                       " – in der Gefährdungsbeurteilung ergänzen")))

    mw = abschnitt(text, r"messwert|messung|messtabelle")
    kopf = next((z for z in mw.splitlines() if z.strip().startswith("|")), "")
    if kopf:
        spalten = [c.strip() for c in kopf.strip().strip("|").split("|")][1:]
        ohne = [c for c in spalten if c and not EINHEIT_KOPF.search(c) and not KATEGORIE.search(c)]
        befunde.append(("Messwerttabelle", "✅" if not ohne else "⚠️",
                        "Einheiten im Tabellenkopf" if not ohne else "ohne Einheit: " + ", ".join(ohne)))
    elif mw:
        befunde.append(("Messwerttabelle", "⚠️", "keine Tabelle im Abschnitt Messwerte"))

    fr = re.search(r"^\s*Freigabe:\s*(.+)$", text, re.M | re.IGNORECASE)
    if not fr:
        befunde.append(("Freigabezeile", "❌", "Zeile „Freigabe: ausstehend“ fehlt – ohne Freigabe keine Ausgabe an Lernende"))
    elif re.match(r"erteilt", fr.group(1).strip(), re.IGNORECASE):
        ok = re.search(r"erteilt\s*[–-]\s*\S+.*\d{4}-\d{2}-\d{2}", fr.group(1), re.IGNORECASE)
        befunde.append(("Freigabezeile", "✅" if ok else "⚠️",
                        "erteilt" if ok else "„erteilt“ ohne Kürzel und Datum (Form: erteilt – KÜRZEL, JJJJ-MM-TT)"))
    else:
        befunde.append(("Freigabezeile", "✅", "ausstehend – Lehrkraft prüft, macht den Vorversuch und gibt frei"))

    platzhalter = re.findall(r"\[[^\]\n]{2,60}\]", re.sub(r"`[^`]*`", "", text))
    platzhalter = [p for p in platzhalter if not re.fullmatch(r"\[\s*[A-Za-zµΩ°%/·³²]+\s*\]", p)]
    if platzhalter:
        befunde.append(("Platzhalter", "⚠️", f"{len(platzhalter)} offen, z. B. {platzhalter[0]}"))
    return befunde


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Versuchsanleitung mit Gefährdungsbeurteilung prüfen.")
    ap.add_argument("datei", type=Path)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if not a.datei.is_file():
        print(f"Fehler: nicht gefunden: {a.datei}", file=sys.stderr)
        return 2
    befunde = pruefe(lies_text(a.datei))
    if a.json:
        print(json.dumps(befunde, ensure_ascii=False, indent=2))
    else:
        print("| Prüfpunkt | Ergebnis | Hinweis |\n|---|---|---|")
        for p, s, h in befunde:
            print(f"| {p} | {s} | {h} |")
        print("\n_Vorprüfung – ersetzt weder Gefährdungsbeurteilung noch Vorversuch der Lehrkraft._")
    return 1 if any(s == "❌" for _, s, _ in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
