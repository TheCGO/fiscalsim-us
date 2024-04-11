from fiscalsim_us.model_api import *


class mi_total_refundable_credits(Variable):
    """
    Line 33 on Michigan individual income tax form MI-1040
    """

    value_type = float
    entity = TaxUnit
    label = "MT total refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI

    adds = [
        "mi_property_tax_credit",
        "mi_farmland_preservation_tax_credit",
        "mi_eitc",
        "mi_historic_preservation_refundable",
        "mi_electing_flow_through_credit",
        "mi_withheld",
        "mi_estimated_tax",
    ]
