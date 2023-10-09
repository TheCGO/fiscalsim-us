from fiscalsim_us.model_api import *


class la_total_subtractions(Variable):
    """
    Subtractions from louisiana adjusted income
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana total subtractions from AGI"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    adds = "gov.states.la.tax.income.agi.subtractions.sources"
