from fiscalsim_us.model_api import *


class mn_gambling_loss_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN gambling loss deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
