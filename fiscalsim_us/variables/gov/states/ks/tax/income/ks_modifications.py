from fiscalsim_us.model_api import *


class ks_modifications(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS modifications"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://www.ksrevenue.gov/pdf/k-4021.pdf"
