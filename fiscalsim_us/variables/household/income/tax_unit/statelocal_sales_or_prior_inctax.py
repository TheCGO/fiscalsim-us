from fiscalsim_us.model_api import *


class statelocal_sales_or_prior_inctax(Variable):
    value_type = float
    entity = TaxUnit
    definition_period = YEAR
    label = "Prior year state and local income taxes paid or state and local sales taxes paid"
    unit = USD

    def formula(tax_unit, period, parameters):
        # Only sales or income tax can be itemized, but not both.
        prior_year_statelocal_inctax = add(
            tax_unit,
            period,
            [
                "prior_year_state_income_tax_paid",
                "prior_year_local_income_tax_paid",
            ],
        )
        sales_tax = add(
            tax_unit, period, ["state_sales_tax", "local_sales_tax"]
        )
        return max_(prior_year_statelocal_inctax, sales_tax)
