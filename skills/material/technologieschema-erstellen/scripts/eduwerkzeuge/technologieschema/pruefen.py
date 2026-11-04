"""
pruefen — Spec laden, prüfen, zu SVG zusammensetzen, Legende erzeugen.

Die Prüfung läuft in zwei Stufen:

1. **Schema** (vor dem Zeichnen): unbekannte Typen und Schlüssel (mit Vorschlag bei Tippfehlern),
   fehlende Pflichtangaben, falsche Werte, doppelte Kennzeichen, Kennzeichen nach DIN EN IEC 81346-2.
2. **Bild** (nach dem Zeichnen): Teile außerhalb des Bildes, überlagerte oder durchlaufene
   Beschriftungen, Legendenzeilen ohne Funktion.
"""

from __future__ import annotations

import difflib
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import grafcet as gc
from . import kennzeichen as kz
from . import symbole
from .teile import (AUFZAEHLUNGEN, EINTRAG_TYPEN, EINZELPUNKTE, GEMEIN, PUNKTLISTEN, SCHEMA, SENSOR_SCHEMA,
                    WAHRHEITEN, ZAHLEN, ZEICHNER, Kontext, SpecFehler, _ist_zahl)
from .zeichnung import Zeichnung

KOPF_SCHLUESSEL = {"titel", "alt", "out", "breite", "hoehe", "fusszeile", "hinweis", "elemente"}
TOLERANZ = 2.0


@dataclass
class Befund:
    stufe: str    # "❌" oder "⚠"
    text: str

    def __str__(self) -> str:
        return f"{self.stufe} {self.text}"


@dataclass
class Szene:
    zeichnung: Zeichnung
    ctx: Kontext
    namen: list[str] = field(default_factory=list)
    spec: dict | None = None      # Spec nach dem Auflösen (typ grafcet in Einzelteile umgesetzt)

    @property
    def svg(self) -> str:
        return self.zeichnung.svg()


def lade(pfad: str | Path) -> dict:
    import yaml
    spec = yaml.safe_load(Path(pfad).read_text(encoding="utf-8"))
    if not isinstance(spec, dict):
        raise SpecFehler("Die Spec ist kein YAML-Mapping (Schlüssel: Wert).")
    return spec


def _name(i: int, e) -> str:
    if isinstance(e, dict):
        kennung = f" {e['id']}" if e.get("id") else ""
        return f"Element {i + 1} ({e.get('typ', '?')}{kennung})"
    return f"Element {i + 1}"


# ───────────────────────────── Stufe 1: Schema ─────────────────────────────

def schema_pruefen(spec: dict) -> list[Befund]:
    b: list[Befund] = []
    fehl = lambda t: b.append(Befund("❌", t))  # noqa: E731
    warn = lambda t: b.append(Befund("⚠", t))  # noqa: E731

    for k in spec:
        if k == "kennzeichnung":
            fehl(f"'kennzeichnung' gibt es nicht mehr: Kennzeichen sind immer nach {kz.NORM} – Schlüssel streichen")
        elif k not in KOPF_SCHLUESSEL:
            fehl(f"Unbekannter Schlüssel '{k}' in der Spec{_vorschlag(k, KOPF_SCHLUESSEL)}")
    for k in ("titel", "alt", "breite", "hoehe", "elemente"):
        if k in ("breite", "hoehe") and gc.enthaelt_grafcet(spec):   # sonst aus dem GRAFCET berechnet
            continue
        if k not in spec:
            fehl(f"Pflichtangabe '{k}' fehlt" + (" (Alternativtext, ein Satz)" if k == "alt" else ""))
    for k in ("breite", "hoehe"):
        if k in spec and (not _ist_zahl(spec[k]) or spec[k] < 100):
            fehl(f"'{k}' muss eine Zahl ≥ 100 sein")
    fuss = spec.get("fusszeile")
    if fuss is not None and not (isinstance(fuss, str) or (isinstance(fuss, list) and all(isinstance(z, str) for z in fuss))):
        fehl("'fusszeile' ist ein Text oder eine Liste von Texten")
    el = spec.get("elemente")
    if el is not None and (not isinstance(el, list) or not el):
        fehl("'elemente' muss eine nicht leere Liste sein")
        return b
    if not isinstance(el, list):
        return b

    if not gc.enthaelt_grafcet(spec) and re.search("grafcet", f"{spec.get('titel', '')} {spec.get('alt', '')}", re.I) \
            and not any(isinstance(e, dict) and e.get("typ") == "grafcet_schritt" for e in el):
        warn("GRAFCET aus Grundformen: 'typ: grafcet' verwenden – nur dann erzwingt die Prüfung Zuweisung und Pfeil "
             "speichernder Aktionen, Überstrich und den Wechsel von Schritt und Transition")

    kennungen: dict[str, str] = {}
    gueltige: list[str] = []
    zugehoerig: list[tuple[str, str]] = []
    schritte_gesamt = {str(s.get("schritt")) for e in el if isinstance(e, dict) and e.get("typ") == "grafcet"
                       for s in _schritte_roh(e.get("kette"))}

    def merke(wert, wo, typ=None, ist_id=False, klassen=None):
        w = str(wert)
        if w in kennungen:
            fehl(f"{wo}: Kennzeichen/ref '{w}' ist schon vergeben ({kennungen[w]})")
        else:
            kennungen[w] = wo
        if ist_id and typ not in ("text", "etikett"):
            probleme = kz.pruefe(w, typ, klassen)
            for pr in probleme:
                fehl(f"{wo}: {pr}")
            if not probleme:
                gueltige.append(w)

    for i, e in enumerate(el):
        wo = _name(i, e)
        if not isinstance(e, dict):
            fehl(f"{wo}: Eintrag ist kein Mapping")
            continue
        _element_pruefen(e, wo, b, merke, kind=False, zugehoerig=zugehoerig)
        if e.get("typ") == "grafcet":
            b += [Befund(st, t) for st, t in gc.pruefe_kette(e, wo, schritte_gesamt)]
        elif e.get("typ") == "grafcet_schritt":
            m: list = []
            gc.lies_aktionen(e.get("aktionen"), f"{wo}", m)
            b += [Befund(st, t) for st, t in m]
    for gz, wo in zugehoerig:
        if gz not in kennungen:
            fehl(f"{wo}: gehoert_zu '{gz}' – kein Teil mit diesem Kennzeichen (id) in der Spec")
    tiefe_fehler, tiefe_hinweise = kz.tiefe_pruefen(gueltige)
    for t_ in tiefe_fehler:
        fehl(t_)
    for t_ in tiefe_hinweise:
        warn(t_)
    return b


def _element_pruefen(e: dict, wo: str, b: list[Befund], merke, kind: bool, zugehoerig: list | None = None) -> None:
    fehl = lambda t: b.append(Befund("❌", t))  # noqa: E731
    typ = e.get("typ")
    if typ not in SCHEMA:
        fehl(f"{wo}: unbekannter typ '{typ}'{_vorschlag(str(typ), SCHEMA)} – gültig: {', '.join(SCHEMA)}")
        return
    pflicht, optional = SCHEMA[typ]
    if kind:
        pflicht = pflicht - {"x", "y"}
    erlaubt = GEMEIN | pflicht | optional | ({"x", "y"} if kind else set())
    for k in e:
        if k not in erlaubt:
            fehl(f"{wo}: unbekannter Schlüssel '{k}'{_vorschlag(k, erlaubt)}")
    for k in pflicht:
        if k not in e:
            fehl(f"{wo}: Pflichtangabe '{k}' fehlt")
    for k, v in e.items():
        if k in ZAHLEN and not _ist_zahl(v):
            fehl(f"{wo}: '{k}' muss eine Zahl sein, nicht {v!r}")
        elif k in WAHRHEITEN and not isinstance(v, bool):
            fehl(f"{wo}: '{k}' muss true oder false sein")
        elif k in AUFZAEHLUNGEN and k != "seite" and not (typ == "symbol" and k == "symbol") and v not in AUFZAEHLUNGEN[k]:
            fehl(f"{wo}: '{k}: {v}' ist ungültig – erlaubt: {', '.join(map(str, AUFZAEHLUNGEN[k]))}")
        elif k in PUNKTLISTEN and not (isinstance(v, list) and len(v) >= 2):
            fehl(f"{wo}: '{k}' braucht eine Liste mit mindestens zwei Punkten ([x, y] oder \"ID@punkt\")")
        elif k in ("id", "ref", "name", "text", "betriebsmittel", "funktion") and not isinstance(v, (str, int, float)):
            fehl(f"{wo}: '{k}' muss Text sein")
    if typ == "symbol" and e.get("betaetigung") and e.get("symbol") in symbole.SYMBOLE \
            and symbole.SYMBOLE[e["symbol"]].wirk is None:
        fehl(f"{wo}: '{e['symbol']}' hat keine Wirkverbindung – 'betaetigung' gibt es nur bei Kontakten "
             f"({', '.join(n for n, s in symbole.SYMBOLE.items() if s.wirk is not None)})")
    if typ == "knoten" and not isinstance(e.get("punkt"), (list, str)):
        fehl(f"{wo}: 'punkt' ist [x, y] oder \"ID@punkt\"")
    if typ == "symbol" and isinstance(e.get("symbol"), str) and e["symbol"] not in symbole.SYMBOLE:
        fehl(f"{wo}: unbekanntes Symbol '{e['symbol']}'{_vorschlag(e['symbol'], symbole.SYMBOLE)} – "
             f"Liste: edu-technologieschema symbole")
    if typ == "behaelter" and e.get("fuellstand") is not None:
        if e.get("form", "tank") != "tank":
            fehl(f"{wo}: 'fuellstand' gibt es nur bei form: tank")
        elif _ist_zahl(e["fuellstand"]) and not 0 <= e["fuellstand"] <= 1:
            fehl(f"{wo}: 'fuellstand' liegt zwischen 0 und 1")
    for k in EINZELPUNKTE:
        if k in e and e[k] is not None and not (isinstance(e[k], (list, str))):
            fehl(f"{wo}: '{k}' ist [x, y] oder \"ID@punkt\"")
    if zugehoerig is None:
        zugehoerig = []
    if e.get("gehoert_zu") not in (None, ""):
        gz = str(e["gehoert_zu"])
        if e.get("id"):
            fehl(f"{wo}: 'gehoert_zu' und 'id' gleichzeitig – ein Teil zeigt entweder ein eigenes Kennzeichen oder das eines anderen")
        for pr in kz.pruefe(gz, typ, symbole.SYMBOLE[e["symbol"]].klassen if typ == "symbol" and e.get("symbol") in symbole.SYMBOLE else None):
            fehl(f"{wo}: gehoert_zu: {pr}")
        zugehoerig.append((gz, wo))
    for k in ("id", "ref"):
        if e.get(k) not in (None, ""):
            klassen = symbole.SYMBOLE[e["symbol"]].klassen if typ == "symbol" and e.get("symbol") in symbole.SYMBOLE else None
            merke(e[k], wo, typ, ist_id=(k == "id"), klassen=klassen)
    if typ == "zylinder":
        for j, s in enumerate(e.get("sensoren") or []):
            sw = f"{wo}, Sensor {j + 1}"
            if not isinstance(s, dict):
                fehl(f"{sw}: kein Mapping")
                continue
            sp, so = SENSOR_SCHEMA
            for k in s:
                if k not in sp | so:
                    fehl(f"{sw}: unbekannter Schlüssel '{k}'{_vorschlag(k, sp | so)}")
            if "seite" not in s:
                fehl(f"{sw}: Pflichtangabe 'seite' fehlt (links, rechts, oben, unten)")
            elif s["seite"] not in AUFZAEHLUNGEN["seite"]:
                fehl(f"{sw}: 'seite: {s['seite']}' ist ungültig – erlaubt: {', '.join(AUFZAEHLUNGEN['seite'])}")
            if "pos" in s and not (_ist_zahl(s["pos"]) and 0 <= s["pos"] <= 1):
                fehl(f"{sw}: 'pos' liegt zwischen 0 (Boden) und 1 (Stangenseite)")
            if s.get("id"):
                merke(s["id"], sw, "sensor", ist_id=True)
    if typ == "bedienfeld":
        if not isinstance(e.get("eintraege"), list) or not e["eintraege"]:
            fehl(f"{wo}: 'eintraege' braucht eine Liste")
        else:
            for j, en in enumerate(e["eintraege"]):
                ew = f"{wo}, Eintrag {j + 1}"
                if not isinstance(en, dict):
                    fehl(f"{ew}: kein Mapping")
                elif en.get("typ") == "leer":
                    continue
                elif en.get("typ") not in EINTRAG_TYPEN:
                    fehl(f"{ew}: typ '{en.get('typ')}' – im Bedienfeld erlaubt: {', '.join(EINTRAG_TYPEN)}, leer")
                else:
                    _element_pruefen(en, ew, b, merke, kind=True, zugehoerig=zugehoerig)
    if typ == "ampel" and not (isinstance(e.get("lampen"), list) and e["lampen"]):
        fehl(f"{wo}: 'lampen' braucht eine Liste von Beschriftungen (z. B. [rt, ge, gn])")


def _schritte_roh(folge):
    """Alle Schritte einer noch nicht geprüften Kette (für Bezüge über mehrere GRAFCET hinweg)."""
    for it in folge if isinstance(folge, list) else []:
        if isinstance(it, dict):
            if "schritt" in it:
                yield it
            for art in ("alternativ", "parallel"):
                for ast in it.get(art) or []:
                    yield from _schritte_roh(ast)


def _vorschlag(k: str, erlaubt) -> str:
    treffer = difflib.get_close_matches(str(k), list(erlaubt), n=1, cutoff=0.6)
    return f" – meinten Sie '{treffer[0]}'?" if treffer else ""


# ───────────────────────────── Aufbau ─────────────────────────────

def _lauf(spec: dict, vorher: dict, strikt: bool) -> Szene:
    fuss = spec.get("fusszeile") or []
    if isinstance(fuss, str):
        fuss = [fuss]
    hoehe, breite = float(spec["hoehe"]), float(spec["breite"])
    gesamt = hoehe + (len(fuss) * 16 + 14 if fuss else 0)
    hinweis = f"Kennzeichnung nach {kz.NORM}. " + str(spec.get("hinweis", ""))
    z = Zeichnung(breite, gesamt, str(spec["titel"]), str(spec["alt"]), hinweis=hinweis.strip())
    ctx = Kontext(z, vorher, strikt)
    namen = []
    for i, e in enumerate(spec["elemente"]):
        ctx.index = i
        z.aktuell = i
        z.zelle = f"e{i}"
        wo = _name(i, e)
        namen.append(wo)
        try:
            ZEICHNER[e["typ"]](ctx, e)
        except SpecFehler as ex:
            raise SpecFehler(f"{wo}: {ex}") from None
        except KeyError as ex:
            raise SpecFehler(f"{wo}: Schlüssel {ex} fehlt") from None
        except (TypeError, ValueError) as ex:
            raise SpecFehler(f"{wo}: {ex}") from None
    z.aktuell = -1
    z.zelle = "fuss"
    for j, zeile in enumerate(fuss):
        z.text(20, hoehe + 14 + 16 * j + 4, zeile, 11)
    return Szene(z, ctx, namen)


def bauen(spec: dict) -> Szene:
    """Zwei Durchläufe: der erste sammelt die Anker, der zweite löst Verweise darauf auf."""
    spec = gc.aufloesen(spec)
    erste = _lauf(spec, {}, False)
    szene = _lauf(spec, erste.ctx.anker, True)
    szene.spec = spec
    return szene


# ───────────────────────────── Stufe 2: Bild ─────────────────────────────

def _schnitt(a, b) -> bool:
    """Überlappen sich zwei Rahmen um mehr als die Toleranz?"""
    return min(a[2], b[2]) - max(a[0], b[0]) > TOLERANZ and min(a[3], b[3]) - max(a[1], b[1]) > TOLERANZ


def _segment_im_rahmen(s, r) -> bool:
    """Schneidet die Strecke s den Rahmen r (verkleinert um die Toleranz)?"""
    x1, y1, x2, y2 = r[0] + TOLERANZ, r[1] + TOLERANZ, r[2] - TOLERANZ, r[3] - TOLERANZ
    if x2 <= x1 or y2 <= y1:
        return False
    # Liang-Barsky
    dx, dy = s[2] - s[0], s[3] - s[1]
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, s[0] - x1), (dx, x2 - s[0]), (-dy, s[1] - y1), (dy, y2 - s[1])):
        if p == 0:
            if q < 0:
                return False
        else:
            t = q / p
            if p < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
            if t0 > t1:
                return False
    return True


def bild_pruefen(spec: dict, szene: Szene) -> list[Befund]:
    b: list[Befund] = []
    z, ctx = szene.zeichnung, szene.ctx
    namen = szene.namen
    spec = szene.spec or spec

    def wer(i: int) -> str:
        return namen[i] if 0 <= i < len(namen) else "Fußzeile"

    for t in ctx.teile:
        x1, y1, x2, y2 = t.box
        if x1 < -TOLERANZ or y1 < -TOLERANZ or x2 > z.breite + TOLERANZ or y2 > float(spec["hoehe"]) + TOLERANZ:
            b.append(Befund("❌", f"{wer(t.index)} liegt (teilweise) außerhalb des Bildes "
                                  f"({z.breite:g} × {float(spec['hoehe']):g}) – Rahmen {x1:.0f},{y1:.0f} bis {x2:.0f},{y2:.0f}"))
    gemeldet: set[tuple] = set()
    for i, t in enumerate(z.texte):
        r = (t.x1, t.y1, t.x2, t.y2)
        kurz = t.text.replace("\n", " ")[:30]
        if t.x1 < -TOLERANZ or t.x2 > z.breite + TOLERANZ or t.y1 < -TOLERANZ or t.y2 > z.hoehe + TOLERANZ:
            b.append(Befund("⚠", f"Text „{kurz}“ ({wer(t.teil)}) ragt über den Bildrand hinaus"))
        for u in z.texte[i + 1:]:
            if _schnitt(r, (u.x1, u.y1, u.x2, u.y2)):
                schluessel = (t.text, u.text)
                if schluessel not in gemeldet:
                    gemeldet.add(schluessel)
                    b.append(Befund("⚠", f"Beschriftungen überlappen: „{kurz}“ ({wer(t.teil)}) und "
                                         f"„{u.text.replace(chr(10), ' ')[:30]}“ ({wer(u.teil)})"))
        for teil in ctx.teile:
            if teil.klein and teil.index != t.teil and _schnitt(r, teil.box):
                b.append(Befund("⚠", f"Beschriftung „{kurz}“ ({wer(t.teil)}) liegt auf {wer(teil.index)}"))
        for s in z.segmente:
            if s.teil != t.teil and _segment_im_rahmen((s.x1, s.y1, s.x2, s.y2), r):
                b.append(Befund("⚠", f"Beschriftung „{kurz}“ ({wer(t.teil)}) wird von einer Linie aus "
                                     f"{wer(s.teil)} durchlaufen"))
                break
    for i, text in ctx.warnungen:
        b.append(Befund("⚠", f"{wer(i)}: {text}"))
    if any(isinstance(e, dict) and e.get("typ") == "grafcet_schritt" for e in spec.get("elemente") or []):
        b += _kreuzungen(z)
    for kennung, bm, fkt, name in ctx.legende:
        if not fkt:
            b.append(Befund("⚠", f"Legende: '{kennung}' ohne 'funktion' und 'name' – Spalte Lage/Aufgabe bleibt leer"))
    return b


def _kreuzungen(z: Zeichnung) -> list[Befund]:
    """Wirkverbindungen eines GRAFCET kreuzen sich möglichst nicht."""
    b: list[Befund] = []
    waagerecht = [s for s in z.segmente if abs(s.y1 - s.y2) < 0.5 and abs(s.x1 - s.x2) > 0.5]
    senkrecht = [s for s in z.segmente if abs(s.x1 - s.x2) < 0.5 and abs(s.y1 - s.y2) > 0.5]
    for w in waagerecht:
        for s in senkrecht:
            if w.teil != s.teil and min(w.x1, w.x2) + 1 < s.x1 < max(w.x1, w.x2) - 1 \
                    and min(s.y1, s.y2) + 1 < w.y1 < max(s.y1, s.y2) - 1:
                b.append(Befund("⚠", f"Linien kreuzen sich bei x={s.x1:.0f}, y={w.y1:.0f} – Äste anders anordnen"))
    return b


def pruefe(spec: dict) -> tuple[list[Befund], Szene | None]:
    """Gesamtprüfung. Bei Schemafehlern kein Aufbau (Szene None)."""
    befunde = schema_pruefen(spec)
    if any(x.stufe == "❌" for x in befunde):
        return befunde, None
    try:
        szene = bauen(spec)
    except SpecFehler as e:
        befunde.append(Befund("❌", str(e)))
        return befunde, None
    befunde += bild_pruefen(spec, szene)
    return befunde, szene


# ───────────────────────────── Legende ─────────────────────────────

def legende_markdown(szene: Szene) -> str:
    """Legende (BMK | Betriebsmittel | Lage/Aufgabe) als Markdown-Tabelle."""
    def zelle(s: str) -> str:
        return s.replace("|", "\\|").replace("\n", " ")

    zeilen = ["| Referenzkennzeichen | Betriebsmittel | Lage / Aufgabe |", "|---|---|---|"]
    for kennung, bm, fkt, _name_ in szene.ctx.legende:
        zeilen.append(f"| {zelle(kennung)} | {zelle(bm)} | {zelle(fkt)} |")
    return "\n".join(zeilen) + "\n"
