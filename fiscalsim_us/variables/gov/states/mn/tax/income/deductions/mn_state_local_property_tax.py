from fiscalsim_us.model_api import *


class mn_state_local_property_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN local and state property tax based on value"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
    # Note: this does not include registration tax for vehicles registered in MN