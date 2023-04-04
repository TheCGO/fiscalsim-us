from fiscalsim_us.model_api import *


class mn_unreimbursed_employee_deduction(Variable):
    """
    Line 23 of 2022 M1SA, Minnesota Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "MN unreimbursed employee expenses deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        fed_agi = tax_unit("adjusted_gross_income", period)
        mult = parameters(
            period
        ).gov.states.mn.tax.income.deductions.unreimbursed_employee_mult
        expense = tax_unit("mn_unreimbursed_employee_expenses", period)

        return max_(expense - fed_agi * mult, 0)
