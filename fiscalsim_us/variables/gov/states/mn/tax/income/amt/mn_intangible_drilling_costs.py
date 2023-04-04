from fiscalsim_us.model_api import *


class mn_intangible_drilling_costs(Variable):
    """
    Line 6 Minnesota 2022 form M1MT, Alternative Minimum Tax
    """

    value_type = float
    entity = TaxUnit
    label = "MN intangible drilling costs"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
