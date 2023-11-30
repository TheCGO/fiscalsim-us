from fiscalsim_us.model_api import *


class ga_deductions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia deductions"
    unit = USD
    reference = (
        "https://dor.georgia.gov/it-511-individual-income-tax-booklet"
    )
    definition_period = YEAR
    defined_for = StateCode.GA

    def formula(tax_unit, period, parameters):
        # In GA if the tax unit itemizes their federal returns, then
        # they must itemize for their GA return.
        # Same for standard deduction
        ga_std_deduction = tax_unit("ga_standard_deduction", period)
        ga_itemized = tax_unit("ga_itemized_deductions", period)
        itemizes = tax_unit("tax_unit_itemizes", period)

        return where(itemizes, ga_itemized, ga_std_deduction)
