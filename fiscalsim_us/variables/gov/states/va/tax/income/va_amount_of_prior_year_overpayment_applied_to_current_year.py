from fiscalsim_us.model_api import *


class va_amount_of_prior_year_overpayment_applied_to_current_year(Variable):
    value_type = float
    entity = TaxUnit
    label = "va tax witheld from the tax year line 21 on form 760 https://www.tax.virginia.gov/sites/default/files/vatax-pdf/2021-760-instructions.pdf for information"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA
