from fiscalsim_us.model_api import *


# TODO: apparently test is required for this, even though this is directly linked to il_personal_exemption_eligibility_status?
class il_personal_exemption(Variable):
    value_type = float
    entity = TaxUnit
    label = "IL personal exemption amount"
    unit = USD
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        il_is_personal_exemption_eligible = tax_unit(
            "il_personal_exemption_eligibility_status", period
        )

        eligibility_status = il_is_personal_exemption_eligible.possible_values

        personal_exemption_amount = parameters(
            period
        ).gov.states.il.tax.income.exemption.personal

        return personal_exemption_amount * select(
            [
                il_is_personal_exemption_eligible
                == eligibility_status.BOTH_ELIGIBLE,
                il_is_personal_exemption_eligible
                == eligibility_status.PARTIALLY_ELIGIBLE,
            ],
            [2, 1],
            0,
        )
