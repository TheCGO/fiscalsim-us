from fiscalsim_us.model_api import *


class mt_charitable_noncash_deduction(Variable):
    """
    Line 12 on Montana itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana charitable non-cash donation deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        noncash_donations = tax_unit(period, ["charitable_non_cash_donations"])

        return noncash_donations
