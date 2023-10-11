from fiscalsim_us.model_api import *


class prior_year_salt_paid(Variable):
    value_type = float
    entity = TaxUnit
    label = "Prior year SALT liability paid"
    unit = USD
    documentation = "State and local taxes plus real estate tax deduction from taxable income."
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/164"

