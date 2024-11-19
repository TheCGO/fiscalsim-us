from fiscalsim_us.model_api import *
from numpy import round


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
        # def high_income_reduction(income):

        #     full_reduction= parameters(period).gov.states.ar.tax.income.high_income_reduction.high_income_reduction_amount
        #     min_income = parameters(period).gov.states.ar.tax.income.rates.regular_bracket_max + 1
        #     phaseout_rate = parameters(period).gov.states.ar.tax.income.high_income_reduction.high_income_reduction_phaseout

        #     def round_to_nearest_50(num):
        #         # Calculate the nearest multiple of 100
        #         nearest_multiple_of_100 = round(num / 100,0) * 100

        #         # Get the last two digits
        #         last_two_digits = num % 100

        #         # Determine the closest ending in "50"
        #         if last_two_digits <= 50 and last_two_digits >= 1:
        #             rounded_income = nearest_multiple_of_100 + 50
        #             return rounded_income
        #         else:
        #             rounded_income = nearest_multiple_of_100 - 50
        #             return rounded_income

        #     std_ded = tax_unit("ar_standard_deduction", period)
        #     itm_ded = tax_unit("ar_itemized_deductions", period)
        #     deduction = where(itm_ded > std_ded, itm_ded, std_ded)

        #     income_less_ded = income - deduction

        #     rounded_income = round_to_nearest_50(income_less_ded)
        #     rounded_min_income = round_to_nearest_50(min_income)

        #     # Calculate the phaseout reduction for each $100 over min_income
        #     excess_income = rounded_income - rounded_min_income
        #     phaseout_reduction = where( excess_income % 100 == 0, (excess_income // 100) * phaseout_rate, ((excess_income // 100) + 1) * phaseout_rate)

        #     # Reduce the credit amount based on the phaseout reduction
        #     reduction_amount = full_reduction - phaseout_reduction

        #     # Ensure credit_amount does not go below 0
        #     reduction_amount = where(reduction_amount < 0 or excess_income < 0 ,
        #         0, reduction_amount)

        #     reduction_amount = round(reduction_amount,0)

        #     return reduction_amount

        p = parameters(period).gov.states.ar.tax.income.lump_sum_dist
        high_income_threshold = (
            parameters(
                period
            ).gov.states.ar.tax.income.rates.regular_bracket_max
            + 1
        )
        high_income_reduction = parameters(
            period
        ).gov.states.ar.tax.income.high_income_reduction.high_income_reduction

        income = tax_unit("ar_distribution_income", period)
        actuarial_value = tax_unit("ar_actuarial_value", period)
        taxable_dist = income + actuarial_value
        min_allowance_threshold = p.min_allowance_threshold

        std_ded = tax_unit("ar_standard_deduction", period)
        itm_ded = tax_unit("ar_itemized_deductions", period)
        deduction = where(itm_ded > std_ded, itm_ded, std_ded)

        line_4_max = p.min_allowance_multiple1_max
        line_4_multiple = p.min_allowance_multiple1

        line_4 = min_(line_4_max, taxable_dist * line_4_multiple)

        min_allowance_subtraction = p.min_allowance_subtract

        line_5 = max_(0, taxable_dist - min_allowance_subtraction)

        line_6_multiple = p.min_allowance_multiple2

        line_6 = line_5 * line_6_multiple

        min_allowance = where(
            taxable_dist < min_allowance_threshold, line_4 - line_6, 0
        )

        line_8 = where(
            taxable_dist < min_allowance_threshold,
            taxable_dist - min_allowance,
            taxable_dist,
        )

        line_9_multiple = p.Line9_multiple

        line_9 = line_8 * line_9_multiple

        # line_9_reduction = high_income_reduction(line_9)
        line_9_reduction = high_income_reduction.calc(line_9)

        line_9_tax = round_(
            where(
                line_9 <= high_income_threshold,
                parameters(period).gov.states.ar.tax.income.rates.rates.calc(
                    (line_9 - deduction)
                ),
                parameters(
                    period
                ).gov.states.ar.tax.income.rates.high_income_rates.calc(
                    (line_9 - deduction)
                ),
            )
            - line_9_reduction,
            0,
        )

        line_11_multiple = p.Line11_multiple

        line_11 = line_9_tax * line_11_multiple

        line_12 = actuarial_value / taxable_dist

        line_13 = min_allowance * line_12

        line_14 = actuarial_value - line_13

        line_15_multiple = p.Line15_multiple

        line_15 = line_14 * line_15_multiple

        line_15_reduction = high_income_reduction.calc(line_15)

        line_15_tax = round_(
            where(
                line_15 <= high_income_threshold,
                parameters(period).gov.states.ar.tax.income.rates.rates.calc(
                    line_15 - deduction
                ),
                parameters(
                    period
                ).gov.states.ar.tax.income.rates.high_income_rates.calc(
                    line_15 - deduction
                ),
            )
            - line_15_reduction,
            0,
        )

        line_17_multiple = p.Line17_multiple

        line_17 = line_15_tax * line_17_multiple

        tax = where(actuarial_value > 0, line_11 - line_17, 0)

        return tax
