from fiscalsim_us.model_api import *


class mn_other_refundable_credits(Variable):
    """
    Other refundable credits that haven't been implemented in other vars.
    Other refundable credits from Line 22 on Minnesota 2022

    * K-12 Education Credit
    * Credit for Parents of Stillborn Children
    * Refundable credit for taxes paid to Wisconsin
    * Credit for Historic Structure Rehabilitation
    * Enterprise Zone Credit
    * Angel Investment Credit
    * Pass Through Entity Credit
    * Claim of right

    If another variable gets added, remove from the list.
    """

    value_type = float
    entity = TaxUnit
    label = "Minnesota other refundable income tax credits"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1c_21.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1c_22.pdf"
    )
    defined_for = StateCode.MN
