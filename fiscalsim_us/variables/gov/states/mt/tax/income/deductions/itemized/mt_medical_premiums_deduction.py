from fiscalsim_us.model_api import *


class mt_medical_premiums_deduction(Variable):
    """
    Line 2 on itemized deductions schedule
    Medical insurance premiums not deducted elsewhere on the return
    """

    value_type = float
    entity = TaxUnit
    label = "Montana medical insurance premiums"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
