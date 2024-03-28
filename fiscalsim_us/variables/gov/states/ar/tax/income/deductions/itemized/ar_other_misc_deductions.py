from fiscalsim_us.model_api import *


class ar_other_misc_deductions(Variable):
    """
    Line 29 of 2022 AR3, Arkansas Itemized Deductions

    Deductions include:
    Volunteer firefighter expenses
    Gambling Losses
    Other miscellaneous deductions
    """

    value_type = float
    entity = TaxUnit
    label = "AR other miscellaneous deductions"
    unit = USD
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR3_ItemizedDeduction.pdf"
    definition_period = YEAR
    defined_for = StateCode.AR
