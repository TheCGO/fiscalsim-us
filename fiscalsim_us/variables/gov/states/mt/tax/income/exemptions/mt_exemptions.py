from fiscalsim_us.model_api import *


class mt_exemptions(Variable):
    """
    Line 16 on Montana state individual tax return form 2
    """
    value_type = float
    entity = TaxUnit
    label = "Montana exemptions amount"
    unit = USD
    definition_period = YEAR
    reference = (
       "https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0140/0150-0300-0210-0140.html"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/05/Montana-Idividiual-Income-Tax-Return-Form-2-2022v6.2.pdf"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2022/12/Form-2-2022-Instructions.pdf"
    )
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        num_exemptions = tax_unit("mt_count_exemptions", period)
        p = parameters(period).gov.states.mt.tax.income.exemptions
        return num_exemptions * p.exemption