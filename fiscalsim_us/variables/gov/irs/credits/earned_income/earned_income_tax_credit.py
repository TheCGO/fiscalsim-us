from fiscalsim_us.model_api import *


class earned_income_tax_credit(Variable):
    value_type = float
    entity = TaxUnit
    definition_period = YEAR
    label = "EITC"
    reference = "https://www.law.cornell.edu/uscode/text/26/32#a"
    unit = USD
    defined_for = "eitc_eligible"

    def formula(tax_unit, period, parameters):
        maximum = tax_unit("eitc_maximum", period)
        phased_in = tax_unit("eitc_phased_in", period)
        reduction = tax_unit("eitc_reduction", period)
        limitation = max_(0, maximum - reduction)
        return min_(phased_in, limitation)


c59660 = variable_alias("c59660", earned_income_tax_credit)
eitc = variable_alias("eitc", earned_income_tax_credit)
