from fiscalsim_us.model_api import *


class az_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arizona income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/resident-personal-income-tax-return-non-calculating-fillable"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        tax_before_credits = tax_unit("az_income_tax_before_credits", period)
        nonrefundable_credits = tax_unit("az_nonrefundable_credits", period)
        return max_(0, tax_before_credits - nonrefundable_credits)
