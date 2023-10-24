from fiscalsim_us.model_api import *


class ct_non_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Connecticut non-refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.CT
