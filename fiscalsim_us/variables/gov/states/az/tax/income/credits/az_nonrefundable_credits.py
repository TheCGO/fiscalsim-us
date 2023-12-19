from fiscalsim_us.model_api import *


class az_nonrefundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ nonrefundable credits"
    unit = USD
    documentation = (
        "AZ nonrefundable credits added on lines 49,50, and 51 of form 140"
    )
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        dependent_credit = tax_unit("az_dependent_credit", period)
        family_income_credit = tax_unit("az_family_income_credit", period)

        return dependent_credit + family_income_credit
