from fiscalsim_us.model_api import *


class ks_income_tax_before_credits(Variable):
    """
    Line 12 on Kansas 2022 Individual Income Tax return form K-40.
    
    """
    value_type = float
    entity = TaxUnit
    label = "Kansas Income Tax Before Credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        income_tax = tax_unit("ks_income_tax_before_additional_taxes", period)
        additional_taxes = tax_unit("ks_additional_taxes", period)

        return (
            income_tax + additional_taxes
        )