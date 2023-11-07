from fiscalsim_us.model_api import *


class az_itemized_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ itemized deductions"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        # medical_and_dental
        expense = add(tax_unit, period, ["medical_expense"])
        fed_med_deduction = add(
            tax_unit, period, ["medical_expense_deduction"]
        )
        line_3 = max_(0, expense - fed_med_deduction)
        line_4 = where(
            fed_med_deduction > expense, fed_med_deduction - expense, 0
        )
        # mortgage interest deduction is not modeled (line_5)

        # charitable_contributions
        cash_donations = add(tax_unit, period, ["charitable_cash_donations"])
        non_cash_donations = add(
            tax_unit, period, ["charitable_non_cash_donations"]
        )
        prior_year_carryover = tax_unit("az_prior_year_carryover", period)
        line_6 = cash_donations + non_cash_donations + prior_year_carryover
        line_7 = tax_unit("az_contribution_credits", period)

        # federal itemized deductions
        line_11 = add(tax_unit, period, ["itemized_taxable_income_deductions"])

        deductions = line_3 + line_11
        adjustments = line_4 + line_6 + line_7

        return max_(0, deductions - adjustments)
