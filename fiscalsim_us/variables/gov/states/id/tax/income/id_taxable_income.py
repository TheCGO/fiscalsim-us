from fiscalsim_us.model_api import *


class id_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "ID taxable income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.ID

    def formula(tax_unit, period, parameters):
        id_agi = tax_unit("id_agi", period)
        deductions_exemptions = add(
            tax_unit, period, ["id_deductions", "id_exemptions"]
        )
        return max_(0, id_agi - deductions_exemptions)
