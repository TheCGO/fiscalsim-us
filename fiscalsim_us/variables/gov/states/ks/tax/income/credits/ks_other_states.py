from fiscalsim_us.model_api import *

#Kansas credit ffo rtaxes paid to other states
class ks_other_tates(Variable):
    value_type = float
    entity = TaxUnit
    label = "Kansas other states credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf"
