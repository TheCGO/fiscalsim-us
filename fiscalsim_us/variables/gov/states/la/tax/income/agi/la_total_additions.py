from fiscalsim_us.model_api import *


class la_total_additions(Variable):
    """
    Additions to Louisiana adjusted income
    Lines 2A-D on Form IT-540 Schedule E. These additions include
    * Interest and dividend income from other states and their political subdivisions
    * Recapture of START contributions
    * Recapture of START K12 contributions
    * Add back of pass-through entity
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana total additions to AGI"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
