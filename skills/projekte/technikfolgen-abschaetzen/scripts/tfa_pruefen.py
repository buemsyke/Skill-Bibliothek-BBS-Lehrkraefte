#!/usr/bin/env python3
"""tfa_pruefen – Technikfolgenabschätzung (Dossier oder vorhandenes Material) prüfen.

Liest ein Dossier nach assets/vorlage-tfa-dossier.md (Markdown; DOCX/ODT/PDF über text_lesen.py,
falls vorhanden – dann ohne Tabellenprüfung, nur Signalwörter):

  Hypothesen     je Hypothese Prüfverfahren, Ergebnis (bestätigt, widerlegt, offen) und Quellen
  Quellen        jede Quelle mit Typ aus der Liste in quellenbewertung.md; eine Hypothese, deren
                 Quellen alle interessengeleitet sind (verband, unternehmen, initiative,
                 einzelmeinung) oder KI-Text, bekommt ⚠
  Perspektiven   mindestens 2 (❌ darunter), Richtwert --min-perspektiven (Standard 3); Pro und Contra
  Wertbereiche   mindestens --min-werte (Standard 3) und ein Abschnitt Zielkonflikt
  Urteil         Abschnitt vorhanden
  Überwältigung  Signalwörter wie „Einwandbehandlung“, „Einwände entkräften“, „Akzeptanz schaffen“;
                 direkt in Anführungszeichen gilt die Fundstelle als Zitat (✅ mit Hinweis)

Aufruf:
    python3 tfa_pruefen.py 44_tfa_….md [--min-perspektiven 3] [--min-werte 3] [--json]

Exit-Code: 0 = kein ❌, 1 = mindestens ein ❌, 2 = Eingabefehler.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from text_lesen import lies_text  # type: ignore
except Exception:  # noqa: BLE001
    def lies_text(pfad: Path) -> str:  # type: ignore[misc]
        return Path(pfad).read_text(encoding="utf-8", errors="replace")

# Kürzel wie in quellenbewertung.md Abschn. 1 (Konsistenz per Test gesichert)
QUELLENTYPEN = ["amtlich", "wissenschaft", "norm", "verband", "unternehmen", "initiative", "presse",
                "sekundaer", "einzelmeinung", "ki"]
INTERESSENGELEITET = {"verband", "unternehmen", "initiative", "einzelmeinung", "ki"}
ERGEBNISSE = ("bestätigt", "widerlegt", "offen")
WERTBEREICHE = ["funktionsfähigkeit", "wirtschaftlichkeit", "wohlstand", "sicherheit", "gesundheit",
                "umweltqualität", "persönlichkeitsentfaltung", "gesellschaftsqualität"]
UEBERWAELTIGUNG = re.compile(r"einwandbehandlung|einwände?\s+(?:entkräften|ausräumen|widerlegen|behandeln)|"
                             r"akzeptanz\s+schaffen|überzeugend(?:er)?\s+präsentieren|bedenken\s+zerstreuen",
                             re.IGNORECASE)


ANFUEHRUNG_AUF = "„\"»«'‚"


def ueberwaeltigung(text: str) -> tuple[str, str, str]:
    """Signalwörter melden; in Anführungszeichen gilt eine Fundstelle als Zitat (Metaebene) – ✅ mit Hinweis."""
    rahmung, zitiert = set(), set()
    for m in UEBERWAELTIGUNG.finditer(text):
        (zitiert if m.start() and text[m.start() - 1] in ANFUEHRUNG_AUF else rahmung).add(m.group(0))
    if rahmung:
        return ("Überwältigungsverbot", "⚠️", "Signalwörter: " + ", ".join(f"„{t}“" for t in sorted(rahmung))
                + " – Rahmung ergebnisoffen formulieren (Beutelsbacher Konsens)")
    if zitiert:
        return ("Überwältigungsverbot", "✅", "nur zitiert: " + ", ".join(f"„{t}“" for t in sorted(zitiert)))
    return ("Überwältigungsverbot", "✅", "keine Signalwörter")


def _zellen(z: str) -> list[str]:
    return [c.strip().strip("*").strip() for c in z.strip().strip("|").split("|")]


def tabelle_unter(text: str, ueberschrift: str) -> list[list[str]]:
    """Erste Tabelle unter einer Überschrift (Zeilen ohne Trennzeile, mit Kopf)."""
    zeilen = text.splitlines()
    for i, z in enumerate(zeilen):
        if re.match(rf"^#+\s+{ueberschrift}", z, re.IGNORECASE):
            tab = []
            for w in zeilen[i + 1:]:
                if w.startswith("#"):
                    break
                if w.strip().startswith("|") and not re.fullmatch(r"\s*\|?[\s:|\-]+\|?\s*", w):
                    tab.append(_zellen(w))
                elif tab and not w.strip().startswith("|"):
                    break
            return tab
    return []


def abschnitt_text(text: str, ueberschrift: str) -> str | None:
    m = re.search(rf"^(#+)\s+{ueberschrift}[^\n]*\n(.*?)(?=^#{{1,6}}\s|\Z)", text, re.IGNORECASE | re.M | re.S)
    return m.group(2).strip() if m else None


def _spalte(kopf: list[str], *namen: str) -> int | None:
    for i, k in enumerate(kopf):
        if any(k.lower().startswith(n) for n in namen):
            return i
    return None


def pruefe(text: str, min_persp: int = 3, min_werte: int = 3) -> list[tuple[str, str, str]]:
    befunde: list[tuple[str, str, str]] = []
    if not any(tabelle_unter(text, u) for u in ("Quellenmappe", "Hypothesen", "Perspektiven")):
        return [("Format", "➖", "kein Dossier nach Vorlage (Modus B: vorhandenes Material) – nur Signalwörter geprüft"),
                ueberwaeltigung(text)]

    # Quellen
    quellen: dict[str, str] = {}
    qt = tabelle_unter(text, "Quellenmappe")
    if qt:
        k = qt[0]
        i_nr, i_typ = _spalte(k, "nr"), _spalte(k, "typ")
        ohne_typ = []
        for r in qt[1:]:
            r = r + [""] * (len(k) - len(r))
            nr = r[i_nr] if i_nr is not None else r[0]
            typ = (r[i_typ] if i_typ is not None else "").lower().strip("` ")
            if typ in QUELLENTYPEN:
                quellen[nr.upper()] = typ
            else:
                ohne_typ.append(nr)
                quellen[nr.upper()] = ""
        befunde.append(("Quellentypen", "✅" if not ohne_typ else "❌",
                        f"{len(quellen)} Quellen typisiert" if not ohne_typ
                        else "ohne gültigen Typ: " + ", ".join(ohne_typ) + f" (Liste: {', '.join(QUELLENTYPEN)})"))
    else:
        befunde.append(("Quellenmappe", "❌", "keine Quellenmappe (Tabelle mit Spalte „Typ“)"))

    # Hypothesen
    ht = tabelle_unter(text, "Hypothesen")
    if not ht:
        befunde.append(("Hypothesen", "❌", "keine Hypothesentabelle"))
    else:
        k = ht[0]
        i_nr, i_hy = _spalte(k, "nr"), _spalte(k, "hypothese")
        i_ve, i_qu, i_er = _spalte(k, "prüfverfahren", "verfahren"), _spalte(k, "quelle"), _spalte(k, "ergebnis")
        mangel, hinweis = [], []
        for r in ht[1:]:
            r = r + [""] * (len(k) - len(r))
            nr = r[i_nr] if i_nr is not None else r[0]
            if i_ve is None or not r[i_ve].strip("–- "):
                mangel.append(f"{nr} ohne Prüfverfahren")
            erg = (r[i_er] if i_er is not None else "").lower()
            if not any(e in erg for e in ERGEBNISSE):
                mangel.append(f"{nr} ohne Ergebnis (bestätigt/widerlegt/offen)")
            refs = re.findall(r"\bQ\d+\b", r[i_qu] if i_qu is not None else "", re.IGNORECASE)
            if not refs:
                mangel.append(f"{nr} ohne Quelle")
            else:
                unbekannt = [q for q in refs if q.upper() not in quellen]
                if unbekannt:
                    mangel.append(f"{nr}: Quelle {', '.join(unbekannt)} fehlt in der Quellenmappe")
                typen = {quellen.get(q.upper(), "") for q in refs}
                if typen and typen <= INTERESSENGELEITET:
                    hinweis.append(f"{nr} stützt sich nur auf interessengeleitete Quellen oder KI-Text ({', '.join(sorted(typen))})")
            if i_hy is not None and len(r[i_hy].split()) < 5:
                hinweis.append(f"{nr}: Hypothese sehr kurz – prüfbar formuliert (Größe, Ort, Maßstab)?")
        befunde.append(("Hypothesen", "❌" if mangel else ("⚠️" if hinweis else "✅"),
                        "; ".join(mangel + hinweis) or f"{len(ht) - 1} Hypothesen mit Verfahren, Ergebnis und Quellen"))
        ergebnisse = " ".join((r + [""] * len(k))[i_er] for r in ht[1:] if i_er is not None).lower()
        if ht[1:] and "bestätigt" not in ergebnisse and "offen" not in ergebnisse:
            befunde.append(("Ergebnisoffenheit", "⚠️", "alle Hypothesen widerlegt – sind die Bedenken der Betroffenen fair geprüft?"))

    # Perspektiven
    pt = tabelle_unter(text, "Perspektiven")
    if not pt:
        befunde.append(("Perspektiven", "❌", "keine Perspektiventabelle"))
    else:
        k = pt[0]
        i_pro, i_con = _spalte(k, "pro"), _spalte(k, "contra", "kontra")
        n = len(pt) - 1
        contra = any((r + [""] * len(k))[i_con].strip("–- ") for r in pt[1:]) if i_con is not None else False
        pro = any((r + [""] * len(k))[i_pro].strip("–- ") for r in pt[1:]) if i_pro is not None else False
        status = "❌" if n < 2 or not (pro and contra) else ("⚠️" if n < min_persp else "✅")
        teile = [f"{n} Perspektiven"]
        if not (pro and contra):
            teile.append("Pro und Contra nicht beide belegt")
        if 2 <= n < min_persp:
            teile.append(f"Richtwert {min_persp}")
        befunde.append(("Perspektiven", status, " · ".join(teile)))

    # Wertbereiche und Zielkonflikt
    wt = tabelle_unter(text, "Wertbereiche")
    gefunden = {w for r in wt[1:] for w in WERTBEREICHE if w in " ".join(r).lower()} if wt else set()
    befunde.append(("Wertbereiche", "✅" if len(gefunden) >= min_werte else ("❌" if not gefunden else "⚠️"),
                    f"{len(gefunden)} Wertbereiche ({', '.join(sorted(gefunden)) or '–'}); Richtwert {min_werte}"))
    zk = abschnitt_text(text, "Zielkonflikt")
    befunde.append(("Zielkonflikt", "✅" if zk and len(zk) > 20 else "❌",
                    "benannt" if zk and len(zk) > 20 else "Abschnitt „Zielkonflikt“ fehlt oder ist leer"))
    ur = abschnitt_text(text, "Urteil")
    befunde.append(("Urteil", "✅" if ur and len(ur) > 20 else "⚠️",
                    "vorhanden" if ur and len(ur) > 20 else "Abschnitt „Urteil“ fehlt"))

    # Überwältigung
    befunde.append(ueberwaeltigung(text))
    return befunde


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Technikfolgenabschätzung prüfen.")
    ap.add_argument("datei", type=Path)
    ap.add_argument("--min-perspektiven", type=int, default=3)
    ap.add_argument("--min-werte", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv)
    if not a.datei.is_file():
        print(f"Fehler: nicht gefunden: {a.datei}", file=sys.stderr)
        return 2
    befunde = pruefe(lies_text(a.datei), a.min_perspektiven, a.min_werte)
    if a.json:
        print(json.dumps(befunde, ensure_ascii=False, indent=2))
    else:
        print("| Prüfpunkt | Ergebnis | Hinweis |\n|---|---|---|")
        for p, s, h in befunde:
            print(f"| {p} | {s} | {h} |")
        print("\n_Prüft Aufbau, Quellenlage und Rahmung – die fachliche Richtigkeit prüft material-pruefen._")
    return 1 if any(s == "❌" for _, s, _ in befunde) else 0


if __name__ == "__main__":
    sys.exit(main())
