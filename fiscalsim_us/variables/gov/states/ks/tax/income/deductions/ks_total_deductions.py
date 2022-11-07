from fiscalsim_us.model_api import *


class ks_total_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS total deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://www.ksrevenue.gov/pdf/k-4021.pdf"

    def formula(tax_unit, period, parameters):
        ks_exemption_allowance = tax_unit("ks_exemption_allowance", period)
        ks_deductions = max(
            tax_unit("ks_itemized_deductions", period),
            tax_unit("ks_standard_deduction", period),
        )
        

        return ks_exemption_allowance + ks_deductions