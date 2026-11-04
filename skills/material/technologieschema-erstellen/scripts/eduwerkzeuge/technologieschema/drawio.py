"""
drawio — Technologieschema als bearbeitbare draw.io-Datei (``.drawio.svg``).

Das SVG allein ist nur ein Bild: Striche ohne Zusammenhang. Für die Weiterarbeit in
diagrams.net (app.diagrams.net, draw.io Desktop, Nextcloud/VS-Code-Erweiterung) baut dieses
Modul aus derselben Szene ein mxGraph-Modell:

* **jedes Bauteil eine Form** (Stencil aus seinen Grundformen) mit **Andockpunkten** an den
  Ankern des Werkzeugs (``unten``, ``an1``, ``spitze`` …) – Verschieben, Drehen, Skalieren,
  Kopieren, Füllung ändern;
* **Beschriftungen als Text** (Kennzeichen fett, Kurzname kursiv), zum Bauteil gruppiert;
* **Linien und Rohre als Verbinder**, die an den Bauteilen hängen und beim Verschieben
  rechtwinklig mitgehen (Rohr als Doppellinie ``shape=link``);
* Kennzeichen und Betriebsmittel als **Daten** der Form (Bearbeiten → Daten bearbeiten).

``drawio_svg`` legt das Modell in das ``content``-Attribut des fertigen SVG: Browser und Word
zeigen das Bild, diagrams.net öffnet die bearbeitbare Fassung.

Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import base64
import math
import re
import urllib.parse
import zlib
from xml.sax.saxutils import escape, quoteattr

from .zeichnung import FUELLUNGEN, LINIEN, Prim, _gruppe, f, textmasse

SCHRIFT = "Helvetica"
GRAU_MUSTER = "#d0d0d0"          # Ersatz für Muster außerhalb von Rechtecken
STRICH = "#000000"
TEXT_VERSATZ = 2.6               # draw.io setzt die Grundlinie unabhängig von der Schriftgröße so viel tiefer (im Viewer gemessen)


# ───────────────────────────── Stencil ─────────────────────────────

def _komprimieren(xml: str) -> str:
    """Wie ``Graph.compress`` in draw.io: encodeURIComponent → raw deflate → Base64."""
    roh = urllib.parse.quote(xml, safe="!*'()").encode("ascii")
    c = zlib.compressobj(9, zlib.DEFLATED, -15)
    return base64.b64encode(c.compress(roh) + c.flush()).decode("ascii")


def entpacken(daten: str) -> str:
    """Gegenstück zu ``_komprimieren`` (für Tests und Prüfungen)."""
    roh = zlib.decompress(base64.b64decode(daten), -15)
    return urllib.parse.unquote(roh.decode("ascii"))


def _linie_attr(linie: str) -> tuple[float, bool]:
    if linie == "keine":
        return 0.0, False
    return LINIEN.get(linie, LINIEN["normal"]), linie == "gestrichelt"


def _stift(out: list[str], linie: str, fuellfarbe: str | None) -> tuple[bool, bool]:
    """Strich- und Füllzustand setzen; gibt (füllen, strich) zurück."""
    breite, gestrichelt = _linie_attr(linie)
    if breite:
        out.append(f'<strokecolor color="{STRICH}"/><strokewidth width="{f(breite)}" fixed="1"/>'
                   f'<dashed dashed="{1 if gestrichelt else 0}"/>')
        if gestrichelt:   # Muster in Vielfachen der Strichbreite (wie das SVG: 6 4 Pixel)
            out.append(f'<dashpattern pattern="{f(6 / breite)} {f(4 / breite)}"/>')
    if fuellfarbe:
        out.append(f'<fillcolor color="{fuellfarbe}"/>')
    return bool(fuellfarbe), bool(breite)


def _op(fuellen: bool, strich: bool) -> str:
    if fuellen and strich:
        return "<fillstroke/>"
    if fuellen:
        return "<fill/>"
    return "<stroke/>" if strich else ""


def _farbe(fuellung: str) -> str | None:
    if fuellung in FUELLUNGEN:
        return None if fuellung == "keine" else FUELLUNGEN[fuellung]
    return GRAU_MUSTER


def _clip(x1, y1, x2, y2, r):
    """Strecke auf Rechteck r beschneiden (Liang-Barsky); None, wenn außerhalb."""
    dx, dy = x2 - x1, y2 - y1
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x1 - r[0]), (dx, r[2] - x1), (-dy, y1 - r[1]), (dy, r[3] - y1)):
        if p == 0:
            if q < 0:
                return None
            continue
        t = q / p
        if p < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 >= t1:
            return None
    return x1 + t0 * dx, y1 + t0 * dy, x1 + t1 * dx, y1 + t1 * dy


def _muster(out: list[str], art: str, r, P) -> None:
    """Schraffur bzw. Mauerwerk eines Rechtecks als Linien nachbilden."""
    striche = []
    if art == "schraffur":
        b = r[2] - r[0] + r[3] - r[1]
        c = -b
        while c < b:
            s = _clip(r[0] + c, r[1], r[0] + c + (r[3] - r[1]), r[3], r)
            if s:
                striche.append(s)
            c += 6 * math.sqrt(2)
        farbe, breite = "#555555", 1.2
    elif art == "ziegel":
        y, reihe = r[1], 0
        while y < r[3]:
            striche.append((r[0], y, r[2], y))
            x = r[0] + (0 if reihe % 2 == 0 else 14)
            while x <= r[2]:
                striche.append((x, y, x, min(y + 12, r[3])))
                x += 28
            y += 12
            reihe += 1
        farbe, breite = "#777777", 1.0
    else:
        return
    out.append(f'<strokecolor color="{farbe}"/><strokewidth width="{f(breite)}" fixed="1"/><dashed dashed="0"/>')
    out.append("<path>" + "".join(f'<move x="{f(P(a, b)[0])}" y="{f(P(a, b)[1])}"/><line x="{f(P(c, d)[0])}" '
                                  f'y="{f(P(c, d)[1])}"/>' for a, b, c, d in striche) + "</path><stroke/>")


def _pfad(punkte, P, geschlossen=False, radius=0.0) -> str:
    pts = [P(*p) for p in punkte]
    teile = [f'<move x="{f(pts[0][0])}" y="{f(pts[0][1])}"/>']
    if radius > 0 and len(pts) > 2:
        for i in range(1, len(pts) - 1):
            p0, p1, p2 = pts[i - 1], pts[i], pts[i + 1]
            r = min(radius, math.dist(p0, p1) / 2, math.dist(p1, p2) / 2)
            a = _richtung(p1, p0, r)
            b = _richtung(p1, p2, r)
            teile.append(f'<line x="{f(a[0])}" y="{f(a[1])}"/><quad x1="{f(p1[0])}" y1="{f(p1[1])}" '
                         f'x2="{f(b[0])}" y2="{f(b[1])}"/>')
        teile.append(f'<line x="{f(pts[-1][0])}" y="{f(pts[-1][1])}"/>')
    else:
        teile += [f'<line x="{f(x)}" y="{f(y)}"/>' for x, y in pts[1:]]
    if geschlossen:
        teile.append("<close/>")
    return "<path>" + "".join(teile) + "</path>"


def _richtung(p, q, laenge):
    d = math.dist(p, q) or 1.0
    return p[0] + (q[0] - p[0]) / d * laenge, p[1] + (q[1] - p[1]) / d * laenge


def _pfeil(out: list[str], spitze, basis, P) -> None:
    a = math.atan2(spitze[1] - basis[1], spitze[0] - basis[0])
    px, py = -math.sin(a) * 3.6, math.cos(a) * 3.6
    b = (spitze[0] - math.cos(a) * 9, spitze[1] - math.sin(a) * 9)
    out.append(f'<fillcolor color="{STRICH}"/>' + _pfad([spitze, (b[0] + px, b[1] + py), (b[0] - px, b[1] - py)],
                                                         P, True) + "<fill/>")


def rahmen(prims: list[Prim]) -> tuple[float, float, float, float]:
    xs, ys = [], []
    for p in prims:
        d = p.d
        if p.art == "rechteck":
            xs += [d["x1"], d["x2"]]
            ys += [d["y1"], d["y2"]]
        elif p.art == "kreis":
            xs += [d["cx"] - d["r"], d["cx"] + d["r"]]
            ys += [d["cy"] - d["r"], d["cy"] + d["r"]]
        else:
            xs += [q[0] for q in d["punkte"]]
            ys += [q[1] for q in d["punkte"]]
    return min(xs), min(ys), max(xs), max(ys)


def stencil_xml(prims: list[Prim], box, anker: dict[str, tuple[float, float]] | None = None,
                name: str = "Bauteil") -> str:
    """Grundformen (Bildkoordinaten) als draw.io-Stencil im Rahmen ``box``."""
    bx, by = box[0], box[1]
    w, h = max(box[2] - bx, 1.0), max(box[3] - by, 1.0)
    P = lambda x, y: (x - bx, y - by)  # noqa: E731
    out: list[str] = []
    for p in prims:
        d = p.d
        if p.art == "rechteck":
            muster = d["fuellung"] in ("schraffur", "ziegel")
            r = (d["x1"], d["y1"], d["x2"], d["y2"])
            x1, y1 = P(d["x1"], d["y1"])
            rw, rh = d["x2"] - d["x1"], d["y2"] - d["y1"]
            if d["rundung"]:
                rr = min(d["rundung"], rw / 2, rh / 2)
                form = (f'<path><move x="{f(x1 + rr)}" y="{f(y1)}"/><line x="{f(x1 + rw - rr)}" y="{f(y1)}"/>'
                        f'<arc rx="{f(rr)}" ry="{f(rr)}" x-axis-rotation="0" large-arc-flag="0" sweep-flag="1" '
                        f'x="{f(x1 + rw)}" y="{f(y1 + rr)}"/><line x="{f(x1 + rw)}" y="{f(y1 + rh - rr)}"/>'
                        f'<arc rx="{f(rr)}" ry="{f(rr)}" x-axis-rotation="0" large-arc-flag="0" sweep-flag="1" '
                        f'x="{f(x1 + rw - rr)}" y="{f(y1 + rh)}"/><line x="{f(x1 + rr)}" y="{f(y1 + rh)}"/>'
                        f'<arc rx="{f(rr)}" ry="{f(rr)}" x-axis-rotation="0" large-arc-flag="0" sweep-flag="1" '
                        f'x="{f(x1)}" y="{f(y1 + rh - rr)}"/><line x="{f(x1)}" y="{f(y1 + rr)}"/>'
                        f'<arc rx="{f(rr)}" ry="{f(rr)}" x-axis-rotation="0" large-arc-flag="0" sweep-flag="1" '
                        f'x="{f(x1 + rr)}" y="{f(y1)}"/><close/></path>')
            else:
                form = f'<rect x="{f(x1)}" y="{f(y1)}" w="{f(rw)}" h="{f(rh)}"/>'
            if muster:
                out.append(f'<fillcolor color="#ffffff"/>{form}<fill/>')
                _muster(out, d["fuellung"], r, P)
                fuellen, strich = _stift(out, d["linie"], None)
            else:
                fuellen, strich = _stift(out, d["linie"], _farbe(d["fuellung"]))
            out.append(form + _op(fuellen, strich))
        elif p.art == "kreis":
            fuellen, strich = _stift(out, d["linie"], _farbe(d["fuellung"]))
            x, y = P(d["cx"] - d["r"], d["cy"] - d["r"])
            out.append(f'<ellipse x="{f(x)}" y="{f(y)}" w="{f(2 * d["r"])}" h="{f(2 * d["r"])}"/>'
                       + _op(fuellen, strich))
        elif p.art == "polygon":
            fuellen, strich = _stift(out, d["linie"], _farbe(d["fuellung"]) if d["geschlossen"] else None)
            out.append(_pfad(d["punkte"], P, d["geschlossen"]) + _op(fuellen, strich))
        elif p.art in ("linie", "zug", "rohr"):
            pts = list(d["punkte"])
            pfeil = d.get("pfeil", "kein")
            if p.art == "rohr":
                aussen = d["weite"] + 2 * LINIEN["normal"]
                out.append(f'<strokecolor color="{STRICH}"/><strokewidth width="{f(aussen)}" fixed="1"/>'
                           f'<dashed dashed="0"/>' + _pfad(pts, P, radius=d["radius"]) + "<stroke/>")
                out.append(f'<strokecolor color="#ffffff"/><strokewidth width="{f(d["weite"])}" fixed="1"/>'
                           + _pfad(pts, P, radius=d["radius"]) + "<stroke/>")
                continue
            ende, anfang = pts[-1], pts[0]
            if pfeil in ("ende", "beide"):
                pts[-1] = _richtung(pts[-1], pts[-2], min(9.0, math.dist(pts[-1], pts[-2]) * 0.9))
            if pfeil in ("anfang", "beide"):
                pts[0] = _richtung(pts[0], pts[1], min(9.0, math.dist(pts[0], pts[1]) * 0.9))
            fuellen, strich = _stift(out, d["linie"], None)
            out.append('<linejoin join="round"/>' + _pfad(pts, P, radius=d.get("radius", 0.0)) + _op(False, strich))
            if pfeil in ("ende", "beide"):
                _pfeil(out, ende, pts[-1], P)
            if pfeil in ("anfang", "beide"):
                _pfeil(out, anfang, pts[0], P)
    verbindungen = ""
    if anker:
        verbindungen = "<connections>" + "".join(
            f'<constraint x="{_rel(x - bx, w)}" y="{_rel(y - by, h)}" perimeter="0" name="{escape(n)}"/>'
            for n, (x, y) in anker.items()) + "</connections>"
    return (f'<shape name={quoteattr(name)} w="{f(w)}" h="{f(h)}" aspect="variable" strokewidth="inherit">'
            f'{verbindungen}<foreground>{"".join(out)}</foreground></shape>')


def _rel(v: float, g: float) -> str:
    return ("%.4f" % (v / g)).rstrip("0").rstrip(".") if g else "0"


# ───────────────────────────── Modell ─────────────────────────────

def _drehe(p, drehung, rueck=False):
    if not drehung:
        return p
    w, cx, cy = drehung
    a = math.radians(-w if rueck else w)
    dx, dy = p[0] - cx, p[1] - cy
    return cx + dx * math.cos(a) - dy * math.sin(a), cy + dx * math.sin(a) + dy * math.cos(a)


def _himmelsrichtung(von, nach) -> str | None:
    dx, dy = nach[0] - von[0], nach[1] - von[1]
    if abs(dx) < 0.5 and abs(dy) < 0.5:
        return None
    if abs(dx) >= abs(dy):
        return "east" if dx > 0 else "west"
    return "south" if dy > 0 else "north"


def _textzelle(d: dict) -> tuple[tuple[float, float, float, float], str, str]:
    """Rahmen, Wert (HTML) und Stil eines Textes; Grundlinie wie im SVG."""
    zeilen = d["text"].split("\n")
    g = d["groesse"]
    b, _ = textmasse(d["text"], g, d["fett"])
    b += 4
    h = g * 1.2 * len(zeilen)
    x = {"start": d["x"] - 2, "middle": d["x"] - b / 2, "end": d["x"] - b + 2}[d["anker"]]
    y = d["y"] - 0.95 * g - TEXT_VERSATZ
    ausr = {"start": "left", "middle": "center", "end": "right"}[d["anker"]]
    stil = (f"text;html=1;align={ausr};verticalAlign=top;whiteSpace=nowrap;spacing=0;spacingLeft=2;"
            f"spacingRight=2;fontFamily={SCHRIFT};fontSize={f(g)};fontStyle={(1 if d['fett'] else 0) + (2 if d['kursiv'] else 0)};"
            "fontColor=#000000;fillColor=none;strokeColor=none;")
    if d.get("spans"):   # Negation als Überstrich, „immer erfüllt“ unterstrichen
        wert = "".join(f'<span style="text-decoration: {deko}">{escape(t)}</span>' if deko else escape(t)
                       for t, deko in d["spans"])
    else:
        wert = "<br>".join(escape(z) for z in zeilen)
    return (x, y, x + b, y + h), wert, stil


def _geo(box, ursprung=(0.0, 0.0)) -> str:
    return (f'<mxGeometry x="{f(box[0] - ursprung[0])}" y="{f(box[1] - ursprung[1])}" '
            f'width="{f(max(box[2] - box[0], 1))}" height="{f(max(box[3] - box[1], 1))}" as="geometry"/>')


def _zellen_ordnen(prims: list[Prim]) -> dict[str, list[Prim]]:
    zellen: dict[str, list[Prim]] = {}
    for p in prims:
        zellen.setdefault(p.zelle, []).append(p)
    return zellen


def modell(szene, spec: dict) -> str:
    """mxfile-XML (unkomprimiert) der Szene."""
    z, ctx = szene.zeichnung, szene.ctx
    spec = szene.spec or spec          # aufgelöst: typ grafcet ist hier schon in Einzelteile umgesetzt
    elemente = spec.get("elemente", [])
    zellen = _zellen_ordnen(z.prims)

    # Zelle → Daten (Kennzeichen, Betriebsmittel) aus der Legende
    legende = {k: (bm, fkt) for k, bm, fkt, _ in ctx.legende}
    kennung_der_zelle = {zelle: kennung for kennung, zelle in ctx.zelle_von.items() if kennung in legende}

    knoten: dict[str, tuple] = {}          # Zelle → (Zell-ID, Rahmen, Drehung)
    gruppen: dict[str, list[tuple]] = {}   # Gruppe → [(id, box, xml-Funktion)]
    kanten_xml: list[str] = []
    zaehler = 0

    def neue_id(basis: str) -> str:
        nonlocal zaehler
        zaehler += 1
        return f"{basis}-{zaehler}"

    for zelle, ps in zellen.items():
        gruppe = _gruppe(zelle)
        i = int(gruppe[1:]) if gruppe.startswith("e") and gruppe[1:].isdigit() else None
        typ = elemente[i].get("typ") if i is not None and i < len(elemente) else None
        kante = ctx.kanten.get(zelle)
        geo = [p for p in ps if p.art != "text" and not (kante and p.art in ("zug", "rohr"))]
        texte = []
        for p in ps:
            if p.art == "text":
                box, wert, stil = _textzelle(p.d)
                tid = neue_id(f"{zelle}-text")
                texte.append(
                    (tid, box, lambda o, tid=tid, wert=wert, stil=stil, box=box:
                     f'<mxCell id="{tid}" value={quoteattr(wert)} style="{stil}" vertex="1" parent="{o[0]}">'
                     f'{_geo(box, o[1])}</mxCell>'))
        if geo:
            # auf ganze Pixel erweitern: draw.io rundet Formgrenzen, sonst Versatz zwischen Form und Linie
            x1, y1, x2, y2 = rahmen(geo)
            box = (math.floor(x1), math.floor(y1), max(math.ceil(x2), math.floor(x1) + 1),
                   max(math.ceil(y2), math.floor(y1) + 1))
            drehung = z.drehungen.get(zelle)
            anker = {n: _drehe(pt, drehung, rueck=True) for n, pt in (ctx.zellen_anker.get(zelle) or {}).items()}
            name = kennung_der_zelle.get(zelle) or (typ or "Teil")
            xml = stencil_xml(geo, box, anker, name)
            # strokeWidth=2 (gerade): sonst verschiebt draw.io die Form um ½ Pixel gegen die Linien (1,6 → 2);
            # die Strichbreiten selbst stehen fest im Stencil
            stil = (f"shape=stencil({_komprimieren(xml)});html=1;whiteSpace=wrap;fillColor=#ffffff;"
                    "strokeColor=#000000;strokeWidth=2;")
            if drehung:
                stil += f"rotation={f(drehung[0])};"
            if typ == "symbol":
                stil += "aspect=fixed;"
            vid = zelle
            kennung = kennung_der_zelle.get(zelle)
            knoten[zelle] = (vid, box, drehung)

            def vertex(o, vid=vid, stil=stil, box=box, kennung=kennung, typ=typ):
                zelle_xml = f'<mxCell style="{stil}" vertex="1" parent="{o[0]}">{_geo(box, o[1])}</mxCell>'
                if kennung:
                    bm, fkt = legende[kennung]
                    return (f'<object label="" id="{vid}" Referenzkennzeichen={quoteattr(kennung)} '
                            f'Betriebsmittel={quoteattr(bm)} Aufgabe={quoteattr(fkt)} '
                            f'tooltip={quoteattr(f"{kennung} – {bm}" + (f" ({fkt})" if fkt else ""))}>'
                            f'{zelle_xml}</object>')
                return zelle_xml.replace("<mxCell ", f'<mxCell id="{vid}" ', 1)
            gruppen.setdefault(gruppe, []).append((vid, box, vertex))
        if texte:
            gruppen.setdefault(gruppe, []).extend(texte)     # Texte über der Form (z. B. „M 3~“ im Motor)

    # Gruppen ausgeben: ein Teil allein direkt, mehrere als draw.io-Gruppe
    zell_xml: list[str] = []
    for gruppe, teile in gruppen.items():
        if len(teile) == 1:
            zell_xml.append(teile[0][2](("1", (0.0, 0.0))))
            continue
        gx1 = min(t[1][0] for t in teile)
        gy1 = min(t[1][1] for t in teile)
        gbox = (gx1, gy1, max(t[1][2] for t in teile), max(t[1][3] for t in teile))
        gid = f"{gruppe}-gruppe"
        zell_xml.append(f'<mxCell id="{gid}" value="" style="group" vertex="1" connectable="0" parent="1">'
                        f'{_geo(gbox)}</mxCell>')
        zell_xml += [t[2]((gid, (gx1, gy1))) for t in teile]

    # Verbindungen
    for zelle, k in ctx.kanten.items():
        pts = k["punkte"]
        teile_stil = ["html=1", f"strokeColor={STRICH}"]
        if k["art"] == "rohr":
            teile_stil += ["edgeStyle=orthogonalEdgeStyle", "shape=link", f"width={f(k['weite'] + LINIEN['normal'])}",
                           f"strokeWidth={f(LINIEN['normal'])}", "rounded=1" if k["radius"] else "rounded=0",
                           "endArrow=none", "startArrow=none"]
        else:
            breite, gestrichelt = _linie_attr(k["stil"])
            teile_stil += ["edgeStyle=none" if k.get("schraeg") else "edgeStyle=orthogonalEdgeStyle",
                           "rounded=1" if k.get("radius") else "rounded=0", f"strokeWidth={f(breite or 1)}"]
            if gestrichelt:
                teile_stil += ["dashed=1", "dashPattern=6 4", "fixDash=1"]
            pfeil = k.get("pfeil", "kein")
            teile_stil += [f"endArrow={'block' if pfeil in ('ende', 'beide') else 'none'}",
                           f"startArrow={'block' if pfeil in ('anfang', 'beide') else 'none'}",
                           "endFill=1", "startFill=1", "endSize=8", "startSize=8"]
        verweis = ""
        for rolle, kennung, pt in (("source", k["von"], pts[0]), ("target", k["nach"], pts[-1])):
            # Richtung des ersten bzw. letzten Teilstücks vom Anschluss weg: draw.io führt die Linie dort
            # heraus, statt sie erst senkrecht zum Formrand abzuknicken
            nachbar = pts[1] if rolle == "source" else pts[-2]
            richtung = _himmelsrichtung(pt, nachbar)
            zz = ctx.zelle_von.get(kennung) if kennung else None
            if zz is None and rolle == "source" and k.get("etikett"):
                # Hinweislinie eines Etiketts: am Etikett-Text beginnen
                zz = next((t for t in gruppen.get(zelle, [])), None)
                if zz:
                    tid, tbox, _ = zz
                    rx, ry = _rel(pt[0] - tbox[0], tbox[2] - tbox[0]), _rel(pt[1] - tbox[1], tbox[3] - tbox[1])
                    verweis += f' source="{tid}"'
                    teile_stil += [f"exitX={rx}", f"exitY={ry}", "exitDx=0", "exitDy=0", "exitPerimeter=0"]
                    if richtung:
                        teile_stil.append(f"sourcePortConstraint={richtung}")
                continue
            if zz is None or zz not in knoten:
                continue
            vid, box, drehung = knoten[zz]
            q = _drehe(pt, drehung, rueck=True)
            w, h = max(box[2] - box[0], 1.0), max(box[3] - box[1], 1.0)
            pre = "exit" if rolle == "source" else "entry"
            verweis += f' {rolle}="{vid}"'
            teile_stil += [f"{pre}X={_rel(q[0] - box[0], w)}", f"{pre}Y={_rel(q[1] - box[1], h)}",
                           f"{pre}Dx=0", f"{pre}Dy=0", f"{pre}Perimeter=0"]
            if richtung and not drehung:
                teile_stil.append(f"{rolle}PortConstraint={richtung}")
        # Stützpunkte: draw.io nimmt dann den Segment-Router und übernimmt den Verlauf genau; ohne sie
        # führt der Orthogonal-Router die Linie erst senkrecht vom Formrand weg (Haken an Anschlüssen)
        stuetz = pts[1:-1] or [((pts[0][0] + pts[-1][0]) / 2, (pts[0][1] + pts[-1][1]) / 2)]
        punkte = "".join(f'<mxPoint x="{f(x)}" y="{f(y)}"/>' for x, y in stuetz)
        kanten_xml.append(
            f'<mxCell id="{zelle}-linie" value="" style="{";".join(teile_stil)};" edge="1" parent="1"{verweis}>'
            f'<mxGeometry relative="1" as="geometry">'
            f'<mxPoint x="{f(pts[0][0])}" y="{f(pts[0][1])}" as="sourcePoint"/>'
            f'<mxPoint x="{f(pts[-1][0])}" y="{f(pts[-1][1])}" as="targetPoint"/>'
            + (f'<Array as="points">{punkte}</Array>' if punkte else "") + "</mxGeometry></mxCell>")

    inhalt = "".join(['<mxCell id="0"/>', '<mxCell id="1" parent="0"/>'] + zell_xml + kanten_xml)
    titel = escape(str(spec.get("titel", "Technologieschema")), {'"': "&quot;"})
    b, h = int(math.ceil(z.breite)), int(math.ceil(z.hoehe))
    return ('<mxfile host="edu-technologieschema" type="device">'
            f'<diagram id="technologieschema" name="{titel}">'
            f'<mxGraphModel dx="{b}" dy="{h}" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" '
            f'fold="1" page="1" pageScale="1" pageWidth="{b}" pageHeight="{h}" background="#ffffff" math="0" shadow="0">'
            f"<root>{inhalt}</root></mxGraphModel></diagram></mxfile>")


def drawio_svg(szene, spec: dict) -> str:
    """Fertiges SVG mit eingebettetem draw.io-Modell (``content``-Attribut)."""
    svg = szene.svg
    m = re.search(r"<svg\b", svg)
    inhalt = escape(modell(szene, spec), {'"': "&quot;"})     # wie draw.io selbst: content="…"
    return svg[:m.end()] + f' content="{inhalt}"' + svg[m.end():]
