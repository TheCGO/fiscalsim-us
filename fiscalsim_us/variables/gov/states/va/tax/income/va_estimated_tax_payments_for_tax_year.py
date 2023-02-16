from fiscalsim_us.model_api import *


class va_estimated_tax_payments_for_tax_year(Variable):
    value_type = float
    entity = TaxUnit
    label = "va estimated tax payments for the current taxable year line 20 on form 760"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
