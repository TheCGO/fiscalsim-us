from fiscalsim_us.model_api import *


class ar_qual_dependents(Variable):
    "Line 7C of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Qualifying Dependents"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR