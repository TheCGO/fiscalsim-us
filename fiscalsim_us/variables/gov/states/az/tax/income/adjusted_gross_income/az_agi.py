from fiscalsim_us.model_api import *


class az_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ adjusted gross income"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        agi = tax_unit("adjusted_gross_income", period)
        additions = tax_unit("az_agi_additions", period)
        subtractions = tax_unit("az_agi_subtractions", period)
        exemptions = tax_unit("az_agi_exemptions", period)
        return max_(0, agi + additions - subtractions - exemptions)
