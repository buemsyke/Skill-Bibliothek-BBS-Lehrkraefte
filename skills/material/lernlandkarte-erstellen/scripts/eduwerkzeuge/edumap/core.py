#!/usr/bin/env python3
r"""
edumap - Konvertiert strukturierte Inhalte in Edumap-JSON

Unterstuetzte Eingabeformate:
  - YAML  (.yaml / .yml)
  - Markdown mit YAML-Frontmatter  (.md)
  - JSON  (.json)

Verwendung:
  edu-edumap eingabe.yaml
  edu-edumap lernlandkarte_le01_09.md -o meine_lernlandkarte_le01_09.json

MARKDOWN-STRUKTUR
  ---
  title: Titel der Map
  language: de
  theme: nacht            # Farbthema (setzt mapbg + Standard-Pfadfarbe)
  mapbg: anthrazit        # Hex-Wert (#1e2d45) ODER Farbname
  format: zeitstrahl      # Anzeigeformat: karte | pinnwand | zeitstrahl | kalender
  extras: nmc             # Kurs-Modus aktivieren
  ---

  ## Pfad-Titel [color=blau] [box_color=ozeanblau] [flags=0] [showdate=2026-06-01 10:00:00]
  # box_color: Farbe fuer alle Karten in diesem Pfad (erbt von Pfadfarbe wenn nicht gesetzt)

  ### Karten-Titel [color=ozeanblau] [flags=16420] [showdate=2026-06-01 10:00:00]
  Inhalt der Karte.

  ### Buchbar (timed) [book=timed] [booktime=2026-06-07 08:00:00] [booklimit=20]
  Buchung oeffnet am booktime, max. booklimit Teilnehmer.
  flags werden automatisch auf 524288 gesetzt.

  ### Buchbar (offen) [book=open] [booklimit=10]
  Buchung sofort offen, max. booklimit Teilnehmer.
  flags werden automatisch auf 131072 gesetzt.

  ### Quiz-Navigation [flags=1048576]
  -- {Karte A}{!#b12345}
  ~|quizstart|~

FARBTHEMEN  (theme: in Frontmatter)
  standard   Hellblau   #c4dcff  - Pfad: blau
  nacht      Nachtblau  #1e2d45  - Pfad: blau
  schiefer   Schiefer   #3d4a5c  - Pfad: tuerkis
  anthrazit  Anthrazit  #2d333d  - Pfad: indigo
  wald       Olivgrau   #383d33  - Pfad: gruen
  warm       Warmgrau   #44403c  - Pfad: orange
  abend      Mitternacht #0f172a - Pfad: lila
  morgen     Eisblau    #e8f4ff  - Pfad: tuerkis   (heller Hintergrund)
  tageslicht Hellgrau   #f1f5f9  - Pfad: blau      (sehr heller Hintergrund)
  kreide     Cremig     #fefce8  - Pfad: bernstein  (warmer heller Hintergrund)

EIGENE FARBGEBUNG  (theme: als Mapping oder YAML-Datei, z. B. passend zum Material)
  theme:
    basis: tageslicht          # optional: eingebautes Theme als Grundlage
    hintergrund: "#eef3f8"     # Name oder #rrggbb (Alias mapbg)
    pfade: [farbe1, farbe2]    # ersetzen die Standardfarben der Quelle der Reihe nach
    karten: pfad               # optional: Karten ohne Farbe in Pfadfarbe
    farben:                    # eigene Farbnamen, auch in color=/box_color= nutzbar
      farbe1: "#1f4e79"
      farbe2: "#c55a11"
  Farbtausch: die erste Standardfarbe der Quelle (Palette-Name oder ohne color)
  wird pfade[0], die zweite pfade[1] … – gleiche Farben bleiben gleich. Hex-Werte
  und eigene Namen bleiben unveraendert. Die Quelle muss dafuer nicht geaendert werden:
    theme: farben-folien.yaml                       (Datei neben der Quelle)
    edu-edumap quelle.md --theme farben-folien.yaml (von aussen, geht vor)

FARBEN AUS AUSGANGSMATERIAL
  edu-edumap --farben-aus folien.pptx               Theme-Vorschlag als YAML ausgeben
  edu-edumap --farben-aus folien.pptx -o farben.yaml
  edu-edumap quelle.md --farben-aus https://schule.example/   direkt anwenden
  Liest .pptx/.docx/.xlsx (Design- und verwendete Farben), .odp/.odt/.ods,
  HTML/CSS/SVG (Datei oder Adresse, verlinkte Stylesheets), Bilder und PDF
  (Pillow; PDF zusaetzlich pdftoppm). Pfadfarben werden bei Bedarf abgedunkelt,
  bis weisse Schrift mindestens 3:1 Kontrast hat.

ANZEIGEFORMATE  (format: in Frontmatter)
  karte      Standardansicht (Spalten und Karten)          mapformat=0
  pinnwand   Pinnwand-Ansicht                              mapformat=1
  zeitstrahl Zeitstrahl-Ansicht (nutzt showdate)           mapformat=2
  kalender   Kalender-Ansicht (nutzt showdate)             mapformat=3

FARBNAMEN  (color=, box_color=, mapbg:)
  Hintergruende dunkel:
    anthrazit   #2d333d    schiefergrau #3d4a5c    nachtblau  #1e2d45
    dunkelgrau  #374151    warmgrau     #44403c    olivgrau   #383d33
    mitternacht #0f172a    stahlblau    #1e3a5f

  Hintergruende hell:
    hellblau    #c4dcff    eisblau      #e8f4ff    mintweiss  #ecfdf5
    hellgrau    #f1f5f9    creme        #fefce8    lavendel   #f5f3ff
    pastellblau #dbeafe    pastellgruen #dcfce7    pastellrose #fce7f3

  Pfad- und Boxfarben:
    blau        #4267F5    ozeanblau    #0087CD    tuerkis    #0d9488
    mintgruen   #059669    gruen        #16a34a    waldgruen  #4d7c0f
    bernstein   #d97706    orange       #ea580c    rot        #dc2626
    koralle     #e11d48    lila         #7c3aed    violett    #6d28d9
    indigo      #4338ca    pink         #db2777    grau       #6b7280
    silber      #94a3b8

KARTEN-FLAGS  (flags= bei ###)
  0        Normal (ausgeklappt)
  4        Eingeklappt / minimiert  (Standard-Vorgabe)
  16420    Hervorgehoben / angepinnt  (empfohlen: color=ozeanblau)
  131072   Buchung offen (kein Zeitlimit)   -- wird automatisch gesetzt bei book=open
  524288   Buchung zeitgesteuert            -- wird automatisch gesetzt bei book=timed
  1048576  Navigations-Karte (kein Titel)

  PFAD-FLAGS  (flags= bei ##)
  0        Normal
  640      Gesperrt (oeffnet erst ab showdate)

BUCHUNGS-SYNTAX
  book=open   Buchung sofort offen (flags=131072 automatisch)
  book=timed  Buchung ab booktime (flags=524288 automatisch, erfordert booktime=)
  booklimit=N Maximale Teilnehmerzahl (0 = unbegrenzt)
  booktime=YYYY-MM-DD HH:MM:SS  Zeitpunkt, ab dem die Buchung oeffnet

DATEI-UPLOADS
  Dateien werden in Edumap direkt hochgeladen (Bueroklammericon).
  Die erzeugte URL hat das Format:
    https://nds.edumaps.de/file/<id>/<kuerzel>
  Diese URL kann im Inhalt (content:) als Datei-Link verwendet werden:
    https://nds.edumaps.de/file/1234567890.pdf/abc123
    Handreichung als PDF

  Fuer YAML kann auch die files:-Liste verwendet werden:
    boxes:
      - title: "Vorgabe-Sketch"
        files:
          - url: "https://nds.edumaps.de/file/5040916620291260057.zip/6ldn3fq"
            label: "uebungvorgabe.zip"
          - url: "https://example.com/datei.pdf"
            label: "Handreichung"
        content: |   <- weiterer Inhalt wird hinter die Dateien angehaengt
          Inhalt der Karte...

ZEITSTRAHL-TIPPS
  format: zeitstrahl setzt mapformat=2
  Jeder Pfad wird als Zeitleisten-Abschnitt dargestellt.
  showdate an Pfaden und Karten bestimmt die zeitliche Einordnung.
  Empfohlen fuer Stundenablauf:
    Jeden Abschnitt (Phase) als eigenen Pfad anlegen.
    showdate = geplante Startzeit der Phase.
    flags=640 am Pfad = Abschnitt erst sichtbar nach showdate.

EDUMAP-INHALTSSYNTAX  (in Karteninhalten)
  **fetter Text**               Fettdruck
  *kursiver Text*               Kursivdruck

  -- Listenpunkt                NUMMERIERTE Liste (-- = zwei Striche) → 1. 2. 3.
  - Listenpunkt                 AUFZAEHLUNG (- = ein Strich) → Punkte
  ---                           Horizontale Trennlinie

  Hinweis: -- und - sehen im Quelltext aehnlich aus, erzeugen aber
  ganz unterschiedliche Darstellungen in Edumap!

  ||| Kopf 1 | Kopf 2 | Kopf 3   Tabellenueberschrift (drei senkrechte Striche)
  || Zelle A | Zelle B | Zelle C  Tabellendatenzeile (zwei senkrechte Striche)
  Zellen trennt ein einzelner Strich | (nicht im Zelltext verwenden).
  Aeltere Quellen mit || als Zelltrenner wandelt edu-edumap automatisch um.

  `Code-Block`                  Mehrzeiliger Code-Block (Backticks)
  `Zeile1\nZeile2\nZeile3`     KEIN Carriage Return (\r) im Code erlaubt!

  {Linktext}{https://url}       Externer Link
  https://url                   Datei-/Bild-URL (Vorschau wird generiert)
  Beschriftung                  (direkt folgende Zeile = Beschriftung)
  {Text}{!#path-123}            Interner Link zu Pfad
  {Text}{!#b123}                Interner Link zu Karte
  !#anker-name                  Anker setzen
  #tag-name                     Tag
  [Anzeigetext]{Tooltip-Text}   Tooltip

  \( Formel \)                  Inline-Formel (LaTeX)
  $$ Block-Formel $$            Block-Formel (LaTeX)

  ?? Versteckter Text           Eingeklappter Text (Spoiler)

  [ ] offene Aufgabe            Checkbox (offen)
  [x] erledigte Aufgabe         Checkbox (erledigt)

  &&count: 300&&                Countdown-Timer (Sekunden)
  &&msg:popup&&                 Popup-Nachricht bei Ablauf

  {qrcode:Text oder URL}        QR-Code

  <quiz>                        Multiple-Choice-Quiz
  Option A
  # Option B -- korrekt         (Zeile mit # = richtige Antwort)
  Option C
  </quiz>

  <poll>                        Abstimmung
  Option A
  Option B
  </poll>

  <audio-de>Text</audio>        Text-to-Speech (Sprachen: de, en, fr, ...)

  ~|quizstart|~                 Quiz-Modus ab hier
  ~|coursestart|~               Kurs-Modus ab hier
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime, time
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

from .farben import Farbgebung, farbgebung


# ---------------------------------------------------------------------------
# Farbpalette
# ---------------------------------------------------------------------------

PALETTE: dict[str, str] = {
    # Hintergruende dunkel
    "anthrazit":    "#2d333d",
    "schiefergrau": "#3d4a5c",
    "nachtblau":    "#1e2d45",
    "dunkelgrau":   "#374151",
    "warmgrau":     "#44403c",
    "olivgrau":     "#383d33",
    "mitternacht":  "#0f172a",
    "stahlblau":    "#1e3a5f",
    # Hintergruende hell
    "hellblau":     "#c4dcff",
    "eisblau":      "#e8f4ff",
    "mintweiss":    "#ecfdf5",
    "hellgrau":     "#f1f5f9",
    "creme":        "#fefce8",
    "lavendel":     "#f5f3ff",
    "pastellblau":  "#dbeafe",
    "pastellgruen": "#dcfce7",
    "pastellrose":  "#fce7f3",
    # Pfad- und Boxfarben
    "blau":         "#4267F5",
    "ozeanblau":    "#0087CD",
    "tuerkis":      "#0d9488",
    "mintgruen":    "#059669",
    "gruen":        "#16a34a",
    "waldgruen":    "#4d7c0f",
    "bernstein":    "#d97706",
    "orange":       "#ea580c",
    "rot":          "#dc2626",
    "koralle":      "#e11d48",
    "lila":         "#7c3aed",
    "violett":      "#6d28d9",
    "indigo":       "#4338ca",
    "pink":         "#db2777",
    "grau":         "#6b7280",
    "silber":       "#94a3b8",
}

# ---------------------------------------------------------------------------
# Farbthemen
# ---------------------------------------------------------------------------

THEMES: dict[str, dict[str, str]] = {
    "standard":   {"mapbg": "hellblau",    "path_color": "blau"    },
    "nacht":      {"mapbg": "nachtblau",   "path_color": "blau"    },
    "schiefer":   {"mapbg": "schiefergrau","path_color": "tuerkis" },
    "anthrazit":  {"mapbg": "anthrazit",   "path_color": "indigo"  },
    "wald":       {"mapbg": "olivgrau",    "path_color": "gruen"   },
    "warm":       {"mapbg": "warmgrau",    "path_color": "orange"  },
    "abend":      {"mapbg": "mitternacht", "path_color": "lila"    },
    "morgen":     {"mapbg": "eisblau",     "path_color": "tuerkis" },
    "tageslicht": {"mapbg": "hellgrau",    "path_color": "blau"    },
    "kreide":     {"mapbg": "creme",       "path_color": "bernstein"},
}

# ---------------------------------------------------------------------------
# Anzeigeformate
# ---------------------------------------------------------------------------

MAPFORMATS: dict[str, str] = {
    "karte":      "0",
    "pinnwand":   "1",
    "zeitstrahl": "2",
    "kalender":   "3",
    # Direkteingabe als Zahl bleibt erhalten
    "0": "0", "1": "1", "2": "2", "3": "3",
}

# ---------------------------------------------------------------------------
# Buchungs-Flags
# ---------------------------------------------------------------------------

BOOK_FLAG_OPEN  = 131072   # Bit 17: Buchung sofort offen
BOOK_FLAG_TIMED = 524288   # Bit 19: Buchung zeitgesteuert (booktime + booklimit)

# ---------------------------------------------------------------------------
# Standardwerte
# ---------------------------------------------------------------------------

DEFAULTS: dict = {
    "mapbg":      "#c4dcff",
    "mapfont":    "0",
    "mapformat":  "0",
    "map_flags":  "3",
    "language":   "de",
    "path_color": "#4267F5",
    "path_flags": "0",
    "box_flags":  "4",   # Standard: eingeklappt
    "booklimit":  "0",
}


# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------

def resolve_color(value: str | None) -> str | None:
    """Loest Farbnamen aus der Palette auf; gibt Hex-Werte unveraendert zurueck."""
    if value is None:
        return None
    v = str(value).strip()
    if v.startswith("#"):
        return v
    resolved = PALETTE.get(v.lower())
    return resolved if resolved is not None else v


def _to_str(value) -> str | None:
    """Konvertiert Python datetime/date/time Objekte sicher in Strings."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    if isinstance(value, date):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, time):
        return value.strftime("%H:%M:%S")
    return str(value) if value != "" else None


def _booking_flags(src: dict) -> int:
    """
    Leitet Buchungs-Flags aus den Buchungsfeldern ab.
    book=timed  oder  booktime gesetzt  -> BOOK_FLAG_TIMED (524288)
    book=open   oder  booklimit>0       -> BOOK_FLAG_OPEN  (131072)
    """
    book_mode = str(src.get("book", "")).lower()
    booktime  = _to_str(src.get("booktime"))
    raw_limit = str(src.get("booklimit", "0"))
    booklimit = int(raw_limit) if raw_limit.isdigit() else 0

    if book_mode == "timed" or booktime:
        return BOOK_FLAG_TIMED
    if book_mode == "open" or booklimit > 0:
        return BOOK_FLAG_OPEN
    return 0


# ---------------------------------------------------------------------------
# Tabellen-Normalisierung
# ---------------------------------------------------------------------------

def _zellen(text: str, alt: bool) -> list[str]:
    """Zerlegt Tabellenzeile (ohne Praefix) in Zellen; alt = Trenner ||, neu = |."""
    return [z.strip() for z in text.split("||" if alt else "|")]


def _normalize_table_rows(content: str) -> str:
    """Schreibt Tabellen in die aktuelle edumaps-Syntax und gleicht die Spaltenzahl an.

    Aktuelle Syntax (seit der Umstellung des Anbieters, Oktober 2026):
        ||| Kopf 1 | Kopf 2 | Kopf 3       Kopfzeile
        || Zelle A | Zelle B | Zelle C     Datenzeile
    Zellen trennt ein einzelner senkrechter Strich.

    edumaps erkennt eine Tabelle nur nach einer Leerzeile; steht direkt Text darueber,
    wird die Tabelle als Fliesstext gezeigt. Die Funktion setzt die Leerzeile ein.

    Aeltere Quellen schreiben `|||Kopf||Kopf` und `||Zelle||Zelle` (Trenner `||`).
    Solche Tabellen erkennt die Funktion an der Kopfzeile und wandelt sie um.

    Datenzeilen mit weniger Zellen als die Kopfzeile werden mit leeren Zellen
    aufgefuellt (abschliessende leere Zellen werden sonst nicht dargestellt).
    Ein Zeichen `|` im Zelltext ist nicht moeglich – anderes Zeichen waehlen.
    """
    result: list[str] = []
    col_count = 0
    alt = False

    for line in content.split("\n"):
        stripped = line.strip()
        indent = line[: len(line) - len(line.lstrip())]
        if stripped.startswith("|||"):
            rest = stripped[3:]
            alt = "||" in rest
            cells = _zellen(rest, alt)
            col_count = len(cells)
            if result and result[-1].strip():
                result.append("")  # Leerzeile vor der Tabelle
            result.append(indent + "||| " + " | ".join(cells))
        elif stripped.startswith("||") and col_count > 0:
            cells = _zellen(stripped[2:], alt)
            # Bei alter Syntax erzeugt ein abschliessendes || eine leere Restzelle
            while alt and len(cells) > col_count and cells[-1] == "":
                cells.pop()
            while len(cells) < col_count:
                cells.append("")
            result.append(indent + "|| " + " | ".join(cells))
        else:
            if not stripped.startswith("||"):
                col_count = 0  # Tabellenkontext verlassen
            result.append(line)

    return "\n".join(result)


# ---------------------------------------------------------------------------
# Farbgebung (Theme-Name, eigenes Theme, Farbtausch)
# ---------------------------------------------------------------------------

class _Farbkontext:
    """Loest Farben einer Map auf: eigene Namen, Palette, Farbtausch des Themes.

    Ein eigenes Theme mit `pfade:` ersetzt die Standardfarben (Palette-Namen und die
    Standard-Pfadfarbe) der Reihe nach: die erste in der Quelle vorkommende
    Standardfarbe wird pfade[0], die zweite pfade[1] … – gleiche Farben bleiben gleich,
    verschiedene verschieden. Hex-Werte und eigene Namen bleiben, wie sie sind.
    """

    def __init__(self, fg: Farbgebung):
        self.fg = fg
        self.tausch: dict[str, str] = {}

    def _name(self, wert) -> tuple[str | None, bool]:
        """(Hex oder Rohwert, ist_standardfarbe)."""
        if wert in (None, ""):
            return None, False
        w = str(wert).strip()
        if w.startswith("#"):
            return w, False
        if w.lower() in self.fg.farben:
            return self.fg.farben[w.lower()], False
        hexwert = PALETTE.get(w.lower())
        return (hexwert, True) if hexwert else (w, False)

    def hintergrund(self, wert) -> str | None:
        return self._name(wert)[0]

    def farbe(self, wert, standard: str | None = None) -> str | None:
        hexwert, ist_standard = self._name(wert)
        if hexwert is None:
            if standard is None:
                return None
            hexwert, ist_standard = standard, True
        if ist_standard and self.fg.tauscht:
            key = hexwert.lower()
            if key not in self.tausch:
                self.tausch[key] = self.fg.pfade[len(self.tausch) % len(self.fg.pfade)]
            return self.tausch[key]
        return hexwert


def _farbkontext(theme, basis_dir: Path | None = None) -> _Farbkontext:
    return _Farbkontext(farbgebung(theme, PALETTE, THEMES, DEFAULTS["path_color"], basis_dir))


# ---------------------------------------------------------------------------
# Builder-Funktionen
# ---------------------------------------------------------------------------

def build_mapdata(src: dict) -> dict:
    fmt_raw  = str(src.get("format") or src.get("mapformat") or DEFAULTS["mapformat"])
    mapformat = MAPFORMATS.get(fmt_raw.lower(), fmt_raw)
    return {
        "title":     src.get("title", "Neue Edumap"),
        "tags":      src.get("tags"),
        "grade":     src.get("grade"),
        "mapbg":     resolve_color(src.get("mapbg")) or DEFAULTS["mapbg"],
        "mapfont":   str(src.get("mapfont", DEFAULTS["mapfont"])),
        "mapformat": mapformat,
        "flags":     str(src.get("flags", DEFAULTS["map_flags"])),
        "password":  src.get("password"),
        "language":  src.get("language", DEFAULTS["language"]),
        "extras":    src.get("extras"),
    }


def build_box(src: dict, inherited_color: str | None = None,
              farben: _Farbkontext | None = None) -> dict:
    raw_title = src.get("title")
    title = None if raw_title in (None, "", "-") else str(raw_title)

    # Farbe: explizit > vererbt > None
    color = (farben.farbe(src.get("color")) if farben else resolve_color(src.get("color"))) \
        or inherited_color

    # Buchungs-Flags: Basis-Flags mit Buchungs-Bits kombinieren
    # Buchungs-Boxen erhalten kein Eingeklappt-Flag als Standard,
    # da Buchung+Collapsed kombiniert i.d.R. nicht korrekt funktioniert.
    booking_bits = _booking_flags(src)
    has_explicit_flags = src.get("flags") is not None
    if booking_bits and not has_explicit_flags:
        base_flags = 0  # Buchungsboxen: kein Eingeklappt-Standard
    else:
        base_flags = int(str(src.get("flags") if has_explicit_flags else DEFAULTS["box_flags"]))
    combined_flags = base_flags | booking_bits

    # Inhalt aufbauen: files: zuerst (URL + Label), dann content
    raw_content = src.get("content") or ""
    # Carriage Returns entfernen (Windows-Zeilenenden), v.a. in Code-Bloecken
    raw_content = raw_content.replace("\r\n", "\n").replace("\r", "\n")
    files = src.get("files") or []
    if files:
        file_lines = []
        for f in files:
            url = (f.get("url") or "").strip()
            label = (f.get("label") or "").strip()
            if url:
                file_lines.append(url)
                if label:
                    file_lines.append(label)
        if file_lines:
            raw_content = "\n".join(file_lines) + ("\n\n" if raw_content.strip() else "") + raw_content
    content = _normalize_table_rows(raw_content)

    return {
        "title":     title,
        "content":   content,
        "subject":   src.get("subject"),
        "booktime":  _to_str(src.get("booktime")),
        "booklimit": str(src.get("booklimit", DEFAULTS["booklimit"])),
        "color":     color,
        "flags":     str(combined_flags),
        "position":  src.get("position"),
        "showdate":  _to_str(src.get("showdate")),
        "extras":    src.get("extras"),
    }


def build_path(src: dict, default_color: str | None = None,
               farben: _Farbkontext | None = None) -> dict:
    farben = farben or _Farbkontext(Farbgebung(None, DEFAULTS["path_color"], [], None, {}))
    color = farben.farbe(src.get("color"), default_color or DEFAULTS["path_color"])

    # box_color: explizit fuer alle Karten dieses Pfades gesetzt,
    # oder Pfadfarbe erben wenn color_inherit: true bzw. Theme karten: pfad
    box_color: str | None = None
    if src.get("color_inherit"):
        box_color = color
    elif src.get("box_color"):
        box_color = farben.farbe(src.get("box_color"))
    elif farben.fg.karten == "pfad":
        box_color = color
    elif farben.fg.karten:
        box_color = farben.fg.karten

    return {
        "title":      src.get("title", ""),
        "showdate":   _to_str(src.get("showdate")),
        "annotation": src.get("annotation"),
        "color":      color,
        "flags":      str(src.get("flags", DEFAULTS["path_flags"])),
        "extras":     src.get("extras"),
        "boxes":      [build_box(b, box_color, farben) for b in src.get("boxes", [])],
    }


def build_edumap(src: dict, basis_dir: Path | None = None, theme=None) -> dict:
    """Baut das finale Edumap-JSON aus einem Python-Dict auf.

    `theme` ueberschreibt das Theme der Quelle (Name, YAML-Datei oder Mapping) –
    so laesst sich dieselbe Quelle in einer anderen Farbgebung ausgeben.
    `basis_dir` ist der Ordner, gegen den eine Theme-Datei der Quelle aufgeloest wird.
    """
    mapdata_src = dict(src.get("mapdata", src))
    mapdata_src.pop("paths", None)
    spec = theme if theme is not None else (src.get("theme") or mapdata_src.get("theme"))
    farben = _farbkontext(spec, basis_dir)

    # mapbg: explizit > Theme > Standard (ein Theme von aussen geht vor)
    eigener_bg = farben.hintergrund(mapdata_src.get("mapbg"))
    if theme is not None and farben.fg.mapbg:
        eigener_bg = None
    mapdata_src["mapbg"] = eigener_bg or farben.fg.mapbg

    paths = src.get("paths") or []
    # Farbtausch in der Reihenfolge der Pfade festlegen, dann erst Kartenfarben
    for p in paths:
        farben.farbe(p.get("color"), farben.fg.standard_pfad)
    return {
        "mapdata": build_mapdata(mapdata_src),
        "paths":   [build_path(p, farben.fg.standard_pfad, farben) for p in paths],
    }


# ---------------------------------------------------------------------------
# Parser: YAML
# ---------------------------------------------------------------------------

def parse_yaml(text: str, basis_dir: Path | None = None, theme=None) -> dict:
    if not HAS_YAML:
        raise RuntimeError(
            "PyYAML ist nicht installiert. Bitte ausfuehren: pip install pyyaml"
        )
    data = yaml.safe_load(text)
    return build_edumap(data, basis_dir, theme)


# ---------------------------------------------------------------------------
# Parser: Markdown
# ---------------------------------------------------------------------------

_ATTR_RE = re.compile(r'\[(\w+)=([^\]]*)\]')


def _extract_attrs(raw: str) -> tuple[str, dict]:
    """Trennt Inline-Attribute [key=value] vom Titel."""
    attrs = {m.group(1): m.group(2) for m in _ATTR_RE.finditer(raw)}
    title = _ATTR_RE.sub("", raw).strip()
    return title, attrs


def markdown_zu_quelle(text: str) -> dict:
    """Liest Markdown mit Frontmatter in dieselbe Struktur wie eine YAML-Quelle."""
    lines = text.split("\n")

    # YAML-Frontmatter
    frontmatter: dict = {}
    content_start = 0
    if lines and lines[0].strip() == "---":
        end = next(
            (i for i, l in enumerate(lines[1:], 1) if l.strip() in ("---", "...")),
            None,
        )
        if end is not None:
            fm_text = "\n".join(lines[1:end])
            if HAS_YAML:
                frontmatter = yaml.safe_load(fm_text) or {}
            content_start = end + 1

    src: dict = {**frontmatter, "paths": []}
    current_path: dict | None = None
    current_box:  dict | None = None
    current_lines: list[str] = []

    def _commit_box() -> None:
        nonlocal current_box, current_lines
        if current_box is not None and current_path is not None:
            current_box["content"] = "\n".join(current_lines).strip()
            current_path["boxes"].append(current_box)
        current_box   = None
        current_lines = []

    for line in lines[content_start:]:
        # H2: neuer Pfad
        if line.startswith("## "):
            _commit_box()
            title, attrs = _extract_attrs(line[3:].strip())
            current_path = {
                "title":        title,
                "color":        attrs.get("color"),
                "box_color":    attrs.get("box_color"),
                "color_inherit":attrs.get("color_inherit"),
                "flags":        attrs.get("flags", DEFAULTS["path_flags"]),
                "showdate":     attrs.get("showdate"),
                "annotation":   attrs.get("annotation"),
                "extras":       attrs.get("extras"),
                "boxes":        [],
            }
            src["paths"].append(current_path)

        # H3: neue Karte
        elif line.startswith("### "):
            if current_path is None:
                current_path = {
                    "title": "", "color": None, "box_color": None,
                    "color_inherit": None,
                    "flags": DEFAULTS["path_flags"], "showdate": None,
                    "annotation": None, "extras": None, "boxes": [],
                }
                src["paths"].append(current_path)
            _commit_box()
            title, attrs = _extract_attrs(line[4:].strip())
            current_box = {
                "title":     None if title in ("", "-") else title,
                "color":     attrs.get("color"),
                "flags":     attrs.get("flags"),   # None = implizit, build_box setzt Default
                "showdate":  attrs.get("showdate"),
                "booktime":  attrs.get("booktime"),
                "booklimit": attrs.get("booklimit", DEFAULTS["booklimit"]),
                "book":      attrs.get("book", ""),
                "subject":   attrs.get("subject"),
                "extras":    attrs.get("extras"),
                "files":     ([{"url": attrs["file_url"], "label": attrs.get("file_label", "")}]
                              if attrs.get("file_url") else []),
            }
            current_lines = []

        # H1: Map-Titel -- nur ausserhalb von Karten gueltig
        elif line.startswith("# ") and not line.startswith("## ") and current_box is None:
            title, _ = _extract_attrs(line[2:].strip())
            src["title"] = title

        # Karteninhalt
        else:
            if current_box is not None:
                current_lines.append(line)

    _commit_box()
    return src


def parse_markdown(text: str, basis_dir: Path | None = None, theme=None) -> dict:
    return build_edumap(markdown_zu_quelle(text), basis_dir, theme)


# ---------------------------------------------------------------------------
# Eingabe-Dispatch
# ---------------------------------------------------------------------------

def parse_file(path: Path, theme=None) -> dict:
    text   = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    basis  = path.parent

    if suffix in (".yaml", ".yml"):
        return parse_yaml(text, basis, theme)
    if suffix == ".md":
        return parse_markdown(text, basis, theme)
    if suffix == ".json":
        raw = json.loads(text)
        if "mapdata" in raw and "paths" in raw:
            return raw
        return build_edumap(raw, basis, theme)

    try:
        return parse_yaml(text, basis, theme)
    except Exception:
        return parse_markdown(text, basis, theme)


def standardfarben_der_quelle(path: Path) -> int:
    """Zahl der verschiedenen Standardfarben der Pfade (fuer --farben-aus)."""
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".md":
        src = markdown_zu_quelle(text)
    elif HAS_YAML:
        src = yaml.safe_load(text) or {}
    else:
        return 1
    farben = _Farbkontext(Farbgebung(None, DEFAULTS["path_color"], ["#000000"], None, {}))
    for p in src.get("paths") or []:
        farben.farbe(p.get("color"), DEFAULTS["path_color"])
    return max(1, len(farben.tausch))


# ---------------------------------------------------------------------------
# Haupt-Funktion
# ---------------------------------------------------------------------------

def generate(
    input_path: Path,
    output_path: Path | None = None,
    pretty: bool = False,
    theme=None,
) -> Path:
    data = parse_file(input_path, theme)

    if output_path is None:
        date_str = datetime.now().strftime("%Y-%m-%d")
        title    = data["mapdata"].get("title", "Edumap")
        safe     = re.sub(r'[\\/:*?"<>|]', "", title).strip()[:60]
        output_path = input_path.parent / f"{date_str} Edumaps - {safe}.json"

    indent     = 2 if pretty else None
    separators = None if pretty else (",", ":")
    output_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=indent, separators=separators),
        encoding="utf-8",
    )
    return output_path
