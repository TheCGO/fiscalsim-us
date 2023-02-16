from fiscalsim_us.model_api import *


class income_from_obligations_fed_exempt(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA income from obligations that are federally exempt https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/schedule-adj-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
