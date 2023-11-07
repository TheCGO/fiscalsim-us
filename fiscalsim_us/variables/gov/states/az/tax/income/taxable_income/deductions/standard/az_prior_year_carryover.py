from fiscalsim_us.model_api import *


class az_prior_year_carryover(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ proir year carryover of charitable contributions"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ


# line 3C from page 3 of 2022 Form 140
