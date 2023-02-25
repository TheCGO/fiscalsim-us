from fiscalsim_us.model_api import *


class mn_income_tax_before_credits(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN income tax before credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        
        taxable_income = tax_unit(
            "mn_taxable_income", period
        )

        tax = 0
        # other tax logic/ table lookup here
        amt = tax_unit(
            "mn_alternative_minimum_tax", period
        )


        return 0
