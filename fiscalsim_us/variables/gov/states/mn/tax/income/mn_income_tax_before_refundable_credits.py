from fiscalsim_us.model_api import *


class mn_income_tax_before_refundable_credits(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        income_tax_before_credits = tax_unit(
            "mn_income_tax_before_credits", period
        )

        nonrefundable_credits = tax_unit(
            "mn_nonrefundable_credits", period
        )

        return max_(income_tax_before_credits - nonrefundable_credits, 0)
