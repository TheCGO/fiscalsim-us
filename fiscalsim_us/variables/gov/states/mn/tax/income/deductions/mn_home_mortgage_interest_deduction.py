from fiscalsim_us.model_api import *


class mn_home_mortgage_interest_deduction(Variable):
    """
    Other itemized deductions from for M1SA lines 11 and 12
    Can only deduct interest from $750,000-$1,000,000 of the loan
    depending on when the loan was take out
    """

    value_type = float
    entity = TaxUnit
    label = "MN home mortgage interest deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
    # use federal variable once it is made
