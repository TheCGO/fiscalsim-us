from fiscalsim_us.model_api import *


class az_capital_gains_subtractions(Variable):
    value_type = float
    entity = TaxUnit
    label = "AZ capital gains subtractions"
    unit = USD
    documentation = "Additions to AZ AGI over federal AGI."
    reference = "https://azdor.gov/forms/individual/form-140-resident-personal-income-tax-form-non-fillable-form"
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        # # capital_gains_subtractions
        # net_long_term_capital_gain = tax_unit(
        #     "long_term_capital_gain", period
        # )
        # net_short_term_capital_gain = tax_unit(
        #     "net_short_term_capital_gain", period
        # )
        net_capital_gain = tax_unit("net_capital_gain", period)
        cg_additions = 0.25 * (
            net_capital_gain
            # + net_long_term_capital_gain
            # + net_short_term_capital_gain
        )

        # cg_from_small_business = tax_unit(
        #     "long_term_capital_gains_on_small_business_stock", period
        # )

        return cg_additions
