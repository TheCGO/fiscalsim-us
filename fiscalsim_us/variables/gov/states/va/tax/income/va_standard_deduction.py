from fiscalsim_us.model_api import *


class va_standard_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA interim step to get to virginia taxable income, line 11 on form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/schedule-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values

        standard_deduction = where(
            (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE)
            | (filing_status == filing_statuses.SEPARATE),
            parameters.gov.states.va.tax.income.va_standard_deduction.SINGLE,
            where(
                filing_status == filing_statuses.JOINT,
                parameters.gov.states.va.tax.income.va_standard_deduction.JOINT,
                parameters.gov.states.va.tax.income.va_standard_deduction.SINGLE,
            ),
        )

        return standard_deduction
