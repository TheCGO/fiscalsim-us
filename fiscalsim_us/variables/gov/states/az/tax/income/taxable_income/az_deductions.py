from fiscalsim_us.model_api import *


class az_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ income deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        return max_(
            tax_unit("az_itemized_deductions", period),
            tax_unit("az_standard_deduction", period),
        )
