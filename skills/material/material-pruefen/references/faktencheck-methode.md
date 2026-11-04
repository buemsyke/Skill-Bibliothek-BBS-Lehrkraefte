# Faktencheck – Methode

## Inhalt
1. Was ist prüfbar? (Aussagetypen)
2. Quellenhierarchie
3. Vorgehen: lateral lesen (SIFT)
4. Typische Fehlermuster in KI-Entwürfen
5. Befundskala und Sicherheit
6. Formulierung im Bericht
7. Quellen mit Interessenlage und KI-Texte

---

## 1. Aussagetypen

| Typ | Beispiel | Prüfweg |
|---|---|---|
| Fachaussage | „Wartung umfasst Reinigen, Schmieren, Nachstellen." | Fachliteratur, Norm, Hersteller |
| Zahl/Grenzwert | „Prüfdruck 1,5-facher Betriebsdruck über 2 h" | Norm/Regelwerk, Hersteller; Zitat mit Fundstelle |
| Normbezug | „nach DIN EN 806-4" | Existenz, Titel, Gegenstand, aktuelle Ausgabe; Inhalt nur gegen Normtext |
| Rechtsbezug | „§ 3 BetrSichV", „DGUV Vorschrift 3" | amtliche Fassung (Gesetze im Internet, DGUV-Publikationen) |
| Definition/Begriff | „Inspektion = Feststellen des Ist-Zustands" | Norm, Fachlexikon |
| Zitat/Quelle | „Laut BIBB-Studie 2023 …" | Originalquelle auffindbar? Wortlaut, Jahr, Kontext |
| Personen/Firmen/Kontakt | „Fa. X, Tel. 0551-…" | in Lernmaterial nur fiktiv; reale Daten entfernen |
| Didaktische Vorgabe | „laut SchuCu-BBS sind 7 Phasen …" | aktuelle Leitlinie |

Nicht prüfbar im engeren Sinn: Werturteile, didaktische Entscheidungen – diese gehören in die
Plausibilität bzw. die fachdidaktische Rückmeldung.

## 2. Quellenhierarchie (von oben nach unten vertrauenswürdiger → weniger)

1. **Vom Auftraggeber gelieferte Unterlagen** (Ordnungsmittel, Herstellerunterlagen, Normauszug)
2. **Amtliche Quellen**: Gesetze und Verordnungen (gesetze-im-internet.de), Kultusministerium/
   NLQ, KMK, DQR-Liste, DGUV-Vorschriften und -Regeln, BAuA-Technische Regeln
3. **Normen** (DIN/EN/ISO) – Titel und Ausgabe frei recherchierbar, Inhalt meist nur im
   Normtext (Schule: Normenportal/Bibliothek)
4. **Hersteller, Fachverbände, Kammern**
5. **Fachbücher und Tabellenbücher** (mit Auflage)
6. **Sekundärquellen** (Lexika, Wikipedia, Fachportale) – als Einstieg, nicht als Beleg für
   sicherheitsrelevante Werte

## 3. Vorgehen: lateral lesen (SIFT nach Caulfield)

- **S**top – Aussage isolieren, nicht sofort glauben oder verwerfen.
- **I**nvestigate the source – Wer steht hinter der Quelle? Aktualität?
- **F**ind better coverage – mehrere unabhängige, verlässliche Quellen suchen.
- **T**race – Zitate und Zahlen zur Originalquelle zurückverfolgen.

Mit Websuche: gezielte Suchanfragen („DIN EN 806-4 Titel", „DGUV Regel 100-500 Kapitel 2.10"),
Treffer aus Stufe 2–4 bevorzugen, Fundstelle (URL, Abschnitt, Abrufdatum) notieren.
Ohne Websuche: Fachwissen nutzen, Sicherheit ehrlich angeben, Prüfauftrag formulieren.

## 4. Typische Fehlermuster in KI-Entwürfen (gezielt prüfen)

| Muster | Beispiel |
|---|---|
| erfundene oder verwechselte Norm-/Regelnummern | „DGUV Regel 101-005 (Betreiben von Arbeitsmitteln)" – gemeint ist DGUV Regel 100-500 |
| falscher Normtitel oder falsche Ausgabe | „DIN EN 806-4:2020-06 – Inbetriebnahme und Spülung" statt „DIN EN 806-4:2010-06 – Teil 4: Installation" |
| veraltete Regelwerke | alte BGV/BGR-Bezeichnungen statt DGUV Vorschrift/Regel; zurückgezogene Normausgaben |
| plausibel klingende, aber falsche Werte | Dichtheitsprüfung „1,5-facher Betriebsdruck, 2 h" statt 1,1-fach, 30 min (Prüfung mit Wasser) |
| falsche Lernfeldzuordnung | richtiges Thema, falsche LF-Nummer oder frei erfundener LF-Titel |
| Tätigkeiten falsch zugeordnet | Auszubildende „kalibrieren" Manometer; Sicherheitsventile werden „eingestellt" |
| Begriffe aus fremdem Kontext | Heizkörper „entlüften" im Spülplan einer Trinkwasserinstallation |
| Länder-Mix | österreichische/schweizerische Normen oder Rechtsbegriffe |
| erfundene Quellen | Studien, Buchtitel, ISBN, URLs, die es nicht gibt |
| echte Kontaktdaten in fiktiven Szenarien | realistisch wirkende Telefonnummern, echte Firmen |
| innere Widersprüche | 12 Wohneinheiten im Text, 8 im Spülplan |
| Tippfehler mit Bedeutungswechsel | „Leichtigkeit" statt „Undichtigkeit" |
| veraltete didaktische Begriffe | „Handlungsprodukt", 7 Phasen statt SchuCu-BBS 2024 |

## 5. Befundskala und Sicherheit

| Befund | Bedeutung |
|---|---|
| ✅ bestätigt | durch Quelle/Rechnung belegt |
| ⚠️ ungenau/unvollständig | im Kern richtig, aber missverständlich, verkürzt oder veraltet |
| ❌ falsch | widerspricht belegter Quelle oder Rechnung (nur bei hoher Sicherheit) |
| 🔎 nicht prüfbar | Quelle nicht zugänglich (z. B. Normtext) oder Sicherheit zu gering → Prüfauftrag |

**Sicherheit:** hoch (Quelle Stufe 1–3 oder eindeutige Rechnung) · mittel (Stufe 4–5 oder
gesichertes Fachwissen ohne Quelle) · niedrig (Einschätzung) → bei „niedrig" immer 🔎.

**Schwere:** kritisch (Sicherheit, Recht, Prüfungsrelevanz) · wesentlich (fachlich falsch) ·
gering (Formulierung, Aktualität ohne Folgen).

## 6. Formulierung im Bericht
7. Quellen mit Interessenlage und KI-Texte

> **F-01** · Phase 3, Teil A · „Dichtheitsprüfung mit 1,5-fachem Betriebsdruck über 2 h" ·
> ❌ falsch · kritisch · Sicherheit hoch · Herstellerunterlage nach DIN EN 806-4 und
> ZVSHK-Merkblatt: Prüfung mit Wasser 1,1-facher zulässiger Betriebsdruck, 30 min (bei
> Kunststoffrohren zusätzliche Stufe). · Vorschlag: Werte aus aktuellem Merkblatt übernehmen,
> Werkstoff der Übungsanlage berücksichtigen. · Quelle: Herstellerunterlage TECE (12/2016) · 🔎 Prüfauftrag: aktuelle
> Merkblattfassung einsehen.

Vollständiges Beispiel eines Prüfberichts: `beispiele/90_pruefbericht_shk-trinkwasser-inbetriebnahme.md`
im Bibliotheksordner (nicht Teil des installierten Skills).

## 7. Quellen mit Interessenlage und KI-Texte

- Neben der Verlässlichkeit (Abschn. 2) auch den **Quellentyp** und die **Interessenlage**
  bestimmen (`quellenbewertung.md`, falls vorhanden): Branchenverband, Unternehmen, Initiative
  oder Einzelperson sind Positionen, keine neutralen Belege.
- Steht eine solche Quelle als einziger Beleg einer Sachaussage: ⚠️ mit Gegenquelle vom Typ
  amtlich, wissenschaftlich oder Norm.
- **Widerlegte Behauptungen** (z. B. Gesundheitsgefahren unterhalb der Grenzwerte, wenn die
  zuständige Bundesbehörde keinen Beleg sieht) nur als gekennzeichneten Analysegegenstand stehen
  lassen; sonst ❌.
- **Linktext gegen Inhalt** prüfen: Titel „Gefahr …“, Seite „Entwarnung …“ ist ein Befund.
- **KI-erzeugte Texte** (auch gekennzeichnete Musterlösungen und Transkripte) wie einen
  Erwartungshorizont prüfen. Typisch sind sachfremde Verknüpfungen, erfundene Studien
  („Laut einer Studie des Instituts X … bis zu 15 %“) und Abschnitte mit schematischem „Fazit“.
  Ungekennzeichnete KI-Anteile an Material als Hinweis an die Lehrkraft melden (Transparenz),
  nicht als Fehler.

