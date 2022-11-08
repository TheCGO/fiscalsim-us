from fiscalsim_us.model_api import *


class oh_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH adjusted gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2021/1040-bundle.pdf"

    def formula(tax_unit, period, parameters):
        federal_agi = tax_unit("adjusted_gross_income", period)
        additions = tax_unit("oh_additions", period)
        deductions = tax_unit("oh_deductions", period)

        return federal_agi + additions - deductions
