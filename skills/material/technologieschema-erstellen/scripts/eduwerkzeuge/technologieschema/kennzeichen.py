"""
kennzeichen — Referenzkennzeichen nach DIN EN IEC 81346-2:2020 (IEC 81346-2:2019).

Technologieschemata tragen **immer** Kennzeichen der aktuellen Ausgabe; die Ausgabe 2009 und freie
Hauskennzeichen (S1, Y1, B2) gibt es hier nicht. Geprüft wird:

* Form ``-`` + 1 bis 3 Großbuchstaben + Zählnummer, ohne Leerzeichen (``-S1``, ``-MM2``),
* Klasse und Unterklasse stehen in Tabelle 2 der Norm (A, I, O sind keine Klassen; D, J, L, V, Y, Z
  reserviert),
* Kennbuchstaben der Ausgabe 2009 (-SF, -RZ, Klasse A) sind veraltet,
* das Kennzeichen passt zur **Art des Bauteils** (ein Taster ist Klasse S, ein Sensor Klasse B),
* innerhalb einer Klasse gilt **eine** Tiefe: nicht -B1 neben -BG2 (Festlegung der Fachberatung,
  Notationsblatt der Skill-Bibliothek); eine Unterklasse nur, wenn die Klasse verschiedenartige
  Betriebsmittel enthält.

Die Tabelle der Unterklassen ist dieselbe wie in ``bmk_pruefen.py`` der Skill-Bibliothek (ein Test
dort vergleicht beide).
"""

from __future__ import annotations

import re

NORM = "DIN EN IEC 81346-2:2020"

#: Unterklassen je Klasse (IEC 81346-2:2019, Tabelle 2). A, I, O sind keine Klassen, D, J, L, V, Y, Z reserviert.
UNTERKLASSEN_2020 = {
    "B": "ABCDEFGHJKLMPQRSTUWXYZ", "C": "ABCFLMNPQ", "E": "ABCEGMPQTUV", "F": "ABCELMNQRS",
    "G": "ABCFLMPQR", "H": "JKLMPQRSUVWX", "K": "EFGHJZ", "M": "ABCDLMST", "N": "ABCDE",
    "P": "FGHJKLZ", "Q": "ABCMNPQRSZ", "R": "ABFLMNQU", "S": "FGHJKZ", "T": "ABCFLMPR",
    "U": "ABCLMNPQTU", "W": "BDEGHJLMPQRVZ", "X": "BDEGHKMNPSTZ",
}

#: Kennbuchstaben der Ausgabe 2009, die in der Ausgabe 2020 anders heißen
AUS_2009 = {"SF": "Taster und Schalter heißen -SJ (SF ist Gesichtserkennung)",
            "RZ": "das Drosselrückschlagventil heißt -RN"}

KLASSENNAMEN = {
    "B": "Information erfassen (Sensor, Geber)", "S": "menschliche Betätigung erfassen (Taster, Schalter)",
    "K": "Signale verarbeiten (SPS, Relais)", "Q": "Fluss steuern (Schütz, Wegeventil)",
    "M": "Antreiben (Motor, Zylinder, Ventilspule)", "P": "Information darstellen (Leuchtmelder, Hupe)",
    "R": "Begrenzen (Drossel, Widerstand, Diode)", "G": "Fluss erzeugen (Pumpe, Lüfter)",
    "T": "Umwandeln (Netzteil, Umrichter)", "F": "Schützen (Sicherung, Überlastrelais)",
    "E": "Aussenden (Leuchte, Heizung)", "C": "Speichern (Kondensator, Tank)",
    "X": "Verbinden (Klemme, Steckdose)", "W": "Leiten (Kabel, Leitung)",
}

#: erlaubte Klassen je Bauteilart (``typ`` der Spec bzw. Symbol-Klassen)
KLASSEN_JE_TYP = {
    "zylinder": "M", "motor": "M", "pumpe": "G", "ventil": "QRS", "sensor": "B", "taster": "S",
    "leuchte": "P", "ampel": "P", "behaelter": "C",
}
#: wenn eine Unterklasse genannt ist, muss sie zur Bauteilart passen (Zylinder: fluidisch, Motor: drehend …)
UNTERKLASSEN_JE_TYP = {
    "zylinder": "M", "motor": "AB", "pumpe": "PQ", "leuchte": "F", "ampel": "F",
}
_UNTER_ERKLAERUNG = {"zylinder": "-MM (fluidisch)", "motor": "-MA (drehend) oder -MB (linear)",
                     "pumpe": "-GP (Flüssigkeit) oder -GQ (Gas)", "leuchte": "-PF (Zustand sichtbar)",
                     "ampel": "-PF (Zustand sichtbar)"}

FORM = re.compile(r"^-([A-Z]{1,3})(\d+)$")
ALT_FORM = re.compile(r"^-?\s*([A-Za-z]{1,3})\s*(\d+)$")


def vorschlag(kennung: str) -> str | None:
    """Korrigierte Schreibweise (``S 1`` → ``-S1``), wenn nur die Form abweicht."""
    m = ALT_FORM.match(str(kennung).strip())
    return f"-{m.group(1).upper()}{m.group(2)}" if m else None


def pruefe(kennung: str, typ: str | None = None, klassen: str | None = None) -> list[str]:
    """Probleme eines einzelnen Kennzeichens (leere Liste = in Ordnung).

    ``klassen`` überschreibt die Klassen der Bauteilart (Symbole bringen ihre eigenen mit).
    """
    k = str(kennung)
    m = FORM.match(k)
    if not m:
        v = vorschlag(k)
        hinweis = f" – gemeint ist wohl '{v}'" if v else ""
        return [f"Kennzeichen '{k}' hat nicht die Form der {NORM} (Bindestrich, Kennbuchstaben, "
                f"Zählnummer ohne Leerzeichen, z. B. -S1 oder -MM2){hinweis}"]
    b = m.group(1)
    fehler: list[str] = []
    if b[0] in "IO":
        fehler.append(f"'{k}': {b[0]} ist keine Klasse")
    elif b[0] == "A":
        fehler.append(f"'{k}': Klasse A gibt es in der {NORM} nicht mehr (Ausgabe 2009)")
    elif b[0] not in UNTERKLASSEN_2020:
        fehler.append(f"'{k}': Klasse {b[0]} ist in der {NORM} reserviert")
    elif b[:2] in AUS_2009:
        fehler.append(f"'{k}': Kennbuchstaben der Ausgabe 2009 – {AUS_2009[b[:2]]}")
    elif len(b) > 1 and b[1] not in UNTERKLASSEN_2020[b[0]]:
        fehler.append(f"'{k}': {b[:2]} steht nicht in Tabelle 2 der {NORM}")
    if fehler:
        return fehler
    erlaubte = klassen or KLASSEN_JE_TYP.get(typ or "")
    if erlaubte and b[0] not in erlaubte:
        erlaubt = " oder ".join(f"-{c} ({KLASSENNAMEN.get(c, c)})" for c in erlaubte)
        return [f"'{k}': Klasse {b[0]} passt nicht zu '{typ}' – nach {NORM} gehört es in Klasse {erlaubt}"]
    if typ in UNTERKLASSEN_JE_TYP and len(b) > 1 and b[1] not in UNTERKLASSEN_JE_TYP[typ]:
        return [f"'{k}': Unterklasse {b[:2]} passt nicht zu '{typ}' – erwartet {_UNTER_ERKLAERUNG[typ]}"]
    return []


def tiefe_pruefen(kennungen: list[str]) -> tuple[list[str], list[str]]:
    """Tiefe je Klasse: (Fehler bei gemischter Tiefe, Hinweise auf kürzere Schreibweise).

    Nur für formal gültige Kennzeichen; ungültige meldet ``pruefe``.
    """
    buchstaben = {}
    for k in kennungen:
        m = FORM.match(str(k))
        if m:
            buchstaben[str(k)] = m.group(1)
    klassen: dict[str, list[str]] = {}
    for k, b in buchstaben.items():
        klassen.setdefault(b[0], []).append(k)
    fehler, hinweise = [], []
    for ks in klassen.values():
        tiefen = {len(buchstaben[k]) for k in ks}
        if len(tiefen) > 1:
            ks = sorted(ks, key=lambda k: len(buchstaben[k]))
            fehler.append(f"Klasse {buchstaben[ks[0]][0]}: gemischte Tiefe – {ks[0]} neben {ks[-1]}; innerhalb einer "
                          f"Klasse alle Kennzeichen gleich tief schreiben (verschiedenartige Betriebsmittel: überall "
                          f"Unterklasse, z. B. -MA1 und -MM1)")
            continue
        arten = {buchstaben[k] for k in ks}
        d = next(d for d in range(1, max(tiefen) + 1) if len({a[:d] for a in arten}) == len(arten))
        if d < max(tiefen):
            kurz = ", ".join(f"-{buchstaben[k][:d]}{buchstaben[k][len(buchstaben[k]):]}{k[len(buchstaben[k]) + 1:]}"
                             for k in ks)
            hinweise.append(f"Klasse {buchstaben[ks[0]][0]}: kürzer möglich, weil keine Unterscheidung nötig – "
                            f"{', '.join(ks)} → {kurz}")
    return fehler, hinweise
