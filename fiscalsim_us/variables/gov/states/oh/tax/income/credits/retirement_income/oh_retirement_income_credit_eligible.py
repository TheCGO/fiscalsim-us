from fiscalsim_us.model_api import *


class oh_retirement_income_credit_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Ohio Retirement Income Credit Eligible"
    unit = USD
    definition_period = YEAR
    reference = "https://codes.ohio.gov/ohio-revised-code/section-5747.055"
    defined_for = StateCode.OH

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.oh.tax.income.credits.retirement_income

        agi = tax_unit("oh_agi", period)
        return agi < p.income_threshold
