#!/usr/bin/env python3
"""edumap_pruefen – prüft eine Edumap-Quelle (Markdown oder YAML) vor dem Erzeugen.

Findet, was edu-edumap still übergeht oder edumaps falsch darstellt: unbekannte Farben,
Themes und Formate, fehlende Zeitangaben im Zeitstrahl, Buchung ohne Startzeit, offene
Code-Blöcke, unvollständige Quiz/Abstimmungen, Markdown-Syntax, die edumaps nicht kennt
(Tabellen mit |, Links [..](..), Bilder, Überschriften in Karten), Platzhalter aus der
Vorlage, Kontaktdaten, eigene Themes (Mapping oder Theme-Datei) und Farben mit zu wenig
Kontrast zu weißer Titelschrift; dazu die Leitlinien des Skills: höchstens sechs Karten je Pfad und
vollständige Lernposten (Auftrag mit Ergebnis, Sozialform/Zeit und Erfolgskriterien, Material,
Hilfen, Selbstcheck). Mit --json wird zusätzlich die erzeugte Import-Datei gegengeprüft.

    python3 scripts/edumap_pruefen.py 92_lernlandkarte_gurtfoerderer.md
    python3 scripts/edumap_pruefen.py 92_lernlandkarte_gurtfoerderer.md --json 92_lernlandkarte_gurtfoerderer.json

Exitcode 1 bei Fehlern (❌). Nur Python-Standardbibliothek; PyYAML wird für das
Frontmatter gebraucht (ohne PyYAML ignoriert auch edu-edumap das Frontmatter).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None  # type: ignore

# Spiegel der Daten aus eduwerkzeuge.edumap (bewusst ohne Import: das Skript soll auch
# ohne mitgelieferte Kopie laufen). Ein Test der Bibliothek hält beide gleich.
PALETTE = {
    "anthrazit": "#2d333d", "schiefergrau": "#3d4a5c", "nachtblau": "#1e2d45", "dunkelgrau": "#374151",
    "warmgrau": "#44403c", "olivgrau": "#383d33", "mitternacht": "#0f172a", "stahlblau": "#1e3a5f",
    "hellblau": "#c4dcff", "eisblau": "#e8f4ff", "mintweiss": "#ecfdf5", "hellgrau": "#f1f5f9",
    "creme": "#fefce8", "lavendel": "#f5f3ff", "pastellblau": "#dbeafe", "pastellgruen": "#dcfce7",
    "pastellrose": "#fce7f3", "blau": "#4267F5", "ozeanblau": "#0087CD", "tuerkis": "#0d9488",
    "mintgruen": "#059669", "gruen": "#16a34a", "waldgruen": "#4d7c0f", "bernstein": "#d97706",
    "orange": "#ea580c", "rot": "#dc2626", "koralle": "#e11d48", "lila": "#7c3aed", "violett": "#6d28d9",
    "indigo": "#4338ca", "pink": "#db2777", "grau": "#6b7280", "silber": "#94a3b8",
}
LERNPOSTEN_RE = re.compile(r"^\s*(?:Lernposten|Station)\b", re.IGNORECASE)
LERNPOSTEN_TEILE = (("Auftrag", r"auftrag"), ("Material", r"material|infoblatt|satzbaustein|vorlage"),
                    ("Hilfen", r"hilfe"), ("Selbstcheck", r"selbstcheck|selbstkontrolle|test"))
THEMES = {"standard", "nacht", "schiefer", "anthrazit", "wald", "warm", "abend", "morgen",
          "tageslicht", "kreide"}
DUNKLE_THEMES = {"nacht", "schiefer", "anthrazit", "wald", "warm", "abend"}
THEME_SCHLUESSEL = {"basis", "hintergrund", "mapbg", "pfade", "karten", "farben"}
MIN_KONTRAST = 3.0  # weiße Titelschrift auf Pfad- und Kartenfarbe
STANDARD_PFADFARBE = "#4267F5"
FORMATE = {"karte", "pinnwand", "zeitstrahl", "kalender", "0", "1", "2", "3"}
PFAD_ATTRIBUTE = {"color", "box_color", "color_inherit", "flags", "showdate", "annotation", "extras"}
KARTEN_ATTRIBUTE_MD = {"color", "flags", "showdate", "booktime", "booklimit", "book", "subject",
                       "extras", "file_url", "file_label"}
KARTEN_SCHLUESSEL_YAML = {"title", "content", "subject", "booktime", "booklimit", "book", "color",
                          "flags", "position", "showdate", "extras", "files"}
PFAD_SCHLUESSEL_YAML = {"title", "boxes"} | PFAD_ATTRIBUTE
FLAG_NAVIGATION = 1048576
FLAG_GESPERRT = 640

ATTR_RE = re.compile(r"\[(\w+)=([^\]]*)\]")
DATUM_RE = re.compile(r"^\d{4}-\d{2}-\d{2}( \d{2}:\d{2}(:\d{2})?)?$")
HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")
MAIL_RE = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
MAIL_ERLAUBT = re.compile(r"@(example\.(com|org|de)|beispiel\.de|schule\.example)$", re.I)
URL_RE = re.compile(r"https?://[^\s}\)]+")
PLATZHALTER_RE = re.compile(r"(?<!!)\[(?![ xX]\])[^\]\n=]{2,}\](?![{(])")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


@dataclass
class Karte:
    titel: str
    attrs: dict
    inhalt: list[str]
    zeile: int | None


@dataclass
class Pfad:
    titel: str
    attrs: dict
    zeile: int | None
    karten: list[Karte] = field(default_factory=list)


@dataclass
class Befund:
    stufe: str  # ❌ ⚠ ℹ
    ort: str
    text: str


# ─────────────────────────────── Einlesen ───────────────────────────────

def lies_markdown(text: str, befunde: list[Befund]) -> tuple[dict, list[Pfad]]:
    zeilen = text.split("\n")
    kopf: dict = {}
    start = 0
    if zeilen and zeilen[0].strip() == "---":
        ende = next((i for i, z in enumerate(zeilen[1:], 1) if z.strip() in ("---", "...")), None)
        if ende is None:
            befunde.append(Befund("❌", "Zeile 1", "Frontmatter wird nicht mit --- geschlossen"))
        else:
            roh = "\n".join(zeilen[1:ende])
            if yaml is None:
                befunde.append(Befund("❌", "Frontmatter", "PyYAML fehlt – edu-edumap würde Titel, "
                                      "Theme und Format ignorieren (pip install pyyaml)"))
            else:
                try:
                    kopf = yaml.safe_load(roh) or {}
                except yaml.YAMLError as e:
                    befunde.append(Befund("❌", "Frontmatter", f"kein gültiges YAML: {e}"))
            start = ende + 1
    pfade: list[Pfad] = []
    karte: Karte | None = None
    for nr, zeile in enumerate(zeilen[start:], start + 1):
        if zeile.startswith("## "):
            titel, attrs = _attrs(zeile[3:])
            pfade.append(Pfad(titel, attrs, nr))
            karte = None
        elif zeile.startswith("### "):
            titel, attrs = _attrs(zeile[4:])
            if not pfade:
                befunde.append(Befund("⚠", f"Zeile {nr}", "Karte vor dem ersten Pfad (##) – "
                                      "edu-edumap legt dafür einen Pfad ohne Titel an"))
                pfade.append(Pfad("", {}, None))
            karte = Karte(titel, attrs, [], nr)
            pfade[-1].karten.append(karte)
        elif zeile.startswith("# ") and karte is None:
            kopf.setdefault("title", _attrs(zeile[2:])[0])
        elif karte is not None:
            karte.inhalt.append(zeile)
        elif zeile.strip() and not zeile.lstrip().startswith("<!--"):
            befunde.append(Befund("⚠", f"Zeile {nr}", "Text außerhalb einer Karte (vor dem ersten ### "
                                  "eines Pfads) – edu-edumap übernimmt ihn nicht"))
    return kopf, pfade


def _attrs(roh: str) -> tuple[str, dict]:
    attrs = {m.group(1): m.group(2) for m in ATTR_RE.finditer(roh)}
    return ATTR_RE.sub("", roh).strip(), attrs


def lies_yaml(text: str, befunde: list[Befund]) -> tuple[dict, list[Pfad]]:
    if yaml is None:
        befunde.append(Befund("❌", "Datei", "PyYAML fehlt (pip install pyyaml)"))
        return {}, []
    try:
        daten = yaml.safe_load(text) or {}
    except yaml.YAMLError as e:
        befunde.append(Befund("❌", "Datei", f"kein gültiges YAML: {e}"))
        return {}, []
    kopf = dict(daten.get("mapdata", daten))
    pfade: list[Pfad] = []
    for i, p in enumerate(daten.get("paths") or [], 1):
        if not isinstance(p, dict):
            befunde.append(Befund("❌", f"Pfad {i}", "ist kein Mapping (title, color, boxes …)"))
            continue
        for k in sorted(set(p) - PFAD_SCHLUESSEL_YAML):
            befunde.append(Befund("❌", f"Pfad {i}", f"unbekannter Schlüssel '{k}' (wird ignoriert)"))
        pfad = Pfad(str(p.get("title") or ""), {k: v for k, v in p.items() if k in PFAD_ATTRIBUTE}, None)
        for j, b in enumerate(p.get("boxes") or [], 1):
            if not isinstance(b, dict):
                befunde.append(Befund("❌", f"Pfad {i}, Karte {j}", "ist kein Mapping"))
                continue
            for k in sorted(set(b) - KARTEN_SCHLUESSEL_YAML):
                befunde.append(Befund("❌", f"Pfad {i}, Karte {j}", f"unbekannter Schlüssel '{k}'"))
            attrs = {k: v for k, v in b.items() if k not in ("title", "content", "files")}
            if any(not (f or {}).get("url") for f in (b.get("files") or [])):
                befunde.append(Befund("❌", f"Pfad {i}, Karte {j}", "files-Eintrag ohne url"))
            if b.get("files"):
                attrs["file_url"] = "files"
            inhalt = str(b.get("content") or "").split("\n")
            pfad.karten.append(Karte(str(b.get("title") or ""), attrs, inhalt, None))
        pfade.append(pfad)
    return kopf, pfade


# ─────────────────────────────── Prüfen ───────────────────────────────

def _farbe_ok(wert, eigene: dict | None = None) -> bool:
    w = str(wert).strip()
    return bool(HEX_RE.match(w)) or w.lower() in PALETTE or w.lower() in (eigene or {})


def _hex(wert, eigene: dict | None = None) -> str | None:
    w = str(wert).strip()
    if HEX_RE.match(w):
        return w
    return (eigene or {}).get(w.lower()) or PALETTE.get(w.lower())


def kontrast(a: str, b: str = "#ffffff") -> float:
    def lum(h: str) -> float:
        k = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        k = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in k]
        return 0.2126 * k[0] + 0.7152 * k[1] + 0.0722 * k[2]
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def _melde_kontrast(wert, eigene: dict, ort: str, was: str, befunde: list[Befund]) -> None:
    h = _hex(wert, eigene)
    if h and kontrast(h) < MIN_KONTRAST:
        k = f"{kontrast(h):.1f}".replace(".", ",")
        befunde.append(Befund("⚠", ort, f"{was} {wert} – weiße Titelschrift kaum lesbar (Kontrast "
                              f"{k}:1, mindestens 3:1); dunkleren Ton wählen"))


def pruefe_theme(kopf: dict, basis: Path | None, befunde: list[Befund]) -> tuple[dict, dict | None]:
    """Prüft theme: (Name, Datei oder Mapping). Rückgabe: (eigene Farbnamen, Theme-Mapping)."""
    roh = kopf.get("theme")
    if roh in (None, ""):
        return {}, None
    if isinstance(roh, str) and roh.lower().endswith((".yaml", ".yml")):
        datei = Path(roh) if Path(roh).is_absolute() or basis is None else basis / roh
        if not datei.is_file():
            befunde.append(Befund("❌", "Frontmatter", f"Theme-Datei {roh} nicht gefunden (relativ zur Quelle)"))
            return {}, None
        if yaml is None:
            return {}, None
        try:
            roh = yaml.safe_load(datei.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            befunde.append(Befund("❌", "Theme-Datei", f"kein gültiges YAML: {e}"))
            return {}, None
        if isinstance(roh, dict) and isinstance(roh.get("theme"), dict):
            roh = roh["theme"]
    if isinstance(roh, str):
        theme = roh.lower()
        if theme not in THEMES:
            befunde.append(Befund("❌", "Frontmatter", f"unbekanntes theme '{theme}' – erlaubt: "
                                  f"{', '.join(sorted(THEMES))}, eine Theme-Datei (.yaml) oder ein Mapping"))
        if theme in DUNKLE_THEMES:
            befunde.append(Befund("ℹ", "Frontmatter", f"dunkles theme '{theme}' – für Beamer und Druck "
                                  "sind tageslicht, morgen oder kreide besser lesbar"))
        return {}, None
    if not isinstance(roh, dict):
        befunde.append(Befund("❌", "Frontmatter", "theme ist weder Name noch Datei noch Mapping"))
        return {}, None

    ort = "Theme"
    for k in sorted(set(roh) - THEME_SCHLUESSEL):
        befunde.append(Befund("❌", ort, f"unbekannter Schlüssel '{k}' – erlaubt: {', '.join(sorted(THEME_SCHLUESSEL))}"))
    if roh.get("basis") and str(roh["basis"]).lower() not in THEMES:
        befunde.append(Befund("❌", ort, f"basis '{roh['basis']}' ist kein eingebautes Theme"))
    eigene: dict = {}
    for name, wert in (roh.get("farben") or {}).items():
        h = _hex(wert)
        if not h:
            befunde.append(Befund("❌", ort, f"farben.{name}: '{wert}' ist weder #rrggbb noch Farbname"))
        else:
            eigene[str(name).lower()] = h
    pfade = roh.get("pfade") or []
    pfade = [pfade] if isinstance(pfade, str) else pfade
    for f in pfade:
        if not _farbe_ok(f, eigene):
            befunde.append(Befund("❌", ort, f"pfade: '{f}' ist keine bekannte Farbe"))
        else:
            _melde_kontrast(f, eigene, ort, "Pfadfarbe", befunde)
    karten = roh.get("karten")
    if karten not in (None, "", "pfad", "keine") and not _farbe_ok(karten, eigene):
        befunde.append(Befund("❌", ort, f"karten: '{karten}' – erlaubt: pfad, keine oder eine Farbe"))
    bg = roh.get("hintergrund") or roh.get("mapbg")
    if bg and not _farbe_ok(bg, eigene):
        befunde.append(Befund("❌", ort, f"hintergrund '{bg}' ist keine bekannte Farbe"))
    elif bg and kontrast(_hex(bg, eigene), "#000000") < 10:
        befunde.append(Befund("ℹ", ort, f"dunkler oder kräftiger hintergrund {bg} – für Beamer und Druck "
                              "ist ein heller Ton besser lesbar"))
    return eigene, {**roh, "pfade": pfade}


def _int_ok(wert) -> bool:
    return str(wert).strip().isdigit()


def pruefe(kopf: dict, pfade: list[Pfad], befunde: list[Befund], basis: Path | None = None) -> dict:
    # Karte als Ganzes
    if not str(kopf.get("title") or "").strip():
        befunde.append(Befund("❌", "Karte", "kein Titel (Frontmatter title: oder Zeile '# Titel')"))
    _melde_platzhalter(_platzhalter(str(kopf.get("title") or "")), "Titel", befunde)
    eigene, theme = pruefe_theme(kopf, basis, befunde)
    fmt = str(kopf.get("format") or kopf.get("mapformat") or "karte").lower()
    if fmt not in FORMATE:
        befunde.append(Befund("❌", "Frontmatter", f"unbekanntes format '{fmt}' – erlaubt: karte, pinnwand, zeitstrahl, kalender"))
    if kopf.get("mapbg") and not _farbe_ok(kopf["mapbg"], eigene):
        befunde.append(Befund("❌", "Frontmatter", f"mapbg '{kopf['mapbg']}' ist weder Farbname noch #rrggbb"))
    if kopf.get("password"):
        befunde.append(Befund("⚠", "Frontmatter", "password steht im Klartext in Quelle und Import-Datei – "
                              "besser nach dem Import in edumaps setzen"))
    zeitbezug = fmt in ("zeitstrahl", "kalender", "2", "3")

    stat = {"pfade": len(pfade), "karten": 0, "ausgeklappt": 0, "quiz": 0, "abstimmung": 0, "links": set()}
    if not pfade:
        befunde.append(Befund("❌", "Karte", "keine Pfade (## Pfad-Titel) gefunden"))
    for i, pfad in enumerate(pfade, 1):
        ort = f"Pfad {i} „{pfad.titel[:40]}“" + (f" (Zeile {pfad.zeile})" if pfad.zeile else "")
        for k in sorted(set(pfad.attrs) - PFAD_ATTRIBUTE):
            befunde.append(Befund("❌", ort, f"unbekanntes Attribut [{k}=…] (wird ignoriert)"))
        for k in ("color", "box_color"):
            if pfad.attrs.get(k) and not _farbe_ok(pfad.attrs[k], eigene):
                befunde.append(Befund("❌", ort, f"{k}={pfad.attrs[k]} ist keine bekannte Farbe"))
            elif pfad.attrs.get(k) and not (theme and theme["pfade"] and str(pfad.attrs[k]).lower() in PALETTE):
                _melde_kontrast(pfad.attrs[k], eigene, ort, k, befunde)
        if "flags" in pfad.attrs and not _int_ok(pfad.attrs["flags"]):
            befunde.append(Befund("❌", ort, f"flags={pfad.attrs['flags']} ist keine Zahl"))
        datum = pfad.attrs.get("showdate")
        if datum and not DATUM_RE.match(str(datum)):
            befunde.append(Befund("❌", ort, f"showdate '{datum}' – Format JJJJ-MM-TT hh:mm:ss"))
        if zeitbezug and not datum:
            befunde.append(Befund("⚠", ort, f"format {fmt} ohne showdate – der Pfad lässt sich nicht einordnen"))
        if str(pfad.attrs.get("flags", "0")) == str(FLAG_GESPERRT) and not datum:
            befunde.append(Befund("❌", ort, "gesperrter Pfad (flags=640) ohne showdate öffnet sich nie"))
        if not pfad.titel:
            befunde.append(Befund("⚠", ort, "Pfad ohne Titel"))
        if not pfad.karten:
            befunde.append(Befund("⚠", ort, "Pfad ohne Karten"))
        if len(pfad.karten) > 6:
            befunde.append(Befund("⚠", ort, f"{len(pfad.karten)} Karten – Leitlinie 3–6 je Pfad; gestufte Hilfen "
                                  "als mehrere ??-Spoiler in einer Karte bündeln oder den Pfad teilen"))
        if LERNPOSTEN_RE.match(pfad.titel):
            titel = " ".join(k.titel.lower() for k in pfad.karten)
            fehlt = [teil for teil, muster in LERNPOSTEN_TEILE if not re.search(muster, titel)]
            if fehlt:
                befunde.append(Befund("⚠", ort, "Lernposten ohne Karte für: " + ", ".join(fehlt)
                                      + " (Leitlinie 2: Auftrag · Material · gestufte Hilfen · Selbstcheck)"))
            auftrag = next((k for k in pfad.karten if "auftrag" in k.titel.lower()), None)
            if auftrag:
                text = " ".join(auftrag.inhalt).lower()
                luecken = [t for t, m in (("Ergebnis", r"ergebnis"), ("Sozialform/Zeit", r"\bmin\b|minuten|sozialform"),
                                          ("Erfolgskriterien", r"erfolgskriter|fertig, wenn"))
                           if not re.search(m, text)]
                if luecken:
                    befunde.append(Befund("⚠", ort, "Auftrag ohne " + ", ".join(luecken)))
        _melde_platzhalter(_platzhalter(pfad.titel), ort, befunde)
        for j, karte in enumerate(pfad.karten, 1):
            stat["karten"] += 1
            _pruefe_karte(karte, f"{ort} › Karte {j}" + (f" (Zeile {karte.zeile})" if karte.zeile else ""),
                          befunde, stat, eigene)
    if theme and theme["pfade"]:
        standard = {str(p.attrs.get("color") or STANDARD_PFADFARBE).lower() for p in pfade
                    if not p.attrs.get("color") or str(p.attrs["color"]).lower() in PALETTE}
        if len(standard) > len(theme["pfade"]):
            befunde.append(Befund("ℹ", "Theme", f"{len(standard)} Standardfarben in den Pfaden, aber nur "
                                  f"{len(theme['pfade'])} Farben unter pfade: – Farben wiederholen sich"))
    return stat


def _pruefe_karte(karte: Karte, ort: str, befunde: list[Befund], stat: dict,
                  eigene: dict | None = None) -> None:
    a = karte.attrs
    if karte.zeile is not None:  # Markdown: nur Inline-Attribute
        for k in sorted(set(a) - KARTEN_ATTRIBUTE_MD):
            befunde.append(Befund("❌", ort, f"unbekanntes Attribut [{k}=…] (wird ignoriert)"))
    if a.get("color") and not _farbe_ok(a["color"], eigene):
        befunde.append(Befund("❌", ort, f"color={a['color']} ist keine bekannte Farbe"))
    flags = a.get("flags")
    if flags is not None and not _int_ok(flags):
        befunde.append(Befund("❌", ort, f"flags={flags} ist keine Zahl"))
    flags_int = int(str(flags)) if flags is not None and _int_ok(flags) else 4
    if flags_int in (0, 16420):
        stat["ausgeklappt"] += 1
    for k in ("showdate", "booktime"):
        if a.get(k) and not DATUM_RE.match(str(a[k])):
            befunde.append(Befund("❌", ort, f"{k} '{a[k]}' – Format JJJJ-MM-TT hh:mm:ss"))
    buch = str(a.get("book") or "").lower()
    if buch and buch not in ("open", "timed"):
        befunde.append(Befund("❌", ort, f"book={buch} – erlaubt: open, timed"))
    if buch == "timed" and not a.get("booktime"):
        befunde.append(Befund("❌", ort, "book=timed ohne booktime"))
    if a.get("booklimit") not in (None, "") and not _int_ok(a["booklimit"]):
        befunde.append(Befund("❌", ort, f"booklimit={a['booklimit']} ist keine Zahl"))
    if not karte.titel or karte.titel == "-":
        if flags_int != FLAG_NAVIGATION:
            befunde.append(Befund("⚠", ort, "Karte ohne Titel (nur Navigationskarten mit flags=1048576 sind titellos)"))
    platzhalter = _platzhalter(karte.titel)

    text = "\n".join(karte.inhalt)
    if not text.strip() and not a.get("file_url"):
        befunde.append(Befund("⚠", ort, "Karte ohne Inhalt"))
    if "\r" in text:
        befunde.append(Befund("❌", ort, "Wagenrücklauf (\\r) im Inhalt – Datei mit LF-Zeilenenden speichern"))
    if text.count("`") % 2:
        befunde.append(Befund("❌", ort, "ungerade Zahl von Backticks – Code-Block nicht geschlossen "
                              "(im Code selbst keine Backticks verwenden)"))
    _pruefe_bloecke(text, "quiz", ort, befunde, stat)
    _pruefe_bloecke(text, "poll", ort, befunde, stat)
    kopf_spalten = 0
    tabelle_alt = False
    in_code = False
    vorige = ""
    for zeile in karte.inhalt:
        davor, vorige = vorige, zeile
        if zeile.count("`") % 2:
            in_code = not in_code
        s = zeile.strip()
        if in_code or not s:
            continue
        if re.match(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$", s):
            befunde.append(Befund("⚠", ort, "Markdown-Tabelle (|---|) – edumaps braucht ||| Kopf | Kopf und || Zelle | Zelle"))
        elif s.startswith("|||"):
            if davor.strip():
                befunde.append(Befund("ℹ", ort, "Tabelle direkt unter Text – edumaps braucht eine Leerzeile "
                                      "davor; edu-edumap ergänzt sie (von Hand in edumaps: Leerzeile einfügen)"))
            tabelle_alt = "||" in s[3:]
            if tabelle_alt:
                befunde.append(Befund("⚠", ort, "Tabelle mit || als Zelltrenner (alte edumaps-Syntax) – "
                                      "neu: ||| Kopf 1 | Kopf 2 und || Zelle | Zelle; edu-edumap wandelt beim Erzeugen um"))
            kopf_spalten = len(_tabellenzellen(s[3:], tabelle_alt))
        elif s.startswith("||") and kopf_spalten:
            zellen = _tabellenzellen(s[2:], tabelle_alt)
            while tabelle_alt and zellen and zellen[-1] == "":
                zellen.pop()
            if len(zellen) > kopf_spalten:
                befunde.append(Befund("⚠", ort, f"Tabellenzeile mit {len(zellen)} Zellen, Kopf hat {kopf_spalten}"))
        elif not s.startswith("||"):
            kopf_spalten = 0
        if re.match(r"^#{2,6}\s", s):
            befunde.append(Befund("⚠", ort, f"Markdown-Überschrift in der Karte („{s[:30]}“) – **fett** verwenden"))
        if re.search(r"!\[[^\]]*\]\([^)]+\)", s):
            befunde.append(Befund("⚠", ort, "Markdown-Bild ![..](..) – in edumaps Bild-URL in eigene Zeile, Beschriftung darunter"))
        elif re.search(r"\[[^\]]+\]\(https?://", s):
            befunde.append(Befund("⚠", ort, "Markdown-Link [..](..) – in edumaps {Linktext}{https://…}"))
        if re.match(r"^\d+\.\s", s):
            befunde.append(Befund("ℹ", ort, f"„{s[:20]}…“ – nummerierte Liste in edumaps mit -- schreiben"))
        platzhalter += _platzhalter(INLINE_CODE_RE.sub("", s))
        for m in MAIL_RE.finditer(s):
            if not MAIL_ERLAUBT.search(m.group(0)):
                befunde.append(Befund("⚠", ort, "E-Mail-Adresse im Inhalt – keine Kontaktdaten von Personen in Karten"))
        m = re.search(r"&&count:\s*([^&]*)&&", s)
        if m and not m.group(1).strip().isdigit():
            befunde.append(Befund("❌", ort, f"Countdown '&&count: {m.group(1)}&&' – Sekunden als Zahl"))
        stat["links"].update(u.rstrip(".,;") for u in URL_RE.findall(s))
    _melde_platzhalter(platzhalter, ort, befunde)


def _tabellenzellen(text: str, alt: bool) -> list[str]:
    """Zellen einer Tabellenzeile ohne Praefix; alt = Trenner ||, sonst |."""
    return [z.strip() for z in text.split("||" if alt else "|")]


def _pruefe_bloecke(text: str, art: str, ort: str, befunde: list[Befund], stat: dict) -> None:
    auf, zu = text.count(f"<{art}>"), text.count(f"</{art}>")
    if auf != zu:
        befunde.append(Befund("❌", ort, f"<{art}> und </{art}> nicht paarig ({auf}/{zu})"))
        return
    for m in re.finditer(rf"<{art}>(.*?)</{art}>", text, re.DOTALL):
        optionen = [z.strip() for z in m.group(1).split("\n") if z.strip()]
        name = "Quiz" if art == "quiz" else "Abstimmung"
        stat["quiz" if art == "quiz" else "abstimmung"] += 1
        if len(optionen) < 2:
            befunde.append(Befund("❌", ort, f"{name} mit weniger als zwei Optionen"))
        if art == "quiz":
            richtig = [o for o in optionen if o.startswith("#")]
            if not richtig:
                befunde.append(Befund("❌", ort, "Quiz ohne richtige Antwort (Zeile mit # beginnen)"))
            if len(richtig) == len(optionen):
                befunde.append(Befund("❌", ort, "Quiz: alle Antworten als richtig markiert"))


def _platzhalter(text: str) -> list[str]:
    return [m.group(0) for m in PLATZHALTER_RE.finditer(ATTR_RE.sub("", text))]


def _melde_platzhalter(funde: list[str], ort: str, befunde: list[Befund]) -> None:
    if funde:
        liste = ", ".join(dict.fromkeys(f if len(f) <= 32 else f[:30] + "…]" for f in funde))
        befunde.append(Befund("⚠", ort, f"Platzhalter aus der Vorlage? {liste}"))


def pruefe_json(pfad: Path, stat: dict, befunde: list[Befund]) -> None:
    try:
        daten = json.loads(pfad.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        befunde.append(Befund("❌", pfad.name, f"nicht lesbar: {e}"))
        return
    if not isinstance(daten, dict) or "mapdata" not in daten or "paths" not in daten:
        befunde.append(Befund("❌", pfad.name, "kein Edumap-Import (mapdata/paths fehlen)"))
        return
    pfade = daten["paths"]
    karten = sum(len(p.get("boxes") or []) for p in pfade)
    if len(pfade) != stat["pfade"] or karten != stat["karten"]:
        befunde.append(Befund("❌", pfad.name, f"{len(pfade)} Pfade/{karten} Karten, Quelle hat "
                              f"{stat['pfade']}/{stat['karten']} – JSON neu erzeugen"))
    farben = [daten["mapdata"].get("mapbg")] + [p.get("color") for p in pfade] + \
             [b.get("color") for p in pfade for b in (p.get("boxes") or [])]
    for f in farben:
        if f and not HEX_RE.match(str(f)):
            befunde.append(Befund("❌", pfad.name, f"Farbe '{f}' nicht aufgelöst"))
            break


# ─────────────────────────────── Ausgabe ───────────────────────────────

def bericht(datei: Path, befunde: list[Befund], stat: dict) -> str:
    zeilen = [f"# Prüfung Edumap-Quelle: {datei.name}", "",
              f"Pfade: {stat.get('pfade', 0)} · Karten: {stat.get('karten', 0)} "
              f"(ausgeklappt: {stat.get('ausgeklappt', 0)}) · Quiz: {stat.get('quiz', 0)} · "
              f"Abstimmungen: {stat.get('abstimmung', 0)} · externe Links: {len(stat.get('links', ()))}", ""]
    for stufe in ("❌", "⚠", "ℹ"):
        for b in (b for b in befunde if b.stufe == stufe):
            zeilen.append(f"- {b.stufe} {b.ort}: {b.text}")
    if stat.get("links"):
        zeilen += ["", "Links (mit material-pruefen bzw. linkcheck.py prüfen):"]
        zeilen += [f"- {u}" for u in sorted(stat["links"])]
    f = sum(b.stufe == "❌" for b in befunde)
    w = sum(b.stufe == "⚠" for b in befunde)
    zeilen += ["", f"Ergebnis: {f} Fehler, {w} Warnungen" + (" – syntaktisch bereit für edu-edumap" if not f else "")]
    return "\n".join(zeilen)


def pruefe_datei(datei: Path, json_datei: Path | None = None) -> tuple[list[Befund], dict]:
    befunde: list[Befund] = []
    text = datei.read_text(encoding="utf-8")
    if datei.suffix.lower() in (".yaml", ".yml"):
        kopf, pfade = lies_yaml(text, befunde)
    else:
        kopf, pfade = lies_markdown(text, befunde)
    stat = pruefe(kopf, pfade, befunde, datei.parent)
    if json_datei is not None:
        pruefe_json(json_datei, stat, befunde)
    return befunde, stat


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Edumap-Quelle (.md/.yaml) vor dem Erzeugen prüfen.")
    p.add_argument("quelle", type=Path)
    p.add_argument("--json", type=Path, default=None, help="erzeugte Import-Datei gegenprüfen")
    a = p.parse_args(argv)
    if not a.quelle.is_file():
        print(f"Datei nicht gefunden: {a.quelle}", file=sys.stderr)
        return 2
    befunde, stat = pruefe_datei(a.quelle, a.json)
    print(bericht(a.quelle, befunde, stat))
    return 1 if any(b.stufe == "❌" for b in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
