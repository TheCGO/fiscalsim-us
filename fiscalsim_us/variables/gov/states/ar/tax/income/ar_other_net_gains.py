from fiscalsim_us.model_api import *


class ar_other_net_gains(Variable):
    value_type = float
    entity = Person
    label = "Other net gains"
    unit = USD
    documentation = "Other net gain/loss from Federal Form 4797"
    definition_period = YEAR
