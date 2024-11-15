from fiscalsim_us.model_api import *


class ar_refundable_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas Child and Dependent Care Credit Nonrefundable Portion"
    unit = USD
    documentation = "https://codes.findlaw.com/ar/title-26-taxation/ar-code-sect-26-51-502/"
    definition_period = YEAR
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        cdcc = tax_unit("ar_cdcc", period)
        refundable_pct = tax_unit("ar_cdcc_refundable_pct", period)

        return cdcc * refundable_pct
