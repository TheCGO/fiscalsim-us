from fiscalsim_us.model_api import *


class la_nonrefundable_credits(Variable):
    """
    Louisiana nonrefundable priority 1 credits
    Line 11 on Form IT-540. These credits include
    the following with codes:
    * 100 - Premium tax credit
    * 120 - Bone Marrow credit
    * 150 - Qualified Playgrounds
    * 155 - Debt Issuance
    * 199 - Other
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana nonrefundable credits"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
    defined_for = StateCode.LA
