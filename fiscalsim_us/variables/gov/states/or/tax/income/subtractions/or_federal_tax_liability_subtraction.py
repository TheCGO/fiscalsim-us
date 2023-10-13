from fiscalsim_us.model_api import *


class or_federal_tax_liability_subtraction(Variable):
    value_type = float
    entity = TaxUnit
    label = "OR federal tax liability subtraction"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://www.oregon.gov/dor/forms/FormsPubs/publication-or-17_101-431_2021.pdf#page=71",
        "https://www.oregonlegislature.gov/bills_laws/ors/ors316.html",  # Subsection 316.800
    )
    defined_for = StateCode.OR

    def formula(tax_unit, period, parameters):
        # calculate Oregon concept of federal income tax
        federal_income_tax = tax_unit("income_tax", period)
        eitc = tax_unit("earned_income_tax_credit", period)
        seca = add(tax_unit, period, ["self_employment_tax"])
        or_federal_income_tax = max_(0, federal_income_tax - seca + eitc)
        # limit subtraction based on caps scaled to federal AGI
        filing_status = tax_unit("filing_status", period)
        status = filing_status.possible_values
        caps = (
            parameters(period)
            .gov.states["or"]
            .tax.income.subtractions.federal_tax_liability.cap
        )
        federal_agi = tax_unit("adjusted_gross_income", period)
        cap = select(
            [
                filing_status == status.SINGLE,
                filing_status == status.JOINT,
                filing_status == status.HEAD_OF_HOUSEHOLD,
                filing_status == status.SEPARATE,
                filing_status == status.WIDOW,
            ],
            [
                caps.single.calc(federal_agi),
                caps.joint.calc(federal_agi),
                caps.head_of_household.calc(federal_agi),
                caps.separate.calc(federal_agi),
                caps.widow.calc(federal_agi),
            ],
        )
        return min_(or_federal_income_tax, cap)
