from fiscalsim_us.model_api import *


class mn_itemized_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN itemized deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        agi_mult = parameters(
            period
        ).gov.states.mn.tax.income.deductions.unreimbursed_employee_expenses_mult
        medical_deduct = tax_unit("mn_medical_dental_deduction", period)
        federal_agi = tax_unit("adjusted_gross_income", period)
        taxes_paid_deduct = tax_unit("mn_taxes_paid_deduction", period)
        # federal model doesn't use mortage interest or investment interest, leaving it out
        charitable = tax_unit("charitable_deduction", period)
        casualty_loss_deduct = tax_unit("casualty_loss", period)

        unreimb_employ_exp = tax_unit("mn_unreimbursed_employee_expenses", period)   
        unreimb_employ_deduc = max(0, federal_agi * agi_mult - unreimb_employ_exp)
        # not including form M1SA line 24 other miscellaneous deductions

        sub_total = medical_deduct + taxes_paid_deduct + charitable + casualty_loss_deduct \
            + unreimb_employ_deduc

        # more stuff here...
        return None
