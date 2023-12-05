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

        p = parameters(period).gov.states.ar.tax.income.lump_sum_dist
        high_income_threshold = parameters(period).gov.states.ar.tax.income.rates.regular_bracket_max

        income = tax_unit('ar_distribution_income', period)
        actuarial_value = tax_unit('ar_actuarial_value', period)
        taxable_dist = income + actuarial_value

        line_4_max = p.min_allowance_multiple1_max
        line_4_multiple = p.min_allowance_multiple1

        line_4 = max(line_4_max, taxable_dist * line_4_multiple)

        min_allowance_subtraction = p.min_allowance_subtract

        line_5 = max(0, taxable_dist - min_allowance_subtraction)

        line_6_multiple = p.min_allowance_multiple2

        line_6 = line_5 * line_6_multiple

        min_allowance = line_6 - line_4

        line_8 = taxable_dist - min_allowance

        line_9_multiple = p.Line9_multiple

        line_9 = line_8 * line_9_multiple

        rate_line_9 = where(line_9 < high_income_threshold, parameters(period).gov.states.ar.tax.income.rates.rates, parameters(period).gov.states.ar.tax.income.rates.high_income_rates)
        
        line_9_tax = rate_line_9.calc(line_9)

        line_11_multiple = p.line11_multiple

        line_11 = line_9_tax * line_11_multiple

        line_12 = actuarial_value / taxable_dist

        line_13 = min_allowance * line_12

        line_14 = actuarial_value - line_13

        line_15_multiple = p.Line15_multiple

        line_15 = line_14 * line_15_multiple

        rate_line_15 = where(line_15 < high_income_threshold, parameters(period).gov.states.ar.tax.income.rates.rates, parameters(period).gov.states.ar.tax.income.rates.high_income_rates)

        line_15_tax = rate_line_15.calc(line_15)

        line_17_multiple = p.Line17_multiple

        line_17 = line_15_tax * line_17_multiple

        tax = where(actuarial_value > 0,line_17 - line_11,0)

        return tax