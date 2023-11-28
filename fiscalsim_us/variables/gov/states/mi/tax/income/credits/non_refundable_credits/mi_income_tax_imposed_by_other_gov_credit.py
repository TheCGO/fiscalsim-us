from fiscalsim_us.model_api import *


class mi_income_tax_imposed_by_other_gov_credit(Variable):
    """
    Line 18b on Michigan 2022 Individual Income Tax return form MI-1040. 
    """

    value_type = float
    entity = TaxUnit
    label = "MI income tax credit imposed by goverment units outside of michigan"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI