from fiscalsim_us.model_api import *


class ca_care_categorically_eligible(Variable):
    value_type = bool
    entity = Household
    definition_period = YEAR
    label = "Eligible for California CARE program"
    documentation = "Eligible for California Alternate Rates for Energy"
    reference = "https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/electric-costs/care-fera-program"
    defined_for = StateCode.CA
    adds = "gov.states.ca.cpuc.care.eligibility.categorical"
