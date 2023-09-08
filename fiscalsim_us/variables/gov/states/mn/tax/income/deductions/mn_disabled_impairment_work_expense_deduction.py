from fiscalsim_us.model_api import *


class mn_disabled_impairment_work_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN impairment-related work expenses for disabled person"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
