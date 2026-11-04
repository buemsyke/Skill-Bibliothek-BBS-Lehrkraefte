#!/usr/bin/env python3
"""lektion_pruefen – Lektionen (lessons/NN_slug/lesson.md) gegen das Lektionsmuster prüfen.

Sucht je Lektion die Elemente aus `lektionsmuster.md`: Selbsteinschätzung vor dem Start,
Eingangsfrage mit Vorhersage und Abgleich, Zugang bzw. Lehrkraftinput, Bewertungskasten und
KI-Hinweis vor der ersten Aufgabe (mit Punktsumme), Phase Entscheiden mit zwei Varianten,
eigenem Kriterium und Protokoll, Realitätstest, Rückmeldung mit Überarbeitung, Lernweg,
Stolperstein-Tabelle, verdeckte Schwierigkeit im Lehrerteil, Zeitplanung, Kernweg,
Lehrkraftinput-Phase und Länge des Schülerteils (ohne Code).

Eine Lernsituation kann mehrere Lektionen umfassen (Kopf: `lernsituation: "<Name>"` und
`teil: "k/n"`). Dann gelten die Elemente der Lernsituation nur dort, wo sie hingehören
(Auftakt: Vor dem Start, Bewertung, KI · Abschluss: Realitätstest, Rückmeldung, Lernweg ·
irgendwo: Eingangsfrage, Entscheiden, verdeckte Schwierigkeit), und das Skript prüft zusätzlich,
ob der Handlungskreis in der Lernsituation geschlossen ist. Lektionen ohne `lernsituation`
sind je eine eigene Lernsituation und werden wie bisher geprüft.

Das ist **keine Bewertung** – das Skript sucht Signalwörter. „Nicht gefunden“ heißt „von Hand
nachsehen“. Nur Python-Standardbibliothek; `--projekt` liest phase_config.yaml mit PyYAML,
falls installiert.

Aufruf:
    python3 lektion_pruefen.py LESSON.md… [--max-woerter 1500] [--loesungen DIR]
                               [--projekt DIR] [--json]

    --loesungen DIR  Lösungsdateien (Name beginnt mit der Lektionsnummer, enthält „loesung“):
                     Die Summe im Bewertungskasten muss dort als Summe vorkommen.
    --projekt DIR    Kursprojekt: jede H1 muss in phase_config.yaml einer Phase zugeordnet
                     oder ausgeschlossen sein – sonst fällt sie still aus der Schülerausgabe.
    --json           Ausgabe {"lektionen": […], "lernsituationen": […]}

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌ („–“ zählt nicht), 2 = Eingabefehler.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PFLICHT_H1 = [
    "Voraussetzungen und Kompetenzen", "Fachwissen", "Handlungssituation", "Material",
    "Hilfestellungen", "Vertiefungen", "Kompetenzcheck", "Aufgaben zur Wiederholung und Übung",
    "Lösungen / Handlungsergebnisse", "Didaktische Hinweise",
]
LEHRER = re.compile(r"Lösung|Didaktisch|Erwartungshorizont|Lehrkr", re.I)
KOMMENTAR = re.compile(r"<!--.*?-->", re.S)       # umfasst auch KI-KENNZEICHNUNG-Blöcke
CODEBLOCK = re.compile(r"(?ms)^[ \t]*(```|~~~)[^\n]*\n.*?^[ \t]*\1[ \t]*$")
WORT = re.compile(r"[0-9A-Za-zÄÖÜäöüß]+(?:[-’'][0-9A-Za-zÄÖÜäöüß]+)*")
AUFGABE = re.compile(r"^\s{0,3}(\d+)\.\s", re.M)
PHASE_KOPF = re.compile(r"(?m)^#{2,4} Phase[^\n]*$")
INPUT_KOPF = re.compile(r"Lehrkraftinput|fachsystematisch", re.I)
KERNWEG_MAX = 65 / 90                              # Anteil der Dauer (Richtwert 60–65 min je 90 min)
INPUT_MAX = 20                                     # Minuten am Stück

# Befunde, die zur Lernsituation statt zur einzelnen Lektion gehören: Rolle → Nummern
ANKER_ERSTE = {2, 5, 6}                            # Auftakt
ANKER_LETZTE = {8, 9, 10}                          # Abschluss
ANKER_IRGENDWO = {3, 7, 12}                        # in irgendeiner Lektion der Lernsituation


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    m = re.match(r"\A---\n(.*?)\n---\n?", text, re.S)
    if not m:
        return {}, text
    felder = {}
    for zeile in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_]+):\s*(.*)$", zeile)
        if km:
            felder[km.group(1)] = km.group(2).split(" #")[0].strip().strip('"')
    return felder, text[m.end():]


def abschnitte(rumpf: str) -> dict[str, str]:
    """H1-Überschrift → Inhalt; H1 in Code-Blöcken zählen nicht."""
    teile: dict[str, list[str]] = {}
    aktuell, im_code = None, False
    for zeile in rumpf.splitlines():
        if zeile.lstrip().startswith(("```", "~~~")):
            im_code = not im_code
        if not im_code and re.match(r"^# \S", zeile):
            aktuell = zeile[2:].strip()
            teile.setdefault(aktuell, [])
            continue
        if aktuell is not None:
            teile[aktuell].append(zeile)
    return {k: "\n".join(v) for k, v in teile.items()}


def ohne_code(text: str) -> tuple[str, int]:
    """Text ohne Code-Blöcke und Anzahl der Codezeilen darin (ohne Zaunzeilen)."""
    zeilen = 0
    for m in CODEBLOCK.finditer(text):
        zeilen += max(m.group(0).count("\n") - 1, 0)
    return CODEBLOCK.sub("", text), zeilen


def woerter(text: str) -> int:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = ohne_code(text)[0]
    text = re.sub(r"\]\([^)]*\)", "]", text)          # Linkziele nicht mitzählen
    return len(WORT.findall(text))


def kasten(text: str, titel: str) -> re.Match | None:
    """Admonition (!!! bzw. ???) mit passendem Titel samt eingerücktem Inhalt."""
    return re.search(rf'(?m)^[!?]{{3}}\+? *\w+ *"[^"\n]*(?:{titel})[^"\n]*"\n((?:[ \t]+.*\n|\s*\n)*)', text)


def zellen(zeile: str) -> list[str] | None:
    if not re.match(r"^\s*\|.*\|\s*$", zeile) or re.match(r"^\s*\|[\s:|-]+\|\s*$", zeile):
        return None
    return [c.strip().strip("*").strip() for c in zeile.strip().strip("|").split("|")]


SUMME = re.compile(r"^(?:Summe|Gesamt|Σ)", re.I)


def punkte(inhalt: str) -> tuple[list[int], int | None]:
    """Punktspalte = letzte Zelle; Summenzeile = erste Zelle beginnt mit Summe/Gesamt/Σ."""
    zeilen, summe = [], None
    for z in inhalt.splitlines():
        c = zellen(z)
        if not c or len(c) < 2 or not re.fullmatch(r"\d+", c[-1]):
            continue
        if SUMME.match(c[0]):
            summe = int(c[-1])
        else:
            zeilen.append(int(c[-1]))
    return zeilen, summe


def befund(liste, nr, name, stufe, hinweis=""):
    liste.append({"nr": nr, "element": name, "stufe": stufe, "hinweis": hinweis})


def phase_config(projekt: Path) -> tuple[set[str], set[str]] | str:
    pfad = projekt / "scripts" / "phase_config.yaml"
    if not pfad.is_file():
        return "scripts/phase_config.yaml fehlt"
    try:
        import yaml  # type: ignore
    except ImportError:
        return "PyYAML fehlt – Zuordnung der H1 nicht geprüft"
    cfg = yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}
    zugeordnet = {s for ph in (cfg.get("phases") or []) for s in (ph.get("sections") or [])}
    return zugeordnet, set(cfg.get("excluded_sections") or [])


def loesungssummen(ordner: Path, nummer: str, ordnername: str = "") -> list[int] | None:
    """Summen der Lösungsdatei; bevorzugt <Lektionsordner>_loesungen.md, sonst NN_*loesung*.md."""
    if not nummer:
        return None
    kandidaten = [ordner / f"{ordnername}_loesungen.md"] if ordnername else []
    kandidaten += sorted(ordner.glob(f"{nummer}_*.md"))
    for datei in kandidaten:
        if not datei.is_file():
            continue
        if "loesung" in datei.name.lower() or "lösung" in datei.name.lower():
            t = datei.read_text(encoding="utf-8", errors="ignore")
            return [int(c[-1]) for z in t.splitlines()
                    if (c := zellen(z)) and len(c) >= 2 and SUMME.match(c[0]) and re.fullmatch(r"\d+", c[-1])]
    return None


def minuten(text: str) -> int | None:
    """Größte Minutenangabe im Text („ca. 15 min“, „60–65 min“ → 65); sonst None."""
    werte = [int(b or a) for a, b in re.findall(r"(\d+)(?:\s*[–-]\s*(\d+))?\s*min", text)]
    return max(werte) if werte else None


def zeitplanung_text(lehrer: str) -> str | None:
    """Text des Spiegelstrichs **Zeitplanung** samt eingerückter Folgezeilen."""
    m = re.search(r"(?m)^[ \t]*-[ \t]*\*\*Zeitplanung\*\*:?[ \t]*(.*)$", lehrer)
    if not m:
        return None
    teile = [m.group(1)]
    for zeile in lehrer[m.end():].splitlines()[1:]:
        if not zeile.strip() or re.match(r"^[ \t]*-[ \t]", zeile) or not zeile.startswith((" ", "\t")):
            break
        teile.append(zeile.strip())
    return " ".join(t for t in teile if t)


def zeitsumme(text: str) -> int:
    """Summe der Minuten einer Zeitplanung; Klammern mit „Σ“ oder Minutenangabe zählen nicht."""
    text = re.sub(r"\([^()]*(?:Σ|min)[^()]*\)", " ", text)
    return sum(int(x) for x in re.findall(r"(\d+)\s*min", text))


def pruefe(pfad: Path, max_woerter: int = 1500, loesungen: Path | None = None,
           cfg: tuple[set[str], set[str]] | str | None = None) -> dict:
    text = KOMMENTAR.sub("", pfad.read_text(encoding="utf-8"))
    fm, rumpf = frontmatter(text)
    ab = abschnitte(rumpf)
    schueler = {k: v for k, v in ab.items() if not LEHRER.search(k)}
    lehrer = "\n".join(v for k, v in ab.items() if LEHRER.search(k))
    hs = ab.get("Handlungssituation", "")
    fw = ab.get("Fachwissen", "")
    vk = ab.get("Voraussetzungen und Kompetenzen", "")
    # erste Aufgabe: nummerierte Zeile, sonst erste ###-Überschrift unter den Arbeitsaufträgen
    erste = AUFGABE.search(hs) or re.search(r"(?m)^### ", hs)
    erste_pos = erste.start() if erste else 0
    b: list[dict] = []
    el: dict[str, bool] = {}

    fehlend = [h for h in PFLICHT_H1 if h not in ab]
    befund(b, 1, "H1-Überschriften", "⚠" if fehlend else "✅",
           ("fehlt: " + ", ".join(fehlend)) if fehlend else "")
    if isinstance(cfg, tuple):
        zugeordnet, ausgeschlossen = cfg
        still = [h for h in ab if h not in zugeordnet and h not in ausgeschlossen]
        befund(b, 1, "H1 in phase_config.yaml", "❌" if still else "✅",
               ("fällt still weg: " + ", ".join(still)) if still else "")
    elif isinstance(cfg, str):
        befund(b, 1, "H1 in phase_config.yaml", "⚠", cfg)

    start = bool(re.search(r"Vor dem Start|Selbsteinschätzung|kann ich schon", vk + fw[:400]))
    el["vorstart"] = start
    befund(b, 2, "Vor dem Start (Selbsteinschätzung)", "✅" if start else "⚠",
           "" if start else "Markierung der Kompetenzen am Anfang fehlt")

    vorher = re.search(r"[Ss]ag\w* \**vorher|Vorhersage|vorhersag", fw)
    abgleich = re.search(r"Abgleich|Auflösung", fw)
    el["eingang"] = bool(vorher and abgleich)
    befund(b, 3, "Eingangsfrage mit Vorhersage",
           "✅" if vorher and abgleich else "⚠",
           "" if vorher and abgleich else ("Abgleich fehlt" if vorher else "keine Vorhersage im Fachwissen"))

    phasen_koepfe = PHASE_KOPF.findall(hs)
    # Lehrkraftinput: als Phase unter den Arbeitsaufträgen oder als Abschnitt im Fachwissen
    input_koepfe = [k for k in phasen_koepfe if INPUT_KOPF.search(k)]
    input_im_fw = [k for k in re.findall(r"(?m)^#{2,4} [^\n]*$", fw) if INPUT_KOPF.search(k)]
    zugang_min = [int(x) for x in re.findall(r"\((\d+)\s*min\)", fw[fw.find("Zug"):])] if re.search(r"Zug[aä]ng", fw) else []
    if re.search(r"Zug[aä]ng", fw):
        befund(b, 4, "Zugang zum Fachwissen", "✅",
               f"{len(zugang_min)} Zugänge zur Wahl" if len(zugang_min) > 1 else "ein Zugang")
    elif input_koepfe or input_im_fw or re.search(r"Lehrkraftinput|Live-Coding|Screencast", fw):
        befund(b, 4, "Zugang zum Fachwissen", "✅", "Lehrkraftinput")
    else:
        befund(b, 4, "Zugang zum Fachwissen", "✅", "Fachwissen ohne ausgewiesenen Zugang")

    bew = kasten(hs, "bewert|Bewert")
    if not bew:
        befund(b, 5, "Bewertung vor Arbeitsbeginn", "❌", "kein Kasten „So wird bewertet“ unter Handlungssituation")
        summe = None
        el["bewertung"] = False
    else:
        el["bewertung"] = True
        vor = bew.start() < erste_pos
        zeilen, summe = punkte(bew.group(1))
        if summe is None and zeilen:
            summe = sum(zeilen)
        stimmt = not zeilen or summe == sum(zeilen)
        hinweis = []
        if not vor:
            hinweis.append("steht nach der ersten Aufgabe")
        if not stimmt:
            hinweis.append(f"Summe {summe} ≠ Zeilen {sum(zeilen)}")
        befund(b, 5, "Bewertung vor Arbeitsbeginn", "✅" if vor and stimmt else "❌",
               "; ".join(hinweis) or (f"Σ {summe} P." if summe else ""))
        if loesungen is not None and summe:
            sums = loesungssummen(loesungen, fm.get("lesson_id", "") or pfad.parent.name[:2], pfad.parent.name)
            if sums is None:
                befund(b, 5, "Summe im Feinraster", "⚠", "keine Lösungsdatei gefunden")
            elif not sums:
                befund(b, 5, "Summe im Feinraster", "⚠", "keine Summenzeile in der Lösungsdatei – von Hand abgleichen")
            else:
                befund(b, 5, "Summe im Feinraster", "✅" if summe in sums else "❌",
                       "" if summe in sums else f"Kasten {summe}, Lösung {sums}")

    ki = kasten(hs, "KI")
    el["ki"] = bool(ki)
    befund(b, 6, "KI-Hinweis vor Arbeitsbeginn",
           "✅" if ki and ki.start() < erste_pos else "⚠",
           "" if ki and ki.start() < erste_pos else ("steht nach der ersten Aufgabe" if ki else "kein Kasten zu KI-Werkzeugen"))

    ent = re.search(r"(?ms)^#{2,4} [^\n]*Entscheid[^\n]*\n(.*?)(?=^#{2,4} |\Z)", hs)
    el["entscheiden"] = bool(ent)
    if not ent:
        befund(b, 7, "Phase Entscheiden", "❌", "keine Überschrift mit „Entscheiden“ in den Arbeitsaufträgen")
    else:
        e = ent.group(1)
        fehlt = []
        # Varianten stehen oft schon in Phase 1 – deshalb in allen Arbeitsaufträgen suchen
        if not (re.search(r"\*\*A\b|Variante A|\bA\s*[–-]", hs) and re.search(r"\*\*B\b|Variante B|\bB\s*[–-]", hs)):
            fehlt.append("zwei Varianten A/B")
        if not re.search(r"eigene[sn]? Kriteri|euer Kriteri|eure[sn]? (?:eigenes )?Kriteri", e):
            fehlt.append("eigenes Kriterium")
        if not re.search(r"Verworfen|Entscheidungsprotokoll|Ausschlag|halte\w* \w* ?fest|fest:", e):
            fehlt.append("Protokoll")
        befund(b, 7, "Phase Entscheiden", "⚠" if fehlt else "✅", ("fehlt: " + ", ".join(fehlt)) if fehlt else "")

    nach = hs[erste_pos:]
    real = re.search(r"Realitätstest|an der Wirklichkeit|\(a\)[^\n]*\n?[^\n]*\(b\)", nach)
    el["realitaet"] = bool(real)
    befund(b, 8, "Realitätstest der Entscheidung", "✅" if real else "⚠",
           "" if real else "keine Überprüfung der Entscheidung an konkreten Fällen gefunden")

    rueck = re.search(r"Rückmeldung|Feedback", nach)
    ueber = re.search(r"überarbeit", nach, re.I)
    el["rueckmeldung"] = bool(rueck and ueber)
    befund(b, 9, "Rückmeldung mit Überarbeitung", "✅" if rueck and ueber else "⚠",
           "" if rueck and ueber else ("Überarbeitung fehlt" if rueck else "keine Rückmeldung"))

    lern = re.search(r"Lernweg|Reflexion|reflektier|Markierungen vom Anfang|Was k(?:annst\s+du|önnen\s+Sie)\s+jetzt", nach)
    el["lernweg"] = bool(lern)
    befund(b, 10, "Reflektieren (Lernweg)", "✅" if lern else "❌",
           "" if lern else "keine Reflexion in den Arbeitsaufträgen")

    hi = ab.get("Hilfestellungen", "")
    st = re.search(r"Stolperstein", hi)
    tab = len(re.findall(r"(?m)^\s*\|(?!\s*-)[^\n]*\|[^\n]*\|[^\n]*\|\s*$", hi[st.start():] if st else ""))
    befund(b, 11, "Stolperstein-Tabelle", "✅" if st and tab >= 3 else "⚠",
           "" if st and tab >= 3 else "Tabelle Symptom → Ursache → Vorgehen fehlt")

    vd = re.search(r"[Vv]erdeckte Schwierigkeit", lehrer)
    verraten = [k for k, v in schueler.items() if re.search(r"[Vv]erdeckte Schwierigkeit", v)]
    el["verdeckt"] = bool(vd)
    stufe = "✅" if vd and not verraten else "⚠"
    hinweis = "" if vd else "nicht in den Didaktischen Hinweisen beschrieben"
    if verraten:
        hinweis = (hinweis + "; " if hinweis else "") + "im Schülerteil erwähnt: " + ", ".join(verraten)
    befund(b, 12, "Verdeckte Schwierigkeit (Lehrerteil)", stufe, hinweis)

    dm = re.search(r"\d+", fm.get("duration", "90"))
    dauer = int(dm.group()) if dm else 90
    phasen = [int(x) for x in re.findall(r"(?m)^#{2,4} Phase[^\n]*?(\d+)\s*min", hs)]
    zp_text = zeitplanung_text(lehrer)
    zeit_hinweis, zeit_stufe = [], "✅"
    if zp_text is not None:
        z = zeitsumme(zp_text)
        if z and z != dauer:
            zeit_stufe = "⚠"
            zeit_hinweis.append(f"Zeitplanung Σ {z} min ≠ Dauer {dauer} min")
        if re.search(r"Zug[aä]ng", fw) and not re.search(r"Zug[aä]ng|Selbstlern|vorbereit", zp_text):
            zeit_stufe = "⚠"
            zeit_hinweis.append("Zeit der Zugänge nicht ausgewiesen")
    elif phasen:
        if sum(phasen) > dauer:
            zeit_stufe = "⚠"
            zeit_hinweis.append(f"Phasen Σ {sum(phasen)} min > Dauer {dauer} min")
        zeit_hinweis.append("keine Zeitplanung im Lehrerteil")
        zeit_stufe = "⚠"
    else:
        zeit_stufe = "⚠"
        zeit_hinweis.append("keine Zeitangaben gefunden")
    if phasen and zugang_min and sum(phasen) + min(zugang_min) > dauer:
        zeit_stufe = "⚠"
        zeit_hinweis.append(f"Phasen {sum(phasen)} min + kürzester Zugang {min(zugang_min)} min > Dauer {dauer} min")
    if phasen:
        zeit_hinweis.insert(0, f"Phasen {'+'.join(map(str, phasen))} = {sum(phasen)} min")
    befund(b, 13, "Zeitplanung", zeit_stufe, "; ".join(zeit_hinweis))

    schueler_text = {k: v for k, v in schueler.items()}
    w_schueler = sum(woerter(v) for v in schueler_text.values())
    w_fach = woerter(fw)
    codezeilen = sum(ohne_code(v)[1] for v in schueler_text.values())
    befund(b, 14, "Länge des Schülerteils (ohne Code)", "✅" if w_schueler <= max_woerter else "⚠",
           f"{w_schueler} Wörter (Fachwissen {w_fach}), {codezeilen} Codezeilen"
           + ("" if w_schueler <= max_woerter else f" > {max_woerter}"))

    km = re.search(r"\*\*Kernweg\*\*:?[ \t]*([^\n]*)", lehrer)
    kernweg = minuten(km.group(1)) if km else None
    if kernweg is None:
        befund(b, 15, "Kernweg", "⚠", "kein Kernweg in den Didaktischen Hinweisen ausgewiesen")
    elif kernweg > dauer * KERNWEG_MAX + 0.5:
        befund(b, 15, "Kernweg", "⚠", f"{kernweg} min > {round(dauer * KERNWEG_MAX)} min (Richtwert 60–65 je 90)")
    else:
        befund(b, 15, "Kernweg", "✅", f"{kernweg} min")

    if not (input_koepfe or input_im_fw):
        befund(b, 16, "Lehrkraftinput (fachsystematische Phase)", "✅", "keine Input-Phase")
    else:
        probleme = []
        pos = {k: i for i, k in enumerate(phasen_koepfe)}
        abschn = re.split(PHASE_KOPF, hs)[1:]            # Inhalt nach jeder Phasenüberschrift
        for kopf in input_koepfe + input_im_fw:
            dauer_input = minuten(kopf)
            if dauer_input is not None and dauer_input > INPUT_MAX:
                probleme.append(f"{dauer_input} min am Stück > {INPUT_MAX} min")
            if kopf in pos:                               # Phase unter den Arbeitsaufträgen
                i = pos[kopf]
                folge = abschn[i + 1] if i + 1 < len(abschn) else ""
                if not (AUFGABE.search(abschn[i]) or AUFGABE.search(folge)):
                    probleme.append("keine Aufgabe zur Anwendung danach")
            elif not AUFGABE.search(hs):                  # Abschnitt im Fachwissen
                probleme.append("keine Aufgabe zur Anwendung danach")
        bm = re.search(r"\*\*Fachsystematische Phase\*\*:?[ \t]*([^\n]*)", lehrer)
        if not (bm and len(bm.group(1).strip()) >= 10):
            probleme.append("keine Begründung (**Fachsystematische Phase**) in den Didaktischen Hinweisen")
        befund(b, 16, "Lehrkraftinput (fachsystematische Phase)", "⚠" if probleme else "✅",
               "; ".join(probleme) if probleme else f"{len(input_koepfe) + len(input_im_fw)} Input-Phase(n), begründet")

    # Phasen des Handlungskreises (für die Lernsituation)
    el["informieren"] = bool(re.search(r"Informieren|Analysieren", "\n".join(phasen_koepfe))) or el["eingang"]
    el["planen"] = bool(re.search(r"Planen", "\n".join(phasen_koepfe)))
    el["durchfuehren"] = bool(re.search(r"Durchführen", "\n".join(phasen_koepfe)))

    return {
        "datei": str(pfad),
        "titel": fm.get("title", ""),
        "lernsituation": fm.get("lernsituation", ""),
        "teil": fm.get("teil", ""),
        "dauer": dauer,
        "kernweg": kernweg,
        "aufgaben": len(set(AUFGABE.findall(hs))),
        "woerter_schuelerteil": w_schueler,
        "woerter_fachwissen": w_fach,
        "codezeilen": codezeilen,
        "bewertung_summe": summe,
        "elemente": el,
        "befunde": b,
    }


# ---------------------------------------------------------------------------------------------
# Lernsituationen (mehrere Lektionen)
# ---------------------------------------------------------------------------------------------

def ordner_schluessel(pfad: str) -> tuple[int, str, str]:
    name = Path(pfad).parent.name or Path(pfad).name
    m = re.match(r"(\d+)([a-z]?)", name)
    return (int(m.group(1)), m.group(2), name) if m else (10 ** 6, "", name)


def teil_zahlen(wert: str) -> tuple[int, int] | None:
    m = re.fullmatch(r"\s*(\d+)\s*/\s*(\d+)\s*", wert or "")
    return (int(m.group(1)), int(m.group(2))) if m else None


def ls_name(e: dict) -> str | None:
    """Name der Lernsituation; None = eigene Lernsituation (Feld fehlt, leer oder Platzhalter)."""
    wert = (e.get("lernsituation") or "").strip()
    if not wert or wert.startswith("["):
        return None
    return wert


def lernsituationen(erg: list[dict]) -> list[dict]:
    """Verteilt die Befunde mehrteiliger Lernsituationen auf Auftakt/Abschluss und prüft den Kreis.

    Ändert die Befunde in `erg` (Befunde außerhalb ihrer Rolle werden „–“) und liefert die
    Befunde je Lernsituation. Lektionen ohne `lernsituation` bleiben unverändert.
    """
    gruppen: dict[str, list[dict]] = {}
    for e in erg:
        name = ls_name(e)
        if name is not None:
            gruppen.setdefault(name.casefold(), []).append(e)
    ausgabe = []
    for schluessel, mitglieder in gruppen.items():
        name = ls_name(mitglieder[0]) or schluessel
        keine = schluessel == "keine"
        mit_teil = [(teil_zahlen(e.get("teil", "")), e) for e in mitglieder]
        b: list[dict] = []
        sortiert = sorted(mitglieder, key=lambda e: ordner_schluessel(e["datei"]))
        if not keine and all(t for t, _ in mit_teil):
            nach_teil = [e for _, e in sorted(mit_teil, key=lambda x: x[0][0])]
            if [e["datei"] for e in nach_teil] != [e["datei"] for e in sortiert]:
                befund(b, "L1", "Reihenfolge der Teile", "⚠", "Ordnerreihenfolge widerspricht `teil`")
            reihenfolge = nach_teil
        else:
            reihenfolge = sortiert
        vollstaendig = True
        if not keine:
            teile = [t for t, _ in mit_teil if t]
            ns = {t[1] for t in teile}
            nummern = [t[0] for t in teile]
            hinweise = []
            if len(teile) < len(mitglieder):
                hinweise.append("`teil` fehlt oder ist nicht „k/n“")
                vollstaendig = False
            if len(ns) > 1:
                hinweise.append(f"widersprüchliche n: {sorted(ns)}")
                vollstaendig = False
            if len(nummern) != len(set(nummern)):
                hinweise.append("Teil doppelt vergeben")
                vollstaendig = False
            if len(ns) == 1 and not hinweise:
                n = next(iter(ns))
                fehlen = sorted(set(range(1, n + 1)) - set(nummern))
                if fehlen:
                    hinweise.append("Teil " + ", ".join(f"{k}/{n}" for k in fehlen) + " nicht übergeben")
                    vollstaendig = False
            befund(b, "L1", f"Teile der Lernsituation „{name}“", "✅" if not hinweise else "⚠",
                   f"{len(mitglieder)} Lektionen" if not hinweise else "; ".join(hinweise))
        # Verteilung der Befunde auf die Rollen
        erste, letzte = reihenfolge[0], reihenfolge[-1]
        for e in mitglieder:
            for bf in e["befunde"]:
                nr = bf["nr"]
                if nr not in ANKER_ERSTE | ANKER_LETZTE | ANKER_IRGENDWO or bf["stufe"] == "✅":
                    continue
                if keine:
                    anker = None
                elif nr in ANKER_ERSTE:
                    anker = erste
                elif nr in ANKER_LETZTE:
                    anker = letzte
                else:
                    key = {3: "eingang", 7: "entscheiden", 12: "verdeckt"}[nr]
                    anker = next((x for x in reihenfolge if x["elemente"].get(key)), erste)
                if anker is not e:
                    bf["hinweis"] = ("in dieser Lektion nicht erwartet" if not keine
                                     else "Zusatzeinheit ohne Lernsituation")
                    bf["stufe"] = "–"
        if keine:
            ausgabe.append({"lernsituation": name, "lektionen": [x["datei"] for x in reihenfolge], "befunde": b})
            continue
        # Handlungskreis
        el = lambda k: any(x["elemente"].get(k) for x in mitglieder)          # noqa: E731
        kreis_fehlt = []
        if not el("entscheiden"):
            kreis_fehlt.append("Entscheiden")
        if not (el("realitaet") or el("rueckmeldung")):
            kreis_fehlt.append("Überprüfen")
        if not el("lernweg"):
            kreis_fehlt.append("Reflektieren")
        duenn = [n for n, k in (("Informieren", "informieren"), ("Planen", "planen"),
                                ("Durchführen", "durchfuehren")) if not el(k)]
        if kreis_fehlt:
            stufe = "❌" if vollstaendig else "⚠"
            befund(b, "L2", "Handlungskreis geschlossen", stufe,
                   "fehlt in der Lernsituation: " + ", ".join(kreis_fehlt + duenn)
                   + ("" if vollstaendig else " (Lernsituation unvollständig übergeben)"))
        elif duenn:
            befund(b, "L2", "Handlungskreis geschlossen", "⚠", "nicht erkennbar: " + ", ".join(duenn))
        else:
            befund(b, "L2", "Handlungskreis geschlossen", "✅", "alle sechs Phasen in der Lernsituation")
        # Reihenfolge der Elemente
        probleme = []
        idx = {id(x): i for i, x in enumerate(reihenfolge)}
        if el("bewertung") and not reihenfolge[0]["elemente"].get("bewertung"):
            probleme.append("Bewertungskasten nicht in der ersten Lektion")
        lern = [idx[id(x)] for x in reihenfolge if x["elemente"].get("lernweg")]
        if lern and max(lern) != len(reihenfolge) - 1:
            probleme.append("Lernweg nicht in der letzten Lektion")
        ent = [idx[id(x)] for x in reihenfolge if x["elemente"].get("entscheiden")]
        real = [idx[id(x)] for x in reihenfolge if x["elemente"].get("realitaet")]
        if ent and real and min(ent) > max(real):
            probleme.append("Realitätstest vor der Entscheidung")
        befund(b, "L3", "Reihenfolge der Elemente", "⚠" if probleme else "✅", "; ".join(probleme))
        # Lernzeit
        kern = [x["kernweg"] for x in mitglieder]
        fehlt_kern = [Path(x["datei"]).parent.name for x in mitglieder if x["kernweg"] is None]
        summe_dauer = sum(x["dauer"] for x in mitglieder)
        hinweis = f"Σ Dauer {summe_dauer} min"
        if fehlt_kern:
            befund(b, "L4", "Lernzeit", "⚠", hinweis + "; Kernweg fehlt in " + ", ".join(fehlt_kern))
        else:
            befund(b, "L4", "Lernzeit", "✅", hinweis + f"; Σ Kernweg {sum(k for k in kern if k)} min")
        ausgabe.append({"lernsituation": name, "lektionen": [x["datei"] for x in reihenfolge], "befunde": b})
    return ausgabe


def markdown(ergebnisse: list[dict], ls: list[dict] | None = None) -> str:
    aus = []
    for e in ergebnisse:
        kopf = f"{e['titel']} · {e['aufgaben']} Aufgaben · {e['woerter_schuelerteil']} Wörter im Schülerteil"
        if e.get("lernsituation"):
            kopf += f" · Lernsituation „{e['lernsituation']}“ Teil {e.get('teil') or '?'}"
        aus.append(f"## {e['datei']}\n\n{kopf}\n")
        aus.append("| Nr. | Element | Ergebnis | Hinweis |\n|---|---|---|---|")
        aus += [f"| {x['nr']} | {x['element']} | {x['stufe']} | {x['hinweis']} |" for x in e["befunde"]]
        aus.append("")
    if ls:
        for g in ls:
            aus.append(f"## Lernsituation „{g['lernsituation']}“ ({len(g['lektionen'])} Lektionen)\n")
            aus.append("| Nr. | Element | Ergebnis | Hinweis |\n|---|---|---|---|")
            aus += [f"| {x['nr']} | {x['element']} | {x['stufe']} | {x['hinweis']} |" for x in g["befunde"]]
            aus.append("")
    if len(ergebnisse) > 1:
        aus.append("## Übersicht\n\n| Lektion | ✅ | ⚠ | ❌ | Wörter | Σ Bewertung |\n|---|---|---|---|---|---|")
        for e in ergebnisse:
            z = {s: sum(1 for x in e["befunde"] if x["stufe"] == s) for s in ("✅", "⚠", "❌")}
            aus.append(f"| {Path(e['datei']).parent.name or e['datei']} | {z['✅']} | {z['⚠']} | {z['❌']} | "
                       f"{e['woerter_schuelerteil']} | {e['bewertung_summe'] or '–'} |")
    aus.append("\nSignalwortsuche, keine Bewertung: „⚠“ heißt „von Hand nachsehen“, „–“ „in dieser "
               "Lektion nicht erwartet“ (lektionsmuster.md).")
    return "\n".join(aus)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Lektionen gegen das Lektionsmuster prüfen.")
    p.add_argument("lektionen", nargs="+", type=Path)
    p.add_argument("--max-woerter", type=int, default=1500)
    p.add_argument("--loesungen", type=Path, default=None)
    p.add_argument("--projekt", type=Path, default=None)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    fehlend = [str(x) for x in a.lektionen if not x.is_file()]
    if fehlend:
        print("Datei nicht gefunden: " + ", ".join(fehlend), file=sys.stderr)
        return 2
    cfg = phase_config(a.projekt) if a.projekt else None
    erg = [pruefe(x, a.max_woerter, a.loesungen, cfg) for x in a.lektionen]
    ls = lernsituationen(erg)
    if a.json:
        print(json.dumps({"lektionen": erg, "lernsituationen": ls}, ensure_ascii=False, indent=2))
    else:
        print(markdown(erg, ls))
    alle = [x for e in erg for x in e["befunde"]] + [x for g in ls for x in g["befunde"]]
    return 1 if any(x["stufe"] == "❌" for x in alle) else 0


if __name__ == "__main__":
    sys.exit(main())
