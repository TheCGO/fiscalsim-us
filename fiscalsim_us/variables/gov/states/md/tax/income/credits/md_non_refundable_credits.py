from fiscalsim_us.model_api import *


class md_non_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD non-refundable credits"
    documentation = "Maryland non-refundable tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MD

    adds = "gov.states.md.tax.income.credits.non_refundable"
