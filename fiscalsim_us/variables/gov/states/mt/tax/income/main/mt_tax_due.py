from fiscalsim_us.model_api import *


class mt_tax_due(Variable):
    """
    Line 26 on Montana state individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana tax due"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT


def formula(tax_unit, period, parameters):
    line20 = tax_unit("mt_tax_after_nonrefundable_credits")
    line25 = tax_unit("mt_total_payments")

    return where(line25 < line20, line20 - line25, 0)
