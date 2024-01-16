from fiscalsim_us.model_api import *


class ar_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arkansas Child and Dependent Care Credit"
    unit = USD
    documentation = "https://codes.findlaw.com/ar/title-26-taxation/ar-code-sect-26-51-502/"
    definition_period = YEAR
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ar.tax.income.credits.cdcc
        cdcc = tax_unit("cdcc", period)
        return cdcc * p.match

        # filing_status = tax_unit('filing_status',period) #Needed?

        # gross_num_eligible = tax_unit.sum(
        #     tax_unit.members("ar_cdcc_qualified_dependent", period)
        # )

        # max_qual_expenses = where(gross_num_eligible >= 2, p.childcare_qual_max *2, p.childcare_qual_max)

        # qualified_expenses = min(tax_unit('tax_unit_qualified_expenses', period), max_qual_expenses)

        # earned_income_head = tax_unit('ar_cdcc_earned_income_head', period) #NOT FINALIZED
        # earned_income_spouse = tax_unit('ar_cdcc_earned_income_spouse', period) #NOT FINALIZED

        # base_amount = min(qualified_expenses, earned_income_head, earned_income_spouse)
        
        # fed_agi = tax_unit('adjusted_gross_income', period)

        # childcare_credit =  p.childcare_rates[fed_agi] * base_amount


        
        # return childcare_credit