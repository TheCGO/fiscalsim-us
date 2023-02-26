from fiscalsim_us.model_api import *


class mn_other_itemized_deductions(Variable):
    """
    ADD A LIST OF NON IMPLEMENTED ITEMIZED DEDUCTIONS HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN other itemized deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
