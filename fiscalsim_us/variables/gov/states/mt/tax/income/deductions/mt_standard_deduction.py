from fiscalsim_us.model_api import *


class mt_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MT standard deduction"
    unit = USD
    definition_period = YEAR
    documentation = "Montana standard deduction"
    reference = (  
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2023/05/Montana-Idividiual-Income-Tax-Return-Form-2-2022v6.2.pdf"
        "https://mtrevenue.gov/wp-content/uploads/dlm_uploads/2022/12/Form-2-2022-Instructions.pdf"
    )
    defined_for = StateCode.MT

    def fomula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mt.tax.income.deductions
        filing_status = tax_unit("filing_status", period)
        line2 = mt_adjusted_gross_income *.2
        line3 = p.standard_deducation_max[filing_status]
        line4 = min(line2,line3)
        line5 = p.standard_deducation_min[filing_status]
        return max (line4, line5)
