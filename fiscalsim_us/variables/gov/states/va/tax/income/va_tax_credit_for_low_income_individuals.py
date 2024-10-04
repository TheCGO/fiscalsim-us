from fiscalsim_us.model_api import *


class va_tax_credit_for_low_income_individuals(Variable):
    value_type = float
    entity = TaxUnit
    label = "va tax credit for low income indivduals https://www.tax.virginia.gov/sites/default/files/taxforms/individual-income-tax/2021/schedule-adj-2021.pdf"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.VA

    def formula(tax_unit, period, parameters):
        agi = tax_unit("va_adj_gross_income", period)
        filing_status = tax_unit("filing_status", period)
        filing_statuses = filing_status.possible_values
        fed_eitc = tax_unit("earned_income_tax_credit", period)
        net_tax = tax_unit("va_income_tax_before_refundable_credits", period)

        spouse_if_filing_jointly = where(
            (filing_status == filing_statuses.SEPARATE)
            | (filing_status == filing_statuses.SINGLE)
            | (filing_status == filing_statuses.SURVIVING_SPOUSE)
            | (filing_status == filing_statuses.HEAD_OF_HOUSEHOLD),
            0,
            where(filing_status == filing_statuses.JOINT, 1, 0),
        )

        spouse_agi = tax_unit("spouse_separate_adjusted_gross_income", period)
        dependents = tax_unit("tax_unit_dependents", period)
        total_num_exemptions = spouse_if_filing_jointly + dependents + 1
        total_agi = agi + spouse_agi
        eitc_rate = parameters(period).gov.states.va.tax.income.va_eitc_rate
        threshold = parameters(
            period
        ).gov.states.va.tax.income.va_eitc_threshold.calc(total_num_exemptions)

        line_13 = where(total_agi < threshold, total_num_exemptions * 300, 0)
        line_14 = fed_eitc
        line_15 = line_14 * eitc_rate
        line_16 = where(line_15 > line_13, line_15, line_13)
        line_17 = where(net_tax > line_16, line_16, net_tax)

        return where(total_agi < threshold, line_17, 0)
