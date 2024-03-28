from fiscalsim_us.model_api import *


class ar_actuarial_value(Variable):
    """Line 31 of form AR1000F
    Line 2 of form AR1000TD"""

    value_type = float
    entity = TaxUnit
    label = "Arkansas Lump Sum Distribution - Actuarial Value"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TD_LumpSumDistributionAveraging.pdf"
    defined_for = StateCode.AR
