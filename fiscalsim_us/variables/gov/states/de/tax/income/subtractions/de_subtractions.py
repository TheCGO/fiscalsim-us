from fiscalsim_us.model_api import *


class de_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Delaware subtractions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.DE
