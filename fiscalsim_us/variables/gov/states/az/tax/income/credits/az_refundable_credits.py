from fiscalsim_us.model_api import *


class az_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ refundable credits"
    unit = USD
    documentation = (
        "AZ refundable credits added on lines 56, 57, and 58 of form 140"
    )
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR
