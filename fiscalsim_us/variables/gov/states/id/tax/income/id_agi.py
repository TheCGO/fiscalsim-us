from fiscalsim_us.model_api import *


class id_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Idaho AGI"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_12-30-2022.pdf"
    )
    defined_for = StateCode.ID
    adds = ["adjusted_gross_income", "id_agi_additions"]
    subtracts = ["id_agi_subtractions"]