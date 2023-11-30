from fiscalsim_us.model_api import *


class ga_itemized_adjustments(Variable):
    value_type = float
    entity = TaxUnit
    label = "Georgia itemized deductions"
    unit = USD
    reference = (
        "https://apps.dor.ga.gov/FillableForms/PDFViewer/Index?form=2022GA500"
        )
    definition_period = YEAR
    defined_for = StateCode.GA

    # Line 12b on GA Tax form 500
    # Adjustments for income taxes other than Georgia state taxes that
    # are used in calculating federal itemized dedctions
