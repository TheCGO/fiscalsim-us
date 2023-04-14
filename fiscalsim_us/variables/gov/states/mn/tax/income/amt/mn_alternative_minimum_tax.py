from pandas._libs.tslibs.period import period_ordinal
from fiscalsim_us.model_api import *


class mn_alternative_minimum_tax(Variable):
    """
    TODO: SOMETHING HERE
    """

    value_type = float
    entity = TaxUnit
    label = "MN alternative minimum tax"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.amt
        fed_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)

        # additions
        form6251 = tax_unit("mn_adjustmnets_fed6251", period)
        bond_interest = tax_unit("non_mn_bond_interest", period)
        depletion = tax_unit("mn_depletion", period)
        intangible = tax_unit("mn_intangible_drilling_costs", period)
        # currently not included:
        # line 4 - other addition from M1MB and M1NC

        line8 = fed_agi + form6251 + bond_interest + depletion + intangible

        # subtractions
        medical = tax_unit("mn_medical_dental_deduction", period)
        investment = add(tax_unit, period, ["interest_expense"])
        charity = tax_unit("mn_charitable_donation_deduction", period)
        theft = tax_unit("mn_casualty_theft_deduction", period)
        unreimbursed = tax_unit("mn_unreimbursed_employee_deduction", period)
        impaired_deduct = tax_unit("mn_disabled_impairment_work_deduction", period)
        # currently not included:
        # line 15 - State income tax refund
        # line 16 - line federal bonus deprecitaion subtraction
        # line 17 - Mutual fund dividends of US bond
        # line 18 - other subtractions

        # line 20
        amt_income_before_std = (
            line8 - medical - investment - charity - theft - unreimbursed - impaired_deduct
        )
        std_deduct_phase_out = p.std_deduct_phase_out[filing_status]
        std_deduct = p.standard_deduct[filing_status]

        # line 23
        income_over_phase_out = max_(0, amt_income_before_std - std_deduct_phase_out)
        # line 25
        phased_std_deduct = max_(0, std_deduct - income_over_phase_out * p.mult)
        amt_income = amt_income_before_std - phased_std_deduct

        normal_rates = parameters(period).gov.states.mn.tax.income.rates
        taxable_income = tax_unit("mn_taxable_income", period)

        filing_statuses = filing_status.possible_values
        tax = select(
            [
                filing_status == filing_statuses.SINGLE,
                filing_status == filing_statuses.SEPARATE,
                filing_status == filing_statuses.JOINT,
                filing_status == filing_statuses.HEAD_OF_HOUSEHOLD,
                filing_status == filing_statuses.WIDOW,
            ],
            [
                normal_rates.single.calc(taxable_income),
                normal_rates.separate.calc(taxable_income),
                normal_rates.joint.calc(taxable_income),
                normal_rates.head.calc(taxable_income),
                normal_rates.widow.calc(taxable_income),
            ],
        )

        amt = max_(0, amt_income * p.rate)

        return max_(0, amt - tax)
