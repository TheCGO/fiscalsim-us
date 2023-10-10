from fiscalsim_us.model_api import *


class va_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "line 26 on the va tax return"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        line_19 = tax_unit("va_witholding", period)

        line_19b = tax_unit("va_spouse_witholding", period)

        line_20 = tax_unit("va_estimated_tax_payments_for_tax_year", period)

        line_21 = tax_unit(
            "va_amount_of_prior_year_overpayment_applied_to_current_year",
            period,
        )

        line_22 = tax_unit("va_extension_payments", period)

        line_23 = tax_unit("va_tax_credit_for_low_income_individuals", period)

        line_24 = tax_unit("va_credits_from_enclosed_schedule_cr", period)

        return (
            line_19
            + line_19b
            + line_20
            + line_21
            + line_22
            + line_24
            + line_23
        )
