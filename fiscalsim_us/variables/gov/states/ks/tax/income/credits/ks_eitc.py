from fiscalsim_us.model_api import *


class ks_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS EITC"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip22.pdf"  # page 8 worksheet
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        eitc = tax_unit("earned_income_tax_credit", period)
        rate = parameters(period).gov.states.ks.tax.income.credits.eitc.match
        return eitc * rate