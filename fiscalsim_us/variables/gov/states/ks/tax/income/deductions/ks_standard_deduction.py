from fiscalsim_us.model_api import *


class ks_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS standard deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf#page=6"
    defined_for = StateCode.KS

# still needs to have the aged/blind standard deductions added

    def formula(tax_unit, period, parameters):
        standard_deduction = parameters(
            period
        ).gov.states.ks.tax.income.deductions
        filing_status = tax_unit("filing_status", period)
        return (
            standard_deduction.amount[filing_status],
        )
