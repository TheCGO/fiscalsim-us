from fiscalsim_us.model_api import *


class mi_withheld(Variable):
    """
    Line 30 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI tax withheld"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI