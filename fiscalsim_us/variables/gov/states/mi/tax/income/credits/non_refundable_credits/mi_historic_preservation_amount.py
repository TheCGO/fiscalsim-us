from fiscalsim_us.model_api import *


class mi_historic_preservation_amount(Variable):
    """
    Line 19a on Michigan 2022 Individual Income Tax return form MI-1040. 
    If you are including Form 3581, enter the amount
    from line 9. If you are including Form 5803, enter the amount from line 7.
    """

    value_type = float
    entity = TaxUnit
    label = "MI amount of Historic Preservation Tax Credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI