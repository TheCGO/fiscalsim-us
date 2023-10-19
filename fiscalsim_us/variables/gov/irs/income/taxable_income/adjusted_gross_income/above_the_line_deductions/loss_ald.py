from fiscalsim_us.model_api import *


class loss_ald(Variable):
    value_type = float
    entity = TaxUnit
    label = "Business loss ALD"
    unit = USD
    documentation = (
        "Above-the-line deduction from gross income for business losses."
    )
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/165"

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        max_loss = parameters(period).gov.irs.ald.loss.max[filing_status]
        person = tax_unit.members
        indiv_se_loss = max_(0, -person("self_employment_income", period))
        self_employment_loss = tax_unit.sum(indiv_se_loss)
        limited_capital_loss = tax_unit("limited_capital_loss", period)
        return min_(max_loss, self_employment_loss + limited_capital_loss)
