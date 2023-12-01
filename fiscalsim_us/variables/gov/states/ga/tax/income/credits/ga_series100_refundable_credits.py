from fiscalsim_us.model_api import *


class ga_series100_refundable_credits(Variable):
    """
    Georgia refundable Series 100 tax credits.
    These credits are claimed using the Form 500 Schedule 2b.
    A tax unit may only claim series 100 tex credits if they
    file online.
    Currently (in 2022) the only refundable series 100 tax credit
    is the Timber Tax Credit (145).
    """

    value_type = float
    entity = TaxUnit
    label = "Georgia series 100 refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.GA
