from fiscalsim_us.model_api import *


class mt_count_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "number of MT exemptions"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://leg.mt.gov/bills/mca/title_0150/chapter_0300/part_0210/section_0140/0150-0300-0210-0140.html"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/05/Montana-Idividiual-Income-Tax-Return-Form-2-2022v6.2.pdf"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2022/12/Form-2-2022-Instructions.pdf"
    )
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        statuses = filing_status.possible_values
        joint = filing_status == statuses.JOINT
        adults = where(joint, 2, 1)
        dependents = tax_unit("tax_unit_dependents", period)
        aged_blind_count = tax_unit("aged_blind_count", period)

        return adults + dependents + aged_blind_count
