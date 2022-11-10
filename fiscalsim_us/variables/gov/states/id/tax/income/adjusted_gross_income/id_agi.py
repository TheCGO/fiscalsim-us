from fiscalsim_us.model_api import *


class id_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "ID adjusted gross income"
    unit = USD
    definition_period = YEAR
    reference = ""
    defined_for = StateCode.ID

    def formula(tax_unit, period, parameters):
        federal_agi = tax_unit("adjusted_gross_income", period)
        id_agi_subtractions = tax_unit("id_agi_subtractions", period)
        id_agi_additions = tax_unit("id_agi_additions", period)
        total_agi = federal_agi - id_agi_subtractions + id_agi_additions
        return total_agi
