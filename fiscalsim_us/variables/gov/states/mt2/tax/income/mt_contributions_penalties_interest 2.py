from fiscalsim_us.model_api import *


class mt_contributions_penalties_interest(Variable):
    """
    Line 24 on Montana individual income tax retrun form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana contributions penatlites and interest"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
