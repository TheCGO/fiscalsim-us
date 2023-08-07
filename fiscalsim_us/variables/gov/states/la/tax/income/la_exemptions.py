from fiscalsim_us.model_api import *


class la_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana exemptions amount"
    unit = USD
    definition_period = YEAR
    reference = (
    )
    defined_for = StateCode.LA

    def formula(tax_unit, period, parameters):

        p = parameters(period).gov.states.la.tax.income.exemptions
        filing_status = tax_unit("filing_status", period)
        statuses = filing_status.possible_values
        joint_separate = (filing_status == statuses.JOINT) | (
            filing_status == statuses.SEPARATE
        )
 
        dependents = tax_unit("tax_unit_dependents", period)
        aged_blind = tax_unit("aged_blind_count", period) 

        personal_multiplier = where(joint_separate, 2, 1)
        n_extra = dependents + aged_blind 

        return p.personal_amount * personal_multiplier + p.additional_amount * n_extra
