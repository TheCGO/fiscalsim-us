from fiscalsim_us.model_api import *


class va_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA taxable income line 15 on form 760"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        line_14 = tax_unit("va_calc_line_14", period)

        line_9 = tax_unit("va_adj_gross_income", period)

        subtotal = line_9 - line_14

        return subtotal
