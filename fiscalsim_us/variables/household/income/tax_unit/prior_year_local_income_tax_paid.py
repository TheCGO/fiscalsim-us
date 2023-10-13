from fiscalsim_us.model_api import *


class prior_year_local_income_tax_paid(Variable):
    value_type = float
    entity = Person
    label = "Prior year local income taxes paid"
    unit = USD
    definition_period = YEAR
