from fiscalsim_us.model_api import *


class va_net_amount_of_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "va net amount of tax line 18 form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit,period,parameters):


        taxable_inc = tax_unit("va_taxable_inc",period)

        if taxable_inc > 0: 

            if taxable_inc < 3000: 

                net_tax = taxable_inc * .02

            if taxable_inc > 3000 and taxable_inc < 5000: 

                excess_taxable = taxable_inc - 3000 

                net_tax = (excess_taxable * .03) + 60 
            
            if taxable_inc > 5000 and taxable_inc < 17000:

                excess_taxable = taxable_inc - 5000 

                net_tax = (excess_taxable * .05) + 120 

            if taxable_inc > 17000: 

                excess_taxable = taxable_inc - 17000 

                net_tax = (excess_taxable * .0575) + 720

            
        else: 

            net_tax = 0

        
        return net_tax


        
