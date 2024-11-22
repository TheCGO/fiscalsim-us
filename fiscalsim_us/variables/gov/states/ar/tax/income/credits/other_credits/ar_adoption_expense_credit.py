from fiscalsim_us.model_api import *


class ar_adoption_expense_credit(Variable):
    "Line 3 of form AR1000TC"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Adoption Expense Credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR


def formula(tax_unit, period, parameters):
    p = parameters(period).gov.states.ar.income.credits.other_credits

    match = p.adoption_credit

    return match * tax_unit("qualified_adoption_expenses", period)
