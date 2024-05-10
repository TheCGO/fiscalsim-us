from fiscalsim_us.model_api import *


class ar_cdcc_refundable_pct(Variable):
    value_type = float
    entity = TaxUnit
    label = "Percentage of AR CCDC that is refundable, meaning that it quaifies for the Early Childhood Program"
    documentation = "https://codes.findlaw.com/ar/title-26-taxation/ar-code-sect-26-51-502/"
    definition_period = YEAR
    defined_for = StateCode.AR
