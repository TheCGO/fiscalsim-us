from fiscalsim_us.model_api import *


class md_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD refundable credits"
    documentation = "Maryland refundable tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MD

    adds = "gov.states.md.tax.income.credits.refundable"
