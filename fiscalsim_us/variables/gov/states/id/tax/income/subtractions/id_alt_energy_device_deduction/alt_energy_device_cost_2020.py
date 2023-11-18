from fiscalsim_us.model_api import *

class alt_energy_device_cost_2020(Variable):
    value_type = float
    entity = TaxUnit
    label = "Idaho Qualifying Alternative Energy Device Cost 2020"
    documentation = "Cost of Idaho qualifying alternative energy device 2020"
    definition_period = YEAR