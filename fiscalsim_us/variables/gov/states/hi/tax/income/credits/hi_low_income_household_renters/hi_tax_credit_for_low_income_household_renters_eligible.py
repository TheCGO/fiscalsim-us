from fiscalsim_us.model_api import *


class hi_tax_credit_for_low_income_household_renters_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Eligible for the Hawaii low income household renters tax credit"
    definition_period = YEAR
    reference = "https://files.hawaii.gov/tax/legal/har/har_235.pdf#page=105"  # §18-235-55.7 (b)
    defined_for = StateCode.HI

    def formula(tax_unit, period, parameters):
        dependent_on_another_return = tax_unit("dsi", period)
        p = parameters(period).gov.states.hi.tax.income.credits.lihrtc
        agi = tax_unit("adjusted_gross_income", period)
        rent = add(tax_unit, period, ["rent"])
        return (
            (rent > p.eligibility.rent_threshold)
            & (agi < p.eligibility.agi_limit)
            & ~dependent_on_another_return
        )
