from fiscalsim_us.model_api import *


class ks_sales_food_tax_credit_qualifiers(Variable):
    value_type = float
    entity = TaxUnit
    label = "KS sales food tax credit qualifiers"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ks.tax.income.credits.food_sales_tax_credit
        dependents = tax_unit("tax_unit_dependents", period)
        age_spouse = tax_unit("age_spouse", period)
        age_head = tax_unit("age_head", period)
        disabled_head = tax_unit("disabled_head", period)
        disabled_spouse = tax_unit("disabled_spouse", period)
        blind_head = tax_unit("blind_head", period)
        blind_spouse = tax_unit("blind_spouse", period)
        age = p.age
        agi_threshold = p.age_threshold
        federal_agi = tax_unit("adjusted_gross_income", period)

#this if statement answeres whether or not a taxpayer qualifies for the 
#KS sales food tax credit. 1 = Quailified; 0 = Disqualified

        if (dependents >= 1 or
                age_spouse >= age or
                age_head >= age or
                disabled_head == 1 or
                disabled_spouse == 1 or
                blind_head == 1 or
                blind_spouse == 1 and
                federal_agi <= agi_threshold):
            1
        else:
            0