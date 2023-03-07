from fiscalsim_us.model_api import *


class mn_itemized_deductions(Variable):
    """
    Line 4 of Minnesota 2022 Individual Income Tax return from M1.
    """
    value_type = float
    entity = TaxUnit
    label = "MN itemized deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN


    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.mn.tax.income.deductions
 
        fed_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)
        deductions = [
            "mn_other_itemized_deductions",
            "mn_medical_dental_deduction",
            "interest_expense",
            "mn_charitable_donation_deduction",
            "mn_casualty_theft_deduction"
            ]

        if fed_agi <= p.itemized_threshold[filing_status]:
            return add(tax_unit, period, deductions)

        reduced_deductions = [
            "mn_other_itemized_deductions",
            "interest_expense",
            "mn_charitable_donation_deduction"
            ]
        
        deduction_amount = add(tax_unit, period, reduced_deductions)
        return min(
            deduction_amount * p.itemized_mult,
            (fed_agi - p.itemized_threshold) * p.itemized_income_mult
        )
