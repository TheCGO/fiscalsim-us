from fiscalsim_us.model_api import *


class me_non_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Maine nonrefundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.ME

    adds = "gov.states.me.tax.income.credits.non_refundable"
