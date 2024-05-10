from fiscalsim_us.model_api import *


class ar_other_state_credit(Variable):
    "Line 2 of form AR1000TC"
    "Credit for taxes paid to other states on income earned outside of AR"
    value_type = float
    entity = TaxUnit
    label = "Arkansas other state tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR
