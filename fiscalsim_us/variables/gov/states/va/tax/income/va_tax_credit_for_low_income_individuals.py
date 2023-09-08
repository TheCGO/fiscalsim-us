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

        fed_eitc = tax_unit("earned_income_tax_credit", period)

        net_tax = tax_unit("va_income_tax_before_refundable_credits", period)

        if filing_status == 1:
            spouse_if_filing_jointly = 0

        elif filing_status == 2:
            spouse_if_filing_jointly = 1

        else:
            spouse_if_filing_jointly = 0

        spouse_agi = tax_unit("spouse_separate_adjusted_gross_income", period)

        dependents = tax_unit("tax_unit_dependents", period)

        total_num_exemptions = spouse_if_filing_jointly + dependents + 1

        total_agi = agi + spouse_agi

        eitc_rate = parameters(period).gov.states.va.tax.income.va_eitc_rate

        # logic to determine if the person qualifies for the EITC

        threshold = parameters(
            period
        ).gov.states.va.tax.income.va_eitc_threshold.calc(total_num_exemptions)

        # threshold = 12880 + (4540*(total_num_exemptions-1))

        if total_agi < threshold:
            line_13 = total_num_exemptions * 300

            # if fed_eitc > 0 :

            # line_13 = 0

            line_14 = fed_eitc

            line_15 = line_14 * eitc_rate

            if line_15 > line_13:
                line_16 = line_15
            else:
                line_16 = line_13

            if net_tax > line_16:
                line_17 = line_16

            else:
                line_17 = net_tax

            return line_17

        else:
            line_17 = 0

            return line_17
