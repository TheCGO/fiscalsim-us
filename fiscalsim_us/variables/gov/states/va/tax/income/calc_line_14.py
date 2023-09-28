from fiscalsim_us.model_api import *


class calc_line_14(Variable):
    value_type = float
    entity = TaxUnit
    label = "VA interim step to get to total virginia taxable income, line 14 on form 760 https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/760-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        # line_11  = tax_unit("va_standard_deduction",period)

        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values

        # for single, head of household, widow filing status
        if (
            filing_status == filing_statuses.SINGLE
            or filing_status == filing_statuses.WIDOW
            or filing_status == filing_statuses.HEAD_OF_HOUSEHOLD
        ):
            va_standard_deduction = parameters(
                period
            ).gov.states.va.tax.income.va_standard_deduction.SINGLE

        if filing_status == filing_statuses.JOINT:
            va_standard_deduction = parameters(
                period
            ).gov.states.va.tax.income.va_standard_deduction.JOINT

        if filing_status == filing_statuses.SEPARATE:
            va_standard_deduction = parameters(
                period
            ).gov.states.va.tax.income.va_standard_deduction.SEPARATE

        line_12 = tax_unit("va_exemptions", period)

        subtotal = va_standard_deduction + line_12

        return subtotal
