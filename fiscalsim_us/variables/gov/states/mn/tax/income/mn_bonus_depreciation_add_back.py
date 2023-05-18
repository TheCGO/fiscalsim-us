from fiscalsim_us.model_api import *


class mn_bonus_depreciation_add_back(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN bonus depreciation add back"
    definition_period = YEAR
    documentation = "Income (or loss) included in Federal AGI under Section 168(k)'s bonus depreciation less the amount that would have been included without it."
    defined_for = StateCode.MN
    # use federal variables if they are added later
