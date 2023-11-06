from fiscalsim_us.model_api import *


class az_agi_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ AGI additions"
    unit = USD
    documentation = "Additions to AZ AGI over federal AGI."
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    # No additions modeled in FiscalSim US.
