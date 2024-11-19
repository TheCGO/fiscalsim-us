from fiscalsim_us.model_api import *
import numpy as np


class ar_high_income_reduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas high income reduction"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_TaxTables.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        reduction = parameters(
            period
        ).gov.states.ar.tax.income.high_income_reduction.high_income_reduction
        min_income = (
            parameters(
                period
            ).gov.states.ar.tax.income.rates.regular_bracket_max
            + 1
        )
        agi = tax_unit("ar_agi", period)

        def round_to_nearest_50(num):
            # Calculate the nearest multiple of 100
            nearest_multiple_of_100 = np.round(num / 100, 0) * 100

            # Get the last two digits
            last_two_digits = num % 100

            # Determine the closest ending in "50"
            if np.isscalar(num):
                if last_two_digits <= 50 and last_two_digits >= 1:
                    rounded_income = nearest_multiple_of_100 + 50
                    return rounded_income
                else:
                    rounded_income = nearest_multiple_of_100 - 50
                    return rounded_income
            else:
                rounded_income = np.zeros_like(num)
                rounded_income[
                    (last_two_digits <= 50) & (last_two_digits >= 1)
                ] = (
                    nearest_multiple_of_100[
                        (last_two_digits <= 50) & (last_two_digits >= 1)
                    ]
                    + 50
                )
                rounded_income[
                    (last_two_digits > 50) | (last_two_digits < 1)
                ] = (
                    nearest_multiple_of_100[
                        (last_two_digits > 50) | (last_two_digits < 1)
                    ]
                    - 50
                )
                return rounded_income

        std_ded = tax_unit("ar_standard_deduction", period)
        itm_ded = tax_unit("ar_itemized_deductions", period)
        deduction = where(itm_ded > std_ded, itm_ded, std_ded)

        agi_less_ded = agi - deduction

        rounded_income = round_to_nearest_50(agi_less_ded)
        rounded_min_income = round_to_nearest_50(min_income)

        reduction_amount = reduction.calc(rounded_income, right=True)

        return reduction_amount
