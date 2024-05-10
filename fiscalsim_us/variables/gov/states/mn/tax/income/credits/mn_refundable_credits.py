from fiscalsim_us.model_api import *


class mn_refundable_credits(Variable):
    """
    Line 22 of form M1 (2023) is the sum of refundable credits. These are
    listed and calculated on form M1REF (2023).
    """

    value_type = float
    entity = TaxUnit
    label = "Minnesota refundable income tax credits"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1ref_21.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1ref_22.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2024-04/m1ref-23.pdf"
    )
    defined_for = StateCode.MN
    adds = "gov.states.mn.tax.income.credits.refundable"
