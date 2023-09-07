from fiscalsim_us.model_api import *


class mn_other_additions(Variable):
    """
    Unimplemented additions to Minnesota taxable income.
    Line 2 of Minnesota 2022 Individual Income Tax return form M1. These
    additions to income include the following categories which aren't calculated with other variables.
    * Interest from municipal bond of another state
    * Federally exempt interest from mutual funds investing in state bonds
    * Expenses deducted on federal form income not taxed by Minnesota
    * Net nonqualified withdrawl from First-Time Homebuyer Savings Acct
    * Distributions from higher ed savings accout used in K-12 tuition
    """

    value_type = float
    entity = TaxUnit
    label = "MN additions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
    # if implemented as separate vars, delete from list and add to sources yaml
