from fiscalsim_us.model_api import *


class mn_itemized_deductions(Variable):
    """
    Line 4 of Minnesota 2022 Individual Income Tax return from M1.
    """
    value_type = float
    entity = TaxUnit
    label = "MN itemized deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
    adds = [
        "mn_other_itemized_deductions",
        "mn_medical_dental_deduction",
        "interest_expense"
        ]
