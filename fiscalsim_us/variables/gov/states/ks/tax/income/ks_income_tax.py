from fiscalsim_us.model_api import *


class ks_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS total income tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

# this is the final tax balance found on line 21 of the KS K-40

    def formula(tax_unit, period, parameters):
        tax_before = tax_unit("ks_income_tax_before_credits", period)
        credits = tax_unit("ks_total_credits", period)
        use_tax = tax_unit("ks_use_tax", period)
        balance_after_credits = max(tax_before - credits, 0)

        return balance_after_credits + use_tax

