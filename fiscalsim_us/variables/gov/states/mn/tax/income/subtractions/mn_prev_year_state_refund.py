from fiscalsim_us.model_api import *


class mmn_prev_year_state_refund(Variable):
    """
    Line 6 of Minnesota 2023 Individual Income Tax return from M1. This is the
    State income refund from a previous year that was reported in line 1 of
    Schedule 1 (Form 1040) of the federal return.
    """

    value_type = float
    entity = TaxUnit
    label = "MN other subtrations from income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2023-12/m1-23.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2024-02/m1-inst-23.pdf"
        "https://www.irs.gov/pub/irs-pdf/f1040s1.pdf"
    )
    defined_for = StateCode.MN
