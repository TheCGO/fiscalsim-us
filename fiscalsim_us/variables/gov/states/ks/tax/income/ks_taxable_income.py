from openfisca_us.model_api import *


class ks_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS taxable income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://www.ksrevenue.gov/pdf/k-4021.pdf"

    def formula(tax_unit, period, parameters):
        ks_total_deductions = tax_unit("ks_total_deductions", period)
        ks_agi = tax_unit("ks_agi", period)

        return max(ks_agi - ks_total_deductions, 0)
