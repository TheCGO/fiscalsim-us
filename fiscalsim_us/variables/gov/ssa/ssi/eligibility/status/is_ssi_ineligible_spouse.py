from fiscalsim_us.model_api import *


class is_ssi_ineligible_spouse(Variable):
    value_type = bool
    entity = Person
    label = "Is an SSI-ineligible spouse"
    unit = USD
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/42/1382c#b"

    def formula(person, period, parameters):
        spouse = person("is_tax_unit_spouse", period)
        return spouse & ~person("is_ssi_eligible_spouse", period)
