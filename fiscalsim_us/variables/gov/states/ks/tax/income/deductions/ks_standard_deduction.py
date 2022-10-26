from fiscalsim_us.model_api import *


class ks_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS standard deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf#page=6"
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        standard_deduction = parameters(
            period
        ).gov.states.ks.tax.income.deductions.standard
        filing_status = tax_unit("filing_status", period)
        count = tax_unit("ks_aged_blind_count", period)
        rates = standard_deduction.aged_blind.aged_blind_rates

        if count >= 1:
            return (rates[filing_status[count]])
            
        else:
            return (standard_deduction.amount[filing_status])
