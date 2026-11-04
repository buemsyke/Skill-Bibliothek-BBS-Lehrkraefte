"""diagramme – ER-, Klassen-, Block- und Struktogramme als draw.io / SVG.

Submodule:
    box           UML-/Relationenschema-Diagramme  (eduwerkzeuge.diagramme.box)
    chen          Chen-ER-Diagramme                (eduwerkzeuge.diagramme.chen)
    flow          Block-/Ablaufdiagramme           (eduwerkzeuge.diagramme.flow)
    struktogramm  Nassi-Shneiderman-Diagramme      (eduwerkzeuge.diagramme.struktogramm)
    svg           Hybrid-.drawio.svg bauen         (eduwerkzeuge.diagramme.svg)
    validate      .drawio-Dateien prüfen           (eduwerkzeuge.diagramme.validate)

Beispiel:
    from eduwerkzeuge.diagramme import validate
    fehler = validate.validate_file(Path("x.drawio.svg"))
"""

from . import box, chen, flow, struktogramm, svg, validate

__all__ = ["box", "chen", "flow", "struktogramm", "svg", "validate"]
