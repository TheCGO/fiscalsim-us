from openfisca_us.model_api import *


class ks_sales_food_tax_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS sales food tax credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ks.tax.income.credits
        ks_exemptions_claimed = tax_unit("ks_exemptions_claimed", period)
        dependents = tax_unit("tax_unit_dependents", period)
        multiplier = p.ks_food_sales_tax_credit_multiplier

        line_g = ks_exemptions_claimed - dependents

        return line_g * multiplier

#still need to add qualifiers for credit