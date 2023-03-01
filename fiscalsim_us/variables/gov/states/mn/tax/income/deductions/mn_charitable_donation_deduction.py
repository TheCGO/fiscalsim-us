from fiscalsim_us.model_api import *


class mn_charitable_donation_deduction(Variable):
    """
    Minnesota charitable donation deduction
    Line 4 of 2022 M1SA, Minnesota Itemized Deductions
    """
    value_type = float
    entity = TaxUnit
    label = "MN charitable donation deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
 
    def formula(tax_unit, period, parameters):
        cash_donations = tax_unit("charitable_cash_donations", period)
        non_cash_donations = tax_unit("charitable_non_cash_donations", period)
        fed_agi = tax_unit("adjusted_gross_income", period)
        mult = (
            period
        ).gov.states.mn.tax.income.deductions.charitable_donation_limit

        return min(mult * fed_agi, cash_donations + non_cash_donations)
