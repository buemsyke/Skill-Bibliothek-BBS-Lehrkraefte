"""technologieschema — Technologieschemata (Anlagenbilder für Steuerungsaufgaben) aus YAML als SVG.

Das Technologieschema zeigt die Anlage mit ihren Betriebsmitteln (Zylinder, Ventile, Sensoren,
Taster, Leuchtmelder, Motoren, Förderbänder, Behälter, Rohre) so, wie Lernende sie vor sich sehen –
keine Normzeichnung (kein Schaltplan, kein Pneumatikplan). Claude beschreibt die Anlage in einer
kurzen Spec; Zeichnung, Anker, Legende und Prüfung übernimmt das Werkzeug.

    edu-technologieschema svg SPEC.yaml        # prüft und erzeugt <out>.svg und <out>.drawio.svg (bearbeitbar)
    edu-technologieschema pruefen SPEC.yaml    # nur prüfen
    edu-technologieschema legende SPEC.yaml    # Legende (Kennzeichen | Betriebsmittel | Lage/Aufgabe)
    edu-technologieschema textform SPEC.yaml   # GRAFCET als Tabelle Schritt | Aktion | Transition
    edu-technologieschema typen                # alle Bauteile mit ihren Schlüsseln
    edu-technologieschema symbole [--svg|--md] # Schaltzeichen nach DIN EN 60617 (Liste, Katalogbogen, Markdown)

GRAFCET entsteht als eigenes Bauteil (``typ: grafcet``): die Spec nennt die Struktur, Lage und Normsymbole
kommen aus dem Werkzeug, speichernde Aktionen haben immer Zuweisung und Pfeil.

Referenzkennzeichen sind immer nach DIN EN IEC 81346-2:2020 (Form, Tabelle 2, Klasse passend zum Bauteil,
eine Tiefe je Klasse); Linien und Rohre verlaufen rechtwinklig; Schaltzeichen tragen Anschlusspunkte.
"""

from .drawio import drawio_svg, modell  # noqa: F401
from .pruefen import Befund, bauen, bild_pruefen, lade, legende_markdown, pruefe, schema_pruefen  # noqa: F401
from .teile import SCHEMA, SpecFehler  # noqa: F401
