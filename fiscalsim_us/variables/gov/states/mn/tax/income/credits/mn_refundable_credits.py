from fiscalsim_us.model_api import *


class mn_refundable_credits(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):

        return 0
