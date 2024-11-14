from fiscalsim_us.model_api import *


class va_age_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA age deduction https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2021-760-instructions.pdf for information"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        age_of_head = tax_unit("age_head", period)
        age_of_spouse = tax_unit("age_spouse", period)
        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values
        federal_agi = tax_unit("adjusted_gross_income", period)
        spouse_agi = tax_unit("spouse_separate_adjusted_gross_income", period)
        you_fdca = tax_unit("va_fixed_date_conformity_additions", period)
        spouse_fdca = 0  # change this
        you_fdcs = tax_unit("va_fixed_date_conformity_subtractions", period)
        spouse_fdcs = 0  # change this

        age_deduction_count = where(
            (age_of_head > 65)
            & (
                (filing_status == filing_statuses.SINGLE)
                | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
                | (filing_status == filing_statuses.SURVIVING_SPOUSE)
            ),
            1,
            where(
                (filing_status == filing_statuses.JOINT)
                & (age_of_spouse > 65),
                2,
                0,  # Default value if none of the conditions are met
            ),
        )

        total_agi = where(
            age_deduction_count > 0, federal_agi + spouse_agi, federal_agi
        )

        total_fda = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE),
            you_fdca,
            you_fdca + spouse_fdca,
        )

        total_fds = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE),
            you_fdcs,
            you_fdcs + spouse_fdcs,
        )

        line4 = total_agi + total_fda
        line6 = line4 - total_fds
        line7 = 0  # Taxable benefits from the tax return, change this.
        line8 = line6 - line7

        threshold_ln9 = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE),
            parameters(
                period
            ).gov.states.va.tax.income.va_age_deduction_threshold.SINGLE,
            where(
                filing_status == filing_statuses.JOINT,
                parameters(
                    period
                ).gov.states.va.tax.income.va_age_deduction_threshold.JOINT,
                parameters(
                    period
                ).gov.states.va.tax.income.va_age_deduction_threshold.SEPARATE,
            ),
        )

        line11 = where(
            line8 >= threshold_ln9,
            line8 - threshold_ln9,
            where(
                (filing_status == filing_statuses.SINGLE)
                | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
                | (filing_status == filing_statuses.SURVIVING_SPOUSE)
                | (filing_status == filing_statuses.SEPARATE),
                12_000,
                where(filing_status == filing_statuses.JOINT, 24_000, 0),
            ),
        )

        line12 = age_deduction_count * 12_000

        line14 = where(line11 < line12, line12 - line11, 0)

        result = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE)
            | (
                (filing_status == filing_statuses.SEPARATE)
                & (age_of_spouse < 65)
            )
            | (
                (filing_status == filing_statuses.JOINT) & (age_of_spouse < 65)
            ),
            line14,
            where(
                (filing_status == filing_statuses.SEPARATE)
                & (age_of_spouse >= 65),
                line14 / 2,
                0,
            ),
        )

        # Check if age_of_head is less than 65 and set result to 0 in that case
        result = where(age_of_head < 65, 0, result)

        return result
