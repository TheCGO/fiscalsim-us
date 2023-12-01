from fiscalsim_us.model_api import *


class ga_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.GA
    adds = ["ga_income_tax_before_credits"]
    subtracts = ["ga_nonrefundable_credits"]

    def formula(tax_unit, period, parameters):
        tax_before_credits = tax_unit("ga_income_tax_before_credits", period)
        nonrefundables = tax_unit("ga_nonrefundable_credits", period)

        return max_(0, tax_before_credits - nonrefundables)
