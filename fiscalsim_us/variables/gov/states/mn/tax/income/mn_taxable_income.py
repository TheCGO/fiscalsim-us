from policyengine_us.model_api import *


class mn_taxable_income(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN taxable income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
    def formula(tax_unit, period, parameters):
        federal_agi = 0 # something here! 

        additions = tax_unit(
            "mn_additions_to_income", period
        )

        subtractions = tax_unit(
            "mn_subtractions_from_income", period
        )

        return federal_agi + additions - subtractions
