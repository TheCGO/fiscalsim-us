from fiscalsim_us.model_api import *


class mn_nonrefundable_credits(Variable):
    """
    Line 16 on Minnesota 2022 Indivual Tax Return from M1.
    These cretis include the following categories and are listed on
    form M1C at https://www.revenue.state.mn.us/sites/default/files/2023-01/m1c_22.pdf
    * Marriage credit
    * Credit for long term care insurcance premiums paid
    * Credit for taxes paid to another state
    * Credit for past military service
    * Employer Transit Pass Credit
    * SEED Capital Investment Credit
    * Education Savings Account Contribution Credit
    * Credit for attaining masters degree in teacher licensure field
    * Student Loan Credit
    * Beginning Farmer Management Credit
    * Film Production Credit
    * Tax Credit for Owners of Agricultural Assets
    * Credit for increasing research activities
    * Carryforward of previous year Farmer Management Credits
    * Carryforward of previous year Owners of Agricultural Assets Credits
    * Carryforward of prior year increasing research activities credit
    * Alternative Minimum Tax Credit
    """

    value_type = float
    entity = TaxUnit
    label = "MN nonrefundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN
