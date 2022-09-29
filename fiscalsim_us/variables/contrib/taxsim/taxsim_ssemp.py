from fiscalsim_us.model_api import *


class taxsim_ssemp(Variable):
    value_type = float
    entity = TaxUnit
    label = "Self-employment income of spouse (excluding QBI)"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        is_primary = person("is_tax_unit_spouse", period)
        semp = person("self_employment_income", period)
        return tax_unit.sum(semp * is_primary)
