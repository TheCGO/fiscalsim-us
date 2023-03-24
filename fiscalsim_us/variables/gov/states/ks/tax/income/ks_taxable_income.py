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

    def formula(tax_unit, period, parameters):
        ks_agi = tax_unit("ks_adjusted_gross_income", period)
        ks_total_deductions = tax_unit("ks_total_deductions", period)
        return max_(ks_agi - ks_total_deductions, 0)
