#!/usr/bin/env python3
"""code_pruefen – Programmcode in Unterrichtsmaterial prüfen (Python, C/C++/Arduino, G-Code).

Liest Codedateien (.py, .c, .cpp, .h, .ino, .nc, .gcode, .cnc, .mpf, .tap), Markdown mit
Codeblöcken (```python, ```cpp, ```arduino, ```gcode …) sowie DOCX, ODT und PDF (über
text_lesen.py, falls vorhanden; Codezeilen werden dann erkannt und zu Blöcken gruppiert).

Prüfungen:
  Python     Syntax mit compile() – es entstehen keine .pyc-Dateien
  C/C++      Syntax mit `g++ -fsyntax-only -Wall` (falls installiert), für Arduino/ESP32 mit
             einem kleinen Stub der Grundfunktionen; unbekannte #include werden übersprungen
             (⚠). Zusätzlich Dezimalkomma-Heuristik (`x = 1,5;`) auch ohne Compiler.
  G-Code     DIN 66025 / PAL: unbekannte Wörter, Komma statt Punkt, Vorschub vor G01–G03,
             I/J/K oder R bei Kreisbögen, Bogenradius Start = Ende, Spindel vor Schnitt,
             Radiuskorrektur G41/G42 mit G40 abgewählt, Programmende M30/M02,
             optional Verfahrbereich gegen das Rohteil (--rohteil).

Aufruf:
    python3 code_pruefen.py DATEI… [--sprache auto|python|cpp|arduino|gcode]
                           [--rohteil "X-50:50,Y-50:50,Z-20:0"] [--ohne-compiler] [--json]

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
Bibliotheksfunktionen (WiFi, BLE, Sensorbibliotheken), Pinbelegungen und Steuerungsdialekte
prüft das Skript nicht – dafür Datenblatt bzw. Herstellerdoku (🔎).
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path

try:  # gemeinsamer Leser für DOCX/ODT/PDF (liegt im selben scripts/-Ordner)
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from text_lesen import lies_text  # type: ignore
except Exception:  # noqa: BLE001
    lies_text = None  # type: ignore

ENDUNG_SPRACHE = {".py": "python", ".c": "cpp", ".cpp": "cpp", ".cc": "cpp", ".h": "cpp",
                  ".hpp": "cpp", ".ino": "arduino", ".nc": "gcode", ".gcode": "gcode",
                  ".cnc": "gcode", ".mpf": "gcode", ".tap": "gcode", ".ngc": "gcode"}
FENCE_SPRACHE = {"python": "python", "py": "python", "c": "cpp", "cpp": "cpp", "c++": "cpp",
                 "arduino": "arduino", "ino": "arduino", "gcode": "gcode", "g-code": "gcode",
                 "nc": "gcode", "cnc": "gcode"}

ARDUINO_STUB = """\
#include <stdint.h>
#include <math.h>
#include <string.h>
#include <string>
typedef bool boolean; typedef uint8_t byte; typedef std::string String;
#define HIGH 1
#define LOW 0
#define INPUT 0
#define OUTPUT 1
#define INPUT_PULLUP 2
#define LED_BUILTIN 2
#define A0 36
#define A1 39
#define A2 34
#define A3 35
#define A4 32
#define A5 33
#define PI 3.14159265358979
struct StubSerial { void begin(long){} void end(){} int available(){return 0;} int read(){return -1;}
  template<class T> void print(T){} template<class T> void print(T,int){}
  template<class T> void println(T){} template<class T> void println(T,int){} void println(){}
  template<class... A> void printf(const char*, A...){} };
static StubSerial Serial, Serial1, Serial2;
inline void pinMode(int,int){} inline void digitalWrite(int,int){} inline int digitalRead(int){return 0;}
inline int analogRead(int){return 0;} inline void analogWrite(int,int){} inline void analogReadResolution(int){}
inline uint32_t analogReadMilliVolts(int){return 0;} inline void delay(unsigned long){}
inline void delayMicroseconds(unsigned int){} inline unsigned long millis(){return 0;}
inline unsigned long micros(){return 0;}
inline long map(long x,long a,long b,long c,long d){return (x-a)*(d-c)/(b-a)+c;}
template<class T,class U,class V> T constrain(T x,U a,V b){return x<a?a:(x>b?b:x);}
inline void tone(int,unsigned int){} inline void noTone(int){} inline long random(long){return 0;}
"""
STUB_ZEILEN = ARDUINO_STUB.count("\n")
STANDARD_HEADER = {"stdio.h", "stdlib.h", "stdint.h", "string.h", "math.h", "iostream", "string",
                   "vector", "cmath", "cstdio", "cstdlib", "cstdint", "array", "map", "algorithm",
                   "Arduino.h"}
ARDUINO_HINWEISE = re.compile(r"\b(void\s+setup\s*\(|void\s+loop\s*\(|Serial\.|analogRead|digitalWrite|pinMode)")

# G-Code: Wörter, die in DIN 66025 bzw. PAL-Fräsen/Drehen üblich sind (Liste bewusst breit).
G_BEKANNT = {0, 1, 2, 3, 4, 9, 10, 17, 18, 19, 20, 21, 22, 23, 28, 33, 40, 41, 42, 43, 44, 45,
             46, 47, 48, 49, 53, 54, 55, 56, 57, 58, 59, 61, 62, 64, 70, 71, 72, 73, 74, 75, 76,
             77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 94, 95, 96, 97, 98, 99}
M_BEKANNT = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 17, 19, 30, 60, 98, 99}
ADRESSEN = set("NGXYZIJKRFSTMHDPQLABCUVWE")


@dataclass
class Befund:
    stelle: str
    sprache: str
    status: str          # ✅ ⚠️ ❌ ℹ️
    text: str


@dataclass
class Block:
    quelle: str
    start: int           # Zeile in der Quelle (1-basiert)
    sprache: str
    code: str


@dataclass
class Ergebnis:
    befunde: list[Befund] = field(default_factory=list)
    bloecke: int = 0
    compiler: str | None = None


# ───────────────────────────── Blöcke finden ─────────────────────────────

def _codezeile(z: str) -> str | None:
    s = z.strip()
    if not s:
        return None
    if re.match(r"^(N\d+\s+)?[GM]\d{1,3}\b", s) or re.match(r"^(%|O\d+)", s):
        return "gcode"
    if re.match(r"^(#include|#define|//|/\*|\*/|\}|\{)", s) or \
            re.search(r"(;\s*(//.*)?$|^\s*(void|int|float|double|const|bool|long|char|unsigned)\b.*[;{(])", s):
        return "cpp"
    return None


def bloecke_finden(pfad: Path, sprache: str = "auto") -> list[Block]:
    endung = pfad.suffix.lower()
    name = pfad.name.encode("utf-8", "surrogateescape").decode("utf-8", "replace")
    if endung in ENDUNG_SPRACHE:
        sp = ENDUNG_SPRACHE[endung] if sprache == "auto" else sprache
        return [Block(name, 1, sp, pfad.read_text(encoding="utf-8", errors="replace"))]
    if endung in (".md", ".markdown", ".txt"):
        text = pfad.read_text(encoding="utf-8", errors="replace")
    elif lies_text is not None and endung in (".docx", ".odt", ".pdf"):
        text = lies_text(pfad)
    else:
        raise ValueError(f"Format nicht unterstützt: {name}")
    bloecke: list[Block] = []
    zeilen = text.splitlines()
    if endung in (".md", ".markdown"):
        i = 0
        while i < len(zeilen):
            m = re.match(r"^\s*```\s*([\w+\-]*)", zeilen[i])
            if m:
                kenn = m.group(1).lower()
                j = i + 1
                while j < len(zeilen) and not zeilen[j].strip().startswith("```"):
                    j += 1
                sp = FENCE_SPRACHE.get(kenn)
                if sprache != "auto":
                    sp = sprache
                if sp:
                    bloecke.append(Block(name, i + 2, sp, "\n".join(zeilen[i + 1:j])))
                i = j + 1
            else:
                i += 1
        return bloecke
    # Fließtext (DOCX/PDF/TXT): Codezeilen gruppieren; Leerzeilen (leere Absätze) unterbrechen
    # einen Block nicht, Fließtext schon.
    akt: list[str] = []
    start, akt_sp = 0, None

    def abschliessen() -> None:
        while akt and not akt[-1].strip():
            akt.pop()
        if sum(1 for z in akt if z.strip()) >= 2:
            bloecke.append(Block(name, start, sprache if sprache != "auto" else akt_sp, "\n".join(akt)))

    for nr, z in enumerate(zeilen + ["ENDE"], 1):
        if not z.strip():
            if akt:
                akt.append("")
            continue
        sp = _codezeile(z)
        if sp and akt_sp in (None, sp):
            if not akt:
                start = nr
            akt.append(z)
            akt_sp = sp
        else:
            abschliessen()
            akt, akt_sp, start = ([z], sp, nr) if sp else ([], None, nr)
    return bloecke


# ───────────────────────────── Python ─────────────────────────────

def pruefe_python(b: Block, erg: Ergebnis) -> None:
    try:
        compile(b.code, b.quelle, "exec", dont_inherit=True)
        erg.befunde.append(Befund(f"{b.quelle}:{b.start}", "python", "✅", "Syntax in Ordnung"))
    except SyntaxError as e:
        zeile = b.start + (e.lineno or 1) - 1
        erg.befunde.append(Befund(f"{b.quelle}:{zeile}", "python", "❌", f"Syntaxfehler: {e.msg}"))


# ───────────────────────────── C/C++/Arduino ─────────────────────────────

KOMMA_RE = re.compile(r"=\s*-?\d+,\d+\s*[;)]")


def pruefe_cpp(b: Block, erg: Ergebnis, ohne_compiler: bool = False) -> None:
    befunde_vorher = len(erg.befunde)
    for i, z in enumerate(b.code.splitlines()):
        if KOMMA_RE.search(z.split("//")[0]):
            erg.befunde.append(Befund(f"{b.quelle}:{b.start + i}", b.sprache, "⚠️",
                                      f"Dezimalkomma? `{z.strip()[:60]}` – in C/C++ ist die Zahl mit Punkt zu schreiben (1.5)"))
    gpp = None if ohne_compiler else shutil.which("g++")
    if not gpp:
        erg.befunde.append(Befund(f"{b.quelle}:{b.start}", b.sprache, "⚠️",
                                  "kein g++ verfügbar – nur heuristisch geprüft; Code in der IDE kompilieren"))
        return
    erg.compiler = "g++"
    arduino = b.sprache == "arduino" or bool(ARDUINO_HINWEISE.search(b.code))
    code_zeilen = []
    for z in b.code.splitlines():
        m = re.match(r"\s*#include\s*[<\"]([^>\"]+)[>\"]", z)
        if m and m.group(1) not in STANDARD_HEADER:
            erg.befunde.append(Befund(f"{b.quelle}:{b.start + len(code_zeilen)}", b.sprache, "⚠️",
                                      f"Bibliothek `{m.group(1)}` nicht geprüft (Funktionen daraus erscheinen als unbekannt)"))
            code_zeilen.append("// " + z)
        elif m and m.group(1) == "Arduino.h":
            code_zeilen.append("// " + z)
        else:
            code_zeilen.append(z)
    vorspann = ARDUINO_STUB if arduino else ""
    with tempfile.TemporaryDirectory() as tmp:
        datei = Path(tmp) / "pruefling.cpp"
        datei.write_text(vorspann + "\n".join(code_zeilen) + "\n", encoding="utf-8")
        aus = subprocess.run([gpp, "-fsyntax-only", "-Wall", "-std=c++17", "-x", "c++", str(datei)],
                             capture_output=True, text=True, errors="replace").stderr
    versatz = STUB_ZEILEN if arduino else 0
    fehler = 0
    for zeile in aus.splitlines():
        m = re.match(r".*?pruefling\.cpp:(\d+):\d+:\s*(error|warning):\s*(.*)", zeile)
        if not m:
            continue
        nr, art, msg = int(m.group(1)) - versatz, m.group(2), m.group(3)
        if nr < 1:
            continue
        stelle = f"{b.quelle}:{b.start + nr - 1}"
        if art == "error":
            unbekannt = "was not declared" in msg or "does not name a type" in msg or "has no member" in msg
            erg.befunde.append(Befund(stelle, b.sprache, "⚠️" if unbekannt else "❌",
                                      ("unbekannter Name (Bibliothek? Tippfehler?): " if unbekannt else "Compilerfehler: ") + msg))
            fehler += 0 if unbekannt else 1
        elif "comma operator" in msg:
            erg.befunde.append(Befund(stelle, b.sprache, "❌",
                                      f"Kommaoperator – vermutlich Dezimalkomma: {msg}"))
            fehler += 1
    if len(erg.befunde) == befunde_vorher:
        erg.befunde.append(Befund(f"{b.quelle}:{b.start}", b.sprache, "✅",
                                  "Syntax in Ordnung (g++" + (", Arduino-Stub" if arduino else "") + ")"))


# ───────────────────────────── G-Code ─────────────────────────────

WORT_RE = re.compile(r"([A-Za-z])\s*([+-]?\d*[.,]?\d+)")
# PAL und andere Dialekte: mehrbuchstabige Adressen (inkrementelle Koordinaten, Zyklusparameter)
PAL_RE = re.compile(r"\b(XI|YI|ZI|XA|YA|ZA|RZ|AS|AR|AP|AL|AK|AI|AN|BS|BE|EP|DR|RN|IA|JA|TC|LP|BP)\s*([+-]?\d*[.,]?\d+)",
                    re.IGNORECASE)
ZYKLUS_DEF = set(range(72, 79)) | set(range(80, 90))   # Zyklusdefinition – keine Bahnbewegung


def _ohne_kommentar(z: str) -> str:
    z = re.sub(r"\([^)]*\)", " ", z)
    return z.split(";")[0]


def pruefe_gcode(b: Block, erg: Ergebnis, rohteil: dict[str, tuple[float, float]] | None = None) -> None:
    pos: dict[str, float | None] = {"X": None, "Y": None, "Z": None}
    absolut, modus = True, None
    f_gesetzt = spindel = False
    korrektur_aktiv: str | None = None
    korrektur_neu = False
    eilgang_unten: list[int] = []
    ende = False
    bewegungen = 0
    weg = 0.0
    box = {a: [math.inf, -math.inf] for a in "XYZ"}
    zeilen = b.code.splitlines()
    vorher = len(erg.befunde)
    kommentar_gemeldet = False
    # Ausschnitt (≤ 3 Programmzeilen, z. B. Beispiel im Infotext): Vorschub, Spindel und
    # Programmende nur als Hinweis
    ausschnitt = len([z for z in zeilen if _ohne_kommentar(z).strip()]) <= 3
    streng = "ℹ️" if ausschnitt else "❌"

    def melde(i: int, status: str, text: str) -> None:
        erg.befunde.append(Befund(f"{b.quelle}:{b.start + i}", "gcode", status, text))

    for i, roh in enumerate(zeilen):
        z = _ohne_kommentar(roh).strip()
        if not z or z.startswith("%") or re.match(r"^O\d+", z):
            continue
        pal = {a.upper(): float(v.replace(",", ".")) for a, v in PAL_RE.findall(z)}
        z = PAL_RE.sub(" ", z)
        rest = WORT_RE.sub(" ", z).strip()
        if rest and re.search(r"[A-Za-zÄÖÜäöüß]{4,}", rest):
            if not kommentar_gemeldet:
                melde(i, "ℹ️", "Text in Programmzeilen als Erläuterung gewertet – im Programm als Kommentar in ( ) setzen")
                kommentar_gemeldet = True
            z = z[:len(z) - len(z.lstrip())] + " ".join(w for w in z.split() if WORT_RE.fullmatch(w))
        elif rest:
            melde(i, "⚠️", f"unerwartete Zeichen `{rest[:20]}` (z. B. Komma zwischen Wörtern)")
        woerter = WORT_RE.findall(z)
        werte: dict[str, float] = {}
        gs, ms = [], []
        for adr, zahl in woerter:
            adr = adr.upper()
            if "," in zahl:
                melde(i, "❌", f"Komma in `{adr}{zahl}` – Dezimaltrennzeichen ist der Punkt")
                zahl = zahl.replace(",", ".")
            if adr not in ADRESSEN:
                melde(i, "⚠️", f"unbekannte Adresse `{adr}`")
                continue
            v = float(zahl)
            if adr == "G":
                gs.append(int(v))
            elif adr == "M":
                ms.append(int(v))
            else:
                werte[adr] = v
        for g in gs:
            if g not in G_BEKANNT:
                melde(i, "⚠️", f"G{g} ist in DIN 66025/PAL nicht üblich – Steuerungsdialekt prüfen")
            if g in (0, 1, 2, 3):
                modus = g
            elif g == 90:
                absolut = True
            elif g == 91:
                absolut = False
            elif g in (41, 42):
                korrektur_aktiv = f"G{g}"
                korrektur_neu = True
            elif g == 40:
                korrektur_aktiv = None
        for m in ms:
            if m not in M_BEKANNT:
                melde(i, "⚠️", f"M{m} unbekannt – Steuerungsdialekt prüfen")
            if m in (3, 4, 13, 14):
                spindel = True
            elif m in (5,):
                spindel = False
            elif m in (2, 30):
                ende = True
        if "F" in werte:
            f_gesetzt = True
        if any(g in ZYKLUS_DEF for g in gs):
            continue                     # Zyklusdefinition (PAL G72–G78, Bohrzyklen G80–G89)
        koord = {a: werte[a] for a in "XYZ" if a in werte}
        inkrementell = {a[0]: v for a, v in pal.items() if a in ("XI", "YI", "ZI")}
        if 79 in gs:                     # Zyklusaufruf an einem Punkt: Werkzeug fährt dorthin
            if not spindel:
                melde(i, streng, "Zyklusaufruf, bevor die Spindel läuft (M03/M04 fehlt)")
            for a, v in koord.items():
                pos[a] = v
            continue
        if not (koord or inkrementell) or modus is None or any(g in (4, 9, 53, 54, 55, 56, 57, 58, 59, 70, 71) for g in gs):
            continue
        if korrektur_neu and modus in (1, 2, 3) and not ({"X", "Y"} & koord.keys() or {"X", "Y"} & inkrementell.keys()):
            melde(i, "⚠️", f"Radiuskorrektur {korrektur_aktiv} ohne Anfahrbewegung in der Ebene (X/Y) – Korrektur wird erst beim nächsten X/Y-Weg aufgebaut")
        if korrektur_aktiv and modus == 0 and ({"X", "Y"} & koord.keys()):
            melde(i, "⚠️", f"Eilgang in der Ebene bei aktiver Radiuskorrektur {korrektur_aktiv} – vorher G40")
        if modus in (1, 2, 3) or ({"X", "Y"} & koord.keys()):
            korrektur_neu = False
        ziel = dict(pos)
        for a, v in koord.items():
            ziel[a] = v if absolut or pos[a] is None else (pos[a] or 0) + v
        for a, v in inkrementell.items():
            ziel[a] = (pos[a] or 0) + v
        if modus in (1, 2, 3):
            bewegungen += 1
            if not f_gesetzt:
                melde(i, streng, f"G0{modus} ohne Vorschub – F vorher oder in dieser Zeile angeben")
            if not spindel:
                melde(i, streng, "Schnittbewegung, bevor die Spindel läuft (M03/M04 fehlt)")
        if modus in (2, 3):
            if not ({"I", "J", "K"} & werte.keys() or "R" in werte):
                melde(i, "❌", f"G0{modus} ohne Kreismittelpunkt (I/J/K) oder Radius (R)")
            elif {"I", "J"} & werte.keys() and pos["X"] is not None and pos["Y"] is not None:
                cx, cy = pos["X"] + werte.get("I", 0.0), pos["Y"] + werte.get("J", 0.0)
                r1 = math.hypot(pos["X"] - cx, pos["Y"] - cy)
                r2 = math.hypot((ziel["X"] or 0) - cx, (ziel["Y"] or 0) - cy)
                if abs(r1 - r2) > 0.01:
                    melde(i, "❌", f"Kreisbogen ungültig: Radius am Start {r1:.3f} mm, am Ende {r2:.3f} mm")
                elif r1 > 0:
                    a1 = math.atan2(pos["Y"] - cy, pos["X"] - cx)
                    a2 = math.atan2((ziel["Y"] or 0) - cy, (ziel["X"] or 0) - cx)
                    d = (a1 - a2) if modus == 2 else (a2 - a1)
                    d = d % (2 * math.pi) or 2 * math.pi
                    weg += r1 * d
        elif modus == 1 and None not in pos.values():
            weg += math.dist([pos[a] for a in "XYZ"], [ziel[a] for a in "XYZ"])  # type: ignore[misc]
        if rohteil and modus == 0 and ziel["Z"] is not None and ziel["Z"] < rohteil.get("Z", (0, 0))[1] \
                and (("X" in koord) or ("Y" in koord)):
            eilgang_unten.append(b.start + i)
        for a in "XYZ":
            if ziel[a] is not None:
                box[a][0] = min(box[a][0], ziel[a])  # type: ignore[arg-type]
                box[a][1] = max(box[a][1], ziel[a])  # type: ignore[arg-type]
                if rohteil and a in rohteil and modus in (1, 2, 3):
                    lo, hi = rohteil[a]
                    if not (lo - 20 <= ziel[a] <= hi + 20):  # type: ignore[operator]
                        melde(i, "⚠️", f"{a}{ziel[a]:g} weit außerhalb des Rohteils ({lo:g} … {hi:g})")
        pos = ziel
    if korrektur_aktiv and not ausschnitt:
        melde(len(zeilen) - 1, "⚠️", f"Radiuskorrektur {korrektur_aktiv} bis Programmende nicht mit G40 abgewählt")
    if not ende:
        if ausschnitt:
            melde(0, "ℹ️", "Ausschnitt (≤ 3 Zeilen) – Programmende nicht geprüft")
        elif bewegungen:
            melde(len(zeilen) - 1, "❌", "Programmende M30 (oder M02) fehlt")
    if eilgang_unten:
        melde(0, "ℹ️", "Eilgang unterhalb der Rohteiloberfläche in Zeile(n) "
              + ", ".join(map(str, eilgang_unten[:8])) + (" …" if len(eilgang_unten) > 8 else "")
              + " – zulässig, wenn dort schon zerspant ist; in der Simulation prüfen")
    if not [x for x in erg.befunde[vorher:] if x.status in ("❌", "⚠️")]:
        melde(0, "✅", "keine Auffälligkeiten")
    if bewegungen:
        bb = ", ".join(f"{a} {box[a][0]:g} … {box[a][1]:g}" for a in "XYZ" if box[a][0] != math.inf)
        melde(0, "ℹ️", f"{bewegungen} Bahnbewegungen, Weg ≈ {weg:.1f} mm, Bereich {bb}")


# ───────────────────────────── Steuerung ─────────────────────────────

def _rohteil(text: str | None) -> dict[str, tuple[float, float]] | None:
    if not text:
        return None
    ergebnis = {}
    for teil in text.split(","):
        m = re.match(r"\s*([XYZ])\s*(-?[\d.]+)\s*:\s*(-?[\d.]+)", teil, re.I)
        if not m:
            raise ValueError(f"Rohteil unklar: {teil!r} (Form X-50:50,Y-50:50,Z-20:0)")
        ergebnis[m.group(1).upper()] = (float(m.group(2)), float(m.group(3)))
    return ergebnis


def pruefe_dateien(pfade: list[Path], sprache: str = "auto", rohteil: str | None = None,
                   ohne_compiler: bool = False) -> Ergebnis:
    erg = Ergebnis()
    rt = _rohteil(rohteil)
    for p in pfade:
        for b in bloecke_finden(p, sprache):
            erg.bloecke += 1
            if b.sprache == "python":
                pruefe_python(b, erg)
            elif b.sprache in ("cpp", "arduino"):
                pruefe_cpp(b, erg, ohne_compiler)
            elif b.sprache == "gcode":
                pruefe_gcode(b, erg, rt)
    return erg


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Programmcode in Unterrichtsmaterial prüfen.")
    ap.add_argument("dateien", nargs="+", type=Path)
    ap.add_argument("--sprache", default="auto", choices=["auto", "python", "cpp", "arduino", "gcode"])
    ap.add_argument("--rohteil", help='Verfahrbereich, z. B. "X-52.5:52.5,Y-52.5:52.5,Z-40:0"')
    ap.add_argument("--ohne-compiler", action="store_true", help="g++ nicht verwenden (nur Heuristik)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    try:
        for p in a.dateien:
            if not p.is_file():
                raise ValueError(f"nicht gefunden: {p}")
        erg = pruefe_dateien(a.dateien, a.sprache, a.rohteil, a.ohne_compiler)
    except (ValueError, OSError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({"bloecke": erg.bloecke, "compiler": erg.compiler,
                          "befunde": [asdict(x) for x in erg.befunde]}, ensure_ascii=False, indent=2))
    else:
        if not erg.bloecke:
            print("Kein Code gefunden (Codeblöcke in Markdown mit Sprachkennung ```cpp, ```python, ```gcode).")
        else:
            print("| Stelle | Sprache | Status | Befund |\n|---|---|---|---|")
            for x in erg.befunde:
                print(f"| {x.stelle} | {x.sprache} | {x.status} | {x.text} |")
            n = {s: sum(1 for x in erg.befunde if x.status == s) for s in ("❌", "⚠️", "✅")}
            cpp = any(x.sprache in ("cpp", "arduino") for x in erg.befunde)
            print(f"\nCodeblöcke: {erg.bloecke} · ❌ {n['❌']} · ⚠️ {n['⚠️']} · ✅ {n['✅']}"
                  + (" · C/C++ ohne Compiler (heuristisch)" if cpp and not erg.compiler else ""))
            print("\n_Syntax und Plausibilität – ersetzt keinen Test auf der Zielhardware bzw. "
                  "keine Simulation an der Steuerung._")
    return 1 if any(x.status == "❌" for x in erg.befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
