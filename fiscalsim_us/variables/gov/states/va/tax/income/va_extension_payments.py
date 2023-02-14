from fiscalsim_us.model_api import *


class va_extension_payments(Variable):
    value_type = float
    entity = TaxUnit
    label = "from form 760IP https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760ip-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
