from fiscalsim_us.model_api import *


class deaf_spouse(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Tax unit spouse is blind"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        deaf = person("is_deaf", period)
        spouse = person("is_tax_unit_spouse", period)
        return tax_unit.any(deaf & spouse)
