from fiscalsim_us.model_api import *


class mt_other_deduction(Variable):
    """
    Line 18 on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana other deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
