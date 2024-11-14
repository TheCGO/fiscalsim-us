from fiscalsim_us.model_api import *


class sc_cdcc(Variable):
    """
    South Carolina Child and Dependent Care Credit, line 11 on form SC1040
    """

    value_type = float
    entity = TaxUnit
    label = "South Carolina CDCC"
    documentation = "South Carolina Child and Dependent Care Credit"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.sc.gov/forms-site/Forms/IITPacket_2023.pdf#page=32"
    )
    defined_for = StateCode.SC

    def formula(tax_unit, period, parameters):
        # Get South Carolina CDCC rate.
        p_sc = parameters(period).gov.states.sc.tax.income.credits.cdcc
        p_us = parameters(period).gov.irs.credits.cdcc

        # Married filing separate are ineligible.
        filing_status = tax_unit("filing_status", period)
        eligible = filing_status != filing_status.possible_values.SEPARATE

        # Number of qualifying people
        count_cdcc_eligible = min_(
            tax_unit("count_cdcc_eligible", period), p_us.eligibility.max
        )
        # Calculate the total state CDCC match for years starting before 2023
        pre_2023 = period.start.year < 2023

        # Year 2021 is different from federal cdcc
        max_decoupled_year_offset = p_sc.max_care_expense_year_offset
        period_max = period.offset(max_decoupled_year_offset)
        sc_max_care_expense = parameters(period_max).gov.irs.credits.cdcc.max

        # Get child care expenses.
        childcare_expenses = tax_unit("tax_unit_childcare_expenses", period)

        # Maximum value cannot exceed cap
        # Calculate total CDCC
        capped_expenses = min_(
            childcare_expenses, sc_max_care_expense * count_cdcc_eligible
        )
        sc_pre2023_tot_cdcc_match = eligible * capped_expenses * p_sc.rate

        # Calculate the total state CDCC match for years starting on or after
        # 2023
        max_expense = min_(
            p_sc.max_amount_pchild * count_cdcc_eligible, p_sc.total_max
        )
        sc_post2023_tot_cdcc_match = min_(
            max_expense, p_sc.rate * tax_unit("cdcc", period)
        )
        sc_tot_cdcc_match = (
            pre_2023 * sc_pre2023_tot_cdcc_match
            + (not pre_2023) * sc_post2023_tot_cdcc_match
        )
        return sc_tot_cdcc_match
