from fiscalsim_us.model_api import *


class ar_lump_sum_dist_tax(Variable):
    "Line 31 of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Lump Sum Distribution Tax"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TD_LumpSumDistributionAveraging.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):

    # Pull in distribution amount here
        taxable_dist = 0

        line_4_max = parameters(period).gov.states.ar.tax.income.lump_sum_dist.min_allowance_multiple1_max
        line_4_multiple = parameters(period).gov.states.ar.tax.income.lump_sum_dist.min_allowance_multiple1

        line_4 = max(line_4_max, taxable_dist * line_4_multiple)

        min_allowance_subtraction = parameters(period).gov.states.ar.tax.income.lump_sum_dist.min_allowance_subtract

        line_5 = max(0, taxable_dist - min_allowance_subtraction)

        line_6_multiple = parameters(period).gov.states.ar.tax.income.lump_sum_dist.min_allowance_multiple2

        line_6 = line_5 * line_6_multiple

        min_allowance = line_6 - line_4

        line_8 = taxable_dist - min_allowance

        line_9_multiple = parameters(period).gov.states.ar.tax.income.lump_sum_dist.Line9_multiple

        line_9 = line_8 * line_9_multiple

        rate = where(taxable_income < high_income_threshold, parameters(period).gov.states.ar.tax.income.rates.rates, parameters(period).gov.states.ar.tax.income.rates.high_income_rates)
        
        tax = rate.calc(line_9)