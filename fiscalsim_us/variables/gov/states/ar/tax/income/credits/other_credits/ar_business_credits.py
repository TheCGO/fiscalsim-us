from fiscalsim_us.model_api import *


class ar_business_credits(Variable):
    "Line 8 of form AR1000TC"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Business Incentive Credits"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR
