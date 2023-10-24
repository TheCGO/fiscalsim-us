from fiscalsim_us.model_api import *


class va_additions_to_federal_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA additions to federal agi https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/schedule-adj-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        income_from_obligations_fed_exempt = tax_unit(
            "va_income_from_obligations_fed_exempt", period
        )

        fixed_date_conformity_additions = tax_unit(
            "va_fixed_date_conformity_additions", period
        )

        additions_to_fed_agi = (
            income_from_obligations_fed_exempt
            + fixed_date_conformity_additions
        )

        return additions_to_fed_agi
