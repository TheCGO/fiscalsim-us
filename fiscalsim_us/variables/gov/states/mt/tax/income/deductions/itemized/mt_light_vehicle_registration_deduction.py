from fiscalsim_us.model_api import *


class mt_light_vehicle_registration_deduction(Variable):
    """
    Line 6 on itemized deductions schedule
    """

    value_type = float
    entity = TaxUnit
    label = "Montana light vehicle registration fees"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
