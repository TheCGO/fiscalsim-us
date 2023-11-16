from fiscalsim_us.model_api import *


class mt_gambling_loss_deduction(Variable):
    """
    Line 17 on itemized deductions schedule
    Limited to what it allowed under federal law
    """

    value_type = float
    entity = TaxUnit
    label = "Montana gambling loss deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
