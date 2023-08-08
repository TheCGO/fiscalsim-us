from fiscalsim_us.model_api import *


class state_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "state income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    adds = [
        "ia_income_tax_before_refundable_credits",
        "il_total_tax",
        "ks_income_tax_before_refundable_credits",
        "ma_income_tax_before_refundable_credits",
        "md_income_tax_before_refundable_credits",
        "mn_income_tax_before_refundable_credits",
        "mo_income_tax_before_refundable_credits",
        "nd_income_tax_before_refundable_credits",
        "ne_income_tax_before_refundable_credits",
        "ny_income_tax_before_refundable_credits",
        "or_income_tax_before_refundable_credits",
        "pa_income_tax",  # PA has no refundable credits.
        "ut_income_tax_before_refundable_credits",
        "wa_income_tax_before_refundable_credits",
    ]
