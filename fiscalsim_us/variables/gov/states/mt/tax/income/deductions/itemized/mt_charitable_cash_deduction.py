from fiscalsim_us.model_api import *


class mt_charitable_cash_deduction(Variable):
    """
    Line 11 on Montana itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana charitable cash donation deduction"
    unit = USD
    documentation = (
        "Montana deduction from taxable income for charitable cash donations."
    )
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        cash_donations = add(tax_unit, period, ["charitable_cash_donations"])

        return cash_donations
