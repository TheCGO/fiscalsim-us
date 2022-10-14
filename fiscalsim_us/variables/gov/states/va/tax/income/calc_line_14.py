from fiscalsim_us.model_api import *


class calc_line_14(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA interim step to get to total virginia taxable income, line 14 on form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit,period,parameters):

        line_11  = tax_unit("va_standard_deduction",period)

        line_12 = tax_unit("va_exemptions",period)

        subtotal = line_11 + line_12 

        return(subtotal)