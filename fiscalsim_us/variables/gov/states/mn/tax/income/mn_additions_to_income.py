from policyengine_us.model_api import *


class mn_additions_to_income(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN additions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):

        return 0
