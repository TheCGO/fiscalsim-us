from fiscalsim_us.model_api import *


class ks_income_tax(Variable):
    """
    Line 19 minus lines 23 and 24 of KS 2022 Individual Income Tax return form K-40.
    """
    value_type = float
    entity = TaxUnit
    label = "KS income tax after refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    adds = ["ks_income_tax_before_refundable_credits"]
    subtracts = ["ks_refundable_credits"]
