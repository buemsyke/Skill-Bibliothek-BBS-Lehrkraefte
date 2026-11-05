# Schaltzeichen (DIN EN 60617) – Katalog des Werkzeugs

Aus `python3 scripts/edu.py technologieschema symbole --md` erzeugt; nicht von Hand ändern. Einsatz:
`typ: symbol`, `symbol: <Name>` (Abschn. 3c der Spec-Referenz). Katalogbogen zum Ansehen:
`python3 scripts/edu.py technologieschema symbole --svg schema/schaltzeichen.svg`.

- **Klasse** – zulässige Kennbuchstaben des Referenzkennzeichens (DIN EN IEC 81346-2:2020); ein anderes
  Kennzeichen ist ❌. Schließer: Taster -S, Sensor -B, Relaiskontakt -K, Schützkontakt -Q.
- **Anschlüsse** – `an1`, `an2` … für Anker (`"-SJ1@an1"`); sie folgen Drehung und Spiegelung.
- **Wirkv.** – „ja“: das Zeichen hat eine Wirkverbindung (Klingenmitte); nur dort wirkt `betaetigung:`
  (Betätigungsarten, Tabelle am Ende).
- **Herkunft** – *Liste*: Form mit einer Vorlage abgeglichen (Wikipedia-Liste der Schaltzeichen
  (Elektrik/Elektronik); Näherungsschalter und Betätigungsarten: Galerien mit Zeichennummern der EN-60617-Reihe);
  *zusammengesetzt*: aus solchen Zeichen gebildet (Taster = Kontakt mit Rückgang + Betätigung);
  *🔎 abgleichen*: nach Lehrbuch-Formensprache gezeichnet, vor dem Einsatz mit Norm oder eingeführtem
  Tabellenbuch vergleichen und im Schemablatt vermerken. Alle Vorlagen sind Sekundärquellen; maßgeblich ist die Norm.
- Die Zeichen sind eigene Zeichnungen (keine Kopien der Wikipedia-Dateien).

### Kontakte

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `schliesser` | Schließer | SBKQF | an1, an2 | ja | Liste | allgemeiner Schalter; schließt, wenn betätigt |
| `oeffner` | Öffner | SBKQF | an1, an2 | ja | Liste | öffnet, wenn betätigt |
| `schliesser_schuetz` | Schließer eines Schützes | QK | an1, an2 | ja | Liste | Halbkreis: Schaltgerät mit Schaltvermögen (Leistungskontakt) |
| `oeffner_schuetz` | Öffner eines Schützes | QK | an1, an2 | ja | Liste |  |
| `positionsschalter_schliesser` | Positionsschalter, Schließer | BS | an1, an2 |  | Liste | in der Wikipedia-Liste „Grenzschalter“; Dreieck an der Klinge: Betätigung durch die Position |
| `positionsschalter_oeffner` | Positionsschalter, Öffner | BS | an1, an2 |  | Liste |  |
| `wechsler` | Wechsler (mit Unterbrechung) | SBKQ | an1, an2, an3 | ja | Liste | an3 = Mittelanschluss; an1 Öffnerseite, an2 Schließerseite |
| `wechsler_ohne_unterbrechung` | Wechsler (ohne Unterbrechung) | SBKQ | an1, an2, an3 | ja | Liste | Querstrich an der Klinge: Überlappung, kein Unterbrechen beim Umschalten |

### Schaltgeräte

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `leistungsschalter` | Leistungsschalter | Q | an1, an2 | ja | Liste | Kreuz am Anschluss: selbsttätige Auslösung möglich (Schaltgerät) |
| `trennschalter` | Trennschalter | Q | an1, an2 | ja | Liste |  |
| `lasttrennschalter` | Lasttrennschalter | Q | an1, an2 | ja | Liste | Kreis: Schaltvermögen (Last schalten) |

### Kontakte

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `schliesser_rueckgang` | Schließer mit selbsttätigem Rückgang | SBK | an1, an2 | ja | Liste | Dreieck: Rückgang in die Ruhelage nach Loslassen (Feder), die Grundform des Tasters |
| `oeffner_rueckgang` | Öffner mit selbsttätigem Rückgang | SBK | an1, an2 | ja | Liste | das Dreieck ersetzt den Fuß des Öffners |

### Antriebe

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `spule` | Spule (Relais, Schütz, Magnetventil) | QKM | an1, an2 |  | Liste | elektromechanischer Antrieb; Relais -K, Schütz -Q, Ventilspule -MB (Zeichen 07-15-01) |
| `thermorelais` | Thermisches Überlastrelais (Bimetall) | F | an1, an2 |  | Liste | Bügel im Rechteck: Bimetall; Auslösung des Motorschutzes |

### Bauelemente

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `widerstand` | Widerstand | R | an1, an2 |  | 🔎 abgleichen |  (Zeichen 04-01-01) |
| `kondensator` | Kondensator | C | an1, an2 |  | 🔎 abgleichen |  (Zeichen 04-02-01) |
| `induktivitaet` | Induktivität (Spule, Drossel) | R | an1, an2 |  | 🔎 abgleichen | vier Halbkreise (Wicklung) |
| `diode` | Diode | R | an1, an2 |  | Liste | an1 Anode, an2 Kathode (Zeichen 05-03-01) |
| `led` | Leuchtdiode (LED) | RPE | an1, an2 |  | Liste | an1 Anode, an2 Kathode (Zeichen 05-03-02) |
| `sicherung` | Sicherung | F | an1, an2 |  | 🔎 abgleichen | Rechteck mit durchgehender Linie |

### Melden

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `meldeleuchte` | Meldeleuchte | PE | an1, an2 |  | 🔎 abgleichen | Kreis mit Kreuz |

### Antriebe

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `motor_drehstrom` | Drehstrommotor | M | an1, an2, an3 |  | 🔎 abgleichen | Kreis mit M und Stromart; an1 bis an3 = U1, V1, W1 |
| `motor_wechselstrom` | Wechselstrommotor | M | an1, an2 |  | 🔎 abgleichen |  |
| `motor_gleichstrom` | Gleichstrommotor | M | an1, an2 |  | 🔎 abgleichen |  |

### Erdung

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `masse` | Masse, Gehäuse | X | an1 |  | Liste | IEC 60417-5020 (Zeichen 02-15-04) |

### Taster

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `taster_schliesser` | Taster, Schließer (handbetätigt) | S | an1, an2 |  | zusammengesetzt | Schließer mit Rückgang plus Handbetätigung |
| `taster_oeffner` | Taster, Öffner (handbetätigt) | S | an1, an2 |  | zusammengesetzt |  |
| `drucktaster_schliesser` | Drucktaster, Schließer | S | an1, an2 |  | zusammengesetzt | Betätigung durch Drücken |
| `drucktaster_oeffner` | Drucktaster, Öffner | S | an1, an2 |  | zusammengesetzt |  |
| `notaus_taster` | Not-Halt-Taster (Pilz, Öffner) | S | an1, an2 |  | zusammengesetzt | Pilz-Betätigung; die Rastung (Verriegelung) zeigt die Quelle nicht – bei Bedarf im Text nennen |

### Näherungsschalter

| Name | Zeichen | Klasse | Anschlüsse | Wirkv. | Herkunft | Hinweis |
|---|---|---|---|---|---|---|
| `naeherungsschalter_schliesser` | Näherungsschalter, Schließer | B | an1, an2 |  | Liste | Rhombus: Näherung; die Wirkverbindung ist kurz (Zeichen 07-20-02) |
| `naeherungsschalter_oeffner` | Näherungsschalter, Öffner | B | an1, an2 |  | zusammengesetzt | Öffner-Gegenstück zu 07-20-02 |
| `naeherungsschalter_eisen_oeffner` | Näherungsschalter, Öffner, Betätigung durch Eisen | B | an1, an2 |  | Liste |  (Zeichen 07-20-04) |
| `naeherungsschalter_magnet_schliesser` | Näherungsschalter, Schließer, Betätigung durch Magnet | B | an1, an2 |  | Liste | z. B. Reedkontakt, Zylinderschalter (Zeichen 07-20-03) |
| `naeherungssensor` | Näherungssensor | B | an1, an2 |  | Liste | allgemein; Rhombus mit zwei Linien (Zeichen 07-19-01) |
| `beruehrungssensor` | Berührungssensor | B | an1, an2 |  | Liste |  (Zeichen 07-19-04) |
| `naeherungseinrichtung_block` | Näherungsempfindliche Einrichtung (Blocksymbol) | B | an1, an2 |  | Liste | Quadrat mit Rhombus; Anschlüsse links und rechts (Zeichen 07-19-02) |

### Betätigungsarten

Zusatz `betaetigung: <Name>` bei Zeichen mit Wirkverbindung (Spalte *Wirkv.*); `wirklaenge` (Standard 2) setzt die Länge der gestrichelten Linie.

| Name | Betätigungsart | Quelle | Hinweis |
|---|---|---|---|
| `hand` | Handbetätigung, allgemein | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `kippen` | Betätigung durch Kippen | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `drucken` | Betätigung durch Drücken (Drucktaster) | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `ziehen` | Betätigung durch Ziehen | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `drehen` | Betätigung durch Drehen | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `not_aus` | Betätigung durch Drücken, Not-Aus (Pilz) | elektricks.com, Betätigungsarten nach DIN EN 60617-7 | Pilzkopf; die Rastung (Verriegelung) zeigt die Quelle nicht |
| `thermisch` | Betätigung durch thermischen Effekt | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `annaehern` | Betätigung durch Annähern | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `beruehren` | Betätigung durch Berühren | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `annaehern_eisen` | Betätigung durch Annähern von Eisen | gallery.proficad.com, Zeichen 07-20-04 der EN-60617-Reihe |  |
| `annaehern_magnet` | Betätigung durch Annähern eines Magneten | gallery.proficad.com, Zeichen 07-20-03 der EN-60617-Reihe |  |
| `handrad` | Betätigung durch Handrad | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `fuss` | Betätigung durch Fuß | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `schluessel` | Betätigung durch Schlüssel | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `nocken` | Betätigung durch Nockensteuerung | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `pegel` | Betätigung durch Flüssigkeitspegel | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `motor` | Antrieb durch Elektromotor | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
| `elektromagnet` | Elektromagnetischer Antrieb | elektricks.com, Betätigungsarten nach DIN EN 60617-7 |  |
