from fiscalsim_us.model_api import *


class mt_other_taxes_paid_deduction(Variable):
    """
    Line 8 on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana other deductible taxes paid"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
