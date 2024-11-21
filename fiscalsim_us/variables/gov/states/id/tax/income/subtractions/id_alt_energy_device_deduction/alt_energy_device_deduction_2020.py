from fiscalsim_us.model_api import *


class alt_energy_device_2020(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Idaho Qualifying Alternative Energy Device 2020"
    documentation = "Idaho qualifying alternative energy device 2020"
    definition_period = YEAR
