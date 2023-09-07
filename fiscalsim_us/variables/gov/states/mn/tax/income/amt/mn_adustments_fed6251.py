from fiscalsim_us.model_api import *


class mn_adjustmnets_fed6251(Variable):
    """
    Adjustements and preferences to income for alternative
    minimum tax on federal Form 6251
    Line 2 Minnesota 2022 form M1MT, Alternative Minimum Tax
    """

    value_type = float
    entity = TaxUnit
    label = "MN income adjustements fed Form 6251"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
