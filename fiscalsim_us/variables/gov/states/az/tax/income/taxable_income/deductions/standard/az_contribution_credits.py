from fiscalsim_us.model_api import *


class az_contribution_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ charitable contribution credits"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

# line 5C from page 3 of 2022 Form 140
# This variable reduces the amount of standard
# deduction increase from charitable contributions
