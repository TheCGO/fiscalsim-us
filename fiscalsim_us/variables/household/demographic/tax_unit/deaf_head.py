from fiscalsim_us.model_api import *


class deaf_head(Variable):
    value_type = bool
    entity = TaxUnit
    definition_period = YEAR
    label = "Tax unit head is deaf"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        deaf = person("is_deaf", period)
        head = person("is_tax_unit_head", period)
        return tax_unit.any(deaf & head)
