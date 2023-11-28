from fiscalsim_us.model_api import *


class mi_historic_preservation_credit(Variable):
    """
    Line 19b on Michigan 2022 Individual Income Tax return form MI-1040.
    If you are including Form 3581, enter the amount
    from line 14. If you are including Form 5803, enter the amount from line 12.
    """

    value_type = float
    entity = TaxUnit
    label = "MI Credit of Historic Preservation Tax Credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI
