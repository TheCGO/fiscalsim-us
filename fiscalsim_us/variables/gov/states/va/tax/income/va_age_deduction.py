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

        federal_agi = tax_unit("adjusted_gross_income", period)

        spouse_agi = tax_unit("spouse_separate_adjusted_gross_income", period)

        you_fdca = tax_unit("fixed_date_conformity_additions", period)

        spouse_fdca = 0  # change this

        you_fdcs = tax_unit("fixed_date_conformity_subtractions", period)

        spouse_fdcs = 0  # change this

        if age_of_head > 65:
            if filing_status == 1:
                age_deduction_count = 1

            if filing_status == 2 & age_of_spouse > 65:
                age_deduction_count = 2

            if filing_status == 1:
                total_agi = federal_agi

            else:
                total_agi = federal_agi + spouse_agi

            if filing_status == 1:
                total_fda = you_fdca

            else:
                total_fda = you_fdca + spouse_fdca

            if filing_status == 1:
                total_fds = you_fdcs

            else:
                total_fds = you_fdcs + spouse_fdcs

            line4 = total_agi + total_fda

            line6 = line4 - total_fds

            line7 = 0  # Taxable benefits from the tax return, change this.

            line8 = line6 - line7

            if filing_status == 1:
                threshold_ln9 = (
                    parameters.gov.states.va.tax.income.va_age_deduction_threshold.single
                )

            if filing_status == 2:
                threshold_ln9 = (
                    parameters.gov.states.va.tax.income.va_age_deduction_threshold.joint
                )

            if filing_status == 3:
                threshold_ln9 = (
                    parameters.gov.states.va.tax.income.va_age_deduction_threshold.separate
                )

            if line8 > threshold_ln9:
                line11 = line8 - threshold_ln9

            line12 = age_deduction_count * 12000

            if line11 > line12:
                final_age_deduction = 0

            if line11 < line12:
                line14 = line12 - line11

            if filing_status == 1 or filing_status == 2:
                return line14

            if filing_status == 3:
                return line14 / 2
