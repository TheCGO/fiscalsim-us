from fiscalsim_us.model_api import *

class alt_energy_device_2022(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Idaho Qualifying Alternative Energy Device 2022"
    documentation = "Idaho qualifying alternative energy device 2022"
    definition_period = YEAR