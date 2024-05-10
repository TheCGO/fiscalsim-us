from fiscalsim_us.model_api import *


class ar_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas adjusted gross income"
    defined_for = StateCode.AR
    unit = USD
    definition_period = YEAR
    # Arkansas Code
    reference = "https://law.justia.com/codes/arkansas/2019/title-26/subtitle-5/chapter-51/subchapter-4/section-26-51-403/"

    adds = ["ar_total_income", "ar_capital_loss_adjustment"]
    subtracts = ["ar_income_adjustments"]
