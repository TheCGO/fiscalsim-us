from fiscalsim_us.model_api import *


class ga_other_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia other additions to incone"
    unit = USD
    definition_period = YEAR
    reference = "https://houpl.org/wp-content/uploads/2023/01/2022-IT-511_Individual_Income_Tax_-Booklet-compressed.pdf#page=34"
    defined_for = StateCode.GA

    # For line 5 of Georgia tax form 500 Schedule 1
    # Also a catch-all for any non-implemented additions
    # Such as interest on non-Georgia municipal or state bonds
