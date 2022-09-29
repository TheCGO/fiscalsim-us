from fiscalsim_us.model_api import *


class va_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA exemptions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        ut_taxpayer_credit_max = tax_unit("ut_taxpayer_credit_max", period)
        ut_taxpayer_credit_reduction = tax_unit(
            "ut_taxpayer_credit_reduction", period
        )

        va_indiv_exempt_multiplier = tax_unit("va_indiv_exemption_multiplier",
                                                period)

        va_indiv_p65_exempt_multiplier = tax_unit("va_indiv_exemption_over_65_multiplier",period)

        dependents = tax_unit("tax_unit_dependents",period)

        spouse_if_filing_jointly = ?

        you_p65 = ?

        spouse_p65 = ? # check to see if this is valid if they are filing separately 

        you_blind = ? 

        spouse_blind = ? 


        total_section_A = ((1 + spouse_if_filing_jointly + dependents) * 
                            va_indiv_exempt_multiplier)

        total_section_B = ((you_p65 + spouse_p65 + you_blind + spouse_blind)*
                            va_indiv_p65_exempt_multiplier)

        return total_section_A + total_section_B
