from fiscalsim_us.model_api import *


class gi_cash_assistance(Variable):
    value_type = float
    entity = Person
    label = "guaranteed income / cash assistance income"
    unit = USD
    documentation = "Income from guaranteed income or cash assistance pilots"
    definition_period = YEAR
