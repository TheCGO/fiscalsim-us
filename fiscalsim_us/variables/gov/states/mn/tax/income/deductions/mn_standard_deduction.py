from symbol import yield_arg
from fiscalsim_us.model_api import *


class mn_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN standard deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.deductions.standard
        filing_status = tax_unit("filing_status", period)

        # in the M1 tax worksheet, 'how many boxes are checked'
        you_p65 = (tax_unit("age_head", period) >= 65 ).astype(int)
        spouse_p65 = (tax_unit("age_spouse", period) >=  65 ).astype(int)
        you_blind = tax_unit("blind_head", period).astype(int)
        spouse_blind = tax_unit("blind_spouse", period).astype(int)

        if filing_status in ["Joint", "Head of household"]:
            num_box_checked = sum(you_p65, you_blind, spouse_p65, spouse_blind)
        else:
            num_box_checked = sum(you_p65, you_blind)

        # look over this again...
        std_deduct_table = p.amount[f"{num_box_checked}_box"]
        std_deduct = std_deduct_table[filing_status]
        federal_agi = tax_unit("adjusted_gross_income", period)
        income_limit = p.limitation_threshold[filing_status]
        
        if federal_agi <= income_limit:
            return std_deduct
        
        # this is for tax units over the income limit, using the M1 tax worksheet for line 4
        income_over_limit = federal_agi - income_limit * p.extra_income_mult
        sub_deduct = std_deduct * p.standard_deduct_over_threshold_mult 
        return std_deduct - min(income_over_limit, sub_deduct)