from fiscalsim_us.model_api import *


class mi_use_tax(Variable):
    """
    Line 23 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI use tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI