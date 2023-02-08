from fiscalsim_us.model_api import *


class md_socsec_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MD social security subtraction from AGI"
    unit = USD
    definition_period = YEAR
    reference = "https://www.marylandtaxes.gov/forms/21_forms/Resident_Booklet.pdf#page=14"
    defined_for = StateCode.MD
    adds = ["md_socsec_subtraction_amount"]
