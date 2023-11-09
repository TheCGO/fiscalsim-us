from fiscalsim_us.model_api import *


class ar_other_limited_expenses(Variable):
    """
    Line 21 of 2022 AR3, Arkansas Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "AR other limited expenses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR