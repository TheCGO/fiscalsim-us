from fiscalsim_us.model_api import *


class mt_charitable_carryover_deduction(Variable):
    """
    Line 13 on Montana itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = (
        "Montana charitable carryover donation from previous year deduction"
    )
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
