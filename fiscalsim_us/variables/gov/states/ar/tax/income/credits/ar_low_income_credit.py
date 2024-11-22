from fiscalsim_us.model_api import *
import numpy as np


class ar_low_income_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas low income tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_TaxTables.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        tax_rate = parameters(period).gov.states.ar.tax.income.rates.rates
        credit_rate = parameters(
            period
        ).gov.states.ar.tax.income.credits.low_income_credit.income_tax_credit_pct
        num_dependents = tax_unit("tax_unit_dependents", period)
        min_income = where(
            num_dependents < 2,
            parameters(
                period
            ).gov.states.ar.tax.income.credits.low_income_credit.low_dep_inc_tax_credit_min_income[
                filing_status
            ],
            parameters(
                period
            ).gov.states.ar.tax.income.credits.low_income_credit.high_dep_inc_tax_credit_min_income[
                filing_status
            ],
        )
        phaseout_rate = where(
            num_dependents < 2,
            parameters(
                period
            ).gov.states.ar.tax.income.credits.low_income_credit.low_dep_inc_tax_credit_phaseout_rate[
                filing_status
            ],
            parameters(
                period
            ).gov.states.ar.tax.income.credits.low_income_credit.high_dep_inc_tax_credit_phaseout_rate[
                filing_status
            ],
        )
        agi = tax_unit("ar_agi", period)

        def round_to_nearest_50(num):
            # Calculate the nearest multiple of 100
            nearest_multiple_of_100 = np.round(num / 100) * 100

            # Get the last two digits
            last_two_digits = num % 100

            # Determine the closest ending in "50"
            if np.isscalar(num):
                if last_two_digits <= 50:
                    rounded_income = nearest_multiple_of_100 + 50
                    return rounded_income
                else:
                    rounded_income = nearest_multiple_of_100 - 50
                    return rounded_income
            else:
                rounded_income = np.zeros_like(num)
                rounded_income[last_two_digits <= 50] = (
                    nearest_multiple_of_100[last_two_digits <= 50] + 50
                )
                rounded_income[last_two_digits > 50] = (
                    nearest_multiple_of_100[last_two_digits > 50] - 50
                )
                return rounded_income

        std_ded = tax_unit("ar_standard_deduction", period)
        itm_ded = tax_unit("ar_itemized_deductions", period)
        deduction = where(itm_ded > std_ded, itm_ded, std_ded)

        agi_less_ded = agi - deduction
        min_inc_less_ded = min_income - deduction

        rounded_income = round_to_nearest_50(agi_less_ded)
        rounded_min_income = round_to_nearest_50(min_inc_less_ded)

        # Calculate the tax liability on min_income
        min_tax_liability = tax_rate.calc(rounded_min_income)

        min_tax_liability = np.round(min_tax_liability)

        # Calculate the credit amount
        credit_amount = min_tax_liability * credit_rate

        # Calculate the phaseout reduction for each $100 over min_income
        excess_income = rounded_income - rounded_min_income
        phaseout_count = where(
            excess_income % 100 > 0,
            excess_income // 100 + 1,
            excess_income // 100,
        )
        phaseout_reduction = phaseout_count * phaseout_rate

        # Reduce the credit amount based on the phaseout reduction
        credit_amount -= phaseout_reduction

        # Ensure credit_amount does not go below 0 and that those who itemize or are married filing separately do not take the credit
        if np.isscalar(credit_amount):
            credit_amount = where(
                credit_amount < 0
                or std_ded < itm_ded
                or filing_status == "SEPARATE",
                0,
                credit_amount,
            )
        else:
            credit_amount[
                (
                    (credit_amount < 0)
                    | (std_ded < itm_ded)
                    | (filing_status == "SEPARATE")
                )
            ] = 0

        credit_amount = np.round(credit_amount, 0)

        return credit_amount
