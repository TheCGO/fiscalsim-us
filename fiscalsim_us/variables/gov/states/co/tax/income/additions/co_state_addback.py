from fiscalsim_us.model_api import *


class co_state_addback(Variable):
    value_type = float
    entity = TaxUnit
    label = "Colorado state income tax addback"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.colorado.gov/sites/tax/files/documents/DR_104_Book_2021.pdf#page=5"
        "https://tax.colorado.gov/sites/tax/files/documents/DR_104_Book_2022.pdf#page=5"
    )
    defined_for = StateCode.CO

    def formula(tax_unit, period, parameters):
        federal_itemizer = tax_unit("tax_unit_itemizes", period)
        # Colorado only requires taxpayers to add back state income tax from
        # Federal Schedule A (line 5a). It does not require taxpayers to
        # add back state real estate or property tax from Schedule A
        state_inctax = max_(0, tax_unit("statelocal_sales_or_prior_inctax", period))
        return federal_itemizer * state_inctax
