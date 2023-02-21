from fiscalsim_us.model_api import *
from fiscalsim_us.variables.gov.states.mn.tax.income.deductions.mn_standard_deduction import mn_standard_deduction


class mn_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN exemptions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.state.mn.us/sites/default/files/2021-12/m1m_21.pdf"
    defined_for = StateCode.MN
    adds = ["mn_income_tax_before_refundable_credits"]
    subtracts = ["mn_refundable_credits"]
