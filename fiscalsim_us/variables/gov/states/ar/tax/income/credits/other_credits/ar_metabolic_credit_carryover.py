from fiscalsim_us.model_api import *


class ar_metabolic_credit_carryover(Variable):
    """
    Line 2 on AR1113 PHENYLKETONURIA DISORDER AND OTHER METABOLIC DISORDERS CREDIT
    """

    value_type = float
    entity = TaxUnit
    label = "Arkansas metabolic credit carryover from previous year"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.AR
