from fiscalsim_us.model_api import *


class la_state_employee_retirement_benefits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana state empoyees' retirement benefits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
