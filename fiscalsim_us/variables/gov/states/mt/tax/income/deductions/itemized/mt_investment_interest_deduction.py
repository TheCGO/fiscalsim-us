from fiscalsim_us.model_api import *


class mt_investment_interest_deduction(Variable):
    """
    Line 10 on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana investment interest deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        contributions = tax_unit("investment_income_form_4952")

        return contributions
