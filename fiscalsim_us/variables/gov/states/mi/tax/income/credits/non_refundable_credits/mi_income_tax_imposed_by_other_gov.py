from fiscalsim_us.model_api import *


class mi_income_tax_imposed_by_other_gov_amount(Variable):
    """
    Line 18a on Michigan 2022 Individual Income Tax return form MI-1040.
    This non-refundable credit includes the amount of income tax paid to:
    - A nonreciprocal state
    - A local government unit outside Michigan, including tax
        paid to local units located in reciprocal states
    - The District of Columbia
    -A Canadian province.
    """

    value_type = float
    entity = TaxUnit
    label = (
        "MI income tax amount imposed by goverment units outside of michigan"
    )
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MI
