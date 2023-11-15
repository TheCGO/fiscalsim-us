from fiscalsim_us.model_api import *


class mt_political_contributions_deduction(Variable):
    """
    Line 16 on itemized deductions schedule
    Limited to $100 per taxpayer
    """

    value_type = float
    entity = TaxUnit
    label = "Montana political contributions deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.mt.tax.income.deductions.itemized.misc
        cap = p.political_contribution_cap
        contributions = tax_unit("mt_political_contributions")

        return min_(cap, contributions)
