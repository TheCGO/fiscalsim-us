from fiscalsim_us.model_api import *


class id_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Idaho taxable income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_12-30-2022.pdf"
    )
    defined_for = StateCode.ID

    def formula(tax_unit, period, parameters):
        std_ded = tax_unit("id_standard_deduction", period)
        itm_ded = tax_unit("id_itemized_deductions", period)
        deductions = where(itm_ded > std_ded, itm_ded, std_ded)
        exemptions = tax_unit("id_exemptions", period)
        return max_(0, tax_unit("id_agi", period) - deductions - exemptions)
