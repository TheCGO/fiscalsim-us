from fiscalsim_us.model_api import *


class mn_personal_property_tax(Variable):
    """
    State and local personal propery tax (non real estate)
    that for taxes based on value alone
    Line 10 of 2022 M1SA, Minnesota Itemized Deductions
    Line 5c of Federal Schedule A
    """

    value_type = float
    entity = TaxUnit
    label = "MN personal property tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
