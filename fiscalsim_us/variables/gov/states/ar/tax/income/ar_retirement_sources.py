from fiscalsim_us.model_api import *


class ar_retirement_sources(Variable):
    value_type = float
    entity = Person
    label = "Income from Qualified IRA distributions and Employer pensions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.CO

    adds = "gov.states.ar.tax.income.retirement_sources"
