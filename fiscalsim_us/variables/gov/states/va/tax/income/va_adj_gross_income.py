from fiscalsim_us.model_api import *


class va_adj_gross_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Line 9 on form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit,period,parameters):
        line3 = tax_unit("calc_line_8",period)

        line8 = tax_unit("calc_line_3",period)

        filing_status = tax_unit("filing_status", period)


        subtotal = line3 - line8 

        if filing_status == 1 or filing_status == 3:

            if subtotal < 11950 :
                
                tax_owed = 0 
                
                return tax_owed

        if filing_status == 2: 

            if subtotal < 23900: 

                tax_owed = 0 

                return tax_owed

        
        va_adj_gross_income = subtotal

        return va_adj_gross_income

    