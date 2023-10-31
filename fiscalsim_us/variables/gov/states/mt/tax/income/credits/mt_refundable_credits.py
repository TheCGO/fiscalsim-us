from fiscalsim_us.model_api import *


class mt_refundable_credits(Variable):
    """
    Line 22 on Montana individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
