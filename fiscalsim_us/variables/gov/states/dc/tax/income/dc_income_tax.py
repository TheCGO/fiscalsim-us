from fiscalsim_us.model_api import *


class dc_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "DC income tax"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/52926_D-40_12.21.21_Final_Rev011122.pdf#page=37"
        "https://otr.cfo.dc.gov/sites/default/files/dc/sites/otr/publication/attachments/2022_D-40_Booklet_Final_blk_01_23_23_Ordc.pdf#page=35"
    )
    defined_for = StateCode.DC
    adds = ["dc_income_tax_before_refundable_credits"]
    subtracts = ["dc_refundable_credits"]
