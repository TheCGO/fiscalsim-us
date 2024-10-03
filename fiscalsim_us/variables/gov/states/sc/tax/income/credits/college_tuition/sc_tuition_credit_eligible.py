from fiscalsim_us.model_api import *


class sc_tuition_credit_eligible(Variable):
    """
    Tuition tax credit, eligibility, refundable credit, line 21 on SC1040 2023
    Invidual Income Tax Return (see form I-319)
    """

    value_type = bool
    entity = Person
    label = "Eligible for the South Carolina Tuition Credit"
    definition_period = YEAR
    reference = (
        "https://dor.sc.gov/forms-site/Forms/I319_2023.pdf",
        "https://dor.sc.gov/forms-site/Forms/I319_2021.pdf#page=2",
        "https://www.scstatehouse.gov/code/t12c006.php",
        # South Carolina Legal Code | SECTION 12-6-3385 (B)(3)(b)
    )
    defined_for = StateCode.SC
