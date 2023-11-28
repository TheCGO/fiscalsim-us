from fiscalsim_us.model_api import *


class mi_total_tax_liability(Variable):
    """
    Line 24 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MT total tax liability"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI

    adds = ["mi_income_tax", "mi_voluntary_contributions", "mi_use_tax"]
