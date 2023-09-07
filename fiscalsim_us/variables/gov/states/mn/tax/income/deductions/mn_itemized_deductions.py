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

        # deductions that are limited to 20% of the deduction over the
        # income threshold
        limited_deductions = [
            "mn_taxes_paid_deducion",
            "charitable_deduction",
            "mn_unreimbursed_employee_deduction",
            "mn_gambling_loss_deduction",
            "mn_disabled_impairment_work_deduction",
            "mn_home_mortgage_interest_deduction",
            "mn_other_itemized_deductions",
        ]

        # deductions that aren't limited over the income threshold
        # (they don't get phased out)
        non_limited_deductions = [
            "mn_medical_dental_deduction",
            "interest_deduction",
            "mn_casualty_theft_deduction",
        ]

        limited_amount = add(tax_unit, period, limited_deductions)
        all_deductions = limited_amount + add(
            tax_unit, period, non_limited_deductions
        )

        return where(
            fed_agi <= p.itemized_threshold[filing_status],
            all_deductions,
            all_deductions
            - min_(
                limited_amount * p.itemized_mult,
                (fed_agi - p.itemized_threshold[filing_status])
                * p.itemized_income_mult,
            ),
        )
