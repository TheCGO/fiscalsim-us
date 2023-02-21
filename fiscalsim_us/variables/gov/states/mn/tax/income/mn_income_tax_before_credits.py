from policyengine_us.model_api import *


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
        
        return 0
