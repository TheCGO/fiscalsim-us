from fiscalsim_us.model_api import *


class la_nonrefundable_priority_3_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana nonrefundable priority 3 income tax credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
    adds = "gov.states.la.tax.income.credits.nonrefundable_p3.sources"
