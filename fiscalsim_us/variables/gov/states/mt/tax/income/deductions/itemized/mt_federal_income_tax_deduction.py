from fiscalsim_us.model_api import *


class mt_federal_income_tax_deduction(Variable):
    """
    Line 4 on itemized deductions schedule
    Includes the following
    *Federal income tax withheld
    *Federal estimated tax payments
    *Prior year federal income taxes
    *Other back year federal income taxes
    Add each of those together but not more then $5,000 if you are single,
        head of household, or married filing sperarately; or $10,000 if you
        are married filing jointly
    """

    value_type = float
    entity = TaxUnit
    label = "Montana federal tax paid/withheld in prior year"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT
