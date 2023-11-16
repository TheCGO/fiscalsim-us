from fiscalsim_us.model_api import *


class mt_medical_dental_expense(Variable):
    """
    Line 1a on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana medical and dental expense"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
