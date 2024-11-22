from fiscalsim_us.model_api import *


class mn_additions(Variable):
    """
    Line 2 of form M1 (2023) andline 10 of schedule M1M and line 9 of Schedule
    M1MB
    """

    value_type = float
    entity = TaxUnit
    label = "Minnesota additions to federal AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.taxformfinder.org/forms/2021/2021-minnesota-form-m1m.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1m_22.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-12/m1m-23.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2024-01/m1mb-23.pdf"
    )
    defined_for = StateCode.MN
    adds = "gov.states.mn.tax.income.additions.sources"
