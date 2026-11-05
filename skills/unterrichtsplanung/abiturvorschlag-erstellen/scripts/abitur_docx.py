#!/usr/bin/env python3
"""abitur_docx – Schüler- und Lehrermaterial eines Abiturvorschlags von Markdown nach Word (DOCX),
in der Dokumentvorlage der Behörde und mit den Abbildungen an der richtigen Stelle.

Die Vorlage liefert Seitenformat, Kopf- und Fußzeile; das Skript ersetzt ihren Textkörper durch den
Inhalt der Markdown-Datei (Aufgaben und Teilaufgaben mit BE rechtsbündig, Tabellen mit Rahmen,
Erwartungshorizont im Tabellenlayout der Vorlage, Listen, Code in Festbreitenschrift, Seitenumbruch
vor Erwartungshorizont und Musterlösung) und füllt Kopf- und Fußzeile aus dem Dateikopf
(Prüfungsjahr, Fach und Schwerpunkt, Vorschlag, Niveau, Bearbeitungszeit, Schule). Die Kopftabelle
der Markdown-Datei entfällt, weil die Kopfzeile sie trägt. Metadaten der Vorlage (Autor, letzte
Bearbeitung) werden ersetzt.

Abbildungen – in dieser Reihenfolge:
1. `![Abbildung 1: Titel](abbildungen/datei.svg)` steht genau dort; eine folgende kursive Zeile
   `*Abbildung 1: …*` ist die Bildunterschrift, sonst der Alternativtext. `{width=80%}` bzw.
   `{width=12cm}` hinter der Klammer legt die Breite fest (Standard: Satzspiegelbreite, höchstens
   natürliche Größe).
2. Eine Platzhalterzeile `[Abbildung 1: …]` (Vorlage des Skills) wird durch die Datei
   `<Dateianfang>_abb1_….svg` ersetzt.
3. Nicht eingebundene Dateien `<Dateianfang>_abbN_*.svg|png|jpg` im Ordner abbildungen/ neben der
   Markdown-Datei setzt das Skript ins Schülermaterial nach dem Absatz, der „Abbildung N“ zuerst
   erwähnt (Hinweise vor Teil A ausgenommen). Endet der Absatz mit „:“, kommt das Bild nach der
   folgenden Tabelle bzw. Liste; „Abbildung N in Anlage M“ setzt es ans Ende der Anlage M.
   Lösungsbilder `<Dateianfang>_loesung_X-Y_*` kommen ins Lehrermaterial vor die Merkmaltabelle der
   Teilaufgabe X.Y. Jede automatische Platzierung wird gemeldet.
SVG wird als SVG eingebettet (Word ab 2016) und mit rsvg-convert zusätzlich als PNG-Ersatzbild
(LibreOffice, ältere Word-Versionen); die Bildunterschrift stammt dann aus dem <title> der SVG-Datei,
der Alternativtext aus <desc>.

Aufruf:
    python3 abitur_docx.py 75_…_A_schuelermaterial.md 75_…_A_lehrermaterial.md \\
        --vorlage ORDNER_ODER_DOCX [--schule "BBS Musterstadt"] [--ueberschreiben]

--seiten zählt danach die Seiten der Word-Fassung (LibreOffice `soffice` und `pdftotext`, optional):
Schülermaterial bis „B. Material“ bzw. zur ersten Anlage – Richtwert höchstens 12 Seiten, Anlagen
zusätzlich; fehlt LibreOffice, meldet das Skript die Zählung als nicht ausgeführt.

--vorlage: DOCX- bzw. DOTX-Vorlage oder Ordner mit beiden Vorlagen (Dateiname mit „schueler“ bzw.
„lehrer“). Standard: Umgebungsvariable ABITUR_VORLAGE, sonst eine schlichte eingebaute Vorlage mit
derselben Kopfzeile. Die Vorlagen der Behörde liegen nicht im Skill. Ziel: gleicher Name mit .docx
(oder -o). Überschreibt nur mit --ueberschreiben. Nur Python-Standardbibliothek; rsvg-convert optional.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile
import zipfile
from dataclasses import dataclass, field, replace
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape, quoteattr

VERSION = "1.1"

SCHRIFT, MONO = "Arial", "Courier New"
TEXT, TABELLE, CODE, UNTERSCHRIFT = 22, 20, 18, 20          # halbe Punkt
GRAU_KOPF, GRAU_SUMME, GRAU_CODE, GRAU_EWH = "D9D9D9", "F2F2F2", "F2F2F2", "C0C0C0"
ROT = "C00000"
EINZUG = 357                                                 # twip je Listenebene
EWH_ANTEILE = (1434, 4990, 834, 831, 697, 706)               # Spaltenbreiten der Vorlage Lehrermaterial
SEITENUMBRUCH_VOR = ("Erwartungshorizont", "Musterlösung")   # wie in der Vorlage Lehrermaterial
EMU_JE_TWIP, EMU_JE_PX, EMU_JE_ZOLL = 635, 9525, 914400
PNG_DPI = 220
MAX_BILDHOEHE = 20 / 2.54 * EMU_JE_ZOLL
BILD_ENDUNGEN = (".svg", ".png", ".jpg", ".jpeg")
INHALTSTYP = {"png": "image/png", "svg": "image/svg+xml", "jpg": "image/jpeg", "jpeg": "image/jpeg"}
SVG_ERWEITERUNG = "{96DAC541-7B7A-43D3-8B79-37D633B846F1}"
NS_SVG = "http://www.w3.org/2000/svg"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_BILD = REL + "/image"
REL_NUMMERIERUNG = REL + "/numbering"
NS_W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS_WP = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
NS_A = "http://schemas.openxmlformats.org/drawingml/2006/main"
NS_PIC = "http://schemas.openxmlformats.org/drawingml/2006/picture"
XML_KOPF = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'


# ------------------------------------------------------------------------------ Markdown lesen

@dataclass
class Block:
    """Ein Baustein der Markdown-Datei."""
    art: str            # ueberschrift absatz tabelle liste code bild platzhalter zitat linie umbruch
    text: str = ""
    ebene: int = 0
    kopf: list = field(default_factory=list)
    ausrichtung: list = field(default_factory=list)
    zeilen: list = field(default_factory=list)      # Tabelle: Zeilen; Code: Zeilen
    punkte: list = field(default_factory=list)      # Liste: je Punkt eine Blockliste; Zitat: [Blöcke]
    geordnet: bool = False
    start: int = 1
    pfad: str = ""                                  # Bild
    breite: str = ""                                # Bild: {width=…}
    unterschrift: str = ""                          # Bild
    nummer: int = 0                                 # Platzhalter
    beschreibung: str = ""                          # Bild: Alternativtext (SVG <desc>)


UEBERSCHRIFT = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ZAUN = re.compile(r"^\s*(`{3,}|~{3,})")
LISTE = re.compile(r"^( *)([-*+]|\d{1,3}[.)])( +|$)")
TRENNZEILE = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
LINIE = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")
BILDZEILE = re.compile(r'^\s*!\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+"[^"]*")?\s*\)\s*(\{[^}]*\})?\s*$')
PLATZHALTER = re.compile(r"^\s*\[((?:Abbildung|Abb\.)\s*(\d+)\b[^\]]*)\]\s*$")
UNTERSCHRIFT_ZEILE = re.compile(r"^\*(?!\*)((?:Abbildung|Abb\.|Lösungsbild|Bild)\b.*)(?<!\*)\*$", re.S)


def kopf_lesen(text: str) -> tuple[dict[str, str], str]:
    """YAML-Kopf (nur „schlüssel: wert“) und Rest der Datei."""
    m = re.match(r"\ufeff?---[ \t]*\n(.*?)\n---[ \t]*\n", text, re.S)
    if not m:
        return {}, text
    werte: dict[str, str] = {}
    for zeile in m.group(1).splitlines():
        if mm := re.match(r"^([A-Za-z_][\w-]*):\s*(.*?)\s*$", zeile):
            wert = mm.group(2)
            if len(wert) >= 2 and wert[0] == wert[-1] and wert[0] in "\"'":
                wert = wert[1:-1]
            werte[mm.group(1)] = wert
    return werte, text[m.end():]


def einzug(zeile: str) -> int:
    return len(zeile) - len(zeile.lstrip(" "))


def zellen(zeile: str) -> list[str]:
    """Zellen einer Tabellenzeile; „|“ in Code und „\\|“ trennen nicht."""
    s = zeile.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    teile, aktuell, code, i = [], [], False, 0
    while i < len(s):
        c = s[i]
        if c == "\\" and s[i + 1:i + 2] == "|":
            aktuell.append("|")
            i += 2
            continue
        if c == "`":
            code = not code
        if c == "|" and not code:
            teile.append("".join(aktuell).strip())
            aktuell = []
        else:
            aktuell.append(c)
        i += 1
    teile.append("".join(aktuell).strip())
    return teile


def blockanfang(zeile: str) -> bool:
    """Beginnt mit dieser Zeile ein neuer Block (beendet einen Absatz)?"""
    s = zeile.strip()
    if (UEBERSCHRIFT.match(zeile) or ZAUN.match(zeile) or LINIE.match(zeile) or BILDZEILE.match(zeile)
            or s.startswith(("|", ">", "<!--"))):
        return True
    m = LISTE.match(zeile)
    return bool(m and m.group(3) and (not m.group(2)[0].isdigit() or m.group(2)[:-1] == "1"))


BEZEICHNUNG = re.compile(r"^[^.!?:]{1,50}?:\s|^-[A-Z]{1,3}\d+:")      # „Rohwert: …“, „-BL1: …“
SATZENDE = re.compile(r"[.!?;:][\"“”)]*$")


def absatz_text(zeilen: list[str]) -> str:
    """Zeilen eines Absatzes verbinden; zwei Leerzeichen oder „\\“ am Zeilenende = Zeilenumbruch.
    Ebenso bleibt eine Zeile, die nach einem Satzende mit „Bezeichnung:“ beginnt, eine eigene Zeile
    (Lösungsgänge im Lehrermaterial: „Rohwert: …“, „Begründung: …“)."""
    teile = []
    for k, z in enumerate(zeilen):
        letzte = k == len(zeilen) - 1
        hart = not letzte and (z.endswith("  ") or z.rstrip().endswith("\\")
                               or (SATZENDE.search(z.rstrip()) and BEZEICHNUNG.match(zeilen[k + 1].strip())))
        t = z.strip()
        if hart and t.endswith("\\"):
            t = t[:-1].rstrip()
        teile.append(t + ("" if letzte else ("\n" if hart else " ")))
    return "".join(teile)


def breite_aus(attribute: str | None) -> str:
    m = re.search(r"width\s*=\s*\"?([\d.,]+\s*(?:%|cm|mm|in|px))", attribute or "")
    return m.group(1).replace(",", ".").replace(" ", "") if m else ""


def liste_lesen(zeilen: list[str], i: int) -> tuple[Block, int]:
    m = LISTE.match(zeilen[i])
    basis, geordnet = len(m.group(1)), m.group(2)[0].isdigit()
    start = int(m.group(2)[:-1]) if geordnet else 1
    punkte, n = [], len(zeilen)

    def gleiche_liste(z: str) -> bool:
        mm = LISTE.match(z)
        return bool(mm and len(mm.group(1)) == basis and mm.group(2)[0].isdigit() == geordnet)

    while i < n and gleiche_liste(zeilen[i]):
        m = LISTE.match(zeilen[i])
        inhalt = m.end()
        teil = [zeilen[i][inhalt:]]
        i += 1
        while i < n:
            z = zeilen[i]
            if not z.strip():
                j = i
                while j < n and not zeilen[j].strip():
                    j += 1
                if j < n and einzug(zeilen[j]) > basis:
                    teil += [""] * (j - i)
                    i = j
                    continue
                break
            mm = LISTE.match(z)
            if mm and len(mm.group(1)) <= basis:
                break
            if einzug(z) > basis:
                teil.append(z[min(einzug(z), inhalt):])
            elif blockanfang(z):
                break
            else:
                teil.append(z.strip())                      # fortgesetzte Zeile
            i += 1
        punkte.append(bloecke_lesen(teil))
        j = i
        while j < n and not zeilen[j].strip():
            j += 1
        if j < n and gleiche_liste(zeilen[j]):
            i = j
        else:
            break
    return Block("liste", punkte=punkte, geordnet=geordnet, start=start), i


def bloecke_lesen(zeilen: list[str]) -> list[Block]:
    zeilen = [z.replace("\t", "    ").rstrip("\r") for z in zeilen]
    aus: list[Block] = []
    i, n = 0, len(zeilen)
    while i < n:
        z = zeilen[i]
        s = z.strip()
        if not s:
            i += 1
            continue
        if s.startswith("<!--"):
            j = i
            while j < n and "-->" not in zeilen[j]:
                j += 1
            if j < n and zeilen[j].rstrip().endswith("-->"):
                kommentar = "\n".join(zeilen[i:j + 1])
                if re.search(r"seitenumbruch|pagebreak|newpage", kommentar, re.I):
                    aus.append(Block("umbruch"))
                i = j + 1
                continue
        if s in ("\\newpage", "\\pagebreak"):
            aus.append(Block("umbruch"))
            i += 1
            continue
        if m := UEBERSCHRIFT.match(z):
            aus.append(Block("ueberschrift", text=m.group(2), ebene=len(m.group(1))))
            i += 1
            continue
        if m := ZAUN.match(z):
            zaun, basis, code = m.group(1), einzug(z), []
            i += 1
            while i < n and not re.match(rf"^\s*{re.escape(zaun[0])}{{{len(zaun)},}}\s*$", zeilen[i]):
                code.append(zeilen[i][min(basis, einzug(zeilen[i])):])
                i += 1
            aus.append(Block("code", zeilen=code))
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and TRENNZEILE.match(zeilen[i + 1]):
            kopf = zellen(z)
            ausrichtung = []
            for zelle in zellen(zeilen[i + 1]):
                zelle = zelle.strip()
                ausrichtung.append("center" if zelle.startswith(":") and zelle.endswith(":")
                                   else "right" if zelle.endswith(":") else "left")
            ausrichtung = (ausrichtung + ["left"] * len(kopf))[:len(kopf)]
            i += 2
            reihen = []
            while i < n and zeilen[i].strip().startswith("|"):
                reihe = zellen(zeilen[i])
                reihen.append((reihe + [""] * len(kopf))[:len(kopf)])
                i += 1
            aus.append(Block("tabelle", kopf=kopf, ausrichtung=ausrichtung, zeilen=reihen))
            continue
        if LINIE.match(z):
            aus.append(Block("linie"))
            i += 1
            continue
        if m := BILDZEILE.match(z):
            aus.append(Block("bild", text=m.group(1), pfad=m.group(2), breite=breite_aus(m.group(3))))
            i += 1
            continue
        if m := PLATZHALTER.match(z):
            aus.append(Block("platzhalter", text=m.group(1), nummer=int(m.group(2))))
            i += 1
            continue
        if (m := LISTE.match(z)) and m.group(3):
            block, i = liste_lesen(zeilen, i)
            aus.append(block)
            continue
        if s.startswith(">"):
            innen = []
            while i < n and zeilen[i].strip().startswith(">"):
                innen.append(re.sub(r"^\s*>\s?", "", zeilen[i]))
                i += 1
            aus.append(Block("zitat", punkte=[bloecke_lesen(innen)]))
            continue
        teile = [z]
        i += 1
        while i < n and zeilen[i].strip() and not blockanfang(zeilen[i]):
            teile.append(zeilen[i])
            i += 1
        aus.append(Block("absatz", text=absatz_text(teile)))
    return aus


def sichtbar(text: str) -> str:
    """Text ohne Markdown-Zeichen (für Vergleiche und Spaltenbreiten)."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>~])", r"\1", text.replace("**", "").replace("`", ""))
    text = re.sub(r"(?<![\w*])\*(?=\S)(.+?)(?<=\S)\*(?![\w*])", r"\1", text)
    return html.unescape(text).strip()


def blocktext(b: Block) -> str:
    if b.art == "absatz":
        return b.text
    if b.art == "tabelle":
        return " ".join(b.kopf + [z for r in b.zeilen for z in r])
    if b.art in ("liste", "zitat"):
        return " ".join(blocktext(x) for p in b.punkte for x in p)
    return ""


def alle_bloecke(bloecke: list[Block]):
    for b in bloecke:
        yield b
        for punkt in b.punkte:
            yield from alle_bloecke(punkt)


def unterschriften_zuordnen(bloecke: list[Block]) -> list[Block]:
    """Kursive Zeile „*Abbildung …*“ direkt nach einem Bild wird dessen Bildunterschrift."""
    aus: list[Block] = []
    for b in bloecke:
        for k, punkt in enumerate(b.punkte):
            b.punkte[k] = unterschriften_zuordnen(punkt)
        if (b.art == "absatz" and aus and aus[-1].art == "bild" and not aus[-1].unterschrift
                and (m := UNTERSCHRIFT_ZEILE.match(b.text.strip()))):
            aus[-1].unterschrift = m.group(1)
            continue
        aus.append(b)
    return aus


# ------------------------------------------------------------------------------ Abbildungen finden und platzieren

@dataclass
class Abbildung:
    pfad: Path
    nummer: int = 0              # Abbildung N
    teilaufgabe: str = ""        # Lösungsbild zu Teilaufgabe X.Y
    titel: str = ""
    beschreibung: str = ""


def svg_titel(pfad: Path) -> tuple[str, str]:
    """(<title>, <desc>) einer SVG-Datei."""
    try:
        wurzel = ET.parse(pfad).getroot()
    except (ET.ParseError, OSError):
        return "", ""
    titel = wurzel.find(f"{{{NS_SVG}}}title")
    beschreibung = wurzel.find(f"{{{NS_SVG}}}desc")
    return (" ".join((titel.text or "").split()) if titel is not None else "",
            " ".join((beschreibung.text or "").split()) if beschreibung is not None else "")


def unterschrift_aus_titel(titel: str, ersatz: str) -> str:
    """„Abbildung 1 – Titel“ → „Abbildung 1: Titel“."""
    if not titel:
        return ersatz
    return re.sub(r"^((?:Abbildung|Lösungsbild)\s+[\d.]+)\s*[–—-]\s*", r"\1: ", titel)


def abbildungen_finden(md: Path, ordner: Path | None) -> list[Abbildung]:
    praefix = re.sub(r"_(schuelermaterial|lehrermaterial)$", "", md.stem)
    orte = [ordner] if ordner else [md.parent / "abbildungen", md.parent]
    gefunden: dict[tuple, Abbildung] = {}
    for ort in orte:
        if not ort.is_dir():
            continue
        for datei in sorted(ort.iterdir()):
            if not datei.name.startswith(praefix + "_") or datei.suffix.lower() not in BILD_ENDUNGEN:
                continue
            rest = datei.stem[len(praefix) + 1:]
            if m := re.match(r"abb(\d+)(?:_|$)", rest):
                schluessel, abb = ("abb", int(m.group(1))), Abbildung(datei, nummer=int(m.group(1)))
            elif m := re.match(r"loesung_(\d+)[-_.](\d+)(?:_|$)", rest):
                ta = f"{m.group(1)}.{m.group(2)}"
                schluessel, abb = ("loesung", ta), Abbildung(datei, teilaufgabe=ta)
            else:
                continue
            alt = gefunden.get(schluessel)
            if alt is None or (alt.pfad.suffix.lower() != ".svg" and datei.suffix.lower() == ".svg"):
                gefunden[schluessel] = abb
    for abb in gefunden.values():
        titel, beschreibung = svg_titel(abb.pfad) if abb.pfad.suffix.lower() == ".svg" else ("", "")
        ersatz = f"Abbildung {abb.nummer}" if abb.nummer else f"Lösungsbild zu Teilaufgabe {abb.teilaufgabe}"
        abb.titel = unterschrift_aus_titel(titel, ersatz)
        abb.beschreibung = beschreibung or abb.titel
    return sorted(gefunden.values(), key=lambda a: (a.nummer == 0, a.nummer, a.teilaufgabe))


def bild_block(abb: Abbildung) -> Block:
    return Block("bild", text=abb.titel, pfad=str(abb.pfad.resolve()), unterschrift=abb.titel,
                 beschreibung=abb.beschreibung)


def abschnittsende(bloecke: list[Block], h: int) -> int:
    for k in range(h + 1, len(bloecke)):
        if bloecke[k].art == "ueberschrift" and bloecke[k].ebene <= bloecke[h].ebene:
            return k
    return len(bloecke)


def abschnitt_vor(bloecke: list[Block], pos: int) -> str:
    for k in range(min(pos, len(bloecke)) - 1, -1, -1):
        if bloecke[k].art == "ueberschrift":
            return sichtbar(bloecke[k].text)
    return "Anfang"


def kurz(text: str, laenge: int = 45) -> str:
    text = " ".join(sichtbar(text).split())
    return text if len(text) <= laenge else text[:laenge - 1].rstrip() + "…"


def abbildungen_platzieren(bloecke: list[Block], md: Path, lehrermaterial: bool, ordner: Path | None,
                           meldungen: list[str]) -> list[Block]:
    """Platzhalter ersetzen und nicht eingebundene Abbildungsdateien einsetzen (siehe Modulhilfe)."""
    dateien = abbildungen_finden(md, ordner)
    eingebunden_pfade, eingebunden_nr, eingebunden_ta = set(), set(), set()
    for b in alle_bloecke(bloecke):
        if b.art != "bild":
            continue
        pfad = (md.parent / b.pfad).resolve()
        eingebunden_pfade.add(pfad)
        quelle = f"{b.text} {pfad.name}"
        if m := re.search(r"(?:Abbildung|Abb\.)\s*(\d+)|_abb(\d+)(?:_|\.)", quelle):
            eingebunden_nr.add(int(m.group(1) or m.group(2)))
        if m := re.search(r"Teilaufgabe\s+(\d+\.\d+)|_loesung_(\d+)[-_.](\d+)", quelle):
            eingebunden_ta.add(m.group(1) or f"{m.group(2)}.{m.group(3)}")

    nach_nummer = {a.nummer: a for a in dateien if a.nummer}
    for b in alle_bloecke(bloecke):
        if b.art == "platzhalter" and b.nummer in nach_nummer:
            abb = nach_nummer[b.nummer]
            b.art, b.pfad, b.unterschrift, b.beschreibung = "bild", str(abb.pfad.resolve()), abb.titel, abb.beschreibung
            b.text = abb.titel
            eingebunden_pfade.add(abb.pfad.resolve())
            eingebunden_nr.add(abb.nummer)
            meldungen.append(f"✔ Abbildung {abb.nummer} ({abb.pfad.name}) → Platzhalter „{kurz(b.text)}“")

    einfuegen: list[tuple[int, int, Block]] = []
    if lehrermaterial:
        offen = [a for a in dateien if a.teilaufgabe and a.teilaufgabe not in eingebunden_ta
                 and a.pfad.resolve() not in eingebunden_pfade]
        for k, abb in enumerate(offen):
            muster = re.compile(rf"Teilaufgabe\s+{re.escape(abb.teilaufgabe)}(?![\d.])")
            h = next((i for i, b in enumerate(bloecke) if b.art == "ueberschrift" and muster.search(b.text)), None)
            if h is None:
                pos, wo = len(bloecke), "ans Ende (Überschrift der Teilaufgabe fehlt)"
                meldungen.append(f"⚠ Lösungsbild {abb.teilaufgabe}: keine Überschrift „… Teilaufgabe "
                                 f"{abb.teilaufgabe}“ gefunden")
            else:
                ende = abschnittsende(bloecke, h)
                pos = next((i for i in range(h + 1, ende) if bloecke[i].art == "tabelle"
                            and any("Bewertungsmerkmal" in sichtbar(z) for z in bloecke[i].kopf)), ende)
                wo = "vor der Merkmaltabelle" if pos < ende else "ans Ende des Abschnitts"
            einfuegen.append((pos, k, bild_block(abb)))
            meldungen.append(f"✔ Lösungsbild {abb.teilaufgabe} ({abb.pfad.name}) → „{abschnitt_vor(bloecke, pos)}“, "
                             f"{wo} (automatisch)")
    else:
        offen = [a for a in dateien if a.nummer and a.nummer not in eingebunden_nr
                 and a.pfad.resolve() not in eingebunden_pfade]
        # Bereich: ab der ersten Überschrift der Ebene 1, ohne Abschnitte „Hinweise“
        zulaessig, stapel, teil_a = [], [], False
        for i, b in enumerate(bloecke):
            if b.art == "ueberschrift":
                teil_a = teil_a or b.ebene == 1
                stapel = [x for x in stapel if x[0] < b.ebene] + [(b.ebene, sichtbar(b.text))]
            zulaessig.append(teil_a and not any(t.lower().startswith("hinweis") for _, t in stapel))
        for k, abb in enumerate(offen):
            erwaehnung = re.compile(rf"(?:Abbildung|Abb\.)\s*{abb.nummer}(?!\d)")
            in_anlage = re.compile(rf"(?:Abbildung|Abb\.)\s*{abb.nummer}(?!\d)\s+in\s+Anlage\s+(\d+)")
            treffer = [i for i, b in enumerate(bloecke) if b.art != "ueberschrift" and erwaehnung.search(blocktext(b))]
            ziel = [i for i in treffer if zulaessig[i]] or treffer
            if not ziel:
                h = next((i for i, b in enumerate(bloecke) if b.art == "ueberschrift"
                          and re.match(r"^B\.\s*Material", sichtbar(b.text))), None)
                pos = abschnittsende(bloecke, h) if h is not None else len(bloecke)
                meldungen.append(f"⚠ Abbildung {abb.nummer} ({abb.pfad.name}) wird im Text nicht erwähnt → "
                                 f"ans Ende von „{abschnitt_vor(bloecke, pos)}“")
                einfuegen.append((pos, k, bild_block(abb)))
                continue
            i = ziel[0]
            if m := in_anlage.search(blocktext(bloecke[i])):
                h = next((j for j, b in enumerate(bloecke) if b.art == "ueberschrift"
                          and re.match(rf"^Anlage\s+{m.group(1)}\b", sichtbar(b.text))), None)
                if h is not None:
                    pos = abschnittsende(bloecke, h)
                    einfuegen.append((pos, k, bild_block(abb)))
                    meldungen.append(f"✔ Abbildung {abb.nummer} ({abb.pfad.name}) → ans Ende von "
                                     f"„{sichtbar(bloecke[h].text)}“ (automatisch)")
                    continue
            pos, b = i + 1, bloecke[i]
            if (b.art == "absatz" and b.text.rstrip().endswith(":") and pos < len(bloecke)
                    and bloecke[pos].art in ("tabelle", "liste", "code")):
                pos += 1
                wo = f"nach „{kurz(b.text)}“ und der folgenden {'Tabelle' if bloecke[i + 1].art == 'tabelle' else 'Liste'}"
            else:
                wo = f"nach „{kurz(b.text)}“"
            if not zulaessig[i]:
                wo += " – nur in den Hinweise erwähnt, bitte prüfen"
            einfuegen.append((pos, k, bild_block(abb)))
            meldungen.append(f"✔ Abbildung {abb.nummer} ({abb.pfad.name}) → „{abschnitt_vor(bloecke, i + 1)}“, "
                             f"{wo} (automatisch)")
        # erwähnte Abbildungen ohne Datei
        erwaehnt = {int(n) for b in bloecke for n in re.findall(r"(?:Abbildung|Abb\.)\s*(\d+)", blocktext(b))}
        vorhanden = eingebunden_nr | {a.nummer for a in dateien}
        for n in sorted(erwaehnt - vorhanden):
            meldungen.append(f"✘ Abbildung {n} wird erwähnt, ist aber weder eingebunden noch als Datei "
                             f"„…_abb{n}_….svg“ vorhanden")
    if not einfuegen:
        return bloecke
    neu: list[Block] = []
    einfuegen.sort(key=lambda e: (e[0], e[1]))
    k = 0
    for i in range(len(bloecke) + 1):
        while k < len(einfuegen) and einfuegen[k][0] == i:
            neu.append(einfuegen[k][2])
            k += 1
        if i < len(bloecke):
            neu.append(bloecke[i])
    return neu


# ------------------------------------------------------------------------------ Bildgrößen und Einbettung

def svg_groesse(daten: bytes) -> tuple[float, float]:
    """Breite und Höhe in px (96 dpi)."""
    try:
        wurzel = ET.fromstring(daten)
    except ET.ParseError:
        return 800.0, 600.0

    def laenge(wert: str | None) -> float | None:
        m = re.match(r"^\s*([\d.]+)\s*(px|pt|mm|cm|in)?\s*$", wert or "")
        if not m:
            return None
        return float(m.group(1)) * {"pt": 96 / 72, "mm": 96 / 25.4, "cm": 96 / 2.54, "in": 96}.get(m.group(2) or "px", 1)

    b, h = laenge(wurzel.get("width")), laenge(wurzel.get("height"))
    vb = [float(x) for x in re.split(r"[\s,]+", (wurzel.get("viewBox") or "").strip()) if x]
    if len(vb) == 4 and vb[2] > 0 and vb[3] > 0:
        if b is None and h is None:
            b, h = vb[2], vb[3]
        elif b is None:
            b = h * vb[2] / vb[3]
        elif h is None:
            h = b * vb[3] / vb[2]
    return b or 800.0, h or 600.0


def raster_groesse(daten: bytes) -> tuple[float, float]:
    """PNG bzw. JPEG: Breite und Höhe in px bei 96 dpi."""
    if daten[:8] == b"\x89PNG\r\n\x1a\n":
        b, h = struct.unpack(">II", daten[16:24])
        dpi, i = 96.0, 8
        while i + 8 <= len(daten):
            laenge, typ = struct.unpack(">I4s", daten[i:i + 8])
            if typ == b"pHYs" and laenge >= 9:
                x, _, einheit = struct.unpack(">IIB", daten[i + 8:i + 17])
                if einheit == 1 and x:
                    dpi = x * 0.0254
                break
            if typ == b"IDAT":
                break
            i += 12 + laenge
        return b * 96 / dpi, h * 96 / dpi
    if daten[:2] == b"\xff\xd8":
        i, dpi = 2, 96.0
        while i + 4 <= len(daten):
            if daten[i] != 0xFF:
                i += 1
                continue
            marke = daten[i + 1]
            laenge = struct.unpack(">H", daten[i + 2:i + 4])[0]
            if marke == 0xE0 and daten[i + 4:i + 9] == b"JFIF\x00":
                einheit, x = daten[i + 11], struct.unpack(">H", daten[i + 12:i + 14])[0]
                dpi = x if einheit == 1 and x else x * 2.54 if einheit == 2 and x else dpi
            if marke in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, b = struct.unpack(">HH", daten[i + 5:i + 9])
                return b * 96 / dpi, h * 96 / dpi
            i += 2 + laenge
    return 800.0, 600.0


def svg_rastern(pfad: Path, breite_px: int) -> bytes | None:
    """PNG-Ersatzbild über rsvg-convert (oder cairosvg, falls installiert)."""
    exe = shutil.which("rsvg-convert")
    if exe:
        try:
            r = subprocess.run([exe, "-w", str(breite_px), "-a", "-b", "white", str(pfad)],
                               capture_output=True, timeout=120)
            if r.returncode == 0 and r.stdout.startswith(b"\x89PNG"):
                return r.stdout
        except (OSError, subprocess.SubprocessError):
            pass
    try:
        import cairosvg  # type: ignore
        return cairosvg.svg2png(url=str(pfad), output_width=breite_px, background_color="white")
    except Exception:  # noqa: BLE001 – optional, jeder Fehler heißt: kein Ersatzbild
        return None


class Medien:
    """Bilddateien, Beziehungen und Inhaltstypen des Pakets."""

    def __init__(self, rels: str):
        self.rels = rels
        self.naechste = max((int(x) for x in re.findall(r'Id="rId(\d+)"', rels)), default=0) + 1
        self.dateien: dict[str, bytes] = {}
        self.endungen: set[str] = set()
        self.docpr = 100
        self.nr = 0
        self.ohne_ersatzbild: list[str] = []

    def beziehung(self, ziel: str, typ: str = REL_BILD) -> str:
        rid = f"rId{self.naechste}"
        self.naechste += 1
        self.rels = self.rels.replace("</Relationships>",
                                      f'<Relationship Id="{rid}" Type="{typ}" Target="{ziel}"/></Relationships>')
        return rid

    def ablegen(self, daten: bytes, endung: str) -> str:
        name = f"media/abitur_bild{self.nr}.{endung}"
        self.dateien["word/" + name] = daten
        self.endungen.add(endung)
        return self.beziehung(name)

    def einbetten(self, pfad: Path, wunsch: str, max_breite: float, name: str, beschreibung: str) -> str:
        daten = pfad.read_bytes()
        endung = pfad.suffix.lower().lstrip(".")
        px_b, px_h = svg_groesse(daten) if endung == "svg" else raster_groesse(daten)
        breite = px_b * EMU_JE_PX
        if m := re.match(r"^([\d.]+)(%|cm|mm|in|px)$", wunsch):
            z = float(m.group(1))
            breite = {"%": max_breite * z / 100, "cm": z / 2.54 * EMU_JE_ZOLL, "mm": z / 25.4 * EMU_JE_ZOLL,
                      "in": z * EMU_JE_ZOLL, "px": z * EMU_JE_PX}[m.group(2)]
        breite = min(breite, max_breite)
        hoehe = breite * px_h / px_b
        if hoehe > MAX_BILDHOEHE:
            breite, hoehe = breite * MAX_BILDHOEHE / hoehe, MAX_BILDHOEHE
        cx, cy = int(breite), int(hoehe)
        self.nr += 1
        if endung == "svg":
            rid_svg = self.ablegen(daten, "svg")
            png = svg_rastern(pfad, max(200, round(breite / EMU_JE_ZOLL * PNG_DPI)))
            if png:
                rid = self.ablegen(png, "png")
                blip = (f'<a:blip r:embed="{rid}"><a:extLst><a:ext uri="{SVG_ERWEITERUNG}">'
                        f'<asvg:svgBlip xmlns:asvg="http://schemas.microsoft.com/office/drawing/2016/SVG/main" '
                        f'r:embed="{rid_svg}"/></a:ext></a:extLst></a:blip>')
            else:
                self.ohne_ersatzbild.append(pfad.name)
                blip = f'<a:blip r:embed="{rid_svg}"/>'
        else:
            rid = self.ablegen(daten, "jpeg" if endung == "jpg" else endung)
            blip = f'<a:blip r:embed="{rid}"/>'
        self.docpr += 1
        name_a, beschr_a = quoteattr(name), quoteattr(beschreibung)
        return (f'<w:r><w:drawing><wp:inline distT="0" distB="0" distL="0" distR="0">'
                f'<wp:extent cx="{cx}" cy="{cy}"/><wp:effectExtent l="0" t="0" r="0" b="0"/>'
                f'<wp:docPr id="{self.docpr}" name={name_a} descr={beschr_a}/>'
                f'<wp:cNvGraphicFramePr><a:graphicFrameLocks xmlns:a="{NS_A}" noChangeAspect="1"/></wp:cNvGraphicFramePr>'
                f'<a:graphic xmlns:a="{NS_A}"><a:graphicData uri="{NS_PIC}"><pic:pic xmlns:pic="{NS_PIC}">'
                f'<pic:nvPicPr><pic:cNvPr id="{self.docpr}" name={quoteattr(pfad.name)} descr={beschr_a}/><pic:cNvPicPr/>'
                f'</pic:nvPicPr><pic:blipFill>{blip}<a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
                f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
                f'<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr></pic:pic></a:graphicData></a:graphic>'
                f'</wp:inline></w:drawing></w:r>')


# ------------------------------------------------------------------------------ WordprocessingML schreiben

@dataclass(frozen=True)
class Stil:
    fett: bool = False
    kursiv: bool = False
    groesse: int = TEXT
    schrift: str = SCHRIFT
    unterstrichen: bool = False
    farbe: str = ""


def rpr(st: Stil) -> str:
    t = [f'<w:rFonts w:ascii="{st.schrift}" w:hAnsi="{st.schrift}" w:eastAsia="{st.schrift}" w:cs="{st.schrift}"/>']
    if st.fett:
        t.append("<w:b/><w:bCs/>")
    if st.kursiv:
        t.append("<w:i/><w:iCs/>")
    if st.farbe:
        t.append(f'<w:color w:val="{st.farbe}"/>')
    t.append(f'<w:sz w:val="{st.groesse}"/><w:szCs w:val="{st.groesse}"/>')
    if st.unterstrichen:
        t.append('<w:u w:val="single"/>')
    return "<w:rPr>" + "".join(t) + "</w:rPr>"


def xml_text(s: str) -> str:
    return escape(re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", s))


BMK_STRICH = re.compile(r"(?<![\w\-/.])-(?=[A-Z]{1,3}\d)")


def lauf(text: str, st: Stil) -> str:
    """Ein Lauf; Tabulator und Zeilenumbruch als eigene Elemente. Der Bindestrich eines
    Betriebsmittelkennzeichens („-P1“) wird geschützt, damit die Zeile nicht nach ihm umbricht."""
    inhalt = []
    for teil in re.split(r"(\t|\n)", text):
        if teil == "\t":
            inhalt.append("<w:tab/>")
        elif teil == "\n":
            inhalt.append("<w:br/>")
        elif teil:
            stuecke = [teil] if st.schrift == MONO else BMK_STRICH.split(teil)
            for k, stueck in enumerate(stuecke):
                if k:
                    inhalt.append("<w:noBreakHyphen/>")
                if stueck:
                    inhalt.append(f'<w:t xml:space="preserve">{xml_text(stueck)}</w:t>')
    return f"<w:r>{rpr(st)}{''.join(inhalt)}</w:r>" if inhalt else ""


INLINE = re.compile(
    r"(?P<kommentar><!--.*?-->)"
    r"|(?P<code>(?P<ticks>`+)(?P<codetext>.+?)(?P=ticks))"
    r"|(?P<esc>\\[\\`*_{}\[\]()#+\-.!|<>~])"
    r"|(?P<br><br\s*/?>|\n)"
    r"|(?P<fett>\*\*(?=\S)(?P<fetttext>.+?)(?<=\S)\*\*)"
    r"|(?P<kursiv>\*(?=[^\s*])(?P<kursivtext>.+?)(?<=[^\s\\])\*(?!\*))"
    r"|(?P<link>\[(?P<linktext>[^\]]+)\]\((?P<ziel>[^)\s]+)\))", re.S)


def inline(text: str, st: Stil) -> str:
    """Markdown-Auszeichnung im Fließtext (fett, kursiv, Code, Umbruch, Link) → Läufe."""
    aus, pos = [], 0
    for m in INLINE.finditer(text):
        aus.append(lauf(html.unescape(text[pos:m.start()]), st))
        pos = m.end()
        if m.group("code"):
            code = m.group("codetext")
            if len(code) > 1 and code[0] == code[-1] == " ":
                code = code[1:-1]
            aus.append(lauf(code, replace(st, schrift=MONO)))
        elif m.group("esc"):
            aus.append(lauf(m.group("esc")[1], st))
        elif m.group("br"):
            aus.append(lauf("\n", st))
        elif m.group("fett"):
            aus.append(inline(m.group("fetttext"), replace(st, fett=True)))
        elif m.group("kursiv"):
            aus.append(inline(m.group("kursivtext"), replace(st, kursiv=True)))
        elif m.group("link"):
            aus.append(inline(m.group("linktext"), st))
            ziel = m.group("ziel")
            if re.match(r"https?://", ziel) and ziel != m.group("linktext"):
                aus.append(lauf(f" ({ziel})", st))
    aus.append(lauf(html.unescape(text[pos:]), st))
    return "".join(aus)


def ppr(*, vor: int = 0, nach: int = 120, zeile: int = 264, regel: str = "auto", links: int = 0,
        haengend: int = 0, jc: str = "", weiter: bool = False, zusammen: bool = False, umbruch: bool = False,
        num: tuple[int, int] | None = None, tabs: tuple = (), fuellung: str = "", rahmen: str = "",
        gliederung: int | None = None) -> str:
    """Absatzeigenschaften in der Reihenfolge des Schemas."""
    t = []
    if weiter:
        t.append("<w:keepNext/>")
    if zusammen:
        t.append("<w:keepLines/>")
    if umbruch:
        t.append("<w:pageBreakBefore/>")
    if num:
        t.append(f'<w:numPr><w:ilvl w:val="{num[1]}"/><w:numId w:val="{num[0]}"/></w:numPr>')
    if rahmen:
        t.append(f'<w:pBdr><w:{rahmen} w:val="single" w:sz="6" w:space="4" w:color="808080"/></w:pBdr>')
    if fuellung:
        t.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{fuellung}"/>')
    if tabs:
        t.append("<w:tabs>" + "".join(f'<w:tab w:val="{a}" w:pos="{p}"/>' for a, p in tabs) + "</w:tabs>")
    t.append(f'<w:spacing w:before="{vor}" w:after="{nach}" w:line="{zeile}" w:lineRule="{regel}"/>')
    if links or haengend:
        t.append(f'<w:ind w:left="{links}"' + (f' w:hanging="{haengend}"' if haengend else "") + "/>")
    if jc:
        t.append(f'<w:jc w:val="{jc}"/>')
    if gliederung is not None:
        t.append(f'<w:outlineLvl w:val="{min(gliederung, 8)}"/>')
    return "<w:pPr>" + "".join(t) + "</w:pPr>"


class Nummerierung:
    """Ergänzt numbering.xml der Vorlage um Aufzählung und Nummerierung."""

    def __init__(self, xml: str | None):
        self.xml = xml or (XML_KOPF + f'<w:numbering xmlns:w="{NS_W}"></w:numbering>')
        self.abstrakt = max((int(x) for x in re.findall(r'<w:abstractNum\b[^>]*w:abstractNumId="(\d+)"', self.xml)),
                            default=-1)
        self.num = max((int(x) for x in re.findall(r'<w:num\b[^>]*w:numId="(\d+)"', self.xml)), default=0)
        self.neu_abstrakt: list[str] = []
        self.neu_num: list[str] = []
        self._punkt: int | None = None
        self._zahl: int | None = None

    def _abstrakt(self, format_: str) -> int:
        self.abstrakt += 1
        ebenen = []
        for k in range(3):
            text = "•–·"[k] if format_ == "bullet" else f"%{k + 1}."
            ebenen.append(f'<w:lvl w:ilvl="{k}"><w:start w:val="1"/><w:numFmt w:val="{format_}"/>'
                          f'<w:lvlText w:val="{text}"/><w:lvlJc w:val="left"/>'
                          f'<w:pPr><w:ind w:left="{EINZUG * (k + 1)}" w:hanging="{EINZUG}"/></w:pPr>'
                          f'<w:rPr><w:rFonts w:ascii="{SCHRIFT}" w:hAnsi="{SCHRIFT}" w:hint="default"/></w:rPr></w:lvl>')
        self.neu_abstrakt.append(f'<w:abstractNum w:abstractNumId="{self.abstrakt}">'
                                 f'<w:multiLevelType w:val="hybridMultilevel"/>{"".join(ebenen)}</w:abstractNum>')
        return self.abstrakt

    def _num(self, abstrakt: int, start: int | None = None) -> int:
        self.num += 1
        override = (f'<w:lvlOverride w:ilvl="0"><w:startOverride w:val="{start}"/></w:lvlOverride>'
                    if start is not None else "")
        self.neu_num.append(f'<w:num w:numId="{self.num}"><w:abstractNumId w:val="{abstrakt}"/>{override}</w:num>')
        return self.num

    def aufzaehlung(self) -> int:
        if self._punkt is None:
            self._punkt = self._num(self._abstrakt("bullet"))
        return self._punkt

    def nummeriert(self, start: int) -> int:
        if self._zahl is None:
            self._zahl = self._abstrakt("decimal")
        return self._num(self._zahl, start)

    def ergebnis(self) -> str:
        xml = self.xml
        if self.neu_abstrakt:
            ende = xml.rfind("</w:abstractNum>")
            if ende >= 0:
                pos = ende + len("</w:abstractNum>")
            else:
                m = re.search(r"<w:num\b|<w:numIdMacAtCleanup|</w:numbering>", xml)
                pos = m.start()
            xml = xml[:pos] + "".join(self.neu_abstrakt) + xml[pos:]
        if self.neu_num:
            m = re.search(r"<w:numIdMacAtCleanup|</w:numbering>", xml)
            xml = xml[:m.start()] + "".join(self.neu_num) + xml[m.start():]
        return xml


ZEICHENBREITE = {**dict.fromkeys("ijlI.,:;!|'’‚ ·[]/", 0.26), **dict.fromkeys("ftr-()°", 0.34),
                 **dict.fromkeys("mwMW%…→—", 0.87)}            # Arial, Anteil am Geviert


def schriftbreite(text: str, groesse: int = TABELLE, fett: bool = False) -> float:
    """Geschätzte Breite in twip (Arial)."""
    em = sum(ZEICHENBREITE.get(c, 0.68 if c.isupper() else 0.556) for c in text)
    return em * groesse * 10 * (1.07 if fett else 1.0)


def spaltenbreiten(spalten: list[list[tuple[str, bool]]], gesamt: int, groesse: int = TABELLE,
                   rand: int = 85) -> tuple[list[int], bool]:
    """Spaltenbreiten (twip) nach Inhalt: erst Mindestbreiten (längstes Wort), Rest nach Bedarf.
    Zweiter Wert: passt jedes Wort in seine Spalte?"""
    polster = 2 * rand + 40
    natuerlich, minimal = [], []
    for zellen_ in spalten:
        zeilen = [(z, fett) for text, fett in zellen_ for z in sichtbar(text).split("\n")]
        natuerlich.append(min(max((schriftbreite(z, groesse, f) for z, f in zeilen), default=0), 0.6 * gesamt) + polster)
        minimal.append(max((schriftbreite(w, groesse, f) for z, f in zeilen for w in z.split()), default=0) + polster)
    passt = sum(minimal) <= gesamt
    if sum(natuerlich) <= gesamt:
        breiten = [b * gesamt / sum(natuerlich) for b in natuerlich]
    elif sum(minimal) >= gesamt:
        breiten = [b * gesamt / sum(minimal) for b in minimal]
    else:
        ueber = [n - m for n, m in zip(natuerlich, minimal)]
        rest = gesamt - sum(minimal)
        breiten = [m + rest * u / sum(ueber) for m, u in zip(minimal, ueber)]
    breiten = [int(b) for b in breiten]
    breiten[-1] += gesamt - sum(breiten)
    return breiten, passt


def zelle(inhalt: str, breite: int, *, fuellung: str = "", spannweite: int = 1, vmerge: str = "",
          mitte: bool = False) -> str:
    t = [f'<w:tcW w:w="{breite}" w:type="dxa"/>']
    if spannweite > 1:
        t.append(f'<w:gridSpan w:val="{spannweite}"/>')
    if vmerge == "start":
        t.append('<w:vMerge w:val="restart"/>')
    elif vmerge == "weiter":
        t.append("<w:vMerge/>")
    if fuellung:
        t.append(f'<w:shd w:val="clear" w:color="auto" w:fill="{fuellung}"/>')
    if mitte:
        t.append('<w:vAlign w:val="center"/>')
    return f"<w:tc><w:tcPr>{''.join(t)}</w:tcPr>{inhalt}</w:tc>"


def tabelle_xml(reihen: list[str], breiten: list[int], einrueckung: int, rahmen: int = 4, rand: int = 85) -> str:
    raender = "".join(f'<w:{s} w:val="single" w:sz="{rahmen}" w:space="0" w:color="000000"/>'
                      for s in ("top", "left", "bottom", "right", "insideH", "insideV"))
    gitter = "".join(f'<w:gridCol w:w="{b}"/>' for b in breiten)
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(breiten)}" w:type="dxa"/>'
            f'<w:tblInd w:w="{einrueckung}" w:type="dxa"/><w:tblBorders>{raender}</w:tblBorders>'
            f'<w:tblLayout w:type="fixed"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/>'
            f'<w:left w:w="{rand}" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="{rand}" w:type="dxa"/>'
            f'</w:tblCellMar><w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" '
            f'w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
            f'<w:tblGrid>{gitter}</w:tblGrid>{"".join(reihen)}</w:tbl>')


def reihe(zellen_xml: list[str], kopf: bool = False) -> str:
    return f"<w:tr><w:trPr><w:cantSplit/>{'<w:tblHeader/>' if kopf else ''}</w:trPr>{''.join(zellen_xml)}</w:tr>"


AUFGABE_UE = re.compile(r"^(\d+\.\s*Aufgabe\b.*?)\s*\((insgesamt\s+\d+(?:,\d+)?\s*BE)\)\s*$")
TEILAUFGABE_UE = re.compile(r"^(\d+\.\d+(?:\.\d+)?\s+.*?)\s*\((\d+(?:,\d+)?\s*BE)\)\s*$")
TEIL_UE = re.compile(r"^([A-E]\.)\s+(.*)$")
ANLAGE_UE = re.compile(r"^(Anlage|Material)\s+\d+")


class Wandler:
    """Blöcke → Textkörper (WordprocessingML) im Satzspiegel der Vorlage."""

    def __init__(self, textbreite: int, nummern: Nummerierung, medien: Medien, basis: Path):
        self.textbreite, self.nummern, self.medien, self.basis = textbreite, nummern, medien, basis
        self.teile: list[str] = []
        self.anzahl = {"Absätze": 0, "Tabellen": 0, "Abbildungen": 0}
        self.fehler: list[str] = []
        self.folgt = ""                                 # Art des nächsten Blocks (Seitenumbruch steuern)

    def absatz(self, inhalt: str, **kw) -> None:
        if not self.teile:
            kw["umbruch"] = False
        self.teile.append(f"<w:p>{ppr(**kw)}{inhalt}</w:p>")
        self.anzahl["Absätze"] += 1

    def bloecke(self, bloecke: list[Block], ebene: int = 0) -> None:
        for k, b in enumerate(bloecke):
            self.folgt = bloecke[k + 1].art if k + 1 < len(bloecke) else ""
            getattr(self, "b_" + b.art)(b, ebene)

    def b_ueberschrift(self, b: Block, ebene: int) -> None:
        text = sichtbar(b.text)
        gl = b.ebene - 1
        umbruch = b.ebene == 1 and text in SEITENUMBRUCH_VOR
        rechts = (("right", self.textbreite),)
        if m := AUFGABE_UE.match(b.text):
            st = Stil(fett=True, groesse=24)
            self.absatz(inline(m.group(1), st) + lauf("\t" + m.group(2), st), vor=360, nach=120, weiter=True,
                        umbruch=umbruch, tabs=rechts, gliederung=gl)
        elif m := TEILAUFGABE_UE.match(b.text):
            st = Stil(fett=True)
            self.absatz(inline(m.group(1), st) + lauf("\t" + m.group(2), st), vor=240, nach=60, weiter=True,
                        tabs=rechts, gliederung=gl)
        elif b.ebene == 1 and (m := TEIL_UE.match(text)):
            st = Stil(fett=True, groesse=28)
            self.absatz(lauf(m.group(1) + "\t", st) + inline(m.group(2), st), vor=360, nach=120, weiter=True,
                        umbruch=umbruch, tabs=(("left", 426),), gliederung=gl)
        elif ANLAGE_UE.match(text):
            st = Stil(fett=True, groesse=24, unterstrichen=True)
            self.absatz(inline(b.text, st), vor=360, nach=120, weiter=True, gliederung=gl)
        else:
            groesse, vor, nach = {1: (28, 360, 120), 2: (24, 240, 120), 3: (22, 200, 60)}.get(b.ebene, (22, 160, 60))
            st = Stil(fett=True, groesse=groesse, kursiv=b.ebene > 3)
            self.absatz(inline(b.text, st), vor=vor, nach=nach, weiter=True, umbruch=umbruch, gliederung=gl)

    def b_absatz(self, b: Block, ebene: int) -> None:
        text = b.text.strip()
        weiter = (text.endswith(":")                                       # leitet Tabelle oder Liste ein
                  or bool(re.fullmatch(r"\*\*[^*]+\*\*", text))            # fette Zwischenüberschrift
                  or (self.folgt == "bild" and len(sichtbar(text)) < 120))  # kurze Zeile vor einem Bild
        self.absatz(inline(b.text, Stil()), links=ebene * EINZUG, weiter=weiter)

    def b_platzhalter(self, b: Block, ebene: int) -> None:
        self.fehler.append(f"✘ Platzhalter „[{kurz(b.text)}]“: keine Datei „…_abb{b.nummer}_….svg“ gefunden")
        self.absatz(lauf(f"[{sichtbar(b.text)} – Abbildung fehlt]", Stil(fett=True, farbe=ROT)), links=ebene * EINZUG)

    def b_umbruch(self, b: Block, ebene: int) -> None:
        self.teile.append('<w:p><w:r><w:br w:type="page"/></w:r></w:p>')

    def b_linie(self, b: Block, ebene: int) -> None:
        self.absatz("", nach=120, rahmen="bottom", links=ebene * EINZUG)

    def b_zitat(self, b: Block, ebene: int) -> None:
        for punkt in b.punkte:
            self.bloecke(punkt, ebene + 1)

    def b_code(self, b: Block, ebene: int) -> None:
        zeilen = b.zeilen or [""]
        for k, z in enumerate(zeilen):
            letzte = k == len(zeilen) - 1
            self.absatz(lauf(z, Stil(schrift=MONO, groesse=CODE)), nach=120 if letzte else 0, zeile=240,
                        links=ebene * EINZUG, fuellung=GRAU_CODE, weiter=not letzte, zusammen=True)

    def b_liste(self, b: Block, ebene: int) -> None:
        ilvl = min(ebene, 2)
        num = self.nummern.nummeriert(b.start) if b.geordnet else self.nummern.aufzaehlung()
        for punkt in b.punkte:
            erster = punkt[0] if punkt and punkt[0].art == "absatz" else None
            text = erster.text if erster else ""
            self.absatz(inline(text, Stil()), nach=60, num=(num, ilvl), weiter=text.rstrip().endswith(":"))
            self.bloecke(punkt[1:] if erster else punkt, ebene + 1)

    def b_bild(self, b: Block, ebene: int) -> None:
        pfad = Path(b.pfad)
        if not pfad.is_absolute():
            pfad = (self.basis / pfad).resolve()
        unterschrift = b.unterschrift or (b.text if re.match(r"(Abbildung|Abb\.|Lösungsbild|Bild)\b", b.text) else "")
        if not pfad.is_file():
            self.fehler.append(f"✘ Bilddatei fehlt: {b.pfad}")
            self.absatz(lauf(f"[Bilddatei fehlt: {b.pfad}]", Stil(fett=True, farbe=ROT)), links=ebene * EINZUG)
            return
        name = re.match(r"((?:Abbildung|Lösungsbild)[^:–]*)", unterschrift or b.text)
        lauf_bild = self.medien.einbetten(pfad, b.breite, (self.textbreite - ebene * EINZUG) * EMU_JE_TWIP,
                                          name.group(1).strip() if name else pfad.stem,
                                          b.beschreibung or sichtbar(b.text) or pfad.stem)
        self.absatz(lauf_bild, vor=120, nach=60 if unterschrift else 200, jc="center", weiter=bool(unterschrift),
                    links=ebene * EINZUG)
        if unterschrift:
            self.absatz(inline(unterschrift, Stil(kursiv=True, groesse=UNTERSCHRIFT)), nach=200, links=ebene * EINZUG)
        self.anzahl["Abbildungen"] += 1

    def abstand_nach_tabelle(self) -> None:
        self.teile.append('<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'
                          '<w:rPr><w:sz w:val="12"/><w:szCs w:val="12"/></w:rPr></w:pPr></w:p>')

    def b_tabelle(self, b: Block, ebene: int) -> None:
        einrueckung = ebene * EINZUG
        gesamt = self.textbreite - einrueckung
        kopf = [sichtbar(k) for k in b.kopf]
        self.anzahl["Tabellen"] += 1
        if (len(kopf) == 6 and kopf[0] in ("Teilaufgabe", "Teilaufg.", "Aufgabe")
                and kopf[2:5] == ["I", "II", "III"] and kopf[5] in ("Σ", "∑")):
            self.teile.append(self.erwartungshorizont(b, gesamt, einrueckung))
            self.abstand_nach_tabelle()
            return
        kopfspalte = len(kopf) >= 8
        spalten = [[(k, True)] + [(r[i], kopfspalte and i == 0) for r in b.zeilen] for i, k in enumerate(b.kopf)]
        groesse, rand = TABELLE, 85
        breiten, passt = spaltenbreiten(spalten, gesamt, groesse, rand)
        if not passt:                                   # breite Tabelle: 9 pt, schmale Zellränder
            groesse, rand = TABELLE - 2, 45
            breiten, _ = spaltenbreiten(spalten, gesamt, groesse, rand)
        zusammen = len(b.zeilen) <= 15                  # kleine Tabellen nicht über den Seitenwechsel teilen
        za = self.zellabsatz
        reihen = [reihe([zelle(za(k, a, True, groesse, zusammen), w, fuellung=GRAU_KOPF)
                         for k, a, w in zip(b.kopf, b.ausrichtung, breiten)], kopf=True)]
        for n, r in enumerate(b.zeilen):
            summe = all(re.fullmatch(r"\*\*.*\*\*", x.strip()) for x in r if x.strip())
            weiter = zusammen and n < len(b.zeilen) - 1
            zs = []
            for i, (x, a, w) in enumerate(zip(r, b.ausrichtung, breiten)):
                erste = kopfspalte and i == 0
                zs.append(zelle(za(x, a, erste, groesse, weiter), w,
                                fuellung=GRAU_KOPF if erste else GRAU_SUMME if summe and any(r) else ""))
            reihen.append(reihe(zs))
        self.teile.append(tabelle_xml(reihen, breiten, einrueckung, rand=rand))
        self.abstand_nach_tabelle()

    @staticmethod
    def zellabsatz(text: str, ausrichtung: str = "left", fett: bool = False, groesse: int = TABELLE,
                   weiter: bool = False) -> str:
        jc = {"right": "right", "center": "center"}.get(ausrichtung, "")
        return (f"<w:p>{ppr(vor=40, nach=40, zeile=240, jc=jc, weiter=weiter)}"
                f"{inline(text, Stil(fett=fett, groesse=groesse))}</w:p>")

    def erwartungshorizont(self, b: Block, gesamt: int, einrueckung: int) -> str:
        """Erwartungshorizont im Layout der Vorlage: zweizeiliger Kopf, Teilaufgabe und Σ verbunden,
        Summenzeilen grau über zwei Spalten."""
        breiten = [int(a * gesamt / sum(EWH_ANTEILE)) for a in EWH_ANTEILE]
        breiten[1] += gesamt - sum(breiten)
        za = self.zellabsatz
        reihen = [
            reihe([zelle(za(b.kopf[0], "center", True), breiten[0], fuellung=GRAU_EWH, vmerge="start", mitte=True),
                   zelle(za(b.kopf[1], "center", True), breiten[1], fuellung=GRAU_EWH, vmerge="start", mitte=True),
                   zelle(za("Anforderungsbereich<br>Bewertung", "center", True), sum(breiten[2:]),
                         fuellung=GRAU_EWH, spannweite=4)], kopf=True),
            reihe([zelle(za(""), breiten[0], fuellung=GRAU_EWH, vmerge="weiter"),
                   zelle(za(""), breiten[1], fuellung=GRAU_EWH, vmerge="weiter")]
                  + [zelle(za(k, "center", True), w, fuellung=GRAU_EWH) for k, w in zip(b.kopf[2:], breiten[2:])],
                  kopf=True)]

        def summenzeile(r: list[str]) -> bool:
            return bool(re.match(r"^(Summe|Gesamt|%)", sichtbar(r[0]), re.I))

        zeilen = b.zeilen
        for k, r in enumerate(zeilen):
            if summenzeile(r):
                reihen.append(reihe([zelle(za(r[0], fett=True), breiten[0] + breiten[1], fuellung=GRAU_EWH,
                                           spannweite=2)]
                                    + [zelle(za(x, "center", True), w, fuellung=GRAU_EWH)
                                       for x, w in zip(r[2:], breiten[2:])]))
                continue
            folge = k + 1 < len(zeilen) and not zeilen[k + 1][0].strip() and not summenzeile(zeilen[k + 1])
            fortsetzung = (not r[0].strip() and k > 0 and not summenzeile(zeilen[k - 1]))
            v0 = "weiter" if fortsetzung else "start" if folge else ""
            v5 = v0 if not r[5].strip() or v0 == "start" else ""
            zs = [zelle(za("" if fortsetzung else r[0], "center"), breiten[0], vmerge=v0, mitte=True),
                  zelle(za(r[1]), breiten[1])]
            zs += [zelle(za(x, "center"), w) for x, w in zip(r[2:5], breiten[2:5])]
            zs.append(zelle(za("" if v5 == "weiter" else r[5], "center", True), breiten[5], vmerge=v5, mitte=True))
            reihen.append(reihe(zs))
        return tabelle_xml(reihen, breiten, einrueckung, rahmen=8)


# ------------------------------------------------------------------------------ Vorlage (DOCX-Paket)

class Paket:
    def __init__(self, dateien: dict[str, bytes]):
        self.dateien = dateien

    @classmethod
    def laden(cls, pfad: Path) -> "Paket":
        with zipfile.ZipFile(pfad) as z:
            return cls({i.filename: z.read(i) for i in z.infolist() if not i.is_dir()})

    def text(self, name: str) -> str:
        return self.dateien[name].decode("utf-8")

    def setze(self, name: str, text: str) -> None:
        self.dateien[name] = text.encode("utf-8")

    def speichern(self, ziel: Path) -> None:
        namen = sorted(self.dateien, key=lambda n: (n != "[Content_Types].xml", n.startswith("word/media/"), n))
        with zipfile.ZipFile(ziel, "w", zipfile.ZIP_DEFLATED) as z:
            for name in namen:
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                z.writestr(info, self.dateien[name])


def _feld(befehl: str, ergebnis: str, st: Stil) -> str:
    return (f'<w:r>{rpr(st)}<w:fldChar w:fldCharType="begin"/></w:r>'
            f'<w:r>{rpr(st)}<w:instrText xml:space="preserve"> {befehl} </w:instrText></w:r>'
            f'<w:r>{rpr(st)}<w:fldChar w:fldCharType="separate"/></w:r>{lauf(ergebnis, st)}'
            f'<w:r>{rpr(st)}<w:fldChar w:fldCharType="end"/></w:r>')


def eingebaute_vorlage(art: str) -> Paket:
    """Schlichte Vorlage mit Kopf- und Fußzeile wie die der Behörde (gleiche Platzhalter)."""
    ns = (f'xmlns:w="{NS_W}" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" '
          f'xmlns:wp="{NS_WP}"')
    st, fett = Stil(groesse=20), Stil(groesse=20, fett=True)

    def kzelle(inhalt: str, breite: int) -> str:
        return zelle(inhalt, breite, fuellung=GRAU_KOPF)

    def kabsatz(inhalt: str, jc: str = "") -> str:
        return f"<w:p>{ppr(nach=0, zeile=240, jc=jc)}{inhalt}</w:p>"

    def ktabelle(reihen: list[str], breiten: list[int]) -> str:
        return (f'<w:tbl><w:tblPr><w:tblW w:w="{sum(breiten)}" w:type="dxa"/>'
                f'<w:tblCellSpacing w:w="15" w:type="dxa"/><w:tblLayout w:type="fixed"/></w:tblPr><w:tblGrid>'
                + "".join(f'<w:gridCol w:w="{b}"/>' for b in breiten) + "</w:tblGrid>" + "".join(reihen) + "</w:tbl>")

    b = [2000, 4500, 3137]
    kopf = ktabelle([
        reihe([kzelle(kabsatz(lauf("Abitur 2026", fett)), b[0]), kzelle(kabsatz(lauf("Technik - -", fett)), b[1]),
               kzelle(kabsatz(lauf(art, Stil(groesse=24, fett=True)), "right"), b[2])]),
        reihe([kzelle(kabsatz(lauf("Vorschlag ", fett) + lauf("A", fett)), b[0]), kzelle(kabsatz(lauf("eA", fett)), b[1]),
               kzelle(kabsatz(lauf("Bearbeitungszeit: 300 Min.", fett), "right"), b[2])])], b)
    fuss = ktabelle([reihe([
        kzelle(kabsatz(lauf("BBS ", fett) + lauf("…", fett) + lauf(" - Berufliches Gymnasium - Technik -", fett)), 6637),
        kzelle(kabsatz(lauf("Seite ", fett) + _feld("PAGE", "1", fett) + lauf(" von ", fett)
                       + _feld("NUMPAGES", "1", fett), "right"), 3000)])], [6637, 3000])
    fuss += kabsatz(_feld("FILENAME", "dokument.docx", Stil(groesse=14)), "right")
    sect = ('<w:sectPr><w:headerReference w:type="default" r:id="rId1"/><w:footerReference w:type="default" r:id="rId2"/>'
            '<w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1588" w:right="851" w:bottom="1531" w:left="1418" '
            'w:header="397" w:footer="680" w:gutter="0"/><w:cols w:space="720"/></w:sectPr>')
    typen = "application/vnd.openxmlformats-officedocument."
    dateien = {
        "[Content_Types].xml": XML_KOPF + (
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
            '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
            '<Default Extension="xml" ContentType="application/xml"/>'
            f'<Override PartName="/word/document.xml" ContentType="{typen}wordprocessingml.document.main+xml"/>'
            f'<Override PartName="/word/styles.xml" ContentType="{typen}wordprocessingml.styles+xml"/>'
            f'<Override PartName="/word/settings.xml" ContentType="{typen}wordprocessingml.settings+xml"/>'
            f'<Override PartName="/word/numbering.xml" ContentType="{typen}wordprocessingml.numbering+xml"/>'
            f'<Override PartName="/word/header1.xml" ContentType="{typen}wordprocessingml.header+xml"/>'
            f'<Override PartName="/word/footer1.xml" ContentType="{typen}wordprocessingml.footer+xml"/>'
            '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
            f'<Override PartName="/docProps/app.xml" ContentType="{typen}extended-properties+xml"/></Types>'),
        "_rels/.rels": XML_KOPF + (
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f'<Relationship Id="rId1" Type="{REL}/officeDocument" Target="word/document.xml"/>'
            '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" '
            'Target="docProps/core.xml"/>'
            f'<Relationship Id="rId3" Type="{REL}/extended-properties" Target="docProps/app.xml"/></Relationships>'),
        "word/_rels/document.xml.rels": XML_KOPF + (
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f'<Relationship Id="rId1" Type="{REL}/header" Target="header1.xml"/>'
            f'<Relationship Id="rId2" Type="{REL}/footer" Target="footer1.xml"/>'
            f'<Relationship Id="rId3" Type="{REL}/styles" Target="styles.xml"/>'
            f'<Relationship Id="rId4" Type="{REL}/settings" Target="settings.xml"/>'
            f'<Relationship Id="rId5" Type="{REL_NUMMERIERUNG}" Target="numbering.xml"/></Relationships>'),
        "word/document.xml": XML_KOPF + f"<w:document {ns}><w:body><w:p/>{sect}</w:body></w:document>",
        "word/styles.xml": XML_KOPF + (
            f'<w:styles xmlns:w="{NS_W}"><w:docDefaults><w:rPrDefault><w:rPr>'
            f'<w:rFonts w:ascii="{SCHRIFT}" w:hAnsi="{SCHRIFT}" w:eastAsia="{SCHRIFT}" w:cs="{SCHRIFT}"/>'
            '<w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="de-DE" w:eastAsia="de-DE" w:bidi="ar-SA"/>'
            '</w:rPr></w:rPrDefault><w:pPrDefault/></w:docDefaults>'
            '<w:style w:type="paragraph" w:default="1" w:styleId="Standard"><w:name w:val="Normal"/><w:qFormat/></w:style>'
            '<w:style w:type="table" w:default="1" w:styleId="NormaleTabelle"><w:name w:val="Normal Table"/>'
            '<w:tblPr><w:tblInd w:w="0" w:type="dxa"/><w:tblCellMar><w:top w:w="0" w:type="dxa"/>'
            '<w:left w:w="108" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/>'
            '</w:tblCellMar></w:tblPr></w:style></w:styles>'),
        "word/settings.xml": XML_KOPF + (
            f'<w:settings xmlns:w="{NS_W}"><w:defaultTabStop w:val="708"/><w:hyphenationZone w:val="425"/>'
            '<w:characterSpacingControl w:val="doNotCompress"/><w:compat><w:compatSetting w:name="compatibilityMode" '
            'w:uri="http://schemas.microsoft.com/office/word" w:val="15"/></w:compat></w:settings>'),
        "word/numbering.xml": XML_KOPF + f'<w:numbering xmlns:w="{NS_W}"></w:numbering>',
        "word/header1.xml": XML_KOPF + f"<w:hdr {ns}>{kopf}<w:p>{ppr(nach=0, zeile=240)}</w:p></w:hdr>",
        "word/footer1.xml": XML_KOPF + f"<w:ftr {ns}>{fuss}</w:ftr>",
        "docProps/core.xml": kern_xml("", "", "2026-01-01T00:00:00Z", False),
        "docProps/app.xml": XML_KOPF + (
            '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
            '<Application>abitur_docx.py</Application></Properties>'),
    }
    return Paket({k: v.encode("utf-8") for k, v in dateien.items()})


def kern_xml(titel: str, betreff: str, datum: str, vertraulich: bool) -> str:
    return XML_KOPF + (
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        f"<dc:title>{xml_text(titel)}</dc:title><dc:subject>{xml_text(betreff)}</dc:subject><dc:creator></dc:creator>"
        f"<cp:keywords>{'vertraulich' if vertraulich else ''}</cp:keywords><cp:lastModifiedBy></cp:lastModifiedBy>"
        f'<cp:revision>1</cp:revision><dcterms:created xsi:type="dcterms:W3CDTF">{datum}</dcterms:created>'
        f'<dcterms:modified xsi:type="dcterms:W3CDTF">{datum}</dcterms:modified></cp:coreProperties>')


WT = re.compile(r"(<w:t(?:\s[^>]*)?>)([^<]*)(</w:t>)")


def _absatz_ersetzen(p: str, neu: str) -> str:
    """Ganzen Absatztext ersetzen: Text in den ersten w:t, die übrigen leeren (Format des ersten Laufs)."""
    erster = [True]

    def ersetze(m: re.Match) -> str:
        if erster[0]:
            erster[0] = False
            return f'<w:t xml:space="preserve">{xml_text(neu)}</w:t>'
        return m.group(1) + m.group(3)
    return WT.sub(ersetze, p)


def beziehungen(rels: str) -> list[tuple[str, str]]:
    """(Typ, Ziel) je Beziehung – unabhängig von der Reihenfolge der Attribute."""
    aus = []
    for element in re.findall(r"<Relationship\b[^>]*>", rels):
        typ, ziel = re.search(r'\bType="([^"]+)"', element), re.search(r'\bTarget="([^"]+)"', element)
        if typ and ziel:
            aus.append((typ.group(1).rsplit("/", 1)[-1], "word/" + ziel.group(1).lstrip("/").removeprefix("word/")))
    return aus


def kopf_fuellen(xml: str, felder: dict[str, str], gefuellt: list[str]) -> str:
    """Platzhalter der Kopf- bzw. Fußzeile füllen (Jahr, Fach, Vorschlag, Niveau, Zeit, Schule, Dateiname)."""

    def absatz(m: re.Match) -> str:
        p = m.group(0)
        texte = WT.findall(p)
        if not texte:
            return p
        voll = "".join(html.unescape(t[1]) for t in texte)
        norm = " ".join(voll.split())
        if "FILENAME" in p and felder.get("dateiname"):
            gefuellt.append("Dateiname")
            return WT.sub(lambda t: (t.group(1) + xml_text(felder["dateiname"]) + t.group(3)
                                     if re.search(r"\.(docx?|dotx?)\s*$", html.unescape(t.group(2)), re.I)
                                     else t.group(0)), p)
        if re.fullmatch(r"Abitur\s*\d{4}", norm) and felder.get("jahr"):
            gefuellt.append(f"Abitur {felder['jahr']}")
            return _absatz_ersetzen(p, f"Abitur {felder['jahr']}")
        if re.fullmatch(r"Technik\s*-\s*-?", norm) and felder.get("fach"):
            gefuellt.append(felder["fach"])
            return _absatz_ersetzen(p, felder["fach"])
        if re.fullmatch(r"Vorschlag\s*[A-Z]?", norm) and felder.get("vorschlag"):
            gefuellt.append(f"Vorschlag {felder['vorschlag']}")
            if any(re.fullmatch(r"\s*[A-Z]\s*", html.unescape(t[1])) for t in texte):
                return WT.sub(lambda t: (t.group(1) + felder["vorschlag"] + t.group(3)
                                         if re.fullmatch(r"\s*[A-Z]\s*", html.unescape(t.group(2))) else t.group(0)), p)
            return _absatz_ersetzen(p, f"Vorschlag {felder['vorschlag']}")
        if re.fullmatch(r"[eg]A", norm) and felder.get("niveau"):
            gefuellt.append(felder["niveau"])
            return _absatz_ersetzen(p, felder["niveau"])
        if re.fullmatch(r"Bearbeitungszeit:?\s*\d*\s*(Min\.?|min)?", norm) and felder.get("zeit"):
            gefuellt.append(f"Bearbeitungszeit: {felder['zeit']} Min.")
            return _absatz_ersetzen(p, f"Bearbeitungszeit: {felder['zeit']} Min.")
        if norm in ("Schülermaterial", "Lehrermaterial") and felder.get("art") and norm != felder["art"]:
            gefuellt.append(felder["art"])
            return _absatz_ersetzen(p, felder["art"])
        if re.match(r"BBS\s*(…|\.\.\.)", norm) and felder.get("schule"):
            schule = felder["schule"]
            gefuellt.append(schule)
            return _absatz_ersetzen(p, re.sub(r"^\s*BBS\s*(…|\.\.\.)", lambda _: schule if schule.upper().startswith("BBS")
                                              else f"BBS {schule}", voll))
        return p

    return re.sub(r"<w:p\b[^>]*>.*?</w:p>", absatz, xml, flags=re.S)


def vorlage_waehlen(angabe: Path | None, art: str) -> Path | None:
    if angabe is None or angabe.is_file():
        return angabe
    if angabe.is_dir():
        schluessel = "schueler" if art == "Schülermaterial" else "lehrer"
        kandidaten = sorted(p for p in angabe.iterdir() if p.suffix.lower() in (".docx", ".dotx")
                            and not p.name.startswith((".", "~$")) and schluessel in p.name.lower())
        return kandidaten[0] if kandidaten else None
    return None


def textbreite_aus(sect: str) -> int:
    def wert(tag: str, name: str, standard: int) -> int:
        m = re.search(rf'<w:{tag}\b[^>]*\bw:{name}="(\d+)"', sect)
        return int(m.group(1)) if m else standard
    return wert("pgSz", "w", 11906) - wert("pgMar", "left", 1418) - wert("pgMar", "right", 1134) - wert("pgMar", "gutter", 0)


# ------------------------------------------------------------------------------ Umwandlung einer Datei

def material_art(md: Path, kopf: dict[str, str]) -> str:
    probe = (md.stem + " " + kopf.get("artefakt", "")).lower()
    if "lehrermaterial" in probe:
        return "Lehrermaterial"
    if "schuelermaterial" in probe or "schülermaterial" in probe:
        return "Schülermaterial"
    m = re.search(r"–\s*(.+)$", kopf.get("artefakt", ""))
    return m.group(1).strip() if m else "Lehrermaterial"


def fach_text(kopf: dict[str, str]) -> str:
    fach, schwerpunkt = kopf.get("fach", "").strip(), kopf.get("schwerpunkt", "").strip()
    if fach and schwerpunkt:
        return f"{fach} - {schwerpunkt} -"
    return fach


def umwandeln(md: Path, ziel: Path, vorlage: Path | None, schule: str, abbildungen: Path | None) -> tuple[int, list[str]]:
    """Eine Markdown-Datei → DOCX. Rückgabe: (Fehlerzahl, Meldungen)."""
    meldungen: list[str] = []
    kopf, rumpf = kopf_lesen(md.read_text(encoding="utf-8"))
    art = material_art(md, kopf)
    lehrer = art != "Schülermaterial"

    bloecke = bloecke_lesen(rumpf.splitlines())
    if (bloecke and bloecke[0].art == "tabelle" and bloecke[0].kopf
            and re.match(r"Abitur\s+\d{4}", sichtbar(bloecke[0].kopf[0]))):
        bloecke = bloecke[1:]
        meldungen.append("✔ Kopftabelle der Markdown-Datei entfällt – die Kopfzeile der Vorlage trägt die Angaben")
    bloecke = unterschriften_zuordnen(bloecke)
    bloecke = abbildungen_platzieren(bloecke, md, lehrer, abbildungen, meldungen)

    paket = Paket.laden(vorlage) if vorlage else eingebaute_vorlage(art)
    if not vorlage:
        meldungen.append("⚠ ohne Dokumentvorlage der Behörde (eingebaute Vorlage) – --vorlage angeben")
    dokument = paket.text("word/document.xml")
    m_rumpf = re.search(r"<w:body>(.*)</w:body>", dokument, re.S)
    alt_rumpf = m_rumpf.group(1)
    s = alt_rumpf.rfind("<w:sectPr")
    sect = alt_rumpf[s:] if s >= 0 and "</w:p>" not in alt_rumpf[s:] else ""
    if not sect:
        meldungen.append("⚠ Vorlage ohne Abschnittseigenschaften am Ende – Kopf- und Fußzeile prüfen")
    rels_name = "word/_rels/document.xml.rels"
    medien = Medien(paket.text(rels_name))
    num_ziel = next((ziel for typ, ziel in beziehungen(medien.rels) if typ == "numbering"), None)
    num_name = num_ziel or "word/numbering.xml"
    nummern = Nummerierung(paket.text(num_name) if num_name in paket.dateien else None)

    wandler = Wandler(textbreite_aus(sect), nummern, medien, md.parent)
    wandler.bloecke(bloecke)
    meldungen += wandler.fehler

    wurzel = dokument[:m_rumpf.start(1)]
    for praefix, ns in (("r", "http://schemas.openxmlformats.org/officeDocument/2006/relationships"), ("wp", NS_WP)):
        if f"xmlns:{praefix}=" not in wurzel:
            wurzel = re.sub(r"<w:document\b", f'<w:document xmlns:{praefix}="{ns}"', wurzel, count=1)
    paket.setze("word/document.xml", wurzel + "".join(wandler.teile) + sect + dokument[m_rumpf.end(1):])

    if nummern.neu_abstrakt:
        paket.setze(num_name, nummern.ergebnis())
        if not num_ziel:
            medien.beziehung("numbering.xml", REL_NUMMERIERUNG)
    paket.setze(rels_name, medien.rels)
    paket.dateien.update(medien.dateien)

    typen = paket.text("[Content_Types].xml")
    typen = typen.replace("wordprocessingml.template.main+xml", "wordprocessingml.document.main+xml")
    for endung in sorted(medien.endungen):
        if not re.search(rf'Extension="{endung}"', typen, re.I):
            typen = typen.replace("</Types>", f'<Default Extension="{endung}" ContentType="{INHALTSTYP[endung]}"/></Types>')
    if "/word/numbering.xml" not in typen and num_name == "word/numbering.xml" and nummern.neu_abstrakt:
        typen = typen.replace("</Types>", '<Override PartName="/word/numbering.xml" ContentType="application/'
                                          'vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/></Types>')
    paket.setze("[Content_Types].xml", typen)

    felder = {"jahr": kopf.get("pruefungsjahr", ""), "fach": fach_text(kopf), "vorschlag": kopf.get("vorschlag", ""),
              "niveau": kopf.get("niveau", ""), "zeit": kopf.get("bearbeitungszeit", ""), "art": art,
              "schule": schule or kopf.get("schule", ""), "dateiname": ziel.name}
    gefuellt: list[str] = []
    for typ, name in beziehungen(medien.rels):
        if typ in ("header", "footer") and name in paket.dateien:
            xml = kopf_fuellen(paket.text(name), felder, gefuellt)
            paket.setze(name, xml)
            if re.search(r"BBS\s*(…|\.\.\.)", "".join(html.unescape(t[1]) for t in WT.findall(xml))):
                meldungen.append("⚠ Fußzeile: Schulname „BBS …“ nicht ersetzt (--schule angeben)")
    if gefuellt:
        meldungen.insert(0, "✔ Kopf- und Fußzeile: " + " · ".join(dict.fromkeys(gefuellt)))

    titel = kopf.get("titel", md.stem)
    betreff = " – ".join(x for x in (f"Abitur {felder['jahr']}" if felder["jahr"] else "", felder["fach"].rstrip(" -"),
                                     f"Vorschlag {felder['vorschlag']}" if felder["vorschlag"] else "", art) if x)
    stand = kopf.get("stand", "")
    datum = f"{stand}T00:00:00Z" if re.fullmatch(r"\d{4}-\d{2}-\d{2}", stand) else dt.date.today().isoformat() + "T00:00:00Z"
    if "docProps/core.xml" in paket.dateien:
        paket.setze("docProps/core.xml", kern_xml(titel, betreff, datum, kopf.get("vertraulich", "") == "true"))
    if "docProps/app.xml" in paket.dateien:
        app = re.sub(r"<Company>.*?</Company>", "<Company></Company>", paket.text("docProps/app.xml"), flags=re.S)
        app = re.sub(r"(<TitlesOfParts>.*?<vt:lpstr>).*?(</vt:lpstr>)", lambda m: m.group(1) + xml_text(titel) + m.group(2),
                     app, flags=re.S)
        paket.setze("docProps/app.xml", app)

    for name, daten in paket.dateien.items():          # Selbstprüfung: alle XML-Teile wohlgeformt
        if name.endswith((".xml", ".rels")):
            try:
                ET.fromstring(daten)
            except ET.ParseError as e:
                raise RuntimeError(f"interner Fehler: {name} nicht wohlgeformt ({e})") from e
    paket.speichern(ziel)
    if medien.ohne_ersatzbild:
        meldungen.append("⚠ ohne PNG-Ersatzbild (rsvg-convert fehlt): " + ", ".join(medien.ohne_ersatzbild)
                         + " – Word ab 2016 zeigt SVG, LibreOffice und ältere Versionen ggf. nicht")
    meldungen.append("✔ " + ", ".join(f"{v} {k}" for k, v in wandler.anzahl.items()))
    return sum(1 for x in meldungen if x.startswith("✘")), meldungen


SEITEN_SM_MAX = 12


def seiten_zaehlen(docx: Path) -> tuple[int, int | None] | None:
    """(Seiten gesamt, Seite mit „B. Material“ bzw. der ersten Anlage) über LibreOffice; None ohne soffice."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice or not shutil.which("pdftotext"):
        return None
    with tempfile.TemporaryDirectory() as tmp:
        try:
            subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", tmp, str(docx)],
                           check=True, capture_output=True, timeout=300)
            pdf = Path(tmp) / (docx.stem + ".pdf")
            text = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], check=True, capture_output=True,
                                  timeout=120).stdout.decode("utf-8", "replace")
        except (OSError, subprocess.SubprocessError):
            return None
    seiten = text.split("\f")
    if seiten and not seiten[-1].strip():
        seiten = seiten[:-1]
    material = next((i + 1 for i, s in enumerate(seiten)
                     if re.search(r"^\s*(?:B\.\s*Material|Anlage\s+1\b\s*[–-])", s, re.M)), None)
    return len(seiten), material


def seiten_melden(docx: Path, art: str) -> str:
    erg = seiten_zaehlen(docx)
    if erg is None:
        return "Seitenzählung nicht ausgeführt (LibreOffice soffice bzw. pdftotext fehlt) – Seitenzahl in Word ablesen"
    gesamt, material = erg
    if art != "Schülermaterial":
        return f"{gesamt} Seiten"
    aufgaben = material or gesamt          # Seite, auf der das Material beginnt, zählt mit
    zeichen = "⚠" if aufgaben > SEITEN_SM_MAX else "✓"
    return (f"{zeichen} {gesamt} Seiten, Aufgabenteil bis Seite {aufgaben}, Anlagen und Hilfsmittel {gesamt - aufgaben} "
            f"weitere – Richtwert ≤ {SEITEN_SM_MAX} Seiten ohne Anlagen" + (" – kürzen" if aufgaben > SEITEN_SM_MAX else ""))


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("dateien", nargs="+", type=Path, help="Schüler- und/oder Lehrermaterial (Markdown)")
    p.add_argument("--vorlage", type=Path, default=Path(os.environ["ABITUR_VORLAGE"]) if os.environ.get("ABITUR_VORLAGE")
                   else None, help="DOCX-Vorlage der Behörde oder Ordner mit beiden Vorlagen (Standard: $ABITUR_VORLAGE)")
    p.add_argument("--schule", default="", help="Schule für die Fußzeile (ersetzt „BBS …“)")
    p.add_argument("--abbildungen", type=Path, help="Ordner der Abbildungen (Standard: abbildungen/ neben der Datei)")
    p.add_argument("-o", "--ausgabe", type=Path, help="Zieldatei (bei einer Eingabe) oder Zielordner")
    p.add_argument("--ueberschreiben", action="store_true", help="vorhandene DOCX-Datei ersetzen")
    p.add_argument("--seiten", action="store_true",
                   help="Seiten der Word-Fassung zählen (LibreOffice); Schülermaterial ohne Anlagen ≤ 12 Seiten")
    p.add_argument("--version", action="version", version=f"abitur_docx {VERSION}")
    a = p.parse_args(argv)
    if a.vorlage is not None and not a.vorlage.exists():
        print(f"✘ Vorlage nicht gefunden: {a.vorlage}")
        return 1
    if a.ausgabe and len(a.dateien) > 1 and a.ausgabe.suffix.lower() == ".docx":
        print("✘ -o mit Dateinamen nur bei einer Eingabedatei; sonst einen Ordner angeben")
        return 1
    fehler = 0
    for md in a.dateien:
        if not md.is_file():
            print(f"✘ Datei fehlt: {md}")
            fehler += 1
            continue
        art = material_art(md, kopf_lesen(md.read_text(encoding="utf-8"))[0])
        if a.ausgabe and a.ausgabe.suffix.lower() == ".docx":
            ziel = a.ausgabe
        elif a.ausgabe:
            a.ausgabe.mkdir(parents=True, exist_ok=True)
            ziel = a.ausgabe / (md.stem + ".docx")
        else:
            ziel = md.with_suffix(".docx")
        vorlage = vorlage_waehlen(a.vorlage, art)
        if a.vorlage is not None and vorlage is None:
            print(f"✘ {md.name}: im Ordner {a.vorlage} keine Vorlage mit „{'schueler' if art == 'Schülermaterial' else 'lehrer'}“ im Namen")
            fehler += 1
            continue
        if vorlage and vorlage.suffix.lower() == ".doc":
            print(f"✘ {vorlage.name}: bitte als .docx speichern")
            fehler += 1
            continue
        if ziel.exists() and not a.ueberschreiben:
            print(f"✘ {ziel} besteht schon – nicht überschrieben (--ueberschreiben)")
            fehler += 1
            continue
        anzahl, meldungen = umwandeln(md, ziel, vorlage, a.schule, a.abbildungen)
        print(f"{md.name} → {ziel}" + (f"  (Vorlage: {vorlage.name})" if vorlage else ""))
        for meldung in meldungen:
            print("  " + meldung)
        if a.seiten:
            print("  " + seiten_melden(ziel, art))
        fehler += anzahl
    if fehler:
        print(f"{fehler} Fehler – Word-Datei prüfen")
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())
