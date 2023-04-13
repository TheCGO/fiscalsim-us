from fiscalsim_us.model_api import *


class mn_other_business_additions_to_income(Variable):
    """

    """

    value_type = float
    entity = TaxUnit
    label = "MN other business additions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
