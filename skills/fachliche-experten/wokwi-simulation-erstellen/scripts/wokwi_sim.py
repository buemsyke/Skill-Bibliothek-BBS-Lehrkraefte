#!/usr/bin/env python3
"""wokwi_sim – Testfälle der Spec ausführen: im Logikmodell und im erzeugten Sketch (g++).

Zwei unabhängige Wege, dieselben Testfälle:
  Logikmodell  wertet die Spec selbst aus (Zyklus wie im Sketch, Zeit in ms, Sprünge bis zur nächsten
               Zeitschwelle, solange sich nichts ändert).
  Programm     übersetzt sketch.ino mit g++ gegen einen nachgebildeten Arduino-Kern (Pins, millis(),
               analogRead, Serial) und steuert ihn über stdin; loop() läuft je Millisekunde einmal.
Stimmen beide mit den Erwartungen überein, ist die Aufgabe so umgesetzt, wie die Spec sie beschreibt.
Die Wokwi-Szenarien werden aus dem Lauf des Logikmodells aufgezeichnet.
"""

from __future__ import annotations

import operator
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import wokwi_projekt as wp
import wokwi_spec as ws

TIPP_MS = 200      # Dauer eines Tastendrucks
NACH_MS = 50       # Wartezeit nach einer Aktion bis zur Prüfung
VORLAUF_MS = 50    # nach dem Start bis zum ersten Testschritt
TOL_MS = 100       # Prüfung kurz vor bzw. nach einer Zeitschwelle (Simulationszeit ist exakt)

_OPS = {"≥": operator.ge, "≤": operator.le, "=": operator.eq, "≠": operator.ne, "<": operator.lt, ">": operator.gt}


class SimFehler(RuntimeError):
    pass


# ───────────────────────────── Logikmodell ─────────────────────────────

class Logikmodell:
    """Wertet die Spec im selben Zyklus aus wie der Sketch."""

    art = "Logik (Spec)"

    def __init__(self, spec: ws.Spec):
        self.spec = spec
        zr = spec.zeitraffer
        self.schwellen = {(n, ms): zr(ms) for n, ms in spec.zeiten()}
        self.pegel: dict[str, int] = {}
        self.roh: dict[str, int] = {}
        self.spur: list[tuple[int, dict]] = []
        self._kompilieren()

    # Bedingungen als Funktionen
    def _k(self, baum):
        art = baum[0]
        if art == "const":
            c = baum[1]
            return lambda m: c
        if art == "sig":
            n = baum[1]
            return lambda m: bool(m.v[n])
        if art == "schritt":
            n = baum[1]
            return lambda m: m.schritt == n
        if art == "zeit":
            n, t = baum[2], self.schwellen[(baum[2], baum[1])]
            return lambda m: m.schritt == n and m.t - m.beginn >= t
        if art == "vgl":
            n, f, w = baum[1], _OPS[baum[2]], baum[3]
            return lambda m: f(m.v[n], w)
        if art == "flanke":
            n = baum[2]
            if baum[1] == "↑":
                return lambda m: bool(m.v[n]) and not m.vorher[n]
            return lambda m: not m.v[n] and bool(m.vorher[n])
        if art == "nicht":
            f = self._k(baum[1])
            return lambda m: not f(m)
        fs = [self._k(x) for x in baum[1]]
        if art == "und":
            return lambda m: all(f(m) for f in fs)
        return lambda m: any(f(m) for f in fs)

    def _kompilieren(self):
        s = self.spec
        self.f_sr = [(m.name, m.dominant, self._k(m.setzen) if m.setzen else None,
                      self._k(m.ruecksetzen) if m.ruecksetzen else None)
                     for m in s.merker if m.setzen or m.ruecksetzen]
        self.f_erzw = [(self._k(e.bedingung), e.nach) for e in s.erzwingen]
        self.f_trans = {x.nr: [(self._k(t.bedingung), t.ziel) for t in x.transitionen] for x in s.schritte}
        self.f_akt: dict[str, list] = {}
        for ziel, arten in s.aktionsziele().items():
            if arten == {"kontinuierlich"}:
                self.f_akt[ziel] = [(x.nr, self._k(a.bedingung) if a.bedingung else None)
                                    for x in s.schritte for a in x.aktionen if a.ziel == ziel]
        self.f_zuw = [(z.ziel, self._k(z.bedingung)) for z in s.zuweisungen]
        self.gesp = {x.nr: ([a for a in x.aktionen if a.art == "aktivierung"],
                            [a for a in x.aktionen if a.art == "deaktivierung"]) for x in s.schritte}

    # Schnittstelle wie Hostprogramm
    def setze_pin(self, pin: str, pegel: int):
        self.pegel[pin] = pegel

    def setze_roh(self, pin: str, roh: int):
        self.roh[pin] = roh

    def start(self):
        s = self.spec
        self.t, self.schritt, self.beginn = 0, s.initial, 0
        self.v: dict[str, float] = {}
        for x in (*s.eingaenge, *s.ausgaenge):
            self.v[x.bmk] = 0
        for m in s.merker:
            self.v[m.name] = m.start
        for a in s.analog:
            self.v[a.bmk] = 0.0
        self.vorher = {f: 0 for f in s.flanken()}
        self._speichernd(self.schritt, 0)
        self.spur = []
        self._lesen()

    def _speichernd(self, nr: int, welche: int):
        for a in self.gesp.get(nr, ([], []))[welche]:
            art = a.ausdruck[0]
            if art == "wert":
                self.v[a.ziel] = a.ausdruck[1]
            else:
                self.v[a.ziel] = self.v[a.ziel] + (a.ausdruck[2] if art == "plus" else -a.ausdruck[2])

    def _wechsel(self, neu: int):
        self._speichernd(self.schritt, 1)
        self.schritt, self.beginn = neu, self.t
        self._speichernd(neu, 0)

    def _lesen(self):
        for e in self.spec.eingaenge:
            self.v[e.bmk] = self.pegel.get(e.pin, 0)
        for a in self.spec.analog:
            self.v[a.bmk] = ws.wert_aus_roh(a, self.roh.get(a.pin, 0))

    def _signatur(self):
        return (self.schritt, self.beginn, tuple(self.v.values()), tuple(self.vorher.values()))

    def zyklus(self):
        self._lesen()
        for name, dominant, fs, fr in self.f_sr:
            folge = ((fs, 1), (fr, 0)) if dominant == "ruecksetzen" else ((fr, 0), (fs, 1))
            for f, w in folge:
                if f and f(self):
                    self.v[name] = w
        erzwungen = False
        for f, nach in self.f_erzw:
            if f(self):
                if self.schritt != nach:
                    self._wechsel(nach)
                erzwungen = True
                break
        if not erzwungen:
            for f, ziel in self.f_trans.get(self.schritt, []):
                if f(self):
                    self._wechsel(ziel)
                    break
        for ziel, quellen in self.f_akt.items():
            self.v[ziel] = int(any(self.schritt == nr and (f is None or f(self)) for nr, f in quellen))
        for ziel, f in self.f_zuw:
            self.v[ziel] = int(f(self))
        for n in self.vorher:
            self.vorher[n] = self.v[n]

    def lauf(self, ms: int):
        ende = self.t + max(0, int(ms))
        while self.t < ende:
            vorher = self._signatur()
            self.t += 1
            self.zyklus()
            if self._signatur() != vorher or not self.spur:
                self._spur()
                continue
            # nichts geändert: bis zur nächsten Zeitschwelle des aktiven Schritts springen
            naechste = [self.beginn + t for (n, _), t in self.schwellen.items()
                        if n == self.schritt and self.beginn + t > self.t]
            self.t = min([ende] + [x - 1 for x in naechste if x - 1 >= self.t])

    def _spur(self):
        self.spur.append((self.t, self.zustand()))

    def zustand(self) -> dict:
        z = {"T": self.t, "W": self.beginn, "X": self.schritt}
        for x in (*self.spec.eingaenge, *self.spec.ausgaenge):
            z[x.bmk] = int(self.v[x.bmk])
        for m in self.spec.merker:
            z[m.name] = int(self.v[m.name])
        for a in self.spec.analog:
            z[a.bmk] = round(self.v[a.bmk], 3)
        return z

    def ende(self):
        return "", self.spur


# ───────────────────────────── Programm (g++) ─────────────────────────────

ARDUINO_H = r"""// Nachgebildeter Arduino-Kern für den Test des Sketches (wokwi-simulation-erstellen) – nur Host.
#pragma once
#include <cstdint>
#include <cstdio>
#include <cstring>
typedef uint8_t byte;
typedef bool boolean;
#define HIGH 1
#define LOW 0
#define INPUT 0
#define OUTPUT 1
#define INPUT_PULLUP 2
#define INPUT_PULLDOWN 3
#ifdef HOST_UNO
static const uint8_t A0 = 14, A1 = 15, A2 = 16, A3 = 17, A4 = 18, A5 = 19;
#endif
namespace host {
extern unsigned long jetzt;
extern int pegel[64];
extern int modus[64];
extern int roh[64];
extern FILE* serial;
}
inline unsigned long millis() { return host::jetzt; }
inline void delay(unsigned long ms) { host::jetzt += ms; }
inline void pinMode(uint8_t p, uint8_t m) { host::modus[p] = m; }
inline int digitalRead(uint8_t p) { return host::pegel[p]; }
inline void digitalWrite(uint8_t p, uint8_t v) { host::pegel[p] = v ? 1 : 0; }
inline int analogRead(uint8_t p) { return host::roh[p]; }
inline uint32_t analogReadMilliVolts(uint8_t p) { return (uint32_t)host::roh[p]; }
class __FlashStringHelper;
#define F(s) (reinterpret_cast<const __FlashStringHelper*>(s))
struct HostSerial {
  void begin(unsigned long) {}
  void print(const char* s) { fputs(s, host::serial); }
  void print(const __FlashStringHelper* s) { fputs(reinterpret_cast<const char*>(s), host::serial); }
  void print(char c) { fputc(c, host::serial); }
  void print(int v) { fprintf(host::serial, "%d", v); }
  void print(unsigned int v) { fprintf(host::serial, "%u", v); }
  void print(long v) { fprintf(host::serial, "%ld", v); }
  void print(unsigned long v) { fprintf(host::serial, "%lu", v); }
  void print(double v, int stellen = 2) { fprintf(host::serial, "%.*f", stellen, v); }
  void println() { fputc('\n', host::serial); }
  template <typename T> void println(T v) { print(v); println(); }
  void println(double v, int stellen) { print(v, stellen); println(); }
};
extern HostSerial Serial;
"""

HOST_CPP = r"""// Testtreiber: Befehle über stdin (pin P V | roh P V | start | lauf MS | zustand | ende)
#include "Arduino.h"
#include "sketch.ino"
#include "zustand.inc"
namespace host {
unsigned long jetzt = 0;
int pegel[64];
int modus[64];
int roh[64];
FILE* serial = nullptr;
}
HostSerial Serial;

int main(int argc, char** argv) {
  if (argc < 3) return 2;
  host::serial = fopen(argv[1], "w");
  FILE* spur = fopen(argv[2], "w");
  char zeile[256], bild[2048], altbild[2048] = "";
  while (fgets(zeile, sizeof zeile, stdin)) {
    int p = 0, v = 0;
    unsigned long ms = 0;
    if (sscanf(zeile, "pin %d %d", &p, &v) == 2) { host::pegel[p] = v; puts("ok"); }
    else if (sscanf(zeile, "roh %d %d", &p, &v) == 2) { host::roh[p] = v; puts("ok"); }
    else if (strncmp(zeile, "start", 5) == 0) {
      setup();  // Spur beginnt mit dem ersten Durchlauf von loop()
      puts("ok");
    }
    else if (sscanf(zeile, "lauf %lu", &ms) == 1) {
      for (unsigned long i = 0; i < ms; i++) {
        host::jetzt++;
        loop();
        host_zustand(bild, sizeof bild);
        // Spur ohne Zeitfelder vergleichen (beginnt nach W=…)
        const char* a = strstr(bild, " X="); const char* b = strstr(altbild, " X=");
        if (!b || strcmp(a, b) != 0) { fprintf(spur, "%s\n", bild); strcpy(altbild, bild); }
      }
      puts("ok");
    }
    else if (strncmp(zeile, "zustand", 7) == 0) { host_zustand(bild, sizeof bild); puts(bild); }
    else if (strncmp(zeile, "ende", 4) == 0) break;
    else { puts("fehler"); }
    fflush(stdout);
  }
  fclose(host::serial);
  fclose(spur);
  return 0;
}
"""


def zustand_inc(spec: ws.Spec) -> str:
    z = ["// erzeugt: Zustand des Sketches für den Testtreiber",
         "void host_zustand(char* b, size_t n) {",
         "  int k = snprintf(b, n, \"T=%lu W=%lu X=%d\", host::jetzt, (unsigned long)schrittBeginn, (int)schritt);"]
    for x in (*spec.eingaenge, *spec.ausgaenge):
        nr = ws.pin_nummer(spec.plattform, x.pin)
        z.append(f"  k += snprintf(b + k, n - k, \" {x.bmk}=%d\", host::pegel[{nr}]);")
    for a in spec.analog:
        nr = ws.pin_nummer(spec.plattform, a.pin)
        z.append(f"  k += snprintf(b + k, n - k, \" {a.bmk}=%.3f\", (double){ws.variable(a.bmk)});")
    for m in spec.merker:
        z.append(f"  k += snprintf(b + k, n - k, \" {m.name}=%d\", (int){m.name});")
    z.append("  (void)k;")
    z.append("}")
    return "\n".join(z) + "\n"


def gxx() -> str | None:
    return shutil.which("g++")


@dataclass
class Uebersetzung:
    ordner: Path
    programm: Path
    warnungen: list[str] = field(default_factory=list)


def uebersetze(spec: ws.Spec, sketch_text: str, ordner: Path | None = None) -> Uebersetzung:
    """sketch.ino mit g++ (gnu++11 wie die Arduino-Umgebung) gegen den nachgebildeten Kern übersetzen."""
    compiler = gxx()
    if not compiler:
        raise SimFehler("g++ nicht gefunden – Programm nicht getestet")
    ordner = Path(ordner or tempfile.mkdtemp(prefix="wokwi_host_"))
    ordner.mkdir(parents=True, exist_ok=True)
    (ordner / "Arduino.h").write_text(ARDUINO_H, encoding="utf-8")
    (ordner / "host.cpp").write_text(HOST_CPP, encoding="utf-8")
    (ordner / "sketch.ino").write_text('#include "Arduino.h"\n#line 1 "sketch.ino"\n' + sketch_text, encoding="utf-8")
    (ordner / "zustand.inc").write_text(zustand_inc(spec), encoding="utf-8")
    programm = ordner / "host"
    makro = "-DHOST_UNO" if spec.plattform == "arduino-uno" else "-DHOST_ESP32"
    r = subprocess.run([compiler, "-std=gnu++11", "-O1", "-Wall", "-Wextra", makro, "-x", "c++", "host.cpp",
                        "-o", str(programm)], cwd=ordner, capture_output=True, text=True)
    if r.returncode != 0:
        raise SimFehler("sketch.ino übersetzt nicht:\n" + r.stderr.strip())
    warn = [z for z in r.stderr.splitlines() if "sketch.ino" in z and "warning" in z]
    return Uebersetzung(ordner, programm, warn)


class Hostprogramm:
    """Erzeugter Sketch, übersetzt mit g++, gesteuert über stdin/stdout."""

    art = "Programm (g++)"

    def __init__(self, spec: ws.Spec, ueb: Uebersetzung):
        self.spec, self.ueb = spec, ueb
        self.proc = None
        self.serial = ueb.ordner / "serial.log"
        self.spurdatei = ueb.ordner / "spur.log"
        self.proc = subprocess.Popen([str(ueb.programm), str(self.serial), str(self.spurdatei)],
                                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)

    def _befehl(self, text: str) -> str:
        self.proc.stdin.write(text + "\n")
        self.proc.stdin.flush()
        antwort = self.proc.stdout.readline().strip()
        if antwort == "fehler" or not antwort:
            raise SimFehler(f"Testtreiber: Befehl „{text}“ nicht verstanden")
        return antwort

    def setze_pin(self, pin: str, pegel: int):
        self._befehl(f"pin {ws.pin_nummer(self.spec.plattform, pin)} {int(pegel)}")

    def setze_roh(self, pin: str, roh: int):
        self._befehl(f"roh {ws.pin_nummer(self.spec.plattform, pin)} {int(roh)}")

    def start(self):
        self._befehl("start")

    def lauf(self, ms: int):
        if ms > 0:
            self._befehl(f"lauf {int(ms)}")

    def zustand(self) -> dict:
        return _lies_zustand(self._befehl("zustand"))

    def ende(self) -> tuple[str, list]:
        try:
            self.proc.stdin.write("ende\n")
            self.proc.stdin.flush()
            self.proc.wait(timeout=10)
        except (BrokenPipeError, subprocess.TimeoutExpired):  # pragma: no cover
            self.proc.kill()
        finally:
            self.proc.stdin.close()
            self.proc.stdout.close()
        serial = self.serial.read_text(encoding="utf-8", errors="replace") if self.serial.exists() else ""
        spur = []
        if self.spurdatei.exists():
            for z in self.spurdatei.read_text(encoding="utf-8").splitlines():
                d = _lies_zustand(z)
                spur.append((d["T"], d))
        return serial, spur


def _lies_zustand(zeile: str) -> dict:
    d: dict = {}
    for teil in zeile.split():
        k, _, v = teil.partition("=")
        d[k] = float(v) if "." in v else int(v)
    return d


# ───────────────────────────── Testablauf ─────────────────────────────

@dataclass
class Pruefpunkt:
    schritt: int
    phase: str        # vorher | erwarte
    zeit: int
    schluessel: str
    soll: object
    ist: object

    @property
    def ok(self) -> bool:
        return self.ist == self.soll


@dataclass
class Ergebnis:
    test: ws.Testfall
    art: str
    punkte: list[Pruefpunkt] = field(default_factory=list)
    fehler: str = ""
    serial: str = ""
    spur: list = field(default_factory=list)
    ereignisse: list = field(default_factory=list)
    wokwi_hinweis: str = ""

    @property
    def ok(self) -> bool:
        return not self.fehler and all(p.ok for p in self.punkte)

    @property
    def bestanden(self) -> int:
        return sum(p.ok for p in self.punkte)


def _taster_gedrueckt(e: ws.Eingang, signal: int) -> int:
    return int(signal == 1) if e.kontakt == "NO" else int(signal == 0)


def fuehre_aus(spec: ws.Spec, test: ws.Testfall, sim) -> Ergebnis:
    erg = Ergebnis(test, sim.art)
    ids = wp.bauteil_ids(spec)
    zr = spec.zeitraffer
    t0 = 0
    hinweise: list[str] = []

    def ereignis(art, *daten):
        erg.ereignisse.append((jetzt(), art, *daten))

    def jetzt() -> int:
        return t0 + uhr[0]

    uhr = [0]

    def lauf(ms):
        ms = max(0, int(ms))
        sim.lauf(ms)
        uhr[0] += ms

    def signal(bmk, wert):
        e, a = spec.eingang(bmk), spec.analogwert(bmk)
        if e:
            sim.setze_pin(e.pin, int(wert))
            if e.bauteil == "taster":
                ereignis("control", ids[bmk], "pressed", _taster_gedrueckt(e, int(wert)))
            else:
                hinweise.append(f"{bmk} ist ein Schiebeschalter – in Wokwi-Szenarien nicht steuerbar")
        elif a:
            roh = ws.roh_aus_wert(spec, a, ws.zahl(wert))
            sim.setze_roh(a.pin, roh)
            ereignis("control", ids[bmk], "position", round(roh / spec.p["roh_vcc"], 4))

    def pruefe(ts, phase, erwartung):
        z = sim.zustand()
        for k, soll in erwartung.items():
            ist = z.get(k)
            soll_n = int(soll) if not isinstance(soll, float) else soll
            erg.punkte.append(Pruefpunkt(ts.nr, phase, z["T"], k, soll_n, ist))
            o = spec.ausgang(k)
            if o:
                ereignis("expect", ws.wokwi_pin(spec.plattform, o.pin), soll_n)

    try:
        for e in spec.eingaenge:
            w = int(test.start.get(e.bmk, e.start))
            sim.setze_pin(e.pin, w)
            if w != e.start:
                if e.bauteil == "taster":
                    raise SimFehler(f"{e.bmk}: Taster beginnt unbetätigt – mit „druecke“ im Ablauf betätigen")
                hinweise.append(f"{e.bmk} beginnt abweichend von diagram.json – in Wokwi von Hand einstellen")
        for a in spec.analog:
            w = ws.zahl(test.start.get(a.bmk, a.start))
            sim.setze_roh(a.pin, ws.roh_aus_wert(spec, a, w))
            if w != a.start:
                ereignis("control", ids[a.bmk], "position", round(ws.roh_aus_wert(spec, a, w) / spec.p["roh_vcc"], 4))
        sim.start()
        lauf(VORLAUF_MS)
        for ts in test.ablauf:
            aktion = False
            for k, v in ts.setze.items():
                signal(k, v)
                aktion = True
            for k in ts.druecke:
                signal(k, 1 if spec.eingang(k).kontakt == "NO" else 0)
                aktion = True
            for k in ts.loese:
                signal(k, 0 if spec.eingang(k).kontakt == "NO" else 1)
                aktion = True
            for k in ts.tippe:
                e = spec.eingang(k)
                signal(k, 1 if e.kontakt == "NO" else 0)
                lauf(TIPP_MS)
                signal(k, 0 if e.kontakt == "NO" else 1)
                aktion = True
            if ts.schrittzeit_ms is not None:
                if aktion:
                    lauf(NACH_MS)
                z = sim.zustand()
                schwelle = zr(ts.schrittzeit_ms)
                tol = TOL_MS
                ziel = z["W"] + schwelle
                if ts.vorher:
                    if ziel - tol <= z["T"]:
                        erg.punkte.append(Pruefpunkt(ts.nr, "vorher", z["T"], "Zeitfenster", "prüfbar",
                                                     "Schwelle bereits erreicht"))
                    else:
                        lauf(ziel - tol - z["T"])
                        pruefe(ts, "vorher", ts.vorher)
                lauf(ziel + tol - sim.zustand()["T"])
                pruefe(ts, "erwarte", ts.erwarte)
                continue
            if ts.warte_ms:
                lauf(zr(ts.warte_ms))
            elif aktion or ts.erwarte:
                lauf(NACH_MS)
            if ts.erwarte:
                pruefe(ts, "erwarte", ts.erwarte)
    except SimFehler as e:
        erg.fehler = str(e)
    finally:
        erg.serial, erg.spur = sim.ende()
    erg.wokwi_hinweis = "; ".join(dict.fromkeys(hinweise))
    return erg


def teste_alle(spec: ws.Spec, sketch_text: str | None = None, nur_logik: bool = False,
               arbeitsordner: Path | None = None) -> dict:
    """Alle Testfälle im Logikmodell und (mit g++) im Programm. Ergebnis-Mapping für Protokoll und CLI."""
    aus = {"logik": [], "programm": [], "programm_status": "", "warnungen": []}
    for t in spec.testfaelle:
        aus["logik"].append(fuehre_aus(spec, t, Logikmodell(spec)))
    if nur_logik:
        aus["programm_status"] = "nicht ausgeführt (--nur-logik)"
        return aus
    if sketch_text is None:
        sketch_text = wp.sketch(spec)
    try:
        ueb = uebersetze(spec, sketch_text, arbeitsordner)
    except SimFehler as e:
        aus["programm_status"] = str(e)
        return aus
    aus["warnungen"] = ueb.warnungen
    for t in spec.testfaelle:
        aus["programm"].append(fuehre_aus(spec, t, Hostprogramm(spec, ueb)))
    aus["programm_status"] = "übersetzt mit g++ (gnu++11, -Wall -Wextra)" + (
        f", {len(ueb.warnungen)} Warnungen" if ueb.warnungen else ", ohne Warnungen")
    if arbeitsordner is None:
        shutil.rmtree(ueb.ordner, ignore_errors=True)
    return aus


# ───────────────────────────── Szenarien ─────────────────────────────

def szenario(spec: ws.Spec, erg: Ergebnis) -> tuple[str, str] | None:
    """(Dateiname, YAML) des Wokwi-Szenarios aus dem Lauf des Logikmodells; None, wenn nicht steuerbar."""
    if erg.wokwi_hinweis:
        return None
    bid = spec.p["id"]
    schritte: list[dict] = [{"kommentar": f"{erg.test.nr} {erg.test.name}" + (f" – {erg.test.zweck}" if erg.test.zweck else "")},
                            {"wait-serial": "Bereit"}]
    t = 0
    for zeit, art, *daten in sorted(erg.ereignisse, key=lambda e: e[0]):
        if zeit > t:
            schritte.append({"delay": f"{zeit - t}ms"})
            t = zeit
        if art == "control":
            schritte.append({"set-control": {"part-id": daten[0], "name": daten[1], "value": daten[2]}})
        else:
            schritte.append({"expect-pin": {"part-id": bid, "name": daten[0], "value": daten[1]}})
    slug = re.sub(r"[^a-z0-9]+", "-", f"{erg.test.nr} {erg.test.name}".lower().replace("ä", "ae").replace(
        "ö", "oe").replace("ü", "ue").replace("ß", "ss")).strip("-")
    return f"szenarien/{slug}.test.yaml", wp.szenario_yaml(f"{erg.test.nr} {erg.test.name}", schritte)


def szenario_dauer(erg: Ergebnis) -> int:
    return max([e[0] for e in erg.ereignisse] + [0])


# ───────────────────────────── Protokoll ─────────────────────────────

def _anzeige(k, v) -> str:
    return f"X{v}" if k == "X" else f"{k} = {v}"


def protokoll(spec: ws.Spec, aus: dict, szenarien: dict[str, str] | None = None) -> str:
    """Markdown: Tabelle der Testfälle mit beiden Wegen, danach Abweichungen."""
    z = ["| Nr. | Testfall | Prüfpunkte | Logik (Spec) | Programm (g++) | Wokwi-Szenario |",
         "|---|---|---:|---|---|---|"]
    prog = {e.test.nr: e for e in aus["programm"]}
    for e in aus["logik"]:
        p = prog.get(e.test.nr)
        z1 = ("✅" if e.ok else "❌") + f" {e.bestanden}/{len(e.punkte)}" + (" – " + e.fehler if e.fehler else "")
        z2 = (("✅" if p.ok else "❌") + f" {p.bestanden}/{len(p.punkte)}" + (" – " + p.fehler if p.fehler else "")) \
            if p else "⚠️ nicht ausgeführt"
        sz = (szenarien or {}).get(e.test.nr)
        z3 = f"`{sz}`" if sz else (f"⚠️ entfällt ({e.wokwi_hinweis})" if e.wokwi_hinweis else "–")
        z.append(f"| {e.test.nr} | {e.test.name} | {len(e.punkte)} | {z1} | {z2} | {z3} |")
    abw = []
    for e in [*aus["logik"], *aus["programm"]]:
        for p in e.punkte:
            if not p.ok:
                abw.append(f"- {e.art}, {e.test.nr} Schritt {p.schritt} ({p.phase}, t = {p.zeit} ms): "
                           f"erwartet {_anzeige(p.schluessel, p.soll)}, ist {_anzeige(p.schluessel, p.ist)}")
    if abw:
        z += ["", "**Abweichungen:**", *abw]
    if not aus["programm"]:
        z += ["", f"Programm: {aus['programm_status']}"]
    return "\n".join(z) + "\n"


# ───────────────────────────── Zeitablauf ─────────────────────────────

def abschnitte(spec: ws.Spec, spur: list) -> list[tuple[int, int, dict]]:
    """Spur → Abschnitte (Beginn, Ende, Zustand); Ende des letzten = letzter Zeitpunkt."""
    if not spur:
        return []
    punkte = []
    for t, d in spur:
        if punkte and punkte[-1][0] == t:
            punkte[-1] = (t, d)
        else:
            punkte.append((t, d))
    ende = punkte[-1][0]
    aus = []
    for i, (t, d) in enumerate(punkte):
        t2 = punkte[i + 1][0] if i + 1 < len(punkte) else max(ende, t)
        aus.append((t, t2, d))
    return aus


def zeitablauf_svg(spec: ws.Spec, erg: Ergebnis, ziel: Path, ende_ms: int | None = None) -> list[tuple]:
    """Zustandsfolge als SVG (matplotlib): ein Feld je Abschnitt, darunter die Simulationszeit.
    Gibt die Abschnitte für die Wertetabelle zurück."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.patches import Rectangle
    except ImportError as e:  # pragma: no cover
        raise SimFehler("matplotlib fehlt – Zeitablauf nicht gezeichnet") from e
    plt.rcParams["svg.fonttype"] = "none"
    plt.rcParams["font.family"] = "DejaVu Sans"
    ab = abschnitte(spec, erg.spur)
    if ende_ms is not None and ab:
        t, _, d = ab[-1]
        ab[-1] = (t, max(t, ende_ms), d)
    zeilen = [("Schritt", "X")] + [(e.bmk, e.bmk) for e in spec.eingaenge] + \
             [(a.bmk, a.bmk) for a in spec.analog] + [(o.bmk, o.bmk) for o in spec.ausgaenge] + \
             [(m.name, m.name) for m in spec.merker if m.typ == "bool"]
    n = len(ab)
    breite = max(6.0, 1.15 * n + 2.2)
    hoehe = 0.42 * len(zeilen) + 1.3
    fig, ax = plt.subplots(figsize=(breite, hoehe))
    for i, (titel, schl) in enumerate(zeilen):
        y = -i
        ax.text(-0.15, y, titel, ha="right", va="center", fontsize=9, family="DejaVu Sans")
        an = spec.analogwert(schl)
        for j, (_, _, d) in enumerate(ab):
            w = d.get(schl)
            if schl == "X":
                ax.add_patch(Rectangle((j + 0.04, y - 0.32), 0.92, 0.64, fill=False, lw=1.0, ec="black"))
                ax.text(j + 0.5, y, f"X{w}", ha="center", va="center", fontsize=9)
            elif an:
                ax.text(j + 0.5, y, f"{w:.{an.stellen}f}".replace(".", ","), ha="center", va="center", fontsize=8)
            else:
                ax.plot([j, j + 1], [y - 0.3, y - 0.3], color="black", lw=0.6)
                if w:
                    ax.add_patch(Rectangle((j, y - 0.3), 1, 0.6, color="0.25", lw=0))
        if an:
            ax.text(n + 0.1, y, an.einheit, ha="left", va="center", fontsize=8)
    for j in range(n + 1):
        ax.plot([j, j], [0.45, -len(zeilen) + 0.55], color="0.6", lw=0.5, ls=":")
    y_zeit = -len(zeilen) + 0.15
    for j, (t1, t2, _) in enumerate(ab):
        ax.text(j + 0.5, y_zeit, f"{t1 / 1000:.1f}".replace(".", ","), ha="center", va="center", fontsize=7.5)
        ax.text(j + 0.5, y_zeit - 0.38, ws.dauer_text(t2 - t1) if t2 > t1 else "–", ha="center", va="center",
                fontsize=7.5, style="italic")
    ax.text(-0.15, y_zeit, "Beginn in s", ha="right", va="center", fontsize=8)
    ax.text(-0.15, y_zeit - 0.38, "Dauer", ha="right", va="center", fontsize=8, style="italic")
    zr = spec.zeitraffer
    ax.set_title(f"{erg.test.nr} {erg.test.name} – Zustandsfolge der Simulation"
                 + (f" (Simulationszeit, Zeitraffer 1:{zr.faktor} ab {ws.dauer_text(zr.ab_ms)})" if zr.faktor > 1 else ""),
                 fontsize=10, loc="left")
    ax.set_xlim(-2.2, n + 0.8)
    ax.set_ylim(y_zeit - 0.7, 0.7)
    ax.axis("off")
    fig.tight_layout()
    ziel.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(ziel, format="svg")
    plt.close(fig)
    return ab


def wertetabelle(spec: ws.Spec, ab: list[tuple]) -> str:
    z = ["| Abschnitt | Beginn in s | Dauer | Schritt | Signale = 1 | Analogwerte |", "|---:|---:|---|---|---|---|"]
    for j, (t1, t2, d) in enumerate(ab, 1):
        an = " ".join(f"{a.bmk} {d.get(a.bmk, 0):.{a.stellen}f} {a.einheit}".replace(".", ",") for a in spec.analog)
        eins = ", ".join(k for k in [*(e.bmk for e in spec.eingaenge), *(o.bmk for o in spec.ausgaenge),
                                     *(m.name for m in spec.merker if m.typ == "bool")] if d.get(k))
        beginn = f"{t1 / 1000:.1f}".replace(".", ",")
        z.append(f"| {j} | {beginn} | {ws.dauer_text(t2 - t1) if t2 > t1 else '–'} | X{d['X']} | "
                 f"{eins or '–'} | {an or '–'} |")
    return "\n".join(z) + "\n"
