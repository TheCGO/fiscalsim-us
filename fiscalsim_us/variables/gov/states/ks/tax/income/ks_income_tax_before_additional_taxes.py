from fiscalsim_us.model_api import *


class ks_income_tax_before_additional_taxes(Variable):
    """
    Line 8 on Kansas 2022 Individual Income Tax return form K-40.

    """

    value_type = float
    entity = TaxUnit
    label = "Kansas Income Tax Before Credits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.KS

    def formula(tax_unit, period, parameters):
        taxable_income = tax_unit("ks_taxable_income", period)
        filing_status = tax_unit("filing_status", period)
        status = filing_status.possible_values

        rates = parameters(period).gov.states.ks.tax.income.rates
        joint = rates.joint
        non_joint = rates.non_joint

        return select(
            [
                filing_status == status.SINGLE,
                filing_status == status.JOINT,
                filing_status == status.HEAD_OF_HOUSEHOLD,
                filing_status == status.WIDOW,
                filing_status == status.SEPARATE,
            ],
            [
                non_joint.calc(taxable_income),
                joint.calc(taxable_income),
                non_joint.calc(taxable_income),
                non_joint.calc(taxable_income),
                non_joint.calc(taxable_income),
            ],
        )
