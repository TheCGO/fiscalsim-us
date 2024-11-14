from fiscalsim_us.model_api import *


class va_calc_line_14(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA interim step to get to total virginia taxable income, line 14 on form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values

        va_standard_deduction = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD),
            parameters(
                period
            ).gov.states.va.tax.income.va_standard_deduction.SINGLE,
            where(
                filing_status == filing_statuses.JOINT,
                parameters(
                    period
                ).gov.states.va.tax.income.va_standard_deduction.JOINT,
                where(
                    filing_status == filing_statuses.SEPARATE,
                    parameters(
                        period
                    ).gov.states.va.tax.income.va_standard_deduction.SEPARATE,
                    0,  # Default value if none of the conditions are met
                ),
            ),
        )

        line_12 = tax_unit("va_exemptions", period)

        subtotal = va_standard_deduction + line_12

        return subtotal
