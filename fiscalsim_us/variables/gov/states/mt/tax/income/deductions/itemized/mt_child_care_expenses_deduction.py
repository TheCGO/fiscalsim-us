from fiscalsim_us.model_api import *


class mt_child_care_expense_deduction(Variable):
    """
    Line 14 on Montana itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana child and dependent care expenses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
