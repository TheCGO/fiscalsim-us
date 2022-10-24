from policyengine_us.model_api import *


class school_meal_countable_income(Variable):
    value_type = float
    entity = SPMUnit
    definition_period = YEAR
    unit = USD
    label = "Countable income for school meals"
    documentation = "SPM unit's countable income for school meal program"

    def formula(spm_unit, period, parameters):
        sources = parameters(period).gov.usda.school_meals.income.sources
        return aggr(spm_unit, period, sources)
