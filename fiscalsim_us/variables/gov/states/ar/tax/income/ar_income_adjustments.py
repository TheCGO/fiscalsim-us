from fiscalsim_us.model_api import *


class ar_income_adjustments(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas adjustments to total income to calculate AR AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000ADJ_AdjustmentsSchedule.pdf"
        "https://law.justia.com/codes/arkansas/2019/title-26/subtitle-5/chapter-51/subchapter-4/section-26-51-403/"
    )
    defined_for = StateCode.AR