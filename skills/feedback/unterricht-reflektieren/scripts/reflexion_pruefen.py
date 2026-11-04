#!/usr/bin/env python3
"""reflexion_pruefen – Unterrichtsreflexion prüfen und das Gerüst aus dem Entwurf erzeugen.

Prüft eine Reflexion nach assets/vorlage-reflexion.md (Markdown; DOCX/ODT/PDF über
text_lesen.py, falls vorhanden – Tabellen dann oft nicht erkennbar):

  Plan und Verlauf   Tabelle mit geplanten und tatsächlichen Minuten je Phase; Summen und
                     Abweichungen rechnet das Skript selbst. Ab --schwelle Minuten (Standard 5)
                     braucht eine Abweichung einen Grund (❌ ohne); eine Σ-Zeile oder Spalte
                     „Abweichung“, die nicht zur Rechnung passt, gibt ⚠️
  Zielerreichung     je Ziel ja · teilweise · nein · offen und ein beobachtbarer Beleg
                     (❌ ohne, ⚠️ bei bloßem Werturteil wie „gut“)
  Leitidee           Zeile „Leitidee: …“ in der Zielerreichung (⚠️ sonst – didaktische Leitidee
                     der Stunde eingelöst?)
  Schwerpunkte       1 bis 3 (❌ sonst)
  Alternativen       vorhanden (⚠️ sonst); Konsequenzen vorhanden (❌), mit Folgestunde (⚠️)
  Phasen             mindestens eine Phase der vollständigen Handlung genannt (⚠️)
  Keine Bewertung    Noten, Notenstufen, Niveaustufen A–E (❌)
  Datenschutz        Pseudonyme (S01), Initialen nach „Schüler/in“ o. Ä., E-Mail-Adressen (❌);
                     Gesundheits- und Förderangaben (⚠️ nur zusammenfassend, keiner Person zuordnen)
  Prüfungsrelevant   bei `pruefungsrelevant: true` Abschnitt „Kennzeichnung der KI-Nutzung“
                     ausgefüllt und kein Modus B (❌)
  Pflichtabschnitte  Qualitätscheck, Annahmen und Prüfaufträge, Übergabe, Transparenzzeile (❌)

Gerüst: --geruest ENTWURF liest den Verlaufsplan eines Entwurfs (Zeitspalte „00–08“, „8'“ oder
„8 min“; Phase fett bzw. vor „–“) und gibt die Tabelle „Plan und Verlauf“ mit den geplanten
Minuten aus – die tatsächlichen trägt die Lehrkraft ein.

Aufruf:
    python3 reflexion_pruefen.py 36_reflexion_….md [--schwelle 5] [--json]
    python3 reflexion_pruefen.py --geruest 30_unterrichtsentwurf_….md

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
Die Prüfung findet Formfehler; ob die Reflexion inhaltlich trägt, beurteilt die Lehrkraft.
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

PHASEN_VH = ("Informieren", "Analysieren", "Planen", "Entscheiden", "Durchführen", "Überprüfen",
             "Kontrollieren", "Reflektieren")
ERREICHT = ("ja", "teilweise", "nein", "offen")
PLATZHALTER = re.compile(r"^(?:|…|\.\.\.|-|–|—|\?|\[[^\]]*\]|ja · teilweise · nein · offen)$")
VAGE = re.compile(r"^(?:sehr\s+)?(?:gut|super|prima|toll|ok(?:ay)?|passt|gelungen|klappte|lief\s+gut|positiv|"
                  r"schlecht|nicht\s+gut|motiviert|die\s+SuS\s+waren\s+motiviert)\W*$", re.IGNORECASE)
# „als gut bewertet“ kann eine Peer-Einschätzung der Lernenden sein – nur Notensprache zählt.
NOTEN = re.compile(r"\bNote\s*(?:[1-6](?:[,.]\d)?|sehr\s+gut|gut|befriedigend|ausreichend|mangelhaft|ungenügend)\b"
                   r"|\bNotenvorschlag|\bStufe\s+[A-E]\b|\bNiveaustufe\s+[A-E1-5]\b"
                   r"|\bmit\s+(?:sehr\s+gut|gut|befriedigend|ausreichend|mangelhaft|ungenügend)\s+(?:bewertet|benotet|beurteilt)"
                   r"|\bals\s+(?:befriedigend|ausreichend|mangelhaft|ungenügend)\s+(?:bewertet|benotet|eingestuft|beurteilt)",
                   re.IGNORECASE)
PSEUDONYM = re.compile(r"\bS\d{2,3}\b")
INITIALE = re.compile(r"\b(?:Schüler(?:in)?|Azubi|Auszubildende[rn]?|Lernende[rn]?|Teilnehmer(?:in)?)\s+"
                      r"[A-ZÄÖÜ]\.(?=[\s,;:)]|$)")
MAIL = re.compile(r"[\w.+-]+@([\w-]+\.)+[A-Za-z]{2,}")
BEISPIEL_DOMAIN = re.compile(r"@example\.(?:org|com|net)\b", re.IGNORECASE)
FOERDER = re.compile(r"\b(?:ADHS|Legasthenie|LRS|Dyskalkulie|Autismus|Asperger|Förderschwerpunkt\w*|"
                     r"Nachteilsausgleich\w*|Attest\w*)\b")
FOLGESTUNDE = re.compile(r"Folgestunde|nächste[nr]?\s+(?:Stunde|Doppelstunde|Sitzung)|Folgesequenz|"
                         r"Folge-?\s*Doppelstunde|in\s+der\s+Stunde\s+\d", re.IGNORECASE)
ZEITSPANNE = re.compile(r"^\s*(\d{1,3})\s*[–\-]\s*(\d{1,3})\s*(?:min|['’])?\s*$")
UHRZEIT = re.compile(r"^\s*(\d{1,2})[:.](\d{2})\s*[–\-]\s*(\d{1,2})[:.](\d{2})\s*(?:Uhr)?\s*$")


# ─────────────────────────────── Lesehilfen ───────────────────────────────

def ohne_kopf_und_kommentare(text: str) -> str:
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.DOTALL)
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def kopf(text: str) -> dict[str, str]:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    werte: dict[str, str] = {}
    if m:
        for z in m.group(1).splitlines():
            k, _, v = z.partition(":")
            if k.strip() and not k.startswith(" "):
                werte[k.strip()] = v.split("#")[0].strip().strip('"\'')
    return werte


def abschnitt(text: str, titel: str) -> str | None:
    """Text unter der ersten Überschrift, die (nach optionaler Nummer) mit titel beginnt."""
    zeilen = text.splitlines()
    for i, z in enumerate(zeilen):
        m = re.match(rf"^(#+)\s+(?:R?\d+\s+)?{titel}", z, re.IGNORECASE)
        if m:
            ebene = len(m.group(1))
            teil = []
            for w in zeilen[i + 1:]:
                n = re.match(r"^(#+)\s", w)
                if n and len(n.group(1)) <= ebene:
                    break
                teil.append(w)
            return "\n".join(teil)
    return None


def _zellen(z: str) -> list[str]:
    return [c.strip() for c in z.strip().strip("|").split("|")]


def tabelle(teil: str | None) -> tuple[list[str], list[list[str]]]:
    """Erste Markdown-Tabelle: (Kopf, Zeilen) ohne Trennzeile."""
    if not teil:
        return [], []
    zeilen = [z for z in teil.splitlines() if z.strip().startswith("|")]
    zeilen = [z for z in zeilen if not re.fullmatch(r"\s*\|?[\s:|\-]+\|?\s*", z)]
    if not zeilen:
        return [], []
    return [c.lower() for c in _zellen(zeilen[0])], [_zellen(z) for z in zeilen[1:]]


def spalte(kopfzeile: list[str], *namen: str) -> int | None:
    for i, c in enumerate(kopfzeile):
        if any(n in c for n in namen):
            return i
    return None


def leer(zelle: str | None) -> bool:
    return zelle is None or bool(PLATZHALTER.match(zelle.strip().strip("*_").strip()))


def minuten(zelle: str | None) -> int | None:
    """„8“, „8 min“, „8'“, „≈ 12“, „00–08“ (Spanne) → Minuten; „entfallen“ → 0; leer → None."""
    if zelle is None:
        return None
    z = zelle.strip().strip("*").strip()
    if re.search(r"entfall|ausgefallen|gestrichen", z, re.IGNORECASE):
        return 0
    m = UHRZEIT.match(z)
    if m:
        h1, m1, h2, m2 = (int(g) for g in m.groups())
        return (h2 * 60 + m2) - (h1 * 60 + m1)
    m = ZEITSPANNE.match(z)
    if m:
        return int(m.group(2)) - int(m.group(1))
    m = re.search(r"\d{1,3}", z)
    return int(m.group(0)) if m else None


def _vorzeichenzahl(zelle: str) -> int | None:
    m = re.search(r"([+−\-]?)\s*(\d{1,3})", zelle)
    if not m:
        return None
    wert = int(m.group(2))
    return -wert if m.group(1) in ("−", "-") else wert


def _listenpunkte(teil: str | None) -> list[str]:
    if not teil:
        return []
    punkte = []
    for z in teil.splitlines():
        m = re.match(r"^\s*(?:\d+[.)]|[-*])\s+(.*)$", z)
        if m and not leer(m.group(1)) and not re.fullmatch(r"\[.*\]\s*[–-]?.*…?", m.group(1)):
            punkte.append(m.group(1))
    return punkte


def _inhalt(teil: str | None) -> bool:
    """Abschnitt hat Inhalt über Platzhalter hinaus: Etiketten („**Folgestunde:**“, „Alternative:“),
    [Platzhalter] und „…“ zählen nicht."""
    if not teil:
        return False
    for z in teil.splitlines():
        rest = re.sub(r"^\s*(?:\d+[.)]|[-*])\s+", "", z)
        rest = re.sub(r"\*\*[^*]+\*\*", "", rest)
        rest = re.sub(r"\[[^\]]*\]", "", rest).replace("…", "")
        rest = re.sub(r"[\wäöüÄÖÜß\-]+:", "", rest)
        rest = re.sub(r"\b(?:weil|und|oder)\b", "", rest)
        rest = re.sub(r"[\s–\-:·*|]+", " ", rest).strip()
        if len(rest) >= 12:
            return True
    return False


# ─────────────────────────────── Prüfung ───────────────────────────────

def zeitabgleich(text: str, schwelle: int = 5) -> dict:
    kopfzeile, zeilen = tabelle(abschnitt(text, r"Plan\s+und\s+Verlauf"))
    erg = {"gefunden": bool(kopfzeile), "phasen": [], "summe_geplant": 0, "summe_tatsaechlich": 0,
           "ohne_grund": [], "ohne_istzeit": [], "abweichung_falsch": [], "summenzeile_falsch": []}
    if not kopfzeile:
        return erg
    i_ph = spalte(kopfzeile, "phase") or 0
    i_plan = spalte(kopfzeile, "geplant", "plan")
    i_ist = spalte(kopfzeile, "tatsächlich", "ist")
    i_abw = spalte(kopfzeile, "abweich", "differenz")
    i_grund = spalte(kopfzeile, "grund")
    if i_plan is None or i_ist is None:
        erg["gefunden"] = False
        return erg
    summenzeilen = []
    for z in zeilen:
        z = z + [""] * (len(kopfzeile) - len(z))
        name = z[i_ph].strip("* ")
        if re.match(r"^(?:Σ|Summe|gesamt)\b", name, re.IGNORECASE):
            summenzeilen.append(z)
            continue
        plan, ist = minuten(z[i_plan]), minuten(z[i_ist])
        if plan is None and ist is None:
            continue
        erg["phasen"].append({"phase": name, "geplant": plan, "tatsaechlich": ist})
        erg["summe_geplant"] += plan or 0
        if ist is None:
            erg["ohne_istzeit"].append(name)
            continue
        erg["summe_tatsaechlich"] += ist
        delta = ist - (plan or 0)
        erg["phasen"][-1]["abweichung"] = delta
        if i_abw is not None and not leer(z[i_abw]):
            angegeben = _vorzeichenzahl(z[i_abw])
            if angegeben is not None and angegeben != delta and not (angegeben == abs(delta) and "+" not in z[i_abw]
                                                                   and delta > 0):
                erg["abweichung_falsch"].append(f"{name} ({z[i_abw]} statt {delta:+d})")
        if abs(delta) >= schwelle and (i_grund is None or leer(z[i_grund])):
            erg["ohne_grund"].append(f"{name} ({delta:+d} min)")
    for z in summenzeilen:
        z = z + [""] * (len(kopfzeile) - len(z))
        for idx, soll, label in ((i_plan, erg["summe_geplant"], "geplant"),
                                 (i_ist, erg["summe_tatsaechlich"], "tatsächlich")):
            angegeben = minuten(z[idx])
            if angegeben is not None and angegeben != soll and not (label == "tatsächlich" and erg["ohne_istzeit"]):
                erg["summenzeile_falsch"].append(f"Σ {label} {angegeben} statt {soll}")
    return erg


def pruefe(text: str, schwelle: int = 5) -> dict:
    k = kopf(text)
    rumpf = ohne_kopf_und_kommentare(text)
    befunde: list[tuple[str, str, str]] = []

    def add(kriterium: str, ergebnis: str, hinweis: str) -> None:
        befunde.append((kriterium, ergebnis, hinweis))

    # Kopf
    if k.get("artefakt", "").lower().startswith("unterrichtsreflexion") and k.get("skill") == "unterricht-reflektieren":
        add("Kopf", "✅", f"Anlass: {k.get('anlass') or '–'} · Modus: {k.get('modus') or '–'}")
    else:
        add("Kopf", "⚠️", "artefakt „Unterrichtsreflexion“ und skill „unterricht-reflektieren“ im YAML-Kopf angeben")

    # Plan und Verlauf
    z = zeitabgleich(rumpf, schwelle)
    if not z["gefunden"]:
        add("Plan und Verlauf", "❌", "Tabelle mit Spalten „geplant“ und „tatsächlich“ unter „Plan und Verlauf“ fehlt")
    elif not z["phasen"]:
        add("Plan und Verlauf", "❌", "keine Phase mit Minuten eingetragen")
    else:
        diff = z["summe_tatsaechlich"] - z["summe_geplant"]
        info = (f"{len(z['phasen'])} Phasen · geplant Σ {z['summe_geplant']} min · tatsächlich "
                f"Σ {z['summe_tatsaechlich']} min ({f'{diff:+d}' if diff else '0'})")
        if z["ohne_grund"]:
            add("Plan und Verlauf", "❌", info + " – Abweichung ohne Grund: " + ", ".join(z["ohne_grund"]))
        elif z["ohne_istzeit"]:
            add("Plan und Verlauf", "⚠️", info + " – tatsächliche Minuten fehlen: " + ", ".join(z["ohne_istzeit"]))
        else:
            add("Plan und Verlauf", "✅", info)
        if z["abweichung_falsch"] or z["summenzeile_falsch"]:
            add("Rechnung", "⚠️", "passt nicht zur Rechnung: " + ", ".join(z["abweichung_falsch"] + z["summenzeile_falsch"]))

    # Zielerreichung
    kopfzeile, zeilen = tabelle(abschnitt(rumpf, r"Zielerreichung"))
    i_ziel, i_err, i_bel = (spalte(kopfzeile, "ziel"), spalte(kopfzeile, "erreicht"), spalte(kopfzeile, "beleg"))
    if not kopfzeile or None in (i_ziel, i_err, i_bel):
        add("Zielerreichung", "❌", "Tabelle mit Spalten „Ziel“, „erreicht“, „Beleg“ fehlt")
    else:
        ziele = [r + [""] * (len(kopfzeile) - len(r)) for r in zeilen]
        ziele = [r for r in ziele if not leer(r[i_ziel])
                 and not re.fullmatch(r"(?:FK|PK|Leitidee):\s*…?", r[i_ziel].strip())]
        ohne_beleg = [r[i_ziel][:40] for r in ziele if leer(r[i_bel])]
        vage = [r[i_bel] for r in ziele if not leer(r[i_bel]) and VAGE.match(r[i_bel].strip())]
        unklar = [r[i_ziel][:40] for r in ziele if not r[i_err].strip("*_ ").lower().startswith(ERREICHT)]
        if not ziele:
            add("Zielerreichung", "❌", "kein Ziel eingetragen")
        elif ohne_beleg:
            add("Zielerreichung", "❌", "Ziel ohne beobachtbaren Beleg: " + "; ".join(ohne_beleg))
        elif vage or unklar:
            teile = []
            if vage:
                teile.append("Beleg ist ein Werturteil, keine Beobachtung: " + ", ".join(f"„{v}“" for v in vage))
            if unklar:
                teile.append("„erreicht“ mit ja · teilweise · nein · offen angeben: " + "; ".join(unklar))
            add("Zielerreichung", "⚠️", " – ".join(teile))
        else:
            n_ziele = sum(not re.match(r"(?:\*\*)?Leitidee", r[i_ziel]) for r in ziele)
            add("Zielerreichung", "✅", f"{n_ziele} Ziele mit Beleg")
        # Didaktische Leitidee (Planungshilfe der Bibliothek): eingelöst? – Zeile in der Zielerreichung
        if any(re.match(r"(?:\*\*)?Leitidee", r[i_ziel]) for r in ziele):
            add("Leitidee", "✅", "Einlösung der Leitidee mit Beleg eingeschätzt")
        elif re.search(r"Leitidee", rumpf):
            add("Leitidee", "⚠️", "Leitidee genannt, aber nicht in der Zielerreichung eingeschätzt (Zeile „Leitidee: …“)")
        else:
            add("Leitidee", "⚠️", "Leitidee nicht aufgegriffen – eingelöst? Fehlt sie im Entwurf, nachträglich festhalten")

    # Schwerpunkte
    punkte = _listenpunkte(abschnitt(rumpf, r"Schwerpunkte"))
    if not punkte:
        add("Schwerpunkte", "❌", "keine Schwerpunkte benannt (1–3)")
    elif len(punkte) > 3:
        add("Schwerpunkte", "❌", f"{len(punkte)} Schwerpunkte – höchstens drei, die übrigen in die Abschnitte")
    else:
        add("Schwerpunkte", "✅", f"{len(punkte)} Schwerpunkt(e)")

    # Alternativen und Konsequenzen
    add("Alternativen", "✅" if _inhalt(abschnitt(rumpf, r"Alternativen")) else "⚠️",
        "begründete Alternative vorhanden" if _inhalt(abschnitt(rumpf, r"Alternativen"))
        else "mindestens eine begründete Alternative zu einem Schwerpunkt nennen")
    kons = abschnitt(rumpf, r"Konsequenzen")
    if not _inhalt(kons):
        add("Konsequenzen", "❌", "Konsequenzen fehlen (Folgestunde, Lernsituation, eigene Entwicklung)")
    elif not any(FOLGESTUNDE.search(z) and _inhalt(z) for z in (kons or "").splitlines()):
        add("Konsequenzen", "⚠️", "keine Konsequenz für die Folgestunde erkennbar")
    else:
        add("Konsequenzen", "✅", "mit Folgestunde")

    # Phasen der vollständigen Handlung
    genannt = [p for p in PHASEN_VH if re.search(rf"\b{p}", rumpf)]
    add("Vollständige Handlung", "✅" if genannt else "⚠️",
        ("genannt: " + ", ".join(genannt)) if genannt else "keine Phase der vollständigen Handlung genannt (SchuCu-BBS 2024)")

    # Keine Bewertung
    noten = sorted({m.group(0) for m in NOTEN.finditer(rumpf)})
    add("Keine Note, keine Stufe", "❌" if noten else "✅",
        ("streichen: " + ", ".join(f"„{n}“" for n in noten)) if noten else "keine Noten oder Niveaustufen")

    # Datenschutz
    treffer = sorted({m.group(0) for m in PSEUDONYM.finditer(rumpf)} | {m.group(0) for m in INITIALE.finditer(rumpf)}
                     | {m.group(0) for m in MAIL.finditer(rumpf) if not BEISPIEL_DOMAIN.search(m.group(0))})
    foerder = sorted({m.group(0) for m in FOERDER.finditer(rumpf)})
    if treffer:
        add("Datenschutz", "❌", f"{len(treffer)} Personenbezug(e) (Pseudonym, Initiale oder E-Mail) – auf Lerngruppe "
                                "bzw. Anzahlen umstellen")
    elif foerder:
        add("Datenschutz", "⚠️", "Gesundheits- bzw. Förderangaben (" + ", ".join(foerder)
            + ") – nur zusammenfassend, keiner Person zuordnen")
    else:
        add("Datenschutz", "✅", "keine Personenbezüge erkannt (heuristisch)")

    # Prüfungsrelevant
    if k.get("pruefungsrelevant", "").lower() in ("true", "ja", "yes"):
        kenn = abschnitt(rumpf, r"Kennzeichnung\s+der\s+KI-Nutzung")
        fehler = []
        if not kenn or re.search(r"\[KI-System\]|\[TT\.MM\.JJJJ\]", kenn) or "Hilfsmittel" not in kenn:
            fehler.append("Abschnitt „Kennzeichnung der KI-Nutzung“ ausfüllen (KI-System, Datum)")
        if k.get("modus", "").strip().upper().startswith("B"):
            fehler.append("bei Prüfungsunterricht nur Modus A (eigene Vorbereitung), keine KI-vorbereitete Nachbesprechung")
        add("Prüfungsrelevant", "❌" if fehler else "✅", "; ".join(fehler) or "gekennzeichnet, Modus A")

    # Pflichtabschnitte
    fehlend = [t for t, muster in (("Qualitätscheck", r"Qualitätscheck"),
                                   ("Annahmen und Prüfaufträge", r"Annahmen\s+und\s+Prüfaufträge"),
                                   ("Übergabe", r"Übergabe")) if abschnitt(rumpf, muster) is None]
    if not re.search(r"^>\s*KI-gestützt", rumpf, re.MULTILINE):
        fehlend.append("Transparenzzeile")
    add("Pflichtabschnitte", "❌" if fehlend else "✅", ("fehlt: " + ", ".join(fehlend)) if fehlend else "vollständig")

    return {"befunde": befunde, "zeit": z, "fehler": sum(b[1] == "❌" for b in befunde),
            "warnungen": sum(b[1] == "⚠️" for b in befunde)}


def markdown(erg: dict) -> str:
    z = ["### Prüfung Unterrichtsreflexion (Form – keine Bewertung)", "",
         "| Kriterium | Ergebnis | Hinweis |", "|---|---|---|"]
    z += [f"| {k} | {e} | {h.replace('|', '/')} |" for k, e, h in erg["befunde"]]
    phasen = erg["zeit"].get("phasen") or []
    if phasen:
        z += ["", "| Phase | geplant | tatsächlich | Abweichung |", "|---|---|---|---|"]
        for p in phasen:
            ab = p.get("abweichung")
            z.append(f"| {p['phase']} | {p['geplant'] if p['geplant'] is not None else '–'} | "
                     f"{p['tatsaechlich'] if p['tatsaechlich'] is not None else '–'} | "
                     f"{(f'{ab:+d}' if ab else '0') if ab is not None else '–'} |")
    z += ["", f"Ergebnis: {erg['fehler']} ❌ · {erg['warnungen']} ⚠️ – Formprüfung; ob die Reflexion trägt, "
              "entscheidet die Lehrkraft."]
    return "\n".join(z)


# ─────────────────────────────── Gerüst ───────────────────────────────

def geruest(entwurf: str) -> str:
    """Tabelle „Plan und Verlauf“ aus dem Verlaufsplan eines Entwurfs (geplante Minuten)."""
    zeilen = []
    kopf_ist_zeit = False     # nur Tabellen, deren erste Kopfzelle „Zeit“ heißt (nicht die Stundenübersicht)
    in_tabelle = False
    for z in entwurf.splitlines():
        if not z.strip().startswith("|"):
            in_tabelle = False
            continue
        if re.fullmatch(r"\s*\|?[\s:|\-]+\|?\s*", z):
            continue
        c = _zellen(z)
        if not in_tabelle:
            in_tabelle = True
            kopf_ist_zeit = bool(re.match(r"^(?:\*\*)?(?:Zeit|Uhrzeit|min)", c[0], re.IGNORECASE))
            continue
        if not kopf_ist_zeit or len(c) < 2:
            continue
        zeit = c[0].strip("* ")
        if re.match(r"^(?:Σ|Summe)", zeit):
            continue
        m = (UHRZEIT.match(zeit) or ZEITSPANNE.match(zeit)
             or re.fullmatch(r"(\d{1,3})\s*(?:min|['’])?", zeit))
        if not m:
            continue
        dauer = minuten(zeit)
        fett = re.search(r"\*\*([^*]+)\*\*", c[1])
        phase = (fett.group(1) if fett else re.split(r"\s+[–-]\s+", c[1])[0])[:40].strip()
        zeilen.append((phase or "Phase", dauer))
    if not zeilen:
        raise ValueError("kein Verlaufsplan mit Zeitspalte gefunden (z. B. „| 00–08 | **Einstieg** – … |“)")
    aus = ["| Phase | geplant (min) | tatsächlich (min) | Abweichung | Grund | Wirkung auf das Lernen |",
           "|---|---|---|---|---|---|"]
    aus += [f"| {p} | {d} | | | | |" for p, d in zeilen]
    aus.append(f"| Σ | {sum(d or 0 for _, d in zeilen)} | | | | |")
    return "\n".join(aus)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Unterrichtsreflexion prüfen bzw. Gerüst aus dem Entwurf erzeugen.")
    p.add_argument("datei", type=Path, nargs="?", help="Reflexion (36_reflexion_….md)")
    p.add_argument("--geruest", type=Path, metavar="ENTWURF", help="Tabelle „Plan und Verlauf“ aus dem Entwurf")
    p.add_argument("--schwelle", type=int, default=5, help="Minuten, ab denen eine Abweichung einen Grund braucht")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    try:
        if a.geruest:
            print(geruest(lies_text(a.geruest)))
            return 0
        if not a.datei:
            p.error("Reflexion oder --geruest ENTWURF angeben")
        erg = pruefe(lies_text(a.datei), a.schwelle)
    except (OSError, ValueError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps(erg, ensure_ascii=False, indent=2))
    else:
        print(markdown(erg))
    return 1 if erg["fehler"] else 0


if __name__ == "__main__":
    sys.exit(main())
