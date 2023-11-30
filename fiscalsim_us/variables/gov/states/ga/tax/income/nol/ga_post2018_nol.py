from fiscalsim_us.model_api import *


class ga_post2018_nol(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia Net Operating Loss (carryover) from years after 2018"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.georgia.gov/it-511-individual-income-tax-booklet"
        # above reference provides access to booklets for all years
        # definition of Georgia taxable income starts on page 12
    )
    defined_for = StateCode.GA
