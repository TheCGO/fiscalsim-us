from fiscalsim_us.model_api import *


class taxsim_gssi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Gross Social Security Income"
    unit = USD
    definition_period = YEAR

    adds = ["social_security"]
