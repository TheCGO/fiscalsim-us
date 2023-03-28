from fiscalsim_us.model_api import *


class ks_nonrefundable_credits(Variable):
    """
    Sum of lines 13 through 18 on Kansas 2022 Individual Income Tax return form K-40.
    https://www.ksrevenue.gov/pdf/k-4022.pdf

    """

    value_type = float
    entity = TaxUnit
    label = "KS nonrefundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

adds = ["ks_eitc"]

# TODO: Add credits for:
# * Line 17: Kansas earned income credit
# * Line 14: Kansas child and dependent care credit
# * Line 18: Food Sales Tax Credit
# * Lines 13 & 15: Other credits
