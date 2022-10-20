from fiscalsim_us.model_api import *


class mn_taxes_paid_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "MN taxes paid itemized deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        real_estate_tax = add(tax_unit, period, ["real_estate_taxes"])
        property_tax = tax_unit("mn_state_local_property_tax", period)
        
        filing_status = tax_unit("filing_status", period)
        max_deduct = parameters(period).gov.states.mn.tax.income.deductions.mn_state_local_property_tax_max[filing_status]
        return min(max_deduct, real_estate_tax + property_tax)