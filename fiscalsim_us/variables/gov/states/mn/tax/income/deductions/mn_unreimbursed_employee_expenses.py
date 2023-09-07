from fiscalsim_us.model_api import *


class mn_unreimbursed_employee_expenses(Variable):
    """
    Line 20 of 2022 M1SA, Minnesota Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "MN unreimbursed employee expenses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
