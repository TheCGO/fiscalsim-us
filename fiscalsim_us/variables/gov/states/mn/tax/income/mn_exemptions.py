from fiscalsim_us.model_api import *


class mn_exemptions(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN exemptions"
    unit = USD
    definition_period = YEAR
    reference = "https://www.revenue.state.mn.us/sites/default/files/2021-12/m1m_21.pdf"
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        P = parameters(period).gov.states.mn.tax.income.exemptions
        federal_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)

        num_dependents = tax_unit("tax_unit_dependents", period)
        exemption = num_dependents * P.amount

        # if income is less than the phase out limit, return the whole exemption amount
        phase_out = P.threshold[filing_status]
        if federal_agi < phase_out:
            return exemption

        # for agi above a the upper limit return no exemption
        agi_over_limit = federal_agi - P.threshold[filing_status] 
        if agi_over_limit > P.upper_limit[filing_status]:
            return 0
        
        # exemption phases out for incomes less than the upper threshold
        return exemption - (round(agi_over_limit/P.phase_out_divisor) * P.phase_out_mult)
        
        