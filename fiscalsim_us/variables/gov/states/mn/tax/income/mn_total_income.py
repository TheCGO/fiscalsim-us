from fiscalsim_us.model_api import *


class mn_total_income(Variable):
    """
    TODO: Something here...
    """

    value_type = float
    entity = TaxUnit
    label = "MN total income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    adds = ["adjusted_gross_income", "mn_additions_to_income"]
