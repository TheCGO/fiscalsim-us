from fiscalsim_us.model_api import *


class mn_additions_to_income(Variable):
    """
    Line 2 of Minnesota 2022 Individual Income Tax return form M1. These
    additions to income include the following categories and are listed at
    https://www.revenue.state.mn.us/sites/default/files/2023-01/m1m_22.pdf
    and on the Minnesota 2022 M1M form.
    * Interest from municipal bond of another state
    * Federally exempt interest from mutual funds investing in state bonds
    * Lump sum distribution
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
