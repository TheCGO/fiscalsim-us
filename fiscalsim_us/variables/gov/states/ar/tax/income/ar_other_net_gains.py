from fiscalsim_us.model_api import *


class ar_other_net_gain(Variable):
    value_type = float
    entity = TaxUnit
    label = "Other net gains"
    unit = USD
    documentation = "Other net gain/loss from Federal Form 4797"
    definition_period = YEAR