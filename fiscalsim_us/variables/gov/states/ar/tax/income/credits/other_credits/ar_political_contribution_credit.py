from fiscalsim_us.model_api import *


class ar_political_contribution_credit(Variable):
    "Line 1 of form AR1000TC"
    value_type = float
    entity = TaxUnit
    label = "Arkansas political contribution tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR


def formula(tax_unit, period, parameters):
    p = parameters(period).gov.states.ar.tax.income.credits.other_credits
    cap = p.political_contrib
    contributions = tax_unit("ar_political_contributions")

    return min_(cap, contributions)
