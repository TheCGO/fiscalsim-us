from fiscalsim_us.model_api import *


class ks_additional_taxes(Variable):
    """
    Lines 10 & 11 on Kansas 2022 Individual Income Tax return form K-40.
    * line 10: Nonresident tax
    * line 11: Kansas tax on lump sum distributions
    
    """
    value_type = float
    entity = TaxUnit
    label = "KS additional taxes"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
