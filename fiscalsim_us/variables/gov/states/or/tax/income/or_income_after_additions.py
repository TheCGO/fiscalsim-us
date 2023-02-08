from fiscalsim_us.model_api import *


class or_income_after_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "OR income after additions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OR
    adds = ["adjusted_gross_income", "or_income_additions"]
