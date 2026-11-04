"""Farbgebung für Edumaps: eigene Themes und Farben aus Ausgangsmaterial.

Ein eigenes Theme (Mapping statt Theme-Name, auch als YAML-Datei) legt die
Standardfarben einer Quelle auf die Farben eines Ausgangsmaterials um – die
Quelle selbst bleibt unverändert:

    theme:
      basis: tageslicht            # optional: Vorgaben eines eingebauten Themes
      hintergrund: "#eef3f8"       # Name oder #rrggbb (Alias: mapbg)
      pfade: [farbe1, farbe2]      # ersetzen die Standardfarben der Reihe nach
      karten: pfad                 # optional: Karten ohne Farbe in Pfadfarbe
      farben:                      # eigene Farbnamen (für color=, box_color=)
        farbe1: "#1f4e79"
        farbe2: "#c55a11"

``farben_aus(quelle)`` liest Farben aus Präsentation, Dokument, Webseite, CSS,
SVG, Bild oder PDF; ``theme_vorschlag`` macht daraus ein lesbares Theme
(Pfadfarben mit mindestens 3:1 Kontrast zu weißer Schrift), ``theme_yaml``
schreibt es als YAML-Block.
"""

from __future__ import annotations

import colorsys
import re
import shutil
import subprocess
import tempfile
import urllib.parse
import urllib.request
import zipfile
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path

#: Kontrast, den Pfad- und Kartenfarben zu weißer Titelschrift mindestens haben
#: (WCAG für große Schrift; die eingebauten Farben liegen ab 3,2:1).
MIN_KONTRAST = 3.0

THEME_SCHLUESSEL = {"basis", "hintergrund", "mapbg", "pfade", "karten", "farben"}

HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")


# ---------------------------------------------------------------------------
# Farbrechnung
# ---------------------------------------------------------------------------

def normiere_hex(wert: str) -> str | None:
    """'#abc', 'ABCDEF', '#aabbccdd' → '#aabbcc' (klein); sonst None."""
    w = str(wert).strip().lstrip("#")
    if re.fullmatch(r"[0-9a-fA-F]{3}", w):
        w = "".join(c * 2 for c in w)
    elif re.fullmatch(r"[0-9a-fA-F]{8}", w):
        w = w[:6]
    if not re.fullmatch(r"[0-9a-fA-F]{6}", w):
        return None
    return "#" + w.lower()


def _rgb(hexwert: str) -> tuple[int, int, int]:
    h = hexwert.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _hex(r: float, g: float, b: float) -> str:
    return "#" + "".join(f"{max(0, min(255, round(c))):02x}" for c in (r, g, b))


def leuchtdichte(hexwert: str) -> float:
    """Relative Leuchtdichte nach WCAG 2."""
    def kanal(c: int) -> float:
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = _rgb(hexwert)
    return 0.2126 * kanal(r) + 0.7152 * kanal(g) + 0.0722 * kanal(b)


def kontrast(a: str, b: str = "#ffffff") -> float:
    la, lb = sorted((leuchtdichte(a), leuchtdichte(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _hls(hexwert: str) -> tuple[float, float, float]:
    r, g, b = _rgb(hexwert)
    return colorsys.rgb_to_hls(r / 255, g / 255, b / 255)


def _aus_hls(h: float, l: float, s: float) -> str:
    r, g, b = colorsys.hls_to_rgb(h, max(0.0, min(1.0, l)), s)
    return _hex(r * 255, g * 255, b * 255)


def mischen(a: str, b: str, anteil_b: float) -> str:
    ra, ga, ba = _rgb(a)
    rb, gb, bb = _rgb(b)
    t = anteil_b
    return _hex(ra + (rb - ra) * t, ga + (gb - ga) * t, ba + (bb - ba) * t)


def lesbar(hexwert: str, ziel: float = MIN_KONTRAST) -> str:
    """Dunkelt eine Farbe (gleicher Farbton) ab, bis weiße Schrift `ziel` erreicht."""
    if kontrast(hexwert) >= ziel:
        return hexwert
    h, l, s = _hls(hexwert)
    while l > 0:
        l -= 0.01
        neu = _aus_hls(h, l, s)
        if kontrast(neu) >= ziel:
            return neu
    return "#000000"


def _abstand(a: str, b: str) -> float:
    return sum((x - y) ** 2 for x, y in zip(_rgb(a), _rgb(b))) ** 0.5


def _gleicher_ton(a: str, b: str) -> bool:
    """Gleicher Farbton bei ähnlicher Helligkeit – als Pfadfarben kaum zu unterscheiden."""
    ha, la, _ = _hls(a)
    hb, lb, _ = _hls(b)
    dh = min(abs(ha - hb), 1 - abs(ha - hb))
    return dh < 0.03 and abs(la - lb) < 0.15


def ist_bunt(hexwert: str) -> bool:
    h, l, s = _hls(hexwert)
    return s >= 0.25 and 0.12 < l < 0.9


# ---------------------------------------------------------------------------
# Eigene Themes
# ---------------------------------------------------------------------------

@dataclass
class Farbgebung:
    """Aufgelöstes Theme: Hintergrund, Standard-Pfadfarbe und Farbtausch."""
    mapbg: str | None
    standard_pfad: str
    pfade: list[str]          # Ersatzfarben für Standardfarben, der Reihe nach
    karten: str | None        # None | "pfad" | Hex
    farben: dict[str, str]    # eigene Namen → Hex

    @property
    def tauscht(self) -> bool:
        return bool(self.pfade)


def lade_theme_datei(pfad: Path) -> dict:
    import yaml  # PyYAML ist Abhängigkeit des Pakets

    daten = yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}
    if isinstance(daten, dict) and isinstance(daten.get("theme"), dict):
        daten = daten["theme"]
    if not isinstance(daten, dict):
        raise ValueError(f"Theme-Datei {pfad} enthält kein Mapping (hintergrund, pfade, farben …)")
    return daten


def farbgebung(spec, palette: dict[str, str], themes: dict[str, dict[str, str]],
               standard_pfad: str, basis_dir: Path | None = None) -> Farbgebung:
    """Löst theme: auf – Name eines eingebauten Themes, YAML-Datei oder Mapping."""
    def name_zu_hex(wert, eigene: dict[str, str]) -> str | None:
        if wert in (None, ""):
            return None
        w = str(wert).strip()
        if w.startswith("#"):
            return normiere_hex(w) or w
        return eigene.get(w.lower()) or palette.get(w.lower()) or w

    if spec in (None, ""):
        return Farbgebung(None, standard_pfad, [], None, {})

    if isinstance(spec, str):
        name = spec.strip()
        if name.lower().endswith((".yaml", ".yml")):
            datei = Path(name)
            if not datei.is_absolute() and basis_dir is not None:
                datei = basis_dir / datei
            if not datei.is_file():
                raise ValueError(f"Theme-Datei nicht gefunden: {datei}")
            return farbgebung(lade_theme_datei(datei), palette, themes, standard_pfad, datei.parent)
        t = themes.get(name.lower(), {})
        return Farbgebung(palette.get(t["mapbg"]) if t else None,
                          palette.get(t.get("path_color", ""), standard_pfad) if t else standard_pfad,
                          [], None, {})

    if not isinstance(spec, dict):
        raise ValueError("theme: muss ein Theme-Name, eine YAML-Datei oder ein Mapping sein")
    unbekannt = set(spec) - THEME_SCHLUESSEL
    if unbekannt:
        raise ValueError(f"theme: unbekannte Schlüssel {', '.join(sorted(unbekannt))} – "
                         f"erlaubt: {', '.join(sorted(THEME_SCHLUESSEL))}")

    basis = farbgebung(spec.get("basis"), palette, themes, standard_pfad, basis_dir)
    eigene: dict[str, str] = {}
    for name, wert in (spec.get("farben") or {}).items():
        hexwert = normiere_hex(str(wert)) or palette.get(str(wert).lower())
        if not hexwert:
            raise ValueError(f"theme.farben.{name}: '{wert}' ist weder #rrggbb noch Farbname")
        eigene[str(name).lower()] = hexwert

    pfade_roh = spec.get("pfade") or []
    if isinstance(pfade_roh, str):
        pfade_roh = [pfade_roh]
    pfade = [name_zu_hex(p, eigene) for p in pfade_roh]

    karten_roh = spec.get("karten")
    if karten_roh in (None, "", "keine"):
        karten = None
    elif str(karten_roh).lower() == "pfad":
        karten = "pfad"
    else:
        karten = name_zu_hex(karten_roh, eigene)

    hintergrund = name_zu_hex(spec.get("hintergrund") or spec.get("mapbg"), eigene) or basis.mapbg
    return Farbgebung(hintergrund, basis.standard_pfad, pfade, karten, eigene)


# ---------------------------------------------------------------------------
# Farben aus Ausgangsmaterial
# ---------------------------------------------------------------------------

@dataclass
class Fund:
    hex: str
    gewicht: float
    herkunft: str


_OOXML = (".pptx", ".potx", ".pptm", ".docx", ".dotx", ".docm", ".xlsx", ".xltx", ".xlsm", ".thmx")
_ODF = (".odp", ".otp", ".odt", ".ott", ".ods", ".ots", ".odg")
_BILD = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".bmp")
_CSS_FARBE = re.compile(r"#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b"
                        r"|rgba?\(\s*(\d{1,3})[\s,]+(\d{1,3})[\s,]+(\d{1,3})")
_CSS_VARIABLE = re.compile(r"--[\w-]*(?:primar|primär|primary|brand|accent|akzent|main|haupt|theme|"
                           r"secondary|sekund|highlight)[\w-]*\s*:\s*([^;}\n]+)", re.I)


def farben_aus(quelle: str | Path) -> list[Fund]:
    """Liest die Farben eines Ausgangsmaterials, nach Bedeutung gewichtet.

    Unterstützt: Office (.pptx/.docx/.xlsx + Vorlagen, Design-Farben und verwendete
    Farben), OpenDocument (.odp/.odt/.ods), HTML/CSS/SVG (Datei oder http(s)-Adresse,
    verlinkte Stylesheets werden mitgelesen), Bilder und PDF (brauchen Pillow, PDF
    zusätzlich pdftoppm aus poppler).
    """
    q = str(quelle)
    if q.startswith(("http://", "https://")):
        return _aus_web(q)
    pfad = Path(q)
    if not pfad.is_file():
        raise FileNotFoundError(f"Ausgangsmaterial nicht gefunden: {pfad}")
    endung = pfad.suffix.lower()
    if endung in _OOXML:
        return _aus_ooxml(pfad)
    if endung in _ODF:
        return _aus_odf(pfad)
    if endung in (".html", ".htm"):
        return _aus_html(pfad.read_text(encoding="utf-8", errors="replace"), pfad.parent, None)
    if endung in (".css", ".svg", ".scss", ".md", ".yaml", ".yml", ".txt"):
        return _aus_css(pfad.read_text(encoding="utf-8", errors="replace"), pfad.name)
    if endung in _BILD:
        return _aus_bild(pfad)
    if endung == ".pdf":
        return _aus_pdf(pfad)
    raise ValueError(f"Format {endung or '(ohne Endung)'} wird nicht unterstützt – Präsentation, "
                     "Dokument, Webseite/CSS, SVG, Bild oder PDF angeben")


def _zaehlen(funde: Counter, herkunft: dict[str, str], gewicht_je: float = 1.0) -> list[Fund]:
    return [Fund(h, n * gewicht_je, herkunft.get(h, "")) for h, n in funde.items()]


def _aus_ooxml(pfad: Path) -> list[Fund]:
    with zipfile.ZipFile(pfad) as z:
        namen = z.namelist()
        theme_dateien = sorted(n for n in namen if re.search(r"theme/theme\d*\.xml$", n))
        schema: dict[str, str] = {}
        if theme_dateien:
            xml = z.read(theme_dateien[0]).decode("utf-8", errors="replace")
            m = re.search(r"<a:clrScheme[^>]*>(.*?)</a:clrScheme>", xml, re.S)
            for rolle, inhalt in re.findall(r"<a:(dk1|lt1|dk2|lt2|accent[1-6])>(.*?)</a:\1>",
                                            m.group(1) if m else "", re.S):
                wert = re.search(r'(?:srgbClr val|lastClr)="([0-9A-Fa-f]{6})"', inhalt)
                if wert:
                    schema[rolle] = "#" + wert.group(1).lower()
        inhalt = [n for n in namen if n.endswith(".xml") and "theme/" not in n
                  and re.match(r"(ppt|word|xl)/", n)]
        direkt: Counter = Counter()
        rollen: Counter = Counter()
        for n in inhalt:
            xml = z.read(n).decode("utf-8", errors="replace")
            for v in re.findall(r'<a:srgbClr val="([0-9A-Fa-f]{6})"', xml):
                direkt["#" + v.lower()] += 1
            for v in re.findall(r'w:(?:color|fill) w:val="([0-9A-Fa-f]{6})"', xml):
                direkt["#" + v.lower()] += 1
            for v in re.findall(r'w:fill="([0-9A-Fa-f]{6})"', xml):
                direkt["#" + v.lower()] += 1
            for v in re.findall(r'<a:schemeClr val="(accent[1-6]|dk2|lt2|tx2|bg2)"', xml):
                rollen[{"tx2": "dk2", "bg2": "lt2"}.get(v, v)] += 1
            for v in re.findall(r'w:themeColor="(accent[1-6]|text2|background2)"', xml):
                rollen[{"text2": "dk2", "background2": "lt2"}.get(v, v)] += 1
    funde = [Fund(h, n, "verwendet") for h, n in direkt.items()]
    for i, rolle in enumerate(("accent1", "accent2", "accent3", "accent4", "accent5", "accent6",
                               "dk2", "lt2")):
        if rolle in schema:
            # Design-Farben zählen auch ohne Verwendung, accent1 vor accent2 …
            funde.append(Fund(schema[rolle], 3 + rollen[rolle] - i * 0.3, f"Design-Farbe {rolle}"))
    return funde


def _aus_odf(pfad: Path) -> list[Fund]:
    zaehler: Counter = Counter()
    with zipfile.ZipFile(pfad) as z:
        for n in ("styles.xml", "content.xml"):
            if n in z.namelist():
                xml = z.read(n).decode("utf-8", errors="replace")
                for v in re.findall(r'(?:fo:color|fo:background-color|draw:fill-color|'
                                    r'svg:stroke-color|draw:stroke-color)="(#[0-9A-Fa-f]{6})"', xml):
                    zaehler[v.lower()] += 1
    return [Fund(h, n, "verwendet") for h, n in zaehler.items()]


def _aus_css(text: str, herkunft: str, gewicht: float = 1.0) -> list[Fund]:
    zaehler: Counter = Counter()
    for m in _CSS_FARBE.finditer(text):
        if m.group(1) is not None:
            hexwert = _hex(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        else:
            hexwert = normiere_hex(m.group(0))
        if hexwert:
            zaehler[hexwert] += gewicht
    # Markenfarben in CSS-Variablen (--primary, --brand-color …) zählen fünffach
    for m in _CSS_VARIABLE.finditer(text):
        for f in _CSS_FARBE.finditer(m.group(1)):
            hexwert = (_hex(int(f.group(1)), int(f.group(2)), int(f.group(3)))
                       if f.group(1) is not None else normiere_hex(f.group(0)))
            if hexwert:
                zaehler[hexwert] += 4 * gewicht
    return [Fund(h, n, herkunft) for h, n in zaehler.items()]


def _lade_web(url: str) -> str:
    anfrage = urllib.request.Request(url, headers={"User-Agent": "eduwerkzeuge-edumap/1.0"})
    with urllib.request.urlopen(anfrage, timeout=15) as antwort:  # noqa: S310 (nur http/https)
        return antwort.read(3_000_000).decode("utf-8", errors="replace")


def _aus_html(html: str, basis_dir: Path | None, basis_url: str | None) -> list[Fund]:
    funde: list[Fund] = []
    for m in re.finditer(r'<meta[^>]+name=["\']theme-color["\'][^>]*content=["\']([^"\']+)', html, re.I):
        hexwert = normiere_hex(m.group(1))
        if hexwert:
            funde.append(Fund(hexwert, 20, "theme-color der Seite"))
    css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", html, re.S | re.I))
    css += "\n" + "\n".join(re.findall(r'style="([^"]*)"', html, re.I))
    funde += _aus_css(css, "Seite")
    links = re.findall(r'<link[^>]+rel=["\']?stylesheet["\']?[^>]*>', html, re.I)
    for tag in links[:6]:
        href = re.search(r'href=["\']([^"\']+)', tag)
        if not href:
            continue
        ziel = href.group(1)
        try:
            if basis_url:
                url = urllib.parse.urljoin(basis_url, ziel)
                if url.startswith(("http://", "https://")):
                    funde += _aus_css(_lade_web(url), Path(urllib.parse.urlparse(url).path).name or url)
            elif basis_dir is not None and not re.match(r"^[a-z]+:", ziel):
                datei = basis_dir / ziel.split("?")[0]
                if datei.is_file():
                    funde += _aus_css(datei.read_text(encoding="utf-8", errors="replace"), datei.name)
        except OSError:
            continue  # Stylesheet nicht erreichbar – mit den übrigen Farben weiter
    return funde


def _aus_web(url: str) -> list[Fund]:
    text = _lade_web(url)
    if url.lower().split("?")[0].endswith(".css"):
        return _aus_css(text, url)
    return _aus_html(text, None, url)


def _aus_bild(pfad: Path, farben: int = 10) -> list[Fund]:
    try:
        from PIL import Image
    except ImportError as e:
        raise RuntimeError("Farben aus Bildern und PDF brauchen Pillow (pip install pillow)") from e
    with Image.open(pfad) as bild:
        bild = bild.convert("RGB")
        bild.thumbnail((160, 160))
        quant = bild.quantize(colors=farben)
        palette = quant.getpalette() or []
        return [Fund(_hex(*palette[i * 3:i * 3 + 3]), n, "Bildfläche")
                for n, i in quant.getcolors() or []]


def _aus_pdf(pfad: Path, seiten: int = 3) -> list[Fund]:
    if not shutil.which("pdftoppm"):
        raise RuntimeError("Farben aus PDF brauchen pdftoppm (poppler-utils)")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-r", "30", "-f", "1", "-l", str(seiten), "-png", str(pfad),
                        str(Path(tmp) / "s")], check=True, capture_output=True)
        funde: list[Fund] = []
        for bild in sorted(Path(tmp).glob("*.png")):
            funde += _aus_bild(bild)
        return funde


# ---------------------------------------------------------------------------
# Vorschlag
# ---------------------------------------------------------------------------

def _buendeln(funde: list[Fund], schwelle: float = 28) -> list[Fund]:
    """Fasst fast gleiche Farben zusammen; die häufigere gibt den Ton an."""
    summe: dict[str, Fund] = {}
    for f in funde:
        hexwert = normiere_hex(f.hex)
        if hexwert is None:
            continue
        summe.setdefault(hexwert, Fund(hexwert, 0, f.herkunft)).gewicht += f.gewicht
        if f.herkunft.startswith("Design") and not summe[hexwert].herkunft.startswith("Design"):
            summe[hexwert].herkunft = f.herkunft
    gruppen: list[Fund] = []
    for f in sorted(summe.values(), key=lambda x: -x.gewicht):
        nah = next((g for g in gruppen if _abstand(g.hex, f.hex) < schwelle), None)
        if nah:
            nah.gewicht += f.gewicht
        else:
            gruppen.append(Fund(f.hex, f.gewicht, f.herkunft))
    return sorted(gruppen, key=lambda x: -x.gewicht)


def _varianten(basis: list[str], anzahl: int) -> list[str]:
    """Ergänzt hellere/dunklere Töne der vorhandenen Farben, alle lesbar."""
    erg = list(basis)
    schritte = (0.12, -0.12, 0.22, -0.2)
    for d in schritte:
        for b in basis:
            if len(erg) >= anzahl:
                return erg
            h, l, s = _hls(b)
            neu = lesbar(_aus_hls(h, l + d, s))
            if all(_abstand(neu, e) >= 40 for e in erg):
                erg.append(neu)
    return erg


def theme_vorschlag(funde: list[Fund], anzahl: int = 6, mindestens: int = 3) -> dict:
    """Macht aus gefundenen Farben ein Theme: Pfadfarben lesbar, Hintergrund hell.

    Höchstens `anzahl` Pfadfarben; hat das Material weniger als `mindestens`
    verschiedene Farben, ergänzen hellere/dunklere Töne der gefundenen.

    Rückgabe: {"hintergrund", "pfade", "karten", "farben", "notizen"} – notizen
    erklären je Farbe Herkunft und Anpassung (für Kommentare im YAML).
    """
    gruppen = _buendeln(funde)
    # Blasse Flächenfarben (Tabellenschattierung …) taugen als Hintergrund, nicht als
    # Pfadfarbe – außer sie sind Design-Farben des Materials.
    bunt = [g for g in gruppen if ist_bunt(g.hex)
            and (_hls(g.hex)[1] < 0.82 or g.herkunft.startswith("Design"))]
    if not bunt:
        # Graue Vorlage: die dunkelsten Töne als Pfadfarben
        bunt = sorted((g for g in gruppen if 0.05 < _hls(g.hex)[1] < 0.6),
                      key=lambda g: leuchtdichte(g.hex))
    if not bunt:
        raise ValueError("Im Ausgangsmaterial wurden keine verwendbaren Farben gefunden")

    farben: dict[str, str] = {}
    notizen: dict[str, str] = {}
    gewaehlt: list[str] = []
    for g in bunt:
        neu = lesbar(g.hex)
        if any(_abstand(neu, e) < 40 or _gleicher_ton(neu, e) for e in gewaehlt):
            continue
        name = f"farbe{len(gewaehlt) + 1}"
        gewaehlt.append(neu)
        farben[name] = neu
        notiz = g.herkunft or "gefunden"
        if neu != g.hex:
            notiz += f", abgedunkelt von {g.hex}"
        notizen[name] = notiz
        if len(gewaehlt) >= anzahl:
            break
    if len(gewaehlt) < mindestens:
        for neu in _varianten(gewaehlt, min(anzahl, mindestens))[len(gewaehlt):]:
            name = f"farbe{len(farben) + 1}"
            farben[name] = neu
            notizen[name] = "Variante der Hauptfarben"

    # Hintergrund: heller, getönter Ton aus dem Material, sonst Hauptfarbe stark aufgehellt
    hell = [g for g in gruppen if _hls(g.hex)[1] >= 0.9 and _hls(g.hex)[2] >= 0.1]
    if hell and hell[0].gewicht >= 2:
        hintergrund, notizen["hintergrund"] = hell[0].hex, f"{hell[0].herkunft or 'gefunden'}"
    else:
        hintergrund = mischen(gewaehlt[0], "#ffffff", 0.9)
        notizen["hintergrund"] = "farbe1, stark aufgehellt"
    return {"hintergrund": hintergrund, "pfade": list(farben), "karten": "pfad",
            "farben": farben, "notizen": notizen}


def theme_yaml(vorschlag: dict, quelle: str, mit_schluessel: bool = True) -> str:
    """Schreibt den Vorschlag als YAML-Block mit Kommentaren."""
    notizen = vorschlag.get("notizen", {})
    ein = "  " if mit_schluessel else ""
    zeilen = [f"# Farbgebung aus {quelle} – erzeugt mit edu-edumap --farben-aus ({date.today():%Y-%m-%d}).",
              "# Pfade: Standardfarben der Quelle werden der Reihe nach ersetzt;",
              "# alle Pfadfarben haben mindestens 3:1 Kontrast zu weißer Schrift."]
    if mit_schluessel:
        zeilen.append("# Verwenden: diesen Block ins Frontmatter der Quelle kopieren "
                      "(ersetzt die Zeile theme:).")
    else:
        zeilen.append("# Verwenden: im Frontmatter der Quelle theme: <diese Datei> "
                      "oder edu-edumap QUELLE --theme <diese Datei>.")
    if mit_schluessel:
        zeilen.append("theme:")
    zeilen.append(f'{ein}hintergrund: "{vorschlag["hintergrund"]}"'
                  + (f"   # {notizen['hintergrund']}" if notizen.get("hintergrund") else ""))
    zeilen.append(f"{ein}pfade: [{', '.join(vorschlag['pfade'])}]")
    if vorschlag.get("karten"):
        zeilen.append(f"{ein}karten: {vorschlag['karten']}             # Karten ohne Farbe in Pfadfarbe")
    zeilen.append(f"{ein}farben:")
    for name, wert in vorschlag["farben"].items():
        k = f"   # {notizen[name]}, Kontrast " + f"{kontrast(wert):.1f}".replace(".", ",") + ":1" \
            if notizen.get(name) else ""
        zeilen.append(f'{ein}  {name}: "{wert}"{k}')
    return "\n".join(zeilen) + "\n"
