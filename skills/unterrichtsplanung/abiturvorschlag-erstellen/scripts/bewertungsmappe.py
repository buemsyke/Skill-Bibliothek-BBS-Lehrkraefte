#!/usr/bin/env python3
"""bewertungsmappe – Excel-Mappe für Korrektur, Bewertungsbogen und Gutachten eines dezentralen
Abiturvorschlags (lokal, deterministisch, ohne Makros).

Eine Quelle für alle Texte: Jedes Bewertungsmerkmal des Bewertungsrasters hat einen Kurztext
(Spalte „Kurztext“, höchstens vier Wörter, ohne Werte; fehlt er, schlägt das Skript einen vor –
Blatt „Korrekturschlüssel“). Ihn notiert die Korrektur am Rand der Klausur, und wörtlich
derselbe Text steht in den Bemerkungen je Teilaufgabe und im Gutachten – Erwartungshorizont,
Korrektur in der Klausur und Gutachten bleiben deckungsgleich.

Blätter: Start (Angaben, Einstellungen, Anleitung) · Korrekturschlüssel (Merkmale, Kurztexte,
Regeln) · Prüflinge · Erfassung (BE je Merkmal und Prüfling, Lösungsquoten) · Übersicht
(Notenpunkte, Grenzfälle, Notenspiegel) · P01 … (Bewertungsbogen und Gutachten je Prüfling) ·
Notenschlüssel (Bewertungsmaßstab) · Textbausteine.

Aufruf:
    python3 bewertungsmappe.py 75_…_A_bewertungsbogen.md [-o DATEI.xlsx] [--prueflinge 20]
    python3 bewertungsmappe.py 75_…_A_schuelermaterial.md 75_…_A_lehrermaterial.md [-o DATEI.xlsx]

Liegen neben dem Bewertungsbogen Schüler- und Lehrermaterial (und das Bewertungsraster) mit gleichem
Dateianfang, übernimmt das Skript Titel der Teilaufgaben, Art der Merkmale, Kurztexte, Regeln
(Toleranz, Folgefehler, Gleichwertig, 0 BE) und Zeilen des Erwartungshorizonts und gleicht
Bewertungsbogen und Bewertungsraster ab. Das Gutachten nennt standardmäßig nur teilweise und nicht
erfüllte Merkmale (kurz, weil es von Hand in die Klausur übertragen wird).
Die Mappe rechnet in Excel (ab 2010) und LibreOffice Calc. Überschreibt nie. Nur
Python-Standardbibliothek; liest und schreibt keine Daten von Prüflingen.
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import re
import sys
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from xml.sax.saxutils import escape

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER))
import abitur_check as AC  # noqa: E402 – gleicher Ordner (Parser, Bewertungsmaßstab)

VERSION = "1.1"
AFB = AC.AFB

# Farben (ohne Alpha)
EINGABE = "FFF2CC"
KOPF = "D9D9D9"
SUMME = "F2F2F2"
AUFGABE = "D6DCE4"
AFB_FARBE = {"I": "E2EFDA", "II": "DDEBF7", "III": "FCE4D6"}
TAB_EINGABE, TAB_PRUEFLING, TAB_REFERENZ = "BF9000", "8EA9DB", "A6A6A6"
ROT, ORANGE, GRAU_TEXT = "C00000", "C65911", "595959"

NOTE = {15: "1+", 14: "1", 13: "1-", 12: "2+", 11: "2", 10: "2-", 9: "3+", 8: "3", 7: "3-", 6: "4+",
        5: "4", 4: "4-", 3: "5+", 2: "5", 1: "5-", 0: "6"}
WORT = {1: "sehr gut", 2: "gut", 3: "befriedigend", 4: "ausreichend", 5: "mangelhaft", 6: "ungenügend"}


def stufe(np_: int) -> int:
    """Notenstufe 1–6 zu Notenpunkten 15–00."""
    return 6 if np_ == 0 else 5 - (np_ - 1) // 3


# ───────────────────────────── XLSX schreiben (OOXML) ─────────────────────────────

class Formel(str):
    """Zellinhalt, der als Formel geschrieben wird (ohne führendes =)."""


def sp(n: int) -> str:
    s = ""
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def adr(z: int, s: int, fest: bool = False) -> str:
    return f"${sp(s)}${z}" if fest else f"{sp(s)}{z}"


def bl(name: str) -> str:
    return "'" + name.replace("'", "''") + "'!"


def q(text: str) -> str:
    """Zeichenkette als Formel-Literal (Excel erlaubt höchstens 255 Zeichen je Literal)."""
    if len(text) > 255:
        raise ValueError(f"Formeltext zu lang ({len(text)} Zeichen): {text[:50]}…")
    return '"' + text.replace('"', '""') + '"'


def np_text(x: str) -> str:
    """Notenpunkte zweistellig als Text (05, 11)."""
    return f'IF({x}<10,"0","")&{x}'


def _xml(text: str) -> str:
    text = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", str(text))
    return escape(text, {'"': "&quot;"})


class Stile:
    FORMATE = {None: 0, "0": 1, "0.00": 2, "0%": 9, "0.00%": 10, "datum": 14}

    def __init__(self) -> None:
        self.fonts: list[tuple] = [(10, False, False, "FF000000")]
        self.fills: list[str | None] = [None, "gray125"]
        self.eigene: dict[str, int] = {}
        self.xfs: list[tuple] = [(0, 0, 0, 0, None, None, False, 0, True)]
        self.dxfs: list[tuple] = []

    @staticmethod
    def _index(liste: list, wert) -> int:
        if wert not in liste:
            liste.append(wert)
        return liste.index(wert)

    def __call__(self, fett=False, kursiv=False, groesse=10, farbe="000000", grund=None, rahmen=False,
                 h=None, v="top", umbruch=False, format=None, offen=False, drehung=0) -> int:
        font = self._index(self.fonts, (groesse, fett, kursiv, "FF" + farbe))
        fill = self._index(self.fills, "FF" + grund) if grund else 0
        if format in self.FORMATE:
            fmt = self.FORMATE[format]
        else:
            fmt = self.eigene.setdefault(format, 164 + len(self.eigene))
        rand = 2 if rahmen == "unten" else (1 if rahmen else 0)
        return self._index(self.xfs, (fmt, font, fill, rand, h, v, umbruch, drehung, not offen))

    def dxf(self, farbe: str | None = None, grund: str | None = None, fett: bool = False) -> int:
        return self._index(self.dxfs, (farbe, grund, fett))

    def xml(self) -> str:
        z = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>',
             '<styleSheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main">']
        if self.eigene:
            z.append(f'<numFmts count="{len(self.eigene)}">' + "".join(
                f'<numFmt numFmtId="{i}" formatCode="{_xml(c)}"/>' for c, i in self.eigene.items()) + "</numFmts>")
        z.append(f'<fonts count="{len(self.fonts)}">' + "".join(
            f'<font>{"<b/>" if b else ""}{"<i/>" if i else ""}<sz val="{g}"/><color rgb="{f}"/>'
            f'<name val="Arial"/><family val="2"/></font>' for g, b, i, f in self.fonts) + "</fonts>")
        fills = []
        for f in self.fills:
            if f is None:
                fills.append('<fill><patternFill patternType="none"/></fill>')
            elif f == "gray125":
                fills.append('<fill><patternFill patternType="gray125"/></fill>')
            else:
                fills.append(f'<fill><patternFill patternType="solid"><fgColor rgb="{f}"/>'
                             f'<bgColor indexed="64"/></patternFill></fill>')
        z.append(f'<fills count="{len(fills)}">' + "".join(fills) + "</fills>")
        linie = '<{0} style="thin"><color rgb="FFA6A6A6"/></{0}>'
        z.append('<borders count="3"><border><left/><right/><top/><bottom/><diagonal/></border><border>' +
                 "".join(linie.format(s) for s in ("left", "right", "top", "bottom")) + "<diagonal/></border>"
                 '<border><left/><right/><top/><bottom style="thin"><color rgb="FF000000"/></bottom><diagonal/>'
                 "</border></borders>")
        z.append('<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>')
        xfs = []
        for fmt, font, fill, border, h, v, umbruch, drehung, gesperrt in self.xfs:
            ausr = "".join([f' horizontal="{h}"' if h else "", f' vertical="{v}"' if v else "",
                            ' wrapText="1"' if umbruch else "", f' textRotation="{drehung}"' if drehung else ""])
            xfs.append(f'<xf numFmtId="{fmt}" fontId="{font}" fillId="{fill}" borderId="{border}" xfId="0" '
                       'applyNumberFormat="1" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1" '
                       f'applyProtection="1"><alignment{ausr}/><protection locked="{1 if gesperrt else 0}"/></xf>')
        z.append(f'<cellXfs count="{len(xfs)}">' + "".join(xfs) + "</cellXfs>")
        z.append('<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>')
        dx = []
        for farbe, grund, fett in self.dxfs:
            font = (f'<font>{"<b/>" if fett else ""}' + (f'<color rgb="FF{farbe}"/>' if farbe else "") + "</font>"
                    if farbe or fett else "")
            fill = (f'<fill><patternFill patternType="solid"><bgColor rgb="FF{grund}"/></patternFill></fill>'
                    if grund else "")
            dx.append(f"<dxf>{font}{fill}</dxf>")
        z.append(f'<dxfs count="{len(dx)}">' + "".join(dx) + "</dxfs>")
        z.append("</styleSheet>")
        return "".join(z)


class Blatt:
    def __init__(self, name: str, farbe: str | None = None) -> None:
        if len(name) > 31 or re.search(r"[\[\]:*?/\\]", name):
            raise ValueError(f"ungültiger Blattname: {name}")
        self.name, self.farbe = name, farbe
        self.zellen: dict[tuple[int, int], tuple[object, int]] = {}
        self.breite: dict[int, float] = {}
        self.versteckt: set[int] = set()
        self.hoehe: dict[int, float] = {}
        self.verbund: list[str] = []
        self.bedingt: list[tuple[str, str, int]] = []
        self.pruefungen: list[dict] = []
        self.fix: tuple[int, int] | None = None
        self.umbrueche: list[int] = []
        self.quer = False
        self.druckbereich: tuple[int, int] | None = None   # (letzte Zeile, letzte Spalte)
        self.titelzeilen: tuple[int, int] | None = None
        self.fuss = ""
        self.schutz = True

    def setze(self, z: int, s: int, wert=None, stil: int = 0) -> None:
        if isinstance(wert, Formel) and len(wert) > 8000:
            raise ValueError(f"Formel zu lang in {self.name}!{adr(z, s)}")
        self.zellen[(z, s)] = (wert, stil)

    def verbinde(self, z1: int, s1: int, z2: int, s2: int, wert=None, stil: int = 0) -> None:
        for z in range(z1, z2 + 1):
            for s in range(s1, s2 + 1):
                self.zellen[(z, s)] = (None, stil)
        self.setze(z1, s1, wert, stil)
        if (z1, s1) != (z2, s2):
            self.verbund.append(f"{adr(z1, s1)}:{adr(z2, s2)}")

    def bedingung(self, bereich: str, formel: str, dxf: int) -> None:
        self.bedingt.append((bereich, formel, dxf))

    def pruefung(self, bereich: str, typ: str, formel1: str, formel2: str | None = None, fehler: bool = True,
                 meldung: str = "", hinweis: str = "") -> None:
        self.pruefungen.append({"bereich": bereich, "typ": typ, "f1": formel1, "f2": formel2,
                                "fehler": fehler, "meldung": meldung, "hinweis": hinweis})

    def xml(self, sst: dict[str, int], aktiv: bool) -> str:
        z = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
             'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">']
        z.append("<sheetPr>" + (f'<tabColor rgb="FF{self.farbe}"/>' if self.farbe else "") +
                 '<pageSetUpPr fitToPage="1"/></sheetPr>')
        zmax = max((k[0] for k in self.zellen), default=1)
        smax = max((k[1] for k in self.zellen), default=1)
        z.append(f'<dimension ref="A1:{adr(zmax, smax)}"/>')
        ausgewaehlt = ' tabSelected="1"' if aktiv else ""
        ansicht = f'<sheetView workbookViewId="0"{ausgewaehlt}>'
        if self.fix:
            fz, fs = self.fix
            teil = []
            if fs > 1:
                teil.append(f'xSplit="{fs - 1}"')
            if fz > 1:
                teil.append(f'ySplit="{fz - 1}"')
            feld = "bottomRight" if fs > 1 and fz > 1 else ("bottomLeft" if fz > 1 else "topRight")
            ansicht += (f'<pane {" ".join(teil)} topLeftCell="{adr(fz, fs)}" activePane="{feld}" state="frozen"/>'
                        f'<selection pane="{feld}" activeCell="{adr(fz, fs)}" sqref="{adr(fz, fs)}"/>')
        z.append(f"<sheetViews>{ansicht}</sheetView></sheetViews>")
        z.append('<sheetFormatPr defaultRowHeight="12.75"/>')
        spalten = sorted(set(self.breite) | self.versteckt)
        if spalten:
            versteckt = ' hidden="1"'
            z.append("<cols>" + "".join(
                f'<col min="{s}" max="{s}" width="{self.breite.get(s, 9)}" customWidth="1"'
                f'{versteckt if s in self.versteckt else ""}/>' for s in spalten) + "</cols>")
        zeilen: dict[int, list[int]] = {}
        for (zz, ss) in self.zellen:
            zeilen.setdefault(zz, []).append(ss)
        for zz in self.hoehe:
            zeilen.setdefault(zz, [])
        daten = []
        for zz in sorted(zeilen):
            attr = f' ht="{self.hoehe[zz]}" customHeight="1"' if zz in self.hoehe else ""
            zellen = []
            for ss in sorted(zeilen[zz]):
                wert, stil = self.zellen[(zz, ss)]
                r = adr(zz, ss)
                s = f' s="{stil}"' if stil else ""
                if isinstance(wert, Formel):
                    zellen.append(f'<c r="{r}"{s}><f>{_xml(wert)}</f></c>')
                elif isinstance(wert, str):
                    nr = sst.setdefault(wert, len(sst))
                    zellen.append(f'<c r="{r}"{s} t="s"><v>{nr}</v></c>')
                elif isinstance(wert, bool):
                    zellen.append(f'<c r="{r}"{s} t="b"><v>{int(wert)}</v></c>')
                elif isinstance(wert, (int, float)):
                    zahl = int(wert) if float(wert).is_integer() else repr(float(wert))
                    zellen.append(f'<c r="{r}"{s}><v>{zahl}</v></c>')
                else:
                    zellen.append(f'<c r="{r}"{s}/>')
            daten.append(f'<row r="{zz}"{attr}>' + "".join(zellen) + "</row>")
        z.append("<sheetData>" + "".join(daten) + "</sheetData>")
        if self.schutz:
            z.append('<sheetProtection sheet="1" objects="1" scenarios="1" formatColumns="0" formatRows="0"/>')
        if self.verbund:
            z.append(f'<mergeCells count="{len(self.verbund)}">' +
                     "".join(f'<mergeCell ref="{v}"/>' for v in self.verbund) + "</mergeCells>")
        for prio, (bereich, formel, dxf) in enumerate(self.bedingt, 1):
            z.append(f'<conditionalFormatting sqref="{bereich}"><cfRule type="expression" dxfId="{dxf}" '
                     f'priority="{prio}"><formula>{_xml(formel)}</formula></cfRule></conditionalFormatting>')
        if self.pruefungen:
            z.append(f'<dataValidations count="{len(self.pruefungen)}">')
            for p in self.pruefungen:
                attr = (f'type="{p["typ"]}" allowBlank="1" showInputMessage="1" '
                        f'showErrorMessage="{1 if p["fehler"] else 0}"')
                if p["typ"] in ("decimal", "whole", "date"):
                    attr += ' operator="between"'
                if p["meldung"]:
                    attr += f' errorTitle="Eingabe prüfen" error="{_xml(p["meldung"])}"'
                if p["hinweis"]:
                    attr += f' prompt="{_xml(p["hinweis"])}"'
                inhalt = f"<formula1>{_xml(p['f1'])}</formula1>"
                if p["f2"] is not None:
                    inhalt += f"<formula2>{_xml(p['f2'])}</formula2>"
                z.append(f'<dataValidation {attr} sqref="{p["bereich"]}">{inhalt}</dataValidation>')
            z.append("</dataValidations>")
        z.append('<pageMargins left="0.55" right="0.45" top="0.6" bottom="0.6" header="0.3" footer="0.3"/>')
        z.append(f'<pageSetup paperSize="9" orientation="{"landscape" if self.quer else "portrait"}" '
                 'fitToWidth="1" fitToHeight="0"/>')
        if self.fuss:
            z.append(f"<headerFooter><oddFooter>{_xml(self.fuss)}</oddFooter></headerFooter>")
        if self.umbrueche:
            z.append(f'<rowBreaks count="{len(self.umbrueche)}" manualBreakCount="{len(self.umbrueche)}">' +
                     "".join(f'<brk id="{r - 1}" max="16383" man="1"/>' for r in self.umbrueche) + "</rowBreaks>")
        z.append("</worksheet>")
        return "".join(z)


class Mappe:
    def __init__(self) -> None:
        self.stil = Stile()
        self.blaetter: list[Blatt] = []
        self.namen: dict[str, str] = {}

    def blatt(self, name: str, farbe: str | None = None) -> Blatt:
        b = Blatt(name, farbe)
        self.blaetter.append(b)
        return b

    def name(self, name: str, blatt: Blatt, bereich: str) -> str:
        self.namen[name] = bl(blatt.name) + bereich
        return name

    def speichern(self, pfad: Path, titel: str, reihenfolge: list[str]) -> None:
        nach_name = {b.name: b for b in self.blaetter}
        blaetter = [nach_name[n] for n in reihenfolge]
        sst: dict[str, int] = {}
        teile = {f"xl/worksheets/sheet{i}.xml": b.xml(sst, i == 1) for i, b in enumerate(blaetter, 1)}
        definiert = []
        for i, b in enumerate(blaetter):
            if b.druckbereich:
                zl, sl = b.druckbereich
                definiert.append(f'<definedName name="_xlnm.Print_Area" localSheetId="{i}">'
                                 f'{_xml(bl(b.name))}$A$1:${sp(sl)}${zl}</definedName>')
            if b.titelzeilen:
                definiert.append(f'<definedName name="_xlnm.Print_Titles" localSheetId="{i}">'
                                 f'{_xml(bl(b.name))}${b.titelzeilen[0]}:${b.titelzeilen[1]}</definedName>')
        definiert += [f'<definedName name="{n}">{_xml(ziel)}</definedName>' for n, ziel in sorted(self.namen.items())]
        arbeitsmappe = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
            'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
            '<workbookPr/><bookViews><workbookView xWindow="0" yWindow="0" windowWidth="28800" '
            'windowHeight="16000" activeTab="0"/></bookViews><sheets>' +
            "".join(f'<sheet name="{_xml(b.name)}" sheetId="{i}" r:id="rId{i}"/>' for i, b in enumerate(blaetter, 1)) +
            "</sheets>" + (f"<definedNames>{''.join(definiert)}</definedNames>" if definiert else "") +
            '<calcPr calcId="191029" fullCalcOnLoad="1"/></workbook>')
        n = len(blaetter)
        wb_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">' +
                   "".join(f'<Relationship Id="rId{i}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                           f'relationships/worksheet" Target="worksheets/sheet{i}.xml"/>' for i in range(1, n + 1)) +
                   f'<Relationship Id="rId{n + 1}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                   'relationships/styles" Target="styles.xml"/>'
                   f'<Relationship Id="rId{n + 2}" Type="http://schemas.openxmlformats.org/officeDocument/2006/'
                   'relationships/sharedStrings" Target="sharedStrings.xml"/></Relationships>')
        strings = sorted(sst, key=sst.get)
        sst_xml = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                   f'<sst xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" count="{len(strings)}" '
                   f'uniqueCount="{len(strings)}">' +
                   "".join(f'<si><t xml:space="preserve">{_xml(s)}</t></si>' for s in strings) + "</sst>")
        typen = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                 '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
                 '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
                 '<Default Extension="xml" ContentType="application/xml"/>'
                 '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.'
                 'spreadsheetml.sheet.main+xml"/>' +
                 "".join(f'<Override PartName="/xl/worksheets/sheet{i}.xml" ContentType="application/'
                         'vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>' for i in range(1, n + 1)) +
                 '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.'
                 'spreadsheetml.styles+xml"/>'
                 '<Override PartName="/xl/sharedStrings.xml" ContentType="application/vnd.openxmlformats-'
                 'officedocument.spreadsheetml.sharedStrings+xml"/>'
                 '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.'
                 'core-properties+xml"/>'
                 '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-'
                 'officedocument.extended-properties+xml"/></Types>')
        rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
                '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
                'officeDocument" Target="xl/workbook.xml"/>'
                '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/'
                'metadata/core-properties" Target="docProps/core.xml"/>'
                '<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/'
                'extended-properties" Target="docProps/app.xml"/></Relationships>')
        jetzt = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        core = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
                '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
                'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
                'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
                f"<dc:title>{_xml(titel)}</dc:title><dc:creator>bewertungsmappe.py {VERSION}</dc:creator>"
                f'<dcterms:created xsi:type="dcterms:W3CDTF">{jetzt}</dcterms:created></cp:coreProperties>')
        app = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties">'
               "<Application>Microsoft Excel</Application></Properties>")
        with zipfile.ZipFile(pfad, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("[Content_Types].xml", typen)
            zf.writestr("_rels/.rels", rels)
            zf.writestr("docProps/core.xml", core)
            zf.writestr("docProps/app.xml", app)
            zf.writestr("xl/workbook.xml", arbeitsmappe)
            zf.writestr("xl/_rels/workbook.xml.rels", wb_rels)
            zf.writestr("xl/styles.xml", self.stil.xml())
            for name, inhalt in teile.items():
                zf.writestr(name, inhalt)
            zf.writestr("xl/sharedStrings.xml", sst_xml)


def hoehe(laenge: int, breite: float, reserve: int = 0) -> float | None:
    """Zeilenhöhe in pt für umbrochenen Text (Arial 10); None = Standardhöhe."""
    zeilen = max(1, math.ceil(laenge / max(8, breite * 1.05))) + reserve
    return None if zeilen == 1 else round(12.75 * zeilen + 2, 2)


def setze_hoehe(b: Blatt, z: int, laenge: int, breite: float, reserve: int = 0) -> None:
    h = hoehe(laenge, breite, reserve)
    if h:
        b.hoehe[z] = max(h, b.hoehe.get(z, 0))


# ───────────────────────────── Modell ─────────────────────────────

BEISPIEL = re.compile(r"\s*\((?:z\.\s?B\.|zum Beispiel|etwa|bspw\.|Musterlösung|vgl\.)[^()]*\)", re.I)


def kurztext(text: str) -> str:
    """Kurztext-Vorschlag für Randvermerk und Gutachten (wenn das Raster keinen nennt): ohne Beispiele,
    Werte und Nachsätze, höchstens vier Wörter."""
    return AC.kurztext_vorschlag(BEISPIEL.sub("", text))


@dataclass
class Merkmal:
    teil: str
    nr: str
    text: str
    afb: str
    be: float
    art: str = ""
    kurztext: str = ""

    @property
    def kurz(self) -> str:
        return self.kurztext or kurztext(self.text)


@dataclass
class Teilaufgabe:
    nummer: str
    titel: str = ""
    merkmale: list[Merkmal] = field(default_factory=list)
    ewh: list[str] = field(default_factory=list)
    regeln: list[tuple[str, str]] = field(default_factory=list)

    @property
    def be(self) -> float:
        return sum(m.be for m in self.merkmale)


@dataclass
class Aufgabe:
    nummer: int
    titel: str
    be: float | None
    teile: list[Teilaufgabe] = field(default_factory=list)

    @property
    def summe(self) -> float:
        return sum(t.be for t in self.teile)

    @property
    def merkmale(self) -> list[Merkmal]:
        return [m for t in self.teile for m in t.merkmale]


@dataclass
class Vorschlag:
    kopf: str
    aufgaben: list[Aufgabe]
    thema: str = ""
    quellen: list[str] = field(default_factory=list)
    hinweise: list[str] = field(default_factory=list)

    @property
    def teile(self) -> list[Teilaufgabe]:
        return [t for a in self.aufgaben for t in a.teile]

    @property
    def merkmale(self) -> list[Merkmal]:
        return [m for a in self.aufgaben for m in a.merkmale]

    @property
    def gesamt(self) -> float:
        return sum(a.summe for a in self.aufgaben)

    def afb(self, bereich: str) -> float:
        return sum(m.be for m in self.merkmale if m.afb == bereich)


AUFGABE_BB = re.compile(r"^##\s+(\d+)\.\s*Aufgabe\s*[–-]?\s*(.*?)\s*(?:\((\d+(?:[.,]\d+)?)\s*BE\))?\s*$")


def lies_bewertungsbogen(text: str) -> Vorschlag:
    text = AC.bereinigt(text)
    k = re.search(r"^#\s+Bewertungsbogen\s*[–-]\s*(.+?)\s*$", text, re.M)
    aufgaben: list[Aufgabe] = []
    sp_ = {"nr": 1, "text": 2, "kurz": None, "afb": 3, "be": 4}      # ältere Bögen ohne Spalte „Kurztext“
    for zeile in text.splitlines():
        if m := AUFGABE_BB.match(zeile):
            aufgaben.append(Aufgabe(int(m.group(1)), m.group(2).strip(" –-"), AC.zahl(m.group(3))))
            continue
        if not aufgaben or not zeile.strip().startswith("|"):
            continue
        z = AC.zellen(zeile)
        kopf = [k.lower() for k in z]
        if any("bewertungsmerkmal" in k for k in kopf) and "afb" in kopf:
            sp_ = {"nr": next((i for i, k in enumerate(kopf) if k.startswith("nr")), 1),
                   "text": next(i for i, k in enumerate(kopf) if "bewertungsmerkmal" in k),
                   "kurz": next((i for i, k in enumerate(kopf) if "kurz" in k), None), "afb": kopf.index("afb"),
                   "be": next((i for i, k in enumerate(kopf) if "erreichbar" in k or k == "be"), kopf.index("afb") + 1)}
            continue
        z += [""] * (max(i for i in sp_.values() if i is not None) + 1 - len(z))
        if not re.fullmatch(r"\d+\.\d+", z[0]) or AC.zahl(z[sp_["be"]]) is None:
            continue
        a = aufgaben[-1]
        if not a.teile or a.teile[-1].nummer != z[0]:
            a.teile.append(Teilaufgabe(z[0]))
        a.teile[-1].merkmale.append(Merkmal(z[0], z[sp_["nr"]], z[sp_["text"]], z[sp_["afb"]].strip().upper(),
                                            AC.zahl(z[sp_["be"]]),
                                            kurztext=z[sp_["kurz"]].strip() if sp_["kurz"] is not None else ""))
    return Vorschlag(k.group(1).strip() if k else "", [a for a in aufgaben if a.teile])


REGEL = re.compile(r"^\*([^*:]{2,30}):\*\s*(.+)$", re.S)


def regeln(text: str) -> list[tuple[str, str]]:
    erg = []
    for absatz in re.split(r"\n\s*\n", text):
        a = " ".join(absatz.split())
        if m := REGEL.match(a):
            erg.append((m.group(1).strip(), re.sub(r"[*`]", "", m.group(2)).strip()))
    return erg


def kopfdaten(text: str) -> dict[str, str]:
    m = re.match(r"\A﻿?---\n(.*?)\n---\n", text, re.S)
    return {mm.group(1): mm.group(2).strip().strip('"') for z in (m.group(1).splitlines() if m else [])
            if (mm := re.match(r"^(\w+):\s*(.*)$", z))}


def pruefe_eingabe(v: Vorschlag) -> None:
    if not v.merkmale:
        raise SystemExit("Keine Bewertungsmerkmale gefunden (Tabellen „Teilaufgabe | Nr. | Bewertungsmerkmal | "
                         "AFB | erreichbar | erreicht“ unter „## 1. Aufgabe – …“).")
    falsch = [f"{m.teil}/{m.nr}" for m in v.merkmale if m.afb not in AFB or m.be <= 0 or (m.be * 2) % 1]
    if falsch:
        v.hinweise.append("Merkmale ohne gültigen AFB (I, II, III) oder mit BE ≤ 0 bzw. nicht in halben BE: " +
                          ", ".join(falsch))
    for a in v.aufgaben:
        if a.be is not None and abs(a.be - a.summe) > 1e-9:
            v.hinweise.append(f"{a.nummer}. Aufgabe: Merkmale ergeben {AC.fmt(a.summe)} BE, angegeben {AC.fmt(a.be)} BE")


def anreichern(v: Vorschlag, sm_text: str, lm_text: str, raster_text: str | None = None) -> None:
    """Titel, Art, Kurztexte, Regeln und Erwartungshorizont aus Schüler-, Lehrermaterial und Bewertungsraster;
    Abgleich mit dem Bogen."""
    opdaten = AC.lade_operatoren(AC.operatorenpfad(None))
    befunde, _info, modell, _ = AC.pruefe(sm_text, lm_text, opdaten, raster_text=raster_text)
    quelle = "Bewertungsraster" if raster_text is not None else "Lehrermaterial"
    sm, lm = modell["sm"], modell["lm"]
    titel = {t.nummer: t.titel for a in sm["aufgaben"] for t in a.teile}
    ewh: dict[str, list[str]] = {}
    for e in lm["ewh"]:
        anteile = ", ".join(f"{k} {AC.fmt(e.afb[k])}" for k in AFB if e.afb.get(k))
        ewh.setdefault(e.teil, []).append(f"{e.text} ({anteile})" if anteile else e.text)
    abweichend = []
    for t in v.teile:
        t.titel = titel.get(t.nummer, "")
        t.ewh = ewh.get(t.nummer, [])
        loesung = modell["bewertung"].get(t.nummer, {})
        t.regeln = regeln(loesung.get("text", ""))
        lm_m = {m.nr: m for m in loesung.get("merkmale", [])}
        for m in t.merkmale:
            g = lm_m.get(m.nr)
            if g:
                m.art = g.art
                m.kurztext = m.kurztext or g.kurz
            if not g or (g.text, g.afb, g.be) != (m.text, m.afb, m.be):
                abweichend.append(f"{t.nummer}/{m.nr}")
        abweichend += [f"{t.nummer}/{nr}" for nr in lm_m if nr not in {m.nr for m in t.merkmale}]
    abweichend += [nr for nr, b in modell["bewertung"].items() if b["merkmale"] and nr not in {t.nummer for t in v.teile}]
    if abweichend:
        v.hinweise.append(f"Bewertungsbogen weicht vom {quelle} ab (" + ", ".join(abweichend[:8]) +
                          (" …" if len(abweichend) > 8 else "") + ") – mit abitur_check.py --bewertungsbogen neu "
                          "erzeugen und die Mappe danach erstellen")
    kd = kopfdaten(lm_text)
    v.thema = kd.get("titel") or sm.get("thema", "")
    mass = lm.get("massstab") or {}
    if mass.get("be"):
        soll = [be for _, _, be in AC.grenzen(v.gesamt)]
        if [x for x in mass["be"] if x is not None] != soll:
            v.hinweise.append("Bewertungsmaßstab im Lehrermaterial weicht von der Rechnung ab – die Mappe rechnet "
                              "mit den Grenzen aus abitur_check.py (auf halbe BE aufgerundet)")
    fehler = [b.kriterium for b in befunde if b.status == "❌"]
    if fehler:
        v.hinweise.append(f"Selbstprüfung meldet {len(fehler)} × ❌ ({', '.join(fehler)}) – vor der Korrektur "
                          "beheben (abitur_check.py)")


# ───────────────────────────── Blätter ─────────────────────────────

class Ablage:
    """Adressen, die andere Blätter brauchen."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.kurz: dict[int, str] = {}          # Merkmal-Index → Zelle Kurztext
        self.e_zeile: dict[int, int] = {}       # Merkmal-Index → Zeile in „Erfassung“
        self.e_aufgabe: dict[int, int] = {}     # Aufgabe → Summenzeile in „Erfassung“
        self.e_afb: dict[str, int] = {}
        self.e_gesamt = self.e_np = self.e_anzahl = self.e_status = 0
        self.e_spalte0 = 7

    def e_spalte(self, i: int) -> int:
        return self.e_spalte0 + i - 1

    @staticmethod
    def p_zeile(i: int) -> int:
        return 4 + i


def blatt_notenschluessel(mp: Mappe, v: Vorschlag) -> None:
    S = mp.stil
    b = mp.blatt("Notenschlüssel", TAB_REFERENZ)
    b.breite = {1: 12, 2: 11, 3: 10, 4: 8, 5: 15, 6: 11}
    b.setze(1, 1, f"Notenschlüssel – Bewertungsmaßstab für {AC.fmt(v.gesamt)} BE", S(fett=True, groesse=12, v=None))
    b.verbinde(2, 1, 2, 6, "Prozentgrenzen 95 … 45/40/33/27/20 %, Grenzen in BE auf halbe BE aufgerundet – wie der "
               "Bewertungsmaßstab im Lehrermaterial (abitur_check.py). Die Notenpunkte ergeben sich aus den "
               "erreichten BE.", S(kursiv=True, umbruch=True))
    b.hoehe[2] = 40
    kopf = ["Notenpunkte", "ab Prozent", "ab BE", "Note", "Notenwort", "Notenstufe"]
    for s, t in enumerate(kopf, 1):
        b.setze(4, s, t, S(fett=True, grund=KOPF, rahmen=True, h="center", umbruch=True))
    zelle = S(rahmen=True, h="center")
    for i, (np_, proz, be) in enumerate(AC.grenzen(v.gesamt)):
        z, n = 5 + i, int(np_)
        b.setze(z, 1, n, S(rahmen=True, h="center", format="00"))
        b.setze(z, 2, proz, zelle)
        b.setze(z, 3, be, zelle)
        b.setze(z, 4, NOTE[n], zelle)
        b.setze(z, 5, WORT[stufe(n)], S(rahmen=True))
        b.setze(z, 6, stufe(n), zelle)
    mp.name("NS_Prozent", b, "$B$5:$B$19")
    mp.name("NS_BE", b, "$C$5:$C$19")
    mp.name("NS_Note", b, "$D$5:$D$20")
    mp.name("NS_Wort", b, "$E$5:$E$20")
    mp.name("NS_Stufe", b, "$F$5:$F$20")
    b.druckbereich = (20, 6)


def blatt_textbausteine(mp: Mappe) -> None:
    S = mp.stil
    b = mp.blatt("Textbausteine", TAB_REFERENZ)
    b.breite = {1: 34, 2: 78, 3: 40}
    b.setze(1, 1, "Textbausteine für Bemerkungen und Gutachten", S(fett=True, groesse=12, v=None))
    b.verbinde(2, 1, 2, 3, "Gelbe Felder sind änderbar und wirken in allen Blättern P01 … – vor dem ersten Einsatz mit "
               "der Fachgruppe abstimmen. Die Kurztexte je Merkmal stehen im Blatt „Korrekturschlüssel“.",
               S(kursiv=True, umbruch=True))
    b.hoehe[2] = 27
    feld, label, notiz = S(grund=EINGABE, rahmen=True, umbruch=True, offen=True), S(umbruch=True), \
        S(kursiv=True, farbe=GRAU_TEXT, umbruch=True)
    z = 4

    def titel(text: str) -> None:
        nonlocal z
        z += 1
        b.verbinde(z, 1, z, 3, text, S(fett=True, grund=KOPF))
        z += 1

    def eintrag(text: str, wert, name: str | None = None, hinweis: str = "", stil: int | None = None) -> int:
        nonlocal z
        b.setze(z, 1, text, label)
        b.setze(z, 2, wert, feld if stil is None else stil)
        if hinweis:
            b.setze(z, 3, hinweis, notiz)
        setze_hoehe(b, z, max(len(str(wert)), 1), 78)
        if name:
            mp.name(name, b, f"$B${z}")
        z += 1
        return z - 1

    titel("Korrekturzeichen (Rand der Klausur, Spalte „Vermerk“)")
    eintrag("erfüllt (volle BE)", "✓", "Zeichen_voll")
    eintrag("teilweise erfüllt (BE dazuschreiben)", "(✓)", "Zeichen_teilweise")
    eintrag("nicht erfüllt (0 BE)", "✗", "Zeichen_nicht")
    titel("Bemerkungen je Teilaufgabe")
    eintrag("Einleitung erfüllte Merkmale", "Erfüllt:", "Text_erfuellt")
    eintrag("Einleitung teilweise erfüllte Merkmale", "Teilweise erfüllt:", "Text_teilweise")
    eintrag("Einleitung nicht erfüllte Merkmale", "Nicht erfüllt:", "Text_nicht")
    eintrag("Einleitung noch offene Merkmale", "Noch nicht bewertet:", "Text_offen")
    eintrag("ohne Bewertung", "noch nicht bewertet", "Text_unbewertet")
    eintrag("Hinweis bei unvollständiger Bewertung", "Bewertung unvollständig.", "Text_unvollstaendig")
    titel("Gesamteindruck je Teilaufgabe (ab Anteil der erreichten BE)")
    erste = z
    for grenze, text in ((0, "ohne anrechenbare Leistung"), (0.01, "in Ansätzen erwartungsgemäß gelöst"),
                         (0.5, "zum Teil erwartungsgemäß gelöst"), (0.75, "weitgehend erwartungsgemäß gelöst"),
                         (1, "vollständig erwartungsgemäß gelöst")):
        b.setze(z, 1, grenze, S(grund=EINGABE, rahmen=True, h="right", format="0%", offen=True))
        b.setze(z, 2, text, feld)
        z += 1
    mp.name("Stufen_Teilaufgabe", b, f"$A${erste}:$B${z - 1}")
    b.setze(erste, 3, "Grenzen aufsteigend lassen; 1 % steht für „mehr als 0 BE“.", notiz)
    titel("Aufgabe insgesamt („Die 1. Aufgabe … ist insgesamt … gelöst“) je Notenstufe")
    erste = z
    for s in range(1, 7):
        eintrag(f"Notenstufe {s} ({WORT[s]})", WORT[s])
    mp.name("TB_Aufgabe", b, f"$B${erste}:$B${z - 1}")
    titel("Anforderungsbereiche")
    eintrag("AFB I", "Anforderungsbereich I (Wiedergeben von Sachverhalten und Anwenden geübter Verfahren im "
            "bekannten Zusammenhang)", "TB_AFB_I", "in eigenen Worten nach den EPA – anpassbar")
    eintrag("AFB II", "Anforderungsbereich II (selbstständiges Bearbeiten und Übertragen bekannter Sachverhalte und "
            "Verfahren auf vergleichbare neue Situationen)", "TB_AFB_II")
    eintrag("AFB III", "Anforderungsbereich III (eigenständiges Lösen komplexer Problemstellungen, Begründen, "
            "Beurteilen und Bewerten)", "TB_AFB_III")
    titel("Einschätzung je Anforderungsbereich je Notenstufe")
    erste = z
    for s, text in enumerate((
            "Die Leistungen entsprechen den Anforderungen in besonderem Maße.",
            "Die Leistungen entsprechen den Anforderungen voll.",
            "Die Leistungen entsprechen im Allgemeinen den Anforderungen.",
            "Die Leistungen weisen zwar Mängel auf, entsprechen im Ganzen aber noch den Anforderungen.",
            "Die Leistungen entsprechen nicht den Anforderungen; die notwendigen Grundkenntnisse sind jedoch erkennbar.",
            "Die Leistungen entsprechen nicht den Anforderungen; selbst die Grundkenntnisse sind lückenhaft."), 1):
        eintrag(f"Notenstufe {s} ({WORT[s]})", text)
    mp.name("TB_AFB", b, f"$B${erste}:$B${z - 1}")
    titel("Gesamturteil je Notenstufe (Notendefinitionen 🔎 mit der geltenden Fassung abgleichen)")
    erste = z
    for s, text in enumerate((
            "Die Leistung entspricht den Anforderungen in besonderem Maße.",
            "Die Leistung entspricht den Anforderungen voll.",
            "Die Leistung entspricht im Allgemeinen den Anforderungen.",
            "Die Leistung weist zwar Mängel auf, entspricht im Ganzen aber noch den Anforderungen.",
            "Die Leistung entspricht den Anforderungen nicht, lässt jedoch erkennen, dass die notwendigen "
            "Grundkenntnisse vorhanden sind und die Mängel in absehbarer Zeit behoben werden können.",
            "Die Leistung entspricht den Anforderungen nicht; selbst die Grundkenntnisse sind so lückenhaft, dass "
            "die Mängel in absehbarer Zeit nicht behoben werden können."), 1):
        eintrag(f"Notenstufe {s} ({WORT[s]})", text)
    mp.name("TB_Gesamt", b, f"$B${erste}:$B${z - 1}")
    titel("Gutachten und Unterschriften")
    eintrag("Einleitung Gesamturteil", "Gesamturteil:", "TB_Gesamt_Einleitung")
    eintrag("kein Abzug für Sprache und Form", "Ein Abzug wegen Verstößen gegen die sprachliche Richtigkeit oder die "
            "äußere Form entfällt.", "TB_Kein_Abzug")
    eintrag("Abzug für Sprache und Form (davor die Zahl)", "Wegen schwerwiegender oder gehäufter Verstöße gegen die "
            "sprachliche Richtigkeit oder die äußere Form (EB-AVO-GOBAK Nr. 9.11) werden abgezogen:", "TB_Abzug",
            "🔎 Fundstelle mit der geltenden Fassung abgleichen")
    eintrag("Endbewertung (danach Notenpunkte und Notenwort)", "Die schriftliche Leistung wird bewertet mit",
            "TB_Endbewertung")
    eintrag("Korreferat, Zustimmung", "Ich schließe mich der Bewertung an.", "TB_Korreferat_ja")
    eintrag("Korreferat, Abweichung (danach Notenpunkte)", "Abweichende Bewertung:", "TB_Korreferat_nein")
    eintrag("Fachprüfungsleitung, Zustimmung", "Ich bin mit der Bewertung einverstanden.", "TB_FPL_ja")
    eintrag("Fachprüfungsleitung, Festsetzung (danach Notenpunkte)", "Festgesetzt:", "TB_FPL_fest")
    eintrag("Fachprüfungsleitung, Festsetzung offen", "Festsetzung durch die Fachprüfungsleitung: ____ Notenpunkte",
            "TB_FPL_offen", "🔎 Verfahren bei abweichender Bewertung nach AVO-GOBAK")
    titel("Ergänzungen zur Auswahl (Spalte H der Blätter P01 …; freier Text bleibt möglich)")
    erste = z
    for text in ("Folgefehler berücksichtigt.", "Gleichwertige Lösung anerkannt.",
                 "Ansatz richtig, Rechenfehler im Ergebnis.", "Einheit fehlt oder ist falsch.",
                 "Lösungsweg nicht nachvollziehbar.", "Darstellung nicht normgerecht.",
                 "Fachbegriffe nicht durchgängig richtig verwendet.", "Lösung unvollständig.",
                 "Teilaufgabe nicht bearbeitet.", None, None, None):
        b.setze(z, 1, "Ergänzung", label)
        b.setze(z, 2, text, feld)
        z += 1
    mp.name("TB_Ergaenzungen", b, f"$B${erste}:$B${z - 1}")
    b.druckbereich = (z, 3)


def blatt_start(mp: Mappe, v: Vorschlag, n: int, datei: str) -> None:
    S = mp.stil
    b = mp.blatt("Start", TAB_EINGABE)
    b.breite = {1: 46, 2: 52, 3: 30}
    b.verbinde(1, 1, 1, 3, f"Bewertungsmappe – {v.kopf}", S(fett=True, groesse=13, v=None))
    b.verbinde(2, 1, 2, 3, "Korrektur, Bewertungsbogen und Gutachten aus einer Quelle: Bewertungsmerkmal im "
               "Erwartungshorizont → Kurztext am Rand der Klausur → derselbe Text in Bemerkung und Gutachten.",
               S(kursiv=True, umbruch=True))
    b.hoehe[2] = 27
    feld = S(grund=EINGABE, rahmen=True, offen=True, umbruch=True)
    label, notiz = S(umbruch=True), S(kursiv=True, farbe=GRAU_TEXT, umbruch=True)
    z = 4

    def titel(text: str) -> None:
        nonlocal z
        z += 1
        b.verbinde(z, 1, z, 3, text, S(fett=True, grund=KOPF))
        z += 1

    def eingabe(text: str, name: str, wert=None, hinweis: str = "", stil: int | None = None) -> int:
        nonlocal z
        b.setze(z, 1, text, label)
        b.setze(z, 2, wert, feld if stil is None else stil)
        if hinweis:
            b.setze(z, 3, hinweis, notiz)
        setze_hoehe(b, z, len(text), 46)
        setze_hoehe(b, z, len(hinweis), 30)
        mp.name(name, b, f"$B${z}")
        z += 1
        return z - 1

    titel("Angaben zur Prüfung (gelbe Felder ausfüllen)")
    eingabe("Schule", "Ang_Schule")
    eingabe("Ort (für „Ort, Datum“)", "Ang_Ort")
    eingabe("Prüfungsgruppe / Kurs", "Ang_Gruppe")
    eingabe("Referent/in (Erstkorrektur), Name", "Ang_Referent")
    eingabe("Kürzel Referent/in", "Ang_Ref_Kuerzel")
    datum = S(grund=EINGABE, rahmen=True, offen=True, format="datum", h="left")
    zd = eingabe("Datum der Erstkorrektur", "Ang_Ref_Datum", stil=datum, hinweis="Datum, z. B. 12.05.2027")
    b.pruefung(f"B{zd}", "date", "1", "73051", meldung="Bitte ein Datum eintragen.")
    eingabe("Korreferent/in (Zweitkorrektur), Name", "Ang_Korreferent")
    eingabe("Kürzel Korreferent/in", "Ang_Kor_Kuerzel")
    zd = eingabe("Datum der Zweitkorrektur", "Ang_Kor_Datum", stil=datum)
    b.pruefung(f"B{zd}", "date", "1", "73051", meldung="Bitte ein Datum eintragen.")
    eingabe("Fachprüfungsleitung, Name", "Ang_FPL")

    titel("Einstellungen")
    zo = eingabe("Erfüllte Merkmale in den Bemerkungen nennen", "Opt_Erfuellt", "nein",
                 "„nein“ (Standard): nur teilweise und nicht erfüllte Merkmale – kurzes Gutachten zum Abschreiben")
    b.pruefung(f"B{zo}", "list", '"ja,nein"', meldung="ja oder nein")
    zo = eingabe("Grenzfall markieren, wenn bis zum nächsten Notenpunkt höchstens … BE fehlen", "Opt_Grenzfall", 1,
                 "Übersicht, Spalte „Grenzfall“: Bewertung der Merkmale noch einmal ansehen")
    b.pruefung(f"B{zo}", "decimal", "0", "20", meldung="Zahl von 0 bis 20")
    zo = eingabe("Abzug-Vorschlag 1 Notenpunkt ab … Fehlern je Seite (R, Z, Gr)", "Opt_Abzug1", 5,
                 "Richtwert der Fachgruppe – anpassen oder leeren; entscheiden muss die Korrektur")
    b.pruefung(f"B{zo}", "decimal", "0", "100", meldung="Zahl eintragen oder leeren")
    zo = eingabe("Abzug-Vorschlag 2 Notenpunkte ab … Fehlern je Seite", "Opt_Abzug2", 7)
    b.pruefung(f"B{zo}", "decimal", "0", "100", meldung="Zahl eintragen oder leeren")
    zo = eingabe("Abweichung vom Ø der Kursergebnisse markieren ab … Notenpunkten", "Opt_Abweichung", 4,
                 "nur Plausibilitätshinweis nach der Korrektur, keine Rechtsfolge 🔎")
    b.pruefung(f"B{zo}", "decimal", "0", "15", meldung="Zahl von 0 bis 15")

    titel("Vorschlag (aus dem Bewertungsbogen erzeugt – nicht ändern)")
    fest = S(rahmen=True, umbruch=True)
    zeilen = [("Prüfung", v.kopf), ("Thema", v.thema or "–"),
              ("Aufgaben", " · ".join(f"{a.nummer}. {a.titel} ({AC.fmt(a.summe)} BE)" for a in v.aufgaben)),
              ("Teilaufgaben / Bewertungsmerkmale", f"{len(v.teile)} / {len(v.merkmale)}"),
              ("BE gesamt", f"{AC.fmt(v.gesamt)} BE – AFB I {AC.fmt(v.afb('I'))}, II {AC.fmt(v.afb('II'))}, "
                            f"III {AC.fmt(v.afb('III'))}"),
              ("Plätze für Prüflinge", f"{n} (Blätter P01 … P{n:02d})"),
              ("Quelle", ", ".join(v.quellen) or datei),
              ("Erzeugt", f"{dt.date.today():%d.%m.%Y} mit bewertungsmappe.py {VERSION} (Skill abiturvorschlag-erstellen)")]
    for text, wert in zeilen:
        b.setze(z, 1, text, label)
        b.verbinde(z, 2, z, 3, wert, fest)
        setze_hoehe(b, z, len(wert), 82)
        z += 1
    if v.hinweise:
        for h in v.hinweise:
            b.setze(z, 1, "⚠ Hinweis", S(fett=True, farbe=ROT))
            b.verbinde(z, 2, z, 3, h, S(farbe=ROT, umbruch=True))
            setze_hoehe(b, z, len(h), 82)
            z += 1

    titel("So arbeiten Sie mit der Mappe")
    schritte = [
        "1. Angaben oben eintragen. Die Kurztexte im Blatt „Korrekturschlüssel“ vor Korrekturbeginn mit der "
        "Fachgruppe abstimmen – sie stehen später wörtlich in Bemerkung und Gutachten und werden von Hand in die "
        "Klausur geschrieben: höchstens vier Wörter, keine Adressen, Zahlenwerte oder Formeln (Merkmal benennen, "
        "nicht die Lösung).",
        "2. Blatt „Prüflinge“: Prüflingsnummern eintragen; Namen nur, wenn die Schule sie im Gutachten verlangt.",
        "3. Korrigieren: In der Klausur am Rand je Merkmal Nummer und Zeichen notieren (z. B. „4 ✗ "
        "Broadcastadresse“), bei (✓) und ✗ mit dem Kurztext. Dann im Blatt „Erfassung“ die BE je Merkmal "
        "eintragen – eine Spalte je Prüfling, Schritte von 0,5 BE; leer = noch nicht bewertet, 0 = nicht erfüllt.",
        "4. Blatt P01 … prüfen: Bewertungsbogen, Bemerkungen je Teilaufgabe und Gutachten entstehen aus den "
        "Eingaben. Ergänzungen (z. B. Folgefehler) in Spalte H auswählen oder schreiben; den Abzug für Sprache und "
        "Form im Blatt „Prüflinge“ festlegen. Lange Ergänzungen: Zeilenhöhe anpassen.",
        "5. Blatt „Übersicht“: Notenpunkte, Grenzfälle, Notenspiegel und Lösungsquoten nach AFB. Die Lösungsquote "
        "je Merkmal steht rechts in „Erfassung“ – Rückmeldung für die Fachgruppe und künftige Vorschläge.",
        "6. Drucken: je Prüfling das Blatt P01 … (Bewertungsbogen, Gutachten); unterschreiben von Hand. Die "
        "Notenpunkte setzen Referat, Korreferat und Fachprüfungsleitung – die Mappe rechnet und formuliert nur vor."]
    for t in schritte:
        b.verbinde(z, 1, z, 3, t, S(umbruch=True))
        setze_hoehe(b, z, len(t), 120)
        z += 1
    titel("Korrekturzeichen")
    for t in ("✓ erfüllt (volle BE) · (✓) teilweise erfüllt (erreichte BE dazuschreiben) · ✗ nicht erfüllt.",
              "Randvermerk = Merkmalnummer + Zeichen, bei (✓) und ✗ zusätzlich der Kurztext aus dem "
              "Korrekturschlüssel. Genau dieser Text erscheint in der Bemerkung zur Teilaufgabe.",
              "Folgefehler und gleichwertige Lösungen: volle BE am Merkmal, Hinweis als Ergänzung (Spalte H) – "
              "Regeln je Teilaufgabe im Korrekturschlüssel."):
        b.verbinde(z, 1, z, 3, t, S(umbruch=True))
        setze_hoehe(b, z, len(t), 120)
        z += 1
    titel("Farben")
    for grund, t in ((EINGABE, "Eingabe"), (AFB_FARBE["I"], "AFB I"), (AFB_FARBE["II"], "AFB II"),
                     (AFB_FARBE["III"], "AFB III"), ("FFC7CE", "Fehler oder prüfen (mehr BE als erreichbar, "
                                                    "Grenzfall, Abweichung)"),
                     ("FFEB9C", "noch offen (Merkmal in einer begonnenen Spalte ohne BE)")):
        b.setze(z, 1, "", S(grund=grund, rahmen=True))
        b.setze(z, 2, t, label)
        setze_hoehe(b, z, len(t), 52)
        z += 1
    titel("Datenschutz und Verantwortung")
    for t in ("Die leere Mappe enthält keine personenbezogenen Daten. Ausgefüllt enthält sie Prüfungsergebnisse: nur "
              "auf dienstlichen bzw. freigegebenen Geräten speichern, nicht in KI-Werkzeuge hochladen, nicht "
              "unverschlüsselt versenden.",
              "Textbausteine und Kurztexte sind Vorschläge. Bewertung und Gutachten verantworten Referent/in, "
              "Korreferent/in und Fachprüfungsleitung (keine ausschließlich automatisierte Entscheidung).",
              "🔎 Notendefinitionen, Abzug für Sprache und Form (EB-AVO-GOBAK) und das Verfahren bei abweichender "
              "Bewertung vor dem ersten Einsatz mit der geltenden Fassung abgleichen."):
        b.verbinde(z, 1, z, 3, t, S(umbruch=True))
        setze_hoehe(b, z, len(t), 120)
        z += 1
    b.druckbereich = (z, 3)
    b.fuss = "&L&8Bewertungsmappe&R&8Seite &P von &N"


def blatt_korrekturschluessel(mp: Mappe, v: Vorschlag, A: Ablage) -> None:
    S = mp.stil
    b = mp.blatt("Korrekturschlüssel", TAB_EINGABE)
    b.breite = {1: 8, 2: 4, 3: 50, 4: 8, 5: 5, 6: 5, 7: 40}
    b.verbinde(1, 1, 1, 7, f"Korrekturschlüssel – {v.kopf}", S(fett=True, groesse=12, v=None))
    b.verbinde(2, 1, 2, 7, "Randvermerk in der Klausur: Merkmalnummer + Zeichen (✓, (✓) mit BE, ✗), bei (✓) und ✗ "
               "zusätzlich der Kurztext. Der Kurztext steht wörtlich in Bemerkung und Gutachten. Kurztexte (gelb, "
               "höchstens vier Wörter, ohne Werte) vor Korrekturbeginn abstimmen; die Merkmale kommen aus dem "
               "Bewertungsraster.",
               S(kursiv=True, umbruch=True))
    b.hoehe[2] = 40
    kopf = ["Teilaufgabe", "Nr.", "Bewertungsmerkmal (Bewertungsraster)", "Art", "AFB", "BE",
            "Kurztext für Randvermerk und Gutachten"]
    for s, t in enumerate(kopf, 1):
        b.setze(4, s, t, S(fett=True, grund=KOPF, rahmen=True, umbruch=True, h="center" if s in (2, 5, 6) else None))
    b.hoehe[4] = 27
    b.titelzeilen = (4, 4)
    z, idx = 5, 0
    text = S(rahmen=True, umbruch=True)
    mitte = S(rahmen=True, h="center")
    kurz = S(rahmen=True, umbruch=True, grund=EINGABE, offen=True)
    for a in v.aufgaben:
        b.verbinde(z, 1, z, 7, f"{a.nummer}. Aufgabe – {a.titel} ({AC.fmt(a.summe)} BE)",
                   S(fett=True, grund=AUFGABE, rahmen=True))
        z += 1
        for t in a.teile:
            kopfzeile = f"{t.nummer} {t.titel} ({AC.fmt(t.be)} BE)".replace("  ", " ")
            if t.ewh:
                kopfzeile += " – Erwartungshorizont: " + " · ".join(t.ewh)
            b.verbinde(z, 1, z, 7, kopfzeile, S(fett=True, grund=SUMME, rahmen=True, umbruch=True))
            setze_hoehe(b, z, len(kopfzeile), 120)
            z += 1
            for m in t.merkmale:
                b.setze(z, 1, m.teil, mitte)
                b.setze(z, 2, m.nr, mitte)
                b.setze(z, 3, m.text, text)
                b.setze(z, 4, m.art, mitte)
                b.setze(z, 5, m.afb, S(rahmen=True, h="center", grund=AFB_FARBE.get(m.afb)))
                b.setze(z, 6, m.be, mitte)
                b.setze(z, 7, m.kurz, kurz)
                setze_hoehe(b, z, max(len(m.text), len(m.kurz) * 50 // 40), 50)
                A.kurz[idx] = bl(b.name) + adr(z, 7, True)
                idx += 1
                z += 1
            for art, regel in t.regeln:
                inhalt = f"{art}: {regel}"
                b.verbinde(z, 1, z, 7, inhalt, S(kursiv=True, rahmen=True, umbruch=True, farbe=GRAU_TEXT))
                setze_hoehe(b, z, len(inhalt), 120)
                z += 1
    b.druckbereich = (z - 1, 7)
    b.fuss = "&L&8Korrekturschlüssel&R&8Seite &P von &N"


def blatt_prueflinge(mp: Mappe, v: Vorschlag, A: Ablage) -> None:
    S = mp.stil
    b = mp.blatt("Prüflinge", TAB_EINGABE)
    b.breite = {1: 5, 2: 16, 3: 24, 4: 8, 5: 11, 6: 9, 7: 10, 8: 10, 9: 11, 10: 11, 11: 11}
    b.verbinde(1, 1, 1, 11, f"Prüflinge – {v.kopf}", S(fett=True, groesse=12, v=None))
    b.verbinde(2, 1, 2, 11, "Prüflingsnummer genügt; Namen nur, wenn die Schule sie im Gutachten verlangt (nur lokal). "
               "Sprachfehler: Anzahl der abzugsrelevanten Fehler (R, Z, Gr) der ganzen Arbeit. Den Abzug "
               "entscheidet die Korrektur; der Vorschlag rechnet mit den Richtwerten im Blatt „Start“. "
               "Korreferat und Festsetzung nur bei abweichender Bewertung.", S(kursiv=True, umbruch=True))
    b.hoehe[2] = 40
    kopf = ["Nr.", "Prüflingsnummer", "Name, Vorname (optional)", "Seiten", "Sprachfehler (R, Z, Gr)",
            "Fehler je Seite", "Abzug-Vorschlag (NP)", "Abzug (NP)", "NP Korreferat (bei Abweichung)",
            "NP festgesetzt (Fachprüfungsleitung)", "Ø Kursergebnisse 12.1–13.2 (optional)"]
    for s, t in enumerate(kopf, 1):
        b.setze(4, s, t, S(fett=True, grund=KOPF, rahmen=True, umbruch=True, h="center"))
    b.hoehe[4] = 40
    b.fix = (5, 3)
    ein = S(grund=EINGABE, rahmen=True, offen=True, h="center")
    ein_l = S(grund=EINGABE, rahmen=True, offen=True)
    rech = S(rahmen=True, h="center")
    for i in range(1, A.n + 1):
        z = A.p_zeile(i)
        b.setze(z, 1, i, rech)
        b.setze(z, 2, None, ein_l)
        b.setze(z, 3, None, ein_l)
        for s in (4, 5, 8, 9, 10, 11):
            b.setze(z, s, None, ein)
        b.setze(z, 6, Formel(f'IF(OR(D{z}="",E{z}="",N(D{z})=0),"",ROUND(E{z}/D{z},1))'), rech)
        b.setze(z, 7, Formel(f'IF(F{z}="","",IF(AND(Opt_Abzug2<>"",F{z}>=Opt_Abzug2),2,'
                             f'IF(AND(Opt_Abzug1<>"",F{z}>=Opt_Abzug1),1,0)))'), rech)
    z1, z2 = A.p_zeile(1), A.p_zeile(A.n)
    b.pruefung(f"D{z1}:E{z2}", "whole", "0", "500", meldung="ganze Zahl ≥ 0")
    b.pruefung(f"H{z1}:H{z2}", "list", '"0,1,2"', meldung="Abzug 0, 1 oder 2 Notenpunkte")
    b.pruefung(f"I{z1}:J{z2}", "whole", "0", "15", meldung="Notenpunkte 0 bis 15")
    b.pruefung(f"K{z1}:K{z2}", "decimal", "0", "15", meldung="Notenpunkte 0 bis 15")
    b.bedingung(f"G{z1}:G{z2}", f'AND(ISNUMBER(G{z1}),G{z1}>0,N(H{z1})<>G{z1})', mp.stil.dxf(ROT, "FFC7CE"))
    b.druckbereich = (z2, 11)
    b.quer = True


def blatt_erfassung(mp: Mappe, v: Vorschlag, A: Ablage, werte: dict[int, list] | None) -> None:
    S = mp.stil
    b = mp.blatt("Erfassung", TAB_EINGABE)
    n, c0 = A.n, A.e_spalte0
    cl = c0 + n - 1
    cm, cq, cn = cl + 1, cl + 2, cl + 3
    b.breite = {1: 3, 2: 10, 3: 4, 4: 46, 5: 5, 6: 5, cm: 6, cq: 8, cn: 4}
    for c in range(c0, cl + 1):
        b.breite[c] = 6.5
    b.versteckt = {1}
    b.verbinde(1, 2, 1, cn, f"Erfassung der BE je Bewertungsmerkmal – {v.kopf}", S(fett=True, groesse=12, v=None))
    b.verbinde(2, 2, 2, cn, "Eine Spalte je Prüfling. BE in Schritten von 0,5; leer = noch nicht bewertet, "
               "0 = nicht erfüllt. Rot: mehr als erreichbar. Gelb-orange: in einer begonnenen Spalte noch offen. "
               "Rechts: Ø BE und Lösungsquote je Merkmal (grün ab 90 %, rot bis 20 %).", S(kursiv=True, umbruch=True))
    b.hoehe[2] = 27
    kopf = {2: "Teilaufgabe", 3: "Nr.", 4: "Bewertungsmerkmal", 5: "AFB", 6: "BE", cm: "Ø BE",
            cq: "Lösungs-quote", cn: "n"}
    hk = S(fett=True, grund=KOPF, rahmen=True, umbruch=True, h="center", v="center")
    for s, t in kopf.items():
        b.setze(3, s, t, hk)
    for i in range(1, n + 1):
        b.setze(3, c0 + i - 1, i, hk)
        pz = A.p_zeile(i)
        quelle = bl("Prüflinge") + f"B{pz}"
        b.setze(4, c0 + i - 1, Formel(f'IF({quelle}="","",{quelle})'),
                S(rahmen=True, h="center", v="bottom", drehung=90, groesse=8))
    b.verbinde(4, 2, 4, 6, "Prüflingsnummer →", S(rahmen=True, h="right", v="bottom", kursiv=True))
    for s in (cm, cq, cn):
        b.setze(4, s, None, S(rahmen=True))
    b.hoehe[3] = 27
    b.hoehe[4] = 62
    b.fix = (5, c0)
    b.titelzeilen = (3, 4)
    pz_s = [sp(c) for c in range(c0, cl + 1)]
    text = S(rahmen=True, umbruch=True)
    mitte = S(rahmen=True, h="center")
    eingabe = S(grund=EINGABE, rahmen=True, offen=True, h="center")
    summe = S(fett=True, grund=SUMME, rahmen=True, h="center")
    summe_l = S(fett=True, grund=SUMME, rahmen=True)
    quote = S(rahmen=True, h="center", format="0%")
    quote_s = S(fett=True, grund=SUMME, rahmen=True, h="center", format="0%")
    schnitt = S(rahmen=True, h="center", format="0.0")
    schnitt_s = S(fett=True, grund=SUMME, rahmen=True, h="center", format="0.0")
    rot, offen = S.dxf(ROT, "FFC7CE", True), S.dxf(None, "FFEB9C")
    gruen, schwer = S.dxf("006100", "C6EFCE"), S.dxf("9C0006", "FFC7CE")

    def statistik(z: int, be: float, stil_m: int, stil_q: int) -> None:
        bereich = f"{pz_s[0]}{z}:{pz_s[-1]}{z}"
        b.setze(z, cm, Formel(f'IF(COUNT({bereich})=0,"",AVERAGE({bereich}))'), stil_m)
        b.setze(z, cq, Formel(f'IF({sp(cm)}{z}="","",{sp(cm)}{z}/{be})'), stil_q)
        b.setze(z, cn, Formel(f"COUNT({bereich})"), summe if stil_m == schnitt_s else mitte)

    z, idx = 5, 0
    eingabebloecke: list[tuple[int, int]] = []
    for a in v.aufgaben:
        b.verbinde(z, 2, z, 6, f"{a.nummer}. Aufgabe – {a.titel} ({AC.fmt(a.summe)} BE)",
                   S(fett=True, grund=AUFGABE, rahmen=True))
        for c in range(c0, cn + 1):
            b.setze(z, c, None, S(grund=AUFGABE, rahmen=True))
        z += 1
        start_aufgabe = z
        for t in a.teile:
            erste = z
            for m in t.merkmale:
                b.setze(z, 1, a.nummer)
                b.setze(z, 2, m.teil, mitte)
                b.setze(z, 3, m.nr, mitte)
                b.setze(z, 4, m.text, text)
                b.setze(z, 5, m.afb, S(rahmen=True, h="center", grund=AFB_FARBE.get(m.afb)))
                b.setze(z, 6, m.be, mitte)
                for i in range(1, n + 1):
                    wert = (werte or {}).get(i, [None] * len(v.merkmale))[idx]
                    b.setze(z, c0 + i - 1, wert, eingabe)
                statistik(z, m.be, schnitt, quote)
                setze_hoehe(b, z, len(m.text), 46)
                A.e_zeile[idx] = z
                idx += 1
                z += 1
            letzte = z - 1
            eingabebloecke.append((erste, letzte))
            b.verbinde(z, 2, z, 5, f"Σ {t.nummer}", summe_l)
            b.setze(z, 6, t.be, summe)
            for s in pz_s:
                b.setze(z, c0 + pz_s.index(s), Formel(f'IF(COUNT({s}{erste}:{s}{letzte})=0,"",SUM({s}{erste}:{s}{letzte}))'),
                        summe)
            statistik(z, t.be, schnitt_s, quote_s)
            z += 1
        b.verbinde(z, 2, z, 5, f"Summe {a.nummer}. Aufgabe", summe_l)
        b.setze(z, 6, a.summe, summe)
        for k, s in enumerate(pz_s):
            b.setze(z, c0 + k, Formel(f'IF(COUNT({s}{start_aufgabe}:{s}{z - 1})=0,"",'
                                      f'SUMIF($A$5:$A$999,{a.nummer},{s}$5:{s}$999))'), summe)
        statistik(z, a.summe, schnitt_s, quote_s)
        A.e_aufgabe[a.nummer] = z
        z += 2
    # Ergebnis je Prüfling
    letzte_daten = z - 2

    def ergebniszeile(text: str, wert, formel, stil=summe, fmt_q=True) -> int:
        nonlocal z
        b.verbinde(z, 2, z, 5, text, summe_l)
        b.setze(z, 6, wert, summe)
        for k, s in enumerate(pz_s):
            b.setze(z, c0 + k, Formel(formel(s)), stil)
        z += 1
        return z - 1

    summen = ",".join(f"{{s}}{A.e_aufgabe[a.nummer]}" for a in v.aufgaben)
    A.e_gesamt = ergebniszeile("Gesamt (BE)", v.gesamt,
                               lambda s: f'IF(COUNT({summen.format(s=s)})=0,"",SUM({summen.format(s=s)}))')
    statistik(A.e_gesamt, v.gesamt, schnitt_s, quote_s)
    for k in AFB:
        A.e_afb[k] = ergebniszeile(f"AFB {k} (BE)", v.afb(k), lambda s, k=k: f'IF({s}{A.e_gesamt}="","",'
                                   f'SUMIF($E$5:$E${letzte_daten},"{k}",{s}$5:{s}${letzte_daten}))')
        statistik(A.e_afb[k], v.afb(k), schnitt_s, quote_s)
    A.e_np = ergebniszeile("Notenpunkte vor Abzug", 15,
                           lambda s: f'IF({s}{A.e_gesamt}="","",SUMPRODUCT(--(NS_BE<={s}{A.e_gesamt})))')
    bloecke = ",".join(f"{{s}}{e}:{{s}}{l}" for e, l in eingabebloecke)
    A.e_anzahl = ergebniszeile("bewertete Merkmale", len(v.merkmale), lambda s: f"COUNT({bloecke.format(s=s)})")
    A.e_status = ergebniszeile("Status", None, lambda s: f'IF({s}{A.e_anzahl}=0,"",IF({s}{A.e_anzahl}='
                               f'{len(v.merkmale)},"fertig","offen "&({len(v.merkmale)}-{s}{A.e_anzahl})))',
                               S(fett=True, grund=SUMME, rahmen=True, h="center", groesse=8))
    # Prüfungen und Hervorhebungen je Eingabeblock
    for e, l in eingabebloecke:
        bereich = f"{pz_s[0]}{e}:{pz_s[-1]}{l}"
        tl = f"{pz_s[0]}{e}"
        b.pruefung(bereich, "custom", f"AND(ISNUMBER({tl}),{tl}>=0,{tl}<=$F{e},MOD({tl}*2,1)=0)",
                   meldung="BE zwischen 0 und dem erreichbaren Wert, in Schritten von 0,5.")
        b.bedingung(bereich, f"AND(ISNUMBER({tl}),{tl}>$F{e})", rot)
        b.bedingung(bereich, f'AND({tl}="",COUNT({pz_s[0]}$5:{pz_s[0]}${letzte_daten})>0)', offen)
    qb = f"{sp(cq)}5:{sp(cq)}{A.e_afb['III']}"
    b.bedingung(qb, f"AND(ISNUMBER({sp(cq)}5),{sp(cq)}5>=0.9)", gruen)
    b.bedingung(qb, f"AND(ISNUMBER({sp(cq)}5),{sp(cq)}5<=0.2)", schwer)
    st = f"{pz_s[0]}{A.e_status}:{pz_s[-1]}{A.e_status}"
    b.bedingung(st, f'LEFT({pz_s[0]}{A.e_status},5)="offen"', offen)
    b.druckbereich = (z - 1, cn)
    b.quer = True
    b.fuss = "&L&8Erfassung&R&8Seite &P von &N"


def blatt_pruefling(mp: Mappe, v: Vorschlag, A: Ablage, i: int) -> None:
    S = mp.stil
    b = mp.blatt(f"P{i:02d}", TAB_PRUEFLING)
    b.breite = {1: 11, 2: 5, 3: 52, 4: 6, 5: 10.5, 6: 8.5, 7: 10.5, 8: 44, 9: 2, 10: 8, 11: 30, 12: 30, 13: 30,
                14: 30}
    b.versteckt = {10, 11, 12, 13, 14}
    E = bl("Erfassung")
    es = sp(A.e_spalte(i))
    P, pz = bl("Prüflinge"), A.p_zeile(i)
    nr = f"{P}B{pz}"
    name = f"{P}C{pz}"
    m_ges = len(v.merkmale)
    anzahl = f"{E}{es}{A.e_anzahl}"
    breit = 104            # Zeichenbreite A:G
    titel = S(fett=True, groesse=12, umbruch=True, v=None)
    hk = S(fett=True, grund=KOPF, rahmen=True, umbruch=True, h="center", v="center")
    hk_l = S(fett=True, grund=KOPF, rahmen=True, umbruch=True, v="center")
    text = S(rahmen=True, umbruch=True)
    mitte = S(rahmen=True, h="center")
    summe = S(fett=True, grund=SUMME, rahmen=True, h="center")
    summe_l = S(fett=True, grund=SUMME, rahmen=True)
    anteil = S(rahmen=True, h="center", format="0%")
    anteil_s = S(fett=True, grund=SUMME, rahmen=True, h="center", format="0%")
    satz = S(umbruch=True)
    satz_f = S(umbruch=True, fett=True)
    warn = S(fett=True, farbe=ROT, umbruch=True)
    ergaenzung = S(grund=EINGABE, rahmen=True, umbruch=True, offen=True)
    nichts = S(rahmen=True)

    b.verbinde(1, 1, 1, 7, f"Bewertungsbogen – {v.kopf}", titel)
    b.verbinde(2, 1, 2, 7, Formel(f'IF(Ang_Schule="","",Ang_Schule&" · ")&"Prüfungsgruppe: "&'
                                  f'IF(Ang_Gruppe="","–",Ang_Gruppe)'), S(v=None))
    b.verbinde(3, 1, 3, 2, "Prüflingsnummer", hk)
    b.setze(3, 3, "Name (nur falls verlangt)", hk_l)
    b.verbinde(3, 4, 3, 5, "Erstkorrektur (Kürzel, Datum)", hk)
    b.verbinde(3, 6, 3, 7, "Zweitkorrektur (Kürzel, Datum)", hk)
    b.hoehe[3] = 27
    b.verbinde(4, 1, 4, 2, Formel(f'IF({nr}="","Nr. {i}",{nr})'), S(rahmen=True, h="center", fett=True))
    b.setze(4, 3, Formel(f'IF({name}="","",{name})'), text)
    b.setze(4, 4, Formel('IF(Ang_Ref_Kuerzel="","",Ang_Ref_Kuerzel)'), mitte)
    b.setze(4, 5, Formel('IF(Ang_Ref_Datum="","",Ang_Ref_Datum)'), S(rahmen=True, h="center", format="datum"))
    b.setze(4, 6, Formel('IF(Ang_Kor_Kuerzel="","",Ang_Kor_Kuerzel)'), mitte)
    b.setze(4, 7, Formel('IF(Ang_Kor_Datum="","",Ang_Kor_Datum)'), S(rahmen=True, h="center", format="datum"))
    b.verbinde(5, 1, 5, 7, Formel(f'IF({anzahl}=0,"Noch keine BE erfasst.",IF({anzahl}<{m_ges},'
                                  f'"Bewertung unvollständig: "&{anzahl}&" von {m_ges} Merkmalen bewertet – vor dem '
                                  f'Druck ergänzen.",""))'), warn)
    # ── Teil 1: Bewertungsbogen je Merkmal ──
    z, idx = 7, 0
    p_zeile: dict[int, int] = {}
    summenzeile: dict[int, int] = {}
    bereich_bb = [z, 0]
    vermerk_rot, vermerk_orange = S.dxf(ROT, None, True), S.dxf(ORANGE, None, True)
    for k, a in enumerate(v.aufgaben):
        if k:
            b.umbrueche.append(z)
        b.verbinde(z, 1, z, 7, f"{a.nummer}. Aufgabe – {a.titel} ({AC.fmt(a.summe)} BE)",
                   S(fett=True, grund=AUFGABE, rahmen=True))
        z += 1
        for s, t in enumerate(["Teilaufgabe", "Nr.", "Bewertungsmerkmal", "AFB", "erreichbar", "erreicht",
                               "Vermerk"], 1):
            b.setze(z, s, t, hk_l if s == 3 else hk)
        z += 1
        erste = z
        for t in a.teile:
            for m in t.merkmale:
                er = A.e_zeile[idx]
                b.setze(z, 1, m.teil, mitte)
                b.setze(z, 2, m.nr, mitte)
                b.setze(z, 3, m.text, text)
                b.setze(z, 4, m.afb, S(rahmen=True, h="center", grund=AFB_FARBE.get(m.afb)))
                b.setze(z, 5, m.be, mitte)
                b.setze(z, 6, Formel(f'IF({E}{es}{er}="","",{E}{es}{er})'), S(rahmen=True, h="center", fett=True))
                setze_hoehe(b, z, len(m.text), 52)
                b.setze(z, 7, Formel(f'IF(J{z}=0,"",CHOOSE(J{z},Zeichen_voll,Zeichen_teilweise,Zeichen_nicht))'),
                        S(rahmen=True, h="center", fett=True))
                ku = A.kurz[idx]
                b.setze(z, 10, Formel(f'IF(F{z}="",0,IF(F{z}>=E{z},1,IF(F{z}>0,2,3)))'))
                b.setze(z, 11, Formel(f'IF(J{z}=1,{ku}&"; ","")'))
                b.setze(z, 12, Formel(f'IF(J{z}=2,{ku}&" ("&F{z}&" von "&E{z}&" BE); ","")'))
                b.setze(z, 13, Formel(f'IF(J{z}=3,{ku}&"; ","")'))
                b.setze(z, 14, Formel(f'IF(J{z}=0,{ku}&"; ","")'))
                p_zeile[idx] = z
                idx += 1
                z += 1
        b.bedingung(f"G{erste}:G{z - 1}", f"G{erste}=Zeichen_nicht", vermerk_rot)
        b.bedingung(f"G{erste}:G{z - 1}", f"G{erste}=Zeichen_teilweise", vermerk_orange)
        b.verbinde(z, 1, z, 4, f"Summe {a.nummer}. Aufgabe", summe_l)
        b.setze(z, 5, a.summe, summe)
        b.setze(z, 6, Formel(f'IF(COUNT(F{erste}:F{z - 1})=0,"",SUM(F{erste}:F{z - 1}))'), summe)
        b.setze(z, 7, None, summe)
        summenzeile[a.nummer] = z
        z += 2
    bereich_bb[1] = z - 2
    b.verbinde(z, 1, z, 7, "Ergebnis", S(fett=True, v=None))
    z += 1
    b.verbinde(z, 1, z, 4, "", hk)
    b.setze(z, 5, "erreichbar", hk)
    b.setze(z, 6, "erreicht", hk)
    z += 1
    alle_summen = ",".join(f"F{summenzeile[a.nummer]}" for a in v.aufgaben)
    z_ges = z
    b.verbinde(z, 1, z, 4, "Gesamt", summe_l)
    b.setze(z, 5, v.gesamt, summe)
    b.setze(z, 6, Formel(f'IF(COUNT({alle_summen})=0,"",SUM({alle_summen}))'), summe)
    z += 1
    z_np = z
    b.verbinde(z, 1, z, 4, "Notenpunkte nach dem Bewertungsmaßstab (vor einem Abzug)", summe_l)
    b.setze(z, 5, None, summe)
    b.setze(z, 6, Formel(f'IF(F{z_ges}="","",SUMPRODUCT(--(NS_BE<=F{z_ges})))'), S(fett=True, grund=SUMME,
                                                                                   rahmen=True, h="center",
                                                                                   format="00"))
    z += 2

    # ── Teil 2: Gutachten ──
    b.umbrueche.append(z)
    b.verbinde(z, 1, z, 7, f"Gutachten – {v.kopf}", titel)
    z += 1
    b.verbinde(z, 1, z, 7, Formel(f'"Prüflingsnummer: "&IF({nr}="","Nr. {i}",{nr})&IF({name}="",""," – "&{name})'),
               S(fett=True, v=None))
    z += 2
    erste_bb, letzte_bb = bereich_bb
    ergaenzungen: list[str] = []
    for a in v.aufgaben:
        zs = summenzeile[a.nummer]
        mm = a.merkmale
        n_a = len(mm)
        e1, e2 = p_zeile[v.merkmale.index(mm[0])], p_zeile[v.merkmale.index(mm[-1])]
        b.setze(z, 10, Formel(f'IF(F{zs}="","",INDEX(NS_Stufe,16-SUMPRODUCT(--(NS_Prozent<='
                              f'ROUND(F{zs}/{a.summe}*100,6)))))'))
        einleitung = f"Die {a.nummer}. Aufgabe („{a.titel}“) ist insgesamt "
        b.verbinde(z, 1, z, 7, Formel(
            f'IF(F{zs}="",{q(f"{a.nummer}. Aufgabe: ")}&Text_unbewertet&".",{q(einleitung)}&INDEX(TB_Aufgabe,J{z})'
            f'&" gelöst: "&F{zs}&" von {AC.fmt(a.summe)} BE ("&ROUND(F{zs}/{a.summe}*100,1)&" %)."'
            f'&IF(COUNT(F{e1}:F{e2})<{n_a}," "&Text_unvollstaendig,""))'), satz_f)
        setze_hoehe(b, z, len(einleitung) + 60, breit)
        z += 1
        b.setze(z, 1, "Teilaufgabe", hk)
        b.verbinde(z, 2, z, 4, "Bemerkungen – Vorzüge und Mängel", hk_l)
        b.setze(z, 5, "erreichbar", hk)
        b.setze(z, 6, "erreicht", hk)
        b.setze(z, 7, "Anteil", hk)
        b.setze(z, 8, "Ergänzung (frei; erscheint in der Bemerkung)", S(fett=True, kursiv=True, umbruch=True,
                                                                         farbe=GRAU_TEXT))
        b.hoehe[z] = 27
        z += 1
        for t in a.teile:
            zeilen = [p_zeile[v.merkmale.index(m)] for m in t.merkmale]
            r1, r2 = zeilen[0], zeilen[-1]
            for s in (11, 12, 13, 14):
                b.setze(z, s, Formel("&".join(f"{sp(s)}{r}" for r in zeilen)))
            b.setze(z, 1, t.nummer, mitte)
            b.setze(z, 5, t.be, mitte)
            b.setze(z, 6, Formel(f'IF(COUNT(F{r1}:F{r2})=0,"",SUM(F{r1}:F{r2}))'), S(rahmen=True, h="center",
                                                                                     fett=True))
            b.setze(z, 7, Formel(f'IF(F{z}="","",F{z}/E{z})'), anteil)
            b.setze(z, 8, None, ergaenzung)
            ergaenzungen.append(f"H{z}")
            kopf = (t.titel or f"Teilaufgabe {t.nummer}") + ": "
            liste = lambda s, label, bed="": (f'&IF({bed}{sp(s)}{z}="",""," "&{label}&" "&LEFT({sp(s)}{z},'
                                              f'LEN({sp(s)}{z})-2)&".")')
            formel = (f'IF(F{z}="",{q(kopf)}&Text_unbewertet&".",{q(kopf)}&VLOOKUP(G{z},Stufen_Teilaufgabe,2,TRUE)&"."'
                      f'&IF(OR(Opt_Erfuellt<>"ja",K{z}=""),""," "&Text_erfuellt&" "&LEFT(K{z},LEN(K{z})-2)&".")'
                      + liste(12, "Text_teilweise") + liste(13, "Text_nicht") + liste(14, "Text_offen") + ")"
                      f'&IF(H{z}="",""," "&H{z})')
            b.verbinde(z, 2, z, 4, Formel(formel), text)
            laenge = len(kopf) + 40 + sum(len(m.kurz) + 4 + (12 if m.be >= 1 else 0) for m in t.merkmale)
            setze_hoehe(b, z, laenge, 63, reserve=1)
            b.hoehe[z] = max(b.hoehe.get(z, 0), 27)
            z += 1
        z += 1
    b.pruefung(" ".join(ergaenzungen), "list", "TB_Ergaenzungen", fehler=False,
               hinweis="Auswahl oder freier Text; erscheint am Ende der Bemerkung.")
    # Schlussseite: Anforderungsbereiche, Gesamturteil, Endbewertung, Unterschriften
    b.umbrueche.append(z)
    b.verbinde(z, 1, z, 7, Formel(f'"Gutachten (Fortsetzung) – Prüflingsnummer: "&IF({nr}="","Nr. {i}",{nr})'),
               S(fett=True, v=None))
    z += 2
    b.setze(z, 1, "AFB", hk)
    b.verbinde(z, 2, z, 4, "Einschätzung nach Anforderungsbereichen", hk_l)
    for s, t in ((5, "erreichbar"), (6, "erreicht"), (7, "Anteil")):
        b.setze(z, s, t, hk)
    z += 1
    for k in AFB:
        gesamt_k = v.afb(k)
        b.setze(z, 1, k, S(rahmen=True, h="center", fett=True, grund=AFB_FARBE[k]))
        b.setze(z, 5, gesamt_k, mitte)
        b.setze(z, 6, Formel(f'IF(F{z_ges}="","",SUMIF(D${erste_bb}:D${letzte_bb},"{k}",F${erste_bb}:F${letzte_bb}))'),
                S(rahmen=True, h="center", fett=True))
        b.setze(z, 7, Formel(f'IF(OR(F{z}="",E{z}=0),"",F{z}/E{z})'), anteil)
        b.setze(z, 10, Formel(f'IF(G{z}="","",INDEX(NS_Stufe,16-SUMPRODUCT(--(NS_Prozent<=ROUND(G{z}*100,6)))))'))
        b.verbinde(z, 2, z, 4, Formel(f'IF(G{z}="","",IF({anzahl}<{m_ges},TB_AFB_{k}&": "&Text_unvollstaendig,'
                                      f'TB_AFB_{k}&": "&INDEX(TB_AFB,J{z})))'), text)
        b.hoehe[z] = 3 * 12.75 + 2
        z += 1
    b.verbinde(z, 1, z, 4, "Gesamt", summe_l)
    b.setze(z, 5, v.gesamt, summe)
    b.setze(z, 6, Formel(f"F{z_ges}"), summe)
    b.setze(z, 7, Formel(f'IF(F{z}="","",F{z}/E{z})'), anteil_s)
    z += 1
    b.verbinde(z, 1, z, 4, "Notenpunkte nach dem Bewertungsmaßstab", summe_l)
    b.setze(z, 5, None, summe)
    b.setze(z, 6, Formel(f"F{z_np}"), S(fett=True, grund=SUMME, rahmen=True, h="center", format="00"))
    b.setze(z, 7, None, summe)
    z += 2
    # Gesamturteil, Abzug, Endbewertung – erst, wenn alle Merkmale bewertet sind
    abzug = f"N({P}H{pz})"
    fertig = f"{anzahl}={m_ges}"
    z_end = z + 3
    b.setze(z_end, 10, Formel(f'IF(OR(F{z_np}="",NOT({fertig})),"",MAX(0,F{z_np}-{abzug}))'))
    b.setze(z, 10, Formel(f'IF(J{z_end}="","",INDEX(NS_Stufe,16-J{z_end}))'))
    b.verbinde(z, 1, z, 7, Formel(f'IF(J{z}="","",TB_Gesamt_Einleitung&" "&INDEX(TB_Gesamt,J{z})'
                                  f'&IF(H{z}="",""," "&H{z}))'), satz)
    b.setze(z, 8, None, ergaenzung)
    b.hoehe[z] = 3 * 12.75 + 2
    b.pruefung(f"H{z}", "list", "TB_Ergaenzungen", fehler=False,
               hinweis="Ergänzung zum Gesamturteil (frei), z. B. besondere Stärken der Arbeit.")
    z += 1
    b.verbinde(z, 1, z, 7, Formel(f'IF(J{z_end}="","",IF({abzug}=0,TB_Kein_Abzug,TB_Abzug&" "&{abzug}&'
                                  f'IF({abzug}=1," Notenpunkt."," Notenpunkte.")))'), satz)
    b.hoehe[z] = 2 * 12.75 + 2
    z += 1
    b.verbinde(z, 1, z, 7, Formel(f'IF(AND({anzahl}>0,{anzahl}<{m_ges}),"Bewertung unvollständig ("&{anzahl}&'
                                  f'" von {m_ges} Merkmalen) – Gesamturteil und Endbewertung erscheinen, sobald '
                                  f'alle Merkmale bewertet sind.","")'), warn)
    b.hoehe[z] = 2 * 12.75 + 2
    z += 1
    b.verbinde(z, 1, z, 7, Formel(f'IF(J{z}="","",TB_Endbewertung&" "&{np_text(f"J{z}")}&IF(J{z}=1," Notenpunkt",'
                                  f'" Notenpunkten")&" ("&INDEX(NS_Wort,16-J{z})&").")'), S(fett=True, groesse=11,
                                                                                         umbruch=True))
    b.hoehe[z] = 2 * 14 + 2
    z += 2
    # Unterschriften
    kor, fest = f"{P}I{pz}", f"{P}J{pz}"
    zustimmung = f'OR({kor}="",{kor}=J{z_end})'
    trenner = f'IF(J{z_end}="","",IF({{n}}="",""," – "))'
    bloecke = [
        (Formel('"Referent/in: "&IF(Ang_Referent="","",Ang_Referent)'), "Ang_Ref_Datum"),
        (Formel(f'"Korreferent/in: "&IF(Ang_Korreferent="","",Ang_Korreferent)&{trenner.format(n="Ang_Korreferent")}'
                f'&IF(J{z_end}="","",IF({zustimmung},TB_Korreferat_ja,TB_Korreferat_nein&" "&{np_text(kor)}&'
                f'" Notenpunkte."))'), "Ang_Kor_Datum"),
        (Formel(f'"Fachprüfungsleitung: "&IF(Ang_FPL="","",Ang_FPL)&{trenner.format(n="Ang_FPL")}'
                f'&IF(J{z_end}="","",IF({zustimmung},TB_FPL_ja,IF({fest}="",TB_FPL_offen,TB_FPL_fest&" "&'
                f'{np_text(fest)}&" Notenpunkte.")))'), None)]
    for formel, datum in bloecke:
        b.verbinde(z, 1, z, 7, formel, S(fett=True, umbruch=True))
        b.hoehe[z] = 2 * 12.75 + 2
        z += 1
        b.verbinde(z, 1, z, 2, "Ort, Datum", S(v="bottom"))
        b.setze(z, 3, Formel('IF(Ang_Ort="","",Ang_Ort)'), S(v="bottom"))
        b.verbinde(z, 4, z, 5, Formel(f'IF({datum}="","",{datum})') if datum else None,
                   S(v="bottom", h="center", format="datum"))
        b.verbinde(z, 6, z, 7, None, S(v="bottom", rahmen="unten"))
        b.hoehe[z] = 30
        z += 1
        b.verbinde(z, 6, z, 7, "Unterschrift", S(kursiv=True, groesse=8, farbe=GRAU_TEXT, h="center"))
        z += 2
    b.druckbereich = (z - 1, 7)
    b.fuss = f"&L&8Bewertungsbogen und Gutachten · {v.kopf[:80].replace('&', '&&')}&R&8&A · Seite &P von &N"


def blatt_uebersicht(mp: Mappe, v: Vorschlag, A: Ablage) -> None:
    S = mp.stil
    b = mp.blatt("Übersicht", TAB_REFERENZ)
    E, P = bl("Erfassung"), bl("Prüflinge")
    spalten = ["Nr.", "Prüflingsnummer", "Name"] + [f"Aufg. {a.nummer}" for a in v.aufgaben] + [
        "Σ BE", "Anteil", "NP (BE)", "Abzug", "NP Referat", "NP Korreferat", "NP fest-gesetzt", "Ergebnis NP",
        "Note", "BE bis nächster NP", "Grenzfall", "Status", "AFB I", "AFB II", "AFB III", "Ø Kurse", "Abwei-chung"]
    c = {name: i for i, name in enumerate(spalten, 1)}
    breiten = {"Nr.": 4, "Prüflingsnummer": 17, "Name": 18, "Status": 9, "Grenzfall": 9.5}
    b.breite = {i: breiten.get(name, 8.5) for name, i in c.items()}
    letzte = len(spalten)
    b.verbinde(1, 1, 1, letzte, f"Übersicht – {v.kopf}", S(fett=True, groesse=12, v=None))
    b.verbinde(2, 1, 2, letzte, "Ergebnis NP = NP Referat (nach Abzug); weicht das Korreferat ab, gilt die Festsetzung "
               "der Fachprüfungsleitung („offen“, solange sie fehlt). Grenzfall: bis zum nächsten Notenpunkt fehlen "
               "höchstens so viele BE wie im Blatt „Start“ eingestellt. Abweichung: Ergebnis minus Ø Kursergebnisse.",
               S(kursiv=True, umbruch=True))
    b.hoehe[2] = 27
    hk = S(fett=True, grund=KOPF, rahmen=True, umbruch=True, h="center", v="center")
    for name, s in c.items():
        b.setze(4, s, name, hk)
    b.hoehe[4] = 40
    b.fix = (6, 4)
    b.titelzeilen = (4, 5)
    erreichbar = S(kursiv=True, grund=SUMME, rahmen=True, h="center")
    b.verbinde(5, 1, 5, 3, "erreichbar", S(kursiv=True, grund=SUMME, rahmen=True))
    for s in range(4, letzte + 1):
        b.setze(5, s, None, erreichbar)
    for a in v.aufgaben:
        b.setze(5, c[f"Aufg. {a.nummer}"], a.summe, erreichbar)
    b.setze(5, c["Σ BE"], v.gesamt, erreichbar)
    for k in AFB:
        b.setze(5, c[f"AFB {k}"], v.afb(k), erreichbar)
    mitte = S(rahmen=True, h="center")
    fett = S(rahmen=True, h="center", fett=True)
    anteil = S(rahmen=True, h="center", format="0%")
    np_fmt = S(rahmen=True, h="center", format="00")
    np_fett = S(rahmen=True, h="center", format="00", fett=True)
    L = lambda name, z: f"{sp(c[name])}{z}"
    z1 = 6
    for i in range(1, A.n + 1):
        z, pz, es = z1 + i - 1, A.p_zeile(i), sp(A.e_spalte(i))
        wenn = lambda quelle: Formel(f'IF({quelle}="","",{quelle})')
        b.setze(z, c["Nr."], i, mitte)
        b.setze(z, c["Prüflingsnummer"], wenn(f"{P}B{pz}"), S(rahmen=True))
        b.setze(z, c["Name"], wenn(f"{P}C{pz}"), S(rahmen=True))
        for a in v.aufgaben:
            b.setze(z, c[f"Aufg. {a.nummer}"], wenn(f"{E}{es}{A.e_aufgabe[a.nummer]}"), mitte)
        b.setze(z, c["Σ BE"], wenn(f"{E}{es}{A.e_gesamt}"), fett)
        b.setze(z, c["Anteil"], Formel(f'IF({L("Σ BE", z)}="","",{L("Σ BE", z)}/{v.gesamt})'), anteil)
        b.setze(z, c["NP (BE)"], wenn(f"{E}{es}{A.e_np}"), np_fmt)
        np_be = L("NP (BE)", z)
        b.setze(z, c["Abzug"], Formel(f'IF({np_be}="","",N({P}H{pz}))'), mitte)
        b.setze(z, c["NP Referat"], Formel(f'IF({np_be}="","",MAX(0,{np_be}-{L("Abzug", z)}))'), np_fmt)
        b.setze(z, c["NP Korreferat"], wenn(f"{P}I{pz}"), np_fmt)
        b.setze(z, c["NP fest-gesetzt"], wenn(f"{P}J{pz}"), np_fmt)
        ref, kor, fest = L("NP Referat", z), L("NP Korreferat", z), L("NP fest-gesetzt", z)
        b.setze(z, c["Ergebnis NP"], Formel(f'IF({ref}="","",IF({L("Status", z)}<>"fertig","offen",IF({fest}<>"",'
                                             f'{fest},IF(OR({kor}="",{kor}={ref}),{ref},"offen"))))'), np_fett)
        erg = L("Ergebnis NP", z)
        b.setze(z, c["Note"], Formel(f'IF(ISNUMBER({erg}),INDEX(NS_Note,16-{erg}),"")'), mitte)
        b.setze(z, c["BE bis nächster NP"], Formel(f'IF({np_be}="","",IF({np_be}>=15,"",INDEX(NS_BE,15-{np_be})-'
                                                    f'{L("Σ BE", z)}))'), mitte)
        bis = L("BE bis nächster NP", z)
        b.setze(z, c["Grenzfall"], Formel(f'IF({bis}="","",IF({bis}<=Opt_Grenzfall,"prüfen",""))'), mitte)
        b.setze(z, c["Status"], wenn(f"{E}{es}{A.e_status}"), S(rahmen=True, h="center", groesse=8))
        for k in AFB:
            b.setze(z, c[f"AFB {k}"], Formel(f'IF({E}{es}{A.e_afb[k]}="","",{E}{es}{A.e_afb[k]}/{v.afb(k) or 1})'),
                    anteil)
        b.setze(z, c["Ø Kurse"], wenn(f"{P}K{pz}"), S(rahmen=True, h="center", format="0.0"))
        b.setze(z, c["Abwei-chung"], Formel(f'IF(OR({L("Ø Kurse", z)}="",NOT(ISNUMBER({erg}))),"",'
                                             f'ROUND({erg}-{L("Ø Kurse", z)},1))'), mitte)
    z2 = z1 + A.n - 1
    warn, offen = S.dxf("9C0006", "FFC7CE", True), S.dxf(None, "FFEB9C")
    b.bedingung(f"{L('Grenzfall', z1)}:{L('Grenzfall', z2)}", f'{L("Grenzfall", z1)}="prüfen"', warn)
    b.bedingung(f"{L('Ergebnis NP', z1)}:{L('Ergebnis NP', z2)}",
                f'AND(ISNUMBER({L("Ergebnis NP", z1)}),{L("Ergebnis NP", z1)}<5)', S.dxf(ROT, None, True))
    b.bedingung(f"{L('Ergebnis NP', z1)}:{L('Ergebnis NP', z2)}", f'{L("Ergebnis NP", z1)}="offen"', offen)
    b.bedingung(f"{L('Abwei-chung', z1)}:{L('Abwei-chung', z2)}",
                f'AND(ISNUMBER({L("Abwei-chung", z1)}),ABS({L("Abwei-chung", z1)})>=Opt_Abweichung)', warn)
    b.bedingung(f"{L('Status', z1)}:{L('Status', z2)}", f'LEFT({L("Status", z1)},5)="offen"', offen)
    # Auswertung der Gruppe
    z = z2 + 2
    erg = f"{L('Ergebnis NP', z1)}:{L('Ergebnis NP', z2)}"
    b.verbinde(z, 1, z, 6, "Auswertung der Prüfungsgruppe", S(fett=True, grund=KOPF))
    z += 1
    zeilen = [("bewertete Arbeiten (Ergebnis feststehend)", Formel(f"COUNT({erg})"), mitte),
              ("Durchschnitt (Notenpunkte)", Formel(f'IF(COUNT({erg})=0,"",ROUND(AVERAGE({erg}),2))'),
               S(rahmen=True, h="center", format="0.00")),
              ("unter 05 Notenpunkten (Anzahl)", Formel(f'COUNTIF({erg},"<5")'), mitte),
              ("unter 05 Notenpunkten (Anteil)", Formel(f'IF(COUNT({erg})=0,"",COUNTIF({erg},"<5")/COUNT({erg}))'),
               anteil)]
    for a in v.aufgaben:
        sp_a = f"{L(f'Aufg. {a.nummer}', z1)}:{L(f'Aufg. {a.nummer}', z2)}"
        zeilen.append((f"{a.nummer}. Aufgabe: mittlerer Anteil der BE",
                       Formel(f'IF(COUNT({sp_a})=0,"",AVERAGE({sp_a})/{a.summe})'), anteil))
    for k in AFB:
        sp_k = f"{L(f'AFB {k}', z1)}:{L(f'AFB {k}', z2)}"
        zeilen.append((f"AFB {k}: mittlerer Anteil der BE", Formel(f'IF(COUNT({sp_k})=0,"",AVERAGE({sp_k}))'), anteil))
    for text, formel, stil in zeilen:
        b.verbinde(z, 1, z, 5, text, S(rahmen=True))
        b.setze(z, 6, formel, stil)
        z += 1
    z += 1
    b.verbinde(z, 1, z, 3, "Notenspiegel", S(fett=True, grund=KOPF))
    z += 1
    b.verbinde(z, 1, z, 3, "Notenpunkte", hk)
    b.verbinde(z + 1, 1, z + 1, 3, "Anzahl", S(rahmen=True, fett=True))
    for k, n_ in enumerate(range(15, -1, -1)):
        b.setze(z, 4 + k, n_, S(fett=True, grund=KOPF, rahmen=True, h="center", format="00"))
        b.setze(z + 1, 4 + k, Formel(f"COUNTIF({erg},{n_})"), mitte)
    z += 3
    b.verbinde(z, 1, z, 3, "Notenstufe", hk)
    b.verbinde(z + 1, 1, z + 1, 3, "Anzahl", S(rahmen=True, fett=True))
    grenzen = {1: (13, 16), 2: (10, 13), 3: (7, 10), 4: (4, 7), 5: (1, 4), 6: (0, 1)}
    for s in range(1, 7):
        von, bis = grenzen[s]
        sp_s = 4 + (s - 1) * 2
        b.verbinde(z, sp_s, z, sp_s + 1, f"{s} ({WORT[s]})", hk)
        b.verbinde(z + 1, sp_s, z + 1, sp_s + 1, Formel(f'COUNTIF({erg},">={von}")-COUNTIF({erg},">={bis}")'), mitte)
    z += 3
    for rolle in ("Referent/in", "Korreferent/in", "Fachprüfungsleitung"):
        b.verbinde(z, 1, z, 3, rolle, S(fett=True, v="bottom"))
        b.verbinde(z, 4, z, 7, "Ort, Datum", S(v="bottom", kursiv=True, farbe=GRAU_TEXT))
        b.verbinde(z, 8, z, 14, "Unterschrift", S(v="bottom", kursiv=True, farbe=GRAU_TEXT))
        b.hoehe[z] = 30
        z += 1
    b.druckbereich = (z - 1, letzte)
    b.quer = True
    b.fuss = "&L&8Übersicht&R&8Seite &P von &N"


def baue_mappe(v: Vorschlag, n: int, datei: str = "", werte: dict[int, list] | None = None) -> Mappe:
    """werte: {Prüfling: [BE je Merkmal]} nur für Tests und Probeläufe mit erfundenen Daten."""
    mp = Mappe()
    A = Ablage(n)
    blatt_notenschluessel(mp, v)
    blatt_textbausteine(mp)
    blatt_korrekturschluessel(mp, v, A)
    blatt_prueflinge(mp, v, A)
    blatt_erfassung(mp, v, A, werte)
    for i in range(1, n + 1):
        blatt_pruefling(mp, v, A, i)
    blatt_uebersicht(mp, v, A)
    blatt_start(mp, v, n, datei)
    return mp


REIHENFOLGE = ["Start", "Korrekturschlüssel", "Prüflinge", "Erfassung", "Übersicht"]


def schreibe(v: Vorschlag, ziel: Path, n: int, werte: dict[int, list] | None = None) -> None:
    mp = baue_mappe(v, n, ziel.name, werte)
    reihe = REIHENFOLGE + [f"P{i:02d}" for i in range(1, n + 1)] + ["Notenschlüssel", "Textbausteine"]
    mp.speichern(ziel, f"Bewertungsmappe – {v.kopf}", reihe)


# ───────────────────────────── Aufruf ─────────────────────────────

def lade(dateien: list[Path]) -> tuple[Vorschlag, Path]:
    """Vorschlag aus Bewertungsbogen (ggf. mit SM/LM daneben) oder aus SM und LM."""
    if len(dateien) == 1:
        bogen = dateien[0]
        v = lies_bewertungsbogen(bogen.read_text(encoding="utf-8"))
        v.quellen.append(bogen.name)
        stamm = re.sub(r"_bewertungsbogen$", "", bogen.stem)
        sm, lm = bogen.with_name(f"{stamm}_schuelermaterial.md"), bogen.with_name(f"{stamm}_lehrermaterial.md")
        rs = bogen.with_name(f"{stamm}_bewertungsraster.md")
        if sm.is_file() and lm.is_file():
            anreichern(v, sm.read_text(encoding="utf-8"), lm.read_text(encoding="utf-8"),
                       rs.read_text(encoding="utf-8") if rs.is_file() else None)
            v.quellen += [sm.name, lm.name] + ([rs.name] if rs.is_file() else [])
        else:
            v.hinweise.append("Schüler- und Lehrermaterial nicht neben dem Bewertungsbogen gefunden – ohne Titel der "
                              "Teilaufgaben, Regeln und Abgleich erzeugt")
        ziel = bogen.with_name(f"{stamm}_bewertungsmappe.xlsx")
    elif len(dateien) == 2:
        sm_text, lm_text = (d.read_text(encoding="utf-8") for d in dateien)
        rs = AC.raster_pfad(dateien[1])
        rs_text = rs.read_text(encoding="utf-8") if rs.is_file() else None
        opdaten = AC.lade_operatoren(AC.operatorenpfad(None))
        _b, info, modell, _ = AC.pruefe(sm_text, lm_text, opdaten, raster_text=rs_text)
        v = lies_bewertungsbogen(AC.bewertungsbogen(info, modell))
        anreichern(v, sm_text, lm_text, rs_text)
        v.quellen += [d.name for d in dateien] + ([rs.name] if rs_text is not None else [])
        stamm = re.sub(r"_lehrermaterial$", "", dateien[1].stem)
        ziel = dateien[1].with_name(f"{stamm}_bewertungsmappe.xlsx")
    else:
        raise SystemExit("Aufruf: bewertungsmappe.py BEWERTUNGSBOGEN.md  oder  SCHUELERMATERIAL.md LEHRERMATERIAL.md")
    pruefe_eingabe(v)
    return v, ziel


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Excel-Mappe für Korrektur, Bewertungsbogen und Gutachten (lokal).")
    p.add_argument("dateien", type=Path, nargs="+", help="Bewertungsbogen.md oder Schülermaterial.md Lehrermaterial.md")
    p.add_argument("-o", "--ausgabe", type=Path, default=None, help="Zieldatei .xlsx (Standard: …_bewertungsmappe.xlsx)")
    p.add_argument("--prueflinge", type=int, default=20, help="Plätze für Prüflinge (1–60, Standard 20)")
    a = p.parse_args(argv)
    if not 1 <= a.prueflinge <= 60:
        p.error("--prueflinge muss zwischen 1 und 60 liegen")
    v, ziel = lade(a.dateien)
    ziel = a.ausgabe or ziel
    if ziel.suffix.lower() != ".xlsx":
        p.error("Zieldatei muss auf .xlsx enden")
    if ziel.exists():
        print(f"{ziel} existiert bereits – nicht überschrieben (anderen Namen wählen; eine ausgefüllte Mappe "
              "enthält Korrekturdaten).", file=sys.stderr)
        return 2
    schreibe(v, ziel, a.prueflinge)
    print(f"Bewertungsmappe geschrieben: {ziel}")
    print(f"  {v.kopf} · {len(v.aufgaben)} Aufgaben · {len(v.teile)} Teilaufgaben · {len(v.merkmale)} Merkmale · "
          f"{AC.fmt(v.gesamt)} BE (AFB I {AC.fmt(v.afb('I'))} · II {AC.fmt(v.afb('II'))} · III {AC.fmt(v.afb('III'))})")
    print(f"  Blätter: {', '.join(REIHENFOLGE)}, P01–P{a.prueflinge:02d}, Notenschlüssel, Textbausteine")
    for h in v.hinweise:
        print(f"  ⚠ {h}")
    print("  Nächster Schritt: Kurztexte im Korrekturschlüssel mit der Fachgruppe abstimmen. Ausgefüllt enthält die "
          "Mappe Prüfungsergebnisse – nicht in KI-Werkzeuge hochladen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
