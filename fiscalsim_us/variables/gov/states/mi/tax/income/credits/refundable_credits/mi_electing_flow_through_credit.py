from fiscalsim_us.model_api import *


class mi_electing_flow_through_credit(Variable):
    """
    Line 29 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MI allocated share of tax paid by an electing flow-through entity credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI
