from fiscalsim_us.model_api import *


class mi_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Michigan taxable income"
    defined_for = StateCode.MI
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
    income = tax_unit("mi_income_subject_to_tax")
    exemption = tax_unit("mi_exemptions")
    return max(0,exemption-income)
