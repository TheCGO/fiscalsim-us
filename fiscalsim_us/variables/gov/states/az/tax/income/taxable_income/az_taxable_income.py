from fiscalsim_us.model_api import *


class az_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ taxable income"
    unit = USD
    documentation = "AZ AGI less taxable income deductions"
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        agi = tax_unit("az_agi", period)
        deductions = tax_unit("az_deductions", period)
        return max_(0, agi - deductions)
