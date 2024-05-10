from fiscalsim_us.model_api import *
from numpy import round


class mn_amt(Variable):
    """
    Line 11 of Form M1 (2023) and line 29 from form M1MT (2023). This amount is
    reported as the liability above the basic tax liability calculation.
    """

    value_type = float
    entity = TaxUnit
    label = "MN alternative minimum tax (amount above basic tax)"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2023-02/m1mt_21.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1mt_22.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-12/m1mt-23.pdf"
    )
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.amt
        amt_income = tax_unit("mn_amt_taxable_income", period)
        amt = max_(0, amt_income * p.rate)
        basic_tax = tax_unit("mn_basic_tax", period)

        return round(max_(0, amt - basic_tax))
