from fiscalsim_us.model_api import *


class prior_year_state_income_tax_paid(Variable):
    value_type = float
    entity = Person
    label = "Prior year state income taxes paid"
    unit = USD
    definition_period = YEAR
