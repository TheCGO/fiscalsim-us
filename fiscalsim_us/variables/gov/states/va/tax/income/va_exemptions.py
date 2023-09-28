from fiscalsim_us.model_api import *


class va_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA exemptions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        va_indiv_exempt_multiplier = parameters(
            period
        ).gov.states.va.tax.income.exemptions.indiv_exemption_multiplier
        # va_indiv_exempt_multiplier = tax_unit("va_indiv_exemption_multiplier",
        #                                         period)

        # va_indiv_p65_exempt_multiplier = tax_unit(
        #     "va_indiv_exemption_over_65_multiplier",period)

        va_indiv_p65_exempt_multiplier = parameters(
            period
        ).gov.states.va.tax.income.exemptions.indiv_exemption_over_65_multiplier

        dependents = tax_unit("tax_unit_dependents", period)

        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values

        if (
            filing_status == filing_statuses.SINGLE
            or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
            or filing_status == filing_statuses.WIDOW
            or filing_status == filing_statuses.SEPARATE
        ):
            spouse_if_filing_jointly = 0

        elif filing_status == filing_statuses.JOINT:
            spouse_if_filing_jointly = 1

        you_p65 = (tax_unit("age_head", period) >= 65).astype(int)

        spouse_p65 = (tax_unit("age_spouse", period) >= 65).astype(
            int
        )  # check to see if this is valid if they are filing separately

        you_blind = tax_unit("blind_head", period).astype(int)

        spouse_blind = tax_unit("blind_spouse", period).astype(int)

        total_section_A = (
            1 + spouse_if_filing_jointly + dependents
        ) * va_indiv_exempt_multiplier

        total_section_B = (
            you_p65 + spouse_p65 + you_blind + spouse_blind
        ) * va_indiv_p65_exempt_multiplier

        return total_section_A + total_section_B
