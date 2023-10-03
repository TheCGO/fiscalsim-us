from fiscalsim_us.model_api import *


class mt_total_payments(Variable):
    """
    Line 25 on Montana individual income tax retrun form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana total payments"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    adds = ["mt_refundable_credits", "mt_eitc"]
    subtracts = ["mt_contributions_penalties_interest"]
