from fiscalsim_us.model_api import *


class mn_unreimbursed_employee_expenses(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN unreimbursed employee business expenses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
