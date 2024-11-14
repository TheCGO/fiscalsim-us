from fiscalsim_us.model_api import *


class va_adj_gross_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Line 9 on form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        line3 = tax_unit("va_calc_line_3", period)
        line8 = tax_unit("va_calc_line_8", period)
        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values

        threshold = parameters(
            period
        ).gov.states.va.tax.income.va_adjusted_gross_income
        single = threshold.SINGLE
        joint = threshold.JOINT

        subtotal = line3 - line8

        tax_owed = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.SEPARATE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE),
            where(subtotal < single, 0, subtotal),
            where(
                filing_status == filing_statuses.JOINT,
                where(subtotal < joint, 0, subtotal),
                subtotal,
            ),
        )

        return tax_owed
