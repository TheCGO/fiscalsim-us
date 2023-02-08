from fiscalsim_us.model_api import *


class ks_adjusted_gross_income(Variable):
    """
    Line 3 on Kansas 2022 Individual Income Tax return form TC-40.
    """
    value_type = float
    entity = TaxUnit
    label = "KS adjusted gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    adds = ["adjusted_gross_income", "ks_modifications"]
