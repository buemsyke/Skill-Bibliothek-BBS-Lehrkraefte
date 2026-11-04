#!/usr/bin/env python3
"""ls_analyse – Vorbefund zu einer vorhandenen Lernsituation nach den Aspekten der Bibliothek.

Liest Markdown/Text sowie DOCX, ODT und PDF (über text_lesen.py im selben Ordner) – in jedem
Format: Schulvorlage, NLQ-Leermaske, KMK-Raster oder Ausgabe von lernsituation-dokumentieren
(dann zusätzlich die Formalprüfung aus lernsituation_pruefen.py). Geprüft wird, was sich finden
und zählen lässt; jede Zeile nennt die Kennung aus dem Prüfkatalog
(references/pruefkatalog-lernsituation.md):

  W1   Bestandteile der Leitlinie gefunden; älteres Format (Handlungsprodukt, sieben Phasen …)
  P    sechs Phasen der vollständigen Handlung, Zeitsumme gegen Zeitrichtwert; Hinweise zu
       Entscheiden (P3), Überprüfen (P5), Reflektieren (P6), Lernhürden (P7), Leitidee (P9)
  A10  Handlungssituation: Länge, Fragen und Aufträge, Ansprache; W5 Lesbarkeit (LIX)
  W2   Kompetenzen: nicht beobachtbare Verben; W4 Operatoren nach Bloom (bloom_check.py)
  W6   Differenzierung genannt
  Q    Querschnittsaufgaben, die vorkommen (ob eingelöst, prüft der Skill)
  W7   Versuche ohne Sicherheitshinweis bzw. Gefährdungsbeurteilung
  W9   Normen, Paragrafen, Links → Faktencheck und Linkcheck
  W10  Kontaktdaten außerhalb von Beispiel-Domains, Telefonnummern, Autorenzeilen, Platzhalter

Das Skript urteilt nicht über Qualität (Ist die Handlungssituation bedeutsam? Trägt sie die ganze
Lernsituation?) – das prüft der Skill mit Belegen. Treffer sind Hinweise: Eine Vorlage kann
Bestandteile anders benennen. Zeilennummern beziehen sich auf den gelesenen Text; --text speichert
ihn. Nur Python-Standardbibliothek.

Aufruf:
    python3 ls_analyse.py LS.(md|docx|odt|pdf) [weitere LS …] [--text ORDNER] [--json]

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bloom_check  # noqa: E402  (bloom_check.py aus _gemeinsam)
import lernsituation_pruefen as lsp  # noqa: E402
import lesbarkeit  # noqa: E402
from text_lesen import lies_text  # noqa: E402

BESTANDTEILE = [
    ("Curriculare Vorgaben", r"\bLernfeld|\bLerngebiet|\bLF\s?\d|Rahmenlehrplan|\bRLP\b|\bRRL\b|Rahmenrichtlinie|"
                             r"curriculare\s+Vorgabe|Kerncurriculum|Qualifizierungsbaustein"),
    ("Zeitrichtwert", r"Zeitrichtwert"),
    ("Fachkompetenz", r"Fachkompetenz"),
    ("Personale Kompetenz", r"Personale\s+Kompetenz"),
    ("Handlungssituation", r"Handlungssituation"),
    ("Handlungsergebnis", r"Handlungsergebnis"),
    ("Inhalte", r"(?m)^\W*Inhalte\b"),
    ("Vereinbarungen und Hinweise zur Umsetzung", r"Vereinbarungen|Hinweise\s+zur\s+Umsetzung|didaktisch-methodisch"),
    ("Distanzunterricht", r"Distanzunterricht|Distanzlernen"),
    ("Leistungsfeststellung und -bewertung", r"Leistungsfeststellung|Leistungsbewertung|Leistungsnachweis|"
                                             r"Bewertungskriterien|Bewertungsraster"),
    ("Materialien und Quellen", r"Materialien|Material\s+und\s+Medien|Quellen"),
    ("Lernumgebung", r"Lernumgebung"),
]
ALTES_FORMAT = [  # Begriffswechsel (schucu-bbs-2024.md Abschn. 7); Phasen groß geschrieben, nicht das Verb
    ("Handlungsprodukt", r"Handlungsprodukt"), ("Lernergebnis", r"\bLernergebnis"),
    ("Einstiegsszenario", r"Einstiegsszenario"), ("Selbstkompetenz", r"Selbstkompetenz"),
    ("Humankompetenz", r"Humankompetenz"), ("Methodenkompetenz", r"Methodenkompetenz"),
    ("Phase Ausführen", r"\bAusführen\b|\bAusführung\b"), ("Phase Bewerten", r"^\W*Bewerten\b"),
]
KOMPETENZ = r"Handlungskompetenz|Fachkompetenz|Personale\s+Kompetenz|Sozialkompetenz|Selbstkompetenz|" \
            r"Selbständigkeit|Methodenkompetenz"
SITUATION = r"Handlungssituation|Ausgangssituation|Einstiegsszenario|Szenario"
ABSCHNITTE = (SITUATION + r"|Handlungsergebnis|Handlungsprodukt|Lernergebnis|Handlungskompetenz|Fachkompetenz|"
              r"Personale\s+Kompetenz|Sozialkompetenz|Selbstkompetenz|Selbständigkeit|Methodenkompetenz|Inhalte|"
              r"Distanzunterricht|Vereinbarungen|Hinweise\s+zur\s+Umsetzung|Phasen\w*|Zeitrichtwert|Lernhürden|"
              r"Leistungs\w+|Materialien|Lernumgebung|Didaktisch\S*|Analysebogen|Curriculare\s+Vorgaben|Titel|"
              r"Informieren|Analysieren|Planen|Entscheiden|Durchführen|Überprüfen|Kontrollieren|Reflektieren")
ABSCHNITT_RE = re.compile(rf"^\s*(?:#{{1,6}}\s*)?\**\s*({ABSCHNITTE})\b\s*\**\s*:?\s*\**\s*(.*)$", re.IGNORECASE)

LEITIDEE = r"Leitidee|Leitgedanke|Leitfrage"
LERNHUERDEN = r"Lernhürde|Stolperstein|Fehlvorstellung|typische\w*\s+Fehler"
DIFFERENZIERUNG = r"Differenzier|Hilfekarte|gestufte\w*\s+Hilfe|Fundamentum|Additum|Sprinter|Zusatzaufgabe"
ALTERNATIVEN = r"Alternative|Variante|Entscheidungsmatrix|abw[äa]gen|Kriterien"
UEBERARBEITEN = r"überarbeit|nachbesser|optimier|Feedback|Rückmeldung"
TRANSFER = r"Transfer|übertrag|Lernfortschritt|Selbsteinschätzung|Kannliste|Lernzuwachs"
QUERSCHNITT = [
    ("BNE", r"Nachhaltig|\bBNE\b|ökolog|Ressourcen|Klima|CO2|CO₂|Energieeffizien|Kreislauf"),
    ("Demokratie", r"Demokrat|kontrovers|Mitbestimmung|Gemeinderat|Bürger|Anhörung|Positionen"),
    ("Europa", r"Europ|\bEU\b"),
    ("Medien", r"Recherche|\bKI\b|Künstliche Intelligenz|Quellenkritik|Medienbildung|digital"),
]
VERSUCH = r"\bVersuch|Experiment|Laborversuch"
SICHERHEIT = r"Gefährdungsbeurteilung|Sicherheit|Schutzbrille|Betriebsanweisung|Unterweisung|Gefahrstoff"
NORM_RE = re.compile(r"\b(?:DIN|EN|ISO|IEC|VDE|VDI|DVGW|TRBS|TRGS|DGUV|ASR)(?:\s+(?:EN|ISO|IEC|VDE))*[\s-]?\d[\d.\-:]*"
                     r"|§\s*\d+\w*")
URL_RE = re.compile(r"https?://[^\s)\]>\"']+")
MAIL_RE = re.compile(r"[\w.+-]+@([\w-]+(?:\.[\w-]+)+)")
TELEFON_RE = re.compile(r"(?<![\d.,])(?:\+49\s?|0)\d{2,5}[\s/-]?\d{3,}(?:[\s-]?\d+)?(?![\d.,])")
AUTOR_RE = re.compile(r"(?im)^\W*(?:Autor\w*|Verfasser\w*|erstellt\s+von|Ansprechpartner\w*)\b")
PLATZHALTER_RE = re.compile(r"\[(?:\.\.\.|…|X{2,}|TODO|tbd|[^\]\n]{0,40}(?:eintragen|ergänzen)[^\]\n]{0,20})\]"
                            r"|\bTODO\b|\?\?\?|\bXXX\b", re.IGNORECASE)
BEISPIEL_DOMAIN = re.compile(r"(?:^|\.)example\.(?:org|com|net)$|\.example$|\.test$|\.invalid$")
ANSPRACHE_RE = re.compile(r"\b(?:Sie|Ihr|Ihre[nmrs]?|Ihnen|ich|wir|euch|ihr)\b")
# Imperativ nur am Satzanfang – „Nach der Wartung übergeben Sie …“ ist eine Aussage
AUFTRAG_RE = re.compile(r"(?:^|[.!?:]\s+)(?:[-*•–]\s*|\d+[.)]\s*)?[A-ZÄÖÜ]\w*(?:en|ern|eln)\s+Sie\b"
                        r"|\bIhr(?:e)?\s+(?:Auftrag|Aufgabe)\b", re.MULTILINE)


def befund(liste: list[dict], kennung: str, aspekt: str, stufe: str, hinweis: str = "",
           zeilen: list[int] | None = None) -> None:
    liste.append({"id": kennung, "aspekt": aspekt, "stufe": stufe, "hinweis": hinweis, "zeilen": zeilen or []})


def zeilen_mit(text: str, muster: str, flags: int = re.IGNORECASE) -> list[int]:
    r = re.compile(muster, flags)
    return [nr for nr, z in enumerate(text.splitlines(), 1) if r.search(z)]


def ist_abschnitt(zeile: str) -> re.Match[str] | None:
    """Überschrift oder Feldbezeichnung einer Vorlage – nicht ein Satz, der das Wort enthält."""
    m = ABSCHNITT_RE.match(zeile)
    if not m:
        return None
    s = zeile.strip()
    if s.startswith("#") or s.startswith("**") or ":" in s[: len(m.group(1)) + 4] or len(s) <= 60:
        return m
    return None


def abschnitt_zeilen(text: str, muster: str) -> list[tuple[int, str]]:
    """Zeilen unter Abschnitten, deren Bezeichnung auf muster passt – bis zu einem anderen Abschnitt.
    Folgen mehrere passende Bezeichnungen aufeinander (Fach- und Personale Kompetenz), zählen alle."""
    aus: list[tuple[int, str]] = []
    drin = False
    for nr, z in enumerate(text.splitlines(), 1):
        m = ist_abschnitt(z)
        if m or re.match(r"^#{1,6}\s", z.strip()):
            drin = bool(m and re.fullmatch(muster, m.group(1), re.IGNORECASE))
            if drin and m.group(2).strip():
                aus.append((nr, m.group(2)))
            continue
        if drin and z.strip():
            aus.append((nr, z))
    return aus


def situation(text: str) -> tuple[str, int]:
    """Text der Handlungssituation (bis zum nächsten Abschnitt) und Zeile ihrer Überschrift."""
    zeilen = text.splitlines()
    for i, z in enumerate(zeilen):
        m = ist_abschnitt(z)
        if not m or not re.fullmatch(SITUATION, m.group(1), re.IGNORECASE):
            continue
        teile = [m.group(2)] if m.group(2).strip() else []
        for folge in zeilen[i + 1:]:
            if ist_abschnitt(folge) or re.match(r"^#{1,6}\s", folge.strip()):
                break
            teile.append(folge)
        rumpf = "\n".join(t for t in teile if t.strip())
        if len(re.findall(r"\w+", rumpf)) >= 15:  # sonst nur ein Verweis („siehe Handlungssituation“)
            return rumpf, i + 1
    return "", 0


def kompetenzen(text: str) -> list[tuple[int, str]]:
    """Kompetenzformulierungen im Abschnitt Handlungskompetenz – Zeilen und Tabellenzellen."""
    aus = []
    for nr, z in abschnitt_zeilen(text, KOMPETENZ):
        zellen = z.strip().strip("|").split("|") if z.lstrip().startswith("|") else [z]
        for c in zellen:
            c = re.sub(r"^\s*(?:[-*•–]|\d+[.)])\s*", "", c).strip()
            if len(c.split()) >= 3 and not re.fullmatch(r"[\s:|-]+", c) and \
                    not re.match(r"^Die\s+(?:Schülerinnen\s+und\s+Schüler|SuS|Lernenden)\s*…?$", c):
                aus.append((nr, c))
    return aus


def zeitrichtwert_min(text: str) -> int | None:
    """Zeitrichtwert der Lernsituation – nicht der des Lernfelds bzw. Lerngebiets."""
    werte = []
    # Wert in derselben oder der nächsten Zeile (Word-Tabellen: Feld und Wert in getrennten Zellen)
    for m in re.finditer(r"Zeitrichtwert([^\d\n]{0,40}\n?[^\d\n]{0,10})(\d+(?:[.,]\d+)?)\s*"
                         r"(UStd|Ustd|Std|Stunden|Unterrichtsstunden|min)?",
                         text, re.IGNORECASE):
        wert = float(m.group(2).replace(",", "."))
        minuten = round(wert) if (m.group(3) or "").lower() == "min" else round(wert * lsp.MIN_JE_STD)
        werte.append((bool(re.search(r"Lernfeld|Lerngebiet|\bLF\b", m.group(1), re.IGNORECASE)), minuten))
    eigene = [w for gebiet, w in werte if not gebiet]
    return eigene[0] if eigene else None


def phasen(text: str, b: list[dict], bibliothek: bool) -> None:
    zeilen = text.splitlines()
    gefunden, zeiten = {}, {}
    for name, muster in lsp.PHASEN:
        # Phasen als Bezeichnung (groß geschrieben) – „die SuS planen …“ in Kompetenzen zählt nicht
        nrs = zeilen_mit(text, rf"\b(?:{muster})\b", flags=0)
        if nrs:
            gefunden[name] = nrs[0]
            for nr in nrs:
                if (m := lsp.minuten(zeilen[nr - 1])) is not None:
                    zeiten[name] = m
                    break
    fehlend = [n for n, _ in lsp.PHASEN if n not in gefunden]
    if len(gefunden) < 3:
        befund(b, "P1–P6", "Sechs Phasen der vollständigen Handlung", "⚠",
               "keine Phasenplanung erkennbar – anders benannt oder nicht dokumentiert (die Leermaske der "
               "Leitlinie verlangt keine; Phasencheck als Hinweis)")
        return
    befund(b, "P1–P6", "Sechs Phasen der vollständigen Handlung", "⚠" if fehlend else "✅",
           ("nicht gefunden: " + ", ".join(fehlend)) if fehlend else "alle sechs genannt",
           sorted(set(gefunden.values())))
    zrw = zeitrichtwert_min(text)
    if bibliothek:
        pass  # Phasensumme rechnet die Formalprüfung exakt (F5)
    elif len(zeiten) == len(lsp.PHASEN) and zrw:
        summe = sum(zeiten.values())
        befund(b, "P10", "Zeitsumme der Phasen", "✅" if summe == zrw else "⚠",
               f"Σ {summe / lsp.MIN_JE_STD:g} Std. gegen Zeitrichtwert {zrw / lsp.MIN_JE_STD:g} Std. (heuristisch gelesen)")
    elif zeiten:
        befund(b, "P10", "Zeitsumme der Phasen", "ℹ", f"Zeiten für {len(zeiten)} von 6 Phasen lesbar – von Hand summieren")
    for kennung, name, muster, fehlt in (
            ("P3", "Entscheiden", ALTERNATIVEN, "keine Alternativen oder Kriterien erkennbar"),
            ("P5", "Überprüfen", UEBERARBEITEN, "keine Überarbeitung bzw. Rückmeldung erkennbar"),
            ("P6", "Reflektieren", TRANSFER, "kein Transfer und kein Blick auf den Lernfortschritt erkennbar")):
        if name in gefunden:
            treffer = zeilen_mit(text, muster)
            befund(b, kennung, f"{name} gestaltet", "ℹ" if treffer else "⚠",
                   "Stichworte gefunden – Gestaltung prüft der Skill" if treffer else fehlt, treffer[:5])


def name_im_feld(zeilen: list[str], nr: int) -> bool:
    """Steht im Feld Autor/Ansprechpartner ein Name (zwei groß geschriebene Wörter)? Leere Felder und
    Platzhalter der Vorlage zählen nicht; in Word-Tabellen steht der Wert in der nächsten Zeile."""
    wert = re.sub(r"(?i)^\W*(?:Autor\w*|Verfasser\w*|erstellt\s+von|Ansprechpartner\w*)(?:/-?in(?:nen)?)?", "",
                  zeilen[nr - 1]).strip(" |:")
    if not wert and nr < len(zeilen) and not ist_abschnitt(zeilen[nr]):
        wert = zeilen[nr].strip(" |:")
    wert = re.sub(r"\[[^\]]*\]", "", wert)
    return bool(re.search(r"\b[A-ZÄÖÜ][a-zäöüß]+\.?\s+[A-ZÄÖÜ][a-zäöüß]+", wert))


def vorhanden(b: list[dict], kennung: str, aspekt: str, text: str, muster: str, fehlt: str) -> None:
    treffer = zeilen_mit(text, muster)
    befund(b, kennung, aspekt, "✅" if treffer else "⚠", "" if treffer else fehlt, treffer[:5])


def pruefe(text: str, name: str, bibliothek: bool = False) -> list[dict]:
    b: list[dict] = []
    # W1 Bestandteile und Format
    fehlt = [n for n, m in BESTANDTEILE if not re.search(m, text, re.IGNORECASE)]
    befund(b, "W1", "Bestandteile der Leitlinie", "✅" if not fehlt else "⚠",
           ("nicht gefunden (ggf. anders benannt): " + ", ".join(fehlt)) if fehlt else "alle gefunden")
    # Änderungslisten und Begriffswechsel-Tabellen nennen alte Begriffe absichtlich
    zeilen = text.splitlines()
    ausgenommen, kopf = set(), ""
    for nr, z in enumerate(zeilen, 1):
        kopf = z if re.match(r"^#{1,6}\s", z) else kopf
        if re.search(r"Änderung|Begriffswechsel", kopf) or \
                re.search(r"→|\bstatt\b|\bersetzt\b|\bvormals\b|\bbisher\b|eingebettet|immanent", z):
            ausgenommen.add(nr)
    alt = [(n, [z for z in zeilen_mit(text, m, flags=re.MULTILINE) if z not in ausgenommen])
           for n, m in ALTES_FORMAT]
    alt = [(n, z) for n, z in alt if z]
    if alt:
        befund(b, "W1", "Begriffe älterer Vorlagen", "⚠",
               ", ".join(n for n, _ in alt) + " – ins Format 2024 überführen (lernsituation-dokumentieren, Modus B)",
               sorted({z[0] for _, z in alt}))
    # Phasen
    phasen(text, b, bibliothek)
    # Handlungssituation
    hs, kopf = situation(text)
    if not hs:
        befund(b, "A6–A14", "Handlungssituation", "⚠", "nicht als eigener Abschnitt gefunden – von Hand zuordnen")
    else:
        woerter = len(re.findall(r"\w+", hs))
        fragen = hs.count("?") + len(AUFTRAG_RE.findall(hs))
        teile = [f"{woerter} Wörter (Richtwert der Bibliothek 120–220)"]
        stufe = "✅"
        if woerter < 60 or woerter > 300:
            stufe = "⚠"
        if fragen > 3:
            stufe = "⚠"
            teile.append(f"{fragen} Fragen bzw. Aufträge – eine zentrale Problemstellung erkennbar? (A10)")
        if not ANSPRACHE_RE.search(hs):
            teile.append("keine Ich-/Sie-Ansprache (Hinweis der Bibliothek)")
        befund(b, "A10", "Handlungssituation – Umfang und Fragestellung", stufe, "; ".join(teile), [kopf])
        k = lesbarkeit.kennzahlen(hs)
        if k.get("lix") is not None:
            befund(b, "W5", "Lesbarkeit der Handlungssituation", "⚠" if k["lix"] > 60 else "✅",
                   f"LIX {k['lix']} ({k['lix_einordnung']}), Ø {k['mittlere_satzlaenge']} Wörter je Satz", [kopf])
    # Kompetenzen (im Abschnitt Handlungskompetenz, auch Tabellenzellen) und Operatoren
    treffer = bloom_check.analysiere(text, name, ziele=True)
    komp = kompetenzen(text)
    if komp:
        nicht = [(nr, c) for nr, c in komp if bloom_check.NICHT_BEOBACHTBAR_RE.search(c)]
    else:  # kein Abschnitt erkannt – Kompetenzformulierungen im ganzen Text
        nicht = [(t["zeile"], t["text"]) for t in treffer if t.get("nicht_beobachtbar")]
        komp = [(t["zeile"], t["text"]) for t in treffer if t.get("ziel")]
    if nicht:
        befund(b, "W2", "Kompetenzen beobachtbar formuliert", "⚠",
               f"{len(nicht)} von {len(komp)} nicht beobachtbar: " + " · ".join(f"„{c[:60]}“" for _, c in nicht[:3]),
               [nr for nr, _ in nicht])
    elif komp:
        befund(b, "W2", "Kompetenzen beobachtbar formuliert", "✅", f"{len(komp)} Formulierungen, keine „verstehen, kennen, wissen“")
    else:
        befund(b, "W2", "Kompetenzen beobachtbar formuliert", "⚠", "keine Kompetenzformulierungen erkannt – von Hand prüfen")
    summe = bloom_check.auswerten(treffer)
    verteilung = " · ".join(f"{s}: {n}" for s, n in summe.get("je_stufe", {}).items())
    befund(b, "W4", "Anspruch der Operatoren (Bloom-Stufen 1–6)", "⚠" if summe.get("hinweise") else "ℹ",
           f"{verteilung}" + (" – " + " ".join(summe["hinweise"]) if summe.get("hinweise") else ""))
    # Lernhürden, Leitidee, Differenzierung
    vorhanden(b, "P7", "Lernhürden dokumentiert", text, LERNHUERDEN, "nicht gefunden (Bibliothek, kein Kriterium der Leitlinie)")
    vorhanden(b, "P9", "Didaktische Leitidee", text, LEITIDEE, "nicht gefunden (Bibliothek, kein Kriterium der Leitlinie)")
    vorhanden(b, "W6", "Differenzierung", text, DIFFERENZIERUNG, "keine Differenzierung genannt")
    # Querschnitt
    q = [n for n, m in QUERSCHNITT if re.search(m, text, re.IGNORECASE)]
    befund(b, "Q1–Q7", "Querschnittsaufgaben", "ℹ",
           ("Stichworte zu: " + ", ".join(q) if q else "keine Stichworte") + " – ob eingelöst, prüft der Skill")
    # Sicherheit bei Versuchen
    if re.search(VERSUCH, text, re.IGNORECASE):
        vorhanden(b, "W7", "Sicherheit bei Versuchen", text, SICHERHEIT,
                  "Versuch ohne Hinweis auf Gefährdungsbeurteilung bzw. Sicherheit")
    # Normen, Paragrafen, Links
    normen = sorted({re.sub(r"\s+", " ", m.group(0)).strip(" .:-") for m in NORM_RE.finditer(text)})
    links = sorted(set(URL_RE.findall(text)))
    if normen or links:
        teile = []
        if normen:
            teile.append(f"{len(normen)} Normen/Paragrafen ({', '.join(normen[:6])}{' …' if len(normen) > 6 else ''})")
        if links:
            teile.append(f"{len(links)} Links")
        befund(b, "W9", "Fachliche Angaben zum Nachprüfen", "ℹ", "; ".join(teile) + " → Faktencheck bzw. Linkcheck")
    # Kontaktdaten, Autorenzeilen, Platzhalter
    mails = [m.group(1) for m in MAIL_RE.finditer(text) if not BEISPIEL_DOMAIN.search(m.group(1).lower())]
    telefone = TELEFON_RE.findall(text)
    if mails or telefone:
        teile = ([f"{len(mails)} E-Mail-Adressen (…@{', …@'.join(sorted(set(mails))[:3])})"] if mails else []) + \
                ([f"{len(telefone)} Telefonnummern"] if telefone else [])
        befund(b, "W10", "Kontaktdaten", "⚠", "; ".join(teile) + " – fiktive Akteure mit Beispiel-Domain?",
               zeilen_mit(text, MAIL_RE.pattern + "|" + TELEFON_RE.pattern)[:5])
    if autor := [nr for nr in zeilen_mit(text, AUTOR_RE.pattern) if name_im_feld(zeilen, nr)]:
        befund(b, "W10", "Namen von Lehrkräften", "ℹ", "Name im Feld Autor bzw. Ansprechpartner – vor Weitergabe "
               "oder KI-Prüfung entfernen?", autor[:3])
    if platz := zeilen_mit(text, PLATZHALTER_RE.pattern):
        befund(b, "W10", "Platzhalter", "⚠", f"{len(platz)} Zeilen mit Platzhalter", platz[:5])
    return b


def bibliotheksformat(pfad: Path, text: str) -> bool:
    return pfad.suffix.lower() in (".md", ".markdown") and bool(
        re.search(r"(?m)^artefakt:\s*\"?Lernsituation", text) or
        (re.search(r"(?m)^## Phasenplanung", text) and re.search(r"(?m)^## Analysebogen", text)))


def analysiere_datei(pfad: Path) -> dict:
    text = lies_text(pfad)
    erg = {"datei": str(pfad), "format": "Bibliotheksformat" if bibliotheksformat(pfad, text) else "freies Format",
           "zeilen": len(text.splitlines()), "woerter": len(re.findall(r"\w+", text)), "text": text}
    erg["befunde"] = pruefe(text, pfad.name, erg["format"] == "Bibliotheksformat")
    if erg["format"] == "Bibliotheksformat":
        formal = lsp.lies(pfad)
        erg["formal"] = formal
        for f in formal["befunde"]:
            befund(erg["befunde"], f"F{f['nr']}", f"Formalprüfung: {f['pruefung']}", f["stufe"], f.get("hinweis", ""))
    return erg


def markdown(ergebnisse: list[dict], quer: list[dict]) -> str:
    teile = []
    for e in ergebnisse:
        teile += [f"## Vorbefund: {Path(e['datei']).name}", "",
                  f"{e['format']} · {e['zeilen']} Zeilen, {e['woerter']} Wörter gelesen", "",
                  "| Kennung | Aspekt | Ergebnis | Hinweis | Zeilen |", "|---|---|---|---|---|"]
        for f in e["befunde"]:
            hinweis = f["hinweis"].replace("|", "/")
            teile.append(f"| {f['id']} | {f['aspekt']} | {f['stufe']} | {hinweis} | "
                         f"{', '.join(map(str, f['zeilen'][:5]))} |")
        teile.append("")
    if quer:
        teile += ["## Über mehrere Lernsituationen", "", "| Kennung | Prüfung | Ergebnis | Hinweis |", "|---|---|---|---|"]
        teile += [f"| {f['nr']} | {f['pruefung']} | {f['stufe']} | {f.get('hinweis', '')} |" for f in quer]
        teile.append("")
    teile += ["**Offen für die inhaltliche Prüfung (Skill, mit Belegen):** Analysebogen A1–A16, Phasencheck "
              "P1–P10, Leitidee L1–L5, Querschnitt Q1–Q7, Niveau W3, Quellen W8 – Zeichen: ✅ gefunden · "
              "⚠ prüfen · ❌ formaler Fehler · ℹ Hinweis.", ""]
    return "\n".join(teile)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Vorbefund zu vorhandenen Lernsituationen (jedes Format).")
    p.add_argument("dateien", nargs="+", type=Path)
    p.add_argument("--text", type=Path, help="Ordner, in den der gelesene Text je Datei gespeichert wird")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    fehlend = [str(d) for d in a.dateien if not d.is_file()]
    if fehlend:
        print("Datei nicht gefunden: " + ", ".join(fehlend), file=sys.stderr)
        return 2
    try:
        ergebnisse = [analysiere_datei(d) for d in a.dateien]
    except (OSError, ValueError, RuntimeError) as e:
        print(f"Lesen fehlgeschlagen: {e}", file=sys.stderr)
        return 2
    quer: list[dict] = []
    if len(ergebnisse) > 1 and all("formal" in e for e in ergebnisse):
        quer = lsp.lerngebiet([e["formal"] for e in ergebnisse], None, None, 0.8, None)
    elif len(ergebnisse) > 1:
        zrw = [zeitrichtwert_min(e["text"]) for e in ergebnisse]
        lesbar = [z for z in zrw if z]
        quer = [{"nr": "W12", "pruefung": "Stundenbilanz", "stufe": "ℹ",
                 "hinweis": f"Zeitrichtwerte in {len(lesbar)} von {len(zrw)} LS lesbar, Σ "
                            f"{sum(lesbar) / lsp.MIN_JE_STD:g} Std. – Kompetenzraster und Rückwärtsprobe prüft der Skill"}]
    if a.text:
        a.text.mkdir(parents=True, exist_ok=True)
        for e in ergebnisse:
            (a.text / (Path(e["datei"]).stem + ".txt")).write_text(e["text"], encoding="utf-8")
    if a.json:
        aus = [{k: v for k, v in e.items() if k not in ("text", "formal")} for e in ergebnisse]
        print(json.dumps({"dateien": aus, "quer": quer}, ensure_ascii=False, indent=2))
    else:
        print(markdown(ergebnisse, quer))
    alle = [f for e in ergebnisse for f in e["befunde"]] + quer
    return 1 if any(f["stufe"] == "❌" for f in alle) else 0


if __name__ == "__main__":
    sys.exit(main())
