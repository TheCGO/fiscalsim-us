from fiscalsim_us.model_api import *


class mt_income_tax_before_refundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "Montana income tax before refundable credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.MT

    def formula(tax_unit, period, parameters):
        income = tax_unit("mt_taxable_income", period)
        p = parameters(period).gov.states.mt.tax.income.main
        filing_status = tax_unit("filing_status", period)
        status = filing_status.possible_values
        return select(
            [
                filing_status == status.SINGLE,
                filing_status == status.JOINT,
                filing_status == status.HEAD_OF_HOUSEHOLD,
                filing_status == status.SEPARATE,
            ],
            [
                p.single.calc(income),
                p.joint.calc(income),
                p.head_of_household.calc(income),
                p.separate.calc(income),
            ],
        )
