from fiscalsim_us.model_api import *

class alt_energy_device_2019(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Idaho Qualifying Alternative Energy Device 2019"
    documentation = "Idaho qualifying alternative energy device 2019"
    definition_period = YEAR