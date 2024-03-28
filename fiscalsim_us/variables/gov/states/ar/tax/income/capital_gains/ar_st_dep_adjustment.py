from fiscalsim_us.model_api import *


class ar_st_dep_adjustment(Variable):
    value_type = float
    entity = Person
    label = "Arkansas difference in short term capital gains depreciation from federal amount"
    unit = USD
    definition_period = YEAR
    reference = "https://www.dfa.arkansas.gov/images/uploads/incomeTaxOffice/2022_AR1000D_CapitalGains.pdf"
    defined_for = StateCode.AR
