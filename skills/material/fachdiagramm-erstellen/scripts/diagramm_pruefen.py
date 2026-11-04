#!/usr/bin/env python3
"""diagramm_pruefen – prüft Diagramm-Specs (YAML) vor dem Erzeugen mit edu-diagramm.

Die Generatoren ersetzen unbekannte Farben und Formen still durch Standardwerte, legen
Knoten auf derselben Rasterposition übereinander und prüfen die Notation nur, wenn der
Dateiname das Kürzel trägt. Dieses Skript findet das vorher:

- type, out und Namenskürzel (_flow_, _nsd_, _chen_, _uml_; relational: _rel_)
- Kanten/Beziehungen zu unbekannten Knoten, doppelte Rasterpositionen
- unbekannte Farben, Formen, Linienarten, Pfeile, Umleitungen, Blocktypen, UML-Kantenarten
- Umleitung links/rechts zwischen Knoten derselben Zeile (läuft ab eduwerkzeuge 0.2.1 unten herum)
- Umleitungen, die hinter einem Kasten durchlaufen (seitlich in einer belegten Zeile, oben/unten
  in einer belegten Spalte) – in der Vorschau oft als scheinbarer Doppelpfeil sichtbar
- Kantenbeschriftungen, die breiter sind als der Abstand zwischen zwei Kästen derselben Zeile
- Chen: Attributfächer benachbarter Entitäten, die sich überlappen
- Schlüsselattribute (Chen, relational), Bedingungen und Rümpfe (Struktogramm)
- sehr lange Beschriftungen

    python3 scripts/diagramm_pruefen.py diagramme/42_flow_regelkreis.yaml [weitere.yaml …]

Exitcode 1 bei Fehlern (❌). Braucht PyYAML.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

TYPEN = {"flow": "flow", "struktogramm": "nsd", "chen": "chen", "uml": "uml", "relational": "rel"}
BEFEHL = {"flow": "flow", "struktogramm": "struktogramm", "chen": "chen", "uml": "box", "relational": "box"}
FARBEN = {"blau", "gruen", "gelb", "rot", "lila", "orange", "grau", "weiss"}
FORMEN = {"box", "rounded", "ellipse", "raute", "note", "zylinder"}
STILE = {"solid", "dashed"}
PFEILE = {"single", "double", "none"}
ROUTEN = {"direkt", "links", "rechts", "oben", "unten"}
BLOCKTYPEN = {"anweisung", "verzweigung", "kopfschleife", "fussschleife", "aufruf"}
UML_KANTEN = {"association", "inheritance", "extends", "implements", "realization", "dependency",
              "aggregation", "composition"}
MAX_TEXT = 45       # Kästen wachsen mit dem Text
# Maße wie in edu-diagramm flow (eduwerkzeuge/diagramme/flow.py, _common.text_breite)
SPALTE_STANDARD, MIN_W, PAD_X = 320, 150, 22


def _textbreite(text: str, groesse: float, fett: bool = False) -> float:
    return len(text) * groesse * (0.60 if fett else 0.545)


def _kastenbreite(p: dict) -> float | None:
    if p.get("children"):
        return None                       # Container: Breite hängt von den Unterkästen ab
    if p.get("w"):
        return float(p["w"])
    lines = p.get("lines") or []
    breiten = [_textbreite(str(p.get("label") or ""), 14, True)] + [_textbreite(str(z), 12.5) for z in lines]
    return max(MIN_W, max(breiten) + 2 * PAD_X)
MAX_TEXT_NSD = 80   # Struktogramme brechen um


def _text(befunde: list, ort: str, text, grenze: int = MAX_TEXT) -> None:
    for zeile in (text if isinstance(text, list) else [text]):
        if zeile is not None and len(str(zeile)) > grenze:
            befunde.append(("⚠", ort, f"Beschriftung mit {len(str(zeile))} Zeichen – kürzen oder auf "
                            "lines/mehrere Zeilen verteilen"))


def _farbe(befunde: list, ort: str, wert) -> None:
    if wert is None:
        return
    w = str(wert)
    if not (w.lower() in FARBEN or re.fullmatch(r"#[0-9a-fA-F]{6}", w)):
        befunde.append(("❌", ort, f"Farbe „{w}“ unbekannt – erlaubt: {', '.join(sorted(FARBEN))} oder #rrggbb "
                        "(sonst still blau)"))


def _positionen(befunde: list, art: str, eintraege: dict) -> None:
    belegt: dict[tuple, str] = {}
    for name, p in eintraege.items():
        if not isinstance(p, dict):
            continue
        pos = (float(p.get("x", 0)), float(p.get("y", 0)))
        if pos in belegt:
            befunde.append(("❌", f"{art} {name}", f"gleiche Rasterposition wie {belegt[pos]} {pos} – überlagert"))
        belegt[pos] = name


def pruefe_flow(d: dict, befunde: list) -> None:
    nodes = d.get("nodes") or {}
    if len(nodes) < 2:
        befunde.append(("❌", "nodes", "mindestens zwei Knoten nötig"))
    ids = set()
    for name, p in nodes.items():
        p = p or {}
        ids.add(str(name))
        o = f"Knoten {name}"
        _farbe(befunde, o, p.get("color"))
        if p.get("shape") and str(p["shape"]).lower() not in FORMEN:
            befunde.append(("❌", o, f"Form „{p['shape']}“ unbekannt – erlaubt: {', '.join(sorted(FORMEN))}"))
        _text(befunde, o, p.get("label"))
        _text(befunde, o, p.get("lines") or [])
        for k in p.get("children") or []:
            if not k.get("id"):
                befunde.append(("❌", o, "Unterkasten (children) ohne id"))
            else:
                ids.add(str(k["id"]))
    _positionen(befunde, "Knoten", nodes)
    zeile = {str(n): float((p or {}).get("y", 0)) for n, p in nodes.items()}
    spalte_x = {str(n): float((p or {}).get("x", 0)) for n, p in nodes.items()}
    breite = {str(n): _kastenbreite(p or {}) for n, p in nodes.items()}
    rasterbreite = float(d.get("spalte") or SPALTE_STANDARD)

    def im_weg(knoten: str, richtung: str) -> list[str]:
        """Knoten, an denen eine Umleitung ab bzw. bis ``knoten`` vorbeiführen müsste."""
        x, y = spalte_x[knoten], zeile[knoten]
        if richtung in ("rechts", "links"):
            return [n for n in nodes if str(n) != knoten and zeile[str(n)] == y
                    and (spalte_x[str(n)] > x if richtung == "rechts" else spalte_x[str(n)] < x)]
        return [n for n in nodes if str(n) != knoten and spalte_x[str(n)] == x
                and (zeile[str(n)] > y if richtung == "unten" else zeile[str(n)] < y)]
    kanten = d.get("edges") or []
    if not kanten:
        befunde.append(("❌", "edges", "keine Kanten – edu-diagramm validate verlangt mindestens eine"))
    for i, e in enumerate(kanten, 1):
        o = f"Kante {i} ({e.get('from')}→{e.get('to')})"
        for ende in ("from", "to"):
            if str(e.get(ende)) not in ids:
                befunde.append(("❌", o, f"{ende}: „{e.get(ende)}“ ist kein Knoten"))
        for schluessel, erlaubt in (("style", STILE), ("arrow", PFEILE), ("route", ROUTEN)):
            if e.get(schluessel) and str(e[schluessel]).lower() not in erlaubt:
                befunde.append(("❌", o, f"{schluessel}: „{e[schluessel]}“ – erlaubt: {', '.join(sorted(erlaubt))}"))
        if str(e.get("route", "direkt")).lower() in ("links", "rechts"):
            a, b = str(e.get("from")), str(e.get("to"))
            if a in zeile and b in zeile and zeile[a] == zeile[b]:
                befunde.append(("⚠", o, f"route: {e['route']} zwischen Knoten derselben Zeile wird unten herum "
                                "geführt (eduwerkzeuge ≥ 0.2.1; ältere Fassungen zeichnen quer über die Zeile) – "
                                "eindeutiger: route: unten"))
        route = str(e.get("route", "direkt")).lower()
        a, b = str(e.get("from")), str(e.get("to"))
        if route in ("links", "rechts", "oben", "unten") and a in zeile and b in zeile \
                and not (route in ("links", "rechts") and zeile[a] == zeile[b]):
            hinter = sorted({str(n) for n in im_weg(a, route) + im_weg(b, route)})
            if hinter:
                befunde.append(("⚠", o, f"route: {route} läuft hinter {', '.join(hinter)} durch (die Umleitung "
                                "verlässt bzw. erreicht ihren Kasten quer durch dessen Zeile/Spalte) – Knoten so "
                                "anordnen, dass Start und Ziel außen liegen, oder eine andere Umleitung wählen"))
        lab = e.get("label")
        if lab and route == "direkt" and a in zeile and b in zeile and zeile[a] == zeile[b] \
                and breite.get(a) and breite.get(b):
            abstand = rasterbreite * abs(spalte_x[b] - spalte_x[a]) - (breite[a] + breite[b]) / 2
            noetig = max(_textbreite(str(z), 12) for z in str(lab).split("\n")) + 12
            if noetig > abstand - 8:
                befunde.append(("⚠", o, f"Beschriftung ca. {noetig:.0f} px breit, Abstand zwischen den Kästen nur "
                                f"ca. {max(abstand, 0):.0f} px – sie wird verdeckt; kürzen, Knoten weiter auseinander "
                                "(x) oder spalte: erhöhen"))
        _text(befunde, o, e.get("label"))


def _bloecke(bloecke, befunde: list, pfad: str) -> int:
    anzahl = 0
    if not bloecke:
        befunde.append(("❌", pfad, "leerer Block (mindestens eine Anweisung)"))
        return 0
    for i, b in enumerate(bloecke, 1):
        o = f"{pfad}/{i}"
        anzahl += 1
        if isinstance(b, str):
            _text(befunde, o, b, MAX_TEXT_NSD)
            continue
        if not isinstance(b, dict):
            befunde.append(("❌", o, "Block ist weder Text noch Mapping"))
            continue
        typ = str(b.get("typ", "anweisung")).lower()
        if typ not in BLOCKTYPEN:
            befunde.append(("❌", o, f"typ „{typ}“ unbekannt – erlaubt: {', '.join(sorted(BLOCKTYPEN))}"))
            continue
        if typ in ("anweisung", "aufruf") and not b.get("text"):
            befunde.append(("❌", o, f"{typ} ohne text"))
        if typ in ("verzweigung", "kopfschleife", "fussschleife") and not b.get("bedingung"):
            befunde.append(("❌", o, f"{typ} ohne bedingung"))
        if typ == "verzweigung":
            ja = b.get("ja", b.get("dann"))
            nein = b.get("nein", b.get("sonst", []))
            if ja is None:
                befunde.append(("❌", o, "verzweigung ohne ja/dann-Zweig"))
            else:
                anzahl += _bloecke(ja, befunde, o + "/ja")
            if nein:
                anzahl += _bloecke(nein, befunde, o + "/nein")
        if typ in ("kopfschleife", "fussschleife"):
            anzahl += _bloecke(b.get("rumpf"), befunde, o + "/rumpf")
        _text(befunde, o, b.get("text"), MAX_TEXT_NSD)
        _text(befunde, o, b.get("bedingung"), MAX_TEXT_NSD)
    return anzahl


def pruefe_struktogramm(d: dict, befunde: list) -> None:
    n = _bloecke(d.get("blocks"), befunde, "blocks")
    if n > 25:
        befunde.append(("⚠", "blocks", f"{n} Blöcke – Struktogramm teilen (Unterprogramm als aufruf)"))


def pruefe_chen(d: dict, befunde: list) -> None:
    ents = d.get("entities") or {}
    if not ents:
        befunde.append(("❌", "entities", "keine Entitäten"))
    _positionen(befunde, "Entität", ents)
    for name, p in ents.items():
        attrs = (p or {}).get("attrs") or []
        if attrs and not any(str(a).rstrip().endswith("*") for a in attrs):
            befunde.append(("⚠", f"Entität {name}", "kein Schlüsselattribut (mit * markieren)"))
    layout = d.get("layout") or {}
    col_w = float(layout.get("col_w", 280))
    abstand = float(layout.get("attr_spacing", 130))

    def halbe_breite(p: dict) -> float:          # Attributfächer: Ellipsen 120 px breit
        n = len(p.get("attrs") or [])
        return (n - 1) * abstand / 2 + 60 if n else 80

    zeilen: dict[float, list] = {}
    for name, p in ents.items():
        p = p or {}
        zeilen.setdefault(float(p.get("y", 0)), []).append((float(p.get("x", 0)), name, p))
    for reihe in zeilen.values():
        reihe.sort(key=lambda z: z[0])
        for (x1, n1, p1), (x2, n2, p2) in zip(reihe, reihe[1:]):
            if halbe_breite(p1) + halbe_breite(p2) + 10 > (x2 - x1) * col_w:
                befunde.append(("⚠", f"Entitäten {n1}/{n2}", "Attribute überlappen – Entitäten weiter "
                                "auseinander (x) oder layout.col_w erhöhen"))
    for i, r in enumerate(d.get("relations") or [], 1):
        o = f"Beziehung {i} „{r.get('name', '')}“"
        a, b = ents.get(r.get("from")) or {}, ents.get(r.get("to")) or {}
        if a and b and float(a.get("y", 0)) != float(b.get("y", 0)) and (a.get("attrs") or b.get("attrs")):
            befunde.append(("⚠", o, "Entitäten in verschiedenen Zeilen: Attribute können die Raute überlagern – "
                            "nebeneinander anordnen (gleiche Zeile, jede zweite Spalte)"))
        if not r.get("name"):
            befunde.append(("❌", o, "Beziehung ohne Namen (Raute bleibt leer)"))
        for ende in ("from", "to"):
            if r.get(ende) not in ents:
                befunde.append(("❌", o, f"{ende}: „{r.get(ende)}“ ist keine Entität"))
        if r.get("cardinality") is not None and len(r["cardinality"]) != 2:
            befunde.append(("❌", o, "cardinality braucht genau zwei Werte"))


def pruefe_box(d: dict, typ: str, befunde: list) -> None:
    klassen = d.get("classes") or d.get("entities") or {}
    if not klassen:
        befunde.append(("❌", "classes", "keine Klassen bzw. Tabellen"))
    _positionen(befunde, "Klasse", klassen)
    for name, p in klassen.items():
        attrs = (p or {}).get("attrs") or []
        if typ == "relational" and not any("*" in str(a).split(":")[0] for a in attrs):
            befunde.append(("⚠", f"Tabelle {name}", "kein Primärschlüssel (Spalte mit * markieren)"))
    for i, r in enumerate(d.get("relations") or [], 1):
        o = f"Beziehung {i} ({r.get('from')}→{r.get('to')})"
        for ende in ("from", "to"):
            if r.get(ende) not in klassen:
                befunde.append(("❌", o, f"{ende}: „{r.get(ende)}“ ist keine Klasse/Tabelle"))
        if typ == "uml" and r.get("kind") and str(r["kind"]).lower() not in UML_KANTEN:
            befunde.append(("❌", o, f"kind „{r['kind']}“ – erlaubt: {', '.join(sorted(UML_KANTEN))}"))


def pruefe_spec(pfad: Path) -> list:
    befunde: list = []
    if yaml is None:
        return [("❌", "PyYAML", "fehlt (python3 -m pip install pyyaml)")]
    try:
        d = yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return [("❌", "YAML", f"nicht lesbar: {e}")]
    typ = str(d.get("type", "")).lower()
    if typ not in TYPEN:
        return [("❌", "type", f"„{typ or '–'}“ – erlaubt: {', '.join(TYPEN)}")]
    if not d.get("title"):
        befunde.append(("⚠", "title", "kein Titel"))
    out = str(d.get("out") or "")
    if not out:
        befunde.append(("❌", "out", "fehlt (Basisname der Ausgabe, relativ zum Arbeitsordner)"))
    elif f"_{TYPEN[typ]}_" not in Path(out).name.lower() + "_" and not Path(out).name.lower().startswith(TYPEN[typ] + "_"):
        befunde.append(("⚠", "out", f"Name ohne Kürzel _{TYPEN[typ]}_ – edu-diagramm validate prüft dann "
                        "nur das XML, nicht die Notation"))
    if typ == "chen" and not any((p or {}).get("attrs") for p in (d.get("entities") or {}).values()) \
            and "_uebersicht" not in out.lower():
        befunde.append(("⚠", "out", "Chen ohne Attribute: Namen mit _uebersicht enden lassen"))
    {"flow": pruefe_flow, "struktogramm": pruefe_struktogramm, "chen": pruefe_chen}.get(
        typ, lambda dd, bb: pruefe_box(dd, typ, bb))(d, befunde)
    return befunde


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Diagramm-Specs vor edu-diagramm prüfen.")
    p.add_argument("specs", nargs="+", type=Path)
    a = p.parse_args(argv)
    fehler = 0
    for spec in a.specs:
        if not spec.is_file():
            print(f"❌ {spec}: Datei nicht gefunden")
            fehler += 1
            continue
        befunde = pruefe_spec(spec)
        typ = ""
        if yaml is not None:
            try:
                typ = str((yaml.safe_load(spec.read_text(encoding="utf-8")) or {}).get("type", "")).lower()
            except yaml.YAMLError:
                pass
        f = sum(1 for b in befunde if b[0] == "❌")
        fehler += f
        befehl = f" → edu-diagramm {BEFEHL[typ]} {spec}" if typ in BEFEHL and not f else ""
        print(f"{'✔' if not f else '✘'} {spec} ({typ or '?'}): {f} Fehler, "
              f"{sum(1 for b in befunde if b[0] == '⚠')} Warnungen{befehl}")
        for stufe in ("❌", "⚠"):
            for s, o, t in befunde:
                if s == stufe:
                    print(f"   {s} {o}: {t}")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
