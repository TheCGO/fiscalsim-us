from fiscalsim_us.model_api import *


class va_calc_line_8(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA interim step to get to total virginia agi, line 8 on form 760"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        age_deduction = tax_unit("va_age_deduction", period)

        subtractions_to_federal_agi = tax_unit(
            "va_subtractions_to_federal_agi", period
        )

        return age_deduction + subtractions_to_federal_agi
