from fiscalsim_us.model_api import *
import numpy as np


class ar_income_tax_before_non_refundable_credits(Variable):
    "Line 29 of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas income tax before non refundable credits"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2023_Final_AR1000ES.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ar.tax.income.rates
        taxable_income = tax_unit("ar_taxable_income", period)
        high_income_threshold = p.regular_bracket_max
        litc = tax_unit("ar_low_income_credit", period)
        high_income_reduction = tax_unit("ar_high_income_reduction", period)

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

        rounded_taxable_income = round_to_nearest_50(taxable_income)

        if np.isscalar(rounded_taxable_income):
            tax = np.round(
                where(
                    taxable_income <= high_income_threshold,
                    p.rates.calc(rounded_taxable_income),
                    p.high_income_rates.calc(rounded_taxable_income),
                )
                - litc
                - high_income_reduction,
                0,
            )
        else:
            tax = np.zeros_like(rounded_taxable_income)
            tax[taxable_income <= high_income_threshold] = np.round(
                p.rates.calc(
                    rounded_taxable_income[
                        taxable_income <= high_income_threshold
                    ]
                )
                - litc[taxable_income <= high_income_threshold]
                - high_income_reduction[
                    taxable_income <= high_income_threshold
                ],
                0,
            )
            tax[taxable_income > high_income_threshold] = np.round(
                p.high_income_rates.calc(
                    rounded_taxable_income[
                        taxable_income > high_income_threshold
                    ]
                )
                - litc[taxable_income > high_income_threshold]
                - high_income_reduction[
                    taxable_income > high_income_threshold
                ],
                0,
            )

        lump_sum_dist_tax = tax_unit("ar_lump_sum_dist_tax", period)

        # Additional tax on IRA and qualified plan withdrawal and overpayment, not modelled

        total_tax = tax + lump_sum_dist_tax

        return total_tax
