from fiscalsim_us.model_api import *

class alt_energy_device_2021(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Idaho Qualifying Alternative Energy Device 2021"
    documentation = "Idaho qualifying alternative energy device 2021"
    definition_period = YEAR