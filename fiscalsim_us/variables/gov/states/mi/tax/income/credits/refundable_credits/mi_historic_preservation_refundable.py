from fiscalsim_us.model_api import *


class mi_historic_preservation_refundable(Variable):
    """
    Line 28 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI Historic Preservation Tax Credit Refundable"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI
