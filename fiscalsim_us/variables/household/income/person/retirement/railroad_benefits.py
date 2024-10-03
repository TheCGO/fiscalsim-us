from fiscalsim_us.model_api import *


class railroad_benefits(Variable):
    value_type = float
    entity = Person
    label = "Receives any railroad benefits"
    definition_period = YEAR
    default_value = 0
