from fiscalsim_us.model_api import *


class va_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "line 26 on the va tax return form 760"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        net_tax = tax_unit("va_income_tax_before_refundable_credits", period)
        line_26 = tax_unit("va_refundable_credits", period)

        owed_tax = where(line_26 < net_tax, net_tax - line_26, 0)
        refund = where(net_tax < line_26, (line_26 - net_tax) * -1, 0)

        return owed_tax + refund
