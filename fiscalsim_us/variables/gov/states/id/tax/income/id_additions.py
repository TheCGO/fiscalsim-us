from fiscalsim_us.model_api import *


class id_additions(Variable):
    """
    Section A on Idaho 2022 Form 39R. These additions to income include:

    * Federal net operating loss deduction
    * Capital loss carryover incurred outside the state before becoming an Idaho resident
    * Non-Idaho state and local bond interest and dividends
    * Idaho college savings account withdrawal
    * Bonus Depreciation
    """
    
    value_type = float
    entity = TaxUnit
    label = "Idaho additions"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_12-30-2022.pdf"
    )
    defined_for = StateCode.ID
