from fiscalsim_us.model_api import *


class ut_total_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Utah total income"
    unit = USD
    documentation = "Form TC-40, line 6"
    definition_period = YEAR
    defined_for = StateCode.UT
    adds = ["adjusted_gross_income", "ut_additions_to_income"]
