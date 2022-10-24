from policyengine_us.model_api import *


class state_income_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "State income tax"
    unit = USD
    definition_period = YEAR

    formula_2021 = sum_of_variables(
        [
            "ma_income_tax",
            "wa_income_tax",
            "md_income_tax",
            "ny_income_tax",
            "pa_income_tax",
            "or_income_tax_after_refundable_credits",
        ]
    )
