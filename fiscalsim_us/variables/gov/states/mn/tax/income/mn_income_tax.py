from policyengine_us.model_api import *


class mn_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN income tax"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.state.mn.us/sites/default/files/2022-12/m1m_22.pdf"
    defined_for = StateCode.MN

    adds = ["mn_income_tax_before_refundable_credits"]
    subtracts = ["mn_refundable_credits"]
