from fiscalsim_us.model_api import *


class oh_exemption_amount(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH exemption allowance"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2021/pit-it1040-booklet.pdf" # page 14

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.oh.tax.income.exemptions
        income = tax_unit("oh_agi", period)
        multiplier = p.exemption_multipliers.calc(income)
        exemptions = tax_unit("oh_exemptions_claimed", period)

        return multiplier * exemptions
