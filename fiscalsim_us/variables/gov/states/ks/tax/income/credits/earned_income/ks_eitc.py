from fiscalsim_us.model_api import *


class ks_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "KansasEITC amount"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf"