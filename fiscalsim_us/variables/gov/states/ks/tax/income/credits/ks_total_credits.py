from openfisca_us.model_api import *

#Total of all credits for Kansas
class ks_sales_food_tax_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS sales food tax credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        other_credits = tax_unit("ks_other", period)
        other_states = tax_unit("ks_other_states", period)
        eitc = tax_unit("ks_eitc", period)
        sales_food = tax_unit("ks_sales_food_tax_credit", period)
        child_care = tax_unit("ks_child_care", period)

        return other_credits + other_states + eitc + sales_food + child_care

#still need to add qualifiers if statement