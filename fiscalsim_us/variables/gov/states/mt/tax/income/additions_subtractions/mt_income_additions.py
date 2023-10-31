from fiscalsim_us.model_api import *


class mt_additions_to_income(Variable):
    """
    Line 12 on Montana 2022 Individual Income Tax return form 2. These
    additions to income include the categories that are listed
    in Montana Additions Schedule on page 4 of Montana 2022 Individual Income Tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "MT additions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
