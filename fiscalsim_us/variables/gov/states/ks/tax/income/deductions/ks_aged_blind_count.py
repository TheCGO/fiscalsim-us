from openfisca_us.model_api import *


class ks_aged_blind_count(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS aged and or blind head and spouse count"
    unit = USD
    definition_period = YEAR
    documentation = "Kansas aged and or blind count"
    reference = "https://www.ksrevenue.gov/pdf/ip21.pdf#page=6"
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states["ks"].tax.income.deductions.standard

        # Aged/blind count for adjusted standard deduction calculation
        # This calculation is the same as the federal aged_blind_count but
        # adjusted for the KS age_threshold
        blind_head = tax_unit("blind_head", period).astype(int)
        blind_spouse = tax_unit("blind_spouse", period).astype(int)
        age_threshold = p.aged_blind.age
        aged_head = (tax_unit("age_head", period) >= age_threshold).astype(int)
        aged_spouse = (tax_unit("age_spouse", period) >= age_threshold).astype(
            int
        )
        aged_blind_count = blind_head + blind_spouse + aged_head + aged_spouse
        return aged_blind_count
