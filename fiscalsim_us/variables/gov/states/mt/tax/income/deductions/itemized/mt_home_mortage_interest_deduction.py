from fiscalsim_us.model_api import *


class mt_home_mortage_interest_deduction(Variable):
    """
    Line 9 on itemized deductions schedule
    Home mortgage interst and points
    """

    value_type = float
    entity = TaxUnit
    label = "Montana home mortage interest deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
