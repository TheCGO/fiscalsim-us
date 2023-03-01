from fiscalsim_us.model_api import *


class mn_refundable_credits(Variable):
    """
    Line 22 on Minnesota 2022 Indivual Tax Return from M1. 
    These cretis include the following categories and are listed on 
    https://www.revenue.state.mn.us/sites/default/files/2022-12/m1ref_22.pdf
    * Child and Dependent Care Credit
    * Minnesota Working Family Credit
    * K-12 Education Credit
    * Credit for Parents of Stillborn Children
    * Refundable credit for taxes paid to Wisconsin
    * Credit for Historic Structure Rehabilitation
    * Enterprise Zone Credit
    * Angel Investment Credit
    * Pass Through Entity Credit
    * Claim of right
    """
    value_type = float
    entity = TaxUnit
    label = "MN refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
