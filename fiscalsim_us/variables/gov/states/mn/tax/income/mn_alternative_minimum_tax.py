from fiscalsim_us.model_api import *


class mn_alternative_minimum_tax(Variable):
    """
    TODO: SOMETHING HERE
    """
    value_type = float
    entity = TaxUnit
    label = "MN alternative minimum tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):

        return 0
