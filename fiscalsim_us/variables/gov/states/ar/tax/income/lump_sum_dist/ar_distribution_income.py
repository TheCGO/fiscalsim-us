from fiscalsim_us.model_api import *


class ar_distribution_income(Variable):
    """Line 31 of form AR1000F
    Line 1 of form AR1000TD"""

    value_type = float
    entity = TaxUnit
    label = "Arkansas Lump Sum Distribution  Income"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TD_LumpSumDistributionAveraging.pdf"
    defined_for = StateCode.AR
