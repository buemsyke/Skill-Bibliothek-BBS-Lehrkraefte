"""
grafcet — GRAFCET nach DIN EN 60848 als Bauteil des Technologieschemas.

Die Spec beschreibt die **Struktur** (``typ: grafcet`` mit einer ``kette`` aus Schritten, Transitionen,
Verzweigungen und Sprüngen); dieses Modul berechnet daraus die Lage und zeichnet die Normsymbole:

* Schritte: normal, Initialschritt (doppelt), Makroschritt, einschließender Schritt, Aktivierung ``*``
* Transitionen: Bedingung rechts, Name links in Klammern, Quell- und Schlusstransition, immer erfüllt
  (``1`` unterstrichen), Negation als **Überstrich** (getippt ``¬-S2``)
* kontinuierliche Aktionen: einfach, mit Zuweisungsbedingung, verzögert, zeitbegrenzt
* speichernde Aktionen: immer mit **Zuweisung** (``-Q1 := 1``) und **Pfeil am Rechteck** (bei Aktivierung,
  bei Deaktivierung, Fähnchen bei Ereignis) – beides erzwingt die Prüfung
* Zwangssteuerung (Doppelrahmen, ``G5 {INIT}``), Alternativ- und Parallelverzweigung, Rücksprung,
  Rahmen eines einschließenden Schritts bzw. Teil-GRAFCET

``aufloesen`` setzt jede ``typ: grafcet`` in die Einzelteile ``grafcet_schritt``, ``grafcet_transition``,
``grafcet_balken``, ``grafcet_rahmen`` und ``linie`` um. Damit bleibt jede Form im draw.io-Export einzeln
verschiebbar und die Verbinder hängen an ihr. Die Einzelteile lassen sich auch direkt mit Koordinaten
verwenden (Symboltafel, nachgestellte Abbildung).

``netz`` liest aus der Kette das Schaltnetz (welche Transition führt von wo nach wo); daraus entstehen die
Textform (Notationsblatt) und die Erreichbarkeitsprüfung.

Nur Python-Standardbibliothek.
"""

from __future__ import annotations

import itertools
import math
import re
import textwrap
from dataclasses import dataclass, field

from . import kennzeichen as kz
from .teile import AUFZAEHLUNGEN, SCHEMA, WAHRHEITEN, ZAHLEN, ZEICHNER, Teilinfo

# ───────────────────────────── Maße ─────────────────────────────

S = 40.0              # Schritt (Quadrat)
STUMMEL = 30.0        # Schritt bis zur ersten Aktion
AKTION_H = 30.0
AKTION_B_MIN = 50.0
BALKEN = 28.0         # Breite der Transition
FAHNE = 16.0          # Pfeil am Rechteck der speichernden Aktion
STIEL_OBEN = 18.0     # Strich der Zuweisungsbedingung bzw. des Ereignisses
STIEL_X = 14.0        # Lage dieses Strichs, gemessen von der linken Kante der Aktion
ABSTAND_T = 25.0      # Transition bis zum Nachbarn (Schritt, Balken)
ABSTAND_B = 14.0      # Verzweigungsbalken bis zum Nachbarn
ABSTAND_Z = 34.0      # Verzweigungsäste (rechte Ausdehnung bis linke Ausdehnung des nächsten)
BAHN = 16.0           # Abstand der Rücksprungbahnen
BAHN_LUFT = 12.0      # Abstand der innersten Bahn von der Folge
EINMUENDUNG = 12.0    # Rücksprung mündet so weit über dem Zielschritt
RAHMEN_LUFT = 28.0
UMBRUCH = 42          # Zeichen je Kommentarzeile

SCHRIFT = 12.0
SCHRIFT_SCHRITT = 13.0
SCHRIFT_KLEIN = 10.5
SCHRIFT_KOMMENTAR = 11.0
ZEICHENBREITE = 0.6   # etwas großzügiger als die Prüfung: Kennzeichen bestehen fast nur aus Großbuchstaben

SCHRITTARTEN = ("normal", "initial", "makro", "einschliessend")
TRANSITIONSARTEN = ("normal", "quelle", "schluss")
AKTIONSARTEN = ("kontinuierlich", "bedingt", "verzoegert", "zeitbegrenzt", "aktivierung", "deaktivierung",
                "ereignis", "zwang")
SPEICHERND = ("aktivierung", "deaktivierung", "ereignis")
MIT_BEDINGUNG = ("bedingt", "verzoegert", "zeitbegrenzt", "ereignis")

ZWANG = re.compile(r"^G\S*\s*\{.*\}$")
ZEIT_IN_BEDINGUNG = re.compile(r"\d+(?:,\d+)?(?:ms|s|min|h)/\S")
SCHRITTVARIABLE = re.compile(r"/X([\w.]+)")
KENNZEICHEN = re.compile(r"(?<![\w-])-[A-Za-z]{1,3}\d+\b")
OHNE_BINDESTRICH = re.compile(r"(?<![\w\-/])(?!X\d)(?!G\d)[A-Z]{1,3}\d+\b")
NEGATION = re.compile(r"¬(\([^()]*\)|\[[^\]]*\]|[^\s·+()\[\]]+)")
ZUWEISUNG = re.compile(r"^(.*?)\s*:=\s*(.*)$")


# ───────────────────────────── Texte ─────────────────────────────

def bedingung_normal(roh) -> str:
    """Bedingung in die Schreibweise des Notationsblatts bringen (``*`` → ``·``, ``!`` → ``¬``, ``5s/X3``)."""
    s = str(roh).strip().replace("̲", "")            # „1̲“ aus fremden Vorlagen
    s = re.sub(r"!(?!=)", "¬", s)
    s = re.sub(r"\s*[*·]\s*", " · ", s)
    s = re.sub(r"(\d+)\.(\d+)(?=\s*(?:ms|s|min|h)\b)", r"\1,\2", s)
    s = re.sub(r"(\d+(?:,\d+)?)\s*(ms|s|min|h)\s*/\s*", r"\1\2/", s)
    return s


def darstellung(bedingung: str) -> tuple[str, list[tuple[str, str | None]] | None]:
    """(Klartext, Abschnitte mit Überstrich/Unterstrich) einer normalisierten Bedingung."""
    if bedingung == "1":
        return "1", [("1", "underline")]
    if "¬" not in bedingung:
        return bedingung, None
    teile: list[tuple[str, str | None]] = []
    pos = 0
    for m in NEGATION.finditer(bedingung):
        if m.start() > pos:
            teile.append((bedingung[pos:m.start()], None))
        inhalt = m.group(1)
        if inhalt.startswith("(") and inhalt.endswith(")"):
            inhalt = inhalt[1:-1]                         # der Überstrich fasst selbst zusammen
        teile.append((inhalt, "overline"))
        pos = m.end()
    if pos < len(bedingung):
        teile.append((bedingung[pos:], None))
    return "".join(t for t, _ in teile), teile


def _w(text: str, groesse: float) -> float:
    return max((len(z) for z in str(text).split("\n")), default=0) * groesse * ZEICHENBREITE


def kommentar_zeilen(roh) -> str:
    """Kommentar in Anführungszeichen (DIN EN 60848), bei Bedarf umgebrochen."""
    s = str(roh).strip().strip("„“”\"").strip()
    zeilen: list[str] = []
    for absatz in s.split("\n"):
        zeilen += textwrap.wrap(absatz, UMBRUCH) or [""]
    return "„" + "\n".join(zeilen) + "“"


# ───────────────────────────── Struktur ─────────────────────────────

@dataclass
class Aktion:
    art: str
    text: str
    bedingung: str | None = None
    kommentar: str | None = None
    b: float | None = None

    @property
    def variable(self) -> str:
        m = ZUWEISUNG.match(self.text)
        return (m.group(1) if m else self.text).strip()

    @property
    def textform(self) -> str:
        if self.art == "aktivierung":
            return f"↑ {self.text}"
        if self.art == "deaktivierung":
            return f"↓ {self.text}"
        if self.art == "ereignis":
            return f"{self.text} bei {self.bedingung}"
        if self.art == "bedingt":
            return f"{self.text} wenn {self.bedingung}"
        if self.art == "verzoegert":
            return f"{self.text} verzögert {self.bedingung}"
        if self.art == "zeitbegrenzt":
            return f"{self.text} begrenzt {self.bedingung}"
        return self.text

    @property
    def oben(self) -> float:
        if self.art == "aktivierung":
            return FAHNE
        return STIEL_OBEN if self.art in MIT_BEDINGUNG else 0.0

    @property
    def unten(self) -> float:
        return FAHNE if self.art == "deaktivierung" else 0.0

    @property
    def breite(self) -> float:
        """Breite des Rechtecks; die Bedingung darf rechts darüber hinausragen (siehe ``breite_mit_bedingung``)."""
        if self.b:
            return float(self.b)
        return max(AKTION_B_MIN, _w(self.text, SCHRIFT) + (22 if self.art == "zwang" else 16))

    @property
    def breite_mit_bedingung(self) -> float:
        """Mindestbreite, wenn rechts daneben noch eine Aktion steht."""
        if self.art in MIT_BEDINGUNG:
            return max(self.breite, STIEL_X + 4 + _w(self.bedingung_zeichen, SCHRIFT_KLEIN) + 6)
        return self.breite

    @property
    def bedingung_zeichen(self) -> str:
        """Text am Strich; zeitbegrenzt heißt: Zeitbedingung negiert."""
        b = self.bedingung or ""
        return f"¬{b}" if self.art == "zeitbegrenzt" and not b.startswith("¬") else b


@dataclass
class Schritt:
    name: str
    art: str = "normal"
    aktivierung: bool = False
    zeilen: list[list[Aktion]] = field(default_factory=list)
    kommentar: str | None = None
    bezeichnung: str | None = None      # nur Textform: „1 Fördern“

    @property
    def lagen(self) -> list[float]:
        """Oberkante jeder Aktionszeile, gemessen von der Schrittmitte."""
        y = -AKTION_H / 2
        lagen = []
        for i, zeile in enumerate(self.zeilen):
            if i:
                luecke = max(max(a.unten for a in self.zeilen[i - 1]), max(a.oben for a in zeile))
                y += AKTION_H + (luecke + 4 if luecke else 0)
            lagen.append(y)
        return lagen

    @property
    def oben_bedarf(self) -> float:
        if not self.zeilen:
            return 0.0
        return max(0.0, max(a.oben for a in self.zeilen[0]) + AKTION_H / 2 - S / 2)

    @property
    def unten_bedarf(self) -> float:
        if not self.zeilen:
            return 0.0
        unterkante = self.lagen[-1] + AKTION_H + max(a.unten for a in self.zeilen[-1])
        return max(0.0, unterkante - S / 2)

    @property
    def aktionen(self) -> list[Aktion]:
        return [a for z in self.zeilen for a in z]

    @property
    def spalten(self) -> list[float]:
        """Breite je Spalte: übereinanderliegende Aktionen bilden ein Raster."""
        anzahl = max((len(z) for z in self.zeilen), default=0)
        return [max((z[i].breite if i == len(z) - 1 else z[i].breite_mit_bedingung) for z in self.zeilen if len(z) > i)
                for i in range(anzahl)]

    @property
    def aktionsbreite(self) -> float:
        return sum(self.spalten)


@dataclass
class Transition:
    bedingung: str
    art: str = "normal"
    name: str | None = None
    kommentar: str | None = None

    @property
    def klartext(self) -> str:
        return darstellung(self.bedingung)[0]


@dataclass
class Verzweigung:
    art: str              # alternativ | parallel
    zweige: list[list]


@dataclass
class Sprung:
    ziel: str


@dataclass
class Uebergang:
    von: list[str]
    bedingung: str
    nach: list[str] = field(default_factory=list)


# ───────────────────────────── Spec lesen und prüfen ─────────────────────────────

Meldung = tuple[str, str]    # (Stufe, Text)


def _vorschlag(k, erlaubt) -> str:
    import difflib
    t = difflib.get_close_matches(str(k), list(erlaubt), n=1, cutoff=0.6)
    return f" – meinten Sie '{t[0]}'?" if t else ""


def _unbekannte(roh: dict, erlaubt: set, wo: str, m: list[Meldung]) -> None:
    for k in roh:
        if k not in erlaubt:
            m.append(("❌", f"{wo}: unbekannter Schlüssel '{k}'{_vorschlag(k, erlaubt)}"))


def lies_aktion(roh, wo: str, m: list[Meldung]) -> Aktion | None:
    if isinstance(roh, (str, int, float)):
        roh = {"text": str(roh)}
    if not isinstance(roh, dict):
        m.append(("❌", f"{wo}: Aktion ist weder Text noch Mapping"))
        return None
    _unbekannte(roh, {"text", "art", "bedingung", "kommentar", "b"}, wo, m)
    text = str(roh.get("text", "")).strip()
    if not text:
        m.append(("❌", f"{wo}: Aktion ohne 'text'"))
        return None
    art = roh.get("art")
    if art is not None and art not in AKTIONSARTEN:
        m.append(("❌", f"{wo}: 'art: {art}' ist ungültig – erlaubt: {', '.join(AKTIONSARTEN)}"))
        return None
    pfeil = re.match(r"^([↑↓])\s*(.*)$", text)
    if pfeil:
        pfeil_art = {"↑": "aktivierung", "↓": "deaktivierung"}[pfeil.group(1)]
        if art not in (None, pfeil_art):
            m.append(("❌", f"{wo}: '{text}' passt nicht zu 'art: {art}'"))
        art, text = pfeil_art, pfeil.group(2).strip()
    if art is None:
        if ZWANG.match(text):
            art = "zwang"
        elif roh.get("bedingung") is not None:
            art = "bedingt"
        else:
            art = "kontinuierlich"
    text = re.sub(r"\s*:=\s*", " := ", text)
    bedingung = bedingung_normal(roh["bedingung"]) if roh.get("bedingung") is not None else None

    if art in SPEICHERND and ":=" not in text:
        m.append(("❌", f"{wo}: speichernde Aktion '{text}' ohne Zuweisung – im Rechteck steht die Zuweisung, "
                        f"z. B. '{text} := 1' oder '{text} := 0', nicht nur die Variable"))
    if ":=" in text and art not in SPEICHERND:
        m.append(("❌", f"{wo}: '{text}' ist eine speichernde Aktion und braucht ihren Auslöser – "
                        f"'↑ {text}' (bei Aktivierung), '↓ {text}' (bei Deaktivierung) oder 'art: ereignis' mit 'bedingung'"))
    if art == "zwang" and not ZWANG.match(text):
        m.append(("❌", f"{wo}: Zwangssteuerung in der Form 'G5 {{INIT}}', 'G5 {{ }}', 'G5 {{3,4,8}}' oder 'G5 {{*}}', nicht '{text}'"))
    if art in MIT_BEDINGUNG and not bedingung:
        m.append(("❌", f"{wo}: 'art: {art}' braucht eine 'bedingung'"))
    if art not in MIT_BEDINGUNG and bedingung:
        m.append(("❌", f"{wo}: 'bedingung' gibt es nicht bei 'art: {art}' (erlaubt: {', '.join(MIT_BEDINGUNG)})"))
    if art in ("verzoegert", "zeitbegrenzt") and bedingung and not ZEIT_IN_BEDINGUNG.search(bedingung):
        m.append(("❌", f"{wo}: 'art: {art}' braucht eine Zeitbedingung der Form '5s/X3', nicht '{bedingung}'"))
    if art == "ereignis" and bedingung and not re.search(r"[↑↓]", bedingung):
        m.append(("⚠", f"{wo}: Ereignis '{bedingung}' ohne Flanke – ein Ereignis schreibt sich '↑-B1' oder '↓-B1'"))
    return Aktion(art, text, bedingung, roh.get("kommentar"), roh.get("b"))


def lies_aktionen(roh, wo: str, m: list[Meldung]) -> list[list[Aktion]]:
    """Flache Liste = eine Zeile nebeneinander; enthält sie Listen, ist jeder Eintrag eine eigene Zeile."""
    if roh in (None, []):
        return []
    if not isinstance(roh, list):
        roh = [roh]
    zeilen_roh = [z if isinstance(z, list) else [z] for z in roh] if any(isinstance(z, list) for z in roh) else [roh]
    zeilen: list[list[Aktion]] = []
    for i, z in enumerate(zeilen_roh):
        aktionen = [lies_aktion(a, f"{wo}, Aktion {a if isinstance(a, str) else i + 1}", m) for a in z]
        aktionen = [a for a in aktionen if a]
        if sum(1 for a in aktionen if a.kommentar) > 1:
            m.append(("❌", f"{wo}: je Aktionszeile höchstens ein Kommentar"))
        if aktionen:
            zeilen.append(aktionen)
    return zeilen


def lies_folge(roh, wo: str, m: list[Meldung]) -> list:
    if not isinstance(roh, list) or not roh:
        m.append(("❌", f"{wo}: braucht eine nicht leere Liste"))
        return []
    folge = []
    for i, it in enumerate(roh):
        ort = f"{wo}[{i + 1}]"
        if not isinstance(it, dict):
            m.append(("❌", f"{ort}: Eintrag ist kein Mapping"))
            continue
        arten = [k for k in ("schritt", "transition", "alternativ", "parallel", "sprung") if k in it]
        if len(arten) != 1:
            m.append(("❌", f"{ort}: genau einer von schritt, transition, alternativ, parallel, sprung"
                            + (f" (gefunden: {', '.join(arten)})" if arten else f"{_vorschlag(next(iter(it), ''), ['schritt', 'transition', 'alternativ', 'parallel', 'sprung'])}")))
            continue
        art = arten[0]
        if art == "schritt":
            name = str(it["schritt"])
            ort = f"Schritt {name}"
            _unbekannte(it, {"schritt", "art", "aktivierung", "aktionen", "kommentar", "bezeichnung"}, ort, m)
            sa = it.get("art", "normal")
            if sa not in SCHRITTARTEN:
                m.append(("❌", f"{ort}: 'art: {sa}' ist ungültig – erlaubt: {', '.join(SCHRITTARTEN)}"))
                sa = "normal"
            zeilen = lies_aktionen(it.get("aktionen"), ort, m)
            folge.append(Schritt(name, sa, bool(it.get("aktivierung")), zeilen, it.get("kommentar"), it.get("bezeichnung")))
        elif art == "transition":
            bed = bedingung_normal(it["transition"])
            ort = f"Transition '{bed}'"
            _unbekannte(it, {"transition", "art", "name", "kommentar"}, ort, m)
            ta = it.get("art", "normal")
            if ta not in TRANSITIONSARTEN:
                m.append(("❌", f"{ort}: 'art: {ta}' ist ungültig – erlaubt: {', '.join(TRANSITIONSARTEN)}"))
                ta = "normal"
            if not bed and not it.get("name"):
                m.append(("❌", f"{wo}[{i + 1}]: Transition ohne Bedingung"))
            folge.append(Transition(bed, ta, it.get("name"), it.get("kommentar")))
        elif art == "sprung":
            _unbekannte(it, {"sprung"}, ort, m)
            folge.append(Sprung(str(it["sprung"])))
        else:
            _unbekannte(it, {art}, ort, m)
            zweige_roh = it[art]
            if not isinstance(zweige_roh, list) or len(zweige_roh) < 2:
                m.append(("❌", f"{ort}: '{art}' braucht mindestens zwei Äste (Liste von Listen)"))
                continue
            folge.append(Verzweigung(art, [lies_folge(z, f"{ort} Ast {j + 1}", m) for j, z in enumerate(zweige_roh)]))
    return folge


def _name(it) -> str:
    if it is None:
        return "dem Verzweigungsbeginn"
    if isinstance(it, Schritt):
        return f"Schritt {it.name}"
    if isinstance(it, Transition):
        return f"Transition '{it.bedingung}'"
    if isinstance(it, Sprung):
        return f"Sprung zu {it.ziel}"
    return f"{it.art}e Verzweigung"


def _abfolge(folge: list, davor: str | None, wo: str, m: list[Meldung], kette_ende: bool = False) -> str | None:
    """Schritt und Transition wechseln sich ab. Gibt zurück, was am Ende der Folge steht."""
    letztes = davor
    vorher = None
    fehl = lambda t: m.append(("❌", t))  # noqa: E731
    for i, it in enumerate(folge):
        wer = _name(it)
        if letztes == "ende":
            fehl(f"{wer}: nach '{_name(vorher)}' geht es nicht weiter – die Folge ist dort zu Ende")
        if isinstance(it, Schritt):
            if letztes == "schritt":
                fehl(f"{wer} folgt auf {_name(vorher)} – dazwischen fehlt die Transition (DIN EN 60848: Schritt und "
                     f"Transition wechseln sich ab)")
            letztes = "schritt"
        elif isinstance(it, Transition):
            if letztes == "transition":
                fehl(f"{wer} folgt auf {_name(vorher)} – dazwischen fehlt ein Schritt (DIN EN 60848: Schritt und "
                     f"Transition wechseln sich ab)")
            if it.art == "quelle" and (letztes is not None or i):
                fehl(f"{wer}: Quelltransition steht nur am Anfang einer Folge")
            if it.art != "quelle" and letztes is None:
                fehl(f"{wer}: vor der ersten Transition steht ein Schritt (oder 'art: quelle')")
            letztes = "ende" if it.art == "schluss" else "transition"
        elif isinstance(it, Sprung):
            if letztes != "transition":
                fehl(f"{wer}: Vor einem Sprung steht eine Transition")
            letztes = "ende"
        else:
            offen = 0
            for j, ast in enumerate(it.zweige):
                ast_wo = f"{wer}, Ast {j + 1}"
                if not ast:
                    continue
                if it.art == "alternativ":
                    if letztes != "schritt":
                        fehl(f"{wer}: Eine Alternativverzweigung beginnt unter einem Schritt")
                    if not isinstance(ast[0], Transition):
                        fehl(f"{ast_wo}: beginnt mit einer Transition (die Bedingung des Asts)")
                    ende = _abfolge(ast, "schritt", ast_wo, m)
                    if ende == "transition":
                        offen += 1
                    elif ende == "schritt":
                        fehl(f"{ast_wo}: endet mit einem Schritt – die Alternative wird nach einer Transition "
                             f"zusammengeführt (oder der Ast endet mit 'sprung')")
                else:
                    if letztes != "transition":
                        fehl(f"{wer}: Eine Parallelverzweigung beginnt unter der gemeinsamen Transition")
                    if not isinstance(ast[0], Schritt):
                        fehl(f"{ast_wo}: beginnt mit einem Schritt")
                    ende = _abfolge(ast, "transition", ast_wo, m)
                    if ende == "schritt":
                        offen += 1
                    elif ende == "transition":
                        fehl(f"{ast_wo}: endet mit einer Transition – die Parallelverzweigung wird unter Schritten "
                             f"zusammengeführt, die gemeinsame Transition folgt danach")
            if it.art == "alternativ":
                letztes = "transition" if offen else "ende"
            else:
                letztes = "schritt" if offen else "ende"
        vorher = it
    if kette_ende and letztes == "transition":
        fehl(f"{_name(vorher)}: Transition ohne Folgeschritt – mit 'sprung' abschließen, einen Schritt anhängen "
             f"oder 'art: schluss' setzen")
    return letztes


def _alle(folge: list):
    for it in folge:
        yield it
        if isinstance(it, Verzweigung):
            for z in it.zweige:
                yield from _alle(z)


# ── Bedingungen auswerten (nur reine Logik) ─────────────────────────

def _wahrheit(ausdruck: str):
    """Boolesche Funktion und Variablen einer Bedingung; None, wenn sie mehr als Logik enthält."""
    if re.search(r"[\[\]↑↓/]", ausdruck):
        return None
    tokens = re.findall(r"[()+·¬]|[^\s()+·¬]+", ausdruck)
    pos = 0
    namen: list[str] = []

    def oder():
        nonlocal pos
        fs = [und()]
        while pos < len(tokens) and tokens[pos] == "+":
            pos += 1
            fs.append(und())
        return lambda w: any(g(w) for g in fs)

    def und():
        nonlocal pos
        fs = [nicht()]
        while pos < len(tokens) and tokens[pos] == "·":
            pos += 1
            fs.append(nicht())
        return lambda w: all(g(w) for g in fs)

    def nicht():
        nonlocal pos
        if pos >= len(tokens):
            raise ValueError
        t = tokens[pos]
        pos += 1
        if t == "¬":
            g = nicht()
            return lambda w: not g(w)
        if t == "(":
            g = oder()
            if pos >= len(tokens) or tokens[pos] != ")":
                raise ValueError
            pos += 1
            return g
        if t in "+·)":
            raise ValueError
        if t == "1":
            return lambda w: True
        if t not in namen:
            namen.append(t)
        return lambda w: w[t]

    try:
        f = oder()
    except ValueError:
        return None
    return (f, namen) if pos == len(tokens) else None


def _schliessen_aus(bedingungen: list[str]) -> str | None:
    """Beispielbelegung, bei der zwei Bedingungen zugleich erfüllt sind; None, wenn keine (oder nicht prüfbar)."""
    fs = [_wahrheit(b) for b in bedingungen]
    if not all(fs):
        return None
    namen = sorted({n for _, ns in fs for n in ns})
    if len(namen) > 12:
        return None
    for werte in itertools.product((False, True), repeat=len(namen)):
        w = dict(zip(namen, werte))
        erfuellt = [b for b, (f, _) in zip(bedingungen, fs) if f(w)]
        if len(erfuellt) > 1:
            belegung = ", ".join(f"{n}={int(v)}" for n, v in w.items())
            return f"'{erfuellt[0]}' und '{erfuellt[1]}' (z. B. {belegung})"
    return None


# ── Netz ────────────────────────────────────────────────────────────

def netz(folge: list) -> tuple[list[Schritt], list[Uebergang]]:
    """Schritte und Übergänge einer Kette (Parallelverzweigung: mehrere ``von`` bzw. ``nach``)."""
    schritte: list[Schritt] = []
    uebergaenge: list[Uebergang] = []

    def lauf(items, offen, schwebend):
        for it in items:
            if isinstance(it, Schritt):
                schritte.append(it)
                for u in schwebend:
                    u.nach.append(it.name)
                schwebend, offen = [], [it.name]
            elif isinstance(it, Transition):
                u = Uebergang(list(offen), it.bedingung)
                uebergaenge.append(u)
                offen, schwebend = [], [u]
            elif isinstance(it, Sprung):
                for u in schwebend:
                    u.nach.append(it.ziel)
                schwebend, offen = [], []
            elif it.art == "alternativ":
                gesammelt = []
                for ast in it.zweige:
                    _, s = lauf(ast, offen, [])
                    gesammelt += s
                offen, schwebend = [], gesammelt
            else:
                gesammelt = []
                for ast in it.zweige:
                    o, _ = lauf(ast, [], schwebend)
                    gesammelt += o
                offen, schwebend = gesammelt, []
        return offen, schwebend

    lauf(folge, [], [])
    return schritte, uebergaenge


def _unerreichbar(schritte: list[Schritt], uebergaenge: list[Uebergang]) -> list[str]:
    """Schritte, die keine Situation aktiv macht (Markenspiel; jede Transition kann schalten)."""
    start = frozenset(s.name for s in schritte if s.art == "initial" or s.aktivierung)
    if not start:
        return []
    erreicht = set(start)
    gesehen = {start}
    offen = [start]
    while offen and len(gesehen) < 5000:
        lage = offen.pop()
        for u in uebergaenge:
            if u.von and all(v in lage for v in u.von):
                neu = frozenset((lage - set(u.von)) | set(u.nach))
                if neu not in gesehen:
                    gesehen.add(neu)
                    erreicht |= neu
                    offen.append(neu)
    return [s.name for s in schritte if s.name not in erreicht]


def _kennzeichen_pruefen(folge: list, wo: str, zuordnung, m: list[Meldung]) -> None:
    eingaenge, ausgaenge = [], []
    if zuordnung is not None:
        if not isinstance(zuordnung, dict) or set(zuordnung) - {"eingaenge", "ausgaenge"}:
            m.append(("❌", f"{wo}: 'zuordnung' hat die Schlüssel 'eingaenge' und 'ausgaenge'"))
        else:
            eingaenge = [str(k) for k in zuordnung.get("eingaenge") or []]
            ausgaenge = [str(k) for k in zuordnung.get("ausgaenge") or []]
    vorgabe = set(eingaenge) | set(ausgaenge)
    in_bedingungen: dict[str, str] = {}
    in_aktionen: dict[str, str] = {}
    fremd: dict[str, str] = {}
    for it in _alle(folge):
        if isinstance(it, Transition):
            for k in KENNZEICHEN.findall(it.bedingung):
                in_bedingungen.setdefault(k, _name(it))
            for k in OHNE_BINDESTRICH.findall(it.bedingung):
                fremd.setdefault(k, _name(it))
        elif isinstance(it, Schritt):
            for a in it.aktionen:
                if a.art != "zwang":
                    for k in KENNZEICHEN.findall(a.variable):
                        in_aktionen.setdefault(k, _name(it))
                    for k in OHNE_BINDESTRICH.findall(a.variable):
                        fremd.setdefault(k, _name(it))
                for k in KENNZEICHEN.findall(a.bedingung or ""):
                    in_bedingungen.setdefault(k, _name(it))
    for k, ort in fremd.items():
        m.append(("⚠", f"{ort}: '{k}' sieht wie ein Kennzeichen ohne Bindestrich aus – Betriebsmittel schreiben sich "
                       f"'-{k}', interne Variablen tragen einen sprechenden Namen (C_Teile)"))
    alle = list(dict.fromkeys([*in_bedingungen, *in_aktionen]))
    gueltig = []
    for k in alle:
        probleme = kz.pruefe(k)
        if probleme and zuordnung is not None and k in vorgabe:
            m.append(("⚠", f"{wo}: {probleme[0]} – bleibt, weil die Zuordnungsliste der Aufgabe es vorgibt"))
        elif probleme:
            ort = in_bedingungen.get(k) or in_aktionen.get(k)
            for p in probleme:
                m.append(("❌", f"{ort}: {p}"))
        else:
            gueltig.append(k)
    for t_ in kz.tiefe_pruefen(gueltig)[0]:
        m.append(("⚠", f"{wo}: {t_}"))
    if zuordnung is None:
        return
    for k, ort in in_bedingungen.items():
        if k not in vorgabe:
            m.append(("❌", f"{ort}: '{k}' steht nicht in der Zuordnungsliste"))
    for k, ort in in_aktionen.items():
        if k in eingaenge:
            m.append(("❌", f"{ort}: '{k}' ist laut Zuordnungsliste ein Eingang und kann keine Aktion sein"))
        elif k not in ausgaenge:
            m.append(("❌", f"{ort}: '{k}' steht nicht unter den Ausgängen der Zuordnungsliste"))
    genutzt = set(in_bedingungen) | set(in_aktionen)
    for k in [*eingaenge, *ausgaenge]:
        if k not in genutzt:
            m.append(("⚠", f"{wo}: '{k}' aus der Zuordnungsliste kommt im GRAFCET nicht vor"))


def pruefe_kette(e: dict, wo: str, alle_schritte: set[str] | None = None) -> list[Meldung]:
    """Alle Regeln einer ``typ: grafcet``: Aufbau, Aktionen, Bedingungen, Kennzeichen, Erreichbarkeit."""
    m: list[Meldung] = []
    folge = lies_folge(e.get("kette"), f"{wo}: kette", m)
    if not folge:
        return m
    _abfolge(folge, None, wo, m, kette_ende=True)
    if isinstance(folge[0], Verzweigung):
        m.append(("❌", f"{wo}: Die Kette beginnt mit einem Schritt, nicht mit einer Verzweigung"))
    gesamt = list(_alle(folge))
    schritte = [it for it in gesamt if isinstance(it, Schritt)]
    namen = [s.name for s in schritte]
    for n in dict.fromkeys(namen):
        if namen.count(n) > 1:
            m.append(("❌", f"{wo}: Schrittname '{n}' kommt {namen.count(n)}-mal vor"))
    for it in gesamt:
        if isinstance(it, Sprung) and it.ziel not in namen:
            m.append(("❌", f"{_name(it)}: Diesen Schritt gibt es nicht ({', '.join(namen)})"))
    if schritte and not any(s.art == "initial" or s.aktivierung for s in schritte) \
            and not any(isinstance(it, Transition) and it.art == "quelle" for it in gesamt):
        m.append(("⚠", f"{wo}: kein Initialschritt ('art: initial') und keine Aktivierung ('aktivierung: true')"))

    # Aktionen über die ganze Kette: dieselbe Variable nicht gemischt, Gesetztes wird zurückgesetzt
    kontinuierlich: dict[str, str] = {}
    gespeichert: dict[str, list[tuple[str, str]]] = {}
    for s in schritte:
        for a in s.aktionen:
            if a.art in SPEICHERND:
                mz = ZUWEISUNG.match(a.text)
                if mz:
                    gespeichert.setdefault(mz.group(1).strip(), []).append((mz.group(2).strip(), s.name))
            elif a.art != "zwang":
                kontinuierlich.setdefault(a.variable, s.name)
    for var, werte in gespeichert.items():
        if var in kontinuierlich:
            m.append(("❌", f"{wo}: '{var}' wirkt in Schritt {kontinuierlich[var]} kontinuierlich und in Schritt "
                            f"{werte[0][1]} speichernd – nie beides auf derselben Variable"))
        gesetzt = [(w, n) for w, n in werte if w == "1" or var in w]    # ein Wert wie "ok" muss nicht zurück auf 0
        if gesetzt and not any(w == "0" for w, _ in werte):
            m.append(("⚠", f"{wo}: '{var}' wird in Schritt {gesetzt[0][1]} zugewiesen, aber nirgends auf 0 zurückgesetzt"))

    # Bedingungen: Zeitbezug und Alternativen
    variablen = set(namen) | (alle_schritte or set())
    for it in gesamt:
        texte = []
        if isinstance(it, Transition):
            texte.append(it.bedingung)
        elif isinstance(it, Schritt):
            texte += [a.bedingung for a in it.aktionen if a.bedingung]
        for t in texte:
            for x in SCHRITTVARIABLE.findall(t):
                if x not in variablen:
                    m.append(("⚠", f"{_name(it)}: '{t}' bezieht sich auf X{x}, aber einen Schritt {x} gibt es nicht"))
        if isinstance(it, Verzweigung) and it.art == "alternativ":
            erste = [a[0].bedingung for a in it.zweige if a and isinstance(a[0], Transition)]
            beide = _schliessen_aus(erste)
            if beide:
                m.append(("⚠", f"{wo}: Die Bedingungen der Alternative schließen sich nicht aus: {beide}"))

    _kennzeichen_pruefen(folge, wo, e.get("zuordnung"), m)
    if not any(s == "❌" for s, _ in m):
        for n in _unerreichbar(*netz(folge)):
            m.append(("⚠", f"{wo}: Schritt {n} wird nie aktiv"))
    return m


# ───────────────────────────── Textform ─────────────────────────────

def textform(e: dict) -> str:
    """Tabelle Schritt | Aktion | Transition zum Folgeschritt (Notationsblatt Abschn. 5) aus derselben Quelle."""
    folge = lies_folge(e.get("kette"), "kette", [])
    schritte, uebergaenge = netz(folge)
    zeilen = ["| Schritt | Aktion | Transition zum Folgeschritt |", "|---|---|---|"]
    for s in schritte:
        kopf = f"{s.name} {s.bezeichnung}" if s.bezeichnung else s.name
        if s.art == "initial":
            kopf += " (Initialschritt)"
        elif s.art == "makro":
            kopf += " (Makroschritt)"
        elif s.art == "einschliessend":
            kopf += " (einschließender Schritt)"
        if s.aktivierung:
            kopf += " (aktiviert mit dem einschließenden Schritt)"
        aktionen = "; ".join(a.textform for a in s.aktionen) or "–"
        wege = []
        for u in uebergaenge:
            if s.name not in u.von:
                continue
            ziel = " und ".join(u.nach) + (" (parallel)" if len(u.nach) > 1 else "") if u.nach else "Ende"
            weg = f"{u.bedingung} → {ziel}"
            andere = [v for v in u.von if v != s.name]
            if andere:
                weg += " (gemeinsam mit " + ", ".join(f"X{v}" for v in andere) + ")"
            wege.append(weg)
        zeilen.append(f"| {kopf} | {aktionen} | {'; '.join(wege) or '–'} |")
    return "\n".join(zeilen) + "\n"


# ───────────────────────────── Zeichnen ─────────────────────────────

def _kommentar(z, x: float, ym: float, roh) -> None:
    text = kommentar_zeilen(roh)
    n = text.count("\n")
    zh = SCHRIFT_KOMMENTAR * 1.25
    z.text(x, ym - n * zh / 2 + SCHRIFT_KOMMENTAR * 0.36, text, SCHRIFT_KOMMENTAR, zeilenhoehe=zh)


def _aktion_zeichnen(ctx, a: Aktion, x: float, y: float, b: float) -> None:
    z = ctx.z
    y2 = y + AKTION_H
    z.rechteck(x, y, x + b, y2)
    if a.art == "zwang":
        z.rechteck(x + 3, y + 3, x + b - 3, y2 - 3)
    z.text(x + b / 2, y + AKTION_H / 2 + 4.3, a.text, SCHRIFT, "middle")
    if a.art == "aktivierung":
        z.linienzug([(x, y), (x, y - FAHNE)], "normal", "ende", registrieren=True)
    elif a.art == "deaktivierung":
        z.linienzug([(x, y2), (x, y2 + FAHNE)], "normal", "ende", registrieren=True)
    elif a.art in MIT_BEDINGUNG:
        xs = x + STIEL_X
        z.linie(xs, y, xs, y - STIEL_OBEN, registrieren=True)
        if a.art == "ereignis":        # Fähnchen: Dreieck am oberen Ende des Strichs, nach links
            ys = y - STIEL_OBEN
            z.polygon([(xs, ys - 4), (xs, ys + 4), (xs - 8, ys)], "schwarz", "keine")
        plain, spans = darstellung(a.bedingung_zeichen)
        z.text(xs + 4, y - STIEL_OBEN + 8, plain, SCHRIFT_KLEIN, spans=spans)
    ctx.teile.append(Teilinfo(ctx.index, "grafcet_aktion", None, (x, y, x + b, y2), True))


def t_schritt(ctx, e: dict) -> None:
    z = ctx.z
    x, y = float(e["x"]), float(e["y"])
    x1, x2, y2 = x - S / 2, x + S / 2, y + S
    art = e.get("schrittart", "normal")
    z.rechteck(x1, y, x2, y2)
    if art == "initial":
        z.rechteck(x1 + 4, y + 4, x2 - 4, y2 - 4)
    elif art == "makro":
        z.linie(x1, y + 5, x2, y + 5)
        z.linie(x1, y2 - 5, x2, y2 - 5)
    elif art == "einschliessend":
        d = 7.0
        for (cx, cy, dx, dy) in ((x1, y, 1, 1), (x2, y, -1, 1), (x1, y2, 1, -1), (x2, y2, -1, -1)):
            z.linie(cx + d * dx, cy, cx, cy + d * dy)
    z.text(x, y + S / 2 + SCHRIFT_SCHRITT * 0.36, str(e["schritt"]), SCHRIFT_SCHRITT, "middle")
    if e.get("aktivierung"):
        z.text(x1 - 6, y + S / 2 + 5, "*", 14.0, "end")
    ctx.melde(e, (x1, y, x2, y2), klein=True)

    zeilen = lies_aktionen(e.get("aktionen"), f"Schritt {e['schritt']}", [])
    ym = y + S / 2
    haupt = z.zelle
    if not zeilen:
        if e.get("kommentar"):
            _kommentar(z, float(e.get("kommentar_x", x2 + 10)), ym, e["kommentar"])
        return
    probe = Schritt(str(e["schritt"]), zeilen=zeilen)
    lagen = probe.lagen
    xl = x2 + STUMMEL
    bus = any(lagen[i] - lagen[i - 1] > AKTION_H for i in range(1, len(lagen)))
    z.zelle = f"{haupt}v"
    if bus:      # Zeilen mit Fähnchen oder Bedingung haben Abstand; eine Sammelleitung verbindet sie
        xb = x2 + STUMMEL / 2
        z.linie(x2, ym, xb, ym)
        z.linie(xb, ym, xb, ym + lagen[-1] + AKTION_H / 2)
        for lage in lagen:
            z.linie(xb, ym + lage + AKTION_H / 2, xl, ym + lage + AKTION_H / 2)
    else:
        z.linie(x2, ym, xl, ym)
    n = 0
    kx = e.get("kommentar_x")
    for zeile, lage in zip(zeilen, lagen):
        xa = xl
        ya = ym + lage
        for a, b in zip(zeile, probe.spalten):
            n += 1
            z.zelle = f"{haupt}a{n}"
            _aktion_zeichnen(ctx, a, xa, ya, b)
            xa += b
        kommentar = next((a.kommentar for a in zeile if a.kommentar), None)
        if kommentar:
            z.zelle = f"{haupt}k{n}"
            _kommentar(z, max(float(kx), xa + 14) if kx is not None else xa + 14, ya + AKTION_H / 2, kommentar)
    z.zelle = haupt


def t_transition(ctx, e: dict) -> None:
    z = ctx.z
    x, y = float(e["x"]), float(e["y"])
    art = e.get("transitionsart", "normal")
    h = BALKEN / 2
    z.rechteck(x - h, y - 1.5, x + h, y + 1.5, "schwarz", "keine")
    if e.get("mit_linie"):
        if art != "quelle":
            z.linie(x, y - 16, x, y - 1.5)
        if art != "schluss":
            z.linie(x, y + 1.5, x, y + 16)
    plain, spans = darstellung(bedingung_normal(e.get("transition", "")))
    if plain:
        z.text(x + h + 8, y + 4.3, plain, SCHRIFT, spans=spans)
    if e.get("name"):
        z.text(x - h - 6, y + 4.3, f"({e['name']})", SCHRIFT, "end")
    if e.get("kommentar"):
        kx = e.get("kommentar_x")
        _kommentar(z, float(kx) if kx is not None else x + h + 8 + _w(plain, SCHRIFT) + 14, y, e["kommentar"])
    ctx.melde(e, (x - h, y - 1.5, x + h, y + 1.5), klein=True, extra={"oben": (x, y - 1.5), "unten": (x, y + 1.5)})


def t_balken(ctx, e: dict) -> None:
    z = ctx.z
    x, y, b = float(e["x"]), float(e["y"]), float(e["b"])
    parallel = e.get("balkenart", "alternativ") == "parallel"
    z.linie(x, y, x + b, y, registrieren=True)
    y2 = y
    if parallel:           # Doppelstrich
        y2 = y + 4
        z.linie(x, y2, x + b, y2, registrieren=True)
    extra = {}
    for i, xi in enumerate(e["abzweige"]):
        extra[f"o{i}"] = (float(xi), y)
        extra[f"u{i}"] = (float(xi), y2)
    ctx.melde(e, (x, y, x + b, y2), extra=extra)


def t_rahmen(ctx, e: dict) -> None:
    z = ctx.z
    x, y, b, h = (float(e[k]) for k in ("x", "y", "b", "h"))
    z.rechteck(x, y, x + b, y + h, "keine", "normal", rundung=4)
    for schluessel, yt in (("oben", y), ("unten", y + h)):
        if e.get(schluessel):
            t = str(e[schluessel])
            w = len(t) * SCHRIFT_SCHRITT * 0.66
            z.rechteck(x + 14, yt - 8, x + 22 + w, yt + 8, "weiss", "keine")
            z.text(x + 18, yt + 4.6, t, SCHRIFT_SCHRITT)
    ctx.melde(e, (x, y, x + b, y + h))


def t_grafcet(ctx, e: dict) -> None:   # pragma: no cover – wird vorher von ``aufloesen`` ersetzt
    raise ValueError("'typ: grafcet' wurde nicht aufgelöst")


SCHEMA.update({
    "grafcet": ({"kette"}, {"x", "y", "zuordnung", "rahmen"}),
    "grafcet_schritt": ({"x", "y", "schritt"}, {"schrittart", "aktivierung", "aktionen", "kommentar_x"}),
    "grafcet_transition": ({"x", "y", "transition"}, {"transitionsart", "mit_linie", "kommentar_x"}),
    "grafcet_balken": ({"x", "y", "b", "abzweige"}, {"balkenart"}),
    "grafcet_rahmen": ({"x", "y", "b", "h"}, {"oben", "unten"}),
})
ZEICHNER.update({
    "grafcet": t_grafcet, "grafcet_schritt": t_schritt, "grafcet_transition": t_transition,
    "grafcet_balken": t_balken, "grafcet_rahmen": t_rahmen,
})
ZAHLEN.add("kommentar_x")
WAHRHEITEN.update({"aktivierung", "mit_linie"})
AUFZAEHLUNGEN.update({"schrittart": SCHRITTARTEN, "transitionsart": TRANSITIONSARTEN,
                      "balkenart": ("alternativ", "parallel")})


# ───────────────────────────── Lage berechnen ─────────────────────────────

@dataclass
class _Mass:
    links: float
    rechts: float
    k_x: float           # Kommentarspalte der Aktionen, von der Mitte aus
    t_x: float           # Kommentarspalte der Transitionen, von der Mitte aus
    versatz: dict = field(default_factory=dict)    # je Verzweigung (id) die Lage der Äste
    spalten: tuple[float, float] = (0.0, 0.0)


def _kommentar_b(roh) -> float:
    return _w(kommentar_zeilen(roh), SCHRIFT_KOMMENTAR) if roh else 0.0


def _spalten(folge: list) -> tuple[float, float]:
    """(Breite der ersten Aktionsspalte, Breite der Bedingungen) aller Teile auf derselben senkrechten Linie.

    Rechtecke einer Linie werden gleich breit, ihre Kommentare stehen in einer Spalte; nur eine Zeile mit
    mehreren Aktionen rückt ihren Kommentar weiter nach rechts.
    """
    b1 = 0.0
    t_b = 0.0
    for it in folge:
        if isinstance(it, Schritt) and it.zeilen:
            b1 = max(b1, it.spalten[0])
        elif isinstance(it, Transition):
            t_b = max(t_b, _w(it.klartext, SCHRIFT))
        elif isinstance(it, Verzweigung) and it.zweige:   # der erste Ast läuft unter der Linie weiter
            b, t = _spalten(it.zweige[0])
            b1, t_b = max(b1, b), max(t_b, t)
    return b1, t_b


def _mass(folge: list, besitzer: dict, spalten: tuple[float, float] | None = None) -> _Mass:
    b1, t_b = spalten or _spalten(folge)
    spalten = (b1, t_b)
    k_x = S / 2 + STUMMEL + b1 + 14 if b1 else S / 2 + 10
    t_x = BALKEN / 2 + 8 + t_b + 14
    links, rechts = S / 2, S / 2
    versatz = {}
    for it in folge:
        if isinstance(it, Schritt):
            links = max(links, S / 2 + (16 if it.aktivierung else 0))
            rest = sum(it.spalten[1:])
            rechts = max(rechts, S / 2 + (STUMMEL + b1 + rest if it.zeilen else 0))
            for zeile in it.zeilen:
                k = next((a.kommentar for a in zeile if a.kommentar), None)
                if k:
                    rechts = max(rechts, k_x + sum(it.spalten[1:len(zeile)]) + _kommentar_b(k))
                a = zeile[-1]
                if a.art in MIT_BEDINGUNG:     # die Bedingung ragt über das letzte Rechteck hinaus
                    x_a = S / 2 + STUMMEL + (sum(it.spalten[1:len(zeile) - 1]) + b1 if len(zeile) > 1 else 0)
                    rechts = max(rechts, x_a + STIEL_X + 4 + _w(a.bedingung_zeichen, SCHRIFT_KLEIN))
            if it.kommentar:
                rechts = max(rechts, k_x + _kommentar_b(it.kommentar))
        elif isinstance(it, Transition):
            if it.name:
                links = max(links, BALKEN / 2 + 6 + _w(f"({it.name})", SCHRIFT))
            r = t_x + _kommentar_b(it.kommentar) if it.kommentar else BALKEN / 2 + 8 + _w(it.klartext, SCHRIFT)
            rechts = max(rechts, r)
        elif isinstance(it, Verzweigung):
            massen = [_mass(z, besitzer, spalten if j == 0 else None) for j, z in enumerate(it.zweige)]
            pos = [0.0]
            for vor, nach in zip(massen, massen[1:]):
                pos.append(pos[-1] + vor.rechts + ABSTAND_Z + nach.links)
            versatz[id(it)] = pos
            for p, ma in zip(pos, massen):
                links = max(links, ma.links - p)
                rechts = max(rechts, p + ma.rechts)
    bahnen_l, bahnen_r = _eigene_spruenge(folge, besitzer)
    if bahnen_l:
        links += BAHN_LUFT + len(bahnen_l) * BAHN
    if bahnen_r:
        rechts += BAHN_LUFT + len(bahnen_r) * BAHN
    return _Mass(links, rechts, k_x, t_x, versatz, spalten)


def _endet_mit_sprung(ast: list) -> bool:
    if not ast:
        return True
    letztes = ast[-1]
    if isinstance(letztes, Sprung):
        return True
    if isinstance(letztes, Transition) and letztes.art == "schluss":
        return True
    if isinstance(letztes, Verzweigung):
        return all(_endet_mit_sprung(z) for z in letztes.zweige)
    return False


def _sprung_ziele(folge: list) -> set[str]:
    return {it.ziel for it in _alle(folge) if isinstance(it, Sprung)}


def _sprung_besitzer(folge: list) -> dict[int, tuple[int, bool]]:
    """Je Sprung die innerste Folge, die das Ziel enthält, und ob die Quelle dort auf dem linken Rand liegt.

    Die Rücklaufbahn liegt neben dieser Folge: links, wenn der Weg dorthin frei ist, sonst rechts.
    """
    ergebnis: dict[int, tuple[int, bool]] = {}

    def lauf(f: list, stapel: list) -> None:
        stapel = [*stapel, [f, True]]
        for it in f:
            if isinstance(it, Sprung):
                for g, links in reversed(stapel):
                    if any(isinstance(t, Schritt) and t.name == it.ziel for t in _alle(g)):
                        ergebnis[id(it)] = (id(g), links)
                        break
            elif isinstance(it, Verzweigung):
                for j, ast in enumerate(it.zweige):
                    gemerkt = [e[1] for e in stapel]
                    if j:
                        for e in stapel:
                            e[1] = False
                    lauf(ast, stapel)
                    for e, wert in zip(stapel, gemerkt):
                        e[1] = wert
                offene = [j for j, ast in enumerate(it.zweige) if not _endet_mit_sprung(ast)]
                if not offene or offene[0] != 0:     # die Kette läuft nicht unter dem ersten Ast weiter
                    for e in stapel:
                        e[1] = False

    lauf(folge, [])
    return ergebnis


def _eigene_spruenge(folge: list, besitzer: dict) -> tuple[list, list]:
    """(linke, rechte) Sprünge, deren Bahn neben dieser Folge liegt."""
    links, rechts = [], []
    for it in _alle(folge):
        if isinstance(it, Sprung) and besitzer.get(id(it), (None,))[0] == id(folge):
            (links if besitzer[id(it)][1] else rechts).append(it)
    return links, rechts


class _Bau:
    """Setzt eine Kette in Einzelteile mit Koordinaten um."""

    def __init__(self, e: dict, nr: int, x: float, y: float) -> None:
        self.e = e
        self.nr = nr
        self.x, self.y = x, y
        self.folge = lies_folge(e["kette"], "kette", [])
        self.ziele = _sprung_ziele(self.folge)
        self.besitzer = _sprung_besitzer(self.folge)
        self.linien: list[dict] = []
        self.formen: list[dict] = []
        self.spruenge: dict[int, tuple] = {}     # Sprung → (Anker, y, x) seiner Quelle
        self.lage: dict[str, tuple[float, float, str, float]] = {}
        self.zaehler = 0
        self.max_x = x
        self.max_y = y

    def ref(self, was: str) -> str:
        self.zaehler += 1
        return f"g{self.nr}_{was}{self.zaehler}"

    def linie(self, von, nach) -> None:
        if von and nach:
            self.linien.append({"typ": "linie", "punkte": [von, nach]})

    def setze(self, folge: list, cx: float, y: float, vor: str | None, links: bool, nach_balken: bool = False,
              spalten: tuple[float, float] | None = None):
        """Rückgabe: (y am Ende, Anker am Ende oder None, x am Ende, liegt der Rest noch ganz links)."""
        ma = _mass(folge, self.besitzer, spalten)
        cx_start = cx
        self.max_x = max(self.max_x, cx + ma.rechts)
        for it in folge:
            if isinstance(it, Schritt):
                if nach_balken:
                    y += ABSTAND_B
                if it.name in self.ziele:
                    y += EINMUENDUNG + (4 if vor is None else 2)
                y += it.oben_bedarf
                ref = self.ref("s")
                form = {"typ": "grafcet_schritt", "ref": ref, "x": cx, "y": y, "schritt": it.name,
                        "schrittart": it.art, "aktivierung": it.aktivierung, "legende": False}
                if it.zeilen:
                    form["aktionen"] = [[_als_spec(a, ma.spalten[0] if i == 0 else None) for i, a in enumerate(z)]
                                        for z in it.zeilen]
                if it.kommentar:
                    form["kommentar"] = it.kommentar
                form["kommentar_x"] = cx + ma.k_x
                self.formen.append(form)
                self.linie(vor, f"{ref}@oben")
                self.lage[it.name] = (cx, y, ref, it.oben_bedarf)
                vor = f"{ref}@unten"
                y += S + it.unten_bedarf
                nach_balken = False
            elif isinstance(it, Transition):
                ref = self.ref("t")
                kommentar_h = (kommentar_zeilen(it.kommentar).count("\n") + 1) * SCHRIFT_KOMMENTAR * 1.25 if it.kommentar else 0
                halb = max(ABSTAND_T, kommentar_h / 2 + 8)
                y_t = y + halb
                form = {"typ": "grafcet_transition", "ref": ref, "x": cx, "y": y_t, "transition": it.bedingung,
                        "transitionsart": it.art, "legende": False, "kommentar_x": cx + ma.t_x}
                if it.name:
                    form["name"] = it.name
                if it.kommentar:
                    form["kommentar"] = it.kommentar
                self.formen.append(form)
                self.linie(vor, f"{ref}@oben")
                vor = None if it.art == "schluss" else f"{ref}@unten"
                y = y_t + halb
                nach_balken = False
            elif isinstance(it, Sprung):
                if nach_balken:      # erst ein Stück senkrecht aus der Zusammenführung, dann zur Bahn
                    y += ABSTAND_B
                self.spruenge[id(it)] = (vor, y, cx)
                vor = None
            else:
                y, vor, cx, links = self._verzweigung(it, ma, cx, y, vor, links)
                nach_balken = True
        self.max_y = max(self.max_y, y)
        self._bahnen(folge, ma, cx_start)
        return y, vor, cx, links

    def _bahnen(self, folge: list, ma: _Mass, cx: float) -> None:
        """Rücksprünge dieser Folge führen: kurze Wege innen, lange außen."""
        def spanne(s):
            return abs(self.spruenge[id(s)][1] - self.lage[s.ziel][1])
        links, rechts = _eigene_spruenge(folge, self.besitzer)
        rand_l = cx - ma.links + (BAHN if links else 0)
        rand_r = cx + ma.rechts - (BAHN if rechts else 0)
        for seite, liste in ((-1, links), (1, rechts)):
            for k, sprung in enumerate(sorted(liste, key=spanne)):
                vor, y, x_von = self.spruenge[id(sprung)]
                x_ziel, y_ziel, ref_ziel, oben = self.lage[sprung.ziel]
                x_bahn = (rand_l + (len(links) - 1 - k) * BAHN) if seite < 0 else (rand_r - (len(rechts) - 1 - k) * BAHN)
                y_ein = y_ziel - oben - EINMUENDUNG      # über den Pfeilen der Aktionen des Zielschritts
                if y > y_ein:      # aufwärts: Pfeil auf dem senkrechten Stück
                    y_mitte = round((y + y_ein) / 2 / 10) * 10
                    self.linien.append({"typ": "linie", "punkte": [vor, [x_von, y], [x_bahn, y], [x_bahn, y_mitte]],
                                        "pfeil": "ende"})
                    self.linien.append({"typ": "linie", "punkte": [[x_bahn, y_mitte], [x_bahn, y_ein], [x_ziel, y_ein],
                                                                   f"{ref_ziel}@oben"]})
                else:
                    self.linien.append({"typ": "linie", "punkte": [vor, [x_von, y], [x_bahn, y], [x_bahn, y_ein],
                                                                   [x_ziel, y_ein], f"{ref_ziel}@oben"]})

    def _verzweigung(self, it: Verzweigung, ma: _Mass, cx: float, y: float, vor: str | None, links: bool):
        parallel = it.art == "parallel"
        pos = ma.versatz[id(it)]
        xs = [cx + p for p in pos]
        art = "parallel" if parallel else "alternativ"
        y_b = y + (ABSTAND_B if not parallel else 0)
        ragen = 12.0 if parallel else 0.0
        ref_o = self.ref("v")
        self.formen.append({"typ": "grafcet_balken", "ref": ref_o, "x": xs[0] - ragen, "y": y_b,
                            "b": xs[-1] - xs[0] + 2 * ragen, "abzweige": xs, "balkenart": art, "legende": False})
        self.linie(vor, f"{ref_o}@o0")
        y_start = y_b + (4 if parallel else 0)
        enden = []
        for j, ast in enumerate(it.zweige):
            y_ast, v_ast, x_ast, _ = self.setze(ast, xs[j], y_start, f"{ref_o}@u{j}", links and j == 0, parallel,
                                                ma.spalten if j == 0 else None)
            if v_ast:
                enden.append((j, x_ast, y_ast, v_ast))
        if not enden:
            return max(self.max_y, y_start), None, cx, links
        y_unten = max(e[2] for e in enden)
        if len(enden) == 1:
            j, x_ast, _, v_ast = enden[0]
            return y_unten, v_ast, x_ast, links and j == 0
        x_e = [e[1] for e in enden]
        y_m = y_unten + (ABSTAND_B if parallel else 0)
        ref_u = self.ref("v")
        self.formen.append({"typ": "grafcet_balken", "ref": ref_u, "x": min(x_e) - ragen, "y": y_m,
                            "b": max(x_e) - min(x_e) + 2 * ragen, "abzweige": x_e, "balkenart": art, "legende": False})
        for i, (_, _, _, v_ast) in enumerate(enden):
            self.linie(v_ast, f"{ref_u}@o{i}")
        return y_m + (4 if parallel else 0), f"{ref_u}@u0", x_e[0], links and enden[0][0] == 0

    def bauen(self) -> list[dict]:
        rahmen = self.e.get("rahmen") or {}
        luft = RAHMEN_LUFT if rahmen else 0.0
        ma = _mass(self.folge, self.besitzer)
        self.setze(self.folge, self.x + luft + ma.links, self.y + luft, None, True)
        teile = []
        if rahmen:
            self.max_x += RAHMEN_LUFT
            self.max_y += RAHMEN_LUFT
            teile.append({"typ": "grafcet_rahmen", "ref": self.ref("r"), "x": self.x, "y": self.y,
                          "b": self.max_x - self.x, "h": self.max_y - self.y, "legende": False,
                          **{k: rahmen[k] for k in ("oben", "unten") if rahmen.get(k)}})
        return teile + self.linien + self.formen


def _als_spec(a: Aktion, mindestbreite: float | None = None) -> dict:
    d = {"art": a.art, "text": a.text}
    if a.bedingung:
        d["bedingung"] = a.bedingung
    if a.kommentar:
        d["kommentar"] = a.kommentar
    if a.b or mindestbreite:
        d["b"] = max(float(a.b or 0), float(mindestbreite or 0))
    return d


def enthaelt_grafcet(spec: dict) -> bool:
    return any(isinstance(e, dict) and e.get("typ") == "grafcet" for e in spec.get("elemente") or [])


def aufloesen(spec: dict) -> dict:
    """Jede ``typ: grafcet`` in Einzelteile umsetzen; fehlende Bildmaße aus dem Ergebnis berechnen."""
    if not enthaelt_grafcet(spec):
        return spec
    neu = dict(spec)
    elemente: list = []
    nr = 0
    x_frei = 30.0
    max_x, max_y = 0.0, 0.0
    for e in spec["elemente"]:
        if isinstance(e, dict) and e.get("typ") == "grafcet":
            nr += 1
            bau = _Bau(e, nr, float(e.get("x", x_frei)), float(e.get("y", 30)))
            elemente += bau.bauen()
            x_frei = bau.max_x + 40
            max_x, max_y = max(max_x, bau.max_x), max(max_y, bau.max_y)
        else:
            elemente.append(e)
    neu["elemente"] = elemente
    fuss = spec.get("fusszeile") or []
    fuss = [fuss] if isinstance(fuss, str) else fuss
    fuss_b = max((len(z) for z in fuss), default=0) * 11 * 0.55 + 40
    neu.setdefault("breite", math.ceil(max(max_x + 24, fuss_b, 200)))
    neu.setdefault("hoehe", math.ceil(max(max_y + 20, 140)))
    return neu
