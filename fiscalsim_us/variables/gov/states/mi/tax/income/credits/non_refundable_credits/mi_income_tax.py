from fiscalsim_us.model_api import *


class mi_income_tax(Variable):
    """
    Line 20 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI income tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI

    def formula(tax_unit, period, parameters):
        imposed = tax_unit("mi_income_tax_imposed_by_other_gov_credit")
        historic = tax_unit("mi_historic_preservation_amount")
        tax = tax_unit("mi_income_tax_before_credits")
        credit = imposed + historic
        return max(0, credit - tax)