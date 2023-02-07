from fiscalsim_us.model_api import *


class mo_non_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Missouri non-refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MO
    adds = "gov.states.mo.tax.income.credits.non_refundable"
