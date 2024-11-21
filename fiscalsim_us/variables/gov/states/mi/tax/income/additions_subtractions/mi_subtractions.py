from fiscalsim_us.model_api import *


class mi_subtractions(Variable):
    """
    Line 13 on Michigan 2022 Individual Income Tax return form MI-1040.
    These subtractions to income include the categories that are listed
    in Michigan Line 30 of Schedule 1 found in the instructions
    """

    value_type = float
    entity = TaxUnit
    label = "MI subtractions to income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI
