from fiscalsim_us.model_api import *


class ga_nol_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia Net Operating Loss deduction from income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.georgia.gov/it-511-individual-income-tax-booklet"
        # above reference provides access to booklets for all years
        # definition of Georgia taxable income starts on page 12
    )
    defined_for = StateCode.GA

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ga.tax.income.deductions.nol_limit
        agi = tax_unit("ga_agi", period)
        deductions = tax_unit("ga_deductions", period)
        exemptions = tax_unit("ga_exemptions", period)
        pre_nol_income = max_(0, agi - deductions - exemptions)

        # no limit on pre-2018 NOL carryover
        pre2018 = tax_unit("ga_pre2018_nol_carryover", period)
        # NOL from years 2018 and after are limited to a percentage of
        # taxable income before NOL
        post2018 = tax_unit("ga_post2018_nol", period)
        limited_post = min_(pre_nol_income * p, post2018)

        return pre2018 + limited_post
