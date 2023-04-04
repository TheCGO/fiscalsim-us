from fiscalsim_us.model_api import *


class mn_depletion(Variable):
    """
    Line 7 Minnesota 2022 form M1MT, Alternative Minimum Tax
    """

    value_type = float
    entity = TaxUnit
    label = "MN depletion"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
