from fiscalsim_us.model_api import *


class mt_per_capita_livestock_deduction(Variable):
    """
    Line 7 on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana per capita livestock fees"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
