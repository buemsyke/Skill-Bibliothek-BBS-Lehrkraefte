#!/usr/bin/env python3
"""klausur_check – Selbstprüfung einer Klassenarbeit oder Lernzielkontrolle (lokal, deterministisch).

Liest die Punkteübersicht aus dem Erwartungshorizont – eine Markdown-Tabelle mit mindestens den
Spalten „Aufgabe", „AFB" und „Punkte", optional „Min.", „Bezug" und „Antwort" – und prüft:

  Summe        Punkte der Zeilen = Σ-Zeile = Gesamtpunkte (Angabe „Gesamtpunkte: N" oder --gesamt)
  Zeit         Minutensumme ≤ Bearbeitungszeit; Takt = Bearbeitungszeit / Gesamtpunkte
  Umfang       Anzahl Hauptaufgaben (Kontextwechsel)
  AFB          Anteile in Prozent der Punkte gegen den Sollwert (gerechnet, nicht abgeschrieben)
  Einstieg     erste Zeile nicht AFB III
  Bezug        jede Zeile mit Bezug zu Lernsituation/Kompetenz (falls Spalte vorhanden)
  Schreiblast  Punkteanteil je Antwortformat (Kurz, Rechnung, Skizze, Text); Freitext über 30 % ⚠
               (nur mit Spalte „Antwort"; Richtwert der Bibliothek, kein amtlicher Wert)
  Single Choice  Verteilung der Lösungsbuchstaben (--sc "CADBE…")

Gibt außerdem den Notenschlüssel in Punkten aus (Grenzen aus der Gesamtpunktzahl gerechnet und auf
halbe Punkte aufgerundet, wie edu-bewertung) und die Zeile „Gesamtsummen …" für die
regelbasierte Begutachtung.

Aufruf:
    python3 klausur_check.py ERWARTUNGSHORIZONT.md [--typ klassenarbeit|klausur-bg|lzk] [--gesamt N] [--zeit MIN]
        [--afb 30/40/30] [--toleranz 10] [--max-aufgaben 10] [--system 15|ihk] [--grenzen "92:1,…,0:6"]
        [--sc CADBE…] [--ganze-punkte]

AFB-Soll: Klassenarbeit und Klausur im Beruflichen Gymnasium 30/40/30 ±10 (Entscheidung der
Fachberatung 10/2026, wie EPA); Lernzielkontrolle 40/50/10. Typ klausur-bg: Bewertungseinheiten
(„BE“), Takt ab 2,0 min/BE, Notenpunkte.

Exit 0 = keine ❌ (⚠ möglich), 1 = mindestens ein ❌, 2 = Eingabefehler.
Nur Python-Standardbibliothek. Arbeitet nur mit Aufgaben und Punkten (Datenschutzstufe 0).
"""

from __future__ import annotations

import argparse
import math
import re
import sys
from collections import Counter
from pathlib import Path

NOTENPUNKTE_15 = [(95, "15 (1+)"), (90, "14 (1)"), (85, "13 (1-)"), (80, "12 (2+)"), (75, "11 (2)"),
                  (70, "10 (2-)"), (65, "09 (3+)"), (60, "08 (3)"), (55, "07 (3-)"), (50, "06 (4+)"),
                  (45, "05 (4)"), (40, "04 (4-)"), (33, "03 (5+)"), (27, "02 (5)"), (20, "01 (5-)"), (0, "00 (6)")]
NOTEN_IHK = [(92, "1 (sehr gut)"), (81, "2 (gut)"), (67, "3 (befriedigend)"), (50, "4 (ausreichend)"),
             (30, "5 (mangelhaft)"), (0, "6 (ungenügend)")]
SCHLUESSEL = {"15": NOTENPUNKTE_15, "ihk": NOTEN_IHK}

TYPEN = {
    # Takt in Minuten je Punkt: ✅ ab „gut", ⚠ ab „mindestens", darunter ❌
    "klassenarbeit": {"afb": (30, 40, 30), "takt_gut": 1.5, "takt_min": 1.0, "max_aufgaben": 10},
    "klausur-bg": {"afb": (30, 40, 30), "takt_gut": 2.0, "takt_min": 1.5, "max_aufgaben": 6, "einheit": "BE"},
    "lzk": {"afb": (40, 50, 10), "takt_gut": 0.8, "takt_min": 0.6, "max_aufgaben": None},
}
FREITEXT_GRENZE = 30.0      # Prozent der Punkte; Richtwert aus der Praxis (Beispielklausur: 16 %)
FORMATE = (("Kurz", ("kurz", "buchst", "zahl", "wert", "luecke", "lücke", "tabelle", "ankreuz", "wahl", "ausdruck")),
           ("Rechnung", ("rechn",)),
           ("Skizze", ("skizz", "zeichn", "diagramm")),
           ("Text", ("text", "frei", "linie", "begründ", "begruend")))
SUMME = re.compile(r"^\s*(?:Σ|∑|summe|gesamt|insgesamt)\b", re.I)
AFB_WERT = re.compile(r"\b(III|II|I)\b(?:\s*[–\-/]\s*(III|II|I)\b)?")
ZAHL = re.compile(r"(\d+(?:[.,]\d+)?)")


class Eingabefehler(Exception):
    pass


def _zahl(text: str) -> float | None:
    m = ZAHL.search(text or "")
    return float(m.group(1).replace(",", ".")) if m else None


def _zelle(text: str) -> str:
    return re.sub(r"[*_`]", "", text).strip()


def _fmt(x: float) -> str:
    return f"{x:g}".replace(".", ",")


def tabellen(text: str) -> list[list[list[str]]]:
    """Alle Markdown-Tabellen als Listen von Zeilen (ohne Trennzeile)."""
    erg, akt = [], []
    for zeile in text.splitlines():
        s = zeile.strip()
        if s.startswith("|"):
            zellen = [_zelle(z) for z in s.strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", z.replace(" ", "")) for z in zellen if z):
                continue
            akt.append(zellen)
        elif akt:
            erg.append(akt)
            akt = []
    if akt:
        erg.append(akt)
    return erg


def lies_uebersicht(text: str) -> tuple[list[dict], float | None]:
    """Findet die Punkteübersicht. Rückgabe: Zeilen und Wert der Σ-Zeile (falls vorhanden).
    Passen mehrere Tabellen (z. B. eine Übersicht je Aufgabe und eine je Teilaufgabe), gilt die
    mit den meisten Zeilen – die feinste Gliederung."""
    treffer = []
    for tab in tabellen(text):
        kopf = [k.lower().strip(" .") for k in tab[0]]

        def spalte(praefixe=(), genau=()):
            return next((i for i, k in enumerate(kopf) if k in genau or any(k.startswith(n) for n in praefixe)), None)
        i_auf = spalte(("aufgabe", "teilaufgabe"), ("nr", "nummer"))
        i_afb = spalte(("afb", "anforderungsbereich"))
        i_pkt = spalte(("punkte", "pkt"), ("p", "be", "bewertungseinheiten"))
        if None in (i_auf, i_afb, i_pkt):
            continue
        i_min = spalte(("min", "zeit"))
        i_bez = spalte(("bezug", "kompetenz", "lernsituation"), ("ls", "k-code"))
        i_ant = spalte(("antwort", "format"))
        zeilen, summe = [], None
        for z in tab[1:]:
            z = z + [""] * (len(kopf) - len(z))
            if SUMME.match(z[i_auf]) or (not z[i_auf] and _zahl(z[i_pkt]) is not None):
                summe = _zahl(z[i_pkt])
                continue
            if not z[i_auf]:
                continue
            zeilen.append({"aufgabe": z[i_auf], "afb": z[i_afb], "punkte": _zahl(z[i_pkt]),
                           "min": _zahl(z[i_min]) if i_min is not None else None,
                           "bezug": z[i_bez] if i_bez is not None else None,
                           "antwort": z[i_ant] if i_ant is not None else None})
        if zeilen:
            treffer.append((zeilen, summe))
    if treffer:
        return max(treffer, key=lambda x: len(x[0]))
    raise Eingabefehler("keine Punkteübersicht gefunden (Tabelle mit den Spalten Aufgabe, AFB, Punkte)")


def afb_anteile(zeilen: list[dict]) -> tuple[dict[str, float], list[str]]:
    """Punkte je AFB; Bereichsangaben wie „I–II" werden zu gleichen Teilen verteilt."""
    stufen = ["I", "II", "III"]
    erg = {s: 0.0 for s in stufen}
    unklar = []
    for z in zeilen:
        m = AFB_WERT.search(z["afb"] or "")
        if not m or z["punkte"] is None:
            unklar.append(z["aufgabe"])
            continue
        von = stufen.index(m.group(1))
        bis = stufen.index(m.group(2)) if m.group(2) else von
        bereich = stufen[min(von, bis):max(von, bis) + 1]
        for s in bereich:
            erg[s] += z["punkte"] / len(bereich)
    return erg, unklar


def antwort_format(wert: str) -> str | None:
    w = (wert or "").lower()
    return next((name for name, schluessel in FORMATE if any(s in w for s in schluessel)), None)


def notenschluessel(gesamt: float, stufen: list[tuple[float, str]], schritt: float = 0.5) -> list[tuple[str, float, float]]:
    """(Label, ab %, ab Punkte) – Grenze = Prozent × Gesamt, auf `schritt` aufgerundet."""
    erg = []
    for prozent, label in stufen:
        roh = prozent / 100 * gesamt
        ab = math.ceil(round(roh / schritt, 9)) * schritt
        erg.append((label, prozent, min(ab, gesamt)))
    return erg


def eigene_grenzen(text: str) -> list[tuple[float, str]]:
    stufen = []
    for teil in (t for t in text.split(",") if t.strip()):
        g, _, lab = teil.partition(":")
        stufen.append((float(g.replace(",", ".")), lab.strip()))
    stufen.sort(key=lambda x: -x[0])
    if not stufen or stufen[-1][0] != 0:
        raise Eingabefehler("eigene Grenzen brauchen eine Stufe ab 0 %")
    return stufen


def hauptnummer(aufgabe: str) -> str:
    m = re.match(r"[A-Za-z]*\s*(\d+)", aufgabe)
    return m.group(1) if m else aufgabe


def pruefe(text: str, a: argparse.Namespace) -> tuple[list[tuple[str, str, str]], dict]:
    typ = TYPEN[a.typ]
    zeilen, summe_zeile = lies_uebersicht(text)
    befunde: list[tuple[str, str, str]] = []
    info: dict = {"zeilen": len(zeilen)}

    # Summe
    ohne = [z["aufgabe"] for z in zeilen if z["punkte"] is None]
    summe = sum(z["punkte"] for z in zeilen if z["punkte"] is not None)
    m = re.search(r"\b(?:Gesamtpunkte|Gesamt-?BE|Bewertungseinheiten(?:\s+gesamt)?|Gesamt)\W{0,3}\s*(\d+(?:[.,]\d+)?)\s*(?:BE|P\b|Punkte)",
                  text, re.I) or re.search(r"Gesamtpunkte\W{0,3}\s*(\d+(?:[.,]\d+)?)", text, re.I)
    gesamt = a.gesamt or (float(m.group(1).replace(",", ".")) if m else None) or summe
    info["gesamt"] = gesamt
    abw = []
    if ohne:
        abw.append("ohne Punkte: " + ", ".join(ohne))
    if summe_zeile is not None and abs(summe_zeile - summe) > 1e-6:
        abw.append(f"Σ-Zeile {_fmt(summe_zeile)} ≠ Summe der Zeilen {_fmt(summe)}")
    if abs(gesamt - summe) > 1e-6:
        abw.append(f"Gesamtpunkte {_fmt(gesamt)} ≠ Summe der Zeilen {_fmt(summe)}")
    halbe = [z["aufgabe"] for z in zeilen if z["punkte"] is not None and z["punkte"] % 1]
    einheit = "BE" if typ.get("einheit") == "BE" else "Punkte"
    text_summe = "; ".join(abw) if abw else f"{_fmt(summe)} {einheit}, stimmig"
    befunde.append(("Punktsumme", "❌" if abw else ("⚠" if halbe else "✅"),
                    text_summe + (f"; halbe Punkte bei {', '.join(halbe)} – möglichst vermeiden" if halbe else "")))

    # Doppelzählung Haupt- und Teilaufgaben
    nummern = [z["aufgabe"] for z in zeilen]
    doppelt = [n for n in nummern if re.fullmatch(r"[A-Za-z]*\s*\d+", n)
               and any(x != n and hauptnummer(x) == hauptnummer(n) for x in nummern)]
    if doppelt:
        befunde.append(("Zeilenstruktur", "❌", "Hauptaufgabe und Teilaufgaben gemeinsam gelistet (doppelt gezählt): "
                        + ", ".join(doppelt)))

    # Zeit und Takt
    m = re.search(r"Bearbeitungszeit\W{0,3}\s*(\d+)\s*Min", text, re.I)
    zeit = a.zeit or (float(m.group(1)) if m else None)
    info["zeit"] = zeit
    minuten = [z["min"] for z in zeilen if z["min"] is not None]
    if zeit and gesamt:
        takt = zeit / gesamt
        info["takt"] = round(takt, 2)
        status = "✅" if takt >= typ["takt_gut"] - 1e-9 else ("⚠" if takt >= typ["takt_min"] - 1e-9 else "❌")
        e = typ.get("einheit", "P")
        befunde.append(("Takt (Minuten je " + ("BE" if e == "BE" else "Punkt") + ")", status,
                        f"{_fmt(zeit)} min / {_fmt(gesamt)} {e} = {_fmt(round(takt, 2))} min/{e} (Richtwert ≥ {_fmt(typ['takt_gut'])}, "
                        f"Untergrenze {_fmt(typ['takt_min'])})"))
        if minuten:
            msum = sum(minuten)
            ok = msum <= zeit + 1e-9
            befunde.append(("Minutensumme", "✅" if ok else "❌",
                            f"Aufgaben {_fmt(msum)} min von {_fmt(zeit)} min Bearbeitungszeit"
                            + ("" if ok else " – Arbeit ist zu lang") + (f", Reserve {_fmt(zeit - msum)} min" if ok else "")))
    else:
        befunde.append(("Takt (Minuten je Punkt)", "⚠", "Bearbeitungszeit nicht erkannt (Angabe „Bearbeitungszeit: N min“ oder --zeit)"))

    # Umfang
    haupt = sorted({hauptnummer(z["aufgabe"]) for z in zeilen}, key=lambda s: (len(s), s))
    info["hauptaufgaben"] = len(haupt)
    grenze = a.max_aufgaben if a.max_aufgaben is not None else typ["max_aufgaben"]
    if grenze:
        befunde.append(("Anzahl Aufgaben", "✅" if len(haupt) <= grenze else "⚠",
                        f"{len(haupt)} Hauptaufgaben (Richtwert ≤ {grenze}; jede weitere ist ein Kontextwechsel)"))

    # AFB
    anteile, unklar = afb_anteile(zeilen)
    s = sum(anteile.values())
    soll = tuple(int(x) for x in a.afb.split("/")) if a.afb else typ["afb"]
    if s:
        proz = {k: 100 * v / s for k, v in anteile.items()}
        info["afb_punkte"] = {k: round(v, 2) for k, v in anteile.items()}
        info["afb_prozent"] = {k: round(v, 1) for k, v in proz.items()}
        aus = [k for k, z in zip(("I", "II", "III"), soll) if abs(proz[k] - z) > a.toleranz + 1e-9]
        kurz = "BE" if typ.get("einheit") == "BE" else "P"
        text_afb = " · ".join(f"AFB {k} {_fmt(round(anteile[k], 2))} {kurz} ({proz[k]:.0f} %)" for k in ("I", "II", "III"))
        text_afb += f"; Soll {soll[0]}/{soll[1]}/{soll[2]} ±{_fmt(a.toleranz)}"
        if aus:
            text_afb += f"; außerhalb: AFB {', '.join(aus)} – ändern oder im Erwartungshorizont begründen"
        if unklar:
            text_afb += f"; ohne AFB: {', '.join(unklar)}"
        bereiche = [z["aufgabe"] for z in zeilen if AFB_WERT.search(z["afb"] or "") and AFB_WERT.search(z["afb"]).group(2)]
        if bereiche:
            text_afb += f"; Bereichsangaben (je zur Hälfte gezählt) bei {', '.join(bereiche)} – in Prüfungen je Zeile einen AFB festlegen"
        befunde.append(("AFB-Verteilung", "⚠" if aus or unklar or bereiche else "✅", text_afb))
    else:
        befunde.append(("AFB-Verteilung", "❌", "keine AFB-Angaben in der Punkteübersicht"))

    # Schreiblast: Punkteanteil je Antwortformat (nur mit Spalte „Antwort“)
    if any(z["antwort"] is not None for z in zeilen):
        punkte = {name: 0.0 for name, _ in FORMATE}
        unbekannt = []
        for z in zeilen:
            f = antwort_format(z["antwort"])
            if f is None or z["punkte"] is None:
                unbekannt.append(z["aufgabe"])
            else:
                punkte[f] += z["punkte"]
        s_ant = sum(punkte.values())
        if s_ant:
            kurz = "BE" if typ.get("einheit") == "BE" else "P"
            proz_ant = {k: 100 * v / s_ant for k, v in punkte.items()}
            info["antwort_prozent"] = {k: round(v, 1) for k, v in proz_ant.items()}
            text_ant = " · ".join(f"{k} {_fmt(round(v, 2))} {kurz} ({proz_ant[k]:.0f} %)" for k, v in punkte.items() if v)
            text_ant += f"; Freitext Richtwert ≤ {_fmt(FREITEXT_GRENZE)} %"
            zu_viel = proz_ant["Text"] > FREITEXT_GRENZE + 1e-9
            if zu_viel:
                text_ant += " – Teil als Kurzantwort, Tabelle oder Skizze stellen oder im Erwartungshorizont begründen"
            if unbekannt:
                text_ant += f"; Format nicht erkannt: {', '.join(unbekannt)} (Kurz · Rechnung · Skizze · Text)"
            befunde.append(("Schreiblast (Freitextanteil)", "⚠" if zu_viel or unbekannt else "✅", text_ant))

    # Einstieg
    m0 = AFB_WERT.search(zeilen[0]["afb"] or "")
    if m0:
        nur3 = m0.group(1) == "III" and not m0.group(2)
        befunde.append(("Einstieg nicht AFB III", "❌" if nur3 else "✅", f"erste Zeile {zeilen[0]['aufgabe']}: AFB {zeilen[0]['afb']}"))

    # Bezug
    if any(z["bezug"] is not None for z in zeilen):
        ohne_bezug = [z["aufgabe"] for z in zeilen if not (z["bezug"] or "").strip("–- ")]
        befunde.append(("Bezug zu Lernsituation/Kompetenz", "⚠" if ohne_bezug else "✅",
                        "ohne Bezug: " + ", ".join(ohne_bezug) if ohne_bezug else "jede Zeile zugeordnet"))
    else:
        befunde.append(("Bezug zu Lernsituation/Kompetenz", "⚠", "Spalte „Bezug“ fehlt – Nachweis, dass Unterrichtetes geprüft wird"))

    # Single Choice
    if a.sc:
        buchst = [b for b in a.sc.upper() if b.isalpha()]
        optionen = [chr(ord("A") + i) for i in range(max(a.optionen, max(ord(b) - 64 for b in buchst)))]
        zaehl = Counter(buchst)
        werte = [zaehl.get(o, 0) for o in optionen]
        serie = max(len(m.group(0)) for m in re.finditer(r"(.)\1*", "".join(buchst)))
        gleich = max(werte) - min(werte) <= 1
        befunde.append(("Single Choice – Lösungsbuchstaben", "✅" if gleich and serie < 4 else "⚠",
                        " · ".join(f"{o} {zaehl.get(o, 0)}×" for o in optionen) + f" bei {len(buchst)} Fragen"
                        + ("" if gleich else " – ungleich verteilt, Zielbuchstaben vorgeben")
                        + (f"; längste Serie gleicher Buchstaben {serie}" if serie >= 4 else "")))
    return befunde, info


def ausgabe(befunde, info, a) -> str:
    art = {"klausur-bg": "Klausur", "lzk": "Lernzielkontrolle"}.get(a.typ, "Klassenarbeit")
    be = TYPEN[a.typ].get("einheit") == "BE"
    z = [f"# Selbstprüfung {art} (klausur_check)", "",
         "| Prüfpunkt | Ergebnis | Hinweis |", "|---|---|---|"]
    z += [f"| {p} | {s} | {h} |" for p, s, h in befunde]
    gesamt = info.get("gesamt")
    if gesamt:
        stufen = eigene_grenzen(a.grenzen) if a.grenzen else SCHLUESSEL[a.system]
        name = "eigene Grenzen" if a.grenzen else {"15": "15-Punkte-System", "ihk": "Kammer-Schlüssel 🔎"}[a.system]
        schritt = 1.0 if a.ganze_punkte else 0.5
        e_lang, e_kurz = ("BE", "BE") if be else ("Punkte", "P")
        z += ["", f"## Notenschlüssel ({name}, {_fmt(gesamt)} {e_lang}, Grenzen auf {_fmt(schritt)} {e_kurz} aufgerundet)", "",
              f"| Note | ab % | ab {e_lang} |", "|---|---|---|"]
        z += [f"| {lab} | {_fmt(p)} | {_fmt(ab)} |" for lab, p, ab in notenschluessel(gesamt, stufen, schritt)]
    if "afb_punkte" in info and all(float(v).is_integer() for v in info["afb_punkte"].values()):
        p = info["afb_punkte"]
        z += ["", "Zeile für die Begutachtung (in den Erwartungshorizont übernehmen):", "",
              f"    Gesamtsummen (AFB I, AFB II, AFB III, gesamt) {p['I']:.0f} {p['II']:.0f} {p['III']:.0f} {sum(p.values()):.0f}"]
    return "\n".join(z) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Selbstprüfung einer Klassenarbeit/Lernzielkontrolle (lokal).")
    p.add_argument("datei", type=Path, help="Erwartungshorizont (Markdown) mit Punkteübersicht")
    p.add_argument("--typ", choices=sorted(TYPEN), default="klassenarbeit")
    p.add_argument("--gesamt", type=float, default=None)
    p.add_argument("--zeit", type=float, default=None, help="Bearbeitungszeit in Minuten")
    p.add_argument("--afb", default=None, help="Soll in Prozent, z. B. 30/40/30")
    p.add_argument("--toleranz", type=float, default=10.0, help="Prozentpunkte (Standard 10)")
    p.add_argument("--max-aufgaben", type=int, default=None)
    p.add_argument("--system", choices=("15", "ihk"), default="15")
    p.add_argument("--grenzen", default=None, help="eigener Schlüssel Prozent:Note, z. B. 92:1,81:2,67:3,50:4,30:5,0:6")
    p.add_argument("--ganze-punkte", action="store_true", help="Grenzen auf ganze Punkte runden (Single Choice)")
    p.add_argument("--sc", default=None, help="Lösungsbuchstaben der Single-Choice-Fragen in Reihenfolge")
    p.add_argument("--optionen", type=int, default=5, help="Antwortoptionen je SC-Frage (Standard 5)")
    a = p.parse_args(argv)
    try:
        if a.afb and not re.fullmatch(r"\d+/\d+/\d+", a.afb):
            raise Eingabefehler("--afb im Format 30/40/30")
        text = a.datei.read_text(encoding="utf-8")
        befunde, info = pruefe(text, a)
        print(ausgabe(befunde, info, a), end="")
    except (Eingabefehler, OSError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2
    return 1 if any(s == "❌" for _, s, _ in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
