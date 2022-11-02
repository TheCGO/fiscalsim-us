from fiscalsim_us.model_api import *

#Kansas credit for child and dependent care expenses
class ks_child_care(Variable):
    value_type = float
    entity = TaxUnit
    label = "Kansas child care credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf"
