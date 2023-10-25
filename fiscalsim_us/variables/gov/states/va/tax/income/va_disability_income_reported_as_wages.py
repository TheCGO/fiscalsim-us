from fiscalsim_us.model_api import *


class va_disability_income_reported_as_wages(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA disability income reported as wages - https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
