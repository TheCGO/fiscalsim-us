from fiscalsim_us.model_api import *


class az_sd_increase_charitable_contributions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ standard deduction increase from charitable contributions"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        cash_donations = add(tax_unit, period, ["charitable_cash_donations"])
        non_cash_donations = add(
            tax_unit, period, ["charitable_non_cash_donations"]
        )
        prior_year_carryover = tax_unit("az_prior_year_carryover", period)
        contribution_credits = tax_unit("az_contribution_credits", period)
        limit_percentage = parameters(
            period
        ).gov.states.az.tax.income.deductions.charitable_deduction_limit
        additions = cash_donations + non_cash_donations + prior_year_carryover

        return (additions - contribution_credits) * limit_percentage
