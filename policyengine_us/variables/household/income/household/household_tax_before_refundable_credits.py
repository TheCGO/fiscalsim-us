from policyengine_us.model_api import *


class household_tax_before_refundable_credits(Variable):
    value_type = float
    entity = Household
    label = "tax"
    documentation = "Total tax liability before refundable credits."
    unit = USD
    definition_period = YEAR
    adds = [
        "employee_payroll_tax",
        "self_employment_tax",
        "income_tax_before_refundable_credits",  # Federal.
        "ma_income_tax_before_refundable_credits",
        "md_income_tax_before_refundable_credits",
        "ny_income_tax_before_refundable_credits",
        "or_income_tax_before_refundable_credits",
        "pa_income_tax",  # PA has no refundable credits.
        "wa_income_tax_before_refundable_credits",
        "flat_tax",
    ]

    def formula(household, period, parameters):
        added_components = household_tax_before_refundable_credits.adds
        params = parameters(period)
        flat_tax = params.gov.contrib.ubi_center.flat_tax
        if flat_tax.abolish_payroll_tax:
            added_components = [
                c for c in added_components if c != "employee_payroll_tax"
            ]
        if flat_tax.abolish_federal_income_tax:
            added_components = [
                c
                for c in added_components
                if c != "income_tax_before_refundable_credits"
            ]
        if params.simulation.reported_state_income_tax:
            added_components = [
                "employee_payroll_tax",
                "self_employment_tax",
                "income_tax_before_refundable_credits",  # Federal.
                "flat_tax",
                "spm_unit_state_tax_reported",
            ]
        return add(household, period, added_components)
