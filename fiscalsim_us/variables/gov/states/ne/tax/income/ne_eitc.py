from fiscalsim_us.model_api import *


class ne_eitc(Variable):
    value_type = float
    entity = TaxUnit
    label = "NE EITC amount"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.nebraska.gov/files/doc/tax-forms/2021/f_1040n_booklet.pdf"
        "https://revenue.nebraska.gov/files/doc/2022_Ne_Individual_Income_Tax_Booklet_8-307-2022_final_5.pdf"
    )
    defined_for = StateCode.NE

    def formula(tax_unit, period, parameters):
        us_eitc = tax_unit("earned_income_tax_credit", period)
        p = parameters(period).gov.states.ne.tax.income.credits
        return us_eitc * p.eitc.fraction
