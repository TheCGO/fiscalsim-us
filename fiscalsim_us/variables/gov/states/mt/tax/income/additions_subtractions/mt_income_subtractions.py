from fiscalsim_us.model_api import *


class mt_subtractions_to_income(Variable):
    """
    Line 13 on Montana 2022 Individual Income Tax return form 2. These
    subtractions to income include the categories that are listed
    in Montana Subtractions Schedule on page 5 of Montana 2022 Individual Income Tax return form 2
    """

    value_type = float
    entity = TaxUnit
    label = "MT subtractions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
