from fiscalsim_us.model_api import *


class az_parents_grandparents_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ additional exemption for qualifyting parents and grandparents"
    unit = USD
    documentation = "Arizona income tax form 140"
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR
