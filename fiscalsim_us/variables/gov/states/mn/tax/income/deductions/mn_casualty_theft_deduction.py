from fiscalsim_us.model_api import *


class mn_casualty_theft_deduction(Variable):
    """
    Minnesota casulaty/ theft deduction
    Line 19 of 2022 M1SA, Minnesota Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "MN charitable donation deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.deductions
        fed_agi = tax_unit("adjusted_gross_income", period)
        loss = add(tax_unit, period, ["casualty_loss"])

        adj_loss = max_(0, loss - p.theft_deduction_floor)

        return max_(0, adj_loss - fed_agi * p.theft_deduction_income_mult)
