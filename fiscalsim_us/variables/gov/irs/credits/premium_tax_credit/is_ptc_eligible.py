import numpy as np
from fiscalsim_us.model_api import *


class is_ptc_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "Premium Tax Credit eligible"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        eligibility = parameters(
            period
        ).gov.irs.credits.premium_tax_credit.eligibility
        income_level = tax_unit("tax_unit_medicaid_income_level", period)
        on_marketplace = (
            add(tax_unit, period, ["has_marketplace_health_coverage"]) > 0
        )
        income_eligible = eligibility.calc(income_level)

        on_marketplace = np.array(on_marketplace, dtype=bool)
        income_eligible = np.array(income_eligible, dtype=bool)

        return on_marketplace & income_eligible
