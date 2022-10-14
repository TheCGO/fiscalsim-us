from fiscalsim_us.model_api import *


class va_tax_owed_or_refunded(Variable):
    value_type = float
    entity = TaxUnit
    label = "line 26 on the va tax return form 760"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit,period,parameters):

        net_tax = tax_unit("va_net_amount_of_tax",period)

        line_26 = tax_unit("va_line_26",period)

        if line_26 < net_tax:

            owed_tax = net_tax - line_26 

            return owed_tax

        if net_tax < line_26: 

            refund = line_26 - net_tax 

            return refund


