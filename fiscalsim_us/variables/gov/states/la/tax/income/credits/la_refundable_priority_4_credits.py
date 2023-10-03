from fiscalsim_us.model_api import *


class la_refundable_priority_4_credits(Variable):
    """
    louisiana refundable priority 4 credits
    Line 25 on Form IT-540. These credits include the
    following with codes:
    * 50F - Inventory Tax
    * 51F - Ad Valorem Natural Gas
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana refundable priority 4 income tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
