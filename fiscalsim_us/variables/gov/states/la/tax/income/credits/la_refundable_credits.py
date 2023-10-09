from fiscalsim_us.model_api import *


class la_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana refundable income tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )

    def formula(tax_unit, period, parameters):
        priority_2_refund = tax_unit(
            "la_refundable_priority_2_credits", period
        )

        # line 18 - floor at 0 since the priority 3 credits are nonrefundable
        tax_afer_p_2_credits = max_(
            0,
            tax_unit("la_income_tax_before_refundable_credits", period)
            - priority_2_refund,
        )

        priority_3_nonrefund_amount = tax_unit(
            "la_nonrefundable_priority_3_credits", period
        )

        # either refund the rest of the tax liability (leftover from p2)
        # or refund the total amount of p3 credits, whichever is less
        priority_3_nonrefund_add = min_(
            tax_afer_p_2_credits, priority_3_nonrefund_amount
        )

        priority_4_refund = tax_unit(
            "la_refundable_priority_4_credits", period
        )

        return priority_2_refund + priority_3_nonrefund_add + priority_4_refund
