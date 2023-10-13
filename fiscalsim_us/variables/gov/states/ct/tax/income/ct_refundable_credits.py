from fiscalsim_us.model_api import *


class ct_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Connecticut refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.CT
