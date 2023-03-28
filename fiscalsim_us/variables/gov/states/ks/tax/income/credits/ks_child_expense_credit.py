from fiscalsim_us.model_api import *


class ks_child_expense_credit(Variable):
    """
    Line 2 on Kansas 2022 Individual Income Tax return form K-40. This is a list of
    modifications to AGI—both additions and subtracions.
    See Schedule S for more information. https://www.ksrevenue.gov/pdf/schs22.pdf

    """

    value_type = float
    entity = TaxUnit
    label = "KS child expense credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
