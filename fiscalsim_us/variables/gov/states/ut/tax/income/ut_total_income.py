from fiscalsim_us.model_api import *


class ut_total_income(Variable):
    """
    Line 6 on Utah 2022 Individual Income Tax return form TC-40.
    """

    value_type = float
    entity = TaxUnit
    label = "UT total income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.UT

    adds = ["adjusted_gross_income", "ut_additions_to_income"]
