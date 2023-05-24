from fiscalsim_us.model_api import *


class mn_taxable_income(Variable):
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
    )
    defined_for = StateCode.MN
    adds = ["adjusted_gross_income", "mn_additions"]
    subtracts = ["mn_subtractions", "mn_exemptions", "mn_deductions"]
