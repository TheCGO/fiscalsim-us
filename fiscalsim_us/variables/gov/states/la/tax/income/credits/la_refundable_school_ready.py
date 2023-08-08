from fiscalsim_us.model_api import *


class la_refundable_school_ready(Variable):
    """
    louisiana refundable school readiness credit
    Line 14 on Form IT-540.
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
