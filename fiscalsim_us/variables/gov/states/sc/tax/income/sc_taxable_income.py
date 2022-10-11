from fiscalsim_us.model_api import *


class sc_total_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "SC total additions"
    unit = USD
    documentation = "South Carolina State income tax total additions."
    definition_period = YEAR
    reference = "https://dor.sc.gov/forms-site/Forms/SC1040_2021.pdf"
    defined_for = StateCode.SC
    defined_for = StateCode.SC

    def formula(tax_unit, period, parameters):
        federal_taxable_income = tax_unit(
            "sc_income", period
        )
        p = parameters(period).gov.states.sc.tax.income
        credit_value = add(tax_unit, period, p.credits.allowed)
        return income_tax_before_credits + credit_value
