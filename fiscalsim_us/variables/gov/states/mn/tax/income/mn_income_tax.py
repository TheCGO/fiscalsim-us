from tkinter import W
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

    def formula(tax_unit, period, parameters):
        agi = tax_unit("mn_total_income", period)
        deductions = max(tax_unit("mn_standard_deduction", period), 
                        tax_unit("mn_itemized_deduction", period))
        exemptions = tax_unit("mn_exemptions", period)
        subtractions = 0 # need to figure this out

        taxable_income = max(0, agi - deductions - exemptions - subtractions)
        tax = 0 # figure out how to code up the whole table  

        # need to worry about part- time residents?
        tax += 0 # place for other tax M1HOME, M1529, M1LS
        
        non_refund_credit = 0
        refund_credit = 0
        tax = max(0, tax - non_refund_credit)
        return tax - refund_credit

