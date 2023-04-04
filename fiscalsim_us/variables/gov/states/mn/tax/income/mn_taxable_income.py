from fiscalsim_us.model_api import *


class mn_taxable_income(Variable):
    """
    TODO: SOMETHING HERE
    """

    value_type = float
    entity = TaxUnit
    label = "MN taxable income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    adds = ["adjusted_gross_income", "mn_additions_to_income"]
    subtracts = ["mn_subtractions_from_income"]
