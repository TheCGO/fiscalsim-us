from fiscalsim_us.model_api import *


class mn_medical_dental_deduction(Variable):
    """
    Minnesota medical and dental expense deduction
    Line 4 of 2022 M1SA, Minnesota Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "MN medical and dental deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        expense = add(tax_unit, period, ["medical_expense"])
        fed_agi = tax_unit("adjusted_gross_income", period)
        mult = parameters(
            period
        ).gov.states.mn.tax.income.deductions.medical_and_dental_mult

        return max_(0, expense - mult * fed_agi)
