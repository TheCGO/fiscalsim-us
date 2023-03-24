from fiscalsim_us.model_api import *


class ks_refundable_credits(Variable):
    """
    Sum of lines 23 & 24 on Kansas 2022 Individual Income Tax return form K-40.
    * 23. Refundable portion of the earned income tax credit
    * 24. Refundable portion of tax credits

    """

    value_type = float
    entity = TaxUnit
    label = "KS refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
