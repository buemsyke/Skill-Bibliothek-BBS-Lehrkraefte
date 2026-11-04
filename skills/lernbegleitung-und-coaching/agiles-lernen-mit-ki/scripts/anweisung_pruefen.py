#!/usr/bin/env python3
r"""anweisung_pruefen – Systemanweisungen für KI-Chatbots prüfen (lokal, deterministisch).

Prüft Systemanweisungen (Systemprompts) für Lernbegleiter, Assistenten und Dialogpartner:
eine einzelne Anweisung (.md/.txt) oder alle Anweisungsblöcke (```text) eines Pakets
(95_ki-chatbot_…, 93_ais-paket_…). Je Anweisung:

  Bausteine    Rolle, Ablauf, Kontextgrenze bzw. Quellenpflicht, „nichts erfinden“, Sprache,
               Abschluss; für Lernende zusätzlich Hilfe statt Lösung und Hinweis für Notlagen
  Grenzen      Datenschutz (keine Namen, Noten …), Schutz gegen Anweisungen in Dateien und
               Eingaben, keine Bewertung von Lernergebnissen (Leitplanke)
  Darstellung  Formeln mit MathJax-Begrenzern (\( … \), $$ … $$ – nicht $ … $), Code in
               Codeblöcken; reine JSON-Ausgabe: Schema, Platz für Rückfragen, Backslashes doppelt
  Form         offene Platzhalter [ … ], Platzhalter der Plattform {{…}} (Datenfluss), Länge
               (--max-zeichen), gehäufte absolute Regeln in Großbuchstaben, Kontaktdaten
Im Paket 95_ki-chatbot_… zusätzlich: Kopf, Hinweis „Du chattest mit einer KI“, Hintergrundwissen
nur öffentlich oder eigen, Probelauf (Pflichttests bestanden?), Freigabezeile
„Freigabe Chatbot: erteilt – KÜRZEL, Datum“, Pflichtabschnitte.

Aufruf:
    python3 anweisung_pruefen.py DATEI [--zielgruppe auto|lernende|lehrkraefte]
                                 [--max-zeichen N] [--json]

Exit 0 = keine ❌ (⚠ möglich), 1 = mindestens ein ❌, 2 = Eingabefehler.
Nur Python-Standardbibliothek. Erkennt Bausteine an Schlüsselwörtern (deutsch und englisch) –
ob sich der Chatbot daran hält, zeigt erst der Probelauf.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

I, M = re.IGNORECASE, re.MULTILINE

# ─────────────────────────────── Muster ───────────────────────────────

ANWEISUNG_START = re.compile(r"^(#+\s*\w|Du bist\b|Sie sind\b|You are\b|Ich gebe dir\b|I'll pass you|"
                             r"I will pass you|This system prompt)", I)
ANWEISUNG_VORSPANN = re.compile(r"Anweisung|System-?prompt|Systemanweisung|Verhalten der KI", I)

LEHRKRAFT = re.compile(r"(für (eine|die) Lehrkraft,? die|unterstützt (eine |die )?Lehrkr|Assistent für Lehrkr|"
                       r"\bLehrkräfte(n)? (beim|bei der|in der)|\bteachers?\b|course creator|input fields|"
                       r"form elements|Formularfeld)", I)
LERNENDE = re.compile(r"(lernende|Lernbegleit|Schüler|\bAzubi|Auszubildend|Lerngruppe|Lernsprint|Probeprüfung|"
                      r"Selbstkontrolle|\bTutor|learners?\b|students?\b)", I)
ROLLENSPIEL = re.compile(r"(Bleib\w* in (der|deiner) Rolle|Dialogpartner|imitierst|\bSTOPP\b|Figur, fiktiv)", I)

ROLLE = re.compile(r"(^#+\s*(ROLLE|ROLE)\b|(^|[.!?:]\s+)(Du bist|Sie sind|You are|Deine Rolle)\b|"
                   r"\bAls (Lernbegleit|Tutor|Assistent))", I | M)
ABLAUF = re.compile(r"(^#+\s*(ABLAUF|START|VORGEHEN|AUFGABE|AUFTRAG|SO \w+ DU|SPIELREGELN|STEPS|TASK)\b|^\s*1\.\s|"
                    r"Begrüße|\bArbeite in\b|\bdeine Aufgabe\b|\byour task\b|give suggestions|\bsuggest\b)", I | M)
KONTEXT = re.compile(r"(nur (\w+ )?(aus |mit |auf |im |in )?(de[mnr] |die |das |den )?(Hintergrundwissen|Quellen|"
                     r"Unterlagen|Material\w*|Dateien|Datei|Kontext|Fragenpool)|(im|in den|in der) (Hintergrundwissen|"
                     r"Quellen|Unterlagen) steht|nicht in den (Quellen|Unterlagen)|steht nicht (in|im)|"
                     r"\bdu \w*\s?nicht (weißt|kennst)|weißt du nicht|not aware|unless the user provides|"
                     r"only (use|based on|from) the)", I)
ERFINDEN = re.compile(r"(erfinde nichts|nichts erfinden|erfinde keine|keine erfundenen|rate nicht|nicht raten|"
                      r"do not (invent|make up|guess)|don't (invent|make up|guess)|unsicher bist|bist du unsicher|"
                      r"wenn du unsicher)", I)
SPRACHE = re.compile(r"(Sprache der|auf Deutsch|in deutscher Sprache|einfache[nr]? (Sprache|Sätze)|einfachen Sätzen|"
                     r"du-Form|Sie-Form|\bduze|\bsieze|Anrede|mit\s+[„\"]?(Sie|du)[“\"]?\s+an\b|\blanguage\b)", I)
ENDE = re.compile(r"(^#+\s*(ENDE|ABSCHLUSS|FEEDBACK)\b|zum Schluss|am Ende|verabschiedet|beenden|„fertig“|"
                  r"\"fertig\"|Gesprächsende|at the end)", I | M)
HILFE = re.compile(r"(keine (fertige|vollständige|komplette|ganze)n? Lösung|nie die (fertige|vollständige|komplette|ganze) "
                   r"Lösung|(löst|lösen) keine Aufgabe|keine Aufgaben (für|vor)|verr(a|ä)t\w* keine Lösung|"
                   r"Verrate keine|nicht vor(sagen|rechnen)|gestufte Hilfe|"
                   r"do not (give|reveal) (the )?(full |complete )?(solution|answer))", I)
NOTLAGE = re.compile(r"(Notlage|Notfall|in Not\b|von Not\b|Krise|Gewalt|Mobbing|Schulsozialarbeit|Vertrauenslehr|"
                     r"Beratungslehr|\b112\b|116\s?111|Nummer gegen Kummer|Seelsorge)", I)
DATENSCHUTZ = re.compile(r"(\bNamen\b|personenbezogen|persönliche[nr]? (Daten|Angaben)|Adressen|Gesundheitsdaten|"
                         r"personal (data|information)|privacy|Datenschutz)", I)
BEWERTUNG = re.compile(r"(vergib\w* (eine |die )?(Note|Punkte|Notenpunkte)|\bbenote\w*|bewerte\w* (die |eine |ihre |seine |"
                       r"deren )?(Leistung|Abgabe|Arbeit|Klausur)|Note (geben|vergeben|festlegen)|"
                       r"grade (the|their|student)|assign (a )?(grade|score)|scor(e|ing) (the )?students?)", I)
VERNEINT = re.compile(r"\b(kein\w*|nicht|nie|niemals|ohne|no|not|never)\b", I)
EXTERN = re.compile(r"(Hintergrundwissen|Datei|hochlad|Upload|Formular|form (elements|structure)|help texts|"
                    r"\{\{|Webseite|Lernakte|Eingabe|Nachricht)", I)
INJEKTION = re.compile(r"(keine Anweisungen (an|für) dich|sind (nur )?(Material|Daten|Inhalte?)\w*,? (und )?keine "
                       r"Anweisung|nicht als Anweisung|Anweisungen in (Dateien|Texten|Nachrichten)|andere Rolle|"
                       r"Regeln (zu )?(ändern|ignorieren)|treat .{0,40}as (data|content)|not (as )?instructions|"
                       r"ignore (any )?instructions)", I)
MATHE = re.compile(r"(Formel|Rechenweg|Gleichung|mathemati|formula|equation|\\frac|MathJax|LaTeX)", I)
MATHE_REGEL = re.compile(r"(MathJax|\\\(|\$\$|LaTeX)", I)
EINFACHES_DOLLAR = re.compile(r"(?<![$\\])\$(?![$\s])[^$\n]{1,80}(?<![$\\\s])\$(?!\$)")
CODE = re.compile(r"(\bCode\b|Programm|Python|C\+\+|Arduino|ESP32|G-Code|\bSQL\b|JavaScript|program code)", I)
CODE_REGEL = re.compile(r"(Codeblock|Codeblöck|code block|fenced|```)", I)
NUR_JSON = re.compile(r"\b(nur|ausschließlich|only|always)\b[^.\n]{0,40}\bJSON\b", I)
RUECKFRAGE = re.compile(r"(Rückfrage|nachfrag|follow-?up|ask .{0,30}questions?)", I)
RUECKFRAGE_PLATZ = re.compile(r"(outro|chatoutput|im Feld [„\"]|in the (field|key) [\"']|"
                              r"\"(text|message|question|chat)\w*\"\s*:)", I)
BACKSLASH_REGEL = re.compile(r"(doppelte?n? Backslash|double backslash|\\\\\\\\|escap)", I)
SCHEMA = re.compile(r"(\"\w+\"\s*:|\bSchema\b|\battributes\b|\bAttribute\b)", I)
PLATZHALTER = re.compile(r"\[(?!x\]|X\]| \]|Coach\]|Rolle:|Role:)[^\]\n]{2,60}\](?!\()")
SYSTEM_PLATZHALTER = re.compile(r"\{\{\s*[\w.]+\s*\}\}")
ABSOLUT = re.compile(r"\b(IMMER|NIEMALS|NIE|ALLE|NUR|MUSST?|ALWAYS|NEVER|MUST|ONLY|ALL)\b")
MAIL = re.compile(r"[\w.+-]+@([\w-]+\.)+[a-z]{2,}", I)
BEISPIEL_DOMAINS = ("example.org", "example.com", "example.net", "example.de")
TELEFON = re.compile(r"(?<![\w.])(?:\+49|0)[\s/-]?\d{2,5}[\s/-]?\d{3,}(?:[\s-]?\d+)*")
HILFETELEFON = re.compile(r"0800[\s-]?111[\s-]?0[\s-]?(111|222|550)")

PFLICHT = ("Qualitätscheck", "Annahmen und Prüfaufträge", "Übergabe")
KI_HINWEIS = re.compile(r"(mit einer KI|mit einem KI|KI-Chat|Künstliche[rn]? Intelligenz|KI-gestützt|Chatbot)", I)
NICHT_OEFFENTLICH = re.compile(r"\b(nein|intern|vertraulich|nicht öffentlich|Schülerarbeit\w*|Abgabe\w*)\b", I)
FREIGABE = re.compile(r"Freigabe\s+Chatbot\s*:\s*\**\s*erteilt\s*\**\s*[-–—]\s*(?P<kuerzel>[A-Za-zÄÖÜäöüß]{1,6})\s*,"
                      r"\s*(?P<datum>\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.\d{2,4})", I)
BESTANDEN = re.compile(r"^(✓|✅|(ja|bestanden|ok)\b)", I)
DURCHGEFALLEN = re.compile(r"^(✗|❌|nein|nicht bestanden|durchgefallen)", I)


@dataclass
class Anweisung:
    name: str
    text: str
    zielgruppe: str = "unbekannt"
    rollenspiel: bool = False
    befunde: list = field(default_factory=list)
    bausteine: dict = field(default_factory=dict)


class Eingabefehler(Exception):
    pass


# ─────────────────────────────── Lesen ───────────────────────────────

def kopf(text: str) -> tuple[dict, str]:
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    daten = {}
    for zeile in m.group(1).splitlines():
        if ":" not in zeile or zeile.lstrip().startswith("#"):
            continue
        k, _, v = zeile.partition(":")
        v = v.strip()
        v = v[1:].split('"', 1)[0] if v.startswith('"') else v.split(" #", 1)[0].strip()
        daten[k.strip()] = v
    return daten, m.group(2)


def anweisungen(text: str, name: str) -> list[Anweisung]:
    """Anweisungsblöcke (```text) mit der Überschrift davor als Name – sonst die ganze Datei."""
    zeilen = text.splitlines()
    gefunden: list[Anweisung] = []
    ueberschrift, vorspann, im_block, sprache, block = name, [], False, "", []
    for z in zeilen:
        if not im_block and z.startswith("```"):
            im_block, sprache, block = True, z[3:].strip().lower(), []
            continue
        if im_block:
            if z.startswith("```"):
                im_block = False
                inhalt = "\n".join(block).strip()
                erste = next((x.strip() for x in block if x.strip()), "")
                if sprache.startswith("text") and inhalt and (
                        ANWEISUNG_START.match(erste) or ANWEISUNG_VORSPANN.search("\n".join(vorspann))):
                    gefunden.append(Anweisung(ueberschrift, inhalt))
                vorspann = []
            else:
                block.append(z)
            continue
        if re.match(r"^#{1,4}\s+\S", z):
            ueberschrift, vorspann = z.lstrip("#").strip(), []
        else:
            vorspann.append(z)
    if gefunden:
        return gefunden
    _, rumpf = kopf(text)
    rumpf = re.sub(r"<!--.*?-->", "", rumpf, flags=re.DOTALL).strip()
    return [Anweisung(name, rumpf)] if rumpf else []


def abschnitte(rumpf: str) -> dict[str, str]:
    """## Überschrift → Inhalt (Überschriften in Codeblöcken zählen nicht)."""
    ergebnis: dict[str, str] = {}
    titel, puffer, im_block = None, [], False
    for z in rumpf.splitlines():
        if z.startswith("```"):
            im_block = not im_block
        if not im_block and re.match(r"^##\s+\S", z):
            if titel is not None:
                ergebnis[titel] = "\n".join(puffer)
            titel, puffer = z[2:].strip(), []
        elif titel is not None:
            puffer.append(z)
    if titel is not None:
        ergebnis[titel] = "\n".join(puffer)
    return ergebnis


def finde(abschn: dict[str, str], wort: str) -> tuple[str, str] | None:
    for titel, inhalt in abschn.items():
        if titel.lower().startswith(wort.lower()):
            return titel, inhalt
    return None


def tabelle(inhalt: str) -> tuple[list[str], list[list[str]]]:
    kopfzeile, zeilen = [], []
    for z in inhalt.splitlines():
        s = z.strip()
        if not s.startswith("|") or re.match(r"^\|?\s*:?-{2,}", s):
            continue
        zellen = [c.strip() for c in s.strip("|").split("|")]
        if not kopfzeile:
            kopfzeile = [c.lower() for c in zellen]
        else:
            zeilen.append(zellen)
    return kopfzeile, zeilen


def spalte(kopfzeile: list[str], *woerter: str) -> int | None:
    return next((i for i, s in enumerate(kopfzeile) if any(w in s for w in woerter)), None)


# ─────────────────────────────── Prüfen ───────────────────────────────

def zielgruppe(text: str, vorgabe: str) -> str:
    if vorgabe in ("lernende", "lehrkraefte"):
        return vorgabe
    if LEHRKRAFT.search(text):
        return "lehrkraefte"
    if LERNENDE.search(text):
        return "lernende"
    return "unbekannt"


def bewertung_ohne_verneinung(text: str) -> str | None:
    for m in BEWERTUNG.finditer(text):
        anfang = max(text.rfind("\n", 0, m.start()), text.rfind(".", 0, m.start())) + 1
        satz = text[anfang:m.end() + 40]
        if not VERNEINT.search(satz):
            return m.group(0)
    return None


def pruefe_anweisung(a: Anweisung, vorgabe: str, max_zeichen: int | None) -> None:
    t = a.text
    a.zielgruppe = zielgruppe(t, vorgabe)
    a.rollenspiel = bool(ROLLENSPIEL.search(t))
    lern = a.zielgruppe == "lernende"

    def b(bereich: str, stufe: str, meldung: str) -> None:
        a.befunde.append((bereich, stufe, meldung))

    def baustein(name: str, ok: bool, stufe: str, meldung: str) -> None:
        a.bausteine[name] = ok
        if not ok and stufe:
            b(name, stufe, meldung)

    if a.zielgruppe == "unbekannt":
        b("Zielgruppe", "⚠", "nicht erkennbar (Lernende oder Lehrkräfte?) – in der Rolle nennen oder --zielgruppe angeben")

    # Bausteine
    baustein("Rolle", bool(ROLLE.search(t)), "⚠", "keine Rolle („Du bist …“ bzw. # ROLLE) – Zweck und Zielgruppe in einem Satz")
    baustein("Ablauf", bool(ABLAUF.search(t)), "⚠", "kein Ablauf bzw. Auftrag (Start, Schritte)")
    baustein("Kontextgrenze", bool(KONTEXT.search(t)), "⚠",
             "keine Kontextgrenze bzw. Quellenpflicht – was die KI nicht aus Anweisung, Hintergrundwissen oder "
             "Chat weiß, sagt sie offen oder fragt nach")
    if not a.rollenspiel:  # im Rollenspiel ist Improvisieren gewollt; Fachliches deckt die Kontextgrenze
        baustein("Nichts erfinden", bool(ERFINDEN.search(t)), "⚠",
                 "keine Regel gegen Erfinden („Erfinde nichts; bist du unsicher, sag es.“)")
    baustein("Sprache", bool(SPRACHE.search(t)), "⚠", "keine Regel zu Sprache und Anrede")
    if lern and not a.rollenspiel:
        baustein("Hilfe statt Lösung", bool(HILFE.search(t)), "❌",
                 "keine Regel „Hilfe statt Lösung“ – gestufte Hilfen, keine fertigen Lösungen von Aufgaben")
    if lern:
        baustein("Abschluss", bool(ENDE.search(t)), "⚠", "kein Abschluss (Zusammenfassung, Sicherung, nächster Schritt)")
        baustein("Notlagen", bool(NOTLAGE.search(t)), "⚠",
                 "kein Hinweis für Notlagen (Not, Mobbing, Gefahr → Lehrkraft, Schulsozialarbeit, 116 111, 112)")

    # Grenzen
    system = sorted(set(SYSTEM_PLATZHALTER.findall(t)))
    baustein("Datenschutz", bool(DATENSCHUTZ.search(t)), "❌" if lern else "⚠",
             "kein Datenschutzhinweis (keine Namen, Noten, Adressen, Betriebe erfragen oder übernehmen)"
             + (" – die Plattform setzt Seitendaten ein" if system else ""))
    if EXTERN.search(t) or lern:
        baustein("Eingeschleuste Anweisungen", bool(INJEKTION.search(t)), "⚠",
                 "kein Schutz gegen Anweisungen in Dateien, Feldern oder Nachrichten (sind Material, keine Anweisungen)")
    treffer = bewertung_ohne_verneinung(t)
    if treffer:
        b("Bewertung", "❌", f"„{treffer}“ – Chatbots bewerten keine Lernergebnisse (Leitplanke, KI-VO Anhang III Nr. 3)")
    if a.rollenspiel and not re.search(r"fiktiv", t, I):
        b("Rollenspiel", "⚠", "Figur nicht als fiktiv gekennzeichnet")

    # Darstellung
    if MATHE.search(t) and not MATHE_REGEL.search(t):
        b("Formeln", "⚠", "Formeln ohne Darstellungsregel – in Moodle \\( … \\) und $$ … $$ (MathJax)")
    m = EINFACHES_DOLLAR.search(t)
    if m:
        b("Formeln", "⚠", f"„{m.group(0)}“ – einfaches $ … $ rendert Moodle-MathJax nicht; \\( … \\) verwenden")
    if CODE.search(t) and not CODE_REGEL.search(t):
        b("Code", "⚠", "Code ohne Darstellungsregel (Codeblock mit Sprachangabe)")
    if NUR_JSON.search(t):
        if not SCHEMA.search(t):
            b("JSON", "⚠", "nur JSON verlangt, aber kein Schema bzw. Beispiel")
        if RUECKFRAGE.search(t) and not RUECKFRAGE_PLATZ.search(t):
            b("JSON", "⚠", "nur JSON, aber Rückfragen ohne festen Platz im Schema – Widerspruch")
        if (MATHE.search(t) or "\\" in t) and not BACKSLASH_REGEL.search(t):
            b("JSON", "⚠", "JSON mit Formeln: Backslashes doppelt verlangen (\\\\( … \\\\))")

    # Form
    offen = PLATZHALTER.findall(t)
    if offen:
        b("Platzhalter", "⚠", f"{len(offen)} offene Platzhalter, z. B. „{offen[0]}“ – vor dem Einfügen ersetzen")
    if system:
        b("Datenfluss", "ℹ", f"Platzhalter der Plattform {', '.join(system)} – im Probelauf klären, welche Daten "
                             "eingesetzt und an das Sprachmodell gesendet werden")
    absolut = [w for z in t.splitlines() if not z.lstrip().startswith("#") for w in ABSOLUT.findall(z)]
    if len(absolut) >= 4:
        b("Form", "⚠", f"{len(absolut)} absolute Regeln in Großbuchstaben ({', '.join(sorted(set(absolut)))}) – "
                       "konkurrieren im Zweifel; Vorrang ausdrücklich regeln")
    if max_zeichen and len(t) > max_zeichen:
        b("Länge", "❌", f"{len(t)} Zeichen – Limit des Anweisungsfelds {max_zeichen}; Längeres als Datei ins Hintergrundwissen")
    for mm in MAIL.finditer(t):
        if not mm.group(0).lower().endswith(BEISPIEL_DOMAINS):
            b("Datenschutz", "❌", "E-Mail-Adresse in der Anweisung – entfernen bzw. Funktionsadresse")
            break
    if any(not HILFETELEFON.search(mm.group(0)) for mm in TELEFON.finditer(t)):
        b("Datenschutz", "⚠", "mögliche Telefonnummer in der Anweisung")


def pruefe_paket(text: str, liste: list[Anweisung]) -> tuple[list, dict]:
    """Zusatzprüfung für 95_ki-chatbot_… (Kopf artefakt: KI-Chatbot)."""
    befunde: list = []
    info: dict = {}

    def b(bereich: str, stufe: str, meldung: str) -> None:
        befunde.append((bereich, stufe, meldung))

    k, rumpf = kopf(text)
    abschn = abschnitte(rumpf)
    for f in ("titel", "zielgruppe", "plattform"):
        if not k.get(f):
            b("Kopf", "⚠", f"Kopffeld „{f}“ fehlt")
    if not finde(abschn, "Systemanweisung"):
        b("Paket", "❌", "Abschnitt „## Systemanweisung“ fehlt")
    elif not liste:
        b("Paket", "❌", "keine Anweisung als ```text-Block unter „## Systemanweisung“")

    if k.get("zielgruppe", "").startswith("lern"):
        begr = finde(abschn, "Begrüßung")
        if not KI_HINWEIS.search(begr[1] if begr else ""):
            b("Transparenz", "⚠", "Lernende erfahren in der Begrüßung nicht, dass sie mit einer KI chatten")

    hw = finde(abschn, "Hintergrundwissen")
    if hw:
        kz, zeilen = tabelle(hw[1])
        oeff = spalte(kz, "öffentlich", "herkunft")
        for z in zeilen:
            if oeff is not None and oeff < len(z) and NICHT_OEFFENTLICH.search(z[oeff]):
                b("Hintergrundwissen", "❌", f"{z[0]}: „{z[oeff]}“ – nur öffentliches oder eigenes Material, keine Schülerarbeiten")

    pl = finde(abschn, "Probelauf")
    tests = {"gesamt": 0, "bestanden": 0, "durchgefallen": [], "offen": [], "pflicht_offen": [], "pflicht_durchgefallen": []}
    if not pl:
        b("Probelauf", "⚠", "Abschnitt „## Probelauf“ fehlt – Testfälle aus references/testfaelle.md")
    else:
        kz, zeilen = tabelle(pl[1])
        erg, pfl = spalte(kz, "ergebnis"), spalte(kz, "pflicht")
        if erg is None:
            b("Probelauf", "❌", "Spalte „Ergebnis“ fehlt")
        for z in zeilen:
            if not z or not z[0]:
                continue
            tests["gesamt"] += 1
            wert = z[erg] if erg is not None and erg < len(z) else ""
            pflicht = pfl is not None and pfl < len(z) and z[pfl].lower().startswith("ja")
            if BESTANDEN.match(wert):
                tests["bestanden"] += 1
            elif DURCHGEFALLEN.match(wert):
                tests["durchgefallen"].append(z[0])
                if pflicht:
                    tests["pflicht_durchgefallen"].append(z[0])
            else:
                tests["offen"].append(z[0])
                if pflicht:
                    tests["pflicht_offen"].append(z[0])
        if tests["gesamt"] < 6:
            b("Probelauf", "⚠", f"nur {tests['gesamt']} Testfälle – mindestens die Pflichttests aus references/testfaelle.md")
        if tests["pflicht_durchgefallen"]:
            b("Probelauf", "⚠", f"Pflichttest nicht bestanden: {', '.join(tests['pflicht_durchgefallen'])} – "
                                "Anweisung nachschärfen, Probelauf wiederholen")
    info["tests"] = tests

    fm = FREIGABE.search(rumpf)
    info["freigabe"] = f"{fm['kuerzel']}, {fm['datum']}" if fm else ""
    if fm and (tests["pflicht_durchgefallen"] or tests["pflicht_offen"]):
        b("Freigabe", "❌", "Freigabe erteilt, aber Pflichttests nicht bestanden: "
                            + ", ".join(tests["pflicht_durchgefallen"] + tests["pflicht_offen"]))
    if not fm and not re.search(r"Freigabe\s+Chatbot\s*:", rumpf, I):
        b("Freigabe", "⚠", "Zeile „Freigabe Chatbot: ausstehend“ fehlt")

    for p in PFLICHT:
        if not finde(abschn, p):
            b("Vertrag", "⚠", f"Pflichtabschnitt „## {p}“ fehlt")
    if not re.search(r"KI-gestützt erstellt", rumpf):
        b("Vertrag", "⚠", "Transparenzhinweis fehlt")
    return befunde, info


def pruefe(text: str, name: str = "Anweisung", vorgabe: str = "auto",
           max_zeichen: int | None = None) -> tuple[list[Anweisung], list, dict]:
    k, _ = kopf(text)
    ist_paket = bool(re.search(r"KI-Chatbot", k.get("artefakt", ""), I))
    if vorgabe == "auto" and ist_paket and k.get("zielgruppe") in ("lernende", "lehrkraefte"):
        vorgabe = k["zielgruppe"]
    liste = anweisungen(text, name)
    if not liste:
        raise Eingabefehler("keine Anweisung gefunden (leere Datei?)")
    for a in liste:
        pruefe_anweisung(a, vorgabe, max_zeichen)
    paket_befunde, info = pruefe_paket(text, liste) if ist_paket else ([], {})
    info["paket"] = ist_paket
    return liste, paket_befunde, info


def alle_befunde(liste: list[Anweisung], paket: list) -> list:
    return [x for a in liste for x in a.befunde] + paket


def naechster_schritt(liste: list[Anweisung], paket: list, info: dict) -> str:
    befunde = alle_befunde(liste, paket)
    if any(s == "❌" for _, s, _ in befunde):
        return "❌ beheben"
    if not info.get("paket"):
        return "Probelauf mit den Testfällen (references/testfaelle.md), Ergebnis im Paket festhalten"
    t = info.get("tests", {})
    if t.get("pflicht_durchgefallen"):
        return "Anweisung nachschärfen und Probelauf wiederholen"
    if not t.get("gesamt") or t.get("pflicht_offen"):
        return "Probelauf mit Zweitgerät bzw. Schüleransicht durchführen und eintragen"
    if not info.get("freigabe"):
        return "Freigabe durch die Lehrkraft eintragen (Freigabe Chatbot: erteilt – KÜRZEL, Datum)"
    return "bereit – einrichten und kennzeichnen (ki-kennzeichnung); Lernende einführen"


def ausgabe(liste: list[Anweisung], paket: list, info: dict) -> str:
    z = [f"Anweisungen: {len(liste)}"]
    reihenfolge = {"❌": 0, "⚠": 1, "ℹ": 2}
    for a in liste:
        art = a.zielgruppe + (", Rollenspiel" if a.rollenspiel else "")
        z.append(f"── {a.name} ({art}, {len(a.text)} Zeichen)")
        if a.bausteine:
            z.append("   Bausteine: " + " · ".join(f"{k} {'✓' if v else '✗'}" for k, v in a.bausteine.items()))
        if not a.befunde:
            z.append("   ✅ keine Befunde")
        for bereich, stufe, meldung in sorted(a.befunde, key=lambda x: reihenfolge[x[1]]):
            z.append(f"   {stufe} {bereich}: {meldung}")
    if info.get("paket"):
        t = info["tests"]
        z.append(f"── Paket · Probelauf: {t['bestanden']}/{t['gesamt']} bestanden"
                 + (f", nicht bestanden: {', '.join(t['durchgefallen'])}" if t["durchgefallen"] else "")
                 + (f", offen: {', '.join(t['offen'])}" if t["offen"] else "")
                 + f" · Freigabe Chatbot: {info.get('freigabe') or 'ausstehend'}")
        if not paket:
            z.append("   ✅ keine Befunde")
        for bereich, stufe, meldung in sorted(paket, key=lambda x: reihenfolge[x[1]]):
            z.append(f"   {stufe} {bereich}: {meldung}")
    befunde = alle_befunde(liste, paket)
    fehler = sum(s == "❌" for _, s, _ in befunde)
    warn = sum(s == "⚠" for _, s, _ in befunde)
    z.append(f"Ergebnis: {fehler} ❌ · {warn} ⚠ · nächster Schritt: {naechster_schritt(liste, paket, info)}")
    return "\n".join(z) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Systemanweisungen für KI-Chatbots prüfen.")
    p.add_argument("datei", type=Path)
    p.add_argument("--zielgruppe", choices=("auto", "lernende", "lehrkraefte"), default="auto")
    p.add_argument("--max-zeichen", type=int, default=None, help="Zeichenlimit des Anweisungsfelds der Plattform")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    try:
        liste, paket, info = pruefe(a.datei.read_text(encoding="utf-8"), a.datei.stem, a.zielgruppe, a.max_zeichen)
    except (Eingabefehler, OSError, UnicodeDecodeError) as e:
        print(f"Fehler: {e}", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({
            "anweisungen": [{"name": x.name, "zielgruppe": x.zielgruppe, "rollenspiel": x.rollenspiel,
                             "zeichen": len(x.text), "bausteine": x.bausteine,
                             "befunde": [{"bereich": b, "stufe": s, "meldung": m} for b, s, m in x.befunde]}
                            for x in liste],
            "paket": {"befunde": [{"bereich": b, "stufe": s, "meldung": m} for b, s, m in paket], **info},
            "naechster_schritt": naechster_schritt(liste, paket, info)}, ensure_ascii=False, indent=2))
    else:
        print(ausgabe(liste, paket, info), end="")
    return 1 if any(s == "❌" for _, s, _ in alle_befunde(liste, paket)) else 0


if __name__ == "__main__":
    sys.exit(main())
