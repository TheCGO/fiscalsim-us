from fiscalsim_us.model_api import *


class taxsim_dividends(Variable):
    value_type = float
    entity = TaxUnit
    label = "Dividends"
    unit = USD
    definition_period = YEAR

    adds = ["dividend_income"]
