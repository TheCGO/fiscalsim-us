from fiscalsim_us.model_api import *


class is_young_adult_for_medicaid_nfc(Variable):
    value_type = bool
    entity = Person
    label = "Medicaid young adult non-financial criteria"
    definition_period = YEAR

    def formula(person, period, parameters):
        ma = parameters(
            period
        ).gov.hhs.medicaid.eligibility.categories.young_adult
        age = person("age", period)
        return ma.age_range.calc(age)
