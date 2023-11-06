from fiscalsim_us.model_api import *


class az_aged_blind_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ additional exemption for aged or blind"
    unit = USD
    documentation = (
        "Exemptions from AZ AGI for spouse and filers aged and or blind."
    )
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):

        # Aged/blind exemption
        p = parameters(period).gov.states["az"].tax.income.exemptions
        blind_head = tax_unit("blind_head", period).astype(int)
        blind_spouse = tax_unit("blind_spouse", period).astype(int)
        age_threshold = p.age_threshold
        aged_amount = p.aged_amount
        blind_amount = p.blind_amount
        aged_head = (tax_unit("age_head", period) >= age_threshold).astype(int)
        aged_spouse = (tax_unit("age_spouse", period) >= age_threshold).astype(
            int
        )
        aged_count = aged_head + aged_spouse
        blind_count = blind_head + blind_spouse

        aged_exemption = aged_count * aged_amount
        blind_exemption = blind_count * blind_amount

        return aged_exemption + blind_exemption
