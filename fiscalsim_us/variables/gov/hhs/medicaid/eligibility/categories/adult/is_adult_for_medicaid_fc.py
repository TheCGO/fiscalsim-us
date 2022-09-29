from fiscalsim_us.model_api import *


class is_adult_for_medicaid_fc(Variable):
    value_type = bool
    entity = Person
    label = "Medicaid adult financial criteria"
    definition_period = YEAR

    def formula(person, period, parameters):
        ma = parameters(period).gov.hhs.medicaid.eligibility.categories.adult
        income = person("medicaid_income_level", period)
        state = person.household("state_code_str", period)
        income_limit = ma.income_limit[state]
        return income < income_limit
