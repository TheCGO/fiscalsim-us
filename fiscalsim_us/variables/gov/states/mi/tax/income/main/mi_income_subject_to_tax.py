from fiscalsim_us.model_api import *


class mi_income_subject_to_tax(Variable):
    """
    Line 14 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI income subject to tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI

    def formula(tax_unit, period, parameters):
    total = tax_unit("mi_total_agi", period)
    subtractions = tax_unit("mi_subtractions", period)
    
    return max(0, subtractions - total)