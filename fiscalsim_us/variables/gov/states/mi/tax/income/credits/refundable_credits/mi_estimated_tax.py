from fiscalsim_us.model_api import *


class mi_estimated_tax(Variable):
    """
    Line 31 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI Estimated Tax, Extension Payments, and Credit Forward"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI