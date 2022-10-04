from fiscalsim_us.model_api import *


class va_calc_line_3(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA interim step to get to total virginia agi"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA


    def formula(tax_unit,period,parameters):

        federal_agi = tax_unit("adjusted_gross_income", period)

        additions_to_federal_agi = ? 




        return federal_agi + additions_to_federal_agi 