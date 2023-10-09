from fiscalsim_us.model_api import *


class la_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana income tax"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
    defined_for = StateCode.LA
    adds = ["la_income_tax_before_refundable_credits"]
    subtracts = ["la_refundable_credits"]
