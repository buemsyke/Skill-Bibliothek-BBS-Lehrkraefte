# Quellen bewerten – Typ, Interessenlage, Belegkraft

Für Lehrkräfte (Material prüfen) und für Lernende (Quellenmappe, Technikfolgenabschätzung,
Recherche). Ergänzt die Quellenhierarchie im Faktencheck (`faktencheck-methode.md`, nur in
`material-pruefen`): Diese fragt *wie verlässlich*, die Quellenbewertung fragt zusätzlich
*wer spricht mit welchem Interesse*.

## 1. Quellentypen (Kürzel verbindlich für Quellenmappen und `tfa_pruefen.py`)

| Kürzel | Typ | Beispiele | Interessenlage | Belegkraft für Sachaussagen |
|---|---|---|---|---|
| `amtlich` | Gesetz, Verordnung, Behörde, amtliche Statistik | Gesetze im Internet, Umweltbundesamt, Bundesamt für Strahlenschutz, BSI, Destatis | gering (staatlicher Auftrag) | hoch |
| `wissenschaft` | begutachtete Studie, Forschungsinstitut, Hochschule | Fachzeitschrift mit Peer-Review, Fraunhofer, KIT-ITAS | gering bis mittel (Auftraggeber prüfen) | hoch |
| `norm` | Norm, technische Regel, Richtlinie | DIN/EN/ISO, VDI-Richtlinie, DGUV-Regel | gering | hoch (Inhalt nur im Normtext) |
| `verband` | Branchen- oder Fachverband, Kammer | Bundesverband WindEnergie, Bundesverband Ziegel, VDZ | **ja** (Branche) | mittel – Zahlen oft korrekt, Auswahl und Deutung interessengeleitet |
| `unternehmen` | Hersteller, Betreiber, Dienstleister | Herstellerdatenblatt, Unternehmensbroschüre | **ja** (Verkauf) | mittel – für eigene Produktdaten hoch, für Vergleiche niedrig |
| `initiative` | NGO, Bürgerinitiative, Lobbyorganisation | Umweltverband, Bürgerinitiative gegen …, Verbraucherorganisation | **ja** (Anliegen) | mittel bis niedrig – Positionen, keine neutrale Datenbasis |
| `presse` | Qualitätsjournalismus, Fachpresse | Tageszeitung, öffentlich-rechtlicher Rundfunk, Fachmagazin | gering bis mittel | mittel – als Hinweis, Primärquelle suchen |
| `sekundaer` | Lexikon, Lehrbuch, Fachportal, Tutorial | Wikipedia, Tabellenbuch, Fachportal | gering | mittel – Einstieg, kein Beleg für Grenzwerte |
| `einzelmeinung` | Blog, Streitschrift, Video einer Einzelperson, Social Media | privater Blog, Reader „… schwere Schäden!“ | **ja** oder unbekannt | niedrig |
| `ki` | KI-generierter Text | Chatbot-Auskunft, KI-erstelltes Transkript | unbekannt | **kein Beleg** – nur Material zum Prüfen |

**Regeln:**
- **Interessengeleitete Quellen** (`verband`, `unternehmen`, `initiative`, `einzelmeinung`)
  sind erlaubt und für Kontroversen sogar nötig. Sie werden als Position gekennzeichnet und
  **nie als einziger Beleg** einer Sachaussage verwendet; daneben steht mindestens eine Quelle
  vom Typ `amtlich`, `wissenschaft` oder `norm`.
- **Desinformation** oder wissenschaftlich widerlegte Aussagen nur als ausdrücklich
  gekennzeichneter **Analysegegenstand** („Prüfen Sie diese Behauptung“), nie als Information.
- **KI-Text** ist nie Beleg. Ein KI-erstelltes Muster (z. B. Rollenspieltranskript) wird wie
  ein Erwartungshorizont fachlich geprüft und gekennzeichnet.
- Für sicherheitsrelevante Werte nur `amtlich`, `norm` oder Herstellerangabe zum konkreten
  Produkt.

## 2. Prüffragen je Quelle (für Lernende)

1. **Wer** steht dahinter (Impressum, Herausgeber, Finanzierung)?
2. **Welches Interesse** könnte die Darstellung prägen?
3. **Wann** erschienen, noch aktuell?
4. **Worauf** stützt sich die Aussage (Daten, Studie, Meinung)? Ist die Originalquelle
   auffindbar?
5. **Was sagen andere** verlässliche Quellen? (lateral lesen)

## 3. Quellenmappe – Format

| Nr. | Quelle (Titel, Herausgeber, Jahr, URL bzw. Fundstelle) | Typ | Interessenlage | Kernaussage | gestützt durch |
|---|---|---|---|---|---|
| Q1 | UBA (2021): Ökobilanzen Windenergie und Photovoltaik, Kap. 7 | amtlich | gering | energetische Amortisation unter einem Jahr | – |
| Q2 | Branchenverband (Jahr): Hintergrundpapier Ökobilanz | verband | Branche Windenergie | 30- bis 40-fache Energierückgewinnung | Q1 |

Die Spalte *Typ* enthält genau ein Kürzel aus Abschn. 1.

## 4. Typische Fehler in Material und Schülerprodukten

- Branchen- oder Aktivistenpapier als neutraler Beleg zitiert.
- Linktext widerspricht dem Inhalt (Titel „Gefahr …“, Seite „Entwarnung …“).
- Lange wörtliche Übernahmen ohne Belegfunktion (Zitatrecht: nur so viel wie nötig, mit Quelle).
- Zahl ohne Quelle und ohne Definition („Netzzugänge stiegen von … auf …“).
- KI-Text mit erfundenen Studien („Laut einer Studie des Instituts X … bis zu 15 %“).
