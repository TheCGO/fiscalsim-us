from fiscalsim_us.model_api import *


class la_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana taxable income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )
    defined_for = StateCode.LA

    def formula(tax_unit, period, parameters):
        ADDS = ["adjusted_gross_income", "la_total_additions"]
        SUBTRACTS = ["la_total_subtractions", "la_exemptions"]

        la_agi = add(tax_unit, period, ADDS) - add(tax_unit, period, SUBTRACTS)

        # LA allows tax units to subtract from income any portion of federal
        # medical expense deductions that is more than the standard deduction
        filing_status = tax_unit("filing_status", period)
        itemizing = tax_unit("tax_unit_itemizes", period)
        std_deduct = parameters(period).gov.irs.deductions.standard.amount[
            filing_status
        ]
        medical_deduct = tax_unit("medical_expense_deduction", period)

        excess_fed_deduct = max_(0, medical_deduct - std_deduct)

        #        return max_(0, la_agi - excess_fed_deduct)
        return where(itemizing, la_agi - excess_fed_deduct, la_agi)
