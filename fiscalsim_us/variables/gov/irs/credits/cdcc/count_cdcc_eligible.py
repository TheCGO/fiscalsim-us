from policyengine_us.model_api import *


class count_cdcc_eligible(Variable):
    value_type = int
    entity = TaxUnit
    label = "CDCC-eligible children"
    unit = USD
    definition_period = YEAR

    formula = sum_of_variables(["is_cdcc_eligible"])
