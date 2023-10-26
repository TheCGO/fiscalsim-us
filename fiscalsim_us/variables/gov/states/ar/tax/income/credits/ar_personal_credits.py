from fiscalsim_us.model_api import *


class ar_income_tax_before_non_refundable_credits(Variable):
    "Line 7A - 7D of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas personal tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        personal_credit_amount = parameters(period).gov.states.ar.tax.income.credits.personal.personal_credit_amount
        boxes_checked = tax_unit("placeholder", period)
        personal_credit = personal_credit_amount * boxes_checked

        dependents = tax_unit("tax_unit_dependents", period)
        dependent_credit_amount  = parameters(period).gov.states.ar.tax.income.credits.personal.dependents
        dependent_credit = dependents *dependent_credit_amount

        
        qual_dependents = tax_unit("placeholder", period)
        qual_dependent_credit_amount  = parameters(period).gov.states.ar.tax.income.credits.personal.qual_dependents
        qual_dependent_credit = qual_dependent_credit_amount * qual_dependents



        return personal_credit + dependent_credit + qual_dependent_credit