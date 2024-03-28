from fiscalsim_us.model_api import *


class ar_other_limited_expenses(Variable):
    """
    Line 21 of 2022 AR3, Arkansas Itemized Deductions

    Other deductions include:
    Union or professional dues
    Tax return preparation fees
    Expenses for safety equipment
    Expenses of entertaining customers
    Tools and supplies
    Fees paid to employment agencies
    """

    value_type = float
    entity = TaxUnit
    label = "AR other limited expenses"
    unit = USD
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR3_ItemizedDeduction.pdf"
    definition_period = YEAR
    defined_for = StateCode.AR
