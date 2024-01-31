from fiscalsim_us.model_api import *


class ar_metabolic_disorder_credit(Variable):
    "Line 4 of form AR1000TC"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Phenylketonuria Disorder Credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR

def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.ar.income.credits.other_credits
        
        maximum_credit = p.metabolic

        tax_due = tax_unit('ar_income_tax_before_non_refundable_credits', period) 
        - tax_unit('ar_personal_credits', period) - tax_unit('ar_political_contribution_credit',period)
        - tax_unit('ar_other_state_credit', period) - tax_unit('ar_adoption_expense_credit', period) - tax_unit('ar_stillborn_child_credit')