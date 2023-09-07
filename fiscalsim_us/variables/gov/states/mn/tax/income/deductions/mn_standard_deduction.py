from fiscalsim_us.model_api import *


class mn_standard_deduction(Variable):
    """
    Line 4 of Minnesota 2022 Individual Income Tax return from M1.
    """

    value_type = float
    entity = TaxUnit
    label = "MN standard deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.deductions.standard

        fed_agi = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)
        aged_blind_count = tax_unit("aged_blind_count", period)

        std_deduct = (
            p.base[filing_status] + p.extra[filing_status] * aged_blind_count
        )

        over_threshold = fed_agi >= p.threshold[filing_status]

        phaseout_subtract = min_(
            (fed_agi - p.threshold[filing_status]) * p.income_mult,
            std_deduct * p.mult,
        )
        return std_deduct - over_threshold * phaseout_subtract
