from fiscalsim_us.model_api import *


class mi_farmland_preservation_tax_credit(Variable):
    """
    Line 26 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI Farmland Preservation Tax Credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI