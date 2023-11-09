from fiscalsim_us.model_api import *


class ar_unreimbursed_employee_expenses(Variable):
    """
    Line 20 of 2022 AR3, Arkansas Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "AR unreimbursed employee expenses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR