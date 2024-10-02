from fiscalsim_us.model_api import *


class sc_parentrefund_credit(Variable):
    """
    Parental refund credit, refundable credit, line 22d on SC1040 2023
    Invidual Income Tax Return (see form I-361)
    """

    value_type = float
    entity = Person
    label = "South Carolina Parent Refund Credit"
    defined_for = "sc_tuition_credit_eligible"
    unit = USD
    definition_period = YEAR
    reference = ("https://dor.sc.gov/forms-site/Forms/I361_2023.pdf",)
