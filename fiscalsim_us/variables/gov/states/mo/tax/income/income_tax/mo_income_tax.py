from fiscalsim_us.model_api import *


class mo_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "Missouri income tax"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.mo.gov/forms/MO-1040%20Instructions_2021.pdf",
        "https://www.revisor.mo.gov/main/OneChapter.aspx?chapter=143",
        "https://revisor.mo.gov/main/OneSection.aspx?section=135.020&bid=6437",
        "https://revisor.mo.gov/main/OneSection.aspx?section=143.177&bid=49978&hl=",
    )
    defined_for = StateCode.MO
    # mo_property_tax_credit is refundable, per pg.17 of: https://dor.mo.gov/forms/4711_2021.pdf and the last reference above.

    adds = ["mo_income_tax_before_refundable_credits"]
    subtracts = ["mo_refundable_credits"]
