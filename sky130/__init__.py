"""sky130 - skywater gdsfactory pdk"""
import gdsfactory as gf
from gdsfactory.pdk import Pdk
from gdsfactory.get_factories import get_cells

from sky130.tech import cross_sections
from sky130 import components

__version__ = "0.0.3"

cells = get_cells(components)
PDK = Pdk(name="sky130", cells=cells, cross_sections=cross_sections)
gf.set_active_pdk(PDK)

__all__ = ["cells", "PDK"]
