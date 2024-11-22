from fiscalsim_us.model_api import *


class ar_other_taxes(Variable):
    """
    Line 6 of 2022 AR3, Arkansas Itemized Deductions
    """

    value_type = float
    entity = TaxUnit
    label = "AR personal property and other taxes"
    unit = USD
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR3_ItemizedDeduction.pdf"
    definition_period = YEAR
    defined_for = StateCode.AR
