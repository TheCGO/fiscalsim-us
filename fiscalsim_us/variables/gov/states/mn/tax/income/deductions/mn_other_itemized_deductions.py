from fiscalsim_us.model_api import *


class mn_other_itemized_deductions(Variable):
    """
    Other itemized deductions from for M1SA lines 20 and 24
    * Federal estate tax on income in respect of a decedent
    * Deduction for amortizable bond premium
    * Deduction for repayment of amounts under a claim of right
    * Certain unrecovered investment in pension
    * Impairment-related work expenses of a person with a disability
    * Deduction allowable in connection with personal property used
    in a short sale as described under section 67(b)(8)
    """

    value_type = float
    entity = TaxUnit
    label = "MN other itemized deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
