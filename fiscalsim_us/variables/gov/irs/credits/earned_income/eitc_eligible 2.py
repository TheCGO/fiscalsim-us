from fiscalsim_us.model_api import *


class eitc_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Eligible for EITC"
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/32#c_1_A"

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        has_child = tax_unit("tax_unit_children", period) > 0
        age = person("age", period)
        # Relative parameter reference break branching in some states that
        # modify EITC age limits.
        eitc = parameters.gov.irs.credits.eitc(period)
        min_age = parameters.gov.irs.credits.eitc.eligibility.age.min(period)
        max_age = parameters.gov.irs.credits.eitc.eligibility.age.max(period)
        meets_age_requirements = (age >= min_age) & (age <= max_age)
        no_loss_capital_gains = max_(
            0,
            add(tax_unit, period, ["capital_gains"]),
        )
        eitc_investment_income = (
            add(
                tax_unit,
                period,
                ["net_investment_income", "tax_exempt_interest_income"],
            )
            # Replace limited-loss capital gains with no-loss capital gains.
            - tax_unit("c01000", period)  # Limited-loss capital gains.
            + no_loss_capital_gains
        )
        inv_income_disqualified = (
            eitc_investment_income > eitc.phase_out.max_investment_income
        )
        demographic_eligible = has_child | tax_unit.any(meets_age_requirements)
        # Define eligibility before considering separate filer limitation.
        eligible = demographic_eligible & ~inv_income_disqualified
        # This parameter is true if separate filers are eligible.
        if eitc.eligibility.separate_filer:
            return eligible
        # If separate filers are not eligible, check if the filer is separate.
        filing_status = tax_unit("filing_status", period)
        separate = filing_status == filing_status.possible_values.SEPARATE
        return eligible & ~separate
