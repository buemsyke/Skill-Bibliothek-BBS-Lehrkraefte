#!/usr/bin/env python3
"""schuelermaterial_pruefen – Material für Lernende auf Kürze, offene Aufträge, Darstellungen
und Dekoration prüfen (lokal, deterministisch).

Prüft den Teil für Lernende einer Markdown-Datei nach `schuelermaterial.md` – alles außer
YAML-Kopf, Kommentaren, den H1-Abschnitten für die Lehrkraft („Lösungen …“, „Didaktische
Hinweise“, „Erwartungshorizont“) und den Pflichtabschnitten (Qualitätscheck, Annahmen und
Prüfaufträge, Übergabe):

   1 Fließtext            Wörter ohne Tabellen, Code, Überschriften und Abbildungen – gegen den
                          Richtwert der Materialart (--art, sonst Kopf `materialart`/`artefakt`
                          oder Dateiname)
   2 Lange Sätze          Sätze über 25 Wörter
   3 Auftragslänge        erster Absatz je Auftrag über 25 Wörter (ohne Zeit- und Sozialform-Klammer)
   4 Teilaufgaben         mehr als drei a), b), c) an einem Auftrag
   5 Kleinschrittigkeit   Reihe kurzer Einzelschritte, „zunächst … dann … anschließend“,
                          Lesen/Unterstreichen/Abschreiben als Auftrag
   6 Darstellungen        Abbildungen, Platzhalter, Diagramme und Tabellen; offene Platzhalter;
                          Abbildungen ohne Alternativtext
   7 Aufträge mit Darstellung
   8 Karten               Hilfe je Stufe ≤ 40 Wörter, Rollenkarte ≤ 60 Wörter
   9 Dekoration           Emojis ohne Funktion, Floskeln, Schmuckbilder, Schriftfarben
  10 Lehrerangaben        Annahmen, Prüfvermerke, AFB im Teil für Lernende
  11 Wiederholungen       gleiche Sätze mehrfach
  12 Zeichnungen als SVG  keine Zeichnung aus Zeichen (ASCII-Art), kein Mermaid – in der ganzen
                          Datei, auch in Lösungen; eingebundene SVG aus einer Spec, ohne
                          Überlagerungen (über zeichnungen_pruefen.py im selben Ordner)

Schritte in Hilfen, Lösungsbeispielen und Sicherheitshinweisen sind gewollt und werden nicht
als kleinschrittig gemeldet. Das ist **keine Bewertung** – Kennzahlen und Signalwörter sind
Orientierung: ⚠ heißt „ansehen“, ❌ heißt „beheben oder im Qualitätscheck begründen“.

Aufruf:
    python3 schuelermaterial_pruefen.py DATEI.md… [--art ART] [--max-woerter N] [--json]

    --art          arbeitsblatt | infoblatt | situation | hilfen | rollenkarten | versuch |
                   programmieraufgabe | lektion | lernlandkarte | sonst
                   (Standard: aus Kopf bzw. Dateiname)
    --max-woerter  eigener Richtwert für den Fließtext

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
Nur Python-Standardbibliothek; liest Markdown und Text (Word vorher z. B. mit pandoc umwandeln).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from zeichnungen_pruefen import pruefe_zeichnungen   # zeichnungen_pruefen.py aus _gemeinsam
except ImportError:  # pragma: no cover – ohne Hilfsmodul entfällt Prüfpunkt 12
    pruefe_zeichnungen = None

RICHTWERTE = {
    "arbeitsblatt": 350, "infoblatt": 300, "situation": 150, "hilfen": 500, "rollenkarten": 400,
    "versuch": 400, "programmieraufgabe": 400, "lektion": 1500, "lernlandkarte": 1500, "sonst": 400,
}
ARTNAMEN = {
    "arbeitsblatt": "Arbeitsblatt", "infoblatt": "Infoblatt", "situation": "Situationsmaterial",
    "hilfen": "Hilfen/Differenzierung", "rollenkarten": "Rollenkarten", "versuch": "Versuchsanleitung",
    "programmieraufgabe": "Programmieraufgabe", "lektion": "Lektion", "lernlandkarte": "Lernlandkarte",
    "sonst": "Material",
}
# Reihenfolge zählt: erster Treffer im Kopf bzw. Dateinamen gewinnt
ART_MUSTER = [
    ("lektion", r"lektion|lesson"),
    ("lernlandkarte", r"lernlandkarte|edumap"),
    ("rollenkarten", r"rollenkarte"),
    ("hilfen", r"hilfe|differenzierung"),
    ("versuch", r"experiment|versuch"),
    ("programmieraufgabe", r"programmieraufgabe"),
    ("infoblatt", r"infoblatt|informationstext|infotext"),
    ("sonst", r"lastenheft|projektplan"),
    ("situation", r"situationsmaterial|störmeldung|kundenauftrag"),
    ("arbeitsblatt", r"arbeitsblatt"),
]
SATZ_MAX = 25
AUFTRAG_MAX = 25
TEILAUFGABEN_MAX = 3
TEILAUFGABEN_FEHLER = 5
SCHRITTE_MIN = 5            # so viele kurze nummerierte Einzelschritte in Folge …
SCHRITT_KURZ = 15           # … mit höchstens so vielen Wörtern
HILFE_MAX = 40
ROLLE_MAX = 60
WIEDERHOLUNG_MIN = 8        # Wörter, ab denen ein doppelter Satz zählt

LEHRER_H1 = re.compile(r"Lösung|Didaktisch|Erwartungshorizont|Lehrkr|Lehrer", re.I)
LEHRER_UNTER = re.compile(r"Lehrkr|Lehrer|Didaktische Hinweise|Erwartungshorizont|^Lösungen?(?:\s|$)", re.I)
PFLICHT = re.compile(r"^(?:Qualitätscheck|Annahmen und Prüfaufträge|Übergabe)$", re.I)
AUSNAHME = re.compile(r"Hilfe|Hilfestellung|Gerüst|Lösungsbeispiel|Beispiel|Sicherheit|"
                      r"Stolperstein|Bedienung", re.I)
DURCHFUEHRUNG = re.compile(r"Durchführung", re.I)
HILFE_KOPF = re.compile(r"\bHilfe\b|Hilfe\s*\d|Hilfekarte", re.I)
ROLLE_KOPF = re.compile(r"Rollenkarte|^Rolle\b", re.I)

WORT = re.compile(r"[0-9A-Za-zÄÖÜäöüß]+(?:[-’'][0-9A-Za-zÄÖÜäöüß]+)*")
UEBERSCHRIFT = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
ADMONITION = re.compile(r"^(?:!!!|\?\?\?\+?)\s*\w+(?:\s+\"([^\"]*)\")?")
ZAUN = re.compile(r"^\s*(```|~~~)\s*([\w-]*)")
TABELLE = re.compile(r"^\s*\|")
TABELLE_TRENNER = re.compile(r"^\s*\|?\s*:?-{3,}")
BILD = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)[^)]*\)")
BILDLINK = re.compile(r"\]\(([^)\s]+\.(?:svg|png|jpe?g|gif|webp|drawio))[^)]*\)", re.I)
HTML_BILD = re.compile(r"<(?:img|svg)\b", re.I)
PLATZHALTER = re.compile(r"\[?\s*ABBILDUNG\s*:\s*([^\]\n]*)", re.I)
# „1. …“ · „**1.** …“ · „**Aufgabe 1:** …“ · „**3 Berechnen Sie,** …“
LISTE_NR = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
LISTE_FETT_NR = re.compile(r"^(\s*)\*\*(?:Aufgabe\s+)?(\d+)[.):]?\*\*\s*(.*)$")
LISTE_FETT_SATZ = re.compile(r"^(\s*)\*\*(\d+)[.)]?\s+(.*)$")
AUFTRAG_KOPF = re.compile(r"^(?:Aufgabe|Auftrag|Arbeitsauftrag)\s*(\d+)", re.I)
TEILAUFGABE = re.compile(r"(?:^|[\s*(])\(?([a-h])\)(?=[\s*:])")
LISTENPUNKT = re.compile(r"^\s*(?:[-*+]|\d+[.)]|\(?[a-h]\))\s+")
META_KLAMMER = re.compile(r"\*?\((?:[^()]*\b(?:min|EA|PA|GA|Einzel|Partner|Gruppe|AFB|BE|Punkte?)\b[^()]*)\)\*?")
KI_ZEICHEN = re.compile(r"[🚫💡🔧]️?")
MIKRO = re.compile(r"^(?:Lesen\s+Sie|Lies|Lest|Unterstreichen\s+Sie|Unterstreiche|Unterstreicht|"
                   r"Übertragen\s+Sie|Übertrage|Übertragt|Kopieren\s+Sie|Kopiere|"
                   r"Schreiben\s+Sie\b[^.]*\bab\b|Schreibe\b[^.]*\bab\b)", re.I)
FOLGEWORT = re.compile(r"\b(?:zuerst|zunächst|dann|danach|anschließend|schließlich|"
                       r"im nächsten Schritt|als Nächstes|zum Schluss)\b", re.I)
SCHRITTWORT = re.compile(r"\bSchritt\s*\d", re.I)
DARST_WORT = re.compile(
    r"\b(?:Abb\.|Abbildung\w*|Bild(?:er|es)?|\w+bild(?:er|es)?|Skizze\w*|skizzier\w*|Zeichnung\w*|"
    r"zeichne\w*|\w*diagramm\w*|Kennlinie\w*|Grafik\w*|grafisch\w*|\w*schema\w*|\w*plan(?:s|es)?|\w*pläne|"
    r"\w*tabelle\w*|Matrix|Foto\w*|Datenblatt\w*|Struktogramm\w*|Schnitt|\w*ansicht|Graph\w*|"
    r"Kurve\w*)\b|[①-⑳]", re.I)
# Piktogramme; technische Zeichen wie ⌀ ⎓ ⏚ und ① bleiben außen vor
EMOJI = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\u231A\u231B\u2328\u23CF\u23E9-\u23F3\u23F8-\u23FA]\uFE0F?")
EMOJI_ERLAUBT = set("🚫💡🔧☐☑☒✔✘✓✗⚠⚡☢☣⛔🔎")   # 🔎 meldet Prüfpunkt 10
FLOSKEL = re.compile(
    r"viel spaß|viel erfolg|los geht'?s|los geht’s|du schaffst das|ihr schafft das|sie schaffen das|"
    r"herzlich willkommen|willkommen (?:zu|in|bei|im)\b|wusstest du|wussten sie|fun ?fact|"
    r"lass(?:t)? uns|gut gemacht|super gemacht|toll gemacht|"
    r"in (?:diesem|dieser) (?:arbeitsblatt|lektion|stunde|einheit|kapitel|abschnitt|infoblatt)\b"
    r"[^.!?]{0,40}\b(?:lernen sie|lernst du|lernt ihr|werden sie|wirst du|erfahren sie|erfährst du)",
    re.I)
DEKO_BILD = re.compile(r"deko|symbolbild|clipart|stockfoto|maskottchen|smiley|titelbild|hintergrundbild", re.I)
DEKO_BILD_HINWEIS = re.compile(r"illustration|logo", re.I)
SCHRIFTFARBE = re.compile(r"<(?:span|font|div)\b[^>]*(?:style\s*=\s*\"[^\"]*color|color\s*=)", re.I)
LEHRER_ANGABE = re.compile(r"⚠️?\s*Annahme|🔎|\bAFB\s*(?:I{1,3}|[1-3_])\b", re.I)
TRANSPARENZ = re.compile(r"^\s*>?\s*_?KI-gestützt erstellt|^\s*_?Erstellt mit KI-Unterstützung", re.I)
ABKUERZUNG = re.compile(r"\b(?:z|d|u|o|s|v|i|n)\.\s?(?:B|h|a|Ä|U|O|g|i|d)\.|\b(?:ggf|bzw|ca|Nr|usw|evtl|vgl|"
                        r"Abb|Tab|inkl|max|min|Std|bzgl|etc|Kap|zzgl|sog|Aufg|Abschn|S)\.")


# ───────────────────────────── Text in Abschnitte zerlegen ─────────────────────────────

def ohne_kommentare(text: str) -> str:
    """HTML-Kommentare durch Leerzeilen ersetzen (Zeilennummern bleiben)."""
    return re.sub(r"<!--.*?-->", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)


def kopf(text: str) -> tuple[dict[str, str], int]:
    """Einfache YAML-Kopfzeilen (schluessel: wert) und Zeilenzahl des Kopfs."""
    zeilen = text.splitlines()
    if not zeilen or zeilen[0].strip() != "---":
        return {}, 0
    werte: dict[str, str] = {}
    for i, z in enumerate(zeilen[1:], start=1):
        if z.strip() == "---":
            return werte, i + 1
        m = re.match(r"^([\w-]+)\s*:\s*(.*)$", z)
        if m:
            werte[m.group(1).lower()] = m.group(2).strip().strip("\"'")
    return {}, 0


def materialart(pfad: Path, werte: dict[str, str], text: str) -> str:
    for quelle in (werte.get("materialart", ""), werte.get("artefakt", ""), pfad.name):
        for art, muster in ART_MUSTER:
            if quelle and re.search(muster, quelle, re.I):
                return art
    if "lesson_id" in werte or re.search(r"(?m)^#\s+Fachwissen\s*$", text):
        return "lektion"
    return "sonst"


def zeilen_fuer_lernende(text: str) -> list[dict]:
    """Zeilen des Teils für Lernende mit Nr., Text, Art und Abschnittstitel."""
    werte, kopfzeilen = kopf(text)
    ergebnis: list[dict] = []
    lehrer: int | None = None              # Ebene der Überschrift, ab der der Lehrerteil gilt
    im_code = False
    code_art = ""
    abschnitt = ""
    admonition: str | None = None
    for nr, roh in enumerate(ohne_kommentare(text).splitlines(), start=1):
        if nr <= kopfzeilen:
            continue
        zaun = ZAUN.match(roh)
        if zaun:
            if not im_code:
                im_code, code_art = True, zaun.group(2).lower()
                if lehrer is None:
                    ergebnis.append({"nr": nr, "text": roh, "art": "zaun", "code": code_art,
                                     "abschnitt": admonition or abschnitt})
            else:
                im_code = False
            continue
        if im_code:
            if lehrer is None:
                ergebnis.append({"nr": nr, "text": roh, "art": "code", "code": code_art,
                                 "abschnitt": admonition or abschnitt})
            continue
        u = UEBERSCHRIFT.match(roh)
        if u:
            ebene, titel = len(u.group(1)), u.group(2)
            if lehrer is not None and ebene <= lehrer:
                lehrer = None
            if lehrer is None and ((ebene == 1 and LEHRER_H1.search(titel))
                                   or (ebene > 1 and (LEHRER_UNTER.search(titel) or PFLICHT.search(titel)))):
                lehrer = ebene
            abschnitt, admonition = titel, None
            if lehrer is None:
                ergebnis.append({"nr": nr, "text": titel, "art": "kopf", "ebene": ebene, "abschnitt": titel})
            continue
        if lehrer is not None:
            continue
        a = ADMONITION.match(roh.strip())
        if a and not roh.startswith(" "):
            admonition = a.group(1) or ""
            ergebnis.append({"nr": nr, "text": admonition, "art": "kopf", "ebene": 5, "abschnitt": admonition})
            continue
        if admonition is not None and roh.strip() and not roh.startswith(("    ", "\t")):
            admonition = None
        s = roh.strip()
        if TRANSPARENZ.search(s):
            continue
        art = "leer" if not s else "tabelle" if TABELLE.match(s) else "text"
        if art == "text" and re.fullmatch(r"(?:-{3,}|\*{3,}|_{3,})", s):
            art = "leer"
        ergebnis.append({"nr": nr, "text": roh, "art": art,
                         "abschnitt": admonition if admonition is not None else abschnitt,
                         "in_admonition": admonition is not None})
    return ergebnis


def bereinigt(zeile: str) -> str:
    """Markdown-Auszeichnung entfernen, Linktext behalten."""
    s = BILD.sub("", zeile)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"^\s*>+\s?", "", s)
    s = re.sub(r"[*_`~]+", "", s)
    return s.strip()


def woerter(text: str) -> int:
    return len(WORT.findall(text))


def ist_fliesstext(z: dict) -> bool:
    s = z["text"].strip()
    return z["art"] == "text" and not PLATZHALTER.match(s) and not s.startswith(("![", "<img", "<svg"))


def absaetze(zeilen: list[dict]) -> list[tuple[int, str]]:
    """(erste Zeilennr., Text) je Absatz bzw. Listenpunkt aus Fließtextzeilen."""
    aus: list[tuple[int, str]] = []
    nr0, puffer = 0, []
    for z in zeilen:
        if not ist_fliesstext(z):
            if puffer:
                aus.append((nr0, " ".join(puffer)))
            nr0, puffer = 0, []
            continue
        roh = z["text"]
        if puffer and LISTENPUNKT.match(roh):
            aus.append((nr0, " ".join(puffer)))
            nr0, puffer = 0, []
        if not puffer:
            nr0 = z["nr"]
        puffer.append(bereinigt(roh))
    if puffer:
        aus.append((nr0, " ".join(puffer)))
    return aus


def saetze(absatz: str) -> list[str]:
    geschuetzt = ABKUERZUNG.sub(lambda m: m.group(0).replace(".", "․"), absatz)
    teile = re.split(r"(?<=[.!?])\s+(?=[\"„»(\[]?[A-ZÄÖÜ0-9])", geschuetzt)
    return [t.replace("․", ".").strip() for t in teile if WORT.search(t)]


# ───────────────────────────── Aufträge ─────────────────────────────

def auftraege(zeilen: list[dict]) -> list[dict]:
    """Nummerierte Aufträge (oberste Ebene) mit Block, erstem Absatz und Abschnitt."""
    liste: list[dict] = []
    aktuell: dict | None = None
    for z in zeilen:
        if z["art"] == "kopf":
            m = AUFTRAG_KOPF.match(z["text"])
            if aktuell:
                liste.append(aktuell)
                aktuell = None
            if m:
                aktuell = {"nr": m.group(1), "zeile": z["nr"], "abschnitt": z["abschnitt"],
                           "kopf": True, "block": []}
            continue
        roh = z["text"]
        m = None
        if z["art"] == "text":
            m = LISTE_FETT_NR.match(roh) or LISTE_FETT_SATZ.match(roh) or LISTE_NR.match(roh)
            if m and len(m.group(1).replace("\t", "    ")) > (4 if z.get("in_admonition") else 1):
                m = None                                   # eingerückt: Unterpunkt
        if m:
            if aktuell:
                liste.append(aktuell)
            aktuell = {"nr": m.group(2), "zeile": z["nr"], "abschnitt": z["abschnitt"],
                       "kopf": False, "block": [dict(z, text=m.group(3))]}
            continue
        if aktuell is not None:
            aktuell["block"].append(z)
    if aktuell:
        liste.append(aktuell)
    for a in liste:
        erster: list[str] = []
        for z in a["block"]:
            if z["art"] != "text" or (erster and LISTENPUNKT.match(z["text"])) \
                    or (erster and z["text"].lstrip().startswith(">")):
                if erster:
                    break
                continue
            erster.append(bereinigt(z["text"]))
        satz = META_KLAMMER.sub("", KI_ZEICHEN.sub("", " ".join(erster))).strip()
        a["text"] = satz
        a["woerter"] = woerter(satz)
        blocktext = "\n".join(z["text"] for z in a["block"])
        a["teilaufgaben"] = len(set(TEILAUFGABE.findall(blocktext)))
        a["darstellung"] = bool(
            DARST_WORT.search(blocktext) or BILD.search(blocktext) or PLATZHALTER.search(blocktext)
            or any(z["art"] in ("tabelle", "zaun") for z in a["block"]))
        a["folgewoerter"] = len(FOLGEWORT.findall(satz))
        a["schrittwoerter"] = len(SCHRITTWORT.findall(blocktext))
        a["mikro"] = bool(MIKRO.match(satz))
        a["ausnahme"] = bool(AUSNAHME.search(a["abschnitt"] or ""))
        a["schritt"] = bool(DURCHFUEHRUNG.search(a["abschnitt"] or ""))   # Versuchsschritt, kein Auftrag
    return liste


def schrittfolgen(auf: list[dict]) -> list[tuple[int, int, int, str]]:
    """Reihen von ≥ SCHRITTE_MIN kurzen Aufträgen im selben Abschnitt: (von, bis, Anzahl, Abschnitt)."""
    reihen, reihe = [], []

    def abschluss():
        if len(reihe) >= SCHRITTE_MIN:
            reihen.append((reihe[0]["zeile"], reihe[-1]["zeile"], len(reihe), reihe[0]["abschnitt"]))

    for a in auf:
        passt = (not a["kopf"] and not a["ausnahme"] and 0 < a["woerter"] <= SCHRITT_KURZ
                 and (not reihe or a["abschnitt"] == reihe[-1]["abschnitt"]))
        if passt:
            reihe.append(a)
            continue
        abschluss()
        reihe = [a] if (not a["kopf"] and not a["ausnahme"] and 0 < a["woerter"] <= SCHRITT_KURZ) else []
    abschluss()
    return reihen


# ───────────────────────────── Prüfung ─────────────────────────────

def befund(liste: list, nr: int, name: str, stufe: str, hinweis: str = "") -> None:
    liste.append({"nr": nr, "pruefpunkt": name, "ergebnis": stufe, "hinweis": hinweis})


def zeilenliste(nummern: list[int], max_n: int = 4) -> str:
    teil = ", ".join(str(n) for n in nummern[:max_n])
    return "Z. " + teil + (" …" if len(nummern) > max_n else "")


def pruefe(pfad: Path, art: str | None = None, max_woerter: int | None = None) -> dict:
    text = pfad.read_text(encoding="utf-8", errors="replace")
    werte, _ = kopf(text)
    art = art or materialart(pfad, werte, text)
    richtwert = max_woerter or RICHTWERTE[art]
    zeilen = zeilen_fuer_lernende(text)
    b: list[dict] = []

    # 1 Fließtext
    fliess = [z for z in zeilen if ist_fliesstext(z)]
    w_fliess = sum(woerter(bereinigt(z["text"])) for z in fliess)
    w_tabelle = sum(woerter(bereinigt(z["text"].replace("|", " "))) for z in zeilen if z["art"] == "tabelle")
    codezeilen = sum(1 for z in zeilen if z["art"] == "code" and z.get("code") != "mermaid" and z["text"].strip())
    stufe = "✅" if w_fliess <= richtwert else "⚠" if w_fliess <= 1.5 * richtwert else "❌"
    befund(b, 1, "Fließtext", stufe,
           f"{w_fliess} Wörter (Richtwert {richtwert}, {ARTNAMEN[art]}); Tabellen {w_tabelle} Wörter, "
           f"{codezeilen} Codezeilen")

    # 2 Lange Sätze
    lange, alle_saetze = [], []
    for nr, absatz in absaetze(zeilen):
        for s in saetze(absatz):
            alle_saetze.append((nr, s))
            if woerter(s) > SATZ_MAX:
                lange.append(nr)
    befund(b, 2, f"Sätze über {SATZ_MAX} Wörter", "✅" if not lange else "⚠",
           "keine" if not lange else f"{len(lange)} ({zeilenliste(sorted(set(lange)))}) – teilen oder kürzen")

    # 3–5 Aufträge
    auf = auftraege(zeilen)
    eigene = [a for a in auf if not a["ausnahme"] and not a["schritt"]]
    zu_lang = [a for a in eigene if a["woerter"] > AUFTRAG_MAX]
    if not eigene:
        befund(b, 3, "Auftragslänge", "–", "keine nummerierten Aufträge erkannt")
    else:
        laengster = max(a["woerter"] for a in eigene)
        befund(b, 3, "Auftragslänge", "✅" if not zu_lang else "⚠",
               f"{len(eigene)} Aufträge, längster {laengster} Wörter (Richtwert {AUFTRAG_MAX})"
               + ("" if not zu_lang else "; über dem Richtwert: "
                  + ", ".join(f"Nr. {a['nr']} ({a['woerter']})" for a in zu_lang[:5])
                  + " – Kontext in die Ausgangslage, Hinweise in die Hilfen"))
    viele = [a for a in eigene if a["teilaufgaben"] > TEILAUFGABEN_MAX]
    stufe = "❌" if any(a["teilaufgaben"] > TEILAUFGABEN_FEHLER for a in viele) else "⚠" if viele else "✅"
    befund(b, 4, f"Teilaufgaben (höchstens {TEILAUFGABEN_MAX})", stufe,
           "passt" if not viele else ", ".join(f"Nr. {a['nr']}: {a['teilaufgaben']}" for a in viele)
           + " – zu einem Auftrag zusammenfassen, Zwischenschritte in die Hilfen")

    klein: list[str] = []
    for von, bis, n, abschnitt in schrittfolgen(auf):
        if DURCHFUEHRUNG.search(abschnitt or ""):
            klein.append(f"Durchführung Z. {von}–{bis}: {n} vorgegebene Schritte – nur Sicherheitsschritte "
                         f"vorgeben, den Rest planen die Lernenden (oder Öffnungsgrad im Lehrerteil begründen)")
        else:
            klein.append(f"Z. {von}–{bis}: {n} kurze Einzelschritte – zu einem Auftrag mit Ergebnis "
                         f"zusammenfassen, Schritte in die Hilfen")
    for a in eigene:
        if a["folgewoerter"] >= 3 or a["schrittwoerter"] >= 3:
            klein.append(f"Nr. {a['nr']} (Z. {a['zeile']}): Lösungsweg vorgegeben (Schrittfolge im Auftrag)")
        if a["mikro"]:
            klein.append(f"Nr. {a['nr']} (Z. {a['zeile']}): Lesen/Unterstreichen/Abschreiben als Auftrag – "
                         f"Mittel, kein Ziel; in einen Auftrag mit Ergebnis einbinden")
    befund(b, 5, "Kleinschrittigkeit", "✅" if not klein else "⚠", "keine Signale" if not klein else " · ".join(klein))

    # 6 Darstellungen
    student = "\n".join(z["text"] for z in zeilen if z["art"] != "code")
    bilder = BILD.findall(student)
    platzhalter = [z["nr"] for z in zeilen if z["art"] == "text" and PLATZHALTER.search(z["text"])]
    mermaid = sum(1 for z in zeilen if z["art"] == "zaun" and z.get("code") == "mermaid")
    links = len(BILDLINK.findall(BILD.sub("", student))) + len(HTML_BILD.findall(student))
    tabellen = sum(1 for z in zeilen if z["art"] == "tabelle" and TABELLE_TRENNER.match(z["text"].strip()))
    grafisch = len(bilder) + len(platzhalter) + mermaid + links
    teile = [f"{n} {name}" for n, name in ((len(bilder), "Abbildungen"), (mermaid, "Diagramme (Mermaid)"),
                                            (links, "verlinkte Grafiken"), (tabellen, "Tabellen")) if n]
    if platzhalter:
        teile.append(f"{len(platzhalter)} Platzhalter offen ({zeilenliste(platzhalter)}) – vor dem Einsatz ersetzen")
    ohne_alt = [alt for alt, _ in bilder if not alt.strip()]
    if ohne_alt:
        teile.append(f"{len(ohne_alt)} Abbildungen ohne Alternativtext")
    if grafisch == 0 and tabellen == 0:
        stufe = "❌" if art in ("arbeitsblatt", "infoblatt") else "⚠"
        teile.append("keine Darstellung – Zeichnung, Diagramm oder Tabelle ergänzen, wo eine trägt (sonst begründen)")
    elif grafisch == 0:
        stufe = "⚠"
        teile.append("nur Tabellen – prüfen, ob eine Zeichnung oder Grafik Text ersetzen kann")
    else:
        stufe = "⚠" if ohne_alt else "✅"
    befund(b, 6, "Darstellungen", stufe, "; ".join(teile) or "keine")

    # 7 Aufträge mit Darstellung
    if len(eigene) < 2:
        befund(b, 7, "Aufträge mit Darstellung", "–", "weniger als zwei Aufträge")
    else:
        mit = [a for a in eigene if a["darstellung"]]
        ohne = [str(a["zeile"]) for a in eigene if not a["darstellung"]]
        stufe = "✅" if len(mit) * 2 >= len(eigene) else "⚠"
        befund(b, 7, "Aufträge mit Darstellung", stufe,
               f"{len(mit)} von {len(eigene)}" + ("" if not ohne else
                                                  f"; ohne: Z. {', '.join(ohne[:6])}" + (" …" if len(ohne) > 6 else "")))

    # 8 Karten
    karten: list[str] = []
    abschnitte: dict[tuple[int, str], int] = {}
    reihenfolge: list[tuple[int, str]] = []
    aktueller: tuple[int, str] | None = None
    ueberschrift: tuple[int, str] | None = None
    for z in zeilen:
        if z["art"] == "kopf":
            aktueller = (z["nr"], z["text"]) if z.get("ebene", 0) > 1 else None
            if z.get("ebene", 0) < 5:
                ueberschrift = aktueller
            if aktueller:
                reihenfolge.append(aktueller)
                abschnitte[aktueller] = 0
            continue
        if aktueller and aktueller != ueberschrift and z["art"] != "leer" and not z.get("in_admonition"):
            aktueller = ueberschrift                      # Kasten zu Ende
        if aktueller and ist_fliesstext(z):
            abschnitte[aktueller] += woerter(bereinigt(z["text"]))
    for k in reihenfolge:
        nr, titel = k
        if HILFE_KOPF.search(titel) and abschnitte[k] > HILFE_MAX:
            karten.append(f"„{titel[:40]}“ (Z. {nr}): {abschnitte[k]} Wörter > {HILFE_MAX}")
        elif ROLLE_KOPF.search(titel) and abschnitte[k] > ROLLE_MAX:
            karten.append(f"„{titel[:40]}“ (Z. {nr}): {abschnitte[k]} Wörter > {ROLLE_MAX}")
    befund(b, 8, "Hilfe- und Rollenkarten", "✅" if not karten else "⚠", "passt" if not karten else " · ".join(karten[:5]))

    # 9 Dekoration
    deko: list[str] = []
    fehler = False
    zeichen = sorted({e.rstrip("️") for e in EMOJI.findall(student)} - EMOJI_ERLAUBT)
    if zeichen:
        deko.append("Symbole ohne Funktion: " + " ".join(zeichen) + " – durch Wörter ersetzen oder streichen")
    floskeln = [(z["nr"], m.group(0)) for z in zeilen if z["art"] in ("text", "kopf")
                for m in [FLOSKEL.search(z["text"])] if m]
    if floskeln:
        deko.append("Floskeln: " + ", ".join(f"„{f}“ (Z. {n})" for n, f in floskeln[:4]))
    bildtexte = [alt for alt, _ in bilder] + [m.group(1) for m in PLATZHALTER.finditer(student)]
    if any(DEKO_BILD.search(t) for t in bildtexte):
        fehler = True
        deko.append("Schmuckbild (Deko, Symbolbild, Clipart …) – streichen")
    elif any(DEKO_BILD_HINWEIS.search(t) for t in bildtexte):
        deko.append("Illustration oder Logo – nur mit Fachinhalt")
    if SCHRIFTFARBE.search(student):
        deko.append("Schriftfarbe als Gestaltung – Bedeutung über Wort oder Auszeichnung")
    befund(b, 9, "Dekoration", "❌" if fehler else "⚠" if deko else "✅", "keine" if not deko else " · ".join(deko))

    # 10 Lehrerangaben
    lehr = [z["nr"] for z in zeilen if z["art"] in ("text", "tabelle") and LEHRER_ANGABE.search(z["text"])]
    annahme = [z["nr"] for z in zeilen if z["art"] in ("text", "tabelle")
               and re.search(r"⚠️?\s*Annahme|🔎", z["text"])]
    befund(b, 10, "Lehrerangaben im Teil für Lernende", "❌" if annahme else "⚠" if lehr else "✅",
           "keine" if not lehr else f"{zeilenliste(lehr)} – Annahmen, Prüfvermerke und AFB in den Lehrerteil")

    # 11 Wiederholungen
    gesehen: dict[str, int] = {}
    doppelt: list[int] = []
    for nr, s in alle_saetze:
        if woerter(s) < WIEDERHOLUNG_MIN:
            continue
        schluessel = " ".join(WORT.findall(s.lower()))
        if schluessel in gesehen:
            doppelt.append(nr)
        else:
            gesehen[schluessel] = nr
    befund(b, 11, "Wiederholungen", "✅" if not doppelt else "⚠",
           "keine" if not doppelt else f"{len(doppelt)} Sätze doppelt ({zeilenliste(doppelt)}) – einmal genügt")

    # 12 Zeichnungen als SVG
    if pruefe_zeichnungen is None:
        befund(b, 12, "Zeichnungen als SVG", "–", "zeichnungen_pruefen.py fehlt im Ordner (bibliothek.py sync)")
    else:
        stufe, hinweis, _ = pruefe_zeichnungen(ohne_kommentare(text), basis=pfad.parent)
        befund(b, 12, "Zeichnungen als SVG", stufe, hinweis)

    return {"datei": str(pfad), "art": art, "richtwert": richtwert, "woerter": w_fliess,
            "auftraege": len(eigene), "darstellungen": grafisch, "tabellen": tabellen, "befunde": b}


# ───────────────────────────── Ausgabe ─────────────────────────────

def markdown(ergebnisse: list[dict]) -> str:
    aus: list[str] = []
    for e in ergebnisse:
        aus.append(f"## {Path(e['datei']).name} – {ARTNAMEN[e['art']]}, {e['woerter']} Wörter Fließtext, "
                   f"{e['auftraege']} Aufträge, {e['darstellungen']} Darstellungen\n")
        aus.append("| Nr. | Prüfpunkt | Ergebnis | Hinweis |\n|---|---|---|---|")
        for f in e["befunde"]:
            aus.append(f"| {f['nr']} | {f['pruefpunkt']} | {f['ergebnis']} | {f['hinweis'].replace('|', '/')} |")
        aus.append("")
    if len(ergebnisse) > 1:
        aus.append("## Übersicht\n\n| Datei | Art | Wörter | Richtwert | Aufträge | Darstellungen | ⚠ | ❌ |\n"
                   "|---|---|---|---|---|---|---|---|")
        for e in ergebnisse:
            stufen = [f["ergebnis"] for f in e["befunde"]]
            aus.append(f"| {Path(e['datei']).name} | {ARTNAMEN[e['art']]} | {e['woerter']} | {e['richtwert']} | "
                       f"{e['auftraege']} | {e['darstellungen']} + {e['tabellen']} Tab. | "
                       f"{stufen.count('⚠')} | {stufen.count('❌')} |")
        aus.append("")
    aus.append("_Signalwortsuche nach `schuelermaterial.md` – Orientierung, keine Bewertung. "
               "⚠ ansehen, ❌ beheben oder im Qualitätscheck begründen._")
    return "\n".join(aus)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Material für Lernende prüfen: kurz, offen, anschaulich, ohne Dekoration")
    p.add_argument("dateien", nargs="+", type=Path)
    p.add_argument("--art", choices=sorted(RICHTWERTE))
    p.add_argument("--max-woerter", type=int)
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    fehlend = [d for d in a.dateien if not d.is_file()]
    if fehlend:
        print("Fehler: nicht gefunden: " + ", ".join(map(str, fehlend)), file=sys.stderr)
        return 2
    erg = [pruefe(d, a.art, a.max_woerter) for d in a.dateien]
    print(json.dumps(erg, ensure_ascii=False, indent=2) if a.json else markdown(erg))
    return 1 if any(f["ergebnis"] == "❌" for e in erg for f in e["befunde"]) else 0


if __name__ == "__main__":
    sys.exit(main())
