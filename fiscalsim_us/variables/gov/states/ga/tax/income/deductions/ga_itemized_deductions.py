from fiscalsim_us.model_api import *


class ga_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia itemized deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.GA

    def formula(tax_unit, period, parameters):
        federal_itemized = tax_unit("itemized_deductions_less_salt", period)
        adjustments = tax_unit("ga_itemized_adjustments", period)

        return federal_itemized - adjustments
