from fiscalsim_us.model_api import *


class la_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
    defined_for = StateCode.LA

    def formula(tax_unit, period, parameters):
        itax_before_credits = tax_unit("la_income_tax_before_credits", period)
        nonrefundable_credits = tax_unit("la_nonrefundable_credits", period)
        return max_(0, itax_before_credits - nonrefundable_credits)
