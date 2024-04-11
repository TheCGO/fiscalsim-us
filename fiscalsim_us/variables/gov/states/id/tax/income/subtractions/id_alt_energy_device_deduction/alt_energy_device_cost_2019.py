from fiscalsim_us.model_api import *


class alt_energy_device_cost_2019(Variable):
    value_type = float
    entity = TaxUnit
    label = "Idaho Qualifying Alternative Energy Device Cost 2019"
    documentation = "Cost of Idaho qualifying alternative energy device 2019"
    definition_period = YEAR
