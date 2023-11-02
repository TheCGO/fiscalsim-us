from fiscalsim_us.model_api import *


class mt_nonrefundable_credits(Variable):
    """
    Line 19 of Montana state individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    adds = "gov.states.mt.tax.income.credits.non_refundable"
