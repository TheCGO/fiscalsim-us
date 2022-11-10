from fiscalsim_us.model_api import *


class id_agi_additions(Variable):
    value_type = float
    entity = TaxUnit
    label = "ID AGI additions"
    unit = USD
    documentation = "Additions to ID AGI over federal AGI."
    definition_period = YEAR
    dict(
        title="Form 39R Additions to Adjusted Gross Income",
        href="https://tax.idaho.gov/forms/EFO00088_09-23-2021.pdf",
    )

    # No additions modeled in FiscalSim US.
