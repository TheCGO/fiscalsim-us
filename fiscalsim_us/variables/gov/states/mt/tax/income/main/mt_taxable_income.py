from fiscalsim_us.model_api import *


class mt_taxable_income(Variable):
    """
    Line 17 on Montana state individual tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "Montana taxable income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT


def formula(tax_unit, period, parameters):
    std_ded = tax_unit("mt_standard_deduction", period)
    itm_ded = tax_unit("mt_itemized_deductions", period)
    deductions = where(itm_ded > std_ded, itm_ded, std_ded)
    exemptions = tax_unit("mt_exemptions", period)
    return max(
        0,
        tax_unit("mt_agi", period) - deductions - exemptions,
    )
