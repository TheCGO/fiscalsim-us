from fiscalsim_us.model_api import *


class la_federal_retirement_benefits(Variable):
    """Amount of retirement benefits recieved from a
    Federal Retirement System
    """

    value_type = float
    entity = TaxUnit
    label = "Louisiana state teacher retirement benefits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    # If this gets implimented in a federal level variable
    # delete this one and change in parameter subtractions.sources.yaml
