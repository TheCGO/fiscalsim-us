from fiscalsim_us.model_api import *


class la_refundable_childcare(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana refundable childcare credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf"
    )

    def formula(tax_unit, period, parameters):

        p = parameters(period).gov.states.la.tax.income.credits.refundable_p2
        agi = tax_unit("adjusted_gross_income", period)
        earned_income = tax_unit("tax_unit_earned_income", period)
        childcare_expenses = tax_unit("tax_unit_childcare_expenses", period)

        # check for eligible children 
        person = tax_unit.members
        dependent = person("is_tax_unit_dependent", period)
        age = person("age", period)
        child = age < p.childcare_child_age_limit
        eligible = dependent & child
        eligible_children = tax_unit.sum(eligible_child)

        max_expense = p.childcare_expense_limit.calc(eligible_children)
        expense = min_(childcare_expenses, max_expense)

        # line 6 of worksheet 
        credit = min_(expense, earned_income)

        income_mult = p.childcare_income_mult.calc(agi)
        mult = p.refundable_childcare_mult

        return credit * income_mult * mult
