from fiscalsim_us.model_api import *


class mn_business_additions_to_income(Variable):
    """
    TODO: SOMETHING HERE
    """

    value_type = float
    entity = TaxUnit
    label = "MN business additions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    adds = ["mn_bonus_depreciation_add_back", "mn_other_business_additions_to_income"]
