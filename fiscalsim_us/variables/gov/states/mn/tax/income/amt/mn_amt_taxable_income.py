from fiscalsim_us.model_api import *


class mn_amt_taxable_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Minnesota alternative minimum tax (AMT) taxable income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.revenue.state.mn.us/sites/default/files/2023-02/m1mt_21.pdf"
        "https://www.revenue.state.mn.us/sites/default/files/2023-01/m1mt_22.pdf"
    )
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.amt
        fed_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)

        ADDITIONS = [
            "mn_adjustmnets_fed6251",
            "non_mn_bond_interest",
            "mn_depletion",
            "mn_intangible_drilling_costs",
        ]
        # currently not included:
        # line 4 - other addition from M1MB and M1NC

        line8 = fed_agi + add(tax_unit, period, ADDITIONS)

        SUBTRACTIONS = [
            "mn_medical_dental_deduction",
            "interest_deduction",
            "charitable_deduction",
            "mn_casualty_theft_deduction",
            "mn_unreimbursed_employee_deduction",
            "mn_disabled_impairment_work_deduction",
            "us_govt_interest",
        ]
        # currently not included:
        # line 15 - State income tax refund
        # line 16 - line federal bonus deprecitaion subtraction
        # line 18 - other subtractions

        # line 20
        amt_income_before_std = line8 - add(tax_unit, period, SUBTRACTIONS)

        # line 23
        income_over_phase_out = max_(
            0, amt_income_before_std - p.std_deduct_phase_out[filing_status]
        )

        # line 25
        phased_std_deduct = max_(
            0,
            p.standard_deduct[filing_status]
            - (income_over_phase_out * p.mult),
        )

        return amt_income_before_std - phased_std_deduct
