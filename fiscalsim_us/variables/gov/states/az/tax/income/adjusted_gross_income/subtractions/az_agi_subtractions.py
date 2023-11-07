from fiscalsim_us.model_api import *


class az_agi_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ AGI subtractions"
    unit = USD
    documentation = "Subtractions from AZ AGI over federal AGI."
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    adds = [
        "az_capital_gains_subtractions",
        "tax_unit_taxable_social_security",
    ]
