from fiscalsim_us.model_api import *


class la_nonrefundable_childcare(Variable):
    value_type = float
    entity = TaxUnit
    label = "Louisiana refundable childcare credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.LA
    reference = (
        "https://revenue.louisiana.gov/TaxForms/IT540WEB(2022)%20F%20D2.pdf",
        "https://revenue.louisiana.gov/TaxForms/IT540iWEB(2022)D1.pdf",
    )

    def formula(tax_unit, period, parameters):
        p = parameters(
            period
        ).gov.states.la.tax.income.credits.nonrefundable_p3.nonrefundable_child_care
        agi = tax_unit("adjusted_gross_income", period)
        fed_cdcc = tax_unit("cdcc", period)

        # for agi under income floor can use the refundable credit
        nonrefundable = agi > p.income_floor
        fed_cdcc = fed_cdcc * nonrefundable

        income_mult = p.income_mult.calc(agi)
        credit = fed_cdcc * income_mult

        # for agi over the threshold the credit is the minimum of
        # fed_cdcc * income_mult and the limit for above the threshold
        return where(
            agi > p.income_threshold,
            min_(credit, p.above_threshold_max),
            credit,
        )
