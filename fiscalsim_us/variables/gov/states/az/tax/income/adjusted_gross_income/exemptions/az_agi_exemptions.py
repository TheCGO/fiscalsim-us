from fiscalsim_us.model_api import *


class az_agi_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ AGI exemptions"
    unit = USD
    documentation = "Exemptions from AZ AGI over federal AGI."
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        aged_blind = tax_unit("az_aged_blind_exemption", period)
        parents_grandparents = tax_unit(
            "az_parents_grandparents_exemption", period
        )
        other = tax_unit("az_other_exemptions", period)

        return aged_blind + parents_grandparents + other
