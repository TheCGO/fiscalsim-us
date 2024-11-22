from fiscalsim_us.model_api import *


class ar_nonqualified_ira_distributions(Variable):
    """
    AR1000F Line 16
    """

    value_type = float
    entity = Person
    label = "Arkansas nonqualified ira and annuity distributions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000D_CapitalGains.pdf"
    defined_for = StateCode.AR
