from fiscalsim_us.model_api import *


class oh_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH additions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2021/pit-it1040-booklet.pdf" #page 14
