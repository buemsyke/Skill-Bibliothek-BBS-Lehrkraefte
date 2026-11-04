#!/usr/bin/env python3
"""engine_pruefen – Schaltung in der echten Falstad-Engine (Chromium ohne Fenster) messen.

Lädt die Schaltung in ``circuitjs.html`` (Projektordner ``falstad/``), lässt sie simulieren und liest
über die JavaScript-Schnittstelle (``CircuitJS1.getElements()``) für **jedes Element** Mittelwert,
Effektivwert, Maximum und Minimum von Spannung und Strom. Das ist die Wahrheit für Dioden,
Transistoren und Schaltvorgänge, die ``falstad_kern.rechne`` nicht berechnet.

Voraussetzungen: ``chromium`` (oder ``chromium-browser``, ``google-chrome``) und die installierte
Falstad-Webversion (``setup.sh`` des Simulationsprojekts). Fehlt etwas, meldet das Skript es und
beendet sich mit Code 2 – die Prüfung ist dann **nicht** bestanden, sondern nur nicht ausgeführt.
"""

from __future__ import annotations

import functools
import http.server
import json
import os
import re
import shutil
import subprocess
import tempfile
import threading
import urllib.parse
from pathlib import Path

PRUEFSEITE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>pruefseite</title></head>
<body><pre id="out">warte</pre><iframe id="f" style="width:900px;height:600px"></iframe>
<script>
const q = new URLSearchParams(location.search);
const settle = parseFloat(q.get('settle') || '0.05');
const win = parseFloat(q.get('win') || '0.04');
const f = document.getElementById('f');
f.src = 'falstad/circuitjs.html?cct=' + encodeURIComponent(q.get('cct') || '') +
  '&euroResistors=true&whiteBackground=true&conventionalCurrent=true&running=true';
const out = document.getElementById('out');
let acc = null, t0 = null, fertig = false;
const wait = setInterval(function () {
  const sim = f.contentWindow && f.contentWindow.CircuitJS1;
  if (!sim || !sim.getElements) return;
  clearInterval(wait);
  sim.ontimestep = function (s) {
    if (fertig) return;
    const t = s.getTime();
    if (t < settle) return;
    const els = s.getElements();
    if (acc === null) { t0 = t; acc = els.map(() => ({n: 0, v: 0, v2: 0, i: 0, i2: 0, vmax: -1e99, vmin: 1e99, imax: -1e99, imin: 1e99})); }
    els.forEach((e, k) => {
      const a = acc[k], v = e.getVoltageDiff(), i = e.getCurrent();
      a.n++; a.v += v; a.v2 += v * v; a.i += i; a.i2 += i * i;
      a.vmax = Math.max(a.vmax, v); a.vmin = Math.min(a.vmin, v); a.imax = Math.max(a.imax, i); a.imin = Math.min(a.imin, i);
    });
    if (t - t0 >= win) {
      fertig = true; s.setSimRunning(false);
      const res = acc.map((a, k) => ({k: k, typ: els[k].getType(), vm: a.v / a.n, vrms: Math.sqrt(a.v2 / a.n),
        vmax: a.vmax, vmin: a.vmin, im: a.i / a.n, irms: Math.sqrt(a.i2 / a.n), imax: a.imax, imin: a.imin,
        info: String(els[k].getInfo())}));
      out.textContent = JSON.stringify({t: t, schritte: acc[0].n, elemente: res});
    }
  };
}, 50);
</script></body></html>
"""

class EngineFehler(Exception):
    pass


def finde_falstad(pfad: str | None = None) -> Path:
    """Ordner mit circuitjs.html: Argument, $FALSTAD_DIR, ./falstad (aufwärts)."""
    kandidaten = []
    if pfad:
        kandidaten.append(Path(pfad))
    if os.environ.get("FALSTAD_DIR"):
        kandidaten.append(Path(os.environ["FALSTAD_DIR"]))
    aktuell = Path.cwd()
    for ordner in [aktuell, *aktuell.parents]:
        kandidaten += [ordner / "falstad", ordner]
    for k in kandidaten:
        if (k / "circuitjs.html").is_file():
            return k.resolve()
    raise EngineFehler("Falstad-Webversion nicht gefunden (Ordner mit circuitjs.html). "
                       "Pfad mit --falstad angeben oder FALSTAD_DIR setzen; Installation: setup.sh im Simulationsprojekt.")


def finde_chromium() -> str:
    for name in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable"):
        p = shutil.which(name)
        if p:
            return p
    raise EngineFehler("Chromium nicht gefunden (chromium, chromium-browser oder google-chrome installieren)")


class _Leise(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args) -> None:  # noqa: D401
        pass


def messe(text: str, *, falstad: str | None = None, dauer: float = 0.1, fenster: float = 0.04,
          timeout: int = 240) -> dict:
    """Simuliert ``dauer`` s und mittelt danach ``fenster`` s; liefert {'t', 'schritte', 'elemente': [...]}

    Ein Chromium-Lauf bricht gelegentlich ab (langsame Rechner); deshalb ein zweiter Versuch.
    """
    try:
        return _messe_einmal(text, falstad, dauer, fenster, timeout)
    except EngineFehler as e:
        if "abgebrochen" not in str(e):
            raise
        return _messe_einmal(text, falstad, dauer, fenster, timeout)


def _messe_einmal(text: str, falstad, dauer: float, fenster: float, timeout: int) -> dict:
    ordner = finde_falstad(falstad)
    chrom = finde_chromium()
    with tempfile.TemporaryDirectory(prefix="cjs_") as tmp:
        wurzel = Path(tmp)
        (wurzel / "falstad").symlink_to(ordner, target_is_directory=True)
        (wurzel / "pruefseite.html").write_text(PRUEFSEITE, encoding="utf-8")
        handler = functools.partial(_Leise, directory=str(wurzel))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        port = server.server_address[1]
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            url = (f"http://127.0.0.1:{port}/pruefseite.html?cct={urllib.parse.quote(text)}"
                   f"&settle={dauer}&win={fenster}")
            budget = int(60000 + 80000 * (dauer + fenster))
            cmd = [chrom, "--headless=new", "--no-sandbox", "--disable-gpu", "--disable-extensions",
                   f"--user-data-dir={wurzel / 'profil'}", f"--virtual-time-budget={budget}", "--dump-dom", url]
            try:
                lauf = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            except subprocess.TimeoutExpired as e:
                raise EngineFehler(f"Chromium nach {timeout} s abgebrochen") from e
        finally:
            server.shutdown()
            server.server_close()
    m = re.search(r'<pre id="out">(.*?)</pre>', lauf.stdout, re.S)
    if not m:
        raise EngineFehler("Keine Ausgabe der Prüfseite (Chromium-Start fehlgeschlagen?)")
    roh = m.group(1).replace("&quot;", '"').replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    if roh.strip() == "warte":
        raise EngineFehler("Engine lieferte kein Ergebnis – Simulation zu kurz oder Schaltung wird nicht berechnet "
                           "(Singuläre Matrix?); Dauer erhöhen oder Schaltung prüfen")
    try:
        return json.loads(roh)
    except json.JSONDecodeError as e:
        raise EngineFehler(f"Ergebnis nicht lesbar: {roh[:120]}") from e


def anzeige(elem: dict, art: str, modus: int) -> float:
    """Wert, den ein Messgerät zeigt: Modus 1 Effektivwert, 2 Spitzenwert, sonst Mittelwert (Gleichwert)."""
    pre = "v" if art == "V" else "i"
    if modus == 1:
        return elem[pre + "rms"]
    if modus == 2:
        return elem[pre + "max"]
    return elem[pre + "m"]


def vergleiche(vorlage, ergebnis: dict) -> list:
    """Erwartungswerte einer Vorlage gegen die Engine: Liste (name, erwartet, engine, ok)."""
    ms = {m.name: m for m in vorlage.bau.messstellen}
    elemente = ergebnis["elemente"]
    zeilen = []
    skala = {"A": 0.0, "V": 0.0}
    for e in vorlage.erwartung:
        m = ms[e.name]
        skala[m.art] = max(skala[m.art], abs(e.wert))
    for e in vorlage.erwartung:
        m = ms[e.name]
        ist = anzeige(elemente[m.element], m.art, m.modus)
        absol = 2e-3 * skala[m.art] if skala[m.art] else 1e-6
        ok = abs(ist - e.wert) <= e.toleranz * abs(e.wert) + absol
        zeilen.append((e.name, e.wert, ist, e.einheit, ok))
    return zeilen
