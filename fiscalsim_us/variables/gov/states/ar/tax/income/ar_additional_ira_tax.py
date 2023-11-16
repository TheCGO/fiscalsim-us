from fiscalsim_us.model_api import *


class ar_additional_ira_tax(Variable):
    "2022 AR 1000F instructions Line 32, 10% of federal amount from form 5329"

    value_type = float
    entity = TaxUnit
    label = "Additional tax on IRA and qualified plan withdrawal and overpayment"
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_and_AR1000NR_Instructions.pdf#page=10"
    defined_for = StateCode.AR
    unit = USD
    definition_period = YEAR