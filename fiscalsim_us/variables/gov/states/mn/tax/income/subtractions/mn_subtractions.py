from fiscalsim_us.model_api import *


class mn_subtractions(Variable):
    """
    Line 7 of form M1 (2023)
    """

    value_type = float
    entity = TaxUnit
    label = "Minnesota subtractions from federal AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2021-12/m1_21_0.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1_inst_21.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2022-12/m1_22.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-03/m1_inst_22.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-12/m1-23.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2024-02/m1-inst-23.pdf"
    )
    defined_for = StateCode.MN
    adds = "gov.states.mn.tax.income.subtractions.sources"
