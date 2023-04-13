from fiscalsim_us.model_api import *


class is_on_tribal_land(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Is on tribal land"
