from fiscalsim_us.model_api import *


class mn_income_tax_before_credits(Variable):
    """
    TODO: SOMETHING HERE
    """

    value_type = float
    entity = TaxUnit
    label = "MN income tax before credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MN

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.mn.tax.income.rates
        taxable_income = tax_unit("mn_taxable_income", period)

        filing_status = tax_unit("filing_status", period)
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
                p.single.calc(taxable_income),
                p.separate.calc(taxable_income),
                p.joint.calc(taxable_income),
                p.head.calc(taxable_income),
                p.widow.calc(taxable_income),
            ],
        )

        amt = tax_unit("mn_alternative_minimum_tax", period)

        return tax + amt
