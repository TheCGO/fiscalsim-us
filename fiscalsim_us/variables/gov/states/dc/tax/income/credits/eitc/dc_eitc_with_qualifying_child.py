from fiscalsim_us.model_api import *


class dc_eitc_with_qualifying_child(Variable):
    value_type = float
    entity = TaxUnit
    label = "DC EITC with qualifying children"
    unit = USD
    definition_period = YEAR
    reference = "https://code.dccouncil.gov/us/dc/council/code/sections/47-1806.04"  # (f)
    defined_for = StateCode.DC

    def formula(tax_unit, period, parameters):
        us_eitc = tax_unit("earned_income_tax_credit", period)
        p = parameters(period).gov.states.dc.tax.income.credits
        return us_eitc * p.eitc.with_children.match
