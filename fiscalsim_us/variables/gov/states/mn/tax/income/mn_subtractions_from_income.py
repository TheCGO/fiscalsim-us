from policyengine_us.model_api import *


class mn_subtractions_from_income(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN subtrations from income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):

        return 0
