from fiscalsim_us.model_api import *


class mt_agi(Variable):
    """
    Montana adjusted gross income. Line 14 on Montana individual income tax
    return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "MT adjusted gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    adds = ["adjusted_gross_income", "mt_income_additions"]
    subtracts = ["mt_income_subtractions"]
