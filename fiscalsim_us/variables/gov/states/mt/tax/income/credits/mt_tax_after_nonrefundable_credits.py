from fiscalsim_us.model_api import *


class mt_tax_after_nonrefundable_credits(Variable):
    """
    Line 20 on Montana individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameter):
        nonrefundable = tax_unit("mt_nonrefundable_credits")
        incometaxbeforecredits = tax_unit(
            "mt_income_tax_before_refundable_credits"
        )
        return incometaxbeforecredits - nonrefundable
