#!/usr/bin/env python3
"""lernakte_pruefen – Selbstprüfung einer Lernakte (agiles Lernen mit KI, lokal, deterministisch).

Prüft eine Lernakte nach assets/vorlage-lernakte.md:

  Kopf         artefakt, titel, start, termin; Termin nach dem Start
  Kickoff      sechs Fragen beantwortet, ohne Platzhalter; Ziel als Können (kein verstehen/kennen/
               wissen/lernen), mit Nachweis
  Zeit         Sprintanzahl passt in den Zeithorizont (Sprintlänge aus Frage 3); Lernzeit je
               Sprint nicht über dem Budget
  Rollen       Fachexpertin benannt
  Quellen      nur öffentliche Quellen (❌ bei „nein", intern, vertraulich); mindestens eine
  Freigabe     „Freigabe Lernpfad: erteilt – KÜRZEL, Datum", spätestens sobald ein Review vorliegt
  Sprints      Sprintziel mit Operator, Zeit, Quellen mit Q-Nummer bzw. Fundstelle, Review-Wert;
               „nicht erreicht/teilweise" → Wiederholungsrunde oder begründet weiter
  Retro        ausgefüllt, wenn alle Sprints durch sind bzw. status abgeschlossen
  Datenschutz  keine E-Mail-Adressen (außer Beispiel-Domains), keine Telefonnummern
  Vertrag      Pflichtabschnitte und Transparenzhinweis

Aufruf:
    python3 lernakte_pruefen.py LERNAKTE.md [--heute JJJJ-MM-TT] [--json]

Exit 0 = keine ❌ (⚠ möglich), 1 = mindestens ein ❌, 2 = Eingabefehler.
Nur Python-Standardbibliothek. Prüft Struktur, nicht die fachliche Richtigkeit – die bleibt bei
Lernenden und Fachexpertin.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import math
import re
import sys
from pathlib import Path

VERBOTEN = re.compile(r"\b(verstehen|verstanden|versteh\w*|kennen|kenne|kennt|wissen|weiß|lernen|"
                      r"vertraut\s+machen|bewusst\s+sein|begreifen|einen\s+überblick)\b", re.I)
PLATZHALTER = re.compile(r"\[[^\]\n]*\](?!\()|…|\.\.\.")  # [Platzhalter], nicht [Link](url)
REVIEW_WERTE = ("nicht erreicht", "teilweise", "erreicht", "offen")
ENTSCHEIDUNGEN = ("wiederholung", "weiter", "fachexpert", "abbruch")
FREIGABE = re.compile(r"Freigabe\s+Lernpfad\s*:\s*\**\s*erteilt\s*\**\s*[-–—]\s*"
                      r"(?P<kuerzel>[A-Za-zÄÖÜäöüß]{1,6})\s*,\s*"
                      r"(?P<datum>\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{2,4})", re.I)
MAIL = re.compile(r"[\w.+-]+@([\w-]+\.)+[a-z]{2,}", re.I)
BEISPIEL_DOMAINS = ("example.org", "example.com", "example.net", "example.de")
TELEFON = re.compile(r"(?<![\w.])(?:\+49|0)[\s/-]?\d{2,5}[\s/-]?\d{3,}(?:[\s-]?\d+)*")
PFLICHT = ("Qualitätscheck", "Annahmen und Prüfaufträge", "Übergabe")
NICHT_OEFFENTLICH = re.compile(r"\b(nein|intern|vertraulich|nicht öffentlich|nur dienstlich)\b", re.I)


class Eingabefehler(Exception):
    pass


# ─────────────────────────────── Lesen ───────────────────────────────

def kopf(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    daten = {}
    for zeile in m.group(1).splitlines():
        if ":" not in zeile or zeile.lstrip().startswith("#"):
            continue
        k, _, v = zeile.partition(":")
        v = v.strip()
        if v.startswith('"'):
            v = v[1:].split('"', 1)[0]
        else:
            v = v.split(" #", 1)[0].strip()
        daten[k.strip()] = v
    return daten, m.group(2)


def abschnitte(rumpf: str, ebene: int = 2) -> dict[str, str]:
    """Überschrift (ohne #) → Inhalt bis zur nächsten Überschrift derselben oder höheren Ebene."""
    muster = re.compile(rf"^(#{{1,{ebene}}})\s+(.*)$", re.MULTILINE)
    treffer = list(muster.finditer(rumpf))
    ergebnis: dict[str, str] = {}
    for i, m in enumerate(treffer):
        if len(m.group(1)) != ebene:
            continue
        ende = treffer[i + 1].start() if i + 1 < len(treffer) else len(rumpf)
        ergebnis[m.group(2).strip()] = rumpf[m.end():ende]
    return ergebnis


def finde(abschn: dict[str, str], wort: str) -> tuple[str, str] | None:
    for titel, inhalt in abschn.items():
        if titel.lower().startswith(wort.lower()):
            return titel, inhalt
    return None


def tabellenzeilen(inhalt: str) -> list[list[str]]:
    zeilen = []
    for z in inhalt.splitlines():
        s = z.strip()
        if not s.startswith("|") or re.match(r"^\|?\s*:?-{2,}", s):
            continue
        zeilen.append([c.strip() for c in s.strip("|").split("|")])
    return zeilen[1:] if zeilen else []


def datum(wert: str) -> dt.date | None:
    wert = (wert or "").strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y"):
        try:
            return dt.datetime.strptime(wert, fmt).date()
        except ValueError:
            continue
    return None


def felder(inhalt: str) -> dict[str, str]:
    """- **Feld:** Wert → {feld: wert} (Feldname klein)."""
    ergebnis = {}
    for m in re.finditer(r"^\s*[-*]\s*\*\*([^*:]+):?\*\*:?\s*(.*)$", inhalt, re.MULTILINE):
        ergebnis[m.group(1).strip().lower()] = m.group(2).strip()
    return ergebnis


def stunden(text: str) -> float | None:
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(h|std|stunde|stunden)\b", text, re.I)
    if m:
        return float(m.group(1).replace(",", "."))
    m = re.search(r"(\d+(?:[.,]\d+)?)\s*(min|minuten)\b", text, re.I)
    if m:
        return float(m.group(1).replace(",", ".")) / 60
    return None


def sprinttage(text: str) -> int | None:
    m = re.search(r"(\d+|eine?|zwei|drei|vier)\s*(woche|wochen|tag|tage)\b", text, re.I)
    if not m:
        return None
    zahl = {"ein": 1, "eine": 1, "zwei": 2, "drei": 3, "vier": 4}.get(m.group(1).lower())
    n = zahl if zahl else int(m.group(1))
    return n * 7 if m.group(2).lower().startswith("woche") else n


def review_wert(text: str) -> str | None:
    t = text.lower()
    for w in REVIEW_WERTE:
        if t.startswith(w):
            return w
    return None


# ─────────────────────────────── Prüfen ───────────────────────────────

def pruefe(text: str, heute: dt.date | None = None) -> tuple[list[tuple[str, str, str]], dict]:
    befunde: list[tuple[str, str, str]] = []

    def b(bereich: str, stufe: str, meldung: str) -> None:
        befunde.append((bereich, stufe, meldung))

    k, rumpf = kopf(text)
    abschn = abschnitte(rumpf)
    info: dict = {"titel": k.get("titel", ""), "status": k.get("status", "")}

    # Kopf
    if not k:
        b("Kopf", "❌", "kein YAML-Kopf (--- … ---)")
    for feld in ("artefakt", "titel", "start", "termin"):
        if k and not k.get(feld):
            b("Kopf", "❌" if feld in ("termin", "titel") else "⚠", f"Kopffeld „{feld}“ fehlt")
    start, termin = datum(k.get("start", "")), datum(k.get("termin", ""))
    if k.get("termin") and not termin:
        b("Kopf", "❌", f"Termin „{k.get('termin')}“ ist kein Datum (JJJJ-MM-TT)")
    if start and termin and termin <= start:
        b("Kopf", "❌", "Termin liegt nicht nach dem Start")

    # Kickoff
    kick = finde(abschn, "Kickoff")
    antworten: dict[int, str] = {}
    if not kick:
        b("Kickoff", "❌", "Abschnitt „## Kickoff“ fehlt")
    else:
        for zeile in tabellenzeilen(kick[1]):
            m = re.match(r"^\**\s*(\d)\b", zeile[0]) if zeile else None
            if m and len(zeile) > 1:
                antworten[int(m.group(1))] = zeile[1]
        for nr in range(1, 7):
            if nr not in antworten:
                b("Kickoff", "❌", f"Kickoff-Frage {nr} fehlt")
            elif not antworten[nr].strip() or PLATZHALTER.search(antworten[nr]):
                b("Kickoff", "⚠", f"Kickoff-Frage {nr} unbeantwortet oder mit Platzhalter")
        ziel = antworten.get(1, "")
        if ziel:
            if VERBOTEN.search(ziel):
                b("Ziel", "⚠", f"Ziel nicht beobachtbar formuliert („{VERBOTEN.search(ziel).group(0)}“) – als Können mit Operator")
            if not re.search(r"nachweis|woran|belegt|gezeigt|zeigen", ziel, re.I):
                b("Ziel", "⚠", "Ziel ohne Nachweis („…, nachweisbar durch …“)")

    # Zeit
    sprints_abschn = finde(abschn, "Lernpfad")
    sprints: list[tuple[str, dict[str, str]]] = []
    if sprints_abschn:
        for titel, inhalt in abschnitte(sprints_abschn[1], 3).items():
            if titel.lower().startswith("sprint"):
                sprints.append((titel, felder(inhalt)))
    info["sprints"] = len(sprints)
    tage = sprinttage(antworten.get(3, ""))
    budget = stunden(antworten.get(3, ""))
    if start and termin and tage:
        verfuegbar = math.floor((termin - start).days / tage)
        info["sprints_verfuegbar"] = verfuegbar
        if len(sprints) > verfuegbar:
            b("Zeit", "⚠", f"{len(sprints)} Sprints geplant, Zeithorizont reicht für {verfuegbar} "
                           f"(Sprintlänge {tage} Tage)")
        elif sprints and len(sprints) == verfuegbar:
            b("Zeit", "⚠", "kein Puffer für eine Wiederholungsrunde")
    elif antworten.get(3) and not tage:
        b("Zeit", "⚠", "Sprintlänge in Frage 3 nicht erkennbar (z. B. „1 Woche“)")

    # Rollen
    rollen = finde(abschn, "Rollen")
    fach = None
    if rollen:
        for zeile in tabellenzeilen(rollen[1]):
            if zeile and re.search(r"fachexpert", zeile[0], re.I):
                fach = zeile[1] if len(zeile) > 1 else ""
    if not fach or PLATZHALTER.fullmatch(fach.strip() or "[]"):
        b("Rollen", "⚠", "Fachexpertin nicht benannt – beim Lernen mit KI die wichtigste Rolle")

    # Quellen
    quellen = finde(abschn, "Quellen")
    qnummern: set[str] = set()
    if not quellen:
        b("Quellen", "⚠", "Abschnitt „## Quellen“ fehlt")
    else:
        zeilen = tabellenzeilen(quellen[1])
        kopfzeile = next((z for z in quellen[1].splitlines() if z.strip().startswith("|")), "")
        spalten = [c.strip().lower() for c in kopfzeile.strip().strip("|").split("|")]
        oeff = next((i for i, s in enumerate(spalten) if "öffentlich" in s), None)
        for zeile in zeilen:
            if not zeile or not zeile[0]:
                continue
            qnummern.add(zeile[0].strip("* "))
            if PLATZHALTER.search(" ".join(zeile[:2])):
                b("Quellen", "⚠", f"{zeile[0]}: Quelle mit Platzhalter")
            if oeff is not None and oeff < len(zeile):
                wert = zeile[oeff]
                if NICHT_OEFFENTLICH.search(wert):
                    b("Quellen", "❌", f"{zeile[0]}: nicht öffentlich – gehört nicht in KI-Quellen")
                elif not re.search(r"\bja\b|frei|cc", wert, re.I):
                    b("Quellen", "⚠", f"{zeile[0]}: öffentlich? unklar („{wert}“)")
        if not zeilen:
            b("Quellen", "⚠", "keine Quelle gebunden – die KI braucht Fundstellen")
        if oeff is None and zeilen:
            b("Quellen", "⚠", "Spalte „öffentlich“ fehlt")

    # Sprints
    if not sprints:
        b("Lernpfad", "❌", "keine Sprints (### Sprint n – …) im Abschnitt „## Lernpfad“")
    begonnen = False
    for i, (titel, f) in enumerate(sprints):
        ziel = f.get("sprintziel", "")
        if not ziel:
            b(titel, "❌", "Sprintziel fehlt")
        elif PLATZHALTER.search(ziel):
            b(titel, "⚠", "Sprintziel mit Platzhalter")
        elif VERBOTEN.search(ziel):
            b(titel, "⚠", f"Sprintziel nicht beobachtbar („{VERBOTEN.search(ziel).group(0)}“)")
        zeit = stunden(f.get("zeit", ""))
        if f.get("zeit") is None:
            b(titel, "⚠", "Zeit fehlt")
        elif budget and zeit and zeit > budget + 1e-9:
            b(titel, "⚠", f"{zeit:g} h über dem Budget von {budget:g} h je Sprint")
        q = f.get("quellen", "")
        if not q:
            b(titel, "⚠", "keine Quellen genannt")
        elif not re.search(r"\bQ\d+|S\.\s*\d|Seite|Kap|Abschn|§", q):
            b(titel, "⚠", "Quellen ohne Q-Nummer oder Fundstelle")
        else:
            for nr in re.findall(r"\bQ\d+\b", q):
                if qnummern and nr not in qnummern:
                    b(titel, "⚠", f"{nr} steht nicht in der Quellentabelle")
        rv = f.get("review")
        wert = review_wert(rv or "")
        if rv is None:
            b(titel, "⚠", "Review-Feld fehlt")
        elif wert is None:
            b(titel, "❌", f"Review „{rv}“ – erlaubt: erreicht | teilweise | nicht erreicht | offen")
        if wert and wert != "offen":
            begonnen = True
            ent = (f.get("entscheidung") or "").lower()
            if not ent.startswith(ENTSCHEIDUNGEN):
                b(titel, "⚠", "Review ohne Entscheidung (weiter | Wiederholung | Fachexpertin)")
            if wert in ("nicht erreicht", "teilweise") and ent.startswith("weiter") and "weil" not in ent and "begründ" not in ent:
                b(titel, "⚠", f"Ziel {wert}, trotzdem weiter – Begründung ergänzen oder Wiederholungsrunde")
            if ent.startswith("wiederholung"):
                folge = sprints[i + 1][0].lower() if i + 1 < len(sprints) else ""
                if not re.search(r"wiederhol|runde", folge):
                    b(titel, "⚠", "Wiederholung beschlossen, aber kein Folgesprint als Wiederholungsrunde")
    info["reviews"] = sum(1 for _, f in sprints if review_wert(f.get("review", "")) not in (None, "offen"))
    info["erreicht"] = sum(1 for _, f in sprints if review_wert(f.get("review", "")) == "erreicht")

    # Freigabe Lernpfad
    fm = FREIGABE.search(rumpf)
    info["freigabe"] = f"{fm['kuerzel']}, {fm['datum']}" if fm else ""
    if not fm:
        if begonnen:
            b("Freigabe", "⚠", "Sprints laufen, aber der Lernpfad ist nicht von der Fachexpertin gegengecheckt "
                               "(Freigabe Lernpfad: erteilt – KÜRZEL, Datum)")
        elif not re.search(r"Freigabe\s+Lernpfad\s*:", rumpf, re.I):
            b("Freigabe", "⚠", "Zeile „Freigabe Lernpfad: ausstehend“ fehlt")

    # Retro
    retro = finde(abschn, "Retro")
    alle_durch = bool(sprints) and all(review_wert(f.get("review", "")) not in (None, "offen") for _, f in sprints)
    abgeschlossen = "abgeschlossen" in k.get("status", "").lower()
    if alle_durch or abgeschlossen:
        gefuellt = [z for z in tabellenzeilen(retro[1]) if len(z) > 1 and z[1].strip()] if retro else []
        if len(gefuellt) < 3:
            b("Retro", "⚠", "alle Sprints durch – Retro ausfüllen (mind. was trug, was nicht, welche Quelle)")
    if termin and heute and heute > termin and not abgeschlossen:
        b("Zeit", "⚠", f"Termin {termin.isoformat()} ist überschritten – Retro oder neuer Termin")

    # Datenschutz
    for m in MAIL.finditer(rumpf):
        if not m.group(0).lower().endswith(BEISPIEL_DOMAINS):
            b("Datenschutz", "❌", "E-Mail-Adresse in der Lernakte – entfernen")
            break
    if TELEFON.search(rumpf):
        b("Datenschutz", "⚠", "mögliche Telefonnummer in der Lernakte")

    # Skill-Vertrag
    for p in PFLICHT:
        if not finde(abschn, p):
            b("Vertrag", "⚠", f"Pflichtabschnitt „## {p}“ fehlt")
    if not re.search(r"KI-gestützt erstellt", rumpf):
        b("Vertrag", "⚠", "Transparenzhinweis fehlt")

    return befunde, info


def naechster_schritt(info: dict, befunde: list) -> str:
    if any(s == "❌" for _, s, _ in befunde):
        return "❌ beheben"
    if not info.get("freigabe"):
        return "Lernpfad der Fachexpertin zeigen (Freigabe Lernpfad)"
    if info.get("sprints") and info.get("reviews", 0) < info["sprints"]:
        return f"Sprint {info['reviews'] + 1} bearbeiten, danach Review"
    if "abgeschlossen" not in info.get("status", "").lower():
        return "Retro durchführen und Ergebnis ablegen"
    return "abgeschlossen"


def ausgabe(befunde: list, info: dict) -> str:
    z = [f"Lernakte: {info.get('titel') or '–'}",
         f"Sprints: {info.get('sprints', 0)} geplant"
         + (f" (Zeithorizont reicht für {info['sprints_verfuegbar']})" if "sprints_verfuegbar" in info else "")
         + f" · Reviews: {info.get('reviews', 0)} · erreicht: {info.get('erreicht', 0)}"
         + f" · Freigabe Lernpfad: {info.get('freigabe') or 'ausstehend'}"]
    if not befunde:
        z.append("✅ keine Befunde")
    for bereich, stufe, meldung in sorted(befunde, key=lambda x: (x[1] != "❌", x[0])):
        z.append(f"{stufe} {bereich}: {meldung}")
    fehler = sum(s == "❌" for _, s, _ in befunde)
    warn = sum(s == "⚠" for _, s, _ in befunde)
    z.append(f"Ergebnis: {fehler} ❌ · {warn} ⚠ · nächster Schritt: {naechster_schritt(info, befunde)}")
    return "\n".join(z) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Lernakte (agiles Lernen mit KI) prüfen.")
    p.add_argument("datei", type=Path)
    p.add_argument("--heute", default=None, help="Stichtag JJJJ-MM-TT (Standard: heute)")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    try:
        heute = datum(a.heute) if a.heute else dt.date.today()
        if a.heute and not heute:
            raise Eingabefehler("--heute im Format JJJJ-MM-TT")
        befunde, info = pruefe(a.datei.read_text(encoding="utf-8"), heute)
    except (Eingabefehler, OSError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({"info": info, "befunde": [{"bereich": b, "stufe": s, "meldung": m}
                                                     for b, s, m in befunde],
                          "naechster_schritt": naechster_schritt(info, befunde)},
                         ensure_ascii=False, indent=2))
    else:
        print(ausgabe(befunde, info), end="")
    return 1 if any(s == "❌" for _, s, _ in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
