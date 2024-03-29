from fiscalsim_us.model_api import *


class va_spouse_witholding(Variable):
    value_type = float
    entity = TaxUnit
    label = "va tax witheld from the tax year line 19b"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
