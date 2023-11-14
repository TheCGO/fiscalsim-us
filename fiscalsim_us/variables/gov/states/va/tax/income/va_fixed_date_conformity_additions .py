from fiscalsim_us.model_api import *


class va_fixed_date_conformity_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Va fixed date conformity additions https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/schedule-adj-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
