from fiscalsim_us.model_api import *


class urgent_care_expense(Variable):
    value_type = float
    entity = Person
    label = "Urgent care expenses"
    unit = USD
    definition_period = YEAR
