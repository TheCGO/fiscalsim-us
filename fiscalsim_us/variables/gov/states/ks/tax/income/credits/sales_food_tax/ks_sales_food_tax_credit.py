from openfisca_us.model_api import *


class ks_sales_food_tax_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS sales food tax credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ks.tax.income.credits.food_sales_tax_credit
        ks_exemptions_claimed = ("ks_exemptions_claimed", period)
        dependents = tax_unit("tax_unit_dependents", period)
        multiplier = p.multiplier
        dep_adults = tax_unit("tax_unit_dependents", period)

        tot_exemptions = ks_exemptions_claimed - dep_adults

        return tot_exemptions * multiplier

#still need to add qualifiers if statement