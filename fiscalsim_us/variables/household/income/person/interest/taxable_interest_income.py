from policyengine_us.model_api import *


class taxable_interest_income(Variable):
    value_type = float
    entity = Person
    label = "Taxable interest income"
    unit = USD
    definition_period = YEAR
