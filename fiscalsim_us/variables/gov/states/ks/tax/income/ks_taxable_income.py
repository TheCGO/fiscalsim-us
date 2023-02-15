from fiscalsim_us.model_api import *


class ks_taxable_income(Variable):
    """
    Line 7 on Kansas 2022 Individual Income Tax return form TC-40.
    """

    value_type = float
    entity = TaxUnit
    label = "KS adjusted gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    max("ks_adjusted_gross_income" - "ks_total_deductions", 0)
