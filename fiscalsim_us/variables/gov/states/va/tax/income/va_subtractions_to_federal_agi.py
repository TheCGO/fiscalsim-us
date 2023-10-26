from fiscalsim_us.model_api import *


class va_subtractions_to_federal_agi(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA subtractions to federal agi https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/schedule-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        income_from_obligations_state_exempt = tax_unit(
            "va_income_from_obligations_state_exempt", period
        )

        fixed_date_conformity_subtractions = tax_unit(
            "va_fixed_date_conformity_subtractions", period
        )

        disability_income_reported_as_wages = tax_unit(
            "va_disability_income_reported_as_wages", period
        )

        subtractions_to_fed_agi = (
            income_from_obligations_state_exempt
            + fixed_date_conformity_subtractions
            + disability_income_reported_as_wages
        )

        return subtractions_to_fed_agi
