from fiscalsim_us.model_api import *


class va_credits_from_enclosed_schedule_cr(Variable):
    value_type = float
    entity = TaxUnit
    label = "Schedule CR, Section 5, Part 1, Line 1A"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
