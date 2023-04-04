from fiscalsim_us.model_api import *


class non_mn_bond_interest(Variable):
    """
    State and municipal bond interest from outside Minnesota
    not included in fed Form 6251
    Line 5 Minnesota 2022 form M1MT, Alternative Minimum Tax
    """

    value_type = float
    entity = TaxUnit
    label = "Non MN state and municipal bond interest"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
