from openfisca_us.model_api import *


class ks_aged_blind_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS aged/blind standard deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://www.ksrevenue.gov/pdf/k-4021.pdf"

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ks.tax.income.deductions.standard.aged_blind
        filing_status = tax_unit("filing_status", period)
        count = ("ks_aged_blind_count")
        rates = p.aged_blind_rates

        return rates[filing_status[count]]
