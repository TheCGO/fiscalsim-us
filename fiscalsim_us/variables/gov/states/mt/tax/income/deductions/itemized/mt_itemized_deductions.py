from fiscalsim_us.model_api import *


class mt_itemized_deduction(Variable):
    """
    See itemized deduction schedule on page 7 of the Montana individual tax return form 2 for how to calculate
    Line 15 on Montana individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "MT itemized deduction"
    unit = USD
    definition_period = YEAR
    documentation = "Montana itemized deduction"
    reference = (
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/05/Montana-Idividiual-Income-Tax-Return-Form-2-2022v6.2.pdf"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2022/12/Form-2-2022-Instructions.pdf"
    )
    defined_for = StateCode.MT

    adds = "gov.states.mt.tax.income.deductions.itemized.itemized_deductions"
