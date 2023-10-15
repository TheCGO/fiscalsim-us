from fiscalsim_us.model_api import *


class ky_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Kentucky adjusted gross income"
    unit = USD
    definition_period = YEAR
    reference = "https://revenue.ky.gov/Forms/740%20Packet%20Instructions%205-9-23.pdf#page=11"
    defined_for = StateCode.KY
