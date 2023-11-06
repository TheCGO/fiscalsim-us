from fiscalsim_us.model_api import *


class az_dependent_credit(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ dependent tax credit"
    unit = USD
    documentation = (
        "AZ nonrefundable credits added on lines 49,50, and 51 of form 140"
    )
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        person = tax_unit.members
        dependent = person("is_tax_unit_dependent", period)
        under_17_count = person("age", period) < 17
        over_17_count = person("age", period) >= 17
        dependents_under_17 = tax_unit.sum(under_17_count & dependent)
        dependents_17_and_over = tax_unit.sum(over_17_count & dependent)
        filing_status = tax_unit("filing_status", period)
        agi = tax_unit("adjusted_gross_income", period)
        p = parameters(period).gov.states.az.tax.income.credits
        joint_difference = agi - p.joint_limitation
        other_difference = agi - p.other_limitation
        # Table one of credit work sheet
        line_1 = dependents_under_17 * 100
        line_2 = dependents_17_and_over * 25

        credit_before_adjustment = line_1 + line_2

        credit_after_adjustment = where(
            filing_status == filing_status.possible_values.JOINT,
            p.adjustment_table.calc(joint_difference) * credit_before_adjustment,
            p.adjustment_table.calc(other_difference) * credit_before_adjustment,
        )

        return credit_after_adjustment