from fiscalsim_us.model_api import *


class la_eitc(Variable):
    """
    Louisiana earned income tax credit
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana EITC"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
    defined_for = StateCode.LA

    def formula(tax_unit, period, parameters):
        federal_eitc = tax_unit("earned_income_tax_credit", period)
        p = parameters(period).gov.states.la.tax.income.credits.refundable_p2

        return federal_eitc * p.eitc_mult
