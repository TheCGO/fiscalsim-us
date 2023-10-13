from fiscalsim_us.model_api import *


class ambulance_expense(Variable):
    value_type = float
    entity = Person
    label = "Ambulance expenses"
    unit = USD
    definition_period = YEAR
