from fiscalsim_us.model_api import *


class mn_total_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN total income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.state.mn.us/sites/default/files/2021-12/m1_21_0.pdf"
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        federal_agi = tax_unit("adjusted_gross_income", period)
        mn_additions = tax_unit("mn_additions_to_income", period)

        return federal_agi + mn_additions