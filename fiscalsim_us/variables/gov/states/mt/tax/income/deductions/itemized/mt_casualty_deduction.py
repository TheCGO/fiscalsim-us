from fiscalsim_us.model_api import *


class mt_casualty_loss_deduction(Variable):
    """
    Line 15 on Montana itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana casualty and theft losses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        deduction = (tax_unit, period, ["casualty_loss_deduction"])

        return deduction
