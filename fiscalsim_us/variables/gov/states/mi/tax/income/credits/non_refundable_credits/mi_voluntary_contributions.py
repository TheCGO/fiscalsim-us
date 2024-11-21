from fiscalsim_us.model_api import *


class mi_voluntary_contributions(Variable):
    """
    Line 22 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI volentary contributions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI
