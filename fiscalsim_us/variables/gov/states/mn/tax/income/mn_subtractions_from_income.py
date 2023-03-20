from fiscalsim_us.model_api import *


class mn_subtractions_from_income(Variable):
    """
    Line 8 of Minnesota 2022 Individual Income Tax return from M1.
    """
    value_type = float
    entity = TaxUnit
    label = "MN subtrations from income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
    adds = ["mn_deductions", "mn_exemptions", "mn_other_subtractions_from_income"]
