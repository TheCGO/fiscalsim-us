from fiscalsim_us.model_api import *


class mt_eitc(Variable):
    """
    Line 23b on Montana individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana EITC amount"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/05/Montana-Idividiual-Income-Tax-Return-Form-2-2022v6.2.pdf"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2022/12/Form-2-2022-Instructions.pdf"
    )
    defined_for = StateCode.MT


def formula(tax_unit, period, parameters):
    p = parameters(period).gov.states.mt.tax.income.credits
    federaleitc = tax_unit("earned_income_tax_credit", period)

    return federaleitc * p.eitc
