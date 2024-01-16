from fiscalsim_us.model_api import *


class mt_political_contributions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Montana political contributions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
