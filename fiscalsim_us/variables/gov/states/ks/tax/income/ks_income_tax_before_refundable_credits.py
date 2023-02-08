from fiscalsim_us.model_api import *


class ks_income_tax_before_refundable_credits(Variable):
    """
    Line 19 of Kansas 2022 Individual Income Tax return form K-40.
    """
    value_type = float
    entity = TaxUnit
    label = "KS income tax before refundable credits"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        income_tax_before_credits = tax_unit(
            "ks_income_tax_before_credits", period
        )
        credits = tax_unit(
            "ks_nonrefundable_credits", period
        )

        return max(income_tax_before_credits - credits, 0)
