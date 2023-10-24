from fiscalsim_us.model_api import *


class co_state_addback(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado state income tax addback"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.colorado.gov/sites/tax/files/documents/DR_104_Book_2021.pdf#page=5",
        "https://tax.colorado.gov/sites/tax/files/documents/DR_104_Book_2022.pdf#page=5",
        "https://tax.colorado.gov/sites/tax/files/documents/ITT_State_Income_Tax_Addback_Jan_2023.pdf",
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        federal_itemizer = tax_unit("tax_unit_itemizes", period)

        salt_deduct = tax_unit("salt_deduction", period)
        local_taxes = add(
            tax_unit, period, ["prior_year_local_income_tax_paid"]
        )
        property_taxes = add(tax_unit, period, ["real_estate_taxes"])
        state_addback = max_(0, salt_deduct - local_taxes - property_taxes)

        # return the max between the "extra" itemized deductions above the std
        # and the state taxes included in the SALT deduction
        p = parameters(period).gov.irs.deductions
        item_deducts = add(tax_unit, period, p.itemized_deductions)
        std_deducts = tax_unit("standard_deduction", period)
        alt_addback = max_(0, item_deducts - std_deducts)

        return federal_itemizer * min_(state_addback, alt_addback)
