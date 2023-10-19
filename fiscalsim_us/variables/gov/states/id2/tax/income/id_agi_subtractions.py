from fiscalsim_us.model_api import *


class id_agi_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "Idaho AGI subtractions from federal AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.idaho.gov/wp-content/uploads/forms/EFO00088/EFO00088_12-30-2022.pdf"
    )
    defined_for = StateCode.ID


    def formula(tax_unit, period, parameters):
        agi = tax_unit("adjusted_gross_income", period)
        taxable_oasdi = add(tax_unit, period, ["taxable_social_security"])
        p = parameters(period).gov.states.id.tax.income.subtractions
        return 