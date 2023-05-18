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
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2021-12/m1_21_0.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1_inst_21.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2022-12/m1_22.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-03/m1_inst_22.pdf"
    )

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.deductions

        fed_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)

        # reduced deductions for households with income over a
        # threshold (deductions allowed for everyone)
        reduced_deductions = [
            "mn_other_itemized_deductions",
            "mn_charitable_donation_deduction",
            "mn_home_mortgage_interest_deduction",
            "mn_unreimbursed_employee_deduction",
            "mn_gambling_loss_deduction",
            "mn_disabled_impairment_work_deduction",
        ]

        # deductions only available for households under the income
        # threshold
        other_deductions = [
            "mn_medical_dental_deduction",
            "mn_casualty_theft_deduction",
            "interest_deduction",
        ]

        deduction_amount = add(tax_unit, period, reduced_deductions)
        all_deductions = deduction_amount + add(
            tax_unit, period, other_deductions
        )

        return where(
            fed_agi <= p.itemized_threshold[filing_status],
            all_deductions,
            deduction_amount - min_(
                deduction_amount * p.itemized_mult,
                (fed_agi - p.itemized_threshold[filing_status])
                * p.itemized_income_mult,
            ),
        )
