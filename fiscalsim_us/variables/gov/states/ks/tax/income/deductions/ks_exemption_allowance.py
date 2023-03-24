from fiscalsim_us.model_api import *


class ks_exemption_allowance(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS exemption allowance"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://www.ksrevenue.gov/pdf/k-4021.pdf"

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ks.tax.income.exemptions
        ks_exemption_allowance_multiplier = p.exemption_allowance_multiplier
        ks_exemptions_claimed = tax_unit("ks_exemptions_claimed", period)

        return ks_exemption_allowance_multiplier * ks_exemptions_claimed
