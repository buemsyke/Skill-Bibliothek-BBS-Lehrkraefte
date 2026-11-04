#!/usr/bin/env python3
"""entwurf_regelcheck – Indikatoren-Check für einen Unterrichtsentwurf (Selbstcheck/Beratung).

Durchsucht einen eigenen Unterrichtsentwurf nach erkennbaren Bestandteilen der Kriterien
A1–A11 (Formalien, Bedingungsfeld, Curriculum, Rahmenbedingungen, Methoden, Handlungs-
situation, Sachanalyse, Sequenz, Leitidee/Ziele/Kompetenzen, Verlauf, Anlagen).

Ergebnis je Kriterium: welche Indikatoren erkennbar sind (mit kurzem Beleg) und welche
nicht. Das ist **keine Bewertung und keine Note** – nur eine Landkarte für den Selbstcheck:
„nicht gefunden" heißt „von Hand nachsehen", nicht „fehlt sicher".

Aufruf:
    python3 entwurf_regelcheck.py ENTWURF.(pdf|docx|odt|md|txt) [--typ A|K|S] [--pruefung] [--ohne-belege] [--json]

    --typ K bzw. S: Kurzentwurf/Sequenz – Bestandteile, die nur der ausführliche Entwurf verlangt
    (Lernausgangslage, Sachanalyse, Anlagenverzeichnis …), werden als „nicht verlangt“ geführt.
    --pruefung: prüfungsrelevanter Entwurf (Prüfungsunterricht, bewerteter Unterrichtsbesuch) –
    prüft zusätzlich, ob die KI-Nutzung im Entwurf als Hilfsmittel gekennzeichnet ist (Leitplanke).

Warnt, wenn der Entwurf Schülerdaten enthält (vor Weitergabe an eine KI entfernen oder
`text_anonymisieren.py` nutzen). Nur Python-Standardbibliothek (PDF über pdftotext).
Idee und Teile der Muster aus „Gutachten Verfahren" (src/analyse/regel.py), verallgemeinert.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

PUNKTKETTE = re.compile(r"[.…·]{3,}")

KRITERIEN: list[tuple[str, str, list[tuple[str, str]]]] = [
    ("A1", "Formalien", [
        ("Thema der Stunde", r"Thema(?:\s+der\s+(?:Unterrichts)?stunde)?\s*[:|]|^#+\s*Unterrichtsentwurf\s*:\s*\S"),
        ("Klasse/Lerngruppe", r"Klasse\s*[:|]|Lerngruppe\s*[:|]"),
        ("Datum", r"Datum(?:,\s*Zeit)?(?:,\s*Raum)?\s*[:|]\s*\S"),   # auch Vorlagenfeld „Datum, Zeit, Raum |“
        ("Zeit/Dauer", r"Zeit\s*:|Uhrzeit|\b\d{1,2}[.:]\d{2}\s*[-–]\s*\d{1,2}[.:]\d{2}|\b(?:45|90)\s*min"),
        ("Raum", r"Raum\s*[:|]"),
        ("Lernfeld/Lerngebiet", r"Lernfeld\s*\d+|\bLF\s*\d+|Lerngebiet\s*\w+"),
        ("Anlagenverzeichnis", r"Anlagenverzeichnis|Verzeichnis\s+der\s+Anlagen|^\s*Anhang\b"),
        ("Erklärung zur Selbständigkeit", r"Eigenständigkeitserklärung|selbst(?:st)?ändig\s+(?:angefertigt|verfasst)|Erklärung\s+zur\s+selbst"),
        ("Ort/Datum/Unterschrift", r"Ort\s*,?\s*Datum|Unterschrift"),
    ]),
    ("A2", "Bedingungsfeld / Lernausgangslage", [
        ("Lerngruppe beschrieben", r"Lerngruppe|Lernausgangslage|Klassenbeschreibung|Bedingungsfeld"),
        ("Vorkenntnisse", r"Vorkenntnis|Vorwissen|bereits\s+(?:bekannt|erarbeitet|eingeführt)"),
        ("Heterogenität", r"heterogen|Heterogenität|Leistungsspektrum|leistungsstark|leistungsschwäch"),
        ("sprachliche Voraussetzungen", r"sprachsensib|sprachliche\s+Voraussetz|Deutsch\s+als\s+Zweitsprache|\bDaZ\b|Fachsprache"),
        ("Folgerung für die Planung", r"(?:daraus|deshalb|daher|aus\s+diesem\s+Grund)\s+\w+(?:\s+\w+){0,4}\s+(?:Planung|geplant|plane|Methode|Differenzierung|Material)"),
    ]),
    ("A3", "Curriculare Einordnung", [
        ("Ordnungsmittel genannt", r"Rahmenlehrplan|Rahmenrichtlinie|Kerncurriculum|Ordnungsmittel|\bRLP\b|\bRRL\b|\bKC\b"),
        ("Lernfeld/Lerngebiet mit Titel", r"(?:Lernfeld|Lerngebiet)\s*\w+\s*[„\"“:*_–]|(?:Lernfeld|\bLF)\s*\d+\s*[:–-]?\s*[A-ZÄÖÜ][a-zäöüß]{3,}"),
        ("Schulisches Curriculum/Jahresplanung", r"schulisch\w*\s+Curricul|Jahresplanung|didaktisch\w*\s+Jahresplan|SchuCu"),
        ("Kompetenz aus Ordnungsmittel zitiert", r"(?:Lernfeld|Lerngebiet|Rahmenlehrplan|Rahmenrichtlinie)[^\n]{0,80}[„\"][^“\"]{25,}"),
        ("DQR-Niveau", r"\bDQR\b|Niveaustufe"),
    ]),
    ("A4", "Rahmenbedingungen", [
        ("Raum benannt", r"Raum\s*[:|]\s*\S|Fachraum|Werkstatt|Labor|Computerraum"),
        ("Medien", r"Beamer|Smartboard|Whiteboard|Tafel|Dokumentenkamera|Moodle|\bLMS\b|Tablet|PC-Arbeitsplätze"),
        ("Sitzordnung/Sitzplan", r"Sitzplan|Sitzordnung"),
        ("Zeitrahmen", r"\b(?:45|90|135|180)\s*(?:min|Minuten)|Doppelstunde|Einzelstunde"),
    ]),
    ("A5", "Methoden und Begründung", [
        ("Methoden/Sozialformen", r"Sozialform|Einzelarbeit|Partnerarbeit|Gruppenarbeit|\bEA\b|\bPA\b|\bGA\b|Plenum|Gruppenpuzzle|Think-Pair|Stationen|Rollenspiel|Placemat|Galerie"),
        ("didaktisch-methodische Begründung", r"didaktisch-?\s*methodisch|Methodenwahl|begründ\w*\s+(?:sich|die|ich)|weil\s+die\s+(?:SuS|Lernenden|Schülerinnen)"),
        ("Alternativen abgewogen", r"(?:alternativ|als\s+Alternative)\s+(?:wäre|hätte|käme|könnte)|(?:verworfen|abgewogen)\s+(?:zugunsten|gegen|habe)|(?:anstelle|anstatt|im\s+Gegensatz\s+zu)\s+(?:eines|einer|der|des|dem)\s+\w+|Methodenreflexion|Methodenvergleich"),
        ("Rolle der Lehrkraft", r"Rolle\s+der\s+Lehrkraft|(?:Lehrkraft|\bL)\s+(?:moderiert|berät|gibt\s+Impuls|informiert|erklärt|zeigt\s+vor|modelliert)"
                                r"|beratend|moderierend|impulsgebend|informierend\w*|bewertend\w*\s+Rolle"
                                r"|(?:Lehrkraft|\bL)\s+in\s+der\s+Rolle|Lehrkraftinput|fachsystematische\w*\s+Phase"),
    ]),
    ("A6", "Handlungssituation und Berufsbezug", [
        ("Handlungssituation", r"Handlungssituation|Lernsituation|Kundenauftrag|Arbeitsauftrag\s+des\s+Betriebs"),
        ("Handlungsergebnis/-produkt", r"Handlungsergebnis|Handlungsprodukt"),
        ("Berufsbezug", r"Kund\w*|Betrieb\w*|Ausbildungsbetrieb|Auftraggeber|Werkstattauftrag|beruflich\w*\s+(?:Alltag|Praxis|Handlung)"),
        ("Erweiterung der Situation je Stunde", r"Erweiterung\s+der\s+Handlungssituation|\bEHS\b|neues\s+Problem|Störung|Reklamation"),
    ]),
    ("A7", "Sachanalyse und Reduktion", [
        ("Sachanalyse", r"Sachanalyse|Sachstruktur|Mindmap|Concept-?Map"),
        ("Reduktion begründet", r"Reduktion|reduziert|bewusst\s+(?:ausgeklammert|verzichtet|nicht)|Auswahlentscheidung"),
        ("Fachquellen", r"Tabellenbuch|Fachbuch|Norm\b|DIN\s*\d|Herstellerangabe|Literatur"),
    ]),
    ("A8", "Einordnung in die Sequenz", [
        ("vorangegangene Stunden", r"vorangegangen|Vorstunde|zuvor|in\s+der\s+letzten\s+Stunde|bisher\s+(?:haben|wurde)"),
        ("Folgestunden", r"Folgestunde|anschließend|in\s+der\s+nächsten\s+Stunde|nachfolgend|danach\s*:"),
        ("Position in der Lernsituation", r"(?:Stunde|U\.-?\s*Std\.|\bStd\.)\s*\d{1,2}(?:\s*[–-]\s*\d{1,2})?\s*(?:von|/)\s*\d{1,2}"
                                          r"|\d{1,2}\s*(?:von|/)\s*\d{1,2}\s*Stunden|Makrosequenz|Unterrichtsreihe|Stundenübersicht"),
    ]),
    ("A9", "Leitidee, Ziele und Kompetenzen", [
        ("Didaktische Leitidee", r"Leitidee"),
        ("Stundenziel", r"Stundenziel|Lernziel|Ziel\s+der\s+Stunde|Kompetenzzuwachs"),
        ("Fachkompetenz", r"Fachkompetenz|\bFK\b"),
        ("Personale Kompetenz", r"Personale\s+Kompetenz|Sozialkompetenz|Selbst(?:st)?ändigkeit|Selbstkompetenz|\bPK\b"),
        ("Ziel mit „indem“ operationalisiert", r"\bindem\s+sie\b"),
        ("Beobachtbarkeit/Überprüfung", r"beobachtbar|überprüf\w+|Indikator|Erfolgskriteri|woran\s+(?:erkenn|seh)"),
    ]),
    ("A10", "Verlaufsplanung", [
        ("Informieren/Analysieren", r"Informieren|Analysieren|Problematisierung|Informationsphase"),
        ("Planen", r"\bPlanen\b|Planungsphase"),
        ("Entscheiden", r"\bEntscheiden\b|Entscheidungsphase"),
        ("Durchführen/Ausführen", r"Durchführen|Ausführen|Erarbeitung"),
        ("Überprüfen/Kontrollieren", r"Überprüfen|Kontrollieren|Kontrolle"),
        ("Reflektieren", r"Reflektieren|Reflexion"),
        ("Sicherung", r"Sicherung|Ergebnissicherung|Systematisierung"),
        ("Zeitangaben", r"\b\d{1,3}\s*['’]|\b\d{1,3}\s*min\b|\b\d{1,2}:\d{2}\b"),
        ("Reserve/Abbruchpunkt", r"didaktische\s+Reserve|Abbruchpunkt|Sollbruchstelle|Zeit\s*[+−-]"),
    ]),
    ("A11", "Anlagen", [
        ("tabellarischer Verlaufsplan", r"Verlaufsplan|Stundenverlauf"),
        ("Sitzplan", r"Sitzplan"),
        ("Material/Arbeitsauftrag", r"Arbeitsblatt|Arbeitsauftrag|Material\s+\d|Informationsblatt|\bAB\s*\d"),
        ("Erwartungshorizont", r"Erwartungshorizont|Musterlösung|Lösungsskizze"),
        ("Quellenverzeichnis", r"Quellenverzeichnis|Literaturverzeichnis|Quellen\s*:"),
    ]),
]

# Typ K (Kurzentwurf) und S (Sequenz) verlangen nicht alle Bestandteile eines ausführlichen
# Entwurfs (Typ A, Unterrichtsbesuch) – Vorlage von unterrichtsentwurf-erstellen.
NICHT_VERLANGT_KURZ = {
    "Anlagenverzeichnis", "Erklärung zur Selbständigkeit", "Ort/Datum/Unterschrift",
    "Lerngruppe beschrieben", "Heterogenität", "sprachliche Voraussetzungen", "Folgerung für die Planung",
    "Ordnungsmittel genannt", "Schulisches Curriculum/Jahresplanung", "Kompetenz aus Ordnungsmittel zitiert",
    "Sitzordnung/Sitzplan", "Alternativen abgewogen", "Sachanalyse", "Reduktion begründet",
    "Sitzplan", "Quellenverzeichnis",
}

# „Schülerdaten“ allein ist kein Signal (Vorlagen und Qualitätschecks schreiben „keine Schülerdaten“) –
# nur als Feldbezeichnung mit Inhalt („Schülerdaten: …“).
SCHUELERDATEN = re.compile(r"Schülerdaten\s*[:|]\s*\w|Schülerliste|Sitzplan\s+mit\s+Einschätzung|\|\s*Vorname\s*\|",
                           re.IGNORECASE)
VERBOTENE_ZIELVERBEN = re.compile(r"\b(?:verstehen|kennenlernen|kennen\s+lernen|wissen|begreifen)\b", re.IGNORECASE)

# Prüfungsrelevante Entwürfe: KI-Nutzung muss im Entwurf gekennzeichnet sein (Leitplanke, 19.10.2026).
KI_KENNZEICHNUNG = ("KI-Nutzung als Hilfsmittel gekennzeichnet",
                    r"KI-gestützt|KI-unterstützt|künstliche[rn]?\s+Intelligenz|Sprachmodell"
                    r"|\bKI\b[^\n]{0,80}(?:Hilfsmittel|genutzt|verwendet|eingesetzt|Selbstcheck)"
                    r"|Hilfsmittel[^\n]{0,120}\bKI\b|ChatGPT|\bClaude\b|Copilot|AIS[.\- ]?chat|fobizz")


def lies_text(pfad: Path) -> str:
    endung = pfad.suffix.lower()
    if endung == ".pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", str(pfad), "-"], capture_output=True,
                                  text=True, check=True, timeout=180).stdout
        except (OSError, subprocess.SubprocessError) as exc:
            raise SystemExit(f"PDF nicht lesbar ({exc}).")
    if endung in {".docx", ".odt"}:
        teil = "word/document.xml" if endung == ".docx" else "content.xml"
        with zipfile.ZipFile(pfad) as z:
            xml = z.read(teil).decode("utf-8", errors="replace")
        xml = re.sub(r"</(?:w:p|text:p|text:h)>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    return pfad.read_text(encoding="utf-8", errors="replace")


def _beleg(text: str, muster: str) -> str | None:
    """Erster Treffer außerhalb des Inhaltsverzeichnisses, als kurzer Auszug."""
    kandidat = None
    for m in re.finditer(muster, text, re.IGNORECASE | re.MULTILINE):
        roh = text[max(0, m.start() - 25):m.end() + 70]
        auszug = re.sub(r"\s+", " ", PUNKTKETTE.sub(" ", roh)).strip()
        if not PUNKTKETTE.search(roh) and len(auszug) >= 20:
            return auszug
        kandidat = kandidat or auszug
    return kandidat


def pruefe(text: str, typ: str = "A", pruefung: bool = False) -> dict:
    """typ: A ausführlicher Entwurf (Standard), K Kurzentwurf, S Sequenz.
    pruefung: prüfungsrelevanter Entwurf – zusätzlicher Indikator „KI-Nutzung gekennzeichnet“ (A1)."""
    ergebnis = {"kriterien": [], "warnungen": [], "typ": typ, "pruefungsrelevant": pruefung}
    for kid, name, indikatoren in KRITERIEN:
        eintraege = []
        if pruefung and kid == "A1":
            indikatoren = indikatoren + [KI_KENNZEICHNUNG]
        for label, muster in indikatoren:
            b = _beleg(text, muster)
            verlangt = typ == "A" or label not in NICHT_VERLANGT_KURZ
            eintraege.append({"indikator": label, "gefunden": b is not None, "beleg": b, "verlangt": verlangt})
        zaehlen = [e for e in eintraege if e["verlangt"]]
        ergebnis["kriterien"].append({"id": kid, "name": name, "indikatoren": eintraege,
                                      "erkennbar": sum(e["gefunden"] for e in zaehlen),
                                      "gesamt": len(zaehlen)})
    # A8 bei Typ S: die Sequenzübersicht ordnet jede Stunde ein
    if typ == "S" and re.search(r"^#+\s*Sequenzübersicht", text, re.MULTILINE):
        a8 = next(k for k in ergebnis["kriterien"] if k["id"] == "A8")
        for e in a8["indikatoren"]:
            if not e["gefunden"]:
                e.update(gefunden=True, beleg="Sequenzübersicht (Typ S)")
        a8["erkennbar"] = sum(e["gefunden"] for e in a8["indikatoren"] if e["verlangt"])
    # A10: Phasen der vollständigen Handlung (SchuCu-BBS 2024)
    a10 = next(k for k in ergebnis["kriterien"] if k["id"] == "A10")
    phasen = [e for e in a10["indikatoren"][:6]]
    fehlend = [e["indikator"] for e in phasen if not e["gefunden"]]
    a10["phasen_fehlend"] = fehlend
    # Zielformulierungen mit nicht beobachtbaren Verben
    ziele = [z for z in text.splitlines() if re.search(r"Stundenziel|Lernziel|Die\s+(?:SuS|Schülerinnen\s+und\s+Schüler|Lernenden)\b", z)]
    verboten = sorted({m.group(0).lower() for z in ziele for m in VERBOTENE_ZIELVERBEN.finditer(z)})
    if verboten:
        ergebnis["warnungen"].append(f"Zielformulierungen mit nicht beobachtbaren Verben: {', '.join(verboten)}")
    if SCHUELERDATEN.search(text):
        ergebnis["warnungen"].append("Entwurf enthält vermutlich Schülerdaten (Schülerliste/Sitzplan mit Einschätzung) – "
                                     "vor der Weitergabe an eine KI entfernen oder mit text_anonymisieren.py bearbeiten.")
    if pruefung and _beleg(text, KI_KENNZEICHNUNG[1]) is None:
        ergebnis["warnungen"].append("Prüfungsrelevanter Entwurf: KI-Nutzung nicht erkennbar gekennzeichnet – als Hilfsmittel "
                                     "angeben (Vorgaben des Studienseminars, sonst Erklärung zur selbständigen Anfertigung).")
    return ergebnis


def markdown(erg: dict, belege: bool = True) -> str:
    z = ["### Indikatoren-Check Unterrichtsentwurf (Selbstcheck – keine Bewertung)", ""]
    if erg.get("pruefungsrelevant"):
        z += ["> **Prüfungsrelevanter Entwurf** – Selbstcheck der Autorin bzw. des Autors, gekennzeichnet: "
              "KI-Nutzung im Entwurf als Hilfsmittel angeben; Überarbeitung und Formulierungen bleiben Eigenleistung.", ""]
    for w in erg["warnungen"]:
        z.append(f"> ⚠️ {w}")
    if erg["warnungen"]:
        z.append("")
    kurz = erg.get("typ", "A") != "A"
    if kurz:
        z += [f"Entwurfstyp {erg['typ']}: Bestandteile, die nur der ausführliche Entwurf (Typ A) verlangt, "
              "werden nicht gezählt.", ""]
    z += ["| Kriterium | erkennbar | nicht gefunden (von Hand prüfen) |"
          + (" nicht verlangt (Typ K/S) |" if kurz else ""), "|---|---|---|" + ("---|" if kurz else "")]
    for k in erg["kriterien"]:
        fehlt = [e["indikator"] for e in k["indikatoren"] if not e["gefunden"] and e.get("verlangt", True)]
        zeile = f"| {k['id']} {k['name']} | {k['erkennbar']}/{k['gesamt']} | {', '.join(fehlt) or '–'} |"
        if kurz:
            frei = [e["indikator"] for e in k["indikatoren"] if not e.get("verlangt", True)]
            zeile += f" {', '.join(frei) or '–'} |"
        z.append(zeile)
    a10 = next(k for k in erg["kriterien"] if k["id"] == "A10")
    z += ["", "Phasen der vollständigen Handlung (SchuCu-BBS 2024) nicht erkennbar: "
          + (", ".join(a10["phasen_fehlend"]) or "keine")]
    if belege:
        z += ["", "#### Belegstellen (Auszüge)"]
        for k in erg["kriterien"]:
            for e in k["indikatoren"]:
                if e["gefunden"]:
                    z.append(f"- {k['id']} · {e['indikator']}: „{e['beleg'][:110]}“")
    z += ["", "_Indikatoren zeigen nur, ob etwas erkennbar benannt ist – nicht, ob es gut gelöst ist. "
          "Die inhaltliche Einschätzung folgt im Selbstcheck._"]
    return "\n".join(z)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Indikatoren-Check für einen Unterrichtsentwurf (lokal).")
    p.add_argument("entwurf", type=Path)
    p.add_argument("--ohne-belege", action="store_true", help="keine Textauszüge ausgeben")
    p.add_argument("--typ", choices=("A", "K", "S"), default="A",
                   help="Entwurfstyp: A ausführlich (Standard), K Kurzentwurf, S Sequenz")
    p.add_argument("--pruefung", action="store_true",
                   help="prüfungsrelevanter Entwurf: Kennzeichnung der KI-Nutzung mitprüfen")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    erg = pruefe(lies_text(a.entwurf), a.typ, a.pruefung)
    if a.json:
        if a.ohne_belege:
            for k in erg["kriterien"]:
                for e in k["indikatoren"]:
                    e["beleg"] = None
        print(json.dumps(erg, ensure_ascii=False, indent=2))
    else:
        print(markdown(erg, belege=not a.ohne_belege))
    return 0


if __name__ == "__main__":
    sys.exit(main())
