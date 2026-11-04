#!/usr/bin/env python3
"""wokwi_vorschau – diagram.json mit den echten Wokwi-Bauteilen ansehen und die Pinnamen prüfen.

Lädt @wokwi/elements (MIT-Lizenz, von unpkg.com) in Chromium ohne Fenster, setzt die Bauteile an ihre
Koordinaten, zeichnet die Leitungen entlang der Wegpunkte und meldet
  - Pins, die das Bauteil nicht hat (Name aus pinInfo des Bauteils),
  - Leitungen, deren letztes Stück schräg zum Ziel-Pin läuft.
Bild als PNG nur zur Sichtprüfung (Lage, Beschriftungen), nicht für Material. Board-Typen außerhalb von
@wokwi/elements (ESP32-Board) werden als Rahmen gezeigt; ihre Pins prüft die Vorschau nicht.
Braucht Chromium und Netz; sonst Exit-Code 2.
"""

from __future__ import annotations

import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

ELEMENTS = "https://unpkg.com/@wokwi/elements@1.9.2/dist/wokwi-elements.bundle.min.js"

_SEITE = """<!doctype html><meta charset=utf-8>
<script src="%(src)s"></script>
<style>body{margin:0;background:#fff;font:12px sans-serif} #f{position:relative;width:%(b)dpx;height:%(h)dpx}
.t{position:absolute;white-space:pre;font:13px monospace;color:#333} .p{position:absolute}
.board{position:absolute;border:2px dashed #888;width:110px;height:260px;font:11px sans-serif;color:#555}</style>
<div id=f></div><pre id=log></pre>
<script>
const D = %(d)s; const OX=%(ox)d, OY=%(oy)d; const f=document.getElementById('f'); const el={};
const log=[];
if (!window.customElements || !customElements.get('wokwi-led')) log.push('BIBLIOTHEK FEHLT');
for (const p of D.parts) {
  if (p.type==='wokwi-text') { const t=document.createElement('div'); t.className='t'; t.textContent=p.attrs.text;
    t.style.left=(OX+p.left)+'px'; t.style.top=(OY+p.top)+'px'; f.appendChild(t); continue; }
  if (!customElements.get(p.type)) { const b=document.createElement('div'); b.className='board'; b.textContent=p.type;
    b.style.left=(OX+p.left)+'px'; b.style.top=(OY+p.top)+'px'; f.appendChild(b); continue; }
  const e=document.createElement(p.type); e.className='p';
  for (const [k,v] of Object.entries(p.attrs||{})) e.setAttribute(k,v);
  if (p.type==='wokwi-slide-switch') e.value = (p.attrs||{}).value==='1'?1:0;
  e.style.left=(OX+p.left)+'px'; e.style.top=(OY+p.top)+'px';
  if (p.rotate) e.style.transform='rotate('+p.rotate+'deg)';
  f.appendChild(e); el[p.id]=[e,p];
}
setTimeout(()=>{
  const svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
  svg.setAttribute('width',%(b)d); svg.setAttribute('height',%(h)d);
  svg.style.position='absolute'; svg.style.left=0; svg.style.top=0; f.appendChild(svg);
  function pos(end){ const [id,pin]=end.split(':'); if(!el[id]) return null;
    const [e,p]=el[id]; const info=(e.pinInfo||[]).find(x=>x.name===pin);
    if(!info){ log.push('PIN FEHLT '+end+' (vorhanden: '+(e.pinInfo||[]).map(x=>x.name).join(',')+')'); return null; }
    const r=e.getBoundingClientRect(); const w=e.offsetWidth, h=e.offsetHeight; const x=info.x-w/2, y=info.y-h/2;
    const a=(p.rotate||0)*Math.PI/180;
    return [r.left+r.width/2+x*Math.cos(a)-y*Math.sin(a), r.top+r.height/2+x*Math.sin(a)+y*Math.cos(a)]; }
  for (const c of D.connections) {
    if (c[0].startsWith('$')||c[1].startsWith('$')) continue;
    const a=pos(c[0]), b=pos(c[1]); if(!a||!b) continue;
    let x=a[0], y=a[1]; const pts=[[x,y]];
    for (const h of c[3]) { if (h==='*') break; const v=parseFloat(h.slice(1)); if (h[0]==='h') x+=v; else y+=v; pts.push([x,y]); }
    pts.push(b);
    if (c[3].length && Math.abs(x-b[0])>0.6 && Math.abs(y-b[1])>0.6) log.push('SCHRÄG '+c[0]+' -> '+c[1]);
    const l=document.createElementNS('http://www.w3.org/2000/svg','polyline');
    l.setAttribute('points', pts.map(p=>p.join(',')).join(' ')); l.setAttribute('fill','none');
    l.setAttribute('stroke',c[2]||'gray'); l.setAttribute('stroke-width',2); l.setAttribute('opacity',0.85);
    svg.appendChild(l); }
  document.getElementById('log').textContent = 'VORSCHAU ' + (log.length ? log.join(' | ') : 'OK');
}, 1500);
</script>"""


def chromium() -> str | None:
    return next((p for p in (shutil.which(n) for n in ("chromium", "chromium-browser", "google-chrome")) if p), None)


def seite(diagramm: dict) -> tuple[str, int, int]:
    xs = [p.get("left", 0) for p in diagramm["parts"]]
    ys = [p.get("top", 0) for p in diagramm["parts"]]
    ox, oy = int(60 - min(xs)), int(60 - min(ys))
    b, h = int(max(xs) - min(xs) + 400), int(max(ys) - min(ys) + 260)
    text = _SEITE % {"src": ELEMENTS, "d": json.dumps(diagramm), "ox": ox, "oy": oy, "b": b, "h": h}
    return text, b, h


def vorschau(diagramm: dict, png: Path | None) -> tuple[int, str]:
    """(Exit-Code, Meldung). 0 = Pins vorhanden, keine schräge Leitung; 1 = Befund; 2 = nicht prüfbar."""
    browser = chromium()
    if not browser:
        return 2, "Chromium nicht gefunden – Vorschau nicht erstellt"
    text, b, h = seite(diagramm)
    with tempfile.TemporaryDirectory(prefix="wokwi_vorschau_") as tmp:
        datei = Path(tmp) / "vorschau.html"
        datei.write_text(text, encoding="utf-8")
        basis = [browser, "--headless=new", "--disable-gpu", "--no-sandbox", "--virtual-time-budget=6000",
                 f"--window-size={b},{h + 40}"]
        try:
            r = subprocess.run(basis + ["--dump-dom", datei.as_uri()], capture_output=True, text=True, timeout=90)
        except subprocess.TimeoutExpired:
            return 2, "Chromium antwortet nicht – Vorschau nicht erstellt"
        m = re.search(r"<pre id=\"log\">(.*?)</pre>", r.stdout, re.S)
        meldung = html.unescape(m.group(1)) if m else ""
        if not meldung or "BIBLIOTHEK FEHLT" in meldung:
            return 2, "@wokwi/elements nicht geladen (Netz?) – Vorschau nicht erstellt"
        if png:
            png.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(basis + [f"--screenshot={png}", datei.as_uri()], capture_output=True, timeout=90)
    befund = meldung.removeprefix("VORSCHAU ").strip()
    return (0 if befund == "OK" else 1), befund
