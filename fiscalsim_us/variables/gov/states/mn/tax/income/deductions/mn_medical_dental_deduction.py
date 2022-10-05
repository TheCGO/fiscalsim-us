from more_itertools import value_chain
from fiscalsim_us.model_api import *


class mn_medical_dental_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN medical and dental itemized deduction"
    unit = USD 
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        medical_dental_expense = tax_unit("medical_expense_deduction", period)
        agi = tax_unit("adjusted_gross_income", period)
        mult = parameters(period).gov.states.mn.tax.income.deductions.mn_medical_deduction_mult

        return max(0, medical_dental_expense - agi * mult)