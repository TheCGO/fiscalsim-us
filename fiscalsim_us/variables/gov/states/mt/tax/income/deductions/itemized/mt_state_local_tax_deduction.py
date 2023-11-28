from fiscalsim_us.model_api import *


class mt_state_local_tax_deduction(Variable):
    """
    Line 5 on itemized deductions schedule
    Includes the following
    *General state and local sales taxes
    *Local income taxes
    *Real estate taxes paid
    *Value-based personal property taxes
    Add each of those together but not more than $10,000 if you are single,
        head of household, or married filing jointly; or $5,000 if you
        are married filing separately
    """

    value_type = float
    entity = TaxUnit
    label = "Montana state and local taxes in prior year"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        salt_amount = add(
            tax_unit,
            period,
            [
                "statelocal_sales_or_prior_inctax",
                "real_estate_taxes",
            ],
        )
        salt = parameters(
            period
        ).gov.state.mt.tax.income.deductions.itemized.misc
        cap = salt.salt_cap[tax_unit("filing_status", period)]
        return min(cap, salt_amount)
