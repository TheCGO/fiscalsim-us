from fiscalsim_us.model_api import *


class mi_total_agi(Variable):
    """
    Line 12 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MT total gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI

    adds = ["adjusted_gross_income", "mi_additions"]
