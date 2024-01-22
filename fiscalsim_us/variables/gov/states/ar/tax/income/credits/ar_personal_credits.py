from fiscalsim_us.model_api import *


class ar_personal_credits(Variable):
    "Line 7A - 7D, 34 of form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas personal tax credit"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000F_FullYearResidentIndividualIncomeTaxReturn.pdf"
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        personal_credit_amount = parameters(period).gov.states.ar.tax.income.credits.personal.personal_credit_amount
        filing_status = tax_unit("filing_status", period)
        married_status = filing_status.possible_values.JOINT
        self_and_spouse_credit = where(filing_status == married_status, 2, 1) * personal_credit_amount


        blind_head = tax_unit("blind_head", period).astype(int)
        blind_spouse = tax_unit("blind_spouse", period).astype(int) * 1
        blind_credit = (blind_head + blind_spouse) * personal_credit_amount

        age_threshold = parameters(period).gov.states.ar.tax.income.credits.personal.age_threshold
        aged_head = where(tax_unit("age_head", period).astype(int)>=age_threshold,1,0)
        aged_spouse = where(tax_unit("age_spouse", period).astype(int)>=age_threshold,1,0)
        aged_credit = (aged_head + aged_spouse) * personal_credit_amount

        head_retirement_income = tax_unit('ar_head_retirement_income', period) # Probably not implemented correctly
        spouse_retirement_income = tax_unit('ar_spouse_retirement_income', period)
        aged_special_head = where(aged_head == 1 and head_retirement_income <= 0, 1, 0)
        aged_special_spouse = where(aged_spouse == 1 and spouse_retirement_income <= 0, 1, 0)

        aged_special_credit = (aged_special_head + aged_special_spouse) * personal_credit_amount


        # I created "is_deaf", "deaf_head", and "deaf_spouse" myself
        deaf_head = tax_unit("deaf_head", period).astype(int)
        deaf_spouse = tax_unit("deaf_spouse", period).astype(int) * 1
        deaf_credit = (deaf_head + deaf_spouse) * personal_credit_amount


        hoh_status = filing_status.possible_values.HEAD_OF_HOUSEHOLD or filing_status.possible_values.WIDOW
        hoh_credit = where(filing_status == hoh_status, 1, 0) * personal_credit_amount


        personal_credit = self_and_spouse_credit + blind_credit + aged_credit + aged_special_credit + deaf_credit + hoh_credit





        dependents = tax_unit("tax_unit_dependents", period)
        dependent_credit_amount  = parameters(period).gov.states.ar.tax.income.credits.personal.dependents
        dependent_credit = dependents *dependent_credit_amount


        qual_dependents = tax_unit("ar_qual_dependents", period) # Probably not implemented correctly
        qual_dependent_credit_amount  = parameters(period).gov.states.ar.tax.income.credits.personal.qual_dependents
        qual_dependent_credit = qual_dependent_credit_amount * qual_dependents



        return personal_credit + dependent_credit + qual_dependent_credit