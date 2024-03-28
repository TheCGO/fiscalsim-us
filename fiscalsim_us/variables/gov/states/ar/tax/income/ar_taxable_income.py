from fiscalsim_us.model_api import *


class ar_taxable_income(Variable):
    "Line 28 of Form AR1000F"
    value_type = float
    entity = TaxUnit
    label = "Arkansas taxable income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/TaxBrackets_2022.pdf"
        "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2023_Final_AR1000ES.pdf"
    )
    defined_for = StateCode.AR

    def formula(tax_unit, period, parameters):
        agi = tax_unit("ar_agi", period)
        std_ded = tax_unit("ar_standard_deduction", period)
        itm_ded = tax_unit("ar_itemized_deductions", period)
        deduction = where(itm_ded > std_ded, itm_ded, std_ded)

        return agi - deduction
