from fiscalsim_us.model_api import *


class az_income_tax_before_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Arizona income tax before credits"
    unit = USD
    definition_period = YEAR
    reference = "https://azdor.gov/forms/individual/resident-personal-income-tax-return-non-calculating-fillable"
    defined_for = StateCode.AZ

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        taxable_income = tax_unit("az_taxable_income", period)
        p = parameters(period).gov.states.az.tax.income.main
        tax = where(
            filing_status == filing_status.possible_values.SINGLE
            or filing_status == filing_status.possible_values.SEPARATE,
            p.single_seperate.calc(taxable_income),
            p.joint_hoh.calc(taxable_income),
        )
        return tax
