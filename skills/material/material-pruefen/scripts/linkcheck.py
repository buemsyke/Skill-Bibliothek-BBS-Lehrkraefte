#!/usr/bin/env python3
"""linkcheck – externe Links in Unterrichtsmaterial prüfen (ohne Zusatzpakete).

Liest Dateien oder Ordner (.md, .txt, .html, .docx, .pptx, .odt, .odp, .pdf), sammelt alle
http(s)-Links, prüft jede URL genau einmal und ordnet ein:

  ok            HTTP 2xx, keine Auffälligkeit
  umgeleitet    Weiterleitung auf dieselbe Domain (Link ggf. aktualisieren)
  verdächtig    Weiterleitung auf andere Domain, Soft-404 im Seitentitel, nur http://
  gesperrt      401/403/429 – Login, Paywall oder Bot-Sperre: von Hand prüfen
  tot           HTTP ≥ 400 (außer gesperrt) oder Verbindungsfehler

Aufruf:
    python3 linkcheck.py material.md [ordner/ …] [--json] [--timeout 10] [--worker 6] [--streng]

    --streng   Exit-Code 1, wenn mindestens ein Link tot ist (für Automatisierung)

PDF: Link-Annotationen über `pdfinfo -url` (poppler), dazu URLs, die nur als Text dastehen
(`pdftotext`; am Zeilenende umbrochene URLs werden zusammengefügt). Ohne poppler: Hinweis.
URLs mit Umlauten (IRI) werden vor dem Abruf kodiert.

Hinweis: In Umgebungen ohne Internetzugang schlagen alle Prüfungen fehl; das Skript erkennt
das und meldet „Netz nicht verfügbar" statt alle Links als tot zu markieren.
Angelehnt an eduwerkzeuge.linkcheck (edu-linkcheck), aber eigenständig lauffähig.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote, urlsplit, urlunsplit

USER_AGENT = "Mozilla/5.0 (compatible; unterrichtsmaterial-linkcheck/1.0; Lehrkraft prüft Material)"
MAX_LESEBYTES = 65536
ENDUNGEN_TEXT = {".md", ".markdown", ".txt", ".html", ".htm"}
ENDUNGEN_ZIP = {".docx", ".pptx", ".odt", ".odp", ".xlsx", ".ods"}
ENDUNGEN_PDF = {".pdf"}

URL_RE = re.compile(r"https?://[^\s<>\[\]\"'()`|]+")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\((https?://[^\s)]+)(?:\s+\"[^\"]*\")?\)")
TITEL_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
SOFT404_RE = re.compile(
    r"\b404\b|nicht gefunden|not found|seite existiert nicht|page (?:does not|doesn't) exist|"
    r"domain (?:is )?for sale|diese domain|parked|fehlerseite", re.IGNORECASE)
SATZZEICHEN_ENDE = ".,;:!?)\"'`”“»›*_"


def _saeubere(url: str) -> str:
    url = url.rstrip(SATZZEICHEN_ENDE)
    while url.endswith(")") and url.count("(") < url.count(")"):
        url = url[:-1]
    return url


def _iri_zu_uri(url: str) -> str:
    """URL mit Umlauten oder Leerzeichen (IRI) in eine abrufbare ASCII-URL umwandeln."""
    try:
        teile = urlsplit(url)
        host = teile.hostname or ""
        try:
            host = host.encode("idna").decode("ascii")
        except UnicodeError:
            pass
        netloc = host + (f":{teile.port}" if teile.port else "")
        if teile.username:
            netloc = f"{teile.username}@{netloc}"
    except ValueError:
        return url
    return urlunsplit((teile.scheme, netloc,
                       quote(teile.path, safe="/%:@!$&'()*+,;=~-._"),
                       quote(teile.query, safe="=&%:@!$'()*+,;/?~-._"),
                       quote(teile.fragment, safe="=&%:@!$'()*+,;/?~-._")))


def _pdf_links(pfad: Path) -> list[tuple[str, str]]:
    """(Fundstelle, URL) aus einem PDF: Link-Annotationen und URLs, die nur als Text dastehen."""
    if not shutil.which("pdftotext"):
        print(f"Hinweis: poppler (pdftotext, pdfinfo) fehlt – PDF nicht geprüft: {pfad.name}",
              file=sys.stderr)
        return []
    links: list[tuple[str, str]] = []
    annotationen: list[str] = []
    if shutil.which("pdfinfo"):
        aus = subprocess.run(["pdfinfo", "-url", str(pfad)], capture_output=True, text=True,
                             errors="replace").stdout
        for zeile in aus.splitlines():
            m = re.match(r"\s*(\d+)\s+\S+\s+(https?://\S+)", zeile)
            if m:
                annotationen.append(m.group(2))
                links.append((f"S. {m.group(1)}", m.group(2)))
    text = subprocess.run(["pdftotext", "-layout", str(pfad), "-"], capture_output=True,
                          text=True, errors="replace").stdout
    for seite, seitentext in enumerate(text.split("\f"), 1):
        zeilen = seitentext.splitlines()
        for i, zeile in enumerate(zeilen):
            for m in URL_RE.finditer(zeile):
                url = _saeubere(m.group(0))
                # am Zeilenende umbrochen? Fortsetzung aus der nächsten Zeile anhängen
                if m.end() >= len(zeile.rstrip()) and i + 1 < len(zeilen):
                    fort = re.match(r"\s*([\w./%?=&#~+:;-]+)", zeilen[i + 1])
                    if fort:
                        kandidat = _saeubere(url + fort.group(1))
                        if url.endswith("-") or any(a.startswith(kandidat) for a in annotationen):
                            url = kandidat
                if any(a == url or a.startswith(url) for a in annotationen):
                    continue  # schon als Annotation erfasst
                links.append((f"S. {seite} (nur Text, nicht verlinkt)", url))
    return links


def texte_aus_datei(pfad: Path) -> list[tuple[int | str, str]]:
    """(Zeilennummer bzw. Fundstelle, Text); bei Office-Dateien Zeilennummer 0."""
    endung = pfad.suffix.lower()
    if endung in ENDUNGEN_PDF:
        return [(stelle, url) for stelle, url in _pdf_links(pfad)]
    if endung in ENDUNGEN_TEXT:
        return list(enumerate(pfad.read_text(encoding="utf-8", errors="replace").splitlines(), 1))
    if endung in ENDUNGEN_ZIP:
        texte: list[tuple[int, str]] = []
        with zipfile.ZipFile(pfad) as z:
            for name in z.namelist():
                if not name.endswith((".xml", ".rels")):
                    continue
                roh = z.read(name).decode("utf-8", errors="replace").replace("&amp;", "&")
                # Hyperlinks: Office-Beziehungen (Target=…) und ODF (xlink:href=…)
                ziele = re.findall(r'(?:Target|xlink:href)="(https?://[^"]+)"', roh)
                # sichtbarer Text ohne Tags – so fallen XML-Namensräume weg
                sichtbar = re.sub(r"<[^>]+>", " ", roh) if name.endswith(".xml") else ""
                texte.append((0, " ".join(ziele) + " " + sichtbar))
        return texte
    return []


def _anzeigename(datei: Path) -> str:
    """Dateiname, der sich immer ausgeben lässt – auch bei kaputten Umlauten aus ZIP-Archiven
    (Bytes, die kein UTF-8 sind, erscheinen als �)."""
    return datei.name.encode("utf-8", "surrogateescape").decode("utf-8", "replace")


def sammle_links(pfade: list[Path]) -> dict[str, list[str]]:
    gefunden: dict[str, list[str]] = {}
    dateien: list[Path] = []
    for p in pfade:
        if p.is_dir():
            dateien += sorted(f for f in p.rglob("*")
                              if f.suffix.lower() in ENDUNGEN_TEXT | ENDUNGEN_ZIP | ENDUNGEN_PDF)
        elif p.is_file():
            dateien.append(p)
        else:
            print(f"nicht gefunden: {p}", file=sys.stderr)
    for datei in dateien:
        for nr, text in texte_aus_datei(datei):
            urls = [m.group(1) for m in MD_LINK_RE.finditer(text)] + URL_RE.findall(text)
            for url in urls:
                url = _saeubere(url)
                name = _anzeigename(datei)
                stelle = f"{name}:{nr}" if nr else name
                liste = gefunden.setdefault(url, [])
                if stelle not in liste:
                    liste.append(stelle)
    return gefunden


def pruefe(url: str, timeout: float) -> dict:
    req = urllib.request.Request(_iri_zu_uri(url), headers={"User-Agent": USER_AGENT,
                                               "Accept": "text/html,application/xhtml+xml,*/*"})
    ergebnis: dict = {"url": url, "status": None, "endziel": None, "titel": None, "fehler": None,
                      "typ": None}
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ergebnis["status"] = resp.status
            ergebnis["endziel"] = resp.geturl()
            ergebnis["typ"] = resp.headers.get_content_type()
            roh = resp.read(MAX_LESEBYTES)
    except urllib.error.HTTPError as e:
        ergebnis["status"] = e.code
        ergebnis["endziel"] = e.geturl() or url
        roh = b""
    except (urllib.error.URLError, TimeoutError, OSError, ValueError) as e:
        ergebnis["fehler"] = str(getattr(e, "reason", e))
        return ergebnis
    if roh and (ergebnis["typ"] or "").startswith("text/html"):
        m = TITEL_RE.search(roh.decode("utf-8", errors="replace"))
        if m:
            ergebnis["titel"] = re.sub(r"\s+", " ", m.group(1)).strip()[:120]
    return ergebnis


def einordnen(e: dict) -> tuple[str, str]:
    if e["fehler"]:
        if "timed out" in e["fehler"].lower():
            return "tot", "Zeitüberschreitung – Server antwortet nicht; später erneut prüfen"
        return "tot", f"Verbindungsfehler: {e['fehler']}"
    s = e["status"] or 0
    if s in (401, 403, 429):
        return "gesperrt", f"HTTP {s} – Login, Paywall oder Bot-Sperre; im Browser prüfen"
    if s >= 400:
        return "tot", f"HTTP {s}"
    hinweise = []
    start, ziel = urlsplit(e["url"]), urlsplit(e["endziel"] or e["url"])
    host = lambda h: (h or "").lower().removeprefix("www.")
    if e["titel"] and SOFT404_RE.search(e["titel"]):
        return "verdächtig", f"Seitentitel deutet auf Fehlerseite: „{e['titel']}“"
    if host(start.hostname) != host(ziel.hostname):
        return "verdächtig", f"leitet auf andere Domain um: {e['endziel']}"
    if start.scheme == "http" and ziel.scheme == "http":
        hinweise.append("nur unverschlüsselt (http)")
    if e["endziel"] and e["endziel"].rstrip("/") != e["url"].rstrip("/"):
        return "umgeleitet", f"neues Ziel: {e['endziel']}" + (f"; {hinweise[0]}" if hinweise else "")
    if hinweise:
        return "verdächtig", hinweise[0]
    return "ok", e["titel"] or (e["typ"] or "")


SYMBOL = {"ok": "✅", "umgeleitet": "↪️", "verdächtig": "⚠️", "gesperrt": "🔒", "tot": "❌"}
REIHENFOLGE = ["tot", "verdächtig", "gesperrt", "umgeleitet", "ok"]


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Externe Links in Material prüfen.")
    p.add_argument("pfade", nargs="+", type=Path)
    p.add_argument("--json", action="store_true")
    p.add_argument("--timeout", type=float, default=10.0)
    p.add_argument("--worker", type=int, default=6)
    p.add_argument("--streng", action="store_true", help="Exit-Code 1 bei toten Links")
    args = p.parse_args(argv)

    links = sammle_links(args.pfade)
    if not links:
        print("Keine externen Links gefunden.")
        return 0
    with ThreadPoolExecutor(max_workers=max(1, args.worker)) as pool:
        roh = list(pool.map(lambda u: pruefe(u, args.timeout), links))

    netz_weg = all(r["fehler"] for r in roh) and len(roh) > 1
    eintraege = []
    for r in roh:
        klasse, hinweis = einordnen(r)
        if klasse == "tot" and r["url"].endswith("-"):
            hinweis += " – endet auf Bindestrich: Link im Dokument vermutlich abgeschnitten (umbrochen)"
        if netz_weg:
            klasse, hinweis = "nicht geprüft", "Netz nicht verfügbar"
        eintraege.append({**r, "klasse": klasse, "hinweis": hinweis, "fundstellen": links[r["url"]]})

    if args.json:
        print(json.dumps({"netz_verfuegbar": not netz_weg, "links": eintraege},
                         ensure_ascii=False, indent=2))
    else:
        if netz_weg:
            print("**Netz nicht verfügbar** – kein Link konnte abgerufen werden. Linkcheck in einer "
                  "Umgebung mit Internetzugang wiederholen oder Links von Hand prüfen.\n")
        zaehler = {k: sum(1 for e in eintraege if e["klasse"] == k) for k in REIHENFOLGE}
        print("| Status | URL | Hinweis | Fundstelle(n) |")
        print("|---|---|---|---|")
        for e in sorted(eintraege, key=lambda x: (REIHENFOLGE.index(x["klasse"])
                                                  if x["klasse"] in REIHENFOLGE else 9, x["url"])):
            sym = SYMBOL.get(e["klasse"], "–")
            print(f"| {sym} {e['klasse']} | {e['url']} | {e['hinweis']} | {', '.join(e['fundstellen'])} |")
        print()
        print("Zusammenfassung: " + " · ".join(f"{SYMBOL[k]} {k}: {n}" for k, n in zaehler.items()))
        print("\n_Technischer Check. Ob die Seite inhaltlich noch passt (Inhalt, Aktualität, "
              "Werbung, Datenschutz, Lizenz), muss zusätzlich geprüft werden._")
    tote = sum(1 for e in eintraege if e["klasse"] == "tot")
    return 1 if (args.streng and tote) else 0


if __name__ == "__main__":
    sys.exit(main())
