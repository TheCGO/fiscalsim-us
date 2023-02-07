from fiscalsim_us.model_api import *


class rrc_cares(Variable):
    value_type = float
    entity = TaxUnit
    label = "Recovery Rebate Credit (CARES)"
    unit = USD
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/6428"

    def formula(tax_unit, period, parameters):
        rrc = parameters(period).gov.irs.credits.recovery_rebate_credit
        filing_status = tax_unit("filing_status", period)
        agi = tax_unit("adjusted_gross_income", period)
        count_children = tax_unit("ctc_qualifying_children", period)
        # (a)(2) specifies CTC eligibility for children
        count_adults = where(tax_unit("tax_unit_is_joint", period), 2, 1)
        max_payment = (
            rrc.cares.max.adult * count_adults
            + rrc.cares.max.child * count_children
        )
        payment_reduction = rrc.cares.phase_out.rate * max_(
            0, agi - rrc.cares.phase_out.threshold[filing_status]
        )
        return max_(0, max_payment - payment_reduction)
