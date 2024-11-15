from fiscalsim_us.model_api import *


class ar_other_income(Variable):
    "AR-OI form"
    """
    Additions to income include:
    Federal Depreciation
    HSA/MSA taxable distributions
    Long-term care insurance contracts
    Gambling Winnings
    Lottery/Contest Winnings
    Scholarships/fellowships/stipends
    Pass Through Entity Adjustment

    Subtractions from Income include:
    State Depreciation
    Net operating loss
    Foreign earned income exclusion
    Pass Through Entity Adjustment
    Other
    """

    value_type = float
    entity = Person
    label = "Arkansas other income"
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf#page=10"
    defined_for = StateCode.AR
    unit = USD
    definition_period = YEAR
