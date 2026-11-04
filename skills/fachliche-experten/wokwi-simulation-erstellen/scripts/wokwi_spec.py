#!/usr/bin/env python3
"""wokwi_spec – Spec einer Steuerungsaufgabe für die Wokwi-Simulation lesen und prüfen.

Die Spec (YAML) beschreibt die Aufgabe so, wie sie im Material steht: Zuordnungsliste, GRAFCET in
Textform, Zwangssteuerung (Stopp, Schutzfunktionen), Verknüpfungen (Logikplan) und Testfälle aus der
Funktionsbeschreibung. Bedingungen stehen in der Schreibweise des Notationsblatts:

    UND ·   ODER +   NICHT ¬   Flanke ↑-S1 ↓-S1   Zeit 5s/X3   Vergleich [-BT1 ≥ 30 °C]   immer 1

Format: references/spec-format.md. Nur Python-Standardbibliothek und PyYAML.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

# ───────────────────────────── Plattformen ─────────────────────────────
# Pegel, ADC und Pins nach normen-technik.md Abschn. 4; Wokwi-Bauteile nach docs.wokwi.com.
# „eap_*“: Ein- und Ausgänge der E/A-Platine (Anlage der Ein- und Ausgänge, Reihenfolge für `entwurf`).

PLATTFORMEN: dict[str, dict] = {
    "arduino-uno": {
        "name": "Arduino Uno",
        "teil": "wokwi-arduino-uno",
        "id": "uno",
        "vcc": "5V",
        "gnd_oben": "GND.1",
        "gnd_unten": "GND.2",
        "spannung": 5.0,
        "digital": [f"D{i}" for i in range(2, 14)] + [f"A{i}" for i in range(6)],
        "verboten": {"D0": "RX der seriellen Schnittstelle", "D1": "TX der seriellen Schnittstelle"},
        "nur_eingang": [],
        "analog": [f"A{i}" for i in range(6)],
        "eap_di": [f"D{i}" for i in range(2, 8)],
        "eap_do": [f"D{i}" for i in range(8, 14)],
        "eap_ai": ["A0", "A1"],
        "adc": "analogRead",
        "adc_text": "4 … 20 mA über 250 Ω → 1 … 5 V → analogRead 205 … 1023",
        "rohbereich": (205, 1023),        # 4 mA bzw. 20 mA
        "roh_vcc": 1023,                  # Rohwert bei Versorgungsspannung (Poti am Anschlag)
        "fqbn": "arduino:avr:uno",
        "firmware": "build/sketch.ino.hex",
        "wokwi_neu": "https://wokwi.com/projects/new/arduino-uno",
    },
    "esp32": {
        "name": "ESP32 DevKitC V4",
        "teil": "board-esp32-devkit-c-v4",
        "id": "esp",
        "vcc": "3V3",
        "gnd_oben": "GND.2",
        "gnd_unten": "GND.1",
        "spannung": 3.3,
        "digital": [f"GPIO{i}" for i in (2, 4, 5, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23,
                                          25, 26, 27, 32, 33, 34, 35, 36, 39)],
        "verboten": {**{f"GPIO{i}": "Flash-Speicher" for i in range(6, 12)},
                     "GPIO1": "TX der seriellen Schnittstelle", "GPIO3": "RX der seriellen Schnittstelle"},
        "nur_eingang": ["GPIO34", "GPIO35", "GPIO36", "GPIO39"],
        "analog": ["GPIO32", "GPIO33", "GPIO34", "GPIO35", "GPIO36", "GPIO39"],
        "eap_di": ["GPIO16", "GPIO17", "GPIO18", "GPIO19"],
        "eap_do": ["GPIO25", "GPIO26", "GPIO27", "GPIO32", "GPIO33"],
        "eap_ai": ["GPIO34", "GPIO35"],
        "adc": "analogReadMilliVolts",
        "adc_text": "4 … 20 mA über 120 Ω → 0,48 … 2,4 V → analogReadMilliVolts 480 … 2400",
        "rohbereich": (480, 2400),
        "roh_vcc": 3300,
        "fqbn": "esp32:esp32:esp32",
        "firmware": "build/sketch.ino.bin",
        "wokwi_neu": "https://wokwi.com/projects/new/esp32",
    },
}
# Wokwi-Pinname eines Board-Pins: D2 → "2", A0 → "A0", GPIO34 → "34" bzw. VP/VN für 36/39
_ESP_SONDER = {"GPIO36": "VP", "GPIO39": "VN"}


def wokwi_pin(plattform: str, pin: str) -> str:
    if plattform == "arduino-uno":
        return pin[1:] if pin.startswith("D") else pin
    return _ESP_SONDER.get(pin, pin.replace("GPIO", ""))


def pin_nummer(plattform: str, pin: str) -> int:
    """Pin-Nummer wie im Programm: Uno D2 → 2, A0 → 14; ESP32 GPIO34 → 34."""
    if plattform == "arduino-uno":
        return 14 + int(pin[1:]) if pin.startswith("A") else int(pin[1:])
    return int(pin.replace("GPIO", ""))


def pin_im_code(plattform: str, pin: str) -> str:
    if plattform == "arduino-uno":
        return pin if pin.startswith("A") else pin[1:]
    return pin.replace("GPIO", "")


# ───────────────────────────── Zeiten ─────────────────────────────

_EINHEIT_MS = {"ms": 1, "s": 1000, "min": 60_000, "h": 3_600_000}
_DAUER = re.compile(r"(\d+(?:[.,]\d+)?)\s*(ms|min|s|h)")


class SpecFehler(ValueError):
    pass


def dauer_ms(text) -> int:
    """'5min' → 300000; '4min 59s', '5,5h', '100ms'; Zahl ohne Einheit = Sekunden."""
    if isinstance(text, (int, float)):
        return int(round(float(text) * 1000))
    s = str(text).strip()
    rest = _DAUER.sub("", s).strip()
    teile = _DAUER.findall(s)
    if not teile or rest:
        raise SpecFehler(f"Zeitangabe „{text}“ nicht lesbar (z. B. 3s, 5min, 5,5h, 4min 59s)")
    return int(round(sum(float(z.replace(",", ".")) * _EINHEIT_MS[e] for z, e in teile)))


def dauer_text(ms: int) -> str:
    """300000 → '5 min', 3000 → '3 s', 19800000 → '330 min' (Schreibweise wie in der Aufgabe)."""
    for einheit, faktor in (("h", 3_600_000), ("min", 60_000), ("s", 1000)):
        if ms >= faktor and ms % faktor == 0 and not (einheit == "h" and ms % 3_600_000):
            return f"{ms // faktor} {einheit}"
    if ms >= 1000:
        return f"{round(ms / 1000, 1):g} s".replace(".", ",")
    return f"{ms} ms"


@dataclass
class Zeitraffer:
    faktor: int = 1
    ab_ms: int = 60_000

    def __call__(self, ms: int) -> int:
        """Simulationszeit einer Aufgabenzeit (wie zeit() im Sketch, ganzzahlig)."""
        return ms // self.faktor if self.faktor > 1 and ms >= self.ab_ms else ms

    def text(self) -> str:
        if self.faktor <= 1:
            return "Echtzeit"
        return (f"Zeitraffer 1:{self.faktor} für Zeiten ab {dauer_text(self.ab_ms)} "
                f"({dauer_text(self.ab_ms)} → {dauer_text(self(self.ab_ms))}); kürzere Zeiten in Echtzeit")


# ───────────────────────────── Bedingungen ─────────────────────────────
# Knoten: ("const", bool) ("sig", name) ("schritt", n) ("nicht", k) ("und", [k…]) ("oder", [k…])
#         ("flanke", "↑"|"↓", name) ("zeit", ms, n) ("vgl", name, op, wert, einheit)

_BMK = r"-[A-Z]{1,3}\d+"
_NAME = r"[A-Za-z][A-Za-z0-9_]*"
_TOKEN = re.compile(rf"""
    (?P<leer>\s+)
  | (?P<zeit>\d+(?:[.,]\d+)?(?:ms|min|s|h)/X\d+)
  | (?P<vgl>\[[^\]]*\])
  | (?P<bmk>{_BMK})
  | (?P<name>{_NAME})
  | (?P<zahl>[01])(?![\d.,])
  | (?P<op>[·*+¬↑↓()])
""", re.VERBOSE)
_VGL = re.compile(rf"^\[\s*({_BMK}|{_NAME})\s*(≥|≤|>=|<=|≠|!=|=|<|>)\s*([−-]?\d+(?:[.,]\d+)?)\s*([^\s\]]*)\s*\]$")
_OP_NORM = {">=": "≥", "<=": "≤", "!=": "≠"}


def zahl(text) -> float:
    if isinstance(text, (int, float)):
        return float(text)
    return float(str(text).strip().replace("−", "-").replace(",", "."))


def _tokens(text: str) -> list[tuple[str, str]]:
    pos, aus = 0, []
    while pos < len(text):
        m = _TOKEN.match(text, pos)
        if not m:
            raise SpecFehler(f"Bedingung „{text}“: nicht lesbar ab „{text[pos:pos + 12]}“ "
                             "(Schreibweise des Notationsblatts: · + ¬ ↑ ↓ 5s/X3 [-BT1 ≥ 30 °C])")
        if m.lastgroup != "leer":
            aus.append((m.lastgroup, m.group()))
        pos = m.end()
    return aus


def bedingung(text) -> tuple:
    """Bedingung in der Schreibweise des Notationsblatts → Syntaxbaum. NICHT vor UND vor ODER."""
    roh = str(text).strip()
    if roh == "":
        raise SpecFehler("leere Bedingung")
    toks = _tokens(roh)
    pos = 0

    def sieh():
        return toks[pos] if pos < len(toks) else (None, None)

    def nimm():
        nonlocal pos
        pos += 1
        return toks[pos - 1]

    def oder():
        teile = [und()]
        while sieh()[1] == "+":
            nimm()
            teile.append(und())
        return teile[0] if len(teile) == 1 else ("oder", teile)

    def und():
        teile = [nicht()]
        while sieh()[1] in ("·", "*"):
            nimm()
            teile.append(nicht())
        return teile[0] if len(teile) == 1 else ("und", teile)

    def nicht():
        if sieh()[1] == "¬":
            nimm()
            return ("nicht", nicht())
        return atom()

    def atom():
        art, wert = sieh()
        if art is None:
            raise SpecFehler(f"Bedingung „{roh}“ endet unerwartet")
        nimm()
        if wert == "(":
            k = oder()
            if sieh()[1] != ")":
                raise SpecFehler(f"Bedingung „{roh}“: „)“ fehlt")
            nimm()
            return k
        if wert in ("↑", "↓"):
            a2, w2 = nimm() if pos < len(toks) else (None, None)
            if a2 not in ("bmk", "name"):
                raise SpecFehler(f"Bedingung „{roh}“: nach {wert} fehlt ein Kennzeichen")
            return ("flanke", wert, w2)
        if art == "zeit":
            dauer, schritt = wert.split("/X")
            return ("zeit", dauer_ms(dauer), int(schritt))
        if art == "vgl":
            m = _VGL.match(wert)
            if not m:
                raise SpecFehler(f"Vergleich „{wert}“ nicht lesbar (z. B. [-BT1 ≥ 30 °C], [C_Teile = 10])")
            op = _OP_NORM.get(m.group(2), m.group(2))
            return ("vgl", m.group(1), op, zahl(m.group(3)), m.group(4))
        if art == "zahl":
            return ("const", wert == "1")
        if art == "name" and re.fullmatch(r"X\d+", wert):
            return ("schritt", int(wert[1:]))
        if art in ("bmk", "name"):
            return ("sig", wert)
        raise SpecFehler(f"Bedingung „{roh}“: unerwartetes Zeichen „{wert}“")

    baum = oder()
    if pos != len(toks):
        raise SpecFehler(f"Bedingung „{roh}“: unerwartet „{toks[pos][1]}“")
    return baum


def knoten(baum: tuple):
    """Alle Knoten eines Syntaxbaums (Tiefensuche)."""
    yield baum
    if baum[0] == "nicht":
        yield from knoten(baum[1])
    elif baum[0] in ("und", "oder"):
        for k in baum[1]:
            yield from knoten(k)


# ───────────────────────────── Datenklassen ─────────────────────────────

@dataclass
class Eingang:
    bmk: str
    name: str
    pin: str
    kontakt: str = "NO"
    bauteil: str = "taster"
    signal_1: str = ""
    start: int = 0
    farbe: str = ""
    taste: str = ""
    kurz: str = ""


@dataclass
class Analog:
    bmk: str
    name: str
    pin: str
    bereich: tuple[float, float]
    einheit: str
    start: float
    signal: str = "4 … 20 mA"
    rohbereich: tuple[int, int] = (0, 0)
    stellen: int = 1
    kurz: str = ""


@dataclass
class Ausgang:
    bmk: str
    name: str
    pin: str
    signal_1: str = ""
    farbe: str = ""
    kurz: str = ""


@dataclass
class Merker:
    name: str
    text: str = ""
    typ: str = "bool"
    start: int = 0
    setzen: tuple | None = None
    ruecksetzen: tuple | None = None
    setzen_text: str = ""
    ruecksetzen_text: str = ""
    dominant: str = "ruecksetzen"


@dataclass
class Aktion:
    art: str               # kontinuierlich | aktivierung | deaktivierung
    ziel: str
    bedingung: tuple | None = None
    bedingung_text: str = ""
    ausdruck: tuple | None = None    # ("wert", n) | ("plus", name, n) | ("minus", name, n)
    text: str = ""


@dataclass
class Transition:
    bedingung: tuple
    text: str
    ziel: int


@dataclass
class Schritt:
    nr: int
    name: str
    aktionen: list[Aktion] = field(default_factory=list)
    transitionen: list[Transition] = field(default_factory=list)
    kommentar: str = ""


@dataclass
class Erzwingen:
    bedingung: tuple
    text: str
    nach: int
    grund: str = ""


@dataclass
class Zuweisung:
    ziel: str
    bedingung: tuple
    text: str
    grund: str = ""


@dataclass
class TestSchritt:
    nr: int
    setze: dict = field(default_factory=dict)
    druecke: list = field(default_factory=list)
    loese: list = field(default_factory=list)
    tippe: list = field(default_factory=list)
    warte_ms: int = 0
    schrittzeit_ms: int | None = None
    vorher: dict = field(default_factory=dict)
    erwarte: dict = field(default_factory=dict)
    text: str = ""


@dataclass
class Testfall:
    nr: str
    name: str
    start: dict
    ablauf: list[TestSchritt]
    zweck: str = ""


@dataclass
class Spec:
    titel: str
    kurztitel: str
    plattform: str
    quelle: str
    zeitraffer: Zeitraffer
    eingaenge: list[Eingang]
    analog: list[Analog]
    ausgaenge: list[Ausgang]
    merker: list[Merker]
    schritte: list[Schritt]
    initial: int
    erzwingen: list[Erzwingen]
    zuweisungen: list[Zuweisung]
    testfaelle: list[Testfall]
    annahmen: list[str]
    pruefauftraege: list[str]
    pfad: Path | None = None
    roh: dict = field(default_factory=dict)

    # Nachschlagen
    @property
    def p(self) -> dict:
        return PLATTFORMEN[self.plattform]

    def eingang(self, bmk: str) -> Eingang | None:
        return next((e for e in self.eingaenge if e.bmk == bmk), None)

    def analogwert(self, bmk: str) -> Analog | None:
        return next((a for a in self.analog if a.bmk == bmk), None)

    def ausgang(self, bmk: str) -> Ausgang | None:
        return next((a for a in self.ausgaenge if a.bmk == bmk), None)

    def merk(self, name: str) -> Merker | None:
        return next((m for m in self.merker if m.name == name), None)

    def schritt(self, nr: int) -> Schritt | None:
        return next((s for s in self.schritte if s.nr == nr), None)

    def alle_bedingungen(self):
        """(Ort, Syntaxbaum, Schritt der Transition oder None)."""
        for m in self.merker:
            if m.setzen:
                yield f"Merker {m.name} (setzen)", m.setzen, None
            if m.ruecksetzen:
                yield f"Merker {m.name} (rücksetzen)", m.ruecksetzen, None
        for e in self.erzwingen:
            yield f"Erzwingen „{e.text}“", e.bedingung, None
        for s in self.schritte:
            for t in s.transitionen:
                yield f"Transition X{s.nr} → X{t.ziel}", t.bedingung, s.nr
            for a in s.aktionen:
                if a.bedingung:
                    yield f"Aktion {a.ziel} in X{s.nr}", a.bedingung, None
        for z in self.zuweisungen:
            yield f"Verknüpfung {z.ziel}", z.bedingung, None

    def zeiten(self) -> list[tuple[int, int]]:
        """Alle Zeitbedingungen (Schritt, ms) in Reihenfolge des Auftretens, ohne Dopplung."""
        aus: list[tuple[int, int]] = []
        for _, baum, _ in self.alle_bedingungen():
            for k in knoten(baum):
                if k[0] == "zeit" and (k[2], k[1]) not in aus:
                    aus.append((k[2], k[1]))
        return aus

    def flanken(self) -> list[str]:
        aus: list[str] = []
        for _, baum, _ in self.alle_bedingungen():
            for k in knoten(baum):
                if k[0] == "flanke" and k[2] not in aus:
                    aus.append(k[2])
        return aus

    def aktionsziele(self) -> dict[str, set[str]]:
        """Ziel → Arten der Aktionen (kontinuierlich, aktivierung, deaktivierung)."""
        ziele: dict[str, set[str]] = {}
        for s in self.schritte:
            for a in s.aktionen:
                ziele.setdefault(a.ziel, set()).add(a.art)
        return ziele

    def gespeichert(self) -> bool:
        return any(a.art != "kontinuierlich" for s in self.schritte for a in s.aktionen)


# ───────────────────────────── Laden ─────────────────────────────

_AKTION_SPEICHERND = re.compile(rf"^([↑↓])\s*({_BMK}|{_NAME})\s*:=\s*(.+)$")
_AUSDRUCK = re.compile(rf"^(?:({_NAME}|{_BMK})\s*([+−-])\s*(\d+)|([−-]?\d+))$")


def _aktion(text: str) -> Aktion:
    s = str(text).strip()
    m = _AKTION_SPEICHERND.match(s)
    if m:
        pfeil, ziel, rechts = m.groups()
        r = _AUSDRUCK.match(rechts.strip())
        if not r:
            raise SpecFehler(f"Aktion „{s}“: rechts von := nur Zahl oder Name ± Zahl (C_Teile + 1)")
        if r.group(4) is not None:
            ausdruck = ("wert", int(zahl(r.group(4))))
        else:
            if r.group(1) != ziel:
                raise SpecFehler(f"Aktion „{s}“: nur Zähler der Art {ziel} := {ziel} + 1")
            ausdruck = ("plus" if r.group(2) == "+" else "minus", ziel, int(r.group(3)))
        return Aktion("aktivierung" if pfeil == "↑" else "deaktivierung", ziel, ausdruck=ausdruck, text=s)
    ziel, _, bed = s.partition(" wenn ")
    ziel = ziel.strip()
    if not re.fullmatch(rf"{_BMK}|{_NAME}", ziel):
        raise SpecFehler(f"Aktion „{s}“: Ziel muss ein Kennzeichen oder Merker sein "
                         "(„-QA2“, „M_Pumpe“, „-M1 wenn -B2“, „↑ C_Teile := C_Teile + 1“)")
    if bed.strip():
        return Aktion("kontinuierlich", ziel, bedingung(bed), bed.strip(), text=s)
    return Aktion("kontinuierlich", ziel, text=s)


def _transitionen(text: str) -> list[Transition]:
    aus = []
    for teil in str(text).split(";"):
        teil = teil.strip()
        if not teil:
            continue
        if "→" not in teil and "->" not in teil:
            raise SpecFehler(f"Transition „{teil}“: Folgeschritt nach „→“ fehlt (z. B. „5s/X1 → 2“)")
        links, _, rechts = teil.replace("->", "→").rpartition("→")
        rechts = rechts.strip()
        if re.search(r"\bund\b|parallel", rechts):
            raise SpecFehler(f"Transition „{teil}“: Parallelverzweigungen werden nicht simuliert "
                             "(Lücke, references/spec-format.md)")
        m = re.fullmatch(r"X?(\d+)", rechts)
        if not m:
            raise SpecFehler(f"Transition „{teil}“: Folgeschritt „{rechts}“ ist keine Schrittnummer")
        aus.append(Transition(bedingung(links), links.strip(), int(m.group(1))))
    return aus


def _wert(spec_eintrag, schluessel, standard=None):
    v = spec_eintrag.get(schluessel, standard)
    return standard if v is None else v


def _testschritt(nr: int, roh) -> TestSchritt:
    if not isinstance(roh, dict):
        raise SpecFehler(f"Testschritt {nr}: Eintrag muss ein Mapping sein (setze, tippe, warte, erwarte …)")
    erlaubt = {"setze", "druecke", "loese", "tippe", "warte", "schrittzeit", "vorher", "erwarte", "text"}
    fremd = set(roh) - erlaubt
    if fremd:
        raise SpecFehler(f"Testschritt {nr}: unbekannte Schlüssel {sorted(fremd)} (erlaubt: {sorted(erlaubt)})")

    def liste(k):
        v = roh.get(k) or []
        return [v] if isinstance(v, str) else list(v)

    ts = TestSchritt(nr, setze=dict(roh.get("setze") or {}), druecke=liste("druecke"), loese=liste("loese"),
                     tippe=liste("tippe"), vorher=dict(roh.get("vorher") or {}),
                     erwarte=dict(roh.get("erwarte") or {}), text=str(roh.get("text", "")))
    if "warte" in roh:
        ts.warte_ms = dauer_ms(roh["warte"])
    if "schrittzeit" in roh:
        ts.schrittzeit_ms = dauer_ms(roh["schrittzeit"])
    if ts.vorher and ts.schrittzeit_ms is None:
        raise SpecFehler(f"Testschritt {nr}: „vorher“ nur zusammen mit „schrittzeit“")
    if ts.warte_ms and ts.schrittzeit_ms is not None:
        raise SpecFehler(f"Testschritt {nr}: „warte“ und „schrittzeit“ nicht im selben Schritt")
    return ts


def lade(quelle) -> Spec:
    """Spec aus YAML-Datei (Pfad) oder Mapping. SpecFehler bei Form- und Schreibfehlern."""
    pfad = None
    if isinstance(quelle, (str, Path)) and Path(quelle).is_file():
        pfad = Path(quelle)
        if yaml is None:
            raise SpecFehler("PyYAML fehlt (pip install pyyaml)")
        roh = yaml.safe_load(pfad.read_text(encoding="utf-8")) or {}
    elif isinstance(quelle, dict):
        roh = quelle
    else:
        raise SpecFehler(f"Spec „{quelle}“ nicht gefunden")
    if not isinstance(roh, dict):
        raise SpecFehler("Spec ist kein Mapping")

    plattform = str(roh.get("plattform", "arduino-uno"))
    if plattform not in PLATTFORMEN:
        raise SpecFehler(f"plattform „{plattform}“ unbekannt ({' | '.join(PLATTFORMEN)})")
    pf = PLATTFORMEN[plattform]

    zr = roh.get("zeitraffer") or {}
    if isinstance(zr, (int, float)):
        zr = {"faktor": zr}
    zeitraffer = Zeitraffer(int(zr.get("faktor", 1)), dauer_ms(zr.get("ab", "1min")))

    eingaenge = []
    for e in roh.get("eingaenge") or []:
        kontakt = _wert(e, "kontakt", "NO")
        if kontakt is False:      # YAML 1.1 liest ein ungequotetes NO als false
            kontakt = "NO"
        kontakt = str(kontakt).upper()
        bauteil = str(_wert(e, "bauteil", "taster"))
        start = int(_wert(e, "start", 1 if kontakt == "NC" else 0))
        eingaenge.append(Eingang(str(e["bmk"]), str(e.get("name", "")), str(e["pin"]), kontakt, bauteil,
                                 str(e.get("signal_1", "")), start, str(e.get("farbe", "")),
                                 str(e.get("taste", "")), str(e.get("kurz", ""))))
    analog = []
    for a in roh.get("analogeingaenge") or roh.get("analog") or []:
        b = a.get("bereich") or [0, 100]
        rb = a.get("rohbereich") or pf["rohbereich"]
        analog.append(Analog(str(a["bmk"]), str(a.get("name", "")), str(a["pin"]), (zahl(b[0]), zahl(b[1])),
                             str(a.get("einheit", "")), zahl(_wert(a, "start", b[0])),
                             str(a.get("signal", "4 … 20 mA")), (int(rb[0]), int(rb[1])),
                             int(_wert(a, "stellen", 1)), str(a.get("kurz", ""))))
    ausgaenge = [Ausgang(str(a["bmk"]), str(a.get("name", "")), str(a["pin"]), str(a.get("signal_1", "")),
                         str(a.get("farbe", "")), str(a.get("kurz", ""))) for a in roh.get("ausgaenge") or []]
    merker = []
    for m in roh.get("merker") or []:
        if isinstance(m, str):
            m = {"name": m}
        mk = Merker(str(m["name"]), str(m.get("text", "")), str(m.get("typ", "bool")), int(_wert(m, "start", 0)),
                    dominant=str(m.get("dominant", "ruecksetzen")))
        if m.get("setzen") is not None:
            mk.setzen, mk.setzen_text = bedingung(m["setzen"]), str(m["setzen"])
        if m.get("ruecksetzen") is not None:
            mk.ruecksetzen, mk.ruecksetzen_text = bedingung(m["ruecksetzen"]), str(m["ruecksetzen"])
        merker.append(mk)

    schritte, initial = [], None
    for s in roh.get("grafcet") or []:
        nr = int(s["schritt"])
        aktionen = [_aktion(a) for a in (s.get("aktionen") or []) if str(a).strip() not in ("", "–", "-")]
        trans = _transitionen(s["transition"]) if s.get("transition") else []
        schritte.append(Schritt(nr, str(s.get("name", f"Schritt {nr}")), aktionen, trans,
                                str(s.get("kommentar", ""))))
        if s.get("initial"):
            initial = nr
    if initial is None:
        initial = 0 if any(s.nr == 0 for s in schritte) else (schritte[0].nr if schritte else 0)

    erzw = []
    for e in roh.get("erzwingen") or []:
        erzw.append(Erzwingen(bedingung(e["bedingung"]), str(e["bedingung"]), int(_wert(e, "nach", initial)),
                              str(e.get("grund", e.get("text", "")))))
    zuw = [Zuweisung(str(z["ziel"]), bedingung(z["bedingung"]), str(z["bedingung"]), str(z.get("grund", "")))
           for z in roh.get("zuweisungen") or []]

    tests = []
    for i, t in enumerate(roh.get("testfaelle") or [], 1):
        ablauf = [_testschritt(j, r) for j, r in enumerate(t.get("ablauf") or [], 1)]
        tests.append(Testfall(str(t.get("nr", f"T{i}")), str(t.get("name", f"Testfall {i}")),
                              dict(t.get("start") or {}), ablauf, str(t.get("zweck", ""))))

    titel = str(roh.get("titel", "Steuerung"))
    kurz = str(roh.get("kurztitel") or re.sub(r"[^a-z0-9]+", "-", titel.lower()).strip("-"))
    return Spec(titel, kurz, plattform, str(roh.get("quelle", "")), zeitraffer, eingaenge, analog, ausgaenge,
                merker, schritte, initial, erzw, zuw, tests,
                [str(a) for a in roh.get("annahmen") or []], [str(p) for p in roh.get("pruefauftraege") or []],
                pfad, roh)


# ───────────────────────────── Prüfen ─────────────────────────────

@dataclass
class Befund:
    stufe: str      # ❌ | ⚠️
    text: str

    def __str__(self) -> str:
        return f"{self.stufe} {self.text}"


def variable(bmk_oder_name: str) -> str:
    """Bezeichner im Programm (Notationsblatt Abschn. 6): -S1 → s1, -BL1 → bl1; Merker bleiben."""
    return bmk_oder_name[1:].lower() if bmk_oder_name.startswith("-") else bmk_oder_name


def pruefe(spec: Spec) -> list[Befund]:
    """Inhaltliche Prüfung: Kennzeichen, Pins, GRAFCET, Bedingungen, Testfälle, Zeitraffer."""
    b: list[Befund] = []
    fehler = lambda t: b.append(Befund("❌", t))       # noqa: E731
    warn = lambda t: b.append(Befund("⚠️", t))         # noqa: E731
    pf = spec.p

    # Kennzeichen und Namen
    alle = [e.bmk for e in spec.eingaenge] + [a.bmk for a in spec.analog] + [a.bmk for a in spec.ausgaenge]
    for k in alle:
        if not re.fullmatch(_BMK, k):
            fehler(f"Kennzeichen „{k}“ nicht nach Notationsblatt (Bindestrich, Kennbuchstabe(n), Zählnummer: -S1)")
    for k in sorted({k for k in alle if alle.count(k) > 1}):
        fehler(f"Kennzeichen {k} mehrfach belegt")
    namen = [m.name for m in spec.merker]
    for n in namen:
        if not re.fullmatch(_NAME, n) or re.fullmatch(r"X\d+", n):
            fehler(f"Merker „{n}“: sprechender Name ohne Bindestrich, nicht X+Zahl (`M_Pumpe`)")
    for n in sorted({n for n in namen if namen.count(n) > 1}):
        fehler(f"Merker {n} mehrfach angelegt")
    belegt = {variable(k) for k in alle}
    for n in namen:
        if n in belegt or n.lower() in belegt:
            fehler(f"Merker {n} kollidiert mit dem Signal eines Kennzeichens")

    # Pins
    pins = [(x.bmk, x.pin) for x in (*spec.eingaenge, *spec.analog, *spec.ausgaenge)]
    for p in sorted({p for _, p in pins if [q for _, q in pins].count(p) > 1}):
        fehler(f"Pin {p} mehrfach belegt ({', '.join(k for k, q in pins if q == p)})")
    for bmk, p in pins:
        if p in pf["verboten"]:
            fehler(f"{bmk}: Pin {p} nicht verwenden ({pf['verboten'][p]})")
        elif p not in pf["digital"]:
            fehler(f"{bmk}: Pin „{p}“ gibt es auf {pf['name']} nicht (Schreibweise wie auf dem Board: "
                   f"{pf['digital'][0]}, {pf['analog'][0]})")
    for a in spec.ausgaenge:
        if a.pin in pf["nur_eingang"]:
            fehler(f"{a.bmk}: {a.pin} ist nur Eingang")
    for a in spec.analog:
        if a.pin in pf["digital"] and a.pin not in pf["analog"]:
            fehler(f"{a.bmk}: {a.pin} hat keinen Analogeingang (ADC: {', '.join(pf['analog'])})")
    eap = {"Digitaleingang": ([e.pin for e in spec.eingaenge], pf["eap_di"]),
           "Digitalausgang": ([a.pin for a in spec.ausgaenge], pf["eap_do"]),
           "Analogeingang": ([a.pin for a in spec.analog], pf["eap_ai"])}
    for art, (benutzt, platine) in eap.items():
        aussen = [p for p in benutzt if p not in platine and p in pf["digital"]]
        if aussen:
            warn(f"{art} {', '.join(aussen)} außerhalb der E/A-Platine ({platine[0]} … {platine[-1]}) – "
                 "mit der Anlage der Ein- und Ausgänge abgleichen")
    if len(spec.ausgaenge) > 16:
        fehler("mehr als 16 Ausgänge – Meldung im Sketch fasst höchstens 16 zusammen")

    # Eingänge
    for e in spec.eingaenge:
        if e.kontakt not in ("NO", "NC"):
            fehler(f"{e.bmk}: Kontaktart „{e.kontakt}“ (NO oder NC)")
        if e.bauteil not in ("taster", "schalter"):
            fehler(f"{e.bmk}: bauteil „{e.bauteil}“ (taster oder schalter)")
        if e.start not in (0, 1):
            fehler(f"{e.bmk}: start muss 0 oder 1 sein (Signal nach Zuordnungsliste)")
        if e.bauteil == "taster" and e.start != (1 if e.kontakt == "NC" else 0):
            fehler(f"{e.bmk}: Taster beginnt unbetätigt – start {1 if e.kontakt == 'NC' else 0} "
                   f"bei {e.kontakt} (dauerhaftes Signal als bauteil: schalter)")
        if not e.signal_1:
            warn(f"{e.bmk}: „signal_1“ fehlt (Spalte „Signal 1 bedeutet“ der Zuordnungsliste)")
        name = e.name.lower()
        if "start" in name and e.farbe == "red":
            warn(f"{e.bmk}: Starttaster nicht rot (DIN EN 60204-1)")
        if "stop" in name and e.farbe == "green":
            warn(f"{e.bmk}: Stopptaster nicht grün (DIN EN 60204-1)")
    for a in spec.analog:
        lo, hi = a.bereich
        if lo >= hi:
            fehler(f"{a.bmk}: Messbereich {lo} … {hi} – Anfang muss kleiner als Ende sein")
        if not lo <= a.start <= hi:
            fehler(f"{a.bmk}: Startwert {a.start} außerhalb des Messbereichs {lo} … {hi}")
        if not a.einheit:
            warn(f"{a.bmk}: Einheit fehlt")
        if not a.signal.replace(" ", "").startswith("4…20mA") and a.rohbereich == pf["rohbereich"]:
            warn(f"{a.bmk}: Signal „{a.signal}“ – Rohwertbereich {a.rohbereich} gilt für 4 … 20 mA; "
                 "für andere Signale „rohbereich“ setzen")

    # GRAFCET
    nummern = [s.nr for s in spec.schritte]
    if not spec.schritte:
        fehler("GRAFCET fehlt (Liste „grafcet“ mit Schritten)")
    for n in sorted({n for n in nummern if nummern.count(n) > 1}):
        fehler(f"Schritt {n} mehrfach")
    if spec.schritte and spec.initial not in nummern:
        fehler(f"Initialschritt {spec.initial} fehlt")
    if spec.initial != 0 and spec.schritte:
        warn(f"Initialschritt ist {spec.initial} – das Notationsblatt sieht Schritt 0 vor")
    for s in spec.schritte:
        if not s.transitionen:
            warn(f"X{s.nr} hat keine Transition (Endschritt)")
        for t in s.transitionen:
            if t.ziel not in nummern:
                fehler(f"Transition X{s.nr} → X{t.ziel}: Schritt {t.ziel} fehlt")
            for k in knoten(t.bedingung):
                if k[0] == "zeit" and k[2] != s.nr:
                    fehler(f"Transition X{s.nr} → X{t.ziel}: Zeit {dauer_text(k[1])}/X{k[2]} bezieht sich auf "
                           f"einen anderen Schritt – „Zeit auf den falschen Schritt bezogen“ (normen-technik.md)")
    erreichbar, offen = set(), [spec.initial]
    for e in spec.erzwingen:
        offen.append(e.nach)
    while offen:
        n = offen.pop()
        if n in erreichbar or spec.schritt(n) is None:
            continue
        erreichbar.add(n)
        offen += [t.ziel for t in spec.schritt(n).transitionen]
    for s in spec.schritte:
        if s.nr not in erreichbar:
            warn(f"X{s.nr} ist vom Initialschritt aus nicht erreichbar")
    for e in spec.erzwingen:
        if e.nach not in nummern:
            fehler(f"Erzwingen „{e.text}“: Schritt {e.nach} fehlt")

    # Aktionen und Quellen der Ausgänge/Merker
    ziele = spec.aktionsziele()
    ausgang = {a.bmk for a in spec.ausgaenge}
    for ziel, arten in ziele.items():
        if ziel not in ausgang and spec.merk(ziel) is None:
            fehler(f"Aktion auf {ziel}: weder Ausgang der Zuordnungsliste noch Merker")
        if "kontinuierlich" in arten and len(arten) > 1:
            fehler(f"{ziel}: kontinuierlich und speichernd wirkende Aktionen nie auf dieselbe Variable "
                   "(normen-technik.md Abschn. 3)")
    zugewiesen = [z.ziel for z in spec.zuweisungen]
    for z in sorted({z for z in zugewiesen if zugewiesen.count(z) > 1}):
        fehler(f"{z}: mehrere Verknüpfungen – zu einer Bedingung zusammenfassen")
    for z in spec.zuweisungen:
        if z.ziel not in ausgang and spec.merk(z.ziel) is None:
            fehler(f"Verknüpfung auf {z.ziel}: weder Ausgang noch Merker")
        if z.ziel in ziele:
            fehler(f"{z.ziel}: Ausgang aus GRAFCET-Aktion und Verknüpfung zugleich – Aktion auf einen Merker "
                   "legen (wie `M_Pumpe`) und den Merker in der Verknüpfung verwenden")
        m = spec.merk(z.ziel)
        if m and (m.setzen or m.ruecksetzen):
            fehler(f"{z.ziel}: Merker mit Setzen/Rücksetzen und Verknüpfung zugleich")
    for m in spec.merker:
        if (m.setzen or m.ruecksetzen) and m.name in ziele:
            fehler(f"{m.name}: Merker mit Setzen/Rücksetzen und GRAFCET-Aktion zugleich")
        if m.typ not in ("bool", "int"):
            fehler(f"{m.name}: typ „{m.typ}“ (bool oder int)")
        if (m.setzen is None) != (m.ruecksetzen is None):
            warn(f"{m.name}: nur {'gesetzt' if m.setzen else 'zurückgesetzt'} – „speichernd gesetzt und nie "
                 "zurückgesetzt“ prüfen")
        if m.dominant not in ("ruecksetzen", "setzen"):
            fehler(f"{m.name}: dominant „{m.dominant}“ (ruecksetzen oder setzen)")
        if m.typ == "bool" and m.name not in ziele and m.name not in zugewiesen and not m.setzen:
            warn(f"Merker {m.name} wird nie beschrieben")
    for s in spec.schritte:
        for a in s.aktionen:
            mk = spec.merk(a.ziel)
            if a.art != "kontinuierlich" and a.ausdruck and a.ausdruck[0] != "wert" and (mk is None or mk.typ != "int"):
                fehler(f"X{s.nr}: Zähler „{a.text}“ braucht einen Merker mit typ: int")
            if a.art == "kontinuierlich" and mk is not None and mk.typ == "int":
                fehler(f"X{s.nr}: Zähler {a.ziel} nur mit speichernder Aktion (↑ {a.ziel} := {a.ziel} + 1)")
    for a in spec.ausgaenge:
        if a.bmk not in ziele and a.bmk not in zugewiesen:
            warn(f"Ausgang {a.bmk} wird nie angesteuert")

    # Bedingungen: Namen, Vergleiche, Flanken
    digital = {e.bmk for e in spec.eingaenge} | ausgang
    for ort, baum, _ in spec.alle_bedingungen():
        for k in knoten(baum):
            if k[0] == "sig":
                m = spec.merk(k[1])
                if k[1] not in digital and m is None:
                    if spec.analogwert(k[1]):
                        fehler(f"{ort}: Analogwert {k[1]} nur im Vergleich ([{k[1]} ≥ … ])")
                    else:
                        fehler(f"{ort}: {k[1]} ist weder Kennzeichen der Zuordnungsliste noch Merker")
                elif m is not None and m.typ == "int":
                    fehler(f"{ort}: Zähler {k[1]} nur im Vergleich ([{k[1]} = 10])")
            elif k[0] == "schritt" and k[1] not in nummern:
                fehler(f"{ort}: Schrittvariable X{k[1]} – Schritt fehlt")
            elif k[0] == "zeit" and k[2] not in nummern:
                fehler(f"{ort}: Zeit /X{k[2]} – Schritt fehlt")
            elif k[0] == "flanke":
                m = spec.merk(k[2])
                if k[2] not in digital and (m is None or m.typ != "bool"):
                    fehler(f"{ort}: Flanke nur an Digitalsignalen und Merkern ({k[1]}{k[2]})")
            elif k[0] == "vgl":
                an, mk = spec.analogwert(k[1]), spec.merk(k[1])
                if an:
                    if k[4] and an.einheit and k[4] != an.einheit:
                        fehler(f"{ort}: [{k[1]} {k[2]} …] in „{k[4]}“, Messbereich in „{an.einheit}“")
                    if not k[4] and an.einheit:
                        warn(f"{ort}: Vergleich mit {k[1]} ohne Einheit – Notationsblatt: physikalischer Wert mit Einheit")
                    if not an.bereich[0] <= k[3] <= an.bereich[1]:
                        warn(f"{ort}: Schwelle {k[3]:g} {k[4]} außerhalb des Messbereichs von {k[1]}")
                elif mk and mk.typ == "int":
                    if k[4]:
                        fehler(f"{ort}: Zähler {k[1]} ohne Einheit vergleichen")
                else:
                    fehler(f"{ort}: Vergleich nur mit Analogwert oder Zähler (typ: int), nicht mit {k[1]}")

    # Zeitraffer
    zr = spec.zeitraffer
    if zr.faktor < 1:
        fehler("zeitraffer.faktor muss mindestens 1 sein")
    zeiten = sorted({ms for _, ms in spec.zeiten()})
    if zr.faktor > 1:
        for t1 in zeiten:
            for t2 in zeiten:
                if t1 < t2 and zr(t1) > zr(t2):
                    warn(f"Zeitraffer vertauscht die Reihenfolge: {dauer_text(t1)} → {dauer_text(zr(t1))}, "
                         f"{dauer_text(t2)} → {dauer_text(zr(t2))}")
        for t in zeiten:
            if zr(t) < 300:
                warn(f"Zeit {dauer_text(t)} läuft im Zeitraffer nur {zr(t)} ms – kaum zu beobachten")
    elif zeiten and max(zeiten) > 600_000:
        warn(f"längste Zeit {dauer_text(max(zeiten))} in Echtzeit – Zeitraffer erwägen (zeitraffer: {{faktor: 60, ab: 1min}})")

    # Testfälle
    if not spec.testfaelle:
        warn("keine Testfälle – Funktionsbeschreibung nicht automatisch geprüft")
    bekannt = digital | {a.bmk for a in spec.analog} | set(namen) | {"X"}
    for t in spec.testfaelle:
        for k, v in t.start.items():
            _pruefe_setzen(spec, f"{t.nr} start", k, v, fehler)
        for ts in t.ablauf:
            ort = f"{t.nr} Schritt {ts.nr}"
            for k, v in ts.setze.items():
                _pruefe_setzen(spec, ort, k, v, fehler)
            for k in (*ts.druecke, *ts.loese, *ts.tippe):
                e = spec.eingang(k)
                if e is None or e.bauteil != "taster":
                    fehler(f"{ort}: drücken, lösen, tippen nur bei Tastern ({k})")
            for k, v in (*ts.erwarte.items(), *ts.vorher.items()):
                if k not in bekannt:
                    fehler(f"{ort}: erwarte {k} – unbekannt (Ausgang, Merker, Eingang oder X)")
                elif k == "X" and int(v) not in nummern:
                    fehler(f"{ort}: erwarteter Schritt X{v} fehlt")
            if not ts.erwarte and not (ts.setze or ts.druecke or ts.loese or ts.tippe or ts.warte_ms):
                warn(f"{ort}: Schritt ohne Aktion und ohne Erwartung")
    return b


def _pruefe_setzen(spec: Spec, ort: str, k: str, v, fehler) -> None:
    e, a = spec.eingang(k), spec.analogwert(k)
    if e:
        if v not in (0, 1):
            fehler(f"{ort}: {k} = {v} – Signal 0 oder 1")
    elif a:
        try:
            w = zahl(v)
        except ValueError:
            fehler(f"{ort}: {k} = {v} – Zahl erwartet")
            return
        if not a.bereich[0] <= w <= a.bereich[1]:
            fehler(f"{ort}: {k} = {v} außerhalb des Messbereichs {a.bereich[0]:g} … {a.bereich[1]:g} {a.einheit}")
    else:
        fehler(f"{ort}: {k} ist kein Eingang (setze nur Eingänge)")


# ───────────────────────────── Analogwerte ─────────────────────────────

def roh_aus_wert(spec: Spec, a: Analog, wert: float) -> int:
    """Physikalischer Wert → Rohwert am Pin (analogRead bzw. mV), wie ihn das Poti liefert."""
    lo, hi = a.bereich
    r0, r1 = a.rohbereich
    return int(round(r0 + (wert - lo) / (hi - lo) * (r1 - r0)))


def wert_aus_roh(a: Analog, roh: float) -> float:
    lo, hi = a.bereich
    r0, r1 = a.rohbereich
    return lo + (roh - r0) * (hi - lo) / (r1 - r0)


def poti_position(spec: Spec, a: Analog, wert: float) -> float:
    """Position des Wokwi-Potis (0 … 1) für einen physikalischen Wert."""
    return round(roh_aus_wert(spec, a, wert) / spec.p["roh_vcc"], 4)
