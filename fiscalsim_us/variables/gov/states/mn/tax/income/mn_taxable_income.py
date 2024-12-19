from fiscalsim_us.model_api import *


class mn_taxable_income(Variable):
    """
    Line 9 from form M1 (2023)
    """

    value_type = float
    entity = TaxUnit
    label = "Minnesota taxable income"
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

    def formula(tax_unit, period, parameters):
        ADDS = ["adjusted_gross_income", "mn_additions"]
        SUBTRACTS = [
            "mn_subtractions",
            "mn_prev_year_state_refund",
            "mn_exemptions",
            "mn_deductions",
        ]

        income = add(tax_unit, period, ADDS) - add(tax_unit, period, SUBTRACTS)
        return max_(0, income)
