from fiscalsim_us.model_api import *


class az_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ standard deduction"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        standard_deduction = parameters(
            period
        ).gov.states.az.tax.income.deductions
        filing_status = tax_unit("filing_status", period)
        charitable_deduction_increase = tax_unit(
            "az_sd_increase_charitable_contributions", period
        )
        return (
            standard_deduction.standard[filing_status]
            + charitable_deduction_increase
        )
