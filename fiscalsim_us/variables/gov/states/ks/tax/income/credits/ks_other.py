from fiscalsim_us.model_api import *


class ks_other(Variable):
    value_type = float
    entity = TaxUnit
    label = "Kansas other credits amount"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf"
