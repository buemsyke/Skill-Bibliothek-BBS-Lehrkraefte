#!/usr/bin/env python3
"""lernsituation_pruefen – Formalprüfung dokumentierter Lernsituationen (SchuCu-BBS 2024).

Je Datei (Ausgabe von `lernsituation-dokumentieren`, `20_lernsituation_….md`):
Kopf, Pflichtabschnitte der Vorlage, genau ein Auftrag in der Handlungssituation (Länge),
Handlungskompetenz in beiden Spalten, sechs Handlungsphasen mit Zeitsumme gleich Zeitrichtwert,
Analysebogen mit 16 Zeilen, gültiger Stufe und Beleg, stehengebliebene Platzhalter,
Transparenzzeile.

Über mehrere Dateien (Lerngebiet bzw. Lernfeld, `curriculum-abgleich.md` Abschn. 7):
Kompetenzraster aus dem Kopffeld `kompetenz_codes` – keine leere Zeile, keine leere Spalte,
Codes, die fast überall angekreuzt sind; Stundenbilanz; wortgleiche Personale Kompetenzen;
gleichlautende Belege im Analysebogen (Hinweis auf schematisch ausgefüllte Bögen).

Das Skript prüft nur Formales. Ob eine Einschätzung im Analysebogen **stimmt**, beurteilt es
nicht. Nur Python-Standardbibliothek.

Aufruf:
    python3 lernsituation_pruefen.py LS.md… [--ziel FK1,FK2,…] [--verfuegbar STD]
                                     [--schwelle 0.8] [--json]

    --ziel        Codes der Zielformulierung (sonst: alle Codes, die in den Dateien vorkommen)
    --verfuegbar  schulintern verfügbare Stunden für das Lerngebiet bzw. Lernfeld
    --schwelle    Anteil der LS, ab dem ein Code als „unterscheidet kaum“ gilt (Standard 0.8)

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

PFLICHT = [
    "## Rahmen", "## Lernsituation", "### Handlungskompetenz", "### Handlungssituation",
    "### Handlungsergebnis", "### Inhalte", "### Distanzunterricht",
    "## Vereinbarungen und Hinweise zur Umsetzung", "## Phasenplanung", "## Analysebogen",
    "## Annahmen und Prüfaufträge", "## Übergabe",
]
PHASEN = [
    ("Informieren", r"Informieren|Analysieren"), ("Planen", r"\bPlanen"),
    ("Entscheiden", r"Entscheiden"), ("Durchführen", r"Durchführen"),
    ("Überprüfen", r"Überprüfen|Kontrollieren"), ("Reflektieren", r"Reflektieren"),
]
STUFEN = {"trifft zu", "trifft eher zu", "trifft eher nicht zu", "trifft nicht zu"}
MIN_JE_STD = 45


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"\A---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    felder = {}
    for zeile in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_]+):\s*(.*)$", zeile)
        if km:
            felder[km.group(1)] = re.sub(r"\s+#.*$", "", km.group(2)).strip().strip('"')
    return felder, text[m.end():]


def abschnitt(text: str, kopf: str) -> str:
    """Inhalt unter einer Überschrift (Präfix) bis zur nächsten gleicher oder höherer Ebene."""
    ebene = len(kopf) - len(kopf.lstrip("#"))
    m = re.search(rf"(?m)^{re.escape(kopf)}[^\n]*\n", text)
    if not m:
        return ""
    ende = re.search(rf"(?m)^#{{1,{ebene}}} ", text[m.end():])
    return text[m.end(): m.end() + ende.start()] if ende else text[m.end():]


def zellen(zeile: str) -> list[str] | None:
    if not re.match(r"^\s*\|.*\|\s*$", zeile) or re.match(r"^\s*\|[\s:|-]+\|\s*$", zeile):
        return None
    return [c.strip() for c in re.split(r"(?<!\\)\|", zeile.strip().strip("|"))]


def tabelle(text: str) -> list[list[str]]:
    return [c for z in text.splitlines() if (c := zellen(z))]


def minuten(angabe: str) -> int | None:
    """„ca. 10 min“ → 10, „ca. 2 Std.“ / „2 Unterrichtsstunden“ → 90; sonst None."""
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*min", angabe)
    if m:
        return round(float(m.group(1).replace(",", ".")))
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:Std|Unterrichtsstunde|Stunde|h\b)", angabe)
    if m:
        return round(float(m.group(1).replace(",", ".")) * MIN_JE_STD)
    return None


def codes(fm: dict[str, str]) -> list[str]:
    return re.findall(r"[A-Za-zÄÖÜ]+\d+(?:\.\d+)?", fm.get("kompetenz_codes", ""))


def norm(s: str) -> str:
    return " ".join(re.findall(r"[0-9a-zäöüß]+", s.lower()))


def befund(liste, nr, name, stufe, hinweis=""):
    liste.append({"nr": nr, "pruefung": name, "stufe": stufe, "hinweis": hinweis})


def lies(pfad: Path) -> dict:
    text = pfad.read_text(encoding="utf-8")
    fm, rumpf = frontmatter(text)
    b: list[dict] = []
    erg = {"datei": str(pfad), "titel": fm.get("titel", ""), "codes": codes(fm), "befunde": b,
           "pk": [], "belege": {}, "zeitrichtwert_min": None}

    fehlt = [k for k in ("artefakt", "titel", "stand", "curriculare_vorgabe", "status") if not fm.get(k)]
    if "gymnasium" in (fm.get("schulform", "") + fm.get("bildungsgang", "")).lower():
        fehlt += [k for k in ("schuljahrgang", "lerngebiet", "zeitrichtwert_lerngebiet") if not fm.get(k)]
    befund(b, 1, "Kopf", "⚠" if fehlt else "✅", ("fehlt: " + ", ".join(fehlt)) if fehlt else "")

    ohne = [k for k in PFLICHT if not re.search(rf"(?m)^{re.escape(k)}", rumpf)]
    befund(b, 2, "Pflichtabschnitte", "❌" if ohne else "✅", ("fehlt: " + ", ".join(ohne)) if ohne else "")

    hs = abschnitt(rumpf, "### Handlungssituation")
    auftraege = len(re.findall(r"\*\*Ihr Auftrag:?\*\*", hs))
    w = len(re.findall(r"\w+", re.sub(r"(?m)^\*Material.*$|^>.*Ihr Auftrag.*$", "", hs)))
    stufe = "✅" if auftraege == 1 and 120 <= w <= 220 else ("❌" if auftraege != 1 else "⚠")
    befund(b, 3, "Handlungssituation", stufe,
           f"{auftraege}× „Ihr Auftrag“, {w} Wörter" + ("" if 120 <= w <= 220 else " (Richtwert 120–220)"))

    hk = tabelle(abschnitt(rumpf, "### Handlungskompetenz"))
    fk = [c[0] for c in hk[2:] if len(c) > 1 and c[0].strip("– ")]
    pk = [c[1] for c in hk[2:] if len(c) > 1 and c[1].strip("– ")]
    erg["pk"] = [p.strip("– .") for p in pk]
    befund(b, 4, "Handlungskompetenz", "✅" if fk and pk else "❌",
           f"{len(fk)} Fach-, {len(pk)} Personale Kompetenz(en)")

    lsrahmen = {c[0]: c[1] for c in tabelle(abschnitt(rumpf, "## Lernsituation")) if len(c) > 1}
    zrw = minuten(lsrahmen.get("Zeitrichtwert Lernsituation", ""))
    erg["zeitrichtwert_min"] = zrw
    pp = tabelle(abschnitt(rumpf, "## Phasenplanung"))
    phasenzeilen = [c for c in pp[1:] if len(c) > 1 and not c[0].startswith("**Σ")]
    vorhanden = [n for n, rx in PHASEN if any(re.search(rx, c[1]) for c in phasenzeilen)]
    fehlend = [n for n, _ in PHASEN if n not in vorhanden]
    befund(b, 5, "Sechs Handlungsphasen", "❌" if fehlend else "✅",
           ("fehlt: " + ", ".join(fehlend)) if fehlend else "")
    zeiten = [minuten(c[0]) for c in phasenzeilen if c[0] and c[0] != "–"]
    if not zeiten:
        befund(b, 5, "Phasensumme", "⚠", "keine Zeitangaben")
    elif None in zeiten:
        befund(b, 5, "Phasensumme", "⚠", "nicht alle Zeiten summierbar (z. B. Arbeit außerhalb des Unterrichts)")
    elif zrw is None:
        befund(b, 5, "Phasensumme", "⚠", f"Σ {sum(zeiten)} min, Zeitrichtwert der LS nicht lesbar")
    else:
        befund(b, 5, "Phasensumme", "✅" if sum(zeiten) == zrw else "❌",
               f"Σ {sum(zeiten)} min, Zeitrichtwert {zrw} min")

    ab = [c for c in tabelle(abschnitt(rumpf, "## Analysebogen")) if c[0].isdigit()]
    nummern = sorted(int(c[0]) for c in ab)
    ungueltig = [c[0] for c in ab if len(c) < 3 or c[2].strip("* ") not in STUFEN]
    ohne_beleg = [c[0] for c in ab if len(c) < 4 or not c[3].strip(" –-")]
    erg["belege"] = {c[0]: norm(c[3]) for c in ab if len(c) > 3}
    if nummern != list(range(1, 17)):
        befund(b, 6, "Analysebogen", "❌", f"{len(ab)} Zeilen statt 16")
    elif ungueltig:
        befund(b, 6, "Analysebogen", "❌", "ungültige oder fehlende Stufe: Nr. " + ", ".join(ungueltig))
    else:
        befund(b, 6, "Analysebogen", "⚠" if ohne_beleg else "✅",
               ("ohne Beleg: Nr. " + ", ".join(ohne_beleg)) if ohne_beleg else "16 Kriterien mit Stufe und Beleg")

    ohne_code = re.sub(r"`[^`\n]*`", "", re.sub(r"(?ms)^```.*?^```", "", rumpf))
    platz = [m.group(0) for m in re.finditer(r"\[[^\]\n]{3,}\](?!\()", ohne_code)
             if not re.search(r"einzutragen|ABBILDUNG", m.group(0))]
    befund(b, 7, "Platzhalter", "⚠" if platz else "✅",
           (f"{len(platz)}× z. B. {platz[0][:60]}") if platz else "")

    befund(b, 8, "Transparenzzeile", "✅" if "KI-gestützt erstellt" in rumpf else "⚠",
           "" if "KI-gestützt erstellt" in rumpf else "Zeile „KI-gestützt erstellt …“ fehlt")
    offen = rumpf.count("🔎")
    befund(b, 9, "Offene Prüfaufträge", "✅" if not offen else "⚠", f"{offen}× 🔎" if offen else "")
    return erg


def lerngebiet(erg: list[dict], ziel: list[str] | None, verfuegbar: float | None,
               schwelle: float, zeitrichtwert: float | None) -> list[dict]:
    b: list[dict] = []
    n = len(erg)
    mit_codes = [e for e in erg if e["codes"]]
    if not mit_codes:
        befund(b, "M1", "Kompetenzraster", "⚠", "kein Kopffeld kompetenz_codes – Raster nicht prüfbar")
    else:
        zaehler = collections.Counter(c for e in erg for c in set(e["codes"]))
        soll = ziel or sorted(zaehler)
        leer = [c for c in soll if not zaehler[c]]
        befund(b, "M1", "Keine leere Zeile", "❌" if leer else "✅",
               ("nicht eingelöst: " + ", ".join(leer)) if leer else f"{len(soll)} Codes eingelöst")
        ohne = [Path(e["datei"]).name for e in erg if not e["codes"]]
        befund(b, "M1", "Keine leere Spalte", "❌" if ohne else "✅",
               ("ohne Code: " + ", ".join(ohne)) if ohne else "")
        fremd = sorted(set(zaehler) - set(soll)) if ziel else []
        if fremd:
            befund(b, "M1", "Codes außerhalb der Zielformulierung", "⚠", ", ".join(fremd))
        breit = [f"{c} ({zaehler[c]}/{n})" for c in soll if n >= 4 and zaehler[c] / n >= schwelle]
        befund(b, "M1", "Kreuze mit Aussagekraft", "⚠" if breit else "✅",
               ("fast überall angekreuzt – Rückwärtsprobe: " + ", ".join(breit)) if breit else "")
        selten = [f"{c} ({zaehler[c]})" for c in soll if zaehler[c] == 1]
        if selten:
            befund(b, "M1", "Nur einmal eingelöst", "⚠", ", ".join(selten))

    zeiten = [e["zeitrichtwert_min"] for e in erg]
    if None in zeiten:
        befund(b, "M2", "Stundenbilanz", "⚠", "Zeitrichtwert nicht in allen LS lesbar")
    else:
        std = sum(zeiten) / MIN_JE_STD
        teile = [f"Σ LS {std:g} Std."]
        stufe = "✅"
        if zeitrichtwert is not None:
            teile.append(f"Zeitrichtwert {zeitrichtwert:g} Std.")
            if std > zeitrichtwert:
                stufe = "⚠"
        if verfuegbar is not None:
            teile.append(f"verfügbar {verfuegbar:g} Std.")
            if std > verfuegbar:
                stufe = "⚠"
        befund(b, "M2", "Stundenbilanz", stufe, ", ".join(teile))

    pk = collections.defaultdict(set)
    anfang = collections.defaultdict(set)
    for e in erg:
        for p in e["pk"]:
            pk[norm(p)].add(Path(e["datei"]).name[:22])
            anfang[" ".join(norm(p).split()[:3])].add(Path(e["datei"]).name[:22])
    gleich = [f"„{k[:50]}…“ ({len(v)} LS)" for k, v in pk.items() if len(v) > 1]
    aehnlich = [f"„{k} …“ ({len(v)} LS)" for k, v in anfang.items() if len(v) >= max(3, n // 4)]
    befund(b, "M3", "Personale Kompetenz", "⚠" if gleich or aehnlich else "✅",
           "; ".join((["wortgleich: " + ", ".join(gleich)] if gleich else [])
                     + (["gleicher Anfang: " + ", ".join(aehnlich[:4])] if aehnlich else [])))

    schematisch = []
    for nr in map(str, range(1, 17)):
        texte = collections.Counter(e["belege"].get(nr) for e in erg if e["belege"].get(nr))
        if texte:
            text, anzahl = texte.most_common(1)[0]
            if n >= 3 and anzahl / n > 0.5:
                schematisch.append(f"Nr. {nr} ({anzahl}/{n})")
    befund(b, "M4", "Belege im Analysebogen", "⚠" if schematisch else "✅",
           ("gleichlautend – Beleg je LS aus der LS selbst: " + ", ".join(schematisch)) if schematisch else "")
    return b


def markdown(erg: list[dict], gebiet: list[dict]) -> str:
    aus = []
    for e in erg:
        aus.append(f"## {Path(e['datei']).name}\n\n| Nr. | Prüfung | Ergebnis | Hinweis |\n|---|---|---|---|")
        aus += [f"| {x['nr']} | {x['pruefung']} | {x['stufe']} | {x['hinweis']} |" for x in e["befunde"]]
        aus.append("")
    if gebiet:
        aus.append("## Lerngebiet bzw. Lernfeld\n\n| Nr. | Prüfung | Ergebnis | Hinweis |\n|---|---|---|---|")
        aus += [f"| {x['nr']} | {x['pruefung']} | {x['stufe']} | {x['hinweis']} |" for x in gebiet]
    aus.append("\nNur Formales – ob eine Einschätzung im Analysebogen stimmt, beurteilt das Skript nicht.")
    return "\n".join(aus)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Dokumentierte Lernsituationen formal prüfen.")
    p.add_argument("dateien", nargs="+", type=Path)
    p.add_argument("--ziel", default=None, help="Codes der Zielformulierung, kommagetrennt")
    p.add_argument("--verfuegbar", type=float, default=None)
    p.add_argument("--schwelle", type=float, default=0.8)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    fehlend = [str(x) for x in a.dateien if not x.is_file()]
    if fehlend:
        print("Datei nicht gefunden: " + ", ".join(fehlend), file=sys.stderr)
        return 2
    erg = [lies(x) for x in a.dateien]
    zrw = None
    for x in a.dateien:
        fm, _ = frontmatter(x.read_text(encoding="utf-8"))
        if re.fullmatch(r"\d+(?:[.,]\d+)?", fm.get("zeitrichtwert_lerngebiet", "") or fm.get("zeitrichtwert_lernfeld", "")):
            zrw = float((fm.get("zeitrichtwert_lerngebiet") or fm.get("zeitrichtwert_lernfeld")).replace(",", "."))
            break
    ziel = [c.strip() for c in a.ziel.split(",") if c.strip()] if a.ziel else None
    gebiet = lerngebiet(erg, ziel, a.verfuegbar, a.schwelle, zrw) if len(erg) > 1 else []
    if a.json:
        for e in erg:
            e.pop("belege", None)
        print(json.dumps({"lernsituationen": erg, "lerngebiet": gebiet}, ensure_ascii=False, indent=2))
    else:
        print(markdown(erg, gebiet))
    alle = [x for e in erg for x in e["befunde"]] + gebiet
    return 1 if any(x["stufe"] == "❌" for x in alle) else 0


if __name__ == "__main__":
    sys.exit(main())
