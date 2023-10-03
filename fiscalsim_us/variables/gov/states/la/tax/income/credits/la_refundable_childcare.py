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
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.la.tax.income.credits.refundable_p2.refundable_child_care
        agi = tax_unit("adjusted_gross_income", period)
        childcare_expenses = tax_unit("tax_unit_childcare_expenses", period)

        # check for eligible children
        person = tax_unit.members
        dependent = person("is_tax_unit_dependent", period)
        age = person("age", period)
        child = age < p.child_age_limit
        eligible = dependent & child
        eligible_children = tax_unit.sum(eligible)

        max_expense = p.expense_limit.calc(eligible_children)
        expense = min_(childcare_expenses, max_expense)

        # line 6 of worksheet
        tax_unit_min_income = tax_unit("min_head_spouse_earned", period)
        credit = min_(expense, tax_unit_min_income)

        income_mult = p.income_mult.calc(agi)
        mult = p.mult

        return credit * income_mult * mult
