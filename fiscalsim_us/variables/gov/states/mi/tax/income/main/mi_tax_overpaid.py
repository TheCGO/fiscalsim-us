from fiscalsim_us.model_api import *


class mi_tax_overpaid(Variable):
    """
    Line 35 on Michigan tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "Michigan Tax Overpayed"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI


def formula(tax_unit, period, parameters):
    line33 = tax_unit("mi_total_refundable_credits")
    line24 = tax_unit("mi_total_tax_liability")

    return where(line33 > line24, line24 - line33, 0)