from fiscalsim_us.model_api import *


class mt_long_term_care_premiums_deduction(Variable):
    """
    Line 3 on itemized deductions schedule
    Long-term core insurance premiums not deducted elsewhere on your return
    """

    value_type = float
    entity = TaxUnit
    label = "Montana long-term care insurance premiums deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
