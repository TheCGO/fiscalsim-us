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
        you_fdca = tax_unit("fixed_date_conformity_additions", period)
        spouse_fdca = 0  # change this
        you_fdcs = tax_unit("fixed_date_conformity_subtractions", period)
        spouse_fdcs = 0  # change this
        if age_of_head > 65:
            if (
                filing_status == filing_statuses.SINGLE
                or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
                or filing_status == filing_status == filing_statuses.WIDOW
            ):
                age_deduction_count = 1
                total_agi = federal_agi
            elif (
                filing_status == filing_statuses.JOINT
                or filing_status == filing_statuses.SEPARATE
            ) & age_of_spouse > 65:
                age_deduction_count = 2
            else:
                total_agi = federal_agi + spouse_agi

            if (
                filing_status == filing_statuses.SINGLE
                or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
                or filing_status == filing_statuses.WIDOW
            ):
                total_fda = you_fdca
                total_fds = you_fdcs
            else:
                total_fda = you_fdca + spouse_fdca
                total_fds = you_fdcs + spouse_fdcs

            line4 = total_agi + total_fda
            line6 = line4 - total_fds
            line7 = 0  # Taxable benefits from the tax return, change this.
            line8 = line6 - line7

            if (
                filing_status == filing_statuses.SINGLE
                or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
                or filing_status == filing_statuses.WIDOW
            ):
                threshold_ln9 = (
                    parameters.gov.states.va.tax.income.va_age_deduction_threshold.single
                )
            elif filing_status == filing_statuses.JOINT:
                threshold_ln9 = (
                    parameters.gov.states.va.tax.income.va_age_deduction_threshold.joint
                )
            elif filing_status == filing_statuses.SEPARATE:
                threshold_ln9 = (
                    parameters.gov.states.va.tax.income.va_age_deduction_threshold.separate
                )

            if line8 >= threshold_ln9:
                line11 = line8 - threshold_ln9
            elif (
                filing_status == filing_statuses.SINGLE
                or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
                or filing_status == filing_statuses.WIDOW
                or filing_status == filing_statuses.SEPARATE
            ):
                return 12_000
            elif filing_status == filing_statuses.JOINT:
                return 24_000

            line12 = age_deduction_count * 12_000

            if line11 >= line12:
                return 0

            if line11 < line12:
                line14 = line12 - line11

            if (
                filing_status == filing_statuses.SINGLE
                or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
                or filing_status == filing_statuses.WIDOW
                or (
                    filing_status == filing_statuses.SEPARATE
                    and age_of_spouse < 65
                )
                or (
                    filing_status == filing_statuses.JOINT
                    and age_of_spouse < 65
                )  # the form has you divide the total by 2, but then if your filing jointly, you'd have to add it back together, so it ends up being the undivided amount
            ):
                return line14
            elif (
                filing_status == filing_statuses.SEPARATE
                and age_of_spouse >= 65
            ):
                return line14 / 2
