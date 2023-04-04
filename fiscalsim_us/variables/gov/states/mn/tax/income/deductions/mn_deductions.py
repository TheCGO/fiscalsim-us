from fiscalsim_us.model_api import *


class mn_deductions(Variable):
    """
    Line 4 of Minnesota 2022 Individual Income Tax return from M1.
    """
    value_type = float
    entity = TaxUnit
    label = "MN deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):

        standard = tax_unit("mn_standard_deduction", period)
        itemized = tax_unit("mn_itemized_deductions", period)

        return max_(standard, itemized)
