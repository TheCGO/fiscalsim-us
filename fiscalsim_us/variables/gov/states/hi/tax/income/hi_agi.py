from fiscalsim_us.model_api import *


class hi_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Hawaii adjusted gross income"
    defined_for = StateCode.HI
    unit = USD
    definition_period = YEAR
    # Hawaii Instructions for Form N-11 Rev 2022 (p4)
    reference = " https://files.hawaii.gov/tax/forms/2022/n11ins.pdf"
