from fiscalsim_us.model_api import *


class ar_income_tax(Variable):
    "Line 38 of Form AR 1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas income tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR

    adds = ["ar_income_tax_before_refundable_credits"]
    subtracts = ["ar_refundable_credits"]
