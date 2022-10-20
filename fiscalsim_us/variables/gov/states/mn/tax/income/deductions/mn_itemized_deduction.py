from fiscalsim_us.model_api import *


class mn_itemized_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN itemized deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        medical_deduct = tax_unit("mn_medical_dental_deduction", period)
        real_estate_tax = add(tax_unit, period, ["real_estate_taxes"])


        # more stuff here...
        return None
