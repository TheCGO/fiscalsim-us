from fiscalsim_us.model_api import *


class ar_stillborn_child_credit(Variable):
    "Line 5 of form AR1000TC"
    value_type = float
    entity = TaxUnit
    label = "Arkansas Stillborn Child Tax Credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000TC_Schedule_of_TaxCredits_andBusiness_IncentiveCredits.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.ar.tax.income.credits.other_credits

        amount = p.stillbirth_credit

        num = tax_unit("tax_unit_stillborn_children", period)

        return amount * num
