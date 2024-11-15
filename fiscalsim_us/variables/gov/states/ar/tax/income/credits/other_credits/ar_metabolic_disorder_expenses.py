from fiscalsim_us.model_api import *


class ar_metabolic_disorder_expenses(Variable):
    "Line 4 of form AR1000TC"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Phenylketonuria Disorder expenses"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR
