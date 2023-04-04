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
        p = parameters(period).gov.states.mn.tax.income.deductions

        fed_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)

        # reduced deductions for households with income over a
        # threshold
        reduced_deductions = [
            "mn_other_itemized_deductions",
            "interest_expense",
            "mn_charitable_donation_deduction",
        ]

        # deductions only available for households under the income
        # threshold
        other_deductions = [
            "mn_medical_dental_deduction",
            "mn_casualty_theft_deduction",
        ]

        deduction_amount = add(tax_unit, period, reduced_deductions)
        all_deductions = deduction_amount + add(
            tax_unit, period, other_deductions
        )

        return where(
            fed_agi <= p.itemized_threshold[filing_status],
            all_deductions,
            min_(
                deduction_amount * p.itemized_mult,
                (fed_agi - p.itemized_threshold[filing_status])
                * p.itemized_income_mult,
            ),
        )
